# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortStatusRequestInfo:

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
        'port': 'int',
        'port_type': 'str',
        'container_id': 'str',
        'host_id': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'port': 'port',
        'port_type': 'port_type',
        'container_id': 'container_id',
        'host_id': 'host_id'
    }

    def __init__(self, agent_id=None, port=None, port_type=None, container_id=None, host_id=None):
        r"""PortStatusRequestInfo

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释**: agent id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 
        :type agent_id: str
        :param port: **参数解释**: 本地端口号 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2147483647 **默认取值**: 不涉及 
        :type port: int
        :param port_type: **参数解释**: 端口类型 **约束限制**: 不涉及 **取值范围**: - TCP - UDP  **默认取值**: 不涉及 
        :type port_type: str
        :param container_id: **参数解释**: 容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 
        :type container_id: str
        :param host_id: **参数解释**: 主机id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 
        :type host_id: str
        """
        
        

        self._agent_id = None
        self._port = None
        self._port_type = None
        self._container_id = None
        self._host_id = None
        self.discriminator = None

        self.agent_id = agent_id
        self.port = port
        self.port_type = port_type
        if container_id is not None:
            self.container_id = container_id
        if host_id is not None:
            self.host_id = host_id

    @property
    def agent_id(self):
        r"""Gets the agent_id of this PortStatusRequestInfo.

        **参数解释**: agent id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 

        :return: The agent_id of this PortStatusRequestInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this PortStatusRequestInfo.

        **参数解释**: agent id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this PortStatusRequestInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def port(self):
        r"""Gets the port of this PortStatusRequestInfo.

        **参数解释**: 本地端口号 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2147483647 **默认取值**: 不涉及 

        :return: The port of this PortStatusRequestInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this PortStatusRequestInfo.

        **参数解释**: 本地端口号 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2147483647 **默认取值**: 不涉及 

        :param port: The port of this PortStatusRequestInfo.
        :type port: int
        """
        self._port = port

    @property
    def port_type(self):
        r"""Gets the port_type of this PortStatusRequestInfo.

        **参数解释**: 端口类型 **约束限制**: 不涉及 **取值范围**: - TCP - UDP  **默认取值**: 不涉及 

        :return: The port_type of this PortStatusRequestInfo.
        :rtype: str
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        r"""Sets the port_type of this PortStatusRequestInfo.

        **参数解释**: 端口类型 **约束限制**: 不涉及 **取值范围**: - TCP - UDP  **默认取值**: 不涉及 

        :param port_type: The port_type of this PortStatusRequestInfo.
        :type port_type: str
        """
        self._port_type = port_type

    @property
    def container_id(self):
        r"""Gets the container_id of this PortStatusRequestInfo.

        **参数解释**: 容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 

        :return: The container_id of this PortStatusRequestInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this PortStatusRequestInfo.

        **参数解释**: 容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 

        :param container_id: The container_id of this PortStatusRequestInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def host_id(self):
        r"""Gets the host_id of this PortStatusRequestInfo.

        **参数解释**: 主机id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 

        :return: The host_id of this PortStatusRequestInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this PortStatusRequestInfo.

        **参数解释**: 主机id **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this PortStatusRequestInfo.
        :type host_id: str
        """
        self._host_id = host_id

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
        if not isinstance(other, PortStatusRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
