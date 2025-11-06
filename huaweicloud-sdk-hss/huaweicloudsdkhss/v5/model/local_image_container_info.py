# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LocalImageContainerInfo:

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
        'container_name': 'str',
        'container_id': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'pod_id': 'str',
        'pod_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'entry_point': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'container_name': 'container_name',
        'container_id': 'container_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'pod_id': 'pod_id',
        'pod_name': 'pod_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'entry_point': 'entry_point'
    }

    def __init__(self, agent_id=None, container_name=None, container_id=None, host_id=None, host_name=None, pod_id=None, pod_name=None, private_ip=None, public_ip=None, entry_point=None):
        r"""LocalImageContainerInfo

        The model defined in huaweicloud sdk

        :param agent_id: Agent id
        :type agent_id: str
        :param container_name: 容器名称
        :type container_name: str
        :param container_id: 容器ID
        :type container_id: str
        :param host_id: 服务器ID
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param pod_id: pod id
        :type pod_id: str
        :param pod_name: pod名称
        :type pod_name: str
        :param private_ip: 私有IP地址
        :type private_ip: str
        :param public_ip: 弹性公网IP地址
        :type public_ip: str
        :param entry_point: 启动命令
        :type entry_point: str
        """
        
        

        self._agent_id = None
        self._container_name = None
        self._container_id = None
        self._host_id = None
        self._host_name = None
        self._pod_id = None
        self._pod_name = None
        self._private_ip = None
        self._public_ip = None
        self._entry_point = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if container_name is not None:
            self.container_name = container_name
        if container_id is not None:
            self.container_id = container_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if pod_id is not None:
            self.pod_id = pod_id
        if pod_name is not None:
            self.pod_name = pod_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if entry_point is not None:
            self.entry_point = entry_point

    @property
    def agent_id(self):
        r"""Gets the agent_id of this LocalImageContainerInfo.

        Agent id

        :return: The agent_id of this LocalImageContainerInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this LocalImageContainerInfo.

        Agent id

        :param agent_id: The agent_id of this LocalImageContainerInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def container_name(self):
        r"""Gets the container_name of this LocalImageContainerInfo.

        容器名称

        :return: The container_name of this LocalImageContainerInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this LocalImageContainerInfo.

        容器名称

        :param container_name: The container_name of this LocalImageContainerInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_id(self):
        r"""Gets the container_id of this LocalImageContainerInfo.

        容器ID

        :return: The container_id of this LocalImageContainerInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this LocalImageContainerInfo.

        容器ID

        :param container_id: The container_id of this LocalImageContainerInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def host_id(self):
        r"""Gets the host_id of this LocalImageContainerInfo.

        服务器ID

        :return: The host_id of this LocalImageContainerInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this LocalImageContainerInfo.

        服务器ID

        :param host_id: The host_id of this LocalImageContainerInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this LocalImageContainerInfo.

        服务器名称

        :return: The host_name of this LocalImageContainerInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this LocalImageContainerInfo.

        服务器名称

        :param host_name: The host_name of this LocalImageContainerInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def pod_id(self):
        r"""Gets the pod_id of this LocalImageContainerInfo.

        pod id

        :return: The pod_id of this LocalImageContainerInfo.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        r"""Sets the pod_id of this LocalImageContainerInfo.

        pod id

        :param pod_id: The pod_id of this LocalImageContainerInfo.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def pod_name(self):
        r"""Gets the pod_name of this LocalImageContainerInfo.

        pod名称

        :return: The pod_name of this LocalImageContainerInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this LocalImageContainerInfo.

        pod名称

        :param pod_name: The pod_name of this LocalImageContainerInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this LocalImageContainerInfo.

        私有IP地址

        :return: The private_ip of this LocalImageContainerInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this LocalImageContainerInfo.

        私有IP地址

        :param private_ip: The private_ip of this LocalImageContainerInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this LocalImageContainerInfo.

        弹性公网IP地址

        :return: The public_ip of this LocalImageContainerInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this LocalImageContainerInfo.

        弹性公网IP地址

        :param public_ip: The public_ip of this LocalImageContainerInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def entry_point(self):
        r"""Gets the entry_point of this LocalImageContainerInfo.

        启动命令

        :return: The entry_point of this LocalImageContainerInfo.
        :rtype: str
        """
        return self._entry_point

    @entry_point.setter
    def entry_point(self, entry_point):
        r"""Sets the entry_point of this LocalImageContainerInfo.

        启动命令

        :param entry_point: The entry_point of this LocalImageContainerInfo.
        :type entry_point: str
        """
        self._entry_point = entry_point

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
        if not isinstance(other, LocalImageContainerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
