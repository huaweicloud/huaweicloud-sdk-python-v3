# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricDataItem:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'collect_time': 'int',
        'metric': 'MetricItemInfo',
        'values': 'list[ValueData]'
    }

    attribute_map = {
        'collect_time': 'collect_time',
        'metric': 'metric',
        'values': 'values'
    }

    def __init__(self, collect_time=None, metric=None, values=None):
        """MetricDataItem - a model defined in huaweicloud sdk"""
        
        

        self._collect_time = None
        self._metric = None
        self._values = None
        self.discriminator = None

        if collect_time is not None:
            self.collect_time = collect_time
        if metric is not None:
            self.metric = metric
        if values is not None:
            self.values = values

    @property
    def collect_time(self):
        """Gets the collect_time of this MetricDataItem.

        取值范围： UNIX时间戳，单位毫秒。 数据收集时间支持过去1天和未来半小时范围内的数据上报。

        :return: The collect_time of this MetricDataItem.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        """Sets the collect_time of this MetricDataItem.

        取值范围： UNIX时间戳，单位毫秒。 数据收集时间支持过去1天和未来半小时范围内的数据上报。

        :param collect_time: The collect_time of this MetricDataItem.
        :type: int
        """
        self._collect_time = collect_time

    @property
    def metric(self):
        """Gets the metric of this MetricDataItem.


        :return: The metric of this MetricDataItem.
        :rtype: MetricItemInfo
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this MetricDataItem.


        :param metric: The metric of this MetricDataItem.
        :type: MetricItemInfo
        """
        self._metric = metric

    @property
    def values(self):
        """Gets the values of this MetricDataItem.

        指标数据的值。

        :return: The values of this MetricDataItem.
        :rtype: list[ValueData]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this MetricDataItem.

        指标数据的值。

        :param values: The values of this MetricDataItem.
        :type: list[ValueData]
        """
        self._values = values

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
        if not isinstance(other, MetricDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
