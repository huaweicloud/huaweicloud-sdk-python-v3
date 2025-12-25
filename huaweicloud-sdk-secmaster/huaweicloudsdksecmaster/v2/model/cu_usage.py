# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CuUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'usage_category': 'str',
        'usage_metric': 'UsageMetric'
    }

    attribute_map = {
        'usage_category': 'usage_category',
        'usage_metric': 'usage_metric'
    }

    def __init__(self, usage_category=None, usage_metric=None):
        r"""CuUsage

        The model defined in huaweicloud sdk

        :param usage_category: **参数解释**: 目录 - USAGE 使用  **约束限制** 不涉及 **取值范围**: - USAGE  **默认值** 不涉及  
        :type usage_category: str
        :param usage_metric: 
        :type usage_metric: :class:`huaweicloudsdksecmaster.v2.UsageMetric`
        """
        
        

        self._usage_category = None
        self._usage_metric = None
        self.discriminator = None

        if usage_category is not None:
            self.usage_category = usage_category
        if usage_metric is not None:
            self.usage_metric = usage_metric

    @property
    def usage_category(self):
        r"""Gets the usage_category of this CuUsage.

        **参数解释**: 目录 - USAGE 使用  **约束限制** 不涉及 **取值范围**: - USAGE  **默认值** 不涉及  

        :return: The usage_category of this CuUsage.
        :rtype: str
        """
        return self._usage_category

    @usage_category.setter
    def usage_category(self, usage_category):
        r"""Sets the usage_category of this CuUsage.

        **参数解释**: 目录 - USAGE 使用  **约束限制** 不涉及 **取值范围**: - USAGE  **默认值** 不涉及  

        :param usage_category: The usage_category of this CuUsage.
        :type usage_category: str
        """
        self._usage_category = usage_category

    @property
    def usage_metric(self):
        r"""Gets the usage_metric of this CuUsage.

        :return: The usage_metric of this CuUsage.
        :rtype: :class:`huaweicloudsdksecmaster.v2.UsageMetric`
        """
        return self._usage_metric

    @usage_metric.setter
    def usage_metric(self, usage_metric):
        r"""Sets the usage_metric of this CuUsage.

        :param usage_metric: The usage_metric of this CuUsage.
        :type usage_metric: :class:`huaweicloudsdksecmaster.v2.UsageMetric`
        """
        self._usage_metric = usage_metric

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
        if not isinstance(other, CuUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
