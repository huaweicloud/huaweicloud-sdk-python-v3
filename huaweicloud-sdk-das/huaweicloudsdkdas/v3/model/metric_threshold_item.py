# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricThresholdItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_code': 'str',
        'metric_name': 'str',
        'threshold': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'metric_code': 'metric_code',
        'metric_name': 'metric_name',
        'threshold': 'threshold',
        'unit': 'unit'
    }

    def __init__(self, metric_code=None, metric_name=None, threshold=None, unit=None):
        r"""MetricThresholdItem

        The model defined in huaweicloud sdk

        :param metric_code: 指标码
        :type metric_code: str
        :param metric_name: 指标名
        :type metric_name: str
        :param threshold: 阈值
        :type threshold: float
        :param unit: 单位
        :type unit: str
        """
        
        

        self._metric_code = None
        self._metric_name = None
        self._threshold = None
        self._unit = None
        self.discriminator = None

        if metric_code is not None:
            self.metric_code = metric_code
        if metric_name is not None:
            self.metric_name = metric_name
        if threshold is not None:
            self.threshold = threshold
        if unit is not None:
            self.unit = unit

    @property
    def metric_code(self):
        r"""Gets the metric_code of this MetricThresholdItem.

        指标码

        :return: The metric_code of this MetricThresholdItem.
        :rtype: str
        """
        return self._metric_code

    @metric_code.setter
    def metric_code(self, metric_code):
        r"""Sets the metric_code of this MetricThresholdItem.

        指标码

        :param metric_code: The metric_code of this MetricThresholdItem.
        :type metric_code: str
        """
        self._metric_code = metric_code

    @property
    def metric_name(self):
        r"""Gets the metric_name of this MetricThresholdItem.

        指标名

        :return: The metric_name of this MetricThresholdItem.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this MetricThresholdItem.

        指标名

        :param metric_name: The metric_name of this MetricThresholdItem.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def threshold(self):
        r"""Gets the threshold of this MetricThresholdItem.

        阈值

        :return: The threshold of this MetricThresholdItem.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this MetricThresholdItem.

        阈值

        :param threshold: The threshold of this MetricThresholdItem.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def unit(self):
        r"""Gets the unit of this MetricThresholdItem.

        单位

        :return: The unit of this MetricThresholdItem.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this MetricThresholdItem.

        单位

        :param unit: The unit of this MetricThresholdItem.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, MetricThresholdItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
