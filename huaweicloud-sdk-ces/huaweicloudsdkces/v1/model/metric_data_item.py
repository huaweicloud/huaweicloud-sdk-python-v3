# coding: utf-8

import pprint
import re

import six





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
        'metric': 'MetricInfo',
        'ttl': 'int',
        'collect_time': 'int',
        'value': 'float',
        'unit': 'str',
        'type': 'str'
    }

    attribute_map = {
        'metric': 'metric',
        'ttl': 'ttl',
        'collect_time': 'collect_time',
        'value': 'value',
        'unit': 'unit',
        'type': 'type'
    }

    def __init__(self, metric=None, ttl=None, collect_time=None, value=None, unit=None, type=None):
        """MetricDataItem - a model defined in huaweicloud sdk"""
        
        

        self._metric = None
        self._ttl = None
        self._collect_time = None
        self._value = None
        self._unit = None
        self._type = None
        self.discriminator = None

        self.metric = metric
        self.ttl = ttl
        self.collect_time = collect_time
        self.value = value
        if unit is not None:
            self.unit = unit
        if type is not None:
            self.type = type

    @property
    def metric(self):
        """Gets the metric of this MetricDataItem.


        :return: The metric of this MetricDataItem.
        :rtype: MetricInfo
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this MetricDataItem.


        :param metric: The metric of this MetricDataItem.
        :type: MetricInfo
        """
        self._metric = metric

    @property
    def ttl(self):
        """Gets the ttl of this MetricDataItem.

        数据的有效期，超出该有效期则自动删除该数据，单位秒，最大值604800。

        :return: The ttl of this MetricDataItem.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this MetricDataItem.

        数据的有效期，超出该有效期则自动删除该数据，单位秒，最大值604800。

        :param ttl: The ttl of this MetricDataItem.
        :type: int
        """
        self._ttl = ttl

    @property
    def collect_time(self):
        """Gets the collect_time of this MetricDataItem.

        数据收集时间  UNIX时间戳，单位毫秒。  说明： 因为客户端到服务器端有延时，因此插入数据的时间戳应该在[当前时间-3天+20秒，当前时间+10分钟-20秒]区间内，保证到达服务器时不会因为传输时延造成数据不能插入数据库。

        :return: The collect_time of this MetricDataItem.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        """Sets the collect_time of this MetricDataItem.

        数据收集时间  UNIX时间戳，单位毫秒。  说明： 因为客户端到服务器端有延时，因此插入数据的时间戳应该在[当前时间-3天+20秒，当前时间+10分钟-20秒]区间内，保证到达服务器时不会因为传输时延造成数据不能插入数据库。

        :param collect_time: The collect_time of this MetricDataItem.
        :type: int
        """
        self._collect_time = collect_time

    @property
    def value(self):
        """Gets the value of this MetricDataItem.

        指标数据的值。

        :return: The value of this MetricDataItem.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MetricDataItem.

        指标数据的值。

        :param value: The value of this MetricDataItem.
        :type: float
        """
        self._value = value

    @property
    def unit(self):
        """Gets the unit of this MetricDataItem.

        数据的单位。

        :return: The unit of this MetricDataItem.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this MetricDataItem.

        数据的单位。

        :param unit: The unit of this MetricDataItem.
        :type: str
        """
        self._unit = unit

    @property
    def type(self):
        """Gets the type of this MetricDataItem.

        数据的类型，只能是\"int\"或\"float\"

        :return: The type of this MetricDataItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MetricDataItem.

        数据的类型，只能是\"int\"或\"float\"

        :param type: The type of this MetricDataItem.
        :type: str
        """
        self._type = type

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetricDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
