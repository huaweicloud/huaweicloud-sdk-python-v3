# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OneResourceGroupRespResourceStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unhealthy': 'int',
        'total': 'int',
        'event_unhealthy': 'int',
        'namespaces': 'int'
    }

    attribute_map = {
        'unhealthy': 'unhealthy',
        'total': 'total',
        'event_unhealthy': 'event_unhealthy',
        'namespaces': 'namespaces'
    }

    def __init__(self, unhealthy=None, total=None, event_unhealthy=None, namespaces=None):
        r"""OneResourceGroupRespResourceStatistics

        The model defined in huaweicloud sdk

        :param unhealthy: **参数解释** 该资源分组中当前处在告警状态的资源个数。  **取值范围** 在[0,9999999]区间内。
        :type unhealthy: int
        :param total: **参数解释** 该资源分组中资源的总个数。  **取值范围** 在[0,9999999]区间内。
        :type total: int
        :param event_unhealthy: **参数解释** 该资源分组中已触发的资源个数。  **取值范围** 在[0,9999999]区间内。
        :type event_unhealthy: int
        :param namespaces: **参数解释** 该资源分组中选择的资源类型个数，如资源分组添加了弹性云服务、弹性公网IP和带宽则值为2。 **取值范围** 在[0,9999999]区间内。
        :type namespaces: int
        """
        
        

        self._unhealthy = None
        self._total = None
        self._event_unhealthy = None
        self._namespaces = None
        self.discriminator = None

        if unhealthy is not None:
            self.unhealthy = unhealthy
        if total is not None:
            self.total = total
        if event_unhealthy is not None:
            self.event_unhealthy = event_unhealthy
        if namespaces is not None:
            self.namespaces = namespaces

    @property
    def unhealthy(self):
        r"""Gets the unhealthy of this OneResourceGroupRespResourceStatistics.

        **参数解释** 该资源分组中当前处在告警状态的资源个数。  **取值范围** 在[0,9999999]区间内。

        :return: The unhealthy of this OneResourceGroupRespResourceStatistics.
        :rtype: int
        """
        return self._unhealthy

    @unhealthy.setter
    def unhealthy(self, unhealthy):
        r"""Sets the unhealthy of this OneResourceGroupRespResourceStatistics.

        **参数解释** 该资源分组中当前处在告警状态的资源个数。  **取值范围** 在[0,9999999]区间内。

        :param unhealthy: The unhealthy of this OneResourceGroupRespResourceStatistics.
        :type unhealthy: int
        """
        self._unhealthy = unhealthy

    @property
    def total(self):
        r"""Gets the total of this OneResourceGroupRespResourceStatistics.

        **参数解释** 该资源分组中资源的总个数。  **取值范围** 在[0,9999999]区间内。

        :return: The total of this OneResourceGroupRespResourceStatistics.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this OneResourceGroupRespResourceStatistics.

        **参数解释** 该资源分组中资源的总个数。  **取值范围** 在[0,9999999]区间内。

        :param total: The total of this OneResourceGroupRespResourceStatistics.
        :type total: int
        """
        self._total = total

    @property
    def event_unhealthy(self):
        r"""Gets the event_unhealthy of this OneResourceGroupRespResourceStatistics.

        **参数解释** 该资源分组中已触发的资源个数。  **取值范围** 在[0,9999999]区间内。

        :return: The event_unhealthy of this OneResourceGroupRespResourceStatistics.
        :rtype: int
        """
        return self._event_unhealthy

    @event_unhealthy.setter
    def event_unhealthy(self, event_unhealthy):
        r"""Sets the event_unhealthy of this OneResourceGroupRespResourceStatistics.

        **参数解释** 该资源分组中已触发的资源个数。  **取值范围** 在[0,9999999]区间内。

        :param event_unhealthy: The event_unhealthy of this OneResourceGroupRespResourceStatistics.
        :type event_unhealthy: int
        """
        self._event_unhealthy = event_unhealthy

    @property
    def namespaces(self):
        r"""Gets the namespaces of this OneResourceGroupRespResourceStatistics.

        **参数解释** 该资源分组中选择的资源类型个数，如资源分组添加了弹性云服务、弹性公网IP和带宽则值为2。 **取值范围** 在[0,9999999]区间内。

        :return: The namespaces of this OneResourceGroupRespResourceStatistics.
        :rtype: int
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        r"""Sets the namespaces of this OneResourceGroupRespResourceStatistics.

        **参数解释** 该资源分组中选择的资源类型个数，如资源分组添加了弹性云服务、弹性公网IP和带宽则值为2。 **取值范围** 在[0,9999999]区间内。

        :param namespaces: The namespaces of this OneResourceGroupRespResourceStatistics.
        :type namespaces: int
        """
        self._namespaces = namespaces

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
        if not isinstance(other, OneResourceGroupRespResourceStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
