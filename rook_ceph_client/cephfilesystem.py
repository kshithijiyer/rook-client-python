"""
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

class MetadataServer(object):
    def __init__(self,
                 activeCount=_omit,  # type: Optional[int]
                 activeStandby=_omit,  # type: Optional[bool]
                 annotations=_omit,  # type: Optional[Any]
                 placement=_omit,  # type: Optional[Any]
                 resources=_omit,  # type: Optional[Any]
                 ):
        self.activeCount = activeCount  # type: ignore
        self.activeStandby = activeStandby  # type: ignore
        self.annotations = annotations  # type: ignore
        self.placement = placement  # type: ignore
        self.resources = resources  # type: ignore

    @property
    def activeCount(self):
        # type: () -> int
        if self._activeCount is _omit:
            raise AttributeError('activeCount not found')
        return self._activeCount
    
    @activeCount.setter
    def activeCount(self, new_val):
        # type: (Optional[int]) -> None
        self._activeCount = new_val
    
    @property
    def activeStandby(self):
        # type: () -> bool
        if self._activeStandby is _omit:
            raise AttributeError('activeStandby not found')
        return self._activeStandby
    
    @activeStandby.setter
    def activeStandby(self, new_val):
        # type: (Optional[bool]) -> None
        self._activeStandby = new_val
    
    @property
    def annotations(self):
        # type: () -> Any
        if self._annotations is _omit:
            raise AttributeError('annotations not found')
        return self._annotations
    
    @annotations.setter
    def annotations(self, new_val):
        # type: (Optional[Any]) -> None
        self._annotations = new_val
    
    @property
    def placement(self):
        # type: () -> Any
        if self._placement is _omit:
            raise AttributeError('placement not found')
        return self._placement
    
    @placement.setter
    def placement(self, new_val):
        # type: (Optional[Any]) -> None
        self._placement = new_val
    
    @property
    def resources(self):
        # type: () -> Any
        if self._resources is _omit:
            raise AttributeError('resources not found')
        return self._resources
    
    @resources.setter
    def resources(self, new_val):
        # type: (Optional[Any]) -> None
        self._resources = new_val

    def to_json(self):
        res = {
            'activeCount': self._activeCount,
            'activeStandby': self._activeStandby,
            'annotations': self._annotations,
            'placement': self._placement,
            'resources': self._resources,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[MetadataServer]
        return cls(
            activeCount=data.get('activeCount', _omit),
            activeStandby=data.get('activeStandby', _omit),
            annotations=data.get('annotations', _omit),
            placement=data.get('placement', _omit),
            resources=data.get('resources', _omit),
        )


class Replicated(object):
    def __init__(self,
                 size=_omit,  # type: Optional[int]
                 ):
        self.size = size  # type: ignore

    @property
    def size(self):
        # type: () -> int
        if self._size is _omit:
            raise AttributeError('size not found')
        return self._size
    
    @size.setter
    def size(self, new_val):
        # type: (Optional[int]) -> None
        self._size = new_val

    def to_json(self):
        res = {
            'size': self._size,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[Replicated]
        return cls(
            size=data.get('size', _omit),
        )


class ErasureCoded(object):
    def __init__(self,
                 dataChunks=_omit,  # type: Optional[int]
                 codingChunks=_omit,  # type: Optional[int]
                 ):
        self.dataChunks = dataChunks  # type: ignore
        self.codingChunks = codingChunks  # type: ignore

    @property
    def dataChunks(self):
        # type: () -> int
        if self._dataChunks is _omit:
            raise AttributeError('dataChunks not found')
        return self._dataChunks
    
    @dataChunks.setter
    def dataChunks(self, new_val):
        # type: (Optional[int]) -> None
        self._dataChunks = new_val
    
    @property
    def codingChunks(self):
        # type: () -> int
        if self._codingChunks is _omit:
            raise AttributeError('codingChunks not found')
        return self._codingChunks
    
    @codingChunks.setter
    def codingChunks(self, new_val):
        # type: (Optional[int]) -> None
        self._codingChunks = new_val

    def to_json(self):
        res = {
            'dataChunks': self._dataChunks,
            'codingChunks': self._codingChunks,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[ErasureCoded]
        return cls(
            dataChunks=data.get('dataChunks', _omit),
            codingChunks=data.get('codingChunks', _omit),
        )


class MetadataPool(object):
    def __init__(self,
                 failureDomain=_omit,  # type: Optional[str]
                 replicated=_omit,  # type: Optional[Replicated]
                 erasureCoded=_omit,  # type: Optional[ErasureCoded]
                 ):
        self.failureDomain = failureDomain  # type: ignore
        self.replicated = replicated  # type: ignore
        self.erasureCoded = erasureCoded  # type: ignore

    @property
    def failureDomain(self):
        # type: () -> str
        if self._failureDomain is _omit:
            raise AttributeError('failureDomain not found')
        return self._failureDomain
    
    @failureDomain.setter
    def failureDomain(self, new_val):
        # type: (Optional[str]) -> None
        self._failureDomain = new_val
    
    @property
    def replicated(self):
        # type: () -> Replicated
        if self._replicated is _omit:
            raise AttributeError('replicated not found')
        return self._replicated
    
    @replicated.setter
    def replicated(self, new_val):
        # type: (Optional[Replicated]) -> None
        self._replicated = new_val
    
    @property
    def erasureCoded(self):
        # type: () -> ErasureCoded
        if self._erasureCoded is _omit:
            raise AttributeError('erasureCoded not found')
        return self._erasureCoded
    
    @erasureCoded.setter
    def erasureCoded(self, new_val):
        # type: (Optional[ErasureCoded]) -> None
        self._erasureCoded = new_val

    def to_json(self):
        res = {
            'failureDomain': self._failureDomain,
            'replicated': self.replicated.to_json() if self._replicated is not _omit else self._replicated,
            'erasureCoded': self.erasureCoded.to_json() if self._erasureCoded is not _omit else self._erasureCoded,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[MetadataPool]
        return cls(
            failureDomain=data.get('failureDomain', _omit),
            replicated=Replicated.from_json(data['replicated']) if 'replicated' in data else _omit,
            erasureCoded=ErasureCoded.from_json(data['erasureCoded']) if 'erasureCoded' in data else _omit,
        )


class DataPoolsItem(object):
    def __init__(self,
                 failureDomain=_omit,  # type: Optional[str]
                 replicated=_omit,  # type: Optional[Replicated]
                 erasureCoded=_omit,  # type: Optional[ErasureCoded]
                 ):
        self.failureDomain = failureDomain  # type: ignore
        self.replicated = replicated  # type: ignore
        self.erasureCoded = erasureCoded  # type: ignore

    @property
    def failureDomain(self):
        # type: () -> str
        if self._failureDomain is _omit:
            raise AttributeError('failureDomain not found')
        return self._failureDomain
    
    @failureDomain.setter
    def failureDomain(self, new_val):
        # type: (Optional[str]) -> None
        self._failureDomain = new_val
    
    @property
    def replicated(self):
        # type: () -> Replicated
        if self._replicated is _omit:
            raise AttributeError('replicated not found')
        return self._replicated
    
    @replicated.setter
    def replicated(self, new_val):
        # type: (Optional[Replicated]) -> None
        self._replicated = new_val
    
    @property
    def erasureCoded(self):
        # type: () -> ErasureCoded
        if self._erasureCoded is _omit:
            raise AttributeError('erasureCoded not found')
        return self._erasureCoded
    
    @erasureCoded.setter
    def erasureCoded(self, new_val):
        # type: (Optional[ErasureCoded]) -> None
        self._erasureCoded = new_val

    def to_json(self):
        res = {
            'failureDomain': self._failureDomain,
            'replicated': self.replicated.to_json() if self._replicated is not _omit else self._replicated,
            'erasureCoded': self.erasureCoded.to_json() if self._erasureCoded is not _omit else self._erasureCoded,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[DataPoolsItem]
        return cls(
            failureDomain=data.get('failureDomain', _omit),
            replicated=Replicated.from_json(data['replicated']) if 'replicated' in data else _omit,
            erasureCoded=ErasureCoded.from_json(data['erasureCoded']) if 'erasureCoded' in data else _omit,
        )


class DataPoolsList(list):
    def to_json(self):
        return [e.to_json() for e in self]

    @classmethod
    def from_json(cls, data):
        # type: (list) -> Optional[DataPoolsList]
        return cls(DataPoolsItem.from_json(e) for e in data)


class Spec(object):
    def __init__(self,
                 metadataServer=_omit,  # type: Optional[MetadataServer]
                 metadataPool=_omit,  # type: Optional[MetadataPool]
                 dataPools=_omit,  # type: Optional[DataPoolsList]
                 ):
        self.metadataServer = metadataServer  # type: ignore
        self.metadataPool = metadataPool  # type: ignore
        self.dataPools = dataPools  # type: ignore

    @property
    def metadataServer(self):
        # type: () -> MetadataServer
        if self._metadataServer is _omit:
            raise AttributeError('metadataServer not found')
        return self._metadataServer
    
    @metadataServer.setter
    def metadataServer(self, new_val):
        # type: (Optional[MetadataServer]) -> None
        self._metadataServer = new_val
    
    @property
    def metadataPool(self):
        # type: () -> MetadataPool
        if self._metadataPool is _omit:
            raise AttributeError('metadataPool not found')
        return self._metadataPool
    
    @metadataPool.setter
    def metadataPool(self, new_val):
        # type: (Optional[MetadataPool]) -> None
        self._metadataPool = new_val
    
    @property
    def dataPools(self):
        # type: () -> DataPoolsList
        if self._dataPools is _omit:
            raise AttributeError('dataPools not found')
        return self._dataPools
    
    @dataPools.setter
    def dataPools(self, new_val):
        # type: (Optional[DataPoolsList]) -> None
        self._dataPools = new_val

    def to_json(self):
        res = {
            'metadataServer': self.metadataServer.to_json() if self._metadataServer is not _omit else self._metadataServer,
            'metadataPool': self.metadataPool.to_json() if self._metadataPool is not _omit else self._metadataPool,
            'dataPools': self.dataPools.to_json() if self._dataPools is not _omit else self._dataPools,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Spec
        return cls(
            metadataServer=MetadataServer.from_json(data['metadataServer']) if 'metadataServer' in data else _omit,
            metadataPool=MetadataPool.from_json(data['metadataPool']) if 'metadataPool' in data else _omit,
            dataPools=DataPoolsList.from_json(data['dataPools']) if 'dataPools' in data else _omit,
        )


class CephFilesystem(object):
    def __init__(self,
                 apiVersion,  # type: str
                 metadata,  # type: Any
                 spec,  # type: Spec
                 kind="CephFilesystem",  # type: str
                 status=_omit,  # type: Optional[Any]
                 ):
        self.apiVersion = apiVersion  # type: ignore
        self.metadata = metadata  # type: ignore
        self.spec = spec  # type: ignore
        self.kind = kind  # type: ignore
        self.status = status  # type: ignore

    @property
    def apiVersion(self):
        # type: () -> str
        if self._apiVersion is _omit:
            raise AttributeError('apiVersion not found')
        return self._apiVersion
    
    @apiVersion.setter
    def apiVersion(self, new_val):
        # type: (str) -> None
        self._apiVersion = new_val
    
    @property
    def kind(self):
        # type: () -> str
        if self._kind is _omit:
            raise AttributeError('kind not found')
        return self._kind
    
    @kind.setter
    def kind(self, new_val):
        # type: (str) -> None
        self._kind = new_val
    
    @property
    def metadata(self):
        # type: () -> Any
        if self._metadata is _omit:
            raise AttributeError('metadata not found')
        return self._metadata
    
    @metadata.setter
    def metadata(self, new_val):
        # type: (Any) -> None
        self._metadata = new_val
    
    @property
    def status(self):
        # type: () -> Any
        if self._status is _omit:
            raise AttributeError('status not found')
        return self._status
    
    @status.setter
    def status(self, new_val):
        # type: (Optional[Any]) -> None
        self._status = new_val
    
    @property
    def spec(self):
        # type: () -> Spec
        if self._spec is _omit:
            raise AttributeError('spec not found')
        return self._spec
    
    @spec.setter
    def spec(self, new_val):
        # type: (Spec) -> None
        self._spec = new_val

    def to_json(self):
        res = {
            'apiVersion': self._apiVersion,
            'kind': self._kind,
            'metadata': self._metadata,
            'status': self._status,
            'spec': self.spec.to_json(),
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> CephFilesystem
        return cls(
            apiVersion=data['apiVersion'],
            kind=data['kind'],
            metadata=data['metadata'],
            status=data.get('status', _omit),
            spec=Spec.from_json(data['spec']),
        )
