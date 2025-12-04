# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKakfaClusterResponseClusterBrokers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'health': 'bool',
        'host': 'str',
        'port': 'int',
        'broker_id': 'str'
    }

    attribute_map = {
        'health': 'health',
        'host': 'host',
        'port': 'port',
        'broker_id': 'broker_id'
    }

    def __init__(self, health=None, host=None, port=None, broker_id=None):
        r"""ShowKakfaClusterResponseClusterBrokers

        The model defined in huaweicloud sdk

        :param health: **参数解释**： 是否健康。   **取值范围**： - true：健康。 - false：不健康。
        :type health: bool
        :param host: **参数解释**： Host地址。   **取值范围**： 不涉及。
        :type host: str
        :param port: **参数解释**： 端口。   **取值范围**： 不涉及。
        :type port: int
        :param broker_id: **参数解释**： 节点ID。   **取值范围**： 不涉及。
        :type broker_id: str
        """
        
        

        self._health = None
        self._host = None
        self._port = None
        self._broker_id = None
        self.discriminator = None

        if health is not None:
            self.health = health
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if broker_id is not None:
            self.broker_id = broker_id

    @property
    def health(self):
        r"""Gets the health of this ShowKakfaClusterResponseClusterBrokers.

        **参数解释**： 是否健康。   **取值范围**： - true：健康。 - false：不健康。

        :return: The health of this ShowKakfaClusterResponseClusterBrokers.
        :rtype: bool
        """
        return self._health

    @health.setter
    def health(self, health):
        r"""Sets the health of this ShowKakfaClusterResponseClusterBrokers.

        **参数解释**： 是否健康。   **取值范围**： - true：健康。 - false：不健康。

        :param health: The health of this ShowKakfaClusterResponseClusterBrokers.
        :type health: bool
        """
        self._health = health

    @property
    def host(self):
        r"""Gets the host of this ShowKakfaClusterResponseClusterBrokers.

        **参数解释**： Host地址。   **取值范围**： 不涉及。

        :return: The host of this ShowKakfaClusterResponseClusterBrokers.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ShowKakfaClusterResponseClusterBrokers.

        **参数解释**： Host地址。   **取值范围**： 不涉及。

        :param host: The host of this ShowKakfaClusterResponseClusterBrokers.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        r"""Gets the port of this ShowKakfaClusterResponseClusterBrokers.

        **参数解释**： 端口。   **取值范围**： 不涉及。

        :return: The port of this ShowKakfaClusterResponseClusterBrokers.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ShowKakfaClusterResponseClusterBrokers.

        **参数解释**： 端口。   **取值范围**： 不涉及。

        :param port: The port of this ShowKakfaClusterResponseClusterBrokers.
        :type port: int
        """
        self._port = port

    @property
    def broker_id(self):
        r"""Gets the broker_id of this ShowKakfaClusterResponseClusterBrokers.

        **参数解释**： 节点ID。   **取值范围**： 不涉及。

        :return: The broker_id of this ShowKakfaClusterResponseClusterBrokers.
        :rtype: str
        """
        return self._broker_id

    @broker_id.setter
    def broker_id(self, broker_id):
        r"""Sets the broker_id of this ShowKakfaClusterResponseClusterBrokers.

        **参数解释**： 节点ID。   **取值范围**： 不涉及。

        :param broker_id: The broker_id of this ShowKakfaClusterResponseClusterBrokers.
        :type broker_id: str
        """
        self._broker_id = broker_id

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
        if not isinstance(other, ShowKakfaClusterResponseClusterBrokers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
