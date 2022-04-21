# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAlarmResult:

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
        'alarm_level': 'str',
        'alarm_rule_id': 'str',
        'alarm_rule_name': 'str',
        'comparison_operator': 'str',
        'dimensions': 'list[Dimension]',
        'evaluation_periods': 'int',
        'id_turn_on': 'bool',
        'insufficient_data_actions': 'list[str]',
        'metric_name': 'str',
        'namespace': 'str',
        'ok_actions': 'list[str]',
        'period': 'int',
        'policy_name': 'str',
        'resources': 'list[str]',
        'state_reason': 'str',
        'state_updated_timestamp': 'str',
        'state_value': 'str',
        'statistic': 'str',
        'threshold': 'str',
        'type': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'action_enabled': 'action_enabled',
        'alarm_actions': 'alarm_actions',
        'alarm_advice': 'alarm_advice',
        'alarm_description': 'alarm_description',
        'alarm_level': 'alarm_level',
        'alarm_rule_id': 'alarm_rule_id',
        'alarm_rule_name': 'alarm_rule_name',
        'comparison_operator': 'comparison_operator',
        'dimensions': 'dimensions',
        'evaluation_periods': 'evaluation_periods',
        'id_turn_on': 'id_turn_on',
        'insufficient_data_actions': 'insufficient_data_actions',
        'metric_name': 'metric_name',
        'namespace': 'namespace',
        'ok_actions': 'ok_actions',
        'period': 'period',
        'policy_name': 'policy_name',
        'resources': 'resources',
        'state_reason': 'state_reason',
        'state_updated_timestamp': 'state_updated_timestamp',
        'state_value': 'state_value',
        'statistic': 'statistic',
        'threshold': 'threshold',
        'type': 'type',
        'unit': 'unit'
    }

    def __init__(self, action_enabled=None, alarm_actions=None, alarm_advice=None, alarm_description=None, alarm_level=None, alarm_rule_id=None, alarm_rule_name=None, comparison_operator=None, dimensions=None, evaluation_periods=None, id_turn_on=None, insufficient_data_actions=None, metric_name=None, namespace=None, ok_actions=None, period=None, policy_name=None, resources=None, state_reason=None, state_updated_timestamp=None, state_value=None, statistic=None, threshold=None, type=None, unit=None):
        """QueryAlarmResult

        The model defined in huaweicloud sdk

        :param action_enabled: 是否启用通知。
        :type action_enabled: bool
        :param alarm_actions: 告警状态通知列表。
        :type alarm_actions: list[str]
        :param alarm_advice: 告警清除建议。
        :type alarm_advice: str
        :param alarm_description: 阈值规则描述。
        :type alarm_description: str
        :param alarm_level: 告警级别。
        :type alarm_level: str
        :param alarm_rule_id: 阈值规则ID。
        :type alarm_rule_id: str
        :param alarm_rule_name: 阈值规则名称。
        :type alarm_rule_name: str
        :param comparison_operator: 极限条件。
        :type comparison_operator: str
        :param dimensions: 时间序列维度。
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.Dimension`]
        :param evaluation_periods: 间隔周期。
        :type evaluation_periods: int
        :param id_turn_on: 阈值规则是否启用。
        :type id_turn_on: bool
        :param insufficient_data_actions: 数据不足通知列表。
        :type insufficient_data_actions: list[str]
        :param metric_name: 时间序列名称。
        :type metric_name: str
        :param namespace: 时间序列命名空间。
        :type namespace: str
        :param ok_actions: 正常状态通知列表。
        :type ok_actions: list[str]
        :param period: 统计周期。
        :type period: int
        :param policy_name: 阈值规则模板名称。
        :type policy_name: str
        :param resources: 资源信息(已废弃)。
        :type resources: list[str]
        :param state_reason: 原因描述。
        :type state_reason: str
        :param state_updated_timestamp: 状态更新时间戳。
        :type state_updated_timestamp: str
        :param state_value: 服务状态。
        :type state_value: str
        :param statistic: 统计方式。
        :type statistic: str
        :param threshold: 临界值。
        :type threshold: str
        :param type: 阈值规则类型。
        :type type: str
        :param unit: 阈值单元。
        :type unit: str
        """
        
        

        self._action_enabled = None
        self._alarm_actions = None
        self._alarm_advice = None
        self._alarm_description = None
        self._alarm_level = None
        self._alarm_rule_id = None
        self._alarm_rule_name = None
        self._comparison_operator = None
        self._dimensions = None
        self._evaluation_periods = None
        self._id_turn_on = None
        self._insufficient_data_actions = None
        self._metric_name = None
        self._namespace = None
        self._ok_actions = None
        self._period = None
        self._policy_name = None
        self._resources = None
        self._state_reason = None
        self._state_updated_timestamp = None
        self._state_value = None
        self._statistic = None
        self._threshold = None
        self._type = None
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
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if alarm_rule_id is not None:
            self.alarm_rule_id = alarm_rule_id
        if alarm_rule_name is not None:
            self.alarm_rule_name = alarm_rule_name
        if comparison_operator is not None:
            self.comparison_operator = comparison_operator
        if dimensions is not None:
            self.dimensions = dimensions
        if evaluation_periods is not None:
            self.evaluation_periods = evaluation_periods
        if id_turn_on is not None:
            self.id_turn_on = id_turn_on
        if insufficient_data_actions is not None:
            self.insufficient_data_actions = insufficient_data_actions
        if metric_name is not None:
            self.metric_name = metric_name
        if namespace is not None:
            self.namespace = namespace
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if period is not None:
            self.period = period
        if policy_name is not None:
            self.policy_name = policy_name
        if resources is not None:
            self.resources = resources
        if state_reason is not None:
            self.state_reason = state_reason
        if state_updated_timestamp is not None:
            self.state_updated_timestamp = state_updated_timestamp
        if state_value is not None:
            self.state_value = state_value
        if statistic is not None:
            self.statistic = statistic
        if threshold is not None:
            self.threshold = threshold
        if type is not None:
            self.type = type
        if unit is not None:
            self.unit = unit

    @property
    def action_enabled(self):
        """Gets the action_enabled of this QueryAlarmResult.

        是否启用通知。

        :return: The action_enabled of this QueryAlarmResult.
        :rtype: bool
        """
        return self._action_enabled

    @action_enabled.setter
    def action_enabled(self, action_enabled):
        """Sets the action_enabled of this QueryAlarmResult.

        是否启用通知。

        :param action_enabled: The action_enabled of this QueryAlarmResult.
        :type action_enabled: bool
        """
        self._action_enabled = action_enabled

    @property
    def alarm_actions(self):
        """Gets the alarm_actions of this QueryAlarmResult.

        告警状态通知列表。

        :return: The alarm_actions of this QueryAlarmResult.
        :rtype: list[str]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        """Sets the alarm_actions of this QueryAlarmResult.

        告警状态通知列表。

        :param alarm_actions: The alarm_actions of this QueryAlarmResult.
        :type alarm_actions: list[str]
        """
        self._alarm_actions = alarm_actions

    @property
    def alarm_advice(self):
        """Gets the alarm_advice of this QueryAlarmResult.

        告警清除建议。

        :return: The alarm_advice of this QueryAlarmResult.
        :rtype: str
        """
        return self._alarm_advice

    @alarm_advice.setter
    def alarm_advice(self, alarm_advice):
        """Sets the alarm_advice of this QueryAlarmResult.

        告警清除建议。

        :param alarm_advice: The alarm_advice of this QueryAlarmResult.
        :type alarm_advice: str
        """
        self._alarm_advice = alarm_advice

    @property
    def alarm_description(self):
        """Gets the alarm_description of this QueryAlarmResult.

        阈值规则描述。

        :return: The alarm_description of this QueryAlarmResult.
        :rtype: str
        """
        return self._alarm_description

    @alarm_description.setter
    def alarm_description(self, alarm_description):
        """Sets the alarm_description of this QueryAlarmResult.

        阈值规则描述。

        :param alarm_description: The alarm_description of this QueryAlarmResult.
        :type alarm_description: str
        """
        self._alarm_description = alarm_description

    @property
    def alarm_level(self):
        """Gets the alarm_level of this QueryAlarmResult.

        告警级别。

        :return: The alarm_level of this QueryAlarmResult.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this QueryAlarmResult.

        告警级别。

        :param alarm_level: The alarm_level of this QueryAlarmResult.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def alarm_rule_id(self):
        """Gets the alarm_rule_id of this QueryAlarmResult.

        阈值规则ID。

        :return: The alarm_rule_id of this QueryAlarmResult.
        :rtype: str
        """
        return self._alarm_rule_id

    @alarm_rule_id.setter
    def alarm_rule_id(self, alarm_rule_id):
        """Sets the alarm_rule_id of this QueryAlarmResult.

        阈值规则ID。

        :param alarm_rule_id: The alarm_rule_id of this QueryAlarmResult.
        :type alarm_rule_id: str
        """
        self._alarm_rule_id = alarm_rule_id

    @property
    def alarm_rule_name(self):
        """Gets the alarm_rule_name of this QueryAlarmResult.

        阈值规则名称。

        :return: The alarm_rule_name of this QueryAlarmResult.
        :rtype: str
        """
        return self._alarm_rule_name

    @alarm_rule_name.setter
    def alarm_rule_name(self, alarm_rule_name):
        """Sets the alarm_rule_name of this QueryAlarmResult.

        阈值规则名称。

        :param alarm_rule_name: The alarm_rule_name of this QueryAlarmResult.
        :type alarm_rule_name: str
        """
        self._alarm_rule_name = alarm_rule_name

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this QueryAlarmResult.

        极限条件。

        :return: The comparison_operator of this QueryAlarmResult.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this QueryAlarmResult.

        极限条件。

        :param comparison_operator: The comparison_operator of this QueryAlarmResult.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def dimensions(self):
        """Gets the dimensions of this QueryAlarmResult.

        时间序列维度。

        :return: The dimensions of this QueryAlarmResult.
        :rtype: list[:class:`huaweicloudsdkaom.v2.Dimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this QueryAlarmResult.

        时间序列维度。

        :param dimensions: The dimensions of this QueryAlarmResult.
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.Dimension`]
        """
        self._dimensions = dimensions

    @property
    def evaluation_periods(self):
        """Gets the evaluation_periods of this QueryAlarmResult.

        间隔周期。

        :return: The evaluation_periods of this QueryAlarmResult.
        :rtype: int
        """
        return self._evaluation_periods

    @evaluation_periods.setter
    def evaluation_periods(self, evaluation_periods):
        """Sets the evaluation_periods of this QueryAlarmResult.

        间隔周期。

        :param evaluation_periods: The evaluation_periods of this QueryAlarmResult.
        :type evaluation_periods: int
        """
        self._evaluation_periods = evaluation_periods

    @property
    def id_turn_on(self):
        """Gets the id_turn_on of this QueryAlarmResult.

        阈值规则是否启用。

        :return: The id_turn_on of this QueryAlarmResult.
        :rtype: bool
        """
        return self._id_turn_on

    @id_turn_on.setter
    def id_turn_on(self, id_turn_on):
        """Sets the id_turn_on of this QueryAlarmResult.

        阈值规则是否启用。

        :param id_turn_on: The id_turn_on of this QueryAlarmResult.
        :type id_turn_on: bool
        """
        self._id_turn_on = id_turn_on

    @property
    def insufficient_data_actions(self):
        """Gets the insufficient_data_actions of this QueryAlarmResult.

        数据不足通知列表。

        :return: The insufficient_data_actions of this QueryAlarmResult.
        :rtype: list[str]
        """
        return self._insufficient_data_actions

    @insufficient_data_actions.setter
    def insufficient_data_actions(self, insufficient_data_actions):
        """Sets the insufficient_data_actions of this QueryAlarmResult.

        数据不足通知列表。

        :param insufficient_data_actions: The insufficient_data_actions of this QueryAlarmResult.
        :type insufficient_data_actions: list[str]
        """
        self._insufficient_data_actions = insufficient_data_actions

    @property
    def metric_name(self):
        """Gets the metric_name of this QueryAlarmResult.

        时间序列名称。

        :return: The metric_name of this QueryAlarmResult.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this QueryAlarmResult.

        时间序列名称。

        :param metric_name: The metric_name of this QueryAlarmResult.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def namespace(self):
        """Gets the namespace of this QueryAlarmResult.

        时间序列命名空间。

        :return: The namespace of this QueryAlarmResult.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this QueryAlarmResult.

        时间序列命名空间。

        :param namespace: The namespace of this QueryAlarmResult.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def ok_actions(self):
        """Gets the ok_actions of this QueryAlarmResult.

        正常状态通知列表。

        :return: The ok_actions of this QueryAlarmResult.
        :rtype: list[str]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        """Sets the ok_actions of this QueryAlarmResult.

        正常状态通知列表。

        :param ok_actions: The ok_actions of this QueryAlarmResult.
        :type ok_actions: list[str]
        """
        self._ok_actions = ok_actions

    @property
    def period(self):
        """Gets the period of this QueryAlarmResult.

        统计周期。

        :return: The period of this QueryAlarmResult.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this QueryAlarmResult.

        统计周期。

        :param period: The period of this QueryAlarmResult.
        :type period: int
        """
        self._period = period

    @property
    def policy_name(self):
        """Gets the policy_name of this QueryAlarmResult.

        阈值规则模板名称。

        :return: The policy_name of this QueryAlarmResult.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this QueryAlarmResult.

        阈值规则模板名称。

        :param policy_name: The policy_name of this QueryAlarmResult.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def resources(self):
        """Gets the resources of this QueryAlarmResult.

        资源信息(已废弃)。

        :return: The resources of this QueryAlarmResult.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this QueryAlarmResult.

        资源信息(已废弃)。

        :param resources: The resources of this QueryAlarmResult.
        :type resources: list[str]
        """
        self._resources = resources

    @property
    def state_reason(self):
        """Gets the state_reason of this QueryAlarmResult.

        原因描述。

        :return: The state_reason of this QueryAlarmResult.
        :rtype: str
        """
        return self._state_reason

    @state_reason.setter
    def state_reason(self, state_reason):
        """Sets the state_reason of this QueryAlarmResult.

        原因描述。

        :param state_reason: The state_reason of this QueryAlarmResult.
        :type state_reason: str
        """
        self._state_reason = state_reason

    @property
    def state_updated_timestamp(self):
        """Gets the state_updated_timestamp of this QueryAlarmResult.

        状态更新时间戳。

        :return: The state_updated_timestamp of this QueryAlarmResult.
        :rtype: str
        """
        return self._state_updated_timestamp

    @state_updated_timestamp.setter
    def state_updated_timestamp(self, state_updated_timestamp):
        """Sets the state_updated_timestamp of this QueryAlarmResult.

        状态更新时间戳。

        :param state_updated_timestamp: The state_updated_timestamp of this QueryAlarmResult.
        :type state_updated_timestamp: str
        """
        self._state_updated_timestamp = state_updated_timestamp

    @property
    def state_value(self):
        """Gets the state_value of this QueryAlarmResult.

        服务状态。

        :return: The state_value of this QueryAlarmResult.
        :rtype: str
        """
        return self._state_value

    @state_value.setter
    def state_value(self, state_value):
        """Sets the state_value of this QueryAlarmResult.

        服务状态。

        :param state_value: The state_value of this QueryAlarmResult.
        :type state_value: str
        """
        self._state_value = state_value

    @property
    def statistic(self):
        """Gets the statistic of this QueryAlarmResult.

        统计方式。

        :return: The statistic of this QueryAlarmResult.
        :rtype: str
        """
        return self._statistic

    @statistic.setter
    def statistic(self, statistic):
        """Sets the statistic of this QueryAlarmResult.

        统计方式。

        :param statistic: The statistic of this QueryAlarmResult.
        :type statistic: str
        """
        self._statistic = statistic

    @property
    def threshold(self):
        """Gets the threshold of this QueryAlarmResult.

        临界值。

        :return: The threshold of this QueryAlarmResult.
        :rtype: str
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this QueryAlarmResult.

        临界值。

        :param threshold: The threshold of this QueryAlarmResult.
        :type threshold: str
        """
        self._threshold = threshold

    @property
    def type(self):
        """Gets the type of this QueryAlarmResult.

        阈值规则类型。

        :return: The type of this QueryAlarmResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QueryAlarmResult.

        阈值规则类型。

        :param type: The type of this QueryAlarmResult.
        :type type: str
        """
        self._type = type

    @property
    def unit(self):
        """Gets the unit of this QueryAlarmResult.

        阈值单元。

        :return: The unit of this QueryAlarmResult.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this QueryAlarmResult.

        阈值单元。

        :param unit: The unit of this QueryAlarmResult.
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
        if not isinstance(other, QueryAlarmResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
