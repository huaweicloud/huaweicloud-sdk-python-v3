# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'metric_value': 'float'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'metric_value': 'metric_value'
    }

    def __init__(self, metric_name=None, metric_value=None):
        r"""Metric

        The model defined in huaweicloud sdk

        :param metric_name: 指标名称
        :type metric_name: str
        :param metric_value: 指标值
        :type metric_value: float
        """
        
        

        self._metric_name = None
        self._metric_value = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if metric_value is not None:
            self.metric_value = metric_value

    @property
    def metric_name(self):
        r"""Gets the metric_name of this Metric.

        指标名称

        :return: The metric_name of this Metric.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this Metric.

        指标名称

        :param metric_name: The metric_name of this Metric.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def metric_value(self):
        r"""Gets the metric_value of this Metric.

        指标值

        :return: The metric_value of this Metric.
        :rtype: float
        """
        return self._metric_value

    @metric_value.setter
    def metric_value(self, metric_value):
        r"""Sets the metric_value of this Metric.

        指标值

        :param metric_value: The metric_value of this Metric.
        :type metric_value: float
        """
        self._metric_value = metric_value

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
        if not isinstance(other, Metric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
