"""
Generate Python Sub file containing static type information for checking
the CRRs submitted to Rook
Usage:
Run
$ python ./generate.py

"""
from abc import ABC, abstractmethod
from collections import OrderedDict
from os.path import expanduser
from typing import List, Union, Iterator, Optional

import yaml
from attr import dataclass

header = '''"""
This file is automatically generated.
Do not modify.
"""

if False:
    from typing import List, Dict, Any, Optional

# Tricking mypy to think `_omit`'s type is NoneType
# To make us not add things like `Union[Optional[str], OmitType]`
NoneType = type(None)  
_omit = None  # type: NoneType
_omit = object()  # type: ignore

'''

@dataclass
class CRDBase(ABC):
    name: str
    nullable: bool
    required: bool

    @property
    def py_name(self):
        return self.name

    @property
    @abstractmethod
    def py_type(self):
        ...

    def py_property(self):
        return f"""
@property
def {self.py_name}(self):
    # type: () -> {self.py_property_return_type}
    if self._{self.py_name} is _omit:
        raise AttributeError('{self.py_name} not found')
    return self._{self.py_name}

@{self.py_name}.setter
def {self.py_name}(self, new_val):
    # type: ({self.py_param_type}) -> None
    self._{self.py_name} = new_val
    """.strip()

    @property
    def py_param(self):
        if not self.has_default:
            return f'{self.py_name},  # type: {self.py_param_type}'
        return f'{self.py_name}=_omit,  # type: {self.py_param_type}'

    @property
    def has_default(self):
        return not self.required

    @property
    def py_param_type(self):
        return f'Optional[{self.py_type}]' if (self.nullable or not self.required) else self.py_type

    @property
    def py_property_return_type(self):
        return f'Optional[{self.py_type}]' if (self.nullable) else self.py_type

    @property
    def py_init_set(self):
        return f'self.{self.py_name} = {self.py_name}  # type: ignore'

    @property
    def py_from_json_val(self):
        if self.required:
            return f"data['{self.name}']"
        return f"data.get('{self.name}', _omit)"

    @property
    def py_not_in(self):
        ret = []
        if self.nullable:
            ret.append(f"self._{self.py_name} is not None")
        if not self.required:
            ret.append(f"self._{self.py_name} is not _omit")
        assert ret, self.name
        return ' and '.join(ret)

@dataclass
class CRDAttribute(CRDBase):
    type: str
    default_value: str='_omit'

    @property
    def py_param(self):
        if not self.has_default:
            return f'{self.py_name},  # type: {self.py_param_type}'
        return f'{self.py_name}={self.default_value},  # type: {self.py_param_type}'

    @property
    def has_default(self):
        return not self.required or self.default_value != '_omit'

    @property
    def py_type(self):
        return {
            'integer': 'int',
            'boolean': 'bool',
            'string': 'str',
            'object': 'Any',
        }[self.type]

    @property
    def py_to_json_val(self):
        return 'self._' + self.py_name

    def flatten(self):
        yield from ()

    def toplevel(self):
        return ''


@dataclass
class CRDList(CRDBase):
    items: 'CRDClass'

    @property
    def py_name(self):
        return self.name

    @property
    def py_type(self):
        return self.name[0].upper() + self.name[1:] + 'List'

    def flatten(self):
        yield from self.items.flatten()
        yield self

    def toplevel(self):
        return f"""
class {self.py_type}(list):
{indent(self.py_to_json())}

{indent(self.py_from_json())}
""".strip()

    def py_to_json(self):
        return f"""
def to_json(self):
    return [e.to_json() for e in self]
""".strip()

    @property
    def py_to_json_val(self):
        if not self.nullable and self.required:
            return f'self.{self.py_name}.to_json()'
        return f'self.{self.py_name}.to_json() if {self.py_not_in} else self._{self.py_name}'

    def py_from_json(self):
        return f"""
@classmethod
def from_json(cls, data):
    # type: (list) -> {self.py_param_type}
    return cls({self.items.py_type}.from_json(e) for e in data)
""".strip()

    @property
    def py_from_json_val(self):
        if self.required:
            return f"{self.py_type}.from_json(data['{self.name}'])"
        return f"{self.py_type}.from_json(data['{self.name}']) if '{self.name}' in data else _omit"


@dataclass
class CRDClass(CRDBase):
    attrs: List[Union[CRDAttribute, 'CRDClass']]

    def toplevel(self):
        ps = '\n\n'.join(a.py_property() for a in self.attrs)
        return f"""class {self.py_type}(object):
{indent(self.py_init())}

{indent(ps)}

{indent(self.py_to_json())}

{indent(self.py_from_json())}
""".strip()

    @property
    def sub_classes(self) -> List["CRDClass"]:
        return [a for a in self.attrs if isinstance(a, CRDClass)]

    @property
    def py_type(self):
        return self.name[0].upper() + self.name[1:]

    def flatten(self) -> Iterator['CRDClass']:
        for sub_cls in self.attrs:
            yield from sub_cls.flatten()
        yield self

    def py_init(self):
        sorted_attrs = sorted(self.attrs, key=lambda a: a.has_default)
        params = '\n'.join(a.py_param for a in sorted_attrs)
        init_set = '\n'.join(a.py_init_set for a in sorted_attrs)
        return f"""
def __init__(self,
{indent(params, indent=4+9)}
             ):
{indent(init_set)}
""".strip()

    def py_to_json(self):
        elems = '\n'.join(f"'{a.name}': {a.py_to_json_val}," for a in self.attrs)
        return f"""
def to_json(self):
    res = {{
{indent(elems, 8)}
    }}
    return {{k: v for k, v in res.items() if v is not _omit}}
""".strip()

    @property
    def py_to_json_val(self):
        if not self.nullable and self.required:
            return f'self.{self.py_name}.to_json()'
        return f'self.{self.py_name}.to_json() if {self.py_not_in} else self._{self.py_name}'

    def py_from_json(self):
        elems = '\n'.join(f"{a.py_name}={a.py_from_json_val}," for a in self.attrs)
        return f"""
@classmethod
def from_json(cls, data):
    # type: (dict) -> {self.py_param_type}
    return cls(
{indent(elems, 8)}
    )
""".strip()

    @property
    def py_from_json_val(self):
        from_json = f"{self.py_type}.from_json(data['{self.name}'])"
        if self.nullable:
            from_json = f"({from_json} if data['{self.name}'] is not None else None)"
        if self.required:
            return from_json
        return f"{from_json} if '{self.name}' in data else _omit"


def indent(s, indent=4):
    return '\n'.join(' '*indent + l for l in s.splitlines())


def handle_property(elem_name, elem: dict, required: bool):
    nullable = elem.get('nullable', False)
    if 'properties' in elem:
        ps = elem['properties']
        required_elems = elem.get('required', [])
        sub_props = [handle_property(k, v, k in required_elems) for k, v in ps.items()]
        return CRDClass(elem_name, nullable, required, sub_props)
    elif 'items' in elem:
        item = handle_property(elem_name + 'Item', elem['items'], False)
        return CRDList(elem_name, nullable, required, item)
    elif 'type' in elem:
        return CRDAttribute(elem_name, nullable, required, elem['type'])
    elif elem == {}:
        return CRDAttribute(elem_name, nullable, required, 'object')
    assert False, str((elem_name, elem))


def handle_crd(c_dict) -> Optional[CRDClass]:
    try:
        name = c_dict['spec']['names']['kind']
        s = c_dict['spec']['validation']['openAPIV3Schema']
    except (KeyError, TypeError):
        return None
    s['required'] = ['spec']
    c = handle_property(name, s, True)
    k8s_attrs = [CRDAttribute('apiVersion', False, True, 'string'),
                 CRDAttribute('kind', False, True, 'string', f'"{name}"'),
                 CRDAttribute('metadata', False, True, 'object'),
                 CRDAttribute('status', False, False, 'object')]
    return CRDClass(c.name, False, True, k8s_attrs + c.attrs)


def download_yaml():
    import requests

    url = 'https://raw.githubusercontent.com/rook/rook/master/cluster/examples/kubernetes/ceph/common.yaml'
    r = requests.get(url, allow_redirects=True)
    yamls = yaml.safe_load_all(r.content.decode('utf-8'))
    for y in yamls:
        try:
            yield y
        except AttributeError:
            pass

def local():
    with open(expanduser('~/go/src/github.com/rook/rook/cluster/examples/kubernetes/ceph/common.yaml')) as f:
        yamls = yaml.safe_load_all(f.read())
        for y in yamls:
            try:
                yield y
            except AttributeError:
                pass


def remove_duplicates(items):
    return OrderedDict.fromkeys(items).keys()


def main():
    #for crd in download_yaml():
    for crd in local():
        valid_crd = handle_crd(crd)
        if valid_crd is not None:
            with open(f'rook_ceph_client/{valid_crd.name.lower()}.py', 'w') as f:
                f.write(header)
                classes = remove_duplicates(cls.toplevel() for cls in valid_crd.flatten())
                f.write('\n\n\n'.join(classes))
                f.write('\n')

if __name__ == '__main__':
    main()
