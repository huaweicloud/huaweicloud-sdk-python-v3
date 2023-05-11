# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceServerResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'ip': 'str',
        'name': 'str',
        'os_type': 'str',
        'os_version': 'str',
        'oem_system': 'bool',
        'state': 'str',
        'migration_cycle': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ip': 'ip',
        'name': 'name',
        'os_type': 'os_type',
        'os_version': 'os_version',
        'oem_system': 'oem_system',
        'state': 'state',
        'migration_cycle': 'migration_cycle'
    }

    def __init__(self, id=None, ip=None, name=None, os_type=None, os_version=None, oem_system=None, state=None, migration_cycle=None):
        """SourceServerResponse

        The model defined in huaweicloud sdk

        :param id: 源端在SMS数据库中的ID
        :type id: str
        :param ip: 源端服务器ip，注册源端时必选，更新非必选
        :type ip: str
        :param name: 用来区分不同源端服务器的名称
        :type name: str
        :param os_type: 源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选
        :type os_type: str
        :param os_version: 操作系统版本，注册必选，更新非必选
        :type os_version: str
        :param oem_system: 是否是OEM操作系统(Windows)
        :type oem_system: bool
        :param state: 当前源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 testing：测试中 finished：启动目的端完成
        :type state: str
        :param migration_cycle: 迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 
        :type migration_cycle: str
        """
        
        

        self._id = None
        self._ip = None
        self._name = None
        self._os_type = None
        self._os_version = None
        self._oem_system = None
        self._state = None
        self._migration_cycle = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.ip = ip
        self.name = name
        self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version
        if oem_system is not None:
            self.oem_system = oem_system
        if state is not None:
            self.state = state
        if migration_cycle is not None:
            self.migration_cycle = migration_cycle

    @property
    def id(self):
        """Gets the id of this SourceServerResponse.

        源端在SMS数据库中的ID

        :return: The id of this SourceServerResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceServerResponse.

        源端在SMS数据库中的ID

        :param id: The id of this SourceServerResponse.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        """Gets the ip of this SourceServerResponse.

        源端服务器ip，注册源端时必选，更新非必选

        :return: The ip of this SourceServerResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SourceServerResponse.

        源端服务器ip，注册源端时必选，更新非必选

        :param ip: The ip of this SourceServerResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def name(self):
        """Gets the name of this SourceServerResponse.

        用来区分不同源端服务器的名称

        :return: The name of this SourceServerResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceServerResponse.

        用来区分不同源端服务器的名称

        :param name: The name of this SourceServerResponse.
        :type name: str
        """
        self._name = name

    @property
    def os_type(self):
        """Gets the os_type of this SourceServerResponse.

        源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选

        :return: The os_type of this SourceServerResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this SourceServerResponse.

        源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选

        :param os_type: The os_type of this SourceServerResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        """Gets the os_version of this SourceServerResponse.

        操作系统版本，注册必选，更新非必选

        :return: The os_version of this SourceServerResponse.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this SourceServerResponse.

        操作系统版本，注册必选，更新非必选

        :param os_version: The os_version of this SourceServerResponse.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def oem_system(self):
        """Gets the oem_system of this SourceServerResponse.

        是否是OEM操作系统(Windows)

        :return: The oem_system of this SourceServerResponse.
        :rtype: bool
        """
        return self._oem_system

    @oem_system.setter
    def oem_system(self, oem_system):
        """Sets the oem_system of this SourceServerResponse.

        是否是OEM操作系统(Windows)

        :param oem_system: The oem_system of this SourceServerResponse.
        :type oem_system: bool
        """
        self._oem_system = oem_system

    @property
    def state(self):
        """Gets the state of this SourceServerResponse.

        当前源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 testing：测试中 finished：启动目的端完成

        :return: The state of this SourceServerResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SourceServerResponse.

        当前源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 testing：测试中 finished：启动目的端完成

        :param state: The state of this SourceServerResponse.
        :type state: str
        """
        self._state = state

    @property
    def migration_cycle(self):
        """Gets the migration_cycle of this SourceServerResponse.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :return: The migration_cycle of this SourceServerResponse.
        :rtype: str
        """
        return self._migration_cycle

    @migration_cycle.setter
    def migration_cycle(self, migration_cycle):
        """Sets the migration_cycle of this SourceServerResponse.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :param migration_cycle: The migration_cycle of this SourceServerResponse.
        :type migration_cycle: str
        """
        self._migration_cycle = migration_cycle

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SourceServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
