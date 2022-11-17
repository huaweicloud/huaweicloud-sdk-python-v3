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
        """MetricDataItem

        The model defined in huaweicloud sdk

        :param collect_time: 数据收集时间支持过去1天和未来半小时范围内的数据上报。数据收集时间需要满足：  当前UTC时间减去collect_time小于等于24小时或者collect_time减去当前UTC时间小于等于30分钟。  若数据上报时间早于当天8点，则指标监控页面只显示当天8点后的数据。 取值范围： UNIX时间戳，单位毫秒。
        :type collect_time: int
        :param metric: 
        :type metric: :class:`huaweicloudsdkaom.v2.MetricItemInfo`
        :param values: 指标数据的值。
        :type values: list[:class:`huaweicloudsdkaom.v2.ValueData`]
        """
        
        

        self._collect_time = None
        self._metric = None
        self._values = None
        self.discriminator = None

        self.collect_time = collect_time
        self.metric = metric
        self.values = values

    @property
    def collect_time(self):
        """Gets the collect_time of this MetricDataItem.

        数据收集时间支持过去1天和未来半小时范围内的数据上报。数据收集时间需要满足：  当前UTC时间减去collect_time小于等于24小时或者collect_time减去当前UTC时间小于等于30分钟。  若数据上报时间早于当天8点，则指标监控页面只显示当天8点后的数据。 取值范围： UNIX时间戳，单位毫秒。

        :return: The collect_time of this MetricDataItem.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        """Sets the collect_time of this MetricDataItem.

        数据收集时间支持过去1天和未来半小时范围内的数据上报。数据收集时间需要满足：  当前UTC时间减去collect_time小于等于24小时或者collect_time减去当前UTC时间小于等于30分钟。  若数据上报时间早于当天8点，则指标监控页面只显示当天8点后的数据。 取值范围： UNIX时间戳，单位毫秒。

        :param collect_time: The collect_time of this MetricDataItem.
        :type collect_time: int
        """
        self._collect_time = collect_time

    @property
    def metric(self):
        """Gets the metric of this MetricDataItem.

        :return: The metric of this MetricDataItem.
        :rtype: :class:`huaweicloudsdkaom.v2.MetricItemInfo`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this MetricDataItem.

        :param metric: The metric of this MetricDataItem.
        :type metric: :class:`huaweicloudsdkaom.v2.MetricItemInfo`
        """
        self._metric = metric

    @property
    def values(self):
        """Gets the values of this MetricDataItem.

        指标数据的值。

        :return: The values of this MetricDataItem.
        :rtype: list[:class:`huaweicloudsdkaom.v2.ValueData`]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this MetricDataItem.

        指标数据的值。

        :param values: The values of this MetricDataItem.
        :type values: list[:class:`huaweicloudsdkaom.v2.ValueData`]
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
