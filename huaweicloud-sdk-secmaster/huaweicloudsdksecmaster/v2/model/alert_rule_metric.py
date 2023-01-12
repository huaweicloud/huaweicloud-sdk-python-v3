# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertRuleMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'metric': 'dict(str, float)'
    }

    attribute_map = {
        'category': 'category',
        'metric': 'metric'
    }

    def __init__(self, category=None, metric=None):
        """AlertRuleMetric

        The model defined in huaweicloud sdk

        :param category: category. GROUP_COUNT
        :type category: str
        :param metric: metric
        :type metric: dict(str, float)
        """
        
        

        self._category = None
        self._metric = None
        self.discriminator = None

        self.category = category
        self.metric = metric

    @property
    def category(self):
        """Gets the category of this AlertRuleMetric.

        category. GROUP_COUNT

        :return: The category of this AlertRuleMetric.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AlertRuleMetric.

        category. GROUP_COUNT

        :param category: The category of this AlertRuleMetric.
        :type category: str
        """
        self._category = category

    @property
    def metric(self):
        """Gets the metric of this AlertRuleMetric.

        metric

        :return: The metric of this AlertRuleMetric.
        :rtype: dict(str, float)
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this AlertRuleMetric.

        metric

        :param metric: The metric of this AlertRuleMetric.
        :type metric: dict(str, float)
        """
        self._metric = metric

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
        if not isinstance(other, AlertRuleMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
