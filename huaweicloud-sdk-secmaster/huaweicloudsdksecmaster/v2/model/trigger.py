# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Trigger:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accumulated_times': 'int',
        'expression': 'str',
        'job_id': 'str',
        'mode': 'str',
        'operator': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'accumulated_times': 'accumulated_times',
        'expression': 'expression',
        'job_id': 'job_id',
        'mode': 'mode',
        'operator': 'operator',
        'severity': 'severity'
    }

    def __init__(self, accumulated_times=None, expression=None, job_id=None, mode=None, operator=None, severity=None):
        r"""Trigger

        The model defined in huaweicloud sdk

        :param accumulated_times: 累计次数
        :type accumulated_times: int
        :param expression: 表达式
        :type expression: str
        :param job_id: UUID
        :type job_id: str
        :param mode: **参数解释**: 模式 - COUNT 计数  **约束限制** 不涉及 **取值范围**: - COUNT  **默认值** 不涉及        
        :type mode: str
        :param operator: **参数解释**: 操作符类型 - GT 大于 - LT 小于 - EQ 等于 - NE 不等于  **约束限制** 不涉及 **取值范围**: - GT - LT - EQ - NE  **默认值** 不涉及     
        :type operator: str
        :param severity: **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及  
        :type severity: str
        """
        
        

        self._accumulated_times = None
        self._expression = None
        self._job_id = None
        self._mode = None
        self._operator = None
        self._severity = None
        self.discriminator = None

        if accumulated_times is not None:
            self.accumulated_times = accumulated_times
        if expression is not None:
            self.expression = expression
        if job_id is not None:
            self.job_id = job_id
        if mode is not None:
            self.mode = mode
        if operator is not None:
            self.operator = operator
        if severity is not None:
            self.severity = severity

    @property
    def accumulated_times(self):
        r"""Gets the accumulated_times of this Trigger.

        累计次数

        :return: The accumulated_times of this Trigger.
        :rtype: int
        """
        return self._accumulated_times

    @accumulated_times.setter
    def accumulated_times(self, accumulated_times):
        r"""Sets the accumulated_times of this Trigger.

        累计次数

        :param accumulated_times: The accumulated_times of this Trigger.
        :type accumulated_times: int
        """
        self._accumulated_times = accumulated_times

    @property
    def expression(self):
        r"""Gets the expression of this Trigger.

        表达式

        :return: The expression of this Trigger.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this Trigger.

        表达式

        :param expression: The expression of this Trigger.
        :type expression: str
        """
        self._expression = expression

    @property
    def job_id(self):
        r"""Gets the job_id of this Trigger.

        UUID

        :return: The job_id of this Trigger.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this Trigger.

        UUID

        :param job_id: The job_id of this Trigger.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def mode(self):
        r"""Gets the mode of this Trigger.

        **参数解释**: 模式 - COUNT 计数  **约束限制** 不涉及 **取值范围**: - COUNT  **默认值** 不涉及        

        :return: The mode of this Trigger.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this Trigger.

        **参数解释**: 模式 - COUNT 计数  **约束限制** 不涉及 **取值范围**: - COUNT  **默认值** 不涉及        

        :param mode: The mode of this Trigger.
        :type mode: str
        """
        self._mode = mode

    @property
    def operator(self):
        r"""Gets the operator of this Trigger.

        **参数解释**: 操作符类型 - GT 大于 - LT 小于 - EQ 等于 - NE 不等于  **约束限制** 不涉及 **取值范围**: - GT - LT - EQ - NE  **默认值** 不涉及     

        :return: The operator of this Trigger.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this Trigger.

        **参数解释**: 操作符类型 - GT 大于 - LT 小于 - EQ 等于 - NE 不等于  **约束限制** 不涉及 **取值范围**: - GT - LT - EQ - NE  **默认值** 不涉及     

        :param operator: The operator of this Trigger.
        :type operator: str
        """
        self._operator = operator

    @property
    def severity(self):
        r"""Gets the severity of this Trigger.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及  

        :return: The severity of this Trigger.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this Trigger.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及  

        :param severity: The severity of this Trigger.
        :type severity: str
        """
        self._severity = severity

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
        if not isinstance(other, Trigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
