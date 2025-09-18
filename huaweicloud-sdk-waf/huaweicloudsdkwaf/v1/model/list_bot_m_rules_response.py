# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBotMRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'tenant_id': 'str',
        'known_bot_detection': 'list[BotMRule]',
        'transparent_detection': 'list[BotMRule]',
        'behavior_detection': 'BotMBehaviorDetectionRule',
        'traffic_detection_conditions': 'list[TrafficDetectionConditionDTO]',
        'interactive_detection': 'list[BotMRule]'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'tenant_id': 'tenant_id',
        'known_bot_detection': 'known_bot_detection',
        'transparent_detection': 'transparent_detection',
        'behavior_detection': 'behavior_detection',
        'traffic_detection_conditions': 'traffic_detection_conditions',
        'interactive_detection': 'interactive_detection'
    }

    def __init__(self, policy_id=None, tenant_id=None, known_bot_detection=None, transparent_detection=None, behavior_detection=None, traffic_detection_conditions=None, interactive_detection=None):
        r"""ListBotMRulesResponse

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释：** 策略Id，关联BotM规则的防护策略唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_id: str
        :param tenant_id: **参数解释：** 租户Id，当前BotM规则所属的租户唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tenant_id: str
        :param known_bot_detection: **参数解释：** 已知Bot相关的所有规则，包含针对已知Bot的检测与防护规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type known_bot_detection: list[:class:`huaweicloudsdkwaf.v1.BotMRule`]
        :param transparent_detection: **参数解释：** 透明检测相关的所有规则，包含无感知的Bot透明检测规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type transparent_detection: list[:class:`huaweicloudsdkwaf.v1.BotMRule`]
        :param behavior_detection: 
        :type behavior_detection: :class:`huaweicloudsdkwaf.v1.BotMBehaviorDetectionRule`
        :param traffic_detection_conditions: **参数解释：** 需要BOT检测的流量检测条件，定义触发Bot检测的流量筛选规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type traffic_detection_conditions: list[:class:`huaweicloudsdkwaf.v1.TrafficDetectionConditionDTO`]
        :param interactive_detection: **参数解释：** 主动特征检测规则列表，包含需要主动交互验证的Bot检测规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type interactive_detection: list[:class:`huaweicloudsdkwaf.v1.BotMRule`]
        """
        
        super(ListBotMRulesResponse, self).__init__()

        self._policy_id = None
        self._tenant_id = None
        self._known_bot_detection = None
        self._transparent_detection = None
        self._behavior_detection = None
        self._traffic_detection_conditions = None
        self._interactive_detection = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if known_bot_detection is not None:
            self.known_bot_detection = known_bot_detection
        if transparent_detection is not None:
            self.transparent_detection = transparent_detection
        if behavior_detection is not None:
            self.behavior_detection = behavior_detection
        if traffic_detection_conditions is not None:
            self.traffic_detection_conditions = traffic_detection_conditions
        if interactive_detection is not None:
            self.interactive_detection = interactive_detection

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListBotMRulesResponse.

        **参数解释：** 策略Id，关联BotM规则的防护策略唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_id of this ListBotMRulesResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListBotMRulesResponse.

        **参数解释：** 策略Id，关联BotM规则的防护策略唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_id: The policy_id of this ListBotMRulesResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ListBotMRulesResponse.

        **参数解释：** 租户Id，当前BotM规则所属的租户唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tenant_id of this ListBotMRulesResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ListBotMRulesResponse.

        **参数解释：** 租户Id，当前BotM规则所属的租户唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tenant_id: The tenant_id of this ListBotMRulesResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def known_bot_detection(self):
        r"""Gets the known_bot_detection of this ListBotMRulesResponse.

        **参数解释：** 已知Bot相关的所有规则，包含针对已知Bot的检测与防护规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The known_bot_detection of this ListBotMRulesResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.BotMRule`]
        """
        return self._known_bot_detection

    @known_bot_detection.setter
    def known_bot_detection(self, known_bot_detection):
        r"""Sets the known_bot_detection of this ListBotMRulesResponse.

        **参数解释：** 已知Bot相关的所有规则，包含针对已知Bot的检测与防护规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param known_bot_detection: The known_bot_detection of this ListBotMRulesResponse.
        :type known_bot_detection: list[:class:`huaweicloudsdkwaf.v1.BotMRule`]
        """
        self._known_bot_detection = known_bot_detection

    @property
    def transparent_detection(self):
        r"""Gets the transparent_detection of this ListBotMRulesResponse.

        **参数解释：** 透明检测相关的所有规则，包含无感知的Bot透明检测规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The transparent_detection of this ListBotMRulesResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.BotMRule`]
        """
        return self._transparent_detection

    @transparent_detection.setter
    def transparent_detection(self, transparent_detection):
        r"""Sets the transparent_detection of this ListBotMRulesResponse.

        **参数解释：** 透明检测相关的所有规则，包含无感知的Bot透明检测规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param transparent_detection: The transparent_detection of this ListBotMRulesResponse.
        :type transparent_detection: list[:class:`huaweicloudsdkwaf.v1.BotMRule`]
        """
        self._transparent_detection = transparent_detection

    @property
    def behavior_detection(self):
        r"""Gets the behavior_detection of this ListBotMRulesResponse.

        :return: The behavior_detection of this ListBotMRulesResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.BotMBehaviorDetectionRule`
        """
        return self._behavior_detection

    @behavior_detection.setter
    def behavior_detection(self, behavior_detection):
        r"""Sets the behavior_detection of this ListBotMRulesResponse.

        :param behavior_detection: The behavior_detection of this ListBotMRulesResponse.
        :type behavior_detection: :class:`huaweicloudsdkwaf.v1.BotMBehaviorDetectionRule`
        """
        self._behavior_detection = behavior_detection

    @property
    def traffic_detection_conditions(self):
        r"""Gets the traffic_detection_conditions of this ListBotMRulesResponse.

        **参数解释：** 需要BOT检测的流量检测条件，定义触发Bot检测的流量筛选规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The traffic_detection_conditions of this ListBotMRulesResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TrafficDetectionConditionDTO`]
        """
        return self._traffic_detection_conditions

    @traffic_detection_conditions.setter
    def traffic_detection_conditions(self, traffic_detection_conditions):
        r"""Sets the traffic_detection_conditions of this ListBotMRulesResponse.

        **参数解释：** 需要BOT检测的流量检测条件，定义触发Bot检测的流量筛选规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param traffic_detection_conditions: The traffic_detection_conditions of this ListBotMRulesResponse.
        :type traffic_detection_conditions: list[:class:`huaweicloudsdkwaf.v1.TrafficDetectionConditionDTO`]
        """
        self._traffic_detection_conditions = traffic_detection_conditions

    @property
    def interactive_detection(self):
        r"""Gets the interactive_detection of this ListBotMRulesResponse.

        **参数解释：** 主动特征检测规则列表，包含需要主动交互验证的Bot检测规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The interactive_detection of this ListBotMRulesResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.BotMRule`]
        """
        return self._interactive_detection

    @interactive_detection.setter
    def interactive_detection(self, interactive_detection):
        r"""Sets the interactive_detection of this ListBotMRulesResponse.

        **参数解释：** 主动特征检测规则列表，包含需要主动交互验证的Bot检测规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param interactive_detection: The interactive_detection of this ListBotMRulesResponse.
        :type interactive_detection: list[:class:`huaweicloudsdkwaf.v1.BotMRule`]
        """
        self._interactive_detection = interactive_detection

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
        if not isinstance(other, ListBotMRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
