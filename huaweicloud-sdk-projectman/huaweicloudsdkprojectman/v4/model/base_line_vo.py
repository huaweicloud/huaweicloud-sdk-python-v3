# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseLineVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'baseline': 'str'
    }

    attribute_map = {
        'baseline': 'baseline'
    }

    def __init__(self, baseline=None):
        r"""BaseLineVO

        The model defined in huaweicloud sdk

        :param baseline: **参数解释**： 基线或取消基线操作类型。 **约束限制**： 不涉及。 **取值范围**： - baselined：基线发布/迭代计划 - unbaseline：取消基线，恢复发布/迭代计划 **默认取值**： 不涉及。
        :type baseline: str
        """
        
        

        self._baseline = None
        self.discriminator = None

        if baseline is not None:
            self.baseline = baseline

    @property
    def baseline(self):
        r"""Gets the baseline of this BaseLineVO.

        **参数解释**： 基线或取消基线操作类型。 **约束限制**： 不涉及。 **取值范围**： - baselined：基线发布/迭代计划 - unbaseline：取消基线，恢复发布/迭代计划 **默认取值**： 不涉及。

        :return: The baseline of this BaseLineVO.
        :rtype: str
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this BaseLineVO.

        **参数解释**： 基线或取消基线操作类型。 **约束限制**： 不涉及。 **取值范围**： - baselined：基线发布/迭代计划 - unbaseline：取消基线，恢复发布/迭代计划 **默认取值**： 不涉及。

        :param baseline: The baseline of this BaseLineVO.
        :type baseline: str
        """
        self._baseline = baseline

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
        if not isinstance(other, BaseLineVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
