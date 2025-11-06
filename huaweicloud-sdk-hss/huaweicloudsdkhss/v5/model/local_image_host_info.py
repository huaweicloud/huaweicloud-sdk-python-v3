# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LocalImageHostInfo:

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
        'agent_status': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'version': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'docker_name': 'str',
        'docker_type': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'agent_status': 'agent_status',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'version': 'version',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'docker_name': 'docker_name',
        'docker_type': 'docker_type'
    }

    def __init__(self, agent_id=None, agent_status=None, host_name=None, host_id=None, version=None, private_ip=None, public_ip=None, docker_name=None, docker_type=None):
        r"""LocalImageHostInfo

        The model defined in huaweicloud sdk

        :param agent_id: Agent ID
        :type agent_id: str
        :param agent_status: agent_status
        :type agent_status: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 服务器ID
        :type host_id: str
        :param version: 服务器开通的版本
        :type version: str
        :param private_ip: 私有IP地址
        :type private_ip: str
        :param public_ip: 弹性公网IP地址
        :type public_ip: str
        :param docker_name: docker名称
        :type docker_name: str
        :param docker_type: docker类型
        :type docker_type: str
        """
        
        

        self._agent_id = None
        self._agent_status = None
        self._host_name = None
        self._host_id = None
        self._version = None
        self._private_ip = None
        self._public_ip = None
        self._docker_name = None
        self._docker_type = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if agent_status is not None:
            self.agent_status = agent_status
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if version is not None:
            self.version = version
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if docker_name is not None:
            self.docker_name = docker_name
        if docker_type is not None:
            self.docker_type = docker_type

    @property
    def agent_id(self):
        r"""Gets the agent_id of this LocalImageHostInfo.

        Agent ID

        :return: The agent_id of this LocalImageHostInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this LocalImageHostInfo.

        Agent ID

        :param agent_id: The agent_id of this LocalImageHostInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_status(self):
        r"""Gets the agent_status of this LocalImageHostInfo.

        agent_status

        :return: The agent_status of this LocalImageHostInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this LocalImageHostInfo.

        agent_status

        :param agent_status: The agent_status of this LocalImageHostInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def host_name(self):
        r"""Gets the host_name of this LocalImageHostInfo.

        服务器名称

        :return: The host_name of this LocalImageHostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this LocalImageHostInfo.

        服务器名称

        :param host_name: The host_name of this LocalImageHostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this LocalImageHostInfo.

        服务器ID

        :return: The host_id of this LocalImageHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this LocalImageHostInfo.

        服务器ID

        :param host_id: The host_id of this LocalImageHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def version(self):
        r"""Gets the version of this LocalImageHostInfo.

        服务器开通的版本

        :return: The version of this LocalImageHostInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this LocalImageHostInfo.

        服务器开通的版本

        :param version: The version of this LocalImageHostInfo.
        :type version: str
        """
        self._version = version

    @property
    def private_ip(self):
        r"""Gets the private_ip of this LocalImageHostInfo.

        私有IP地址

        :return: The private_ip of this LocalImageHostInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this LocalImageHostInfo.

        私有IP地址

        :param private_ip: The private_ip of this LocalImageHostInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this LocalImageHostInfo.

        弹性公网IP地址

        :return: The public_ip of this LocalImageHostInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this LocalImageHostInfo.

        弹性公网IP地址

        :param public_ip: The public_ip of this LocalImageHostInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def docker_name(self):
        r"""Gets the docker_name of this LocalImageHostInfo.

        docker名称

        :return: The docker_name of this LocalImageHostInfo.
        :rtype: str
        """
        return self._docker_name

    @docker_name.setter
    def docker_name(self, docker_name):
        r"""Sets the docker_name of this LocalImageHostInfo.

        docker名称

        :param docker_name: The docker_name of this LocalImageHostInfo.
        :type docker_name: str
        """
        self._docker_name = docker_name

    @property
    def docker_type(self):
        r"""Gets the docker_type of this LocalImageHostInfo.

        docker类型

        :return: The docker_type of this LocalImageHostInfo.
        :rtype: str
        """
        return self._docker_type

    @docker_type.setter
    def docker_type(self, docker_type):
        r"""Sets the docker_type of this LocalImageHostInfo.

        docker类型

        :param docker_type: The docker_type of this LocalImageHostInfo.
        :type docker_type: str
        """
        self._docker_type = docker_type

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
        if not isinstance(other, LocalImageHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
