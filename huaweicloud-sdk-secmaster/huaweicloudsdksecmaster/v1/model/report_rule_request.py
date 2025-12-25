# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule': 'str',
        'rule_end': 'str',
        'start_time': 'ReportRuleRequestStartTime',
        'end_time': 'ReportRuleRequestEndTime'
    }

    attribute_map = {
        'rule': 'rule',
        'rule_end': 'rule_end',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, rule=None, rule_end=None, start_time=None, end_time=None):
        r"""ReportRuleRequest

        The model defined in huaweicloud sdk

        :param rule: 报告发送任务cron表达式
        :type rule: str
        :param rule_end: 报告发送任务启动截止时间
        :type rule_end: str
        :param start_time: 
        :type start_time: :class:`huaweicloudsdksecmaster.v1.ReportRuleRequestStartTime`
        :param end_time: 
        :type end_time: :class:`huaweicloudsdksecmaster.v1.ReportRuleRequestEndTime`
        """
        
        

        self._rule = None
        self._rule_end = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if rule is not None:
            self.rule = rule
        if rule_end is not None:
            self.rule_end = rule_end
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def rule(self):
        r"""Gets the rule of this ReportRuleRequest.

        报告发送任务cron表达式

        :return: The rule of this ReportRuleRequest.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this ReportRuleRequest.

        报告发送任务cron表达式

        :param rule: The rule of this ReportRuleRequest.
        :type rule: str
        """
        self._rule = rule

    @property
    def rule_end(self):
        r"""Gets the rule_end of this ReportRuleRequest.

        报告发送任务启动截止时间

        :return: The rule_end of this ReportRuleRequest.
        :rtype: str
        """
        return self._rule_end

    @rule_end.setter
    def rule_end(self, rule_end):
        r"""Sets the rule_end of this ReportRuleRequest.

        报告发送任务启动截止时间

        :param rule_end: The rule_end of this ReportRuleRequest.
        :type rule_end: str
        """
        self._rule_end = rule_end

    @property
    def start_time(self):
        r"""Gets the start_time of this ReportRuleRequest.

        :return: The start_time of this ReportRuleRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ReportRuleRequestStartTime`
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ReportRuleRequest.

        :param start_time: The start_time of this ReportRuleRequest.
        :type start_time: :class:`huaweicloudsdksecmaster.v1.ReportRuleRequestStartTime`
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ReportRuleRequest.

        :return: The end_time of this ReportRuleRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ReportRuleRequestEndTime`
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ReportRuleRequest.

        :param end_time: The end_time of this ReportRuleRequest.
        :type end_time: :class:`huaweicloudsdksecmaster.v1.ReportRuleRequestEndTime`
        """
        self._end_time = end_time

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
        if not isinstance(other, ReportRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
