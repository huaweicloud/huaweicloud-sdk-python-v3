# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLoadbalancerAutoscalingOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'min_l7_flavor_id': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'min_l7_flavor_id': 'min_l7_flavor_id'
    }

    def __init__(self, enable=None, min_l7_flavor_id=None):
        r"""CreateLoadbalancerAutoscalingOption

        The model defined in huaweicloud sdk

        :param enable: **参数解释**：负载均衡器实例弹性扩缩容开关。  **约束限制**：不涉及  **取值范围**： - true：开启。 - false：关闭。   **默认取值**：不涉及  [网关型LB不支持该字段。](tag:hws_eu)
        :type enable: bool
        :param min_l7_flavor_id: **参数解释**：实例弹性扩缩容的最小七层规格ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type min_l7_flavor_id: str
        """
        
        

        self._enable = None
        self._min_l7_flavor_id = None
        self.discriminator = None

        self.enable = enable
        if min_l7_flavor_id is not None:
            self.min_l7_flavor_id = min_l7_flavor_id

    @property
    def enable(self):
        r"""Gets the enable of this CreateLoadbalancerAutoscalingOption.

        **参数解释**：负载均衡器实例弹性扩缩容开关。  **约束限制**：不涉及  **取值范围**： - true：开启。 - false：关闭。   **默认取值**：不涉及  [网关型LB不支持该字段。](tag:hws_eu)

        :return: The enable of this CreateLoadbalancerAutoscalingOption.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this CreateLoadbalancerAutoscalingOption.

        **参数解释**：负载均衡器实例弹性扩缩容开关。  **约束限制**：不涉及  **取值范围**： - true：开启。 - false：关闭。   **默认取值**：不涉及  [网关型LB不支持该字段。](tag:hws_eu)

        :param enable: The enable of this CreateLoadbalancerAutoscalingOption.
        :type enable: bool
        """
        self._enable = enable

    @property
    def min_l7_flavor_id(self):
        r"""Gets the min_l7_flavor_id of this CreateLoadbalancerAutoscalingOption.

        **参数解释**：实例弹性扩缩容的最小七层规格ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The min_l7_flavor_id of this CreateLoadbalancerAutoscalingOption.
        :rtype: str
        """
        return self._min_l7_flavor_id

    @min_l7_flavor_id.setter
    def min_l7_flavor_id(self, min_l7_flavor_id):
        r"""Sets the min_l7_flavor_id of this CreateLoadbalancerAutoscalingOption.

        **参数解释**：实例弹性扩缩容的最小七层规格ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param min_l7_flavor_id: The min_l7_flavor_id of this CreateLoadbalancerAutoscalingOption.
        :type min_l7_flavor_id: str
        """
        self._min_l7_flavor_id = min_l7_flavor_id

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
        if not isinstance(other, CreateLoadbalancerAutoscalingOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
