# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class L7Limit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection': 'int',
        'cps': 'int'
    }

    attribute_map = {
        'connection': 'connection',
        'cps': 'cps'
    }

    def __init__(self, connection=None, cps=None):
        r"""L7Limit

        The model defined in huaweicloud sdk

        :param connection: **参数解释**：负载均衡实例的七层规格的最大并发连接数限速值。  **取值范围**：不涉及
        :type connection: int
        :param cps: **参数解释**：负载均衡实例的七层规格的每秒新建连接数限速值。  **取值范围**：不涉及
        :type cps: int
        """
        
        

        self._connection = None
        self._cps = None
        self.discriminator = None

        if connection is not None:
            self.connection = connection
        if cps is not None:
            self.cps = cps

    @property
    def connection(self):
        r"""Gets the connection of this L7Limit.

        **参数解释**：负载均衡实例的七层规格的最大并发连接数限速值。  **取值范围**：不涉及

        :return: The connection of this L7Limit.
        :rtype: int
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this L7Limit.

        **参数解释**：负载均衡实例的七层规格的最大并发连接数限速值。  **取值范围**：不涉及

        :param connection: The connection of this L7Limit.
        :type connection: int
        """
        self._connection = connection

    @property
    def cps(self):
        r"""Gets the cps of this L7Limit.

        **参数解释**：负载均衡实例的七层规格的每秒新建连接数限速值。  **取值范围**：不涉及

        :return: The cps of this L7Limit.
        :rtype: int
        """
        return self._cps

    @cps.setter
    def cps(self, cps):
        r"""Sets the cps of this L7Limit.

        **参数解释**：负载均衡实例的七层规格的每秒新建连接数限速值。  **取值范围**：不涉及

        :param cps: The cps of this L7Limit.
        :type cps: int
        """
        self._cps = cps

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
        if not isinstance(other, L7Limit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
