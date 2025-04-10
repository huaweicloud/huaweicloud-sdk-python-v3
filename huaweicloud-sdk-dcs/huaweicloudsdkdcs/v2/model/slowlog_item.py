# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowlogItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'command': 'str',
        'start_time': 'str',
        'duration': 'str',
        'shard_name': 'str',
        'database_id': 'int',
        'username': 'str',
        'node_role': 'str',
        'client_ip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'command': 'command',
        'start_time': 'start_time',
        'duration': 'duration',
        'shard_name': 'shard_name',
        'database_id': 'database_id',
        'username': 'username',
        'node_role': 'node_role',
        'client_ip': 'client_ip'
    }

    def __init__(self, id=None, command=None, start_time=None, duration=None, shard_name=None, database_id=None, username=None, node_role=None, client_ip=None):
        r"""SlowlogItem

        The model defined in huaweicloud sdk

        :param id: 慢日志的唯一标识
        :type id: int
        :param command: 慢命令
        :type command: str
        :param start_time: 执行开始时间,格式为“2020-06-19T07:06:07Z”
        :type start_time: str
        :param duration: 持续时间，单位是ms
        :type duration: str
        :param shard_name: 慢命令所在的分片名称，仅在实例类型为集群时支持
        :type shard_name: str
        :param database_id: 数据库id，当前只对指定客户开放
        :type database_id: int
        :param username: 操作慢日志的账号名称，当前只对指定客户开放
        :type username: str
        :param node_role: **参数解释**： 节点类型。 **取值范围**： 不涉及。 
        :type node_role: str
        :param client_ip: **参数解释**： 客户端IP地址。 **取值范围**： 不涉及。 
        :type client_ip: str
        """
        
        

        self._id = None
        self._command = None
        self._start_time = None
        self._duration = None
        self._shard_name = None
        self._database_id = None
        self._username = None
        self._node_role = None
        self._client_ip = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if command is not None:
            self.command = command
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if shard_name is not None:
            self.shard_name = shard_name
        if database_id is not None:
            self.database_id = database_id
        if username is not None:
            self.username = username
        if node_role is not None:
            self.node_role = node_role
        if client_ip is not None:
            self.client_ip = client_ip

    @property
    def id(self):
        r"""Gets the id of this SlowlogItem.

        慢日志的唯一标识

        :return: The id of this SlowlogItem.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SlowlogItem.

        慢日志的唯一标识

        :param id: The id of this SlowlogItem.
        :type id: int
        """
        self._id = id

    @property
    def command(self):
        r"""Gets the command of this SlowlogItem.

        慢命令

        :return: The command of this SlowlogItem.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this SlowlogItem.

        慢命令

        :param command: The command of this SlowlogItem.
        :type command: str
        """
        self._command = command

    @property
    def start_time(self):
        r"""Gets the start_time of this SlowlogItem.

        执行开始时间,格式为“2020-06-19T07:06:07Z”

        :return: The start_time of this SlowlogItem.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SlowlogItem.

        执行开始时间,格式为“2020-06-19T07:06:07Z”

        :param start_time: The start_time of this SlowlogItem.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def duration(self):
        r"""Gets the duration of this SlowlogItem.

        持续时间，单位是ms

        :return: The duration of this SlowlogItem.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this SlowlogItem.

        持续时间，单位是ms

        :param duration: The duration of this SlowlogItem.
        :type duration: str
        """
        self._duration = duration

    @property
    def shard_name(self):
        r"""Gets the shard_name of this SlowlogItem.

        慢命令所在的分片名称，仅在实例类型为集群时支持

        :return: The shard_name of this SlowlogItem.
        :rtype: str
        """
        return self._shard_name

    @shard_name.setter
    def shard_name(self, shard_name):
        r"""Sets the shard_name of this SlowlogItem.

        慢命令所在的分片名称，仅在实例类型为集群时支持

        :param shard_name: The shard_name of this SlowlogItem.
        :type shard_name: str
        """
        self._shard_name = shard_name

    @property
    def database_id(self):
        r"""Gets the database_id of this SlowlogItem.

        数据库id，当前只对指定客户开放

        :return: The database_id of this SlowlogItem.
        :rtype: int
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        r"""Sets the database_id of this SlowlogItem.

        数据库id，当前只对指定客户开放

        :param database_id: The database_id of this SlowlogItem.
        :type database_id: int
        """
        self._database_id = database_id

    @property
    def username(self):
        r"""Gets the username of this SlowlogItem.

        操作慢日志的账号名称，当前只对指定客户开放

        :return: The username of this SlowlogItem.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this SlowlogItem.

        操作慢日志的账号名称，当前只对指定客户开放

        :param username: The username of this SlowlogItem.
        :type username: str
        """
        self._username = username

    @property
    def node_role(self):
        r"""Gets the node_role of this SlowlogItem.

        **参数解释**： 节点类型。 **取值范围**： 不涉及。 

        :return: The node_role of this SlowlogItem.
        :rtype: str
        """
        return self._node_role

    @node_role.setter
    def node_role(self, node_role):
        r"""Sets the node_role of this SlowlogItem.

        **参数解释**： 节点类型。 **取值范围**： 不涉及。 

        :param node_role: The node_role of this SlowlogItem.
        :type node_role: str
        """
        self._node_role = node_role

    @property
    def client_ip(self):
        r"""Gets the client_ip of this SlowlogItem.

        **参数解释**： 客户端IP地址。 **取值范围**： 不涉及。 

        :return: The client_ip of this SlowlogItem.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this SlowlogItem.

        **参数解释**： 客户端IP地址。 **取值范围**： 不涉及。 

        :param client_ip: The client_ip of this SlowlogItem.
        :type client_ip: str
        """
        self._client_ip = client_ip

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
        if not isinstance(other, SlowlogItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
