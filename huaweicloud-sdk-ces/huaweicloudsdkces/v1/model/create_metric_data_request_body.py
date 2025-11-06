# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMetricDataRequestBody:

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
        r"""CreateMetricDataRequestBody

        The model defined in huaweicloud sdk

        :param metric: 
        :type metric: :class:`huaweicloudsdkces.v1.MetricInfo`
        :param ttl: **参数解释**： 数据的有效期，超出该有效期则自动删除该数据，单位秒。 **约束限制**： 不涉及。 **取值范围**： 大小为[1,604800]的整数。 **默认取值**： 不涉及。 
        :type ttl: int
        :param collect_time: **参数解释**： 数据收集时间 。UNIX时间戳，单位毫秒。 **约束限制**： 不涉及。 **取值范围**： 因为客户端到服务器端有延时，因此插入数据的时间戳应该在[当前时间-3天+10秒，当前时间+10分钟-10秒]区间内，保证到达服务器时不会因为传输时延造成数据不能插入数据库。 **默认取值**： 不涉及。 
        :type collect_time: int
        :param value: **参数解释**： 待添加的监控指标数据的值。 **约束限制**： 不涉及。 **取值范围**： 数值类型支持“整数”或“浮点数”。 **默认取值**： 不涉及。 
        :type value: float
        :param unit: **参数解释**： 数据的单位。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。 **默认取值**： 不涉及。 
        :type unit: str
        :param type: **参数解释**： 数据类型。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能是\&quot;int\&quot;或\&quot;float\&quot;。 - int：整数 - float：浮点数 **默认取值**： 不涉及。 
        :type type: str
        """
        
        

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
        r"""Gets the metric of this CreateMetricDataRequestBody.

        :return: The metric of this CreateMetricDataRequestBody.
        :rtype: :class:`huaweicloudsdkces.v1.MetricInfo`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this CreateMetricDataRequestBody.

        :param metric: The metric of this CreateMetricDataRequestBody.
        :type metric: :class:`huaweicloudsdkces.v1.MetricInfo`
        """
        self._metric = metric

    @property
    def ttl(self):
        r"""Gets the ttl of this CreateMetricDataRequestBody.

        **参数解释**： 数据的有效期，超出该有效期则自动删除该数据，单位秒。 **约束限制**： 不涉及。 **取值范围**： 大小为[1,604800]的整数。 **默认取值**： 不涉及。 

        :return: The ttl of this CreateMetricDataRequestBody.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this CreateMetricDataRequestBody.

        **参数解释**： 数据的有效期，超出该有效期则自动删除该数据，单位秒。 **约束限制**： 不涉及。 **取值范围**： 大小为[1,604800]的整数。 **默认取值**： 不涉及。 

        :param ttl: The ttl of this CreateMetricDataRequestBody.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def collect_time(self):
        r"""Gets the collect_time of this CreateMetricDataRequestBody.

        **参数解释**： 数据收集时间 。UNIX时间戳，单位毫秒。 **约束限制**： 不涉及。 **取值范围**： 因为客户端到服务器端有延时，因此插入数据的时间戳应该在[当前时间-3天+10秒，当前时间+10分钟-10秒]区间内，保证到达服务器时不会因为传输时延造成数据不能插入数据库。 **默认取值**： 不涉及。 

        :return: The collect_time of this CreateMetricDataRequestBody.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        r"""Sets the collect_time of this CreateMetricDataRequestBody.

        **参数解释**： 数据收集时间 。UNIX时间戳，单位毫秒。 **约束限制**： 不涉及。 **取值范围**： 因为客户端到服务器端有延时，因此插入数据的时间戳应该在[当前时间-3天+10秒，当前时间+10分钟-10秒]区间内，保证到达服务器时不会因为传输时延造成数据不能插入数据库。 **默认取值**： 不涉及。 

        :param collect_time: The collect_time of this CreateMetricDataRequestBody.
        :type collect_time: int
        """
        self._collect_time = collect_time

    @property
    def value(self):
        r"""Gets the value of this CreateMetricDataRequestBody.

        **参数解释**： 待添加的监控指标数据的值。 **约束限制**： 不涉及。 **取值范围**： 数值类型支持“整数”或“浮点数”。 **默认取值**： 不涉及。 

        :return: The value of this CreateMetricDataRequestBody.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CreateMetricDataRequestBody.

        **参数解释**： 待添加的监控指标数据的值。 **约束限制**： 不涉及。 **取值范围**： 数值类型支持“整数”或“浮点数”。 **默认取值**： 不涉及。 

        :param value: The value of this CreateMetricDataRequestBody.
        :type value: float
        """
        self._value = value

    @property
    def unit(self):
        r"""Gets the unit of this CreateMetricDataRequestBody.

        **参数解释**： 数据的单位。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。 **默认取值**： 不涉及。 

        :return: The unit of this CreateMetricDataRequestBody.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this CreateMetricDataRequestBody.

        **参数解释**： 数据的单位。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。 **默认取值**： 不涉及。 

        :param unit: The unit of this CreateMetricDataRequestBody.
        :type unit: str
        """
        self._unit = unit

    @property
    def type(self):
        r"""Gets the type of this CreateMetricDataRequestBody.

        **参数解释**： 数据类型。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能是\"int\"或\"float\"。 - int：整数 - float：浮点数 **默认取值**： 不涉及。 

        :return: The type of this CreateMetricDataRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateMetricDataRequestBody.

        **参数解释**： 数据类型。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能是\"int\"或\"float\"。 - int：整数 - float：浮点数 **默认取值**： 不涉及。 

        :param type: The type of this CreateMetricDataRequestBody.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, CreateMetricDataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
