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

class CephVersion(object):
    def __init__(self,
                 allowUnsupported=_omit,  # type: Optional[bool]
                 image=_omit,  # type: Optional[str]
                 name=_omit,  # type: Optional[str]
                 ):
        self.allowUnsupported = allowUnsupported  # type: ignore
        self.image = image  # type: ignore
        self.name = name  # type: ignore

    @property
    def allowUnsupported(self):
        # type: () -> bool
        if self._allowUnsupported is _omit:
            raise AttributeError('allowUnsupported not found')
        return self._allowUnsupported
    
    @allowUnsupported.setter
    def allowUnsupported(self, new_val):
        # type: (Optional[bool]) -> None
        self._allowUnsupported = new_val
    
    @property
    def image(self):
        # type: () -> str
        if self._image is _omit:
            raise AttributeError('image not found')
        return self._image
    
    @image.setter
    def image(self, new_val):
        # type: (Optional[str]) -> None
        self._image = new_val
    
    @property
    def name(self):
        # type: () -> str
        if self._name is _omit:
            raise AttributeError('name not found')
        return self._name
    
    @name.setter
    def name(self, new_val):
        # type: (Optional[str]) -> None
        self._name = new_val

    def to_json(self):
        res = {
            'allowUnsupported': self._allowUnsupported,
            'image': self._image,
            'name': self._name,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[CephVersion]
        return cls(
            allowUnsupported=data.get('allowUnsupported', _omit),
            image=data.get('image', _omit),
            name=data.get('name', _omit),
        )


class Dashboard(object):
    def __init__(self,
                 enabled=_omit,  # type: Optional[bool]
                 urlPrefix=_omit,  # type: Optional[str]
                 port=_omit,  # type: Optional[int]
                 ssl=_omit,  # type: Optional[bool]
                 ):
        self.enabled = enabled  # type: ignore
        self.urlPrefix = urlPrefix  # type: ignore
        self.port = port  # type: ignore
        self.ssl = ssl  # type: ignore

    @property
    def enabled(self):
        # type: () -> bool
        if self._enabled is _omit:
            raise AttributeError('enabled not found')
        return self._enabled
    
    @enabled.setter
    def enabled(self, new_val):
        # type: (Optional[bool]) -> None
        self._enabled = new_val
    
    @property
    def urlPrefix(self):
        # type: () -> str
        if self._urlPrefix is _omit:
            raise AttributeError('urlPrefix not found')
        return self._urlPrefix
    
    @urlPrefix.setter
    def urlPrefix(self, new_val):
        # type: (Optional[str]) -> None
        self._urlPrefix = new_val
    
    @property
    def port(self):
        # type: () -> int
        if self._port is _omit:
            raise AttributeError('port not found')
        return self._port
    
    @port.setter
    def port(self, new_val):
        # type: (Optional[int]) -> None
        self._port = new_val
    
    @property
    def ssl(self):
        # type: () -> bool
        if self._ssl is _omit:
            raise AttributeError('ssl not found')
        return self._ssl
    
    @ssl.setter
    def ssl(self, new_val):
        # type: (Optional[bool]) -> None
        self._ssl = new_val

    def to_json(self):
        res = {
            'enabled': self._enabled,
            'urlPrefix': self._urlPrefix,
            'port': self._port,
            'ssl': self._ssl,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[Dashboard]
        return cls(
            enabled=data.get('enabled', _omit),
            urlPrefix=data.get('urlPrefix', _omit),
            port=data.get('port', _omit),
            ssl=data.get('ssl', _omit),
        )


class Mon(object):
    def __init__(self,
                 count,  # type: int
                 allowMultiplePerNode=_omit,  # type: Optional[bool]
                 preferredCount=_omit,  # type: Optional[int]
                 ):
        self.count = count  # type: ignore
        self.allowMultiplePerNode = allowMultiplePerNode  # type: ignore
        self.preferredCount = preferredCount  # type: ignore

    @property
    def allowMultiplePerNode(self):
        # type: () -> bool
        if self._allowMultiplePerNode is _omit:
            raise AttributeError('allowMultiplePerNode not found')
        return self._allowMultiplePerNode
    
    @allowMultiplePerNode.setter
    def allowMultiplePerNode(self, new_val):
        # type: (Optional[bool]) -> None
        self._allowMultiplePerNode = new_val
    
    @property
    def count(self):
        # type: () -> int
        if self._count is _omit:
            raise AttributeError('count not found')
        return self._count
    
    @count.setter
    def count(self, new_val):
        # type: (int) -> None
        self._count = new_val
    
    @property
    def preferredCount(self):
        # type: () -> int
        if self._preferredCount is _omit:
            raise AttributeError('preferredCount not found')
        return self._preferredCount
    
    @preferredCount.setter
    def preferredCount(self, new_val):
        # type: (Optional[int]) -> None
        self._preferredCount = new_val

    def to_json(self):
        res = {
            'allowMultiplePerNode': self._allowMultiplePerNode,
            'count': self._count,
            'preferredCount': self._preferredCount,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Mon
        return cls(
            allowMultiplePerNode=data.get('allowMultiplePerNode', _omit),
            count=data['count'],
            preferredCount=data.get('preferredCount', _omit),
        )


class Network(object):
    def __init__(self,
                 hostNetwork=_omit,  # type: Optional[bool]
                 ):
        self.hostNetwork = hostNetwork  # type: ignore

    @property
    def hostNetwork(self):
        # type: () -> bool
        if self._hostNetwork is _omit:
            raise AttributeError('hostNetwork not found')
        return self._hostNetwork
    
    @hostNetwork.setter
    def hostNetwork(self, new_val):
        # type: (Optional[bool]) -> None
        self._hostNetwork = new_val

    def to_json(self):
        res = {
            'hostNetwork': self._hostNetwork,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[Network]
        return cls(
            hostNetwork=data.get('hostNetwork', _omit),
        )


class Config(object):
    def __init__(self,
                 metadataDevice=_omit,  # type: Optional[str]
                 storeType=_omit,  # type: Optional[str]
                 databaseSizeMB=_omit,  # type: Optional[str]
                 walSizeMB=_omit,  # type: Optional[str]
                 journalSizeMB=_omit,  # type: Optional[str]
                 osdsPerDevice=_omit,  # type: Optional[str]
                 encryptedDevice=_omit,  # type: Optional[str]
                 ):
        self.metadataDevice = metadataDevice  # type: ignore
        self.storeType = storeType  # type: ignore
        self.databaseSizeMB = databaseSizeMB  # type: ignore
        self.walSizeMB = walSizeMB  # type: ignore
        self.journalSizeMB = journalSizeMB  # type: ignore
        self.osdsPerDevice = osdsPerDevice  # type: ignore
        self.encryptedDevice = encryptedDevice  # type: ignore

    @property
    def metadataDevice(self):
        # type: () -> str
        if self._metadataDevice is _omit:
            raise AttributeError('metadataDevice not found')
        return self._metadataDevice
    
    @metadataDevice.setter
    def metadataDevice(self, new_val):
        # type: (Optional[str]) -> None
        self._metadataDevice = new_val
    
    @property
    def storeType(self):
        # type: () -> str
        if self._storeType is _omit:
            raise AttributeError('storeType not found')
        return self._storeType
    
    @storeType.setter
    def storeType(self, new_val):
        # type: (Optional[str]) -> None
        self._storeType = new_val
    
    @property
    def databaseSizeMB(self):
        # type: () -> str
        if self._databaseSizeMB is _omit:
            raise AttributeError('databaseSizeMB not found')
        return self._databaseSizeMB
    
    @databaseSizeMB.setter
    def databaseSizeMB(self, new_val):
        # type: (Optional[str]) -> None
        self._databaseSizeMB = new_val
    
    @property
    def walSizeMB(self):
        # type: () -> str
        if self._walSizeMB is _omit:
            raise AttributeError('walSizeMB not found')
        return self._walSizeMB
    
    @walSizeMB.setter
    def walSizeMB(self, new_val):
        # type: (Optional[str]) -> None
        self._walSizeMB = new_val
    
    @property
    def journalSizeMB(self):
        # type: () -> str
        if self._journalSizeMB is _omit:
            raise AttributeError('journalSizeMB not found')
        return self._journalSizeMB
    
    @journalSizeMB.setter
    def journalSizeMB(self, new_val):
        # type: (Optional[str]) -> None
        self._journalSizeMB = new_val
    
    @property
    def osdsPerDevice(self):
        # type: () -> str
        if self._osdsPerDevice is _omit:
            raise AttributeError('osdsPerDevice not found')
        return self._osdsPerDevice
    
    @osdsPerDevice.setter
    def osdsPerDevice(self, new_val):
        # type: (Optional[str]) -> None
        self._osdsPerDevice = new_val
    
    @property
    def encryptedDevice(self):
        # type: () -> str
        if self._encryptedDevice is _omit:
            raise AttributeError('encryptedDevice not found')
        return self._encryptedDevice
    
    @encryptedDevice.setter
    def encryptedDevice(self, new_val):
        # type: (Optional[str]) -> None
        self._encryptedDevice = new_val

    def to_json(self):
        res = {
            'metadataDevice': self._metadataDevice,
            'storeType': self._storeType,
            'databaseSizeMB': self._databaseSizeMB,
            'walSizeMB': self._walSizeMB,
            'journalSizeMB': self._journalSizeMB,
            'osdsPerDevice': self._osdsPerDevice,
            'encryptedDevice': self._encryptedDevice,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[Config]
        return cls(
            metadataDevice=data.get('metadataDevice', _omit),
            storeType=data.get('storeType', _omit),
            databaseSizeMB=data.get('databaseSizeMB', _omit),
            walSizeMB=data.get('walSizeMB', _omit),
            journalSizeMB=data.get('journalSizeMB', _omit),
            osdsPerDevice=data.get('osdsPerDevice', _omit),
            encryptedDevice=data.get('encryptedDevice', _omit),
        )


class DirectoriesItem(object):
    def __init__(self,
                 path=_omit,  # type: Optional[str]
                 ):
        self.path = path  # type: ignore

    @property
    def path(self):
        # type: () -> str
        if self._path is _omit:
            raise AttributeError('path not found')
        return self._path
    
    @path.setter
    def path(self, new_val):
        # type: (Optional[str]) -> None
        self._path = new_val

    def to_json(self):
        res = {
            'path': self._path,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[DirectoriesItem]
        return cls(
            path=data.get('path', _omit),
        )


class DirectoriesList(list):
    def to_json(self):
        return [e.to_json() for e in self]

    @classmethod
    def from_json(cls, data):
        # type: (list) -> Optional[DirectoriesList]
        return cls(DirectoriesItem.from_json(e) for e in data)


class DevicesItem(object):
    def __init__(self,
                 name=_omit,  # type: Optional[str]
                 config=_omit,  # type: Optional[Config]
                 ):
        self.name = name  # type: ignore
        self.config = config  # type: ignore

    @property
    def name(self):
        # type: () -> str
        if self._name is _omit:
            raise AttributeError('name not found')
        return self._name
    
    @name.setter
    def name(self, new_val):
        # type: (Optional[str]) -> None
        self._name = new_val
    
    @property
    def config(self):
        # type: () -> Optional[Config]
        if self._config is _omit:
            raise AttributeError('config not found')
        return self._config
    
    @config.setter
    def config(self, new_val):
        # type: (Optional[Config]) -> None
        self._config = new_val

    def to_json(self):
        res = {
            'name': self._name,
            'config': self.config.to_json() if self._config is not None and self._config is not _omit else self._config,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[DevicesItem]
        return cls(
            name=data.get('name', _omit),
            config=(Config.from_json(data['config']) if data['config'] is not None else None) if 'config' in data else _omit,
        )


class DevicesList(list):
    def to_json(self):
        return [e.to_json() for e in self]

    @classmethod
    def from_json(cls, data):
        # type: (list) -> Optional[DevicesList]
        return cls(DevicesItem.from_json(e) for e in data)


class NodesItem(object):
    def __init__(self,
                 name=_omit,  # type: Optional[str]
                 config=_omit,  # type: Optional[Config]
                 useAllDevices=_omit,  # type: Optional[bool]
                 deviceFilter=_omit,  # type: Optional[str]
                 directories=_omit,  # type: Optional[DirectoriesList]
                 devices=_omit,  # type: Optional[DevicesList]
                 location=_omit,  # type: Optional[str]
                 resources=_omit,  # type: Optional[Any]
                 ):
        self.name = name  # type: ignore
        self.config = config  # type: ignore
        self.useAllDevices = useAllDevices  # type: ignore
        self.deviceFilter = deviceFilter  # type: ignore
        self.directories = directories  # type: ignore
        self.devices = devices  # type: ignore
        self.location = location  # type: ignore
        self.resources = resources  # type: ignore

    @property
    def name(self):
        # type: () -> str
        if self._name is _omit:
            raise AttributeError('name not found')
        return self._name
    
    @name.setter
    def name(self, new_val):
        # type: (Optional[str]) -> None
        self._name = new_val
    
    @property
    def config(self):
        # type: () -> Config
        if self._config is _omit:
            raise AttributeError('config not found')
        return self._config
    
    @config.setter
    def config(self, new_val):
        # type: (Optional[Config]) -> None
        self._config = new_val
    
    @property
    def useAllDevices(self):
        # type: () -> bool
        if self._useAllDevices is _omit:
            raise AttributeError('useAllDevices not found')
        return self._useAllDevices
    
    @useAllDevices.setter
    def useAllDevices(self, new_val):
        # type: (Optional[bool]) -> None
        self._useAllDevices = new_val
    
    @property
    def deviceFilter(self):
        # type: () -> Optional[str]
        if self._deviceFilter is _omit:
            raise AttributeError('deviceFilter not found')
        return self._deviceFilter
    
    @deviceFilter.setter
    def deviceFilter(self, new_val):
        # type: (Optional[str]) -> None
        self._deviceFilter = new_val
    
    @property
    def directories(self):
        # type: () -> DirectoriesList
        if self._directories is _omit:
            raise AttributeError('directories not found')
        return self._directories
    
    @directories.setter
    def directories(self, new_val):
        # type: (Optional[DirectoriesList]) -> None
        self._directories = new_val
    
    @property
    def devices(self):
        # type: () -> DevicesList
        if self._devices is _omit:
            raise AttributeError('devices not found')
        return self._devices
    
    @devices.setter
    def devices(self, new_val):
        # type: (Optional[DevicesList]) -> None
        self._devices = new_val
    
    @property
    def location(self):
        # type: () -> Optional[str]
        if self._location is _omit:
            raise AttributeError('location not found')
        return self._location
    
    @location.setter
    def location(self, new_val):
        # type: (Optional[str]) -> None
        self._location = new_val
    
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
            'name': self._name,
            'config': self.config.to_json() if self._config is not _omit else self._config,
            'useAllDevices': self._useAllDevices,
            'deviceFilter': self._deviceFilter,
            'directories': self.directories.to_json() if self._directories is not _omit else self._directories,
            'devices': self.devices.to_json() if self._devices is not _omit else self._devices,
            'location': self._location,
            'resources': self._resources,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[NodesItem]
        return cls(
            name=data.get('name', _omit),
            config=Config.from_json(data['config']) if 'config' in data else _omit,
            useAllDevices=data.get('useAllDevices', _omit),
            deviceFilter=data.get('deviceFilter', _omit),
            directories=DirectoriesList.from_json(data['directories']) if 'directories' in data else _omit,
            devices=DevicesList.from_json(data['devices']) if 'devices' in data else _omit,
            location=data.get('location', _omit),
            resources=data.get('resources', _omit),
        )


class NodesList(list):
    def to_json(self):
        return [e.to_json() for e in self]

    @classmethod
    def from_json(cls, data):
        # type: (list) -> Optional[NodesList]
        return cls(NodesItem.from_json(e) for e in data)


class Storage(object):
    def __init__(self,
                 useAllNodes=_omit,  # type: Optional[bool]
                 nodes=_omit,  # type: Optional[NodesList]
                 useAllDevices=_omit,  # type: Optional[bool]
                 deviceFilter=_omit,  # type: Optional[str]
                 location=_omit,  # type: Optional[Any]
                 directories=_omit,  # type: Optional[DirectoriesList]
                 config=_omit,  # type: Optional[Config]
                 topologyAware=_omit,  # type: Optional[bool]
                 ):
        self.useAllNodes = useAllNodes  # type: ignore
        self.nodes = nodes  # type: ignore
        self.useAllDevices = useAllDevices  # type: ignore
        self.deviceFilter = deviceFilter  # type: ignore
        self.location = location  # type: ignore
        self.directories = directories  # type: ignore
        self.config = config  # type: ignore
        self.topologyAware = topologyAware  # type: ignore

    @property
    def useAllNodes(self):
        # type: () -> bool
        if self._useAllNodes is _omit:
            raise AttributeError('useAllNodes not found')
        return self._useAllNodes
    
    @useAllNodes.setter
    def useAllNodes(self, new_val):
        # type: (Optional[bool]) -> None
        self._useAllNodes = new_val
    
    @property
    def nodes(self):
        # type: () -> NodesList
        if self._nodes is _omit:
            raise AttributeError('nodes not found')
        return self._nodes
    
    @nodes.setter
    def nodes(self, new_val):
        # type: (Optional[NodesList]) -> None
        self._nodes = new_val
    
    @property
    def useAllDevices(self):
        # type: () -> bool
        if self._useAllDevices is _omit:
            raise AttributeError('useAllDevices not found')
        return self._useAllDevices
    
    @useAllDevices.setter
    def useAllDevices(self, new_val):
        # type: (Optional[bool]) -> None
        self._useAllDevices = new_val
    
    @property
    def deviceFilter(self):
        # type: () -> Optional[str]
        if self._deviceFilter is _omit:
            raise AttributeError('deviceFilter not found')
        return self._deviceFilter
    
    @deviceFilter.setter
    def deviceFilter(self, new_val):
        # type: (Optional[str]) -> None
        self._deviceFilter = new_val
    
    @property
    def location(self):
        # type: () -> Any
        if self._location is _omit:
            raise AttributeError('location not found')
        return self._location
    
    @location.setter
    def location(self, new_val):
        # type: (Optional[Any]) -> None
        self._location = new_val
    
    @property
    def directories(self):
        # type: () -> DirectoriesList
        if self._directories is _omit:
            raise AttributeError('directories not found')
        return self._directories
    
    @directories.setter
    def directories(self, new_val):
        # type: (Optional[DirectoriesList]) -> None
        self._directories = new_val
    
    @property
    def config(self):
        # type: () -> Optional[Config]
        if self._config is _omit:
            raise AttributeError('config not found')
        return self._config
    
    @config.setter
    def config(self, new_val):
        # type: (Optional[Config]) -> None
        self._config = new_val
    
    @property
    def topologyAware(self):
        # type: () -> bool
        if self._topologyAware is _omit:
            raise AttributeError('topologyAware not found')
        return self._topologyAware
    
    @topologyAware.setter
    def topologyAware(self, new_val):
        # type: (Optional[bool]) -> None
        self._topologyAware = new_val

    def to_json(self):
        res = {
            'useAllNodes': self._useAllNodes,
            'nodes': self.nodes.to_json() if self._nodes is not _omit else self._nodes,
            'useAllDevices': self._useAllDevices,
            'deviceFilter': self._deviceFilter,
            'location': self._location,
            'directories': self.directories.to_json() if self._directories is not _omit else self._directories,
            'config': self.config.to_json() if self._config is not None and self._config is not _omit else self._config,
            'topologyAware': self._topologyAware,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[Storage]
        return cls(
            useAllNodes=data.get('useAllNodes', _omit),
            nodes=NodesList.from_json(data['nodes']) if 'nodes' in data else _omit,
            useAllDevices=data.get('useAllDevices', _omit),
            deviceFilter=data.get('deviceFilter', _omit),
            location=data.get('location', _omit),
            directories=DirectoriesList.from_json(data['directories']) if 'directories' in data else _omit,
            config=(Config.from_json(data['config']) if data['config'] is not None else None) if 'config' in data else _omit,
            topologyAware=data.get('topologyAware', _omit),
        )


class Monitoring(object):
    def __init__(self,
                 enabled=_omit,  # type: Optional[bool]
                 rulesNamespace=_omit,  # type: Optional[str]
                 ):
        self.enabled = enabled  # type: ignore
        self.rulesNamespace = rulesNamespace  # type: ignore

    @property
    def enabled(self):
        # type: () -> bool
        if self._enabled is _omit:
            raise AttributeError('enabled not found')
        return self._enabled
    
    @enabled.setter
    def enabled(self, new_val):
        # type: (Optional[bool]) -> None
        self._enabled = new_val
    
    @property
    def rulesNamespace(self):
        # type: () -> str
        if self._rulesNamespace is _omit:
            raise AttributeError('rulesNamespace not found')
        return self._rulesNamespace
    
    @rulesNamespace.setter
    def rulesNamespace(self, new_val):
        # type: (Optional[str]) -> None
        self._rulesNamespace = new_val

    def to_json(self):
        res = {
            'enabled': self._enabled,
            'rulesNamespace': self._rulesNamespace,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[Monitoring]
        return cls(
            enabled=data.get('enabled', _omit),
            rulesNamespace=data.get('rulesNamespace', _omit),
        )


class RbdMirroring(object):
    def __init__(self,
                 workers=_omit,  # type: Optional[int]
                 ):
        self.workers = workers  # type: ignore

    @property
    def workers(self):
        # type: () -> int
        if self._workers is _omit:
            raise AttributeError('workers not found')
        return self._workers
    
    @workers.setter
    def workers(self, new_val):
        # type: (Optional[int]) -> None
        self._workers = new_val

    def to_json(self):
        res = {
            'workers': self._workers,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[RbdMirroring]
        return cls(
            workers=data.get('workers', _omit),
        )


class Spec(object):
    def __init__(self,
                 mon,  # type: Mon
                 annotations=_omit,  # type: Optional[Any]
                 cephVersion=_omit,  # type: Optional[CephVersion]
                 dashboard=_omit,  # type: Optional[Dashboard]
                 dataDirHostPath=_omit,  # type: Optional[str]
                 network=_omit,  # type: Optional[Network]
                 storage=_omit,  # type: Optional[Storage]
                 monitoring=_omit,  # type: Optional[Monitoring]
                 rbdMirroring=_omit,  # type: Optional[RbdMirroring]
                 placement=_omit,  # type: Optional[Any]
                 resources=_omit,  # type: Optional[Any]
                 ):
        self.mon = mon  # type: ignore
        self.annotations = annotations  # type: ignore
        self.cephVersion = cephVersion  # type: ignore
        self.dashboard = dashboard  # type: ignore
        self.dataDirHostPath = dataDirHostPath  # type: ignore
        self.network = network  # type: ignore
        self.storage = storage  # type: ignore
        self.monitoring = monitoring  # type: ignore
        self.rbdMirroring = rbdMirroring  # type: ignore
        self.placement = placement  # type: ignore
        self.resources = resources  # type: ignore

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
    def cephVersion(self):
        # type: () -> CephVersion
        if self._cephVersion is _omit:
            raise AttributeError('cephVersion not found')
        return self._cephVersion
    
    @cephVersion.setter
    def cephVersion(self, new_val):
        # type: (Optional[CephVersion]) -> None
        self._cephVersion = new_val
    
    @property
    def dashboard(self):
        # type: () -> Dashboard
        if self._dashboard is _omit:
            raise AttributeError('dashboard not found')
        return self._dashboard
    
    @dashboard.setter
    def dashboard(self, new_val):
        # type: (Optional[Dashboard]) -> None
        self._dashboard = new_val
    
    @property
    def dataDirHostPath(self):
        # type: () -> str
        if self._dataDirHostPath is _omit:
            raise AttributeError('dataDirHostPath not found')
        return self._dataDirHostPath
    
    @dataDirHostPath.setter
    def dataDirHostPath(self, new_val):
        # type: (Optional[str]) -> None
        self._dataDirHostPath = new_val
    
    @property
    def mon(self):
        # type: () -> Mon
        if self._mon is _omit:
            raise AttributeError('mon not found')
        return self._mon
    
    @mon.setter
    def mon(self, new_val):
        # type: (Mon) -> None
        self._mon = new_val
    
    @property
    def network(self):
        # type: () -> Network
        if self._network is _omit:
            raise AttributeError('network not found')
        return self._network
    
    @network.setter
    def network(self, new_val):
        # type: (Optional[Network]) -> None
        self._network = new_val
    
    @property
    def storage(self):
        # type: () -> Storage
        if self._storage is _omit:
            raise AttributeError('storage not found')
        return self._storage
    
    @storage.setter
    def storage(self, new_val):
        # type: (Optional[Storage]) -> None
        self._storage = new_val
    
    @property
    def monitoring(self):
        # type: () -> Monitoring
        if self._monitoring is _omit:
            raise AttributeError('monitoring not found')
        return self._monitoring
    
    @monitoring.setter
    def monitoring(self, new_val):
        # type: (Optional[Monitoring]) -> None
        self._monitoring = new_val
    
    @property
    def rbdMirroring(self):
        # type: () -> RbdMirroring
        if self._rbdMirroring is _omit:
            raise AttributeError('rbdMirroring not found')
        return self._rbdMirroring
    
    @rbdMirroring.setter
    def rbdMirroring(self, new_val):
        # type: (Optional[RbdMirroring]) -> None
        self._rbdMirroring = new_val
    
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
            'annotations': self._annotations,
            'cephVersion': self.cephVersion.to_json() if self._cephVersion is not _omit else self._cephVersion,
            'dashboard': self.dashboard.to_json() if self._dashboard is not _omit else self._dashboard,
            'dataDirHostPath': self._dataDirHostPath,
            'mon': self.mon.to_json(),
            'network': self.network.to_json() if self._network is not _omit else self._network,
            'storage': self.storage.to_json() if self._storage is not _omit else self._storage,
            'monitoring': self.monitoring.to_json() if self._monitoring is not _omit else self._monitoring,
            'rbdMirroring': self.rbdMirroring.to_json() if self._rbdMirroring is not _omit else self._rbdMirroring,
            'placement': self._placement,
            'resources': self._resources,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Spec
        return cls(
            annotations=data.get('annotations', _omit),
            cephVersion=CephVersion.from_json(data['cephVersion']) if 'cephVersion' in data else _omit,
            dashboard=Dashboard.from_json(data['dashboard']) if 'dashboard' in data else _omit,
            dataDirHostPath=data.get('dataDirHostPath', _omit),
            mon=Mon.from_json(data['mon']),
            network=Network.from_json(data['network']) if 'network' in data else _omit,
            storage=Storage.from_json(data['storage']) if 'storage' in data else _omit,
            monitoring=Monitoring.from_json(data['monitoring']) if 'monitoring' in data else _omit,
            rbdMirroring=RbdMirroring.from_json(data['rbdMirroring']) if 'rbdMirroring' in data else _omit,
            placement=data.get('placement', _omit),
            resources=data.get('resources', _omit),
        )


class CephCluster(object):
    def __init__(self,
                 apiVersion,  # type: str
                 metadata,  # type: Any
                 spec,  # type: Spec
                 kind="CephCluster",  # type: str
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
        # type: (dict) -> CephCluster
        return cls(
            apiVersion=data['apiVersion'],
            kind=data['kind'],
            metadata=data['metadata'],
            status=data.get('status', _omit),
            spec=Spec.from_json(data['spec']),
        )
