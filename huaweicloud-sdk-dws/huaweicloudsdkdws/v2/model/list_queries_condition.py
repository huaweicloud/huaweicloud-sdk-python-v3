# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueriesCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field': 'str',
        'value': 'str',
        'operator': 'str'
    }

    attribute_map = {
        'field': 'field',
        'value': 'value',
        'operator': 'operator'
    }

    def __init__(self, field=None, value=None, operator=None):
        r"""ListQueriesCondition

        The model defined in huaweicloud sdk

        :param field: **参数解释**： 字段名称。 **取值范围**： systemQuery：是否隐藏系统查询。 userName：用户名称。 applicationName：应用名称。 dbName：数据库名称。 resourcePool：资源池。 queryStatus：查询状态。 enqueue：排队状态。 lane：通道。 instName：实例名称。 pid：进程ID。 blockTime：阻塞时间。 duration：持续时间。 minCpuTime：最小CPU时间。 maxCpuTime：最大CPU时间。 totalCpuTime：总CPU时间。 cpuSkewPercent：CPU倾斜率。 spillInfo：下盘信息。 minSpillSize：最小下盘大小。 maxSpillSize：最大下盘大小。 averageSpillSize：平均下盘大小。 spillSkewPercent：下盘倾斜率。 queryBand：查询标签。 jobName：作业名称。 jobInst：作业实例。 clientHostname：客户端主机名。 clientPort：客户端端口。 waiting：等待状态。 estimateTotalTime：预估总时间。 estimateLeftTime：预估剩余时间。 controlGroup：控制组。 minPeakMemory：最小峰值内存。 maxPeakMemory：最大峰值内存。 averagePeakMemory：平均峰值内存。 memorySkewPercent：内存倾斜率。 estimateMemory：预估内存。 minDnTime：最小DN时间。 maxDnTime：最大DN时间。 averageDnTime：平均DN时间。 dntimeSkewPercent：DN时间倾斜率。 warning：告警。 averagePeakIops：平均峰值IOPS。 iopsSkewPercent：IOPS倾斜率。 wlmStatus：WLM状态。 wlmAttrib：WLM属性。
        :type field: str
        :param value: **参数解释**： 字段值。 **取值范围**： 不涉及。
        :type value: str
        :param operator: **参数解释**： 比较方式。 **取值范围**： String类型参数：&#x3D;、!&#x3D;、like、not like、&lt;&gt; int类型参数：&#x3D;、!&#x3D;、&gt;、&lt;、&gt;&#x3D;、&lt;&#x3D;、&lt;&gt; boolean类型参数：&#x3D;、!&#x3D;
        :type operator: str
        """
        
        

        self._field = None
        self._value = None
        self._operator = None
        self.discriminator = None

        self.field = field
        self.value = value
        self.operator = operator

    @property
    def field(self):
        r"""Gets the field of this ListQueriesCondition.

        **参数解释**： 字段名称。 **取值范围**： systemQuery：是否隐藏系统查询。 userName：用户名称。 applicationName：应用名称。 dbName：数据库名称。 resourcePool：资源池。 queryStatus：查询状态。 enqueue：排队状态。 lane：通道。 instName：实例名称。 pid：进程ID。 blockTime：阻塞时间。 duration：持续时间。 minCpuTime：最小CPU时间。 maxCpuTime：最大CPU时间。 totalCpuTime：总CPU时间。 cpuSkewPercent：CPU倾斜率。 spillInfo：下盘信息。 minSpillSize：最小下盘大小。 maxSpillSize：最大下盘大小。 averageSpillSize：平均下盘大小。 spillSkewPercent：下盘倾斜率。 queryBand：查询标签。 jobName：作业名称。 jobInst：作业实例。 clientHostname：客户端主机名。 clientPort：客户端端口。 waiting：等待状态。 estimateTotalTime：预估总时间。 estimateLeftTime：预估剩余时间。 controlGroup：控制组。 minPeakMemory：最小峰值内存。 maxPeakMemory：最大峰值内存。 averagePeakMemory：平均峰值内存。 memorySkewPercent：内存倾斜率。 estimateMemory：预估内存。 minDnTime：最小DN时间。 maxDnTime：最大DN时间。 averageDnTime：平均DN时间。 dntimeSkewPercent：DN时间倾斜率。 warning：告警。 averagePeakIops：平均峰值IOPS。 iopsSkewPercent：IOPS倾斜率。 wlmStatus：WLM状态。 wlmAttrib：WLM属性。

        :return: The field of this ListQueriesCondition.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this ListQueriesCondition.

        **参数解释**： 字段名称。 **取值范围**： systemQuery：是否隐藏系统查询。 userName：用户名称。 applicationName：应用名称。 dbName：数据库名称。 resourcePool：资源池。 queryStatus：查询状态。 enqueue：排队状态。 lane：通道。 instName：实例名称。 pid：进程ID。 blockTime：阻塞时间。 duration：持续时间。 minCpuTime：最小CPU时间。 maxCpuTime：最大CPU时间。 totalCpuTime：总CPU时间。 cpuSkewPercent：CPU倾斜率。 spillInfo：下盘信息。 minSpillSize：最小下盘大小。 maxSpillSize：最大下盘大小。 averageSpillSize：平均下盘大小。 spillSkewPercent：下盘倾斜率。 queryBand：查询标签。 jobName：作业名称。 jobInst：作业实例。 clientHostname：客户端主机名。 clientPort：客户端端口。 waiting：等待状态。 estimateTotalTime：预估总时间。 estimateLeftTime：预估剩余时间。 controlGroup：控制组。 minPeakMemory：最小峰值内存。 maxPeakMemory：最大峰值内存。 averagePeakMemory：平均峰值内存。 memorySkewPercent：内存倾斜率。 estimateMemory：预估内存。 minDnTime：最小DN时间。 maxDnTime：最大DN时间。 averageDnTime：平均DN时间。 dntimeSkewPercent：DN时间倾斜率。 warning：告警。 averagePeakIops：平均峰值IOPS。 iopsSkewPercent：IOPS倾斜率。 wlmStatus：WLM状态。 wlmAttrib：WLM属性。

        :param field: The field of this ListQueriesCondition.
        :type field: str
        """
        self._field = field

    @property
    def value(self):
        r"""Gets the value of this ListQueriesCondition.

        **参数解释**： 字段值。 **取值范围**： 不涉及。

        :return: The value of this ListQueriesCondition.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ListQueriesCondition.

        **参数解释**： 字段值。 **取值范围**： 不涉及。

        :param value: The value of this ListQueriesCondition.
        :type value: str
        """
        self._value = value

    @property
    def operator(self):
        r"""Gets the operator of this ListQueriesCondition.

        **参数解释**： 比较方式。 **取值范围**： String类型参数：=、!=、like、not like、<> int类型参数：=、!=、>、<、>=、<=、<> boolean类型参数：=、!=

        :return: The operator of this ListQueriesCondition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ListQueriesCondition.

        **参数解释**： 比较方式。 **取值范围**： String类型参数：=、!=、like、not like、<> int类型参数：=、!=、>、<、>=、<=、<> boolean类型参数：=、!=

        :param operator: The operator of this ListQueriesCondition.
        :type operator: str
        """
        self._operator = operator

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
        if not isinstance(other, ListQueriesCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
