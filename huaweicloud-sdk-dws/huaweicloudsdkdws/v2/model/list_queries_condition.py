# coding: utf-8

import six

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
        """ListQueriesCondition

        The model defined in huaweicloud sdk

        :param field: 字段名称参考下方字段列表 systemQuery boolean 是否隐藏系统查询 userName String 用户名称 applicationName String 应用名称 dbName String 数据库名称 resourcePool String 资源池 queryStatus String 查询状态 enqueue String 排队状态 lane String 快慢车道 instName String 接入CN pid String 会话ID blockTime int 阻塞时间（ms） duration int 执行时间（ms） minCpuTime int 最小cpu时间（ms） maxCpuTime int 最大cpu时间（ms） totalCpuTime int CPU时间（ms） cpuSkewPercent int CPU时间倾斜（%） spillInfo String dn下盘信息 minSpillSize int dn上下盘的最小数据量（mb） maxSpillSize int dn上下盘的最大数据量（mb） averageSpillSize int 平均下盘量（MB） spillSkewPercent int dn间下盘倾斜率 queryBand String 作业类型 jobName String 任务名称 jobInst String 任务实例 clientHostname String 主机名称 clientPort String TCP端口 waiting boolean 是否等待 estimateTotalTime int 预估总执行时间（ms） estimateLeftTime int 预估剩余时间（ms） controlGroup String cgroup minPeakMemory int dn最小内存峰值（mb） maxPeakMemory int dn最大内存峰值（mb） averagePeakMemory int 内存使用平均值（mb） memorySkewPercent int 各dn内存使用倾斜率 estimateMemory int 预估使用内存（mb） minDnTime int dn最小执行时间（ms） maxDnTime int dn最大执行时间（ms） averageDnTime int dn平均执行时间（ms） dntimeSkewPercent int 各dn的执行时间倾斜率 warning String 告警 averagePeakIops int dn每秒平均io 峰值（列存是次/s，行存是万次/s） iopsSkewPercent int dn间的io倾斜率 wlmStatus String 语句运行状态 wlmAttrib String 语句属性
        :type field: str
        :param value: 字段值
        :type value: str
        :param operator: 比较方式： String类型参数：&#x3D;、!&#x3D;、like、not like int类型参数：&#x3D;、!&#x3D;、&gt;、&lt;、&gt;&#x3D;、&lt;&#x3D; boolean类型参数：&#x3D;、!&#x3D;
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
        """Gets the field of this ListQueriesCondition.

        字段名称参考下方字段列表 systemQuery boolean 是否隐藏系统查询 userName String 用户名称 applicationName String 应用名称 dbName String 数据库名称 resourcePool String 资源池 queryStatus String 查询状态 enqueue String 排队状态 lane String 快慢车道 instName String 接入CN pid String 会话ID blockTime int 阻塞时间（ms） duration int 执行时间（ms） minCpuTime int 最小cpu时间（ms） maxCpuTime int 最大cpu时间（ms） totalCpuTime int CPU时间（ms） cpuSkewPercent int CPU时间倾斜（%） spillInfo String dn下盘信息 minSpillSize int dn上下盘的最小数据量（mb） maxSpillSize int dn上下盘的最大数据量（mb） averageSpillSize int 平均下盘量（MB） spillSkewPercent int dn间下盘倾斜率 queryBand String 作业类型 jobName String 任务名称 jobInst String 任务实例 clientHostname String 主机名称 clientPort String TCP端口 waiting boolean 是否等待 estimateTotalTime int 预估总执行时间（ms） estimateLeftTime int 预估剩余时间（ms） controlGroup String cgroup minPeakMemory int dn最小内存峰值（mb） maxPeakMemory int dn最大内存峰值（mb） averagePeakMemory int 内存使用平均值（mb） memorySkewPercent int 各dn内存使用倾斜率 estimateMemory int 预估使用内存（mb） minDnTime int dn最小执行时间（ms） maxDnTime int dn最大执行时间（ms） averageDnTime int dn平均执行时间（ms） dntimeSkewPercent int 各dn的执行时间倾斜率 warning String 告警 averagePeakIops int dn每秒平均io 峰值（列存是次/s，行存是万次/s） iopsSkewPercent int dn间的io倾斜率 wlmStatus String 语句运行状态 wlmAttrib String 语句属性

        :return: The field of this ListQueriesCondition.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this ListQueriesCondition.

        字段名称参考下方字段列表 systemQuery boolean 是否隐藏系统查询 userName String 用户名称 applicationName String 应用名称 dbName String 数据库名称 resourcePool String 资源池 queryStatus String 查询状态 enqueue String 排队状态 lane String 快慢车道 instName String 接入CN pid String 会话ID blockTime int 阻塞时间（ms） duration int 执行时间（ms） minCpuTime int 最小cpu时间（ms） maxCpuTime int 最大cpu时间（ms） totalCpuTime int CPU时间（ms） cpuSkewPercent int CPU时间倾斜（%） spillInfo String dn下盘信息 minSpillSize int dn上下盘的最小数据量（mb） maxSpillSize int dn上下盘的最大数据量（mb） averageSpillSize int 平均下盘量（MB） spillSkewPercent int dn间下盘倾斜率 queryBand String 作业类型 jobName String 任务名称 jobInst String 任务实例 clientHostname String 主机名称 clientPort String TCP端口 waiting boolean 是否等待 estimateTotalTime int 预估总执行时间（ms） estimateLeftTime int 预估剩余时间（ms） controlGroup String cgroup minPeakMemory int dn最小内存峰值（mb） maxPeakMemory int dn最大内存峰值（mb） averagePeakMemory int 内存使用平均值（mb） memorySkewPercent int 各dn内存使用倾斜率 estimateMemory int 预估使用内存（mb） minDnTime int dn最小执行时间（ms） maxDnTime int dn最大执行时间（ms） averageDnTime int dn平均执行时间（ms） dntimeSkewPercent int 各dn的执行时间倾斜率 warning String 告警 averagePeakIops int dn每秒平均io 峰值（列存是次/s，行存是万次/s） iopsSkewPercent int dn间的io倾斜率 wlmStatus String 语句运行状态 wlmAttrib String 语句属性

        :param field: The field of this ListQueriesCondition.
        :type field: str
        """
        self._field = field

    @property
    def value(self):
        """Gets the value of this ListQueriesCondition.

        字段值

        :return: The value of this ListQueriesCondition.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ListQueriesCondition.

        字段值

        :param value: The value of this ListQueriesCondition.
        :type value: str
        """
        self._value = value

    @property
    def operator(self):
        """Gets the operator of this ListQueriesCondition.

        比较方式： String类型参数：=、!=、like、not like int类型参数：=、!=、>、<、>=、<= boolean类型参数：=、!=

        :return: The operator of this ListQueriesCondition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ListQueriesCondition.

        比较方式： String类型参数：=、!=、like、not like int类型参数：=、!=、>、<、>=、<= boolean类型参数：=、!=

        :param operator: The operator of this ListQueriesCondition.
        :type operator: str
        """
        self._operator = operator

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
        if not isinstance(other, ListQueriesCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
