# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Agent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'agent_id': 'str',
        'agent_version': 'str',
        'agent_type': 'str',
        'host_name': 'str',
        'host_nickname': 'str',
        'host_ip': 'str',
        'host_os': 'str',
        'status': 'str',
        'last_active_time': 'datetime',
        'paths': 'list[Path]'
    }

    attribute_map = {
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'agent_id': 'agent_id',
        'agent_version': 'agent_version',
        'agent_type': 'agent_type',
        'host_name': 'host_name',
        'host_nickname': 'host_nickname',
        'host_ip': 'host_ip',
        'host_os': 'host_os',
        'status': 'status',
        'last_active_time': 'last_active_time',
        'paths': 'paths'
    }

    def __init__(self, created_at=None, updated_at=None, agent_id=None, agent_version=None, agent_type=None, host_name=None, host_nickname=None, host_ip=None, host_os=None, status=None, last_active_time=None, paths=None):
        """Agent

        The model defined in huaweicloud sdk

        :param created_at: 客户端创建时间
        :type created_at: datetime
        :param updated_at: 客户端更新时间
        :type updated_at: datetime
        :param agent_id: 客户端ID
        :type agent_id: str
        :param agent_version: 客户端版本号
        :type agent_version: str
        :param agent_type: 客户端类型
        :type agent_type: str
        :param host_name: 客户端所在的主机名
        :type host_name: str
        :param host_nickname: 客户端所在的主机昵称
        :type host_nickname: str
        :param host_ip: 客户端所在主机的IP
        :type host_ip: str
        :param host_os: 客户端主机所在的操作系统
        :type host_os: str
        :param status: 客户端状态
        :type status: str
        :param last_active_time: 客户端上次激活时间
        :type last_active_time: datetime
        :param paths: 客户端的备份路径
        :type paths: list[:class:`huaweicloudsdkcbr.v1.Path`]
        """
        
        

        self._created_at = None
        self._updated_at = None
        self._agent_id = None
        self._agent_version = None
        self._agent_type = None
        self._host_name = None
        self._host_nickname = None
        self._host_ip = None
        self._host_os = None
        self._status = None
        self._last_active_time = None
        self._paths = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.agent_id = agent_id
        if agent_version is not None:
            self.agent_version = agent_version
        if agent_type is not None:
            self.agent_type = agent_type
        if host_name is not None:
            self.host_name = host_name
        if host_nickname is not None:
            self.host_nickname = host_nickname
        if host_ip is not None:
            self.host_ip = host_ip
        if host_os is not None:
            self.host_os = host_os
        if status is not None:
            self.status = status
        if last_active_time is not None:
            self.last_active_time = last_active_time
        if paths is not None:
            self.paths = paths

    @property
    def created_at(self):
        """Gets the created_at of this Agent.

        客户端创建时间

        :return: The created_at of this Agent.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Agent.

        客户端创建时间

        :param created_at: The created_at of this Agent.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Agent.

        客户端更新时间

        :return: The updated_at of this Agent.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Agent.

        客户端更新时间

        :param updated_at: The updated_at of this Agent.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def agent_id(self):
        """Gets the agent_id of this Agent.

        客户端ID

        :return: The agent_id of this Agent.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this Agent.

        客户端ID

        :param agent_id: The agent_id of this Agent.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_version(self):
        """Gets the agent_version of this Agent.

        客户端版本号

        :return: The agent_version of this Agent.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this Agent.

        客户端版本号

        :param agent_version: The agent_version of this Agent.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def agent_type(self):
        """Gets the agent_type of this Agent.

        客户端类型

        :return: The agent_type of this Agent.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """Sets the agent_type of this Agent.

        客户端类型

        :param agent_type: The agent_type of this Agent.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def host_name(self):
        """Gets the host_name of this Agent.

        客户端所在的主机名

        :return: The host_name of this Agent.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this Agent.

        客户端所在的主机名

        :param host_name: The host_name of this Agent.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_nickname(self):
        """Gets the host_nickname of this Agent.

        客户端所在的主机昵称

        :return: The host_nickname of this Agent.
        :rtype: str
        """
        return self._host_nickname

    @host_nickname.setter
    def host_nickname(self, host_nickname):
        """Sets the host_nickname of this Agent.

        客户端所在的主机昵称

        :param host_nickname: The host_nickname of this Agent.
        :type host_nickname: str
        """
        self._host_nickname = host_nickname

    @property
    def host_ip(self):
        """Gets the host_ip of this Agent.

        客户端所在主机的IP

        :return: The host_ip of this Agent.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this Agent.

        客户端所在主机的IP

        :param host_ip: The host_ip of this Agent.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_os(self):
        """Gets the host_os of this Agent.

        客户端主机所在的操作系统

        :return: The host_os of this Agent.
        :rtype: str
        """
        return self._host_os

    @host_os.setter
    def host_os(self, host_os):
        """Sets the host_os of this Agent.

        客户端主机所在的操作系统

        :param host_os: The host_os of this Agent.
        :type host_os: str
        """
        self._host_os = host_os

    @property
    def status(self):
        """Gets the status of this Agent.

        客户端状态

        :return: The status of this Agent.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Agent.

        客户端状态

        :param status: The status of this Agent.
        :type status: str
        """
        self._status = status

    @property
    def last_active_time(self):
        """Gets the last_active_time of this Agent.

        客户端上次激活时间

        :return: The last_active_time of this Agent.
        :rtype: datetime
        """
        return self._last_active_time

    @last_active_time.setter
    def last_active_time(self, last_active_time):
        """Sets the last_active_time of this Agent.

        客户端上次激活时间

        :param last_active_time: The last_active_time of this Agent.
        :type last_active_time: datetime
        """
        self._last_active_time = last_active_time

    @property
    def paths(self):
        """Gets the paths of this Agent.

        客户端的备份路径

        :return: The paths of this Agent.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.Path`]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this Agent.

        客户端的备份路径

        :param paths: The paths of this Agent.
        :type paths: list[:class:`huaweicloudsdkcbr.v1.Path`]
        """
        self._paths = paths

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
        if not isinstance(other, Agent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
