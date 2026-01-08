# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListenerNode:

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
        'name': 'str',
        'protocol': 'str',
        'protocol_port': 'int',
        'port_ranges': 'list[PortRange]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'protocol': 'protocol',
        'protocol_port': 'protocol_port',
        'port_ranges': 'port_ranges'
    }

    def __init__(self, id=None, name=None, protocol=None, protocol_port=None, port_ranges=None):
        r"""ListenerNode

        The model defined in huaweicloud sdk

        :param id: **参数解释**：监听器id。  **取值范围**：不涉及
        :type id: str
        :param name: **参数解释**：监听器名称。  **取值范围**：不涉及
        :type name: str
        :param protocol: **参数解释**：监听器协议。  **取值范围**：不涉及
        :type protocol: str
        :param protocol_port: **参数解释**：监听器监听端口。  **取值范围**：不涉及
        :type protocol_port: int
        :param port_ranges: **参数解释**：全端口监听，指定端口监听范围（闭区间)，最多指定10个端口组，每个组范围不可有重叠部分 &gt;仅当protocol_port为0时可以传入。
        :type port_ranges: list[:class:`huaweicloudsdkelb.v3.PortRange`]
        """
        
        

        self._id = None
        self._name = None
        self._protocol = None
        self._protocol_port = None
        self._port_ranges = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.protocol = protocol
        self.protocol_port = protocol_port
        if port_ranges is not None:
            self.port_ranges = port_ranges

    @property
    def id(self):
        r"""Gets the id of this ListenerNode.

        **参数解释**：监听器id。  **取值范围**：不涉及

        :return: The id of this ListenerNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListenerNode.

        **参数解释**：监听器id。  **取值范围**：不涉及

        :param id: The id of this ListenerNode.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListenerNode.

        **参数解释**：监听器名称。  **取值范围**：不涉及

        :return: The name of this ListenerNode.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListenerNode.

        **参数解释**：监听器名称。  **取值范围**：不涉及

        :param name: The name of this ListenerNode.
        :type name: str
        """
        self._name = name

    @property
    def protocol(self):
        r"""Gets the protocol of this ListenerNode.

        **参数解释**：监听器协议。  **取值范围**：不涉及

        :return: The protocol of this ListenerNode.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ListenerNode.

        **参数解释**：监听器协议。  **取值范围**：不涉及

        :param protocol: The protocol of this ListenerNode.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this ListenerNode.

        **参数解释**：监听器监听端口。  **取值范围**：不涉及

        :return: The protocol_port of this ListenerNode.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this ListenerNode.

        **参数解释**：监听器监听端口。  **取值范围**：不涉及

        :param protocol_port: The protocol_port of this ListenerNode.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def port_ranges(self):
        r"""Gets the port_ranges of this ListenerNode.

        **参数解释**：全端口监听，指定端口监听范围（闭区间)，最多指定10个端口组，每个组范围不可有重叠部分 >仅当protocol_port为0时可以传入。

        :return: The port_ranges of this ListenerNode.
        :rtype: list[:class:`huaweicloudsdkelb.v3.PortRange`]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        r"""Sets the port_ranges of this ListenerNode.

        **参数解释**：全端口监听，指定端口监听范围（闭区间)，最多指定10个端口组，每个组范围不可有重叠部分 >仅当protocol_port为0时可以传入。

        :param port_ranges: The port_ranges of this ListenerNode.
        :type port_ranges: list[:class:`huaweicloudsdkelb.v3.PortRange`]
        """
        self._port_ranges = port_ranges

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
        if not isinstance(other, ListenerNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
