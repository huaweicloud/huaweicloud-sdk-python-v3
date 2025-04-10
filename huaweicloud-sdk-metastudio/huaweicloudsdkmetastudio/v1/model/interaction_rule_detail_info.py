# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InteractionRuleDetailInfo:

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
        'review_config': 'ReviewConfig',
        'rule_id': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'rule_index': 'rule_index',
        'rule_name': 'rule_name',
        'enabled': 'enabled',
        'event_type': 'event_type',
        'hit_condition': 'hit_condition',
        'trigger': 'trigger',
        'review_config': 'review_config',
        'rule_id': 'rule_id',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, rule_index=None, rule_name=None, enabled=None, event_type=None, hit_condition=None, trigger=None, review_config=None, rule_id=None, create_time=None, update_time=None):
        r"""InteractionRuleDetailInfo

        The model defined in huaweicloud sdk

        :param rule_index: **参数解释**： 规则索引。用于触发规则时索引具体规则。 **约束限制**： 无需用户填写。 **取值范围**： 字符0-64位 **默认取值**： 不涉及。
        :type rule_index: str
        :param rule_name: **参数解释**： 规则名称。 **约束限制**： 不涉及。 **取值范围**： 字符0-256位 **默认取值**： 不涉及。
        :type rule_name: str
        :param enabled: **参数解释**： 是否启用。 **约束限制**： 不涉及。 **取值范围**： * true：启用 * fasle：不启用  **默认取值**： true
        :type enabled: bool
        :param event_type: **参数解释**： 规则匹配直播事件类型。接口的取值范围[0,100]，实际业务取值如下所示： * 1：弹幕事件  * 2：用户入场事件  * 3：用户点赞事件 * 4：用户送礼事件  * 10: 预置话术事件  请以实际业务取值为准。 &gt; * 1,2,3,4：与LiveEventReport中的event.type对应。 &gt; * 10：匹配预置剧本  **约束限制**： 不涉及。 **默认取值**： 不涉及
        :type event_type: int
        :param hit_condition: 
        :type hit_condition: :class:`huaweicloudsdkmetastudio.v1.HitCondition`
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkmetastudio.v1.TriggerProcess`
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param rule_id: 互动规则ID
        :type rule_id: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type update_time: str
        """
        
        

        self._rule_index = None
        self._rule_name = None
        self._enabled = None
        self._event_type = None
        self._hit_condition = None
        self._trigger = None
        self._review_config = None
        self._rule_id = None
        self._create_time = None
        self._update_time = None
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
        if rule_id is not None:
            self.rule_id = rule_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def rule_index(self):
        r"""Gets the rule_index of this InteractionRuleDetailInfo.

        **参数解释**： 规则索引。用于触发规则时索引具体规则。 **约束限制**： 无需用户填写。 **取值范围**： 字符0-64位 **默认取值**： 不涉及。

        :return: The rule_index of this InteractionRuleDetailInfo.
        :rtype: str
        """
        return self._rule_index

    @rule_index.setter
    def rule_index(self, rule_index):
        r"""Sets the rule_index of this InteractionRuleDetailInfo.

        **参数解释**： 规则索引。用于触发规则时索引具体规则。 **约束限制**： 无需用户填写。 **取值范围**： 字符0-64位 **默认取值**： 不涉及。

        :param rule_index: The rule_index of this InteractionRuleDetailInfo.
        :type rule_index: str
        """
        self._rule_index = rule_index

    @property
    def rule_name(self):
        r"""Gets the rule_name of this InteractionRuleDetailInfo.

        **参数解释**： 规则名称。 **约束限制**： 不涉及。 **取值范围**： 字符0-256位 **默认取值**： 不涉及。

        :return: The rule_name of this InteractionRuleDetailInfo.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this InteractionRuleDetailInfo.

        **参数解释**： 规则名称。 **约束限制**： 不涉及。 **取值范围**： 字符0-256位 **默认取值**： 不涉及。

        :param rule_name: The rule_name of this InteractionRuleDetailInfo.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def enabled(self):
        r"""Gets the enabled of this InteractionRuleDetailInfo.

        **参数解释**： 是否启用。 **约束限制**： 不涉及。 **取值范围**： * true：启用 * fasle：不启用  **默认取值**： true

        :return: The enabled of this InteractionRuleDetailInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this InteractionRuleDetailInfo.

        **参数解释**： 是否启用。 **约束限制**： 不涉及。 **取值范围**： * true：启用 * fasle：不启用  **默认取值**： true

        :param enabled: The enabled of this InteractionRuleDetailInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def event_type(self):
        r"""Gets the event_type of this InteractionRuleDetailInfo.

        **参数解释**： 规则匹配直播事件类型。接口的取值范围[0,100]，实际业务取值如下所示： * 1：弹幕事件  * 2：用户入场事件  * 3：用户点赞事件 * 4：用户送礼事件  * 10: 预置话术事件  请以实际业务取值为准。 > * 1,2,3,4：与LiveEventReport中的event.type对应。 > * 10：匹配预置剧本  **约束限制**： 不涉及。 **默认取值**： 不涉及

        :return: The event_type of this InteractionRuleDetailInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this InteractionRuleDetailInfo.

        **参数解释**： 规则匹配直播事件类型。接口的取值范围[0,100]，实际业务取值如下所示： * 1：弹幕事件  * 2：用户入场事件  * 3：用户点赞事件 * 4：用户送礼事件  * 10: 预置话术事件  请以实际业务取值为准。 > * 1,2,3,4：与LiveEventReport中的event.type对应。 > * 10：匹配预置剧本  **约束限制**： 不涉及。 **默认取值**： 不涉及

        :param event_type: The event_type of this InteractionRuleDetailInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def hit_condition(self):
        r"""Gets the hit_condition of this InteractionRuleDetailInfo.

        :return: The hit_condition of this InteractionRuleDetailInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HitCondition`
        """
        return self._hit_condition

    @hit_condition.setter
    def hit_condition(self, hit_condition):
        r"""Sets the hit_condition of this InteractionRuleDetailInfo.

        :param hit_condition: The hit_condition of this InteractionRuleDetailInfo.
        :type hit_condition: :class:`huaweicloudsdkmetastudio.v1.HitCondition`
        """
        self._hit_condition = hit_condition

    @property
    def trigger(self):
        r"""Gets the trigger of this InteractionRuleDetailInfo.

        :return: The trigger of this InteractionRuleDetailInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TriggerProcess`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this InteractionRuleDetailInfo.

        :param trigger: The trigger of this InteractionRuleDetailInfo.
        :type trigger: :class:`huaweicloudsdkmetastudio.v1.TriggerProcess`
        """
        self._trigger = trigger

    @property
    def review_config(self):
        r"""Gets the review_config of this InteractionRuleDetailInfo.

        :return: The review_config of this InteractionRuleDetailInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        r"""Sets the review_config of this InteractionRuleDetailInfo.

        :param review_config: The review_config of this InteractionRuleDetailInfo.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def rule_id(self):
        r"""Gets the rule_id of this InteractionRuleDetailInfo.

        互动规则ID

        :return: The rule_id of this InteractionRuleDetailInfo.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this InteractionRuleDetailInfo.

        互动规则ID

        :param rule_id: The rule_id of this InteractionRuleDetailInfo.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def create_time(self):
        r"""Gets the create_time of this InteractionRuleDetailInfo.

        创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The create_time of this InteractionRuleDetailInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this InteractionRuleDetailInfo.

        创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param create_time: The create_time of this InteractionRuleDetailInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this InteractionRuleDetailInfo.

        更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The update_time of this InteractionRuleDetailInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this InteractionRuleDetailInfo.

        更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param update_time: The update_time of this InteractionRuleDetailInfo.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, InteractionRuleDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
