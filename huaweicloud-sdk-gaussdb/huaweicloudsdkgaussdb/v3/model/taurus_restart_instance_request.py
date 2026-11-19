# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaurusRestartInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delay': 'bool',
        'max_connections': 'int'
    }

    attribute_map = {
        'delay': 'delay',
        'max_connections': 'max_connections'
    }

    def __init__(self, delay=None, max_connections=None):
        r"""TaurusRestartInstanceRequest

        The model defined in huaweicloud sdk

        :param delay: 实例是否延迟重启，默认false，立即重启。  - true: 延迟重启，实例将在运维时间窗内自动重启。 - false: 立即重启。
        :type delay: bool
        :param max_connections: **参数解释**：  实例重启后生效的max_connections内核参数配置值。max_connections用于设置允许同时连接到数据库实例的最大客户端连接数。  **约束限制**：  不涉及。  **取值范围**： 30-100000。  **默认取值**： 不涉及。
        :type max_connections: int
        """
        
        

        self._delay = None
        self._max_connections = None
        self.discriminator = None

        if delay is not None:
            self.delay = delay
        if max_connections is not None:
            self.max_connections = max_connections

    @property
    def delay(self):
        r"""Gets the delay of this TaurusRestartInstanceRequest.

        实例是否延迟重启，默认false，立即重启。  - true: 延迟重启，实例将在运维时间窗内自动重启。 - false: 立即重启。

        :return: The delay of this TaurusRestartInstanceRequest.
        :rtype: bool
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this TaurusRestartInstanceRequest.

        实例是否延迟重启，默认false，立即重启。  - true: 延迟重启，实例将在运维时间窗内自动重启。 - false: 立即重启。

        :param delay: The delay of this TaurusRestartInstanceRequest.
        :type delay: bool
        """
        self._delay = delay

    @property
    def max_connections(self):
        r"""Gets the max_connections of this TaurusRestartInstanceRequest.

        **参数解释**：  实例重启后生效的max_connections内核参数配置值。max_connections用于设置允许同时连接到数据库实例的最大客户端连接数。  **约束限制**：  不涉及。  **取值范围**： 30-100000。  **默认取值**： 不涉及。

        :return: The max_connections of this TaurusRestartInstanceRequest.
        :rtype: int
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        r"""Sets the max_connections of this TaurusRestartInstanceRequest.

        **参数解释**：  实例重启后生效的max_connections内核参数配置值。max_connections用于设置允许同时连接到数据库实例的最大客户端连接数。  **约束限制**：  不涉及。  **取值范围**： 30-100000。  **默认取值**： 不涉及。

        :param max_connections: The max_connections of this TaurusRestartInstanceRequest.
        :type max_connections: int
        """
        self._max_connections = max_connections

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
        if not isinstance(other, TaurusRestartInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
