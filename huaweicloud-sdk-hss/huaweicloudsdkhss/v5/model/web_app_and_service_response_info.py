# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebAppAndServiceResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalogue': 'str',
        'name': 'str',
        'version': 'str',
        'agent_id': 'str',
        'install_path': 'str',
        'config_path': 'str',
        'uid': 'int',
        'gid': 'int',
        'mode': 'str',
        'ctime': 'int',
        'mtime': 'int',
        'atime': 'int',
        'pid': 'int',
        'proc_path': 'str',
        'container_id': 'str',
        'container_name': 'str',
        'record_time': 'int',
        'host_id': 'str',
        'host_name': 'str',
        'host_ip': 'str'
    }

    attribute_map = {
        'catalogue': 'catalogue',
        'name': 'name',
        'version': 'version',
        'agent_id': 'agent_id',
        'install_path': 'install_path',
        'config_path': 'config_path',
        'uid': 'uid',
        'gid': 'gid',
        'mode': 'mode',
        'ctime': 'ctime',
        'mtime': 'mtime',
        'atime': 'atime',
        'pid': 'pid',
        'proc_path': 'proc_path',
        'container_id': 'container_id',
        'container_name': 'container_name',
        'record_time': 'record_time',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip'
    }

    def __init__(self, catalogue=None, name=None, version=None, agent_id=None, install_path=None, config_path=None, uid=None, gid=None, mode=None, ctime=None, mtime=None, atime=None, pid=None, proc_path=None, container_id=None, container_name=None, record_time=None, host_id=None, host_name=None, host_ip=None):
        r"""WebAppAndServiceResponseInfo

        The model defined in huaweicloud sdk

        :param catalogue: **参数解释**: web应用、web服务、数据库资产指纹种类 **取值范围**: 字符长度0-64 
        :type catalogue: str
        :param name: **参数解释**: 资产指纹名字 **取值范围**: 字符长度0-64 
        :type name: str
        :param version: **参数解释**: 资产指纹版本 **取值范围**: 字符长度0-64 
        :type version: str
        :param agent_id: **参数解释** agent id **取值范围** 字符长度1-64 
        :type agent_id: str
        :param install_path: **参数解释** 安装路径 **取值范围** 字符长度0-256 
        :type install_path: str
        :param config_path: **参数解释** 配置文件路径 **取值范围** 字符长度0-256 
        :type config_path: str
        :param uid: **参数解释**: uid **取值范围**: 最小值0，最大值2147483647 
        :type uid: int
        :param gid: **参数解释**: gid **取值范围**: 最小值0，最大值2147483647 
        :type gid: int
        :param mode: **参数解释**: 资产指纹文件权限 **取值范围**: 字符长度1-32 
        :type mode: str
        :param ctime: **参数解释**: 资产指纹文件最近状态改变时间 **取值范围**: 最小值0，最大值2^63-1 
        :type ctime: int
        :param mtime: **参数解释**: 资产指纹文件最近修改时间 **取值范围**: 最小值0，最大值2^63-1 
        :type mtime: int
        :param atime: **参数解释**: 资产指纹文件最近访问时间 **取值范围**: 最小值0，最大值2^63-1 
        :type atime: int
        :param pid: **参数解释**: pid **取值范围**: 最小值0，最大值2147483647 
        :type pid: int
        :param proc_path: **参数解释**: 资产指纹进程路径 **取值范围**: 字符长度0-256 
        :type proc_path: str
        :param container_id: **参数解释**: 容器id **取值范围**: 字符长度0-256 
        :type container_id: str
        :param container_name: **参数解释**: 容器名称 **取值范围**: 字符长度0-256 
        :type container_name: str
        :param record_time: **参数解释**: 资产指纹扫描时间 **取值范围**: 最小值0，最大值2^63-1 
        :type record_time: int
        :param host_id: **参数解释** 主机id **取值范围** 字符长度1-64 
        :type host_id: str
        :param host_name: **参数解释** 服务器名称 **取值范围** 字符长度1-64 
        :type host_name: str
        :param host_ip: **参数解释** 服务器ip **取值范围** 字符长度1-64 
        :type host_ip: str
        """
        
        

        self._catalogue = None
        self._name = None
        self._version = None
        self._agent_id = None
        self._install_path = None
        self._config_path = None
        self._uid = None
        self._gid = None
        self._mode = None
        self._ctime = None
        self._mtime = None
        self._atime = None
        self._pid = None
        self._proc_path = None
        self._container_id = None
        self._container_name = None
        self._record_time = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self.discriminator = None

        if catalogue is not None:
            self.catalogue = catalogue
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if agent_id is not None:
            self.agent_id = agent_id
        if install_path is not None:
            self.install_path = install_path
        if config_path is not None:
            self.config_path = config_path
        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid
        if mode is not None:
            self.mode = mode
        if ctime is not None:
            self.ctime = ctime
        if mtime is not None:
            self.mtime = mtime
        if atime is not None:
            self.atime = atime
        if pid is not None:
            self.pid = pid
        if proc_path is not None:
            self.proc_path = proc_path
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if record_time is not None:
            self.record_time = record_time
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip

    @property
    def catalogue(self):
        r"""Gets the catalogue of this WebAppAndServiceResponseInfo.

        **参数解释**: web应用、web服务、数据库资产指纹种类 **取值范围**: 字符长度0-64 

        :return: The catalogue of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._catalogue

    @catalogue.setter
    def catalogue(self, catalogue):
        r"""Sets the catalogue of this WebAppAndServiceResponseInfo.

        **参数解释**: web应用、web服务、数据库资产指纹种类 **取值范围**: 字符长度0-64 

        :param catalogue: The catalogue of this WebAppAndServiceResponseInfo.
        :type catalogue: str
        """
        self._catalogue = catalogue

    @property
    def name(self):
        r"""Gets the name of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹名字 **取值范围**: 字符长度0-64 

        :return: The name of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹名字 **取值范围**: 字符长度0-64 

        :param name: The name of this WebAppAndServiceResponseInfo.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹版本 **取值范围**: 字符长度0-64 

        :return: The version of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹版本 **取值范围**: 字符长度0-64 

        :param version: The version of this WebAppAndServiceResponseInfo.
        :type version: str
        """
        self._version = version

    @property
    def agent_id(self):
        r"""Gets the agent_id of this WebAppAndServiceResponseInfo.

        **参数解释** agent id **取值范围** 字符长度1-64 

        :return: The agent_id of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this WebAppAndServiceResponseInfo.

        **参数解释** agent id **取值范围** 字符长度1-64 

        :param agent_id: The agent_id of this WebAppAndServiceResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def install_path(self):
        r"""Gets the install_path of this WebAppAndServiceResponseInfo.

        **参数解释** 安装路径 **取值范围** 字符长度0-256 

        :return: The install_path of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._install_path

    @install_path.setter
    def install_path(self, install_path):
        r"""Sets the install_path of this WebAppAndServiceResponseInfo.

        **参数解释** 安装路径 **取值范围** 字符长度0-256 

        :param install_path: The install_path of this WebAppAndServiceResponseInfo.
        :type install_path: str
        """
        self._install_path = install_path

    @property
    def config_path(self):
        r"""Gets the config_path of this WebAppAndServiceResponseInfo.

        **参数解释** 配置文件路径 **取值范围** 字符长度0-256 

        :return: The config_path of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._config_path

    @config_path.setter
    def config_path(self, config_path):
        r"""Sets the config_path of this WebAppAndServiceResponseInfo.

        **参数解释** 配置文件路径 **取值范围** 字符长度0-256 

        :param config_path: The config_path of this WebAppAndServiceResponseInfo.
        :type config_path: str
        """
        self._config_path = config_path

    @property
    def uid(self):
        r"""Gets the uid of this WebAppAndServiceResponseInfo.

        **参数解释**: uid **取值范围**: 最小值0，最大值2147483647 

        :return: The uid of this WebAppAndServiceResponseInfo.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this WebAppAndServiceResponseInfo.

        **参数解释**: uid **取值范围**: 最小值0，最大值2147483647 

        :param uid: The uid of this WebAppAndServiceResponseInfo.
        :type uid: int
        """
        self._uid = uid

    @property
    def gid(self):
        r"""Gets the gid of this WebAppAndServiceResponseInfo.

        **参数解释**: gid **取值范围**: 最小值0，最大值2147483647 

        :return: The gid of this WebAppAndServiceResponseInfo.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        r"""Sets the gid of this WebAppAndServiceResponseInfo.

        **参数解释**: gid **取值范围**: 最小值0，最大值2147483647 

        :param gid: The gid of this WebAppAndServiceResponseInfo.
        :type gid: int
        """
        self._gid = gid

    @property
    def mode(self):
        r"""Gets the mode of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹文件权限 **取值范围**: 字符长度1-32 

        :return: The mode of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹文件权限 **取值范围**: 字符长度1-32 

        :param mode: The mode of this WebAppAndServiceResponseInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def ctime(self):
        r"""Gets the ctime of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹文件最近状态改变时间 **取值范围**: 最小值0，最大值2^63-1 

        :return: The ctime of this WebAppAndServiceResponseInfo.
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        r"""Sets the ctime of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹文件最近状态改变时间 **取值范围**: 最小值0，最大值2^63-1 

        :param ctime: The ctime of this WebAppAndServiceResponseInfo.
        :type ctime: int
        """
        self._ctime = ctime

    @property
    def mtime(self):
        r"""Gets the mtime of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹文件最近修改时间 **取值范围**: 最小值0，最大值2^63-1 

        :return: The mtime of this WebAppAndServiceResponseInfo.
        :rtype: int
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        r"""Sets the mtime of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹文件最近修改时间 **取值范围**: 最小值0，最大值2^63-1 

        :param mtime: The mtime of this WebAppAndServiceResponseInfo.
        :type mtime: int
        """
        self._mtime = mtime

    @property
    def atime(self):
        r"""Gets the atime of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹文件最近访问时间 **取值范围**: 最小值0，最大值2^63-1 

        :return: The atime of this WebAppAndServiceResponseInfo.
        :rtype: int
        """
        return self._atime

    @atime.setter
    def atime(self, atime):
        r"""Sets the atime of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹文件最近访问时间 **取值范围**: 最小值0，最大值2^63-1 

        :param atime: The atime of this WebAppAndServiceResponseInfo.
        :type atime: int
        """
        self._atime = atime

    @property
    def pid(self):
        r"""Gets the pid of this WebAppAndServiceResponseInfo.

        **参数解释**: pid **取值范围**: 最小值0，最大值2147483647 

        :return: The pid of this WebAppAndServiceResponseInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this WebAppAndServiceResponseInfo.

        **参数解释**: pid **取值范围**: 最小值0，最大值2147483647 

        :param pid: The pid of this WebAppAndServiceResponseInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def proc_path(self):
        r"""Gets the proc_path of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹进程路径 **取值范围**: 字符长度0-256 

        :return: The proc_path of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._proc_path

    @proc_path.setter
    def proc_path(self, proc_path):
        r"""Sets the proc_path of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹进程路径 **取值范围**: 字符长度0-256 

        :param proc_path: The proc_path of this WebAppAndServiceResponseInfo.
        :type proc_path: str
        """
        self._proc_path = proc_path

    @property
    def container_id(self):
        r"""Gets the container_id of this WebAppAndServiceResponseInfo.

        **参数解释**: 容器id **取值范围**: 字符长度0-256 

        :return: The container_id of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this WebAppAndServiceResponseInfo.

        **参数解释**: 容器id **取值范围**: 字符长度0-256 

        :param container_id: The container_id of this WebAppAndServiceResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this WebAppAndServiceResponseInfo.

        **参数解释**: 容器名称 **取值范围**: 字符长度0-256 

        :return: The container_name of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this WebAppAndServiceResponseInfo.

        **参数解释**: 容器名称 **取值范围**: 字符长度0-256 

        :param container_name: The container_name of this WebAppAndServiceResponseInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def record_time(self):
        r"""Gets the record_time of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹扫描时间 **取值范围**: 最小值0，最大值2^63-1 

        :return: The record_time of this WebAppAndServiceResponseInfo.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        r"""Sets the record_time of this WebAppAndServiceResponseInfo.

        **参数解释**: 资产指纹扫描时间 **取值范围**: 最小值0，最大值2^63-1 

        :param record_time: The record_time of this WebAppAndServiceResponseInfo.
        :type record_time: int
        """
        self._record_time = record_time

    @property
    def host_id(self):
        r"""Gets the host_id of this WebAppAndServiceResponseInfo.

        **参数解释** 主机id **取值范围** 字符长度1-64 

        :return: The host_id of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this WebAppAndServiceResponseInfo.

        **参数解释** 主机id **取值范围** 字符长度1-64 

        :param host_id: The host_id of this WebAppAndServiceResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this WebAppAndServiceResponseInfo.

        **参数解释** 服务器名称 **取值范围** 字符长度1-64 

        :return: The host_name of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this WebAppAndServiceResponseInfo.

        **参数解释** 服务器名称 **取值范围** 字符长度1-64 

        :param host_name: The host_name of this WebAppAndServiceResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this WebAppAndServiceResponseInfo.

        **参数解释** 服务器ip **取值范围** 字符长度1-64 

        :return: The host_ip of this WebAppAndServiceResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this WebAppAndServiceResponseInfo.

        **参数解释** 服务器ip **取值范围** 字符长度1-64 

        :param host_ip: The host_ip of this WebAppAndServiceResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebAppAndServiceResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
