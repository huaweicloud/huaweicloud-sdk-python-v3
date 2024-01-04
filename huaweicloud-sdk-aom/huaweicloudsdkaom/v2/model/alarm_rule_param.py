# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmRuleParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_enabled': 'bool',
        'alarm_actions': 'list[str]',
        'alarm_advice': 'str',
        'alarm_description': 'str',
        'alarm_level': 'int',
        'alarm_rule_name': 'str',
        'comparison_operator': 'str',
        'dimensions': 'list[Dimension]',
        'evaluation_periods': 'int',
        'is_turn_on': 'bool',
        'insufficient_data_actions': 'list[str]',
        'metric_name': 'str',
        'namespace': 'str',
        'ok_actions': 'list[str]',
        'period': 'int',
        'statistic': 'str',
        'threshold': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'action_enabled': 'action_enabled',
        'alarm_actions': 'alarm_actions',
        'alarm_advice': 'alarm_advice',
        'alarm_description': 'alarm_description',
        'alarm_level': 'alarm_level',
        'alarm_rule_name': 'alarm_rule_name',
        'comparison_operator': 'comparison_operator',
        'dimensions': 'dimensions',
        'evaluation_periods': 'evaluation_periods',
        'is_turn_on': 'is_turn_on',
        'insufficient_data_actions': 'insufficient_data_actions',
        'metric_name': 'metric_name',
        'namespace': 'namespace',
        'ok_actions': 'ok_actions',
        'period': 'period',
        'statistic': 'statistic',
        'threshold': 'threshold',
        'unit': 'unit'
    }

    def __init__(self, action_enabled=None, alarm_actions=None, alarm_advice=None, alarm_description=None, alarm_level=None, alarm_rule_name=None, comparison_operator=None, dimensions=None, evaluation_periods=None, is_turn_on=None, insufficient_data_actions=None, metric_name=None, namespace=None, ok_actions=None, period=None, statistic=None, threshold=None, unit=None):
        """AlarmRuleParam

        The model defined in huaweicloud sdk

        :param action_enabled: 是否启用通知。
        :type action_enabled: bool
        :param alarm_actions: 告警状态通知列表。
        :type alarm_actions: list[str]
        :param alarm_advice: 告警清除建议。
        :type alarm_advice: str
        :param alarm_description: 阈值规则描述。
        :type alarm_description: str
        :param alarm_level: 告警级别。1：紧急，2：重要，3：一般，4：提示。
        :type alarm_level: int
        :param alarm_rule_name: 阈值规则名称。规则名称包含大小写字母、数字、特殊字符（-_）和汉字组成，不能以特殊字符开头或结尾，最大长度为100。
        :type alarm_rule_name: str
        :param comparison_operator: 超限条件。&lt;：小于阈值。&gt;：大于阈值。&lt;&#x3D;：小于等于阈值。&gt;&#x3D;：大于等于阈值。
        :type comparison_operator: str
        :param dimensions: 时间序列维度。
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.Dimension`]
        :param evaluation_periods: 间隔周期。
        :type evaluation_periods: int
        :param is_turn_on: 阈值规则是否启用。
        :type is_turn_on: bool
        :param insufficient_data_actions: 数据不足通知列表。
        :type insufficient_data_actions: list[str]
        :param metric_name: 时间序列名称。名称长度取值范围为1~255个字符。
        :type metric_name: str
        :param namespace: 时间序列命名空间。
        :type namespace: str
        :param ok_actions: 正常状态通知列表。
        :type ok_actions: list[str]
        :param period: 统计周期。60000：一分钟。300000：五分钟。900000：十五分钟。3600000：一小时。
        :type period: int
        :param statistic: 统计方式。
        :type statistic: str
        :param threshold: 超限值。
        :type threshold: str
        :param unit: 时间序列单位
        :type unit: str
        """
        
        

        self._action_enabled = None
        self._alarm_actions = None
        self._alarm_advice = None
        self._alarm_description = None
        self._alarm_level = None
        self._alarm_rule_name = None
        self._comparison_operator = None
        self._dimensions = None
        self._evaluation_periods = None
        self._is_turn_on = None
        self._insufficient_data_actions = None
        self._metric_name = None
        self._namespace = None
        self._ok_actions = None
        self._period = None
        self._statistic = None
        self._threshold = None
        self._unit = None
        self.discriminator = None

        if action_enabled is not None:
            self.action_enabled = action_enabled
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if alarm_advice is not None:
            self.alarm_advice = alarm_advice
        if alarm_description is not None:
            self.alarm_description = alarm_description
        self.alarm_level = alarm_level
        self.alarm_rule_name = alarm_rule_name
        self.comparison_operator = comparison_operator
        self.dimensions = dimensions
        self.evaluation_periods = evaluation_periods
        if is_turn_on is not None:
            self.is_turn_on = is_turn_on
        if insufficient_data_actions is not None:
            self.insufficient_data_actions = insufficient_data_actions
        self.metric_name = metric_name
        self.namespace = namespace
        if ok_actions is not None:
            self.ok_actions = ok_actions
        self.period = period
        self.statistic = statistic
        self.threshold = threshold
        self.unit = unit

    @property
    def action_enabled(self):
        """Gets the action_enabled of this AlarmRuleParam.

        是否启用通知。

        :return: The action_enabled of this AlarmRuleParam.
        :rtype: bool
        """
        return self._action_enabled

    @action_enabled.setter
    def action_enabled(self, action_enabled):
        """Sets the action_enabled of this AlarmRuleParam.

        是否启用通知。

        :param action_enabled: The action_enabled of this AlarmRuleParam.
        :type action_enabled: bool
        """
        self._action_enabled = action_enabled

    @property
    def alarm_actions(self):
        """Gets the alarm_actions of this AlarmRuleParam.

        告警状态通知列表。

        :return: The alarm_actions of this AlarmRuleParam.
        :rtype: list[str]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        """Sets the alarm_actions of this AlarmRuleParam.

        告警状态通知列表。

        :param alarm_actions: The alarm_actions of this AlarmRuleParam.
        :type alarm_actions: list[str]
        """
        self._alarm_actions = alarm_actions

    @property
    def alarm_advice(self):
        """Gets the alarm_advice of this AlarmRuleParam.

        告警清除建议。

        :return: The alarm_advice of this AlarmRuleParam.
        :rtype: str
        """
        return self._alarm_advice

    @alarm_advice.setter
    def alarm_advice(self, alarm_advice):
        """Sets the alarm_advice of this AlarmRuleParam.

        告警清除建议。

        :param alarm_advice: The alarm_advice of this AlarmRuleParam.
        :type alarm_advice: str
        """
        self._alarm_advice = alarm_advice

    @property
    def alarm_description(self):
        """Gets the alarm_description of this AlarmRuleParam.

        阈值规则描述。

        :return: The alarm_description of this AlarmRuleParam.
        :rtype: str
        """
        return self._alarm_description

    @alarm_description.setter
    def alarm_description(self, alarm_description):
        """Sets the alarm_description of this AlarmRuleParam.

        阈值规则描述。

        :param alarm_description: The alarm_description of this AlarmRuleParam.
        :type alarm_description: str
        """
        self._alarm_description = alarm_description

    @property
    def alarm_level(self):
        """Gets the alarm_level of this AlarmRuleParam.

        告警级别。1：紧急，2：重要，3：一般，4：提示。

        :return: The alarm_level of this AlarmRuleParam.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this AlarmRuleParam.

        告警级别。1：紧急，2：重要，3：一般，4：提示。

        :param alarm_level: The alarm_level of this AlarmRuleParam.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def alarm_rule_name(self):
        """Gets the alarm_rule_name of this AlarmRuleParam.

        阈值规则名称。规则名称包含大小写字母、数字、特殊字符（-_）和汉字组成，不能以特殊字符开头或结尾，最大长度为100。

        :return: The alarm_rule_name of this AlarmRuleParam.
        :rtype: str
        """
        return self._alarm_rule_name

    @alarm_rule_name.setter
    def alarm_rule_name(self, alarm_rule_name):
        """Sets the alarm_rule_name of this AlarmRuleParam.

        阈值规则名称。规则名称包含大小写字母、数字、特殊字符（-_）和汉字组成，不能以特殊字符开头或结尾，最大长度为100。

        :param alarm_rule_name: The alarm_rule_name of this AlarmRuleParam.
        :type alarm_rule_name: str
        """
        self._alarm_rule_name = alarm_rule_name

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this AlarmRuleParam.

        超限条件。<：小于阈值。>：大于阈值。<=：小于等于阈值。>=：大于等于阈值。

        :return: The comparison_operator of this AlarmRuleParam.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this AlarmRuleParam.

        超限条件。<：小于阈值。>：大于阈值。<=：小于等于阈值。>=：大于等于阈值。

        :param comparison_operator: The comparison_operator of this AlarmRuleParam.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def dimensions(self):
        """Gets the dimensions of this AlarmRuleParam.

        时间序列维度。

        :return: The dimensions of this AlarmRuleParam.
        :rtype: list[:class:`huaweicloudsdkaom.v2.Dimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this AlarmRuleParam.

        时间序列维度。

        :param dimensions: The dimensions of this AlarmRuleParam.
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.Dimension`]
        """
        self._dimensions = dimensions

    @property
    def evaluation_periods(self):
        """Gets the evaluation_periods of this AlarmRuleParam.

        间隔周期。

        :return: The evaluation_periods of this AlarmRuleParam.
        :rtype: int
        """
        return self._evaluation_periods

    @evaluation_periods.setter
    def evaluation_periods(self, evaluation_periods):
        """Sets the evaluation_periods of this AlarmRuleParam.

        间隔周期。

        :param evaluation_periods: The evaluation_periods of this AlarmRuleParam.
        :type evaluation_periods: int
        """
        self._evaluation_periods = evaluation_periods

    @property
    def is_turn_on(self):
        """Gets the is_turn_on of this AlarmRuleParam.

        阈值规则是否启用。

        :return: The is_turn_on of this AlarmRuleParam.
        :rtype: bool
        """
        return self._is_turn_on

    @is_turn_on.setter
    def is_turn_on(self, is_turn_on):
        """Sets the is_turn_on of this AlarmRuleParam.

        阈值规则是否启用。

        :param is_turn_on: The is_turn_on of this AlarmRuleParam.
        :type is_turn_on: bool
        """
        self._is_turn_on = is_turn_on

    @property
    def insufficient_data_actions(self):
        """Gets the insufficient_data_actions of this AlarmRuleParam.

        数据不足通知列表。

        :return: The insufficient_data_actions of this AlarmRuleParam.
        :rtype: list[str]
        """
        return self._insufficient_data_actions

    @insufficient_data_actions.setter
    def insufficient_data_actions(self, insufficient_data_actions):
        """Sets the insufficient_data_actions of this AlarmRuleParam.

        数据不足通知列表。

        :param insufficient_data_actions: The insufficient_data_actions of this AlarmRuleParam.
        :type insufficient_data_actions: list[str]
        """
        self._insufficient_data_actions = insufficient_data_actions

    @property
    def metric_name(self):
        """Gets the metric_name of this AlarmRuleParam.

        时间序列名称。名称长度取值范围为1~255个字符。

        :return: The metric_name of this AlarmRuleParam.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this AlarmRuleParam.

        时间序列名称。名称长度取值范围为1~255个字符。

        :param metric_name: The metric_name of this AlarmRuleParam.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def namespace(self):
        """Gets the namespace of this AlarmRuleParam.

        时间序列命名空间。

        :return: The namespace of this AlarmRuleParam.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AlarmRuleParam.

        时间序列命名空间。

        :param namespace: The namespace of this AlarmRuleParam.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def ok_actions(self):
        """Gets the ok_actions of this AlarmRuleParam.

        正常状态通知列表。

        :return: The ok_actions of this AlarmRuleParam.
        :rtype: list[str]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        """Sets the ok_actions of this AlarmRuleParam.

        正常状态通知列表。

        :param ok_actions: The ok_actions of this AlarmRuleParam.
        :type ok_actions: list[str]
        """
        self._ok_actions = ok_actions

    @property
    def period(self):
        """Gets the period of this AlarmRuleParam.

        统计周期。60000：一分钟。300000：五分钟。900000：十五分钟。3600000：一小时。

        :return: The period of this AlarmRuleParam.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this AlarmRuleParam.

        统计周期。60000：一分钟。300000：五分钟。900000：十五分钟。3600000：一小时。

        :param period: The period of this AlarmRuleParam.
        :type period: int
        """
        self._period = period

    @property
    def statistic(self):
        """Gets the statistic of this AlarmRuleParam.

        统计方式。

        :return: The statistic of this AlarmRuleParam.
        :rtype: str
        """
        return self._statistic

    @statistic.setter
    def statistic(self, statistic):
        """Sets the statistic of this AlarmRuleParam.

        统计方式。

        :param statistic: The statistic of this AlarmRuleParam.
        :type statistic: str
        """
        self._statistic = statistic

    @property
    def threshold(self):
        """Gets the threshold of this AlarmRuleParam.

        超限值。

        :return: The threshold of this AlarmRuleParam.
        :rtype: str
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this AlarmRuleParam.

        超限值。

        :param threshold: The threshold of this AlarmRuleParam.
        :type threshold: str
        """
        self._threshold = threshold

    @property
    def unit(self):
        """Gets the unit of this AlarmRuleParam.

        时间序列单位

        :return: The unit of this AlarmRuleParam.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this AlarmRuleParam.

        时间序列单位

        :param unit: The unit of this AlarmRuleParam.
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
        if not isinstance(other, AlarmRuleParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
