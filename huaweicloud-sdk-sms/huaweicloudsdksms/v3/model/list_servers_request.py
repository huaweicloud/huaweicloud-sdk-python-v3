# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'name': 'str',
        'id': 'str',
        'ip': 'str',
        'migproject': 'str',
        'limit': 'int',
        'offset': 'int',
        'migration_cycle': 'str',
        'connected': 'bool',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'state': 'state',
        'name': 'name',
        'id': 'id',
        'ip': 'ip',
        'migproject': 'migproject',
        'limit': 'limit',
        'offset': 'offset',
        'migration_cycle': 'migration_cycle',
        'connected': 'connected',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, state=None, name=None, id=None, ip=None, migproject=None, limit=None, offset=None, migration_cycle=None, connected=None, enterprise_project_id=None):
        """ListServersRequest

        The model defined in huaweicloud sdk

        :param state: 源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成
        :type state: str
        :param name: 源端服务器名称
        :type name: str
        :param id: 源端服务器ID
        :type id: str
        :param ip: 源端服务器IP地址
        :type ip: str
        :param migproject: 迁移项目ID，填写该参数将查询迁移项目下的所有虚拟机
        :type migproject: str
        :param limit: 每一页记录的源端服务器数量，0表示用默认值 200
        :type limit: int
        :param offset: 偏移量，默认值0
        :type offset: int
        :param migration_cycle: checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 cutovering:启动目的端中 cutovered:启动目的端完成
        :type migration_cycle: str
        :param connected: 查询失去连接的源端
        :type connected: bool
        :param enterprise_project_id: 需要查询的企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._state = None
        self._name = None
        self._id = None
        self._ip = None
        self._migproject = None
        self._limit = None
        self._offset = None
        self._migration_cycle = None
        self._connected = None
        self._enterprise_project_id = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if migproject is not None:
            self.migproject = migproject
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if migration_cycle is not None:
            self.migration_cycle = migration_cycle
        if connected is not None:
            self.connected = connected
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def state(self):
        """Gets the state of this ListServersRequest.

        源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成

        :return: The state of this ListServersRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListServersRequest.

        源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成

        :param state: The state of this ListServersRequest.
        :type state: str
        """
        self._state = state

    @property
    def name(self):
        """Gets the name of this ListServersRequest.

        源端服务器名称

        :return: The name of this ListServersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListServersRequest.

        源端服务器名称

        :param name: The name of this ListServersRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ListServersRequest.

        源端服务器ID

        :return: The id of this ListServersRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListServersRequest.

        源端服务器ID

        :param id: The id of this ListServersRequest.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        """Gets the ip of this ListServersRequest.

        源端服务器IP地址

        :return: The ip of this ListServersRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListServersRequest.

        源端服务器IP地址

        :param ip: The ip of this ListServersRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def migproject(self):
        """Gets the migproject of this ListServersRequest.

        迁移项目ID，填写该参数将查询迁移项目下的所有虚拟机

        :return: The migproject of this ListServersRequest.
        :rtype: str
        """
        return self._migproject

    @migproject.setter
    def migproject(self, migproject):
        """Sets the migproject of this ListServersRequest.

        迁移项目ID，填写该参数将查询迁移项目下的所有虚拟机

        :param migproject: The migproject of this ListServersRequest.
        :type migproject: str
        """
        self._migproject = migproject

    @property
    def limit(self):
        """Gets the limit of this ListServersRequest.

        每一页记录的源端服务器数量，0表示用默认值 200

        :return: The limit of this ListServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServersRequest.

        每一页记录的源端服务器数量，0表示用默认值 200

        :param limit: The limit of this ListServersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListServersRequest.

        偏移量，默认值0

        :return: The offset of this ListServersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListServersRequest.

        偏移量，默认值0

        :param offset: The offset of this ListServersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def migration_cycle(self):
        """Gets the migration_cycle of this ListServersRequest.

        checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 cutovering:启动目的端中 cutovered:启动目的端完成

        :return: The migration_cycle of this ListServersRequest.
        :rtype: str
        """
        return self._migration_cycle

    @migration_cycle.setter
    def migration_cycle(self, migration_cycle):
        """Sets the migration_cycle of this ListServersRequest.

        checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 cutovering:启动目的端中 cutovered:启动目的端完成

        :param migration_cycle: The migration_cycle of this ListServersRequest.
        :type migration_cycle: str
        """
        self._migration_cycle = migration_cycle

    @property
    def connected(self):
        """Gets the connected of this ListServersRequest.

        查询失去连接的源端

        :return: The connected of this ListServersRequest.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this ListServersRequest.

        查询失去连接的源端

        :param connected: The connected of this ListServersRequest.
        :type connected: bool
        """
        self._connected = connected

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListServersRequest.

        需要查询的企业项目ID

        :return: The enterprise_project_id of this ListServersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListServersRequest.

        需要查询的企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListServersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
