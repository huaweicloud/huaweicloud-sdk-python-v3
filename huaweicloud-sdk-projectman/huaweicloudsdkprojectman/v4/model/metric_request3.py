# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricRequest3:

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
        'sprint_id': 'str',
        'dividend': 'MetricRequest3Dividend',
        'divisor': 'object'
    }

    attribute_map = {
        'date_range': 'date_range',
        'metric_type': 'metric_type',
        'sprint_id': 'sprint_id',
        'dividend': 'dividend',
        'divisor': 'divisor'
    }

    def __init__(self, date_range=None, metric_type=None, sprint_id=None, dividend=None, divisor=None):
        """MetricRequest3

        The model defined in huaweicloud sdk

        :param date_range: 统计周期
        :type date_range: str
        :param metric_type: 指标类型
        :type metric_type: str
        :param sprint_id: 迭代ID
        :type sprint_id: str
        :param dividend: 
        :type dividend: :class:`huaweicloudsdkprojectman.v4.MetricRequest3Dividend`
        :param divisor: 指标分母过滤条件
        :type divisor: object
        """
        
        

        self._date_range = None
        self._metric_type = None
        self._sprint_id = None
        self._dividend = None
        self._divisor = None
        self.discriminator = None

        if date_range is not None:
            self.date_range = date_range
        if metric_type is not None:
            self.metric_type = metric_type
        if sprint_id is not None:
            self.sprint_id = sprint_id
        if dividend is not None:
            self.dividend = dividend
        if divisor is not None:
            self.divisor = divisor

    @property
    def date_range(self):
        """Gets the date_range of this MetricRequest3.

        统计周期

        :return: The date_range of this MetricRequest3.
        :rtype: str
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range):
        """Sets the date_range of this MetricRequest3.

        统计周期

        :param date_range: The date_range of this MetricRequest3.
        :type date_range: str
        """
        self._date_range = date_range

    @property
    def metric_type(self):
        """Gets the metric_type of this MetricRequest3.

        指标类型

        :return: The metric_type of this MetricRequest3.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """Sets the metric_type of this MetricRequest3.

        指标类型

        :param metric_type: The metric_type of this MetricRequest3.
        :type metric_type: str
        """
        self._metric_type = metric_type

    @property
    def sprint_id(self):
        """Gets the sprint_id of this MetricRequest3.

        迭代ID

        :return: The sprint_id of this MetricRequest3.
        :rtype: str
        """
        return self._sprint_id

    @sprint_id.setter
    def sprint_id(self, sprint_id):
        """Sets the sprint_id of this MetricRequest3.

        迭代ID

        :param sprint_id: The sprint_id of this MetricRequest3.
        :type sprint_id: str
        """
        self._sprint_id = sprint_id

    @property
    def dividend(self):
        """Gets the dividend of this MetricRequest3.

        :return: The dividend of this MetricRequest3.
        :rtype: :class:`huaweicloudsdkprojectman.v4.MetricRequest3Dividend`
        """
        return self._dividend

    @dividend.setter
    def dividend(self, dividend):
        """Sets the dividend of this MetricRequest3.

        :param dividend: The dividend of this MetricRequest3.
        :type dividend: :class:`huaweicloudsdkprojectman.v4.MetricRequest3Dividend`
        """
        self._dividend = dividend

    @property
    def divisor(self):
        """Gets the divisor of this MetricRequest3.

        指标分母过滤条件

        :return: The divisor of this MetricRequest3.
        :rtype: object
        """
        return self._divisor

    @divisor.setter
    def divisor(self, divisor):
        """Sets the divisor of this MetricRequest3.

        指标分母过滤条件

        :param divisor: The divisor of this MetricRequest3.
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
        if not isinstance(other, MetricRequest3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
