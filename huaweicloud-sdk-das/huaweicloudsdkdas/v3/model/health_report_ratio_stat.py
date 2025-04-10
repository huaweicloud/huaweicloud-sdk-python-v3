# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportRatioStat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric': 'str',
        'max_value': 'float',
        'critical_ratio': 'float',
        'medium_ratio': 'float',
        'light_ratio': 'float'
    }

    attribute_map = {
        'metric': 'metric',
        'max_value': 'max_value',
        'critical_ratio': 'critical_ratio',
        'medium_ratio': 'medium_ratio',
        'light_ratio': 'light_ratio'
    }

    def __init__(self, metric=None, max_value=None, critical_ratio=None, medium_ratio=None, light_ratio=None):
        r"""HealthReportRatioStat

        The model defined in huaweicloud sdk

        :param metric: 指标名。
        :type metric: str
        :param max_value: 最大值。
        :type max_value: float
        :param critical_ratio: 高水位占比。
        :type critical_ratio: float
        :param medium_ratio: 中水位占比。
        :type medium_ratio: float
        :param light_ratio: 低水位占比。
        :type light_ratio: float
        """
        
        

        self._metric = None
        self._max_value = None
        self._critical_ratio = None
        self._medium_ratio = None
        self._light_ratio = None
        self.discriminator = None

        self.metric = metric
        self.max_value = max_value
        self.critical_ratio = critical_ratio
        self.medium_ratio = medium_ratio
        self.light_ratio = light_ratio

    @property
    def metric(self):
        r"""Gets the metric of this HealthReportRatioStat.

        指标名。

        :return: The metric of this HealthReportRatioStat.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this HealthReportRatioStat.

        指标名。

        :param metric: The metric of this HealthReportRatioStat.
        :type metric: str
        """
        self._metric = metric

    @property
    def max_value(self):
        r"""Gets the max_value of this HealthReportRatioStat.

        最大值。

        :return: The max_value of this HealthReportRatioStat.
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        r"""Sets the max_value of this HealthReportRatioStat.

        最大值。

        :param max_value: The max_value of this HealthReportRatioStat.
        :type max_value: float
        """
        self._max_value = max_value

    @property
    def critical_ratio(self):
        r"""Gets the critical_ratio of this HealthReportRatioStat.

        高水位占比。

        :return: The critical_ratio of this HealthReportRatioStat.
        :rtype: float
        """
        return self._critical_ratio

    @critical_ratio.setter
    def critical_ratio(self, critical_ratio):
        r"""Sets the critical_ratio of this HealthReportRatioStat.

        高水位占比。

        :param critical_ratio: The critical_ratio of this HealthReportRatioStat.
        :type critical_ratio: float
        """
        self._critical_ratio = critical_ratio

    @property
    def medium_ratio(self):
        r"""Gets the medium_ratio of this HealthReportRatioStat.

        中水位占比。

        :return: The medium_ratio of this HealthReportRatioStat.
        :rtype: float
        """
        return self._medium_ratio

    @medium_ratio.setter
    def medium_ratio(self, medium_ratio):
        r"""Sets the medium_ratio of this HealthReportRatioStat.

        中水位占比。

        :param medium_ratio: The medium_ratio of this HealthReportRatioStat.
        :type medium_ratio: float
        """
        self._medium_ratio = medium_ratio

    @property
    def light_ratio(self):
        r"""Gets the light_ratio of this HealthReportRatioStat.

        低水位占比。

        :return: The light_ratio of this HealthReportRatioStat.
        :rtype: float
        """
        return self._light_ratio

    @light_ratio.setter
    def light_ratio(self, light_ratio):
        r"""Sets the light_ratio of this HealthReportRatioStat.

        低水位占比。

        :param light_ratio: The light_ratio of this HealthReportRatioStat.
        :type light_ratio: float
        """
        self._light_ratio = light_ratio

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
        if not isinstance(other, HealthReportRatioStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
