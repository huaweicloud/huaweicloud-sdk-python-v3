# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentRegister:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'host_os': 'str',
        'host_nickname': 'str',
        'agent_version': 'str',
        'agent_type': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'host_os': 'host_os',
        'host_nickname': 'host_nickname',
        'agent_version': 'agent_version',
        'agent_type': 'agent_type'
    }

    def __init__(self, agent_id=None, host_name=None, host_ip=None, host_os=None, host_nickname=None, agent_version=None, agent_type=None):
        """AgentRegister

        The model defined in huaweicloud sdk

        :param agent_id: 客户端ID
        :type agent_id: str
        :param host_name: 客户端所在的主机名
        :type host_name: str
        :param host_ip: 客户端所在主机的IP
        :type host_ip: str
        :param host_os: 客户端所在主机的操作系统
        :type host_os: str
        :param host_nickname: 客户端所在主机的主机别名
        :type host_nickname: str
        :param agent_version: 客户端版本
        :type agent_version: str
        :param agent_type: 客户端类型，分本地客户端和云上客户端(cloud/native)
        :type agent_type: str
        """
        
        

        self._agent_id = None
        self._host_name = None
        self._host_ip = None
        self._host_os = None
        self._host_nickname = None
        self._agent_version = None
        self._agent_type = None
        self.discriminator = None

        self.agent_id = agent_id
        self.host_name = host_name
        self.host_ip = host_ip
        self.host_os = host_os
        if host_nickname is not None:
            self.host_nickname = host_nickname
        if agent_version is not None:
            self.agent_version = agent_version
        if agent_type is not None:
            self.agent_type = agent_type

    @property
    def agent_id(self):
        """Gets the agent_id of this AgentRegister.

        客户端ID

        :return: The agent_id of this AgentRegister.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this AgentRegister.

        客户端ID

        :param agent_id: The agent_id of this AgentRegister.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_name(self):
        """Gets the host_name of this AgentRegister.

        客户端所在的主机名

        :return: The host_name of this AgentRegister.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this AgentRegister.

        客户端所在的主机名

        :param host_name: The host_name of this AgentRegister.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this AgentRegister.

        客户端所在主机的IP

        :return: The host_ip of this AgentRegister.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this AgentRegister.

        客户端所在主机的IP

        :param host_ip: The host_ip of this AgentRegister.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_os(self):
        """Gets the host_os of this AgentRegister.

        客户端所在主机的操作系统

        :return: The host_os of this AgentRegister.
        :rtype: str
        """
        return self._host_os

    @host_os.setter
    def host_os(self, host_os):
        """Sets the host_os of this AgentRegister.

        客户端所在主机的操作系统

        :param host_os: The host_os of this AgentRegister.
        :type host_os: str
        """
        self._host_os = host_os

    @property
    def host_nickname(self):
        """Gets the host_nickname of this AgentRegister.

        客户端所在主机的主机别名

        :return: The host_nickname of this AgentRegister.
        :rtype: str
        """
        return self._host_nickname

    @host_nickname.setter
    def host_nickname(self, host_nickname):
        """Sets the host_nickname of this AgentRegister.

        客户端所在主机的主机别名

        :param host_nickname: The host_nickname of this AgentRegister.
        :type host_nickname: str
        """
        self._host_nickname = host_nickname

    @property
    def agent_version(self):
        """Gets the agent_version of this AgentRegister.

        客户端版本

        :return: The agent_version of this AgentRegister.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this AgentRegister.

        客户端版本

        :param agent_version: The agent_version of this AgentRegister.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def agent_type(self):
        """Gets the agent_type of this AgentRegister.

        客户端类型，分本地客户端和云上客户端(cloud/native)

        :return: The agent_type of this AgentRegister.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """Sets the agent_type of this AgentRegister.

        客户端类型，分本地客户端和云上客户端(cloud/native)

        :param agent_type: The agent_type of this AgentRegister.
        :type agent_type: str
        """
        self._agent_type = agent_type

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
        if not isinstance(other, AgentRegister):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
