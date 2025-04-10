# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportSingleValueStat:

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
        'value': 'float',
        'max_value': 'float',
        'normalized': 'float',
        'stage': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'metric': 'metric',
        'value': 'value',
        'max_value': 'max_value',
        'normalized': 'normalized',
        'stage': 'stage',
        'timestamp': 'timestamp'
    }

    def __init__(self, metric=None, value=None, max_value=None, normalized=None, stage=None, timestamp=None):
        r"""HealthReportSingleValueStat

        The model defined in huaweicloud sdk

        :param metric: 指标名。
        :type metric: str
        :param value: 数值。
        :type value: float
        :param max_value: 最大值。
        :type max_value: float
        :param normalized: 归一化值。
        :type normalized: float
        :param stage: 当前状态。
        :type stage: str
        :param timestamp: 指标采集时间。
        :type timestamp: int
        """
        
        

        self._metric = None
        self._value = None
        self._max_value = None
        self._normalized = None
        self._stage = None
        self._timestamp = None
        self.discriminator = None

        self.metric = metric
        self.value = value
        self.max_value = max_value
        self.normalized = normalized
        self.stage = stage
        self.timestamp = timestamp

    @property
    def metric(self):
        r"""Gets the metric of this HealthReportSingleValueStat.

        指标名。

        :return: The metric of this HealthReportSingleValueStat.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this HealthReportSingleValueStat.

        指标名。

        :param metric: The metric of this HealthReportSingleValueStat.
        :type metric: str
        """
        self._metric = metric

    @property
    def value(self):
        r"""Gets the value of this HealthReportSingleValueStat.

        数值。

        :return: The value of this HealthReportSingleValueStat.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this HealthReportSingleValueStat.

        数值。

        :param value: The value of this HealthReportSingleValueStat.
        :type value: float
        """
        self._value = value

    @property
    def max_value(self):
        r"""Gets the max_value of this HealthReportSingleValueStat.

        最大值。

        :return: The max_value of this HealthReportSingleValueStat.
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        r"""Sets the max_value of this HealthReportSingleValueStat.

        最大值。

        :param max_value: The max_value of this HealthReportSingleValueStat.
        :type max_value: float
        """
        self._max_value = max_value

    @property
    def normalized(self):
        r"""Gets the normalized of this HealthReportSingleValueStat.

        归一化值。

        :return: The normalized of this HealthReportSingleValueStat.
        :rtype: float
        """
        return self._normalized

    @normalized.setter
    def normalized(self, normalized):
        r"""Sets the normalized of this HealthReportSingleValueStat.

        归一化值。

        :param normalized: The normalized of this HealthReportSingleValueStat.
        :type normalized: float
        """
        self._normalized = normalized

    @property
    def stage(self):
        r"""Gets the stage of this HealthReportSingleValueStat.

        当前状态。

        :return: The stage of this HealthReportSingleValueStat.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this HealthReportSingleValueStat.

        当前状态。

        :param stage: The stage of this HealthReportSingleValueStat.
        :type stage: str
        """
        self._stage = stage

    @property
    def timestamp(self):
        r"""Gets the timestamp of this HealthReportSingleValueStat.

        指标采集时间。

        :return: The timestamp of this HealthReportSingleValueStat.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this HealthReportSingleValueStat.

        指标采集时间。

        :param timestamp: The timestamp of this HealthReportSingleValueStat.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, HealthReportSingleValueStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
