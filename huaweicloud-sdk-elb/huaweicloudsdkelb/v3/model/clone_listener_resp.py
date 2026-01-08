# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloneListenerResp:

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
        'loadbalancer_id': 'str',
        'protocol_port': 'int',
        'port_ranges': 'list[ResPortRange]'
    }

    attribute_map = {
        'id': 'id',
        'loadbalancer_id': 'loadbalancer_id',
        'protocol_port': 'protocol_port',
        'port_ranges': 'port_ranges'
    }

    def __init__(self, id=None, loadbalancer_id=None, protocol_port=None, port_ranges=None):
        r"""CloneListenerResp

        The model defined in huaweicloud sdk

        :param id: **参数解释**：新监听器ID。 **取值范围**：标准的UUID格式，长度为36个字符。
        :type id: str
        :param loadbalancer_id: **参数解释**：目的负载均衡器ID。 **取值范围**：标准的UUID格式，长度为36个字符。
        :type loadbalancer_id: str
        :param protocol_port: **参数解释**：新监听器监听端口。 **取值范围**：1-65535
        :type protocol_port: int
        :param port_ranges: **参数解释**：端口监听范围（闭区间)。
        :type port_ranges: list[:class:`huaweicloudsdkelb.v3.ResPortRange`]
        """
        
        

        self._id = None
        self._loadbalancer_id = None
        self._protocol_port = None
        self._port_ranges = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if port_ranges is not None:
            self.port_ranges = port_ranges

    @property
    def id(self):
        r"""Gets the id of this CloneListenerResp.

        **参数解释**：新监听器ID。 **取值范围**：标准的UUID格式，长度为36个字符。

        :return: The id of this CloneListenerResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CloneListenerResp.

        **参数解释**：新监听器ID。 **取值范围**：标准的UUID格式，长度为36个字符。

        :param id: The id of this CloneListenerResp.
        :type id: str
        """
        self._id = id

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this CloneListenerResp.

        **参数解释**：目的负载均衡器ID。 **取值范围**：标准的UUID格式，长度为36个字符。

        :return: The loadbalancer_id of this CloneListenerResp.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this CloneListenerResp.

        **参数解释**：目的负载均衡器ID。 **取值范围**：标准的UUID格式，长度为36个字符。

        :param loadbalancer_id: The loadbalancer_id of this CloneListenerResp.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this CloneListenerResp.

        **参数解释**：新监听器监听端口。 **取值范围**：1-65535

        :return: The protocol_port of this CloneListenerResp.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this CloneListenerResp.

        **参数解释**：新监听器监听端口。 **取值范围**：1-65535

        :param protocol_port: The protocol_port of this CloneListenerResp.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def port_ranges(self):
        r"""Gets the port_ranges of this CloneListenerResp.

        **参数解释**：端口监听范围（闭区间)。

        :return: The port_ranges of this CloneListenerResp.
        :rtype: list[:class:`huaweicloudsdkelb.v3.ResPortRange`]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        r"""Sets the port_ranges of this CloneListenerResp.

        **参数解释**：端口监听范围（闭区间)。

        :param port_ranges: The port_ranges of this CloneListenerResp.
        :type port_ranges: list[:class:`huaweicloudsdkelb.v3.ResPortRange`]
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
        if not isinstance(other, CloneListenerResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
