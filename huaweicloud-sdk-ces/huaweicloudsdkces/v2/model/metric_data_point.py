# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricDataPoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[MetricDataPointDimensions]',
        'timestamp': 'int',
        'value': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'timestamp': 'timestamp',
        'value': 'value',
        'unit': 'unit'
    }

    def __init__(self, dimensions=None, timestamp=None, value=None, unit=None):
        r"""MetricDataPoint

        The model defined in huaweicloud sdk

        :param dimensions: **参数解释**： 维度信息 
        :type dimensions: list[:class:`huaweicloudsdkces.v2.MetricDataPointDimensions`]
        :param timestamp: **参数解释**： 指标采集时间 **取值范围**： 最小值为0 
        :type timestamp: int
        :param value: **参数解释**： 指标值 **取值范围**： 不涉及 
        :type value: float
        :param unit: **参数解释**： 数据的单位。    **取值范围**： 长度为[0,32]个字符。 
        :type unit: str
        """
        
        

        self._dimensions = None
        self._timestamp = None
        self._value = None
        self._unit = None
        self.discriminator = None

        if dimensions is not None:
            self.dimensions = dimensions
        if timestamp is not None:
            self.timestamp = timestamp
        if value is not None:
            self.value = value
        if unit is not None:
            self.unit = unit

    @property
    def dimensions(self):
        r"""Gets the dimensions of this MetricDataPoint.

        **参数解释**： 维度信息 

        :return: The dimensions of this MetricDataPoint.
        :rtype: list[:class:`huaweicloudsdkces.v2.MetricDataPointDimensions`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this MetricDataPoint.

        **参数解释**： 维度信息 

        :param dimensions: The dimensions of this MetricDataPoint.
        :type dimensions: list[:class:`huaweicloudsdkces.v2.MetricDataPointDimensions`]
        """
        self._dimensions = dimensions

    @property
    def timestamp(self):
        r"""Gets the timestamp of this MetricDataPoint.

        **参数解释**： 指标采集时间 **取值范围**： 最小值为0 

        :return: The timestamp of this MetricDataPoint.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this MetricDataPoint.

        **参数解释**： 指标采集时间 **取值范围**： 最小值为0 

        :param timestamp: The timestamp of this MetricDataPoint.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def value(self):
        r"""Gets the value of this MetricDataPoint.

        **参数解释**： 指标值 **取值范围**： 不涉及 

        :return: The value of this MetricDataPoint.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this MetricDataPoint.

        **参数解释**： 指标值 **取值范围**： 不涉及 

        :param value: The value of this MetricDataPoint.
        :type value: float
        """
        self._value = value

    @property
    def unit(self):
        r"""Gets the unit of this MetricDataPoint.

        **参数解释**： 数据的单位。    **取值范围**： 长度为[0,32]个字符。 

        :return: The unit of this MetricDataPoint.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this MetricDataPoint.

        **参数解释**： 数据的单位。    **取值范围**： 长度为[0,32]个字符。 

        :param unit: The unit of this MetricDataPoint.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, MetricDataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
