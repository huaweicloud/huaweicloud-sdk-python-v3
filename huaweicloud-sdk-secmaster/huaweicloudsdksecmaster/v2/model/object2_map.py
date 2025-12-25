# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Object2Map:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric': 'dict(str, float)',
        'category': 'str'
    }

    attribute_map = {
        'metric': 'metric',
        'category': 'category'
    }

    def __init__(self, metric=None, category=None):
        r"""Object2Map

        The model defined in huaweicloud sdk

        :param metric: 表示一个 Map&lt;String, BigDecimal&gt;，用于存储高精度数值类型的指标
        :type metric: dict(str, float)
        :param category: 目录状态相关描述
        :type category: str
        """
        
        

        self._metric = None
        self._category = None
        self.discriminator = None

        if metric is not None:
            self.metric = metric
        if category is not None:
            self.category = category

    @property
    def metric(self):
        r"""Gets the metric of this Object2Map.

        表示一个 Map<String, BigDecimal>，用于存储高精度数值类型的指标

        :return: The metric of this Object2Map.
        :rtype: dict(str, float)
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this Object2Map.

        表示一个 Map<String, BigDecimal>，用于存储高精度数值类型的指标

        :param metric: The metric of this Object2Map.
        :type metric: dict(str, float)
        """
        self._metric = metric

    @property
    def category(self):
        r"""Gets the category of this Object2Map.

        目录状态相关描述

        :return: The category of this Object2Map.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this Object2Map.

        目录状态相关描述

        :param category: The category of this Object2Map.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, Object2Map):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
