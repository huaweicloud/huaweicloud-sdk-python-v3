# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricRequestV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'date_range': 'str',
        'metric_type': 'str',
        'dividend': 'MetricRequestV2Dividend',
        'divisor': 'object'
    }

    attribute_map = {
        'date_range': 'date_range',
        'metric_type': 'metric_type',
        'dividend': 'dividend',
        'divisor': 'divisor'
    }

    def __init__(self, date_range=None, metric_type=None, dividend=None, divisor=None):
        r"""MetricRequestV2

        The model defined in huaweicloud sdk

        :param date_range: 统计周期
        :type date_range: str
        :param metric_type: 指标类型
        :type metric_type: str
        :param dividend: 
        :type dividend: :class:`huaweicloudsdkprojectman.v4.MetricRequestV2Dividend`
        :param divisor: 指标分母过滤条件
        :type divisor: object
        """
        
        

        self._date_range = None
        self._metric_type = None
        self._dividend = None
        self._divisor = None
        self.discriminator = None

        if date_range is not None:
            self.date_range = date_range
        if metric_type is not None:
            self.metric_type = metric_type
        if dividend is not None:
            self.dividend = dividend
        if divisor is not None:
            self.divisor = divisor

    @property
    def date_range(self):
        r"""Gets the date_range of this MetricRequestV2.

        统计周期

        :return: The date_range of this MetricRequestV2.
        :rtype: str
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range):
        r"""Sets the date_range of this MetricRequestV2.

        统计周期

        :param date_range: The date_range of this MetricRequestV2.
        :type date_range: str
        """
        self._date_range = date_range

    @property
    def metric_type(self):
        r"""Gets the metric_type of this MetricRequestV2.

        指标类型

        :return: The metric_type of this MetricRequestV2.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        r"""Sets the metric_type of this MetricRequestV2.

        指标类型

        :param metric_type: The metric_type of this MetricRequestV2.
        :type metric_type: str
        """
        self._metric_type = metric_type

    @property
    def dividend(self):
        r"""Gets the dividend of this MetricRequestV2.

        :return: The dividend of this MetricRequestV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.MetricRequestV2Dividend`
        """
        return self._dividend

    @dividend.setter
    def dividend(self, dividend):
        r"""Sets the dividend of this MetricRequestV2.

        :param dividend: The dividend of this MetricRequestV2.
        :type dividend: :class:`huaweicloudsdkprojectman.v4.MetricRequestV2Dividend`
        """
        self._dividend = dividend

    @property
    def divisor(self):
        r"""Gets the divisor of this MetricRequestV2.

        指标分母过滤条件

        :return: The divisor of this MetricRequestV2.
        :rtype: object
        """
        return self._divisor

    @divisor.setter
    def divisor(self, divisor):
        r"""Sets the divisor of this MetricRequestV2.

        指标分母过滤条件

        :param divisor: The divisor of this MetricRequestV2.
        :type divisor: object
        """
        self._divisor = divisor

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
        if not isinstance(other, MetricRequestV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
