# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InteractionRuleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_index': 'str',
        'rule_name': 'str',
        'enabled': 'bool',
        'event_type': 'int',
        'hit_condition': 'HitCondition',
        'trigger': 'TriggerProcess',
        'review_config': 'ReviewConfig'
    }

    attribute_map = {
        'rule_index': 'rule_index',
        'rule_name': 'rule_name',
        'enabled': 'enabled',
        'event_type': 'event_type',
        'hit_condition': 'hit_condition',
        'trigger': 'trigger',
        'review_config': 'review_config'
    }

    def __init__(self, rule_index=None, rule_name=None, enabled=None, event_type=None, hit_condition=None, trigger=None, review_config=None):
        """InteractionRuleInfo

        The model defined in huaweicloud sdk

        :param rule_index: 规则索引
        :type rule_index: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param enabled: 是否启用
        :type enabled: bool
        :param event_type: 事件类型。 * 1：弹幕事件 * 2：用户入场事件 * 3：用户点赞事件 * 4：用户送礼事件 * 10: 预置话术事件
        :type event_type: int
        :param hit_condition: 
        :type hit_condition: :class:`huaweicloudsdkmetastudio.v1.HitCondition`
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkmetastudio.v1.TriggerProcess`
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        
        

        self._rule_index = None
        self._rule_name = None
        self._enabled = None
        self._event_type = None
        self._hit_condition = None
        self._trigger = None
        self._review_config = None
        self.discriminator = None

        if rule_index is not None:
            self.rule_index = rule_index
        if rule_name is not None:
            self.rule_name = rule_name
        if enabled is not None:
            self.enabled = enabled
        if event_type is not None:
            self.event_type = event_type
        if hit_condition is not None:
            self.hit_condition = hit_condition
        if trigger is not None:
            self.trigger = trigger
        if review_config is not None:
            self.review_config = review_config

    @property
    def rule_index(self):
        """Gets the rule_index of this InteractionRuleInfo.

        规则索引

        :return: The rule_index of this InteractionRuleInfo.
        :rtype: str
        """
        return self._rule_index

    @rule_index.setter
    def rule_index(self, rule_index):
        """Sets the rule_index of this InteractionRuleInfo.

        规则索引

        :param rule_index: The rule_index of this InteractionRuleInfo.
        :type rule_index: str
        """
        self._rule_index = rule_index

    @property
    def rule_name(self):
        """Gets the rule_name of this InteractionRuleInfo.

        规则名称

        :return: The rule_name of this InteractionRuleInfo.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this InteractionRuleInfo.

        规则名称

        :param rule_name: The rule_name of this InteractionRuleInfo.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def enabled(self):
        """Gets the enabled of this InteractionRuleInfo.

        是否启用

        :return: The enabled of this InteractionRuleInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this InteractionRuleInfo.

        是否启用

        :param enabled: The enabled of this InteractionRuleInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def event_type(self):
        """Gets the event_type of this InteractionRuleInfo.

        事件类型。 * 1：弹幕事件 * 2：用户入场事件 * 3：用户点赞事件 * 4：用户送礼事件 * 10: 预置话术事件

        :return: The event_type of this InteractionRuleInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this InteractionRuleInfo.

        事件类型。 * 1：弹幕事件 * 2：用户入场事件 * 3：用户点赞事件 * 4：用户送礼事件 * 10: 预置话术事件

        :param event_type: The event_type of this InteractionRuleInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def hit_condition(self):
        """Gets the hit_condition of this InteractionRuleInfo.

        :return: The hit_condition of this InteractionRuleInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HitCondition`
        """
        return self._hit_condition

    @hit_condition.setter
    def hit_condition(self, hit_condition):
        """Sets the hit_condition of this InteractionRuleInfo.

        :param hit_condition: The hit_condition of this InteractionRuleInfo.
        :type hit_condition: :class:`huaweicloudsdkmetastudio.v1.HitCondition`
        """
        self._hit_condition = hit_condition

    @property
    def trigger(self):
        """Gets the trigger of this InteractionRuleInfo.

        :return: The trigger of this InteractionRuleInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TriggerProcess`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this InteractionRuleInfo.

        :param trigger: The trigger of this InteractionRuleInfo.
        :type trigger: :class:`huaweicloudsdkmetastudio.v1.TriggerProcess`
        """
        self._trigger = trigger

    @property
    def review_config(self):
        """Gets the review_config of this InteractionRuleInfo.

        :return: The review_config of this InteractionRuleInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        """Sets the review_config of this InteractionRuleInfo.

        :param review_config: The review_config of this InteractionRuleInfo.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

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
        if not isinstance(other, InteractionRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
