# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRoutingFlowControlPolicyResponse(SdkResponse):

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
        'policy_name': 'str',
        'description': 'str',
        'scope': 'str',
        'scope_value': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'description': 'description',
        'scope': 'scope',
        'scope_value': 'scope_value',
        'limit': 'limit'
    }

    def __init__(self, policy_id=None, policy_name=None, description=None, scope=None, scope_value=None, limit=None):
        r"""ShowRoutingFlowControlPolicyResponse

        The model defined in huaweicloud sdk

        :param policy_id: **参数说明**：数据流转流控策略id，用于唯一标识一个数据流转流控策略，在创建数据流转流控策略时由物联网平台分配获得。
        :type policy_id: str
        :param policy_name: **参数说明**：数据流转流控策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type policy_name: str
        :param description: **参数说明**：用户自定义的数据流转流控策略描述。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type description: str
        :param scope: **参数说明**：流控策略作用域. **取值范围**： - USER：租户级流控策略。 - CHANNEL：转发通道级流控策略。 - RULE：转发规则级流控策略。 - ACTION：转发动作级流控策略。
        :type scope: str
        :param scope_value: **参数说明**：流控策略作用域附加值。 scope取值为USER时，可不携带该字段，表示租户级流控。 scope取值为CHANNEL时，**取值范围**：HTTP_FORWARDING、DIS_FORWARDING、OBS_FORWARDING、AMQP_FORWARDING、DMS_KAFKA_FORWARDING。 scope取值为RULE时，该字段为对应的ruleId。 scope取值为ACTION时，该字段为对应的actionId。
        :type scope_value: str
        :param limit: **参数说明**：数据转发流控大小。单位为tps，取值范围为1~1000的整数，默认为1000.
        :type limit: int
        """
        
        super(ShowRoutingFlowControlPolicyResponse, self).__init__()

        self._policy_id = None
        self._policy_name = None
        self._description = None
        self._scope = None
        self._scope_value = None
        self._limit = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if description is not None:
            self.description = description
        if scope is not None:
            self.scope = scope
        if scope_value is not None:
            self.scope_value = scope_value
        if limit is not None:
            self.limit = limit

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：数据流转流控策略id，用于唯一标识一个数据流转流控策略，在创建数据流转流控策略时由物联网平台分配获得。

        :return: The policy_id of this ShowRoutingFlowControlPolicyResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：数据流转流控策略id，用于唯一标识一个数据流转流控策略，在创建数据流转流控策略时由物联网平台分配获得。

        :param policy_id: The policy_id of this ShowRoutingFlowControlPolicyResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：数据流转流控策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The policy_name of this ShowRoutingFlowControlPolicyResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：数据流转流控策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param policy_name: The policy_name of this ShowRoutingFlowControlPolicyResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def description(self):
        r"""Gets the description of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：用户自定义的数据流转流控策略描述。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The description of this ShowRoutingFlowControlPolicyResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：用户自定义的数据流转流控策略描述。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param description: The description of this ShowRoutingFlowControlPolicyResponse.
        :type description: str
        """
        self._description = description

    @property
    def scope(self):
        r"""Gets the scope of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：流控策略作用域. **取值范围**： - USER：租户级流控策略。 - CHANNEL：转发通道级流控策略。 - RULE：转发规则级流控策略。 - ACTION：转发动作级流控策略。

        :return: The scope of this ShowRoutingFlowControlPolicyResponse.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：流控策略作用域. **取值范围**： - USER：租户级流控策略。 - CHANNEL：转发通道级流控策略。 - RULE：转发规则级流控策略。 - ACTION：转发动作级流控策略。

        :param scope: The scope of this ShowRoutingFlowControlPolicyResponse.
        :type scope: str
        """
        self._scope = scope

    @property
    def scope_value(self):
        r"""Gets the scope_value of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：流控策略作用域附加值。 scope取值为USER时，可不携带该字段，表示租户级流控。 scope取值为CHANNEL时，**取值范围**：HTTP_FORWARDING、DIS_FORWARDING、OBS_FORWARDING、AMQP_FORWARDING、DMS_KAFKA_FORWARDING。 scope取值为RULE时，该字段为对应的ruleId。 scope取值为ACTION时，该字段为对应的actionId。

        :return: The scope_value of this ShowRoutingFlowControlPolicyResponse.
        :rtype: str
        """
        return self._scope_value

    @scope_value.setter
    def scope_value(self, scope_value):
        r"""Sets the scope_value of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：流控策略作用域附加值。 scope取值为USER时，可不携带该字段，表示租户级流控。 scope取值为CHANNEL时，**取值范围**：HTTP_FORWARDING、DIS_FORWARDING、OBS_FORWARDING、AMQP_FORWARDING、DMS_KAFKA_FORWARDING。 scope取值为RULE时，该字段为对应的ruleId。 scope取值为ACTION时，该字段为对应的actionId。

        :param scope_value: The scope_value of this ShowRoutingFlowControlPolicyResponse.
        :type scope_value: str
        """
        self._scope_value = scope_value

    @property
    def limit(self):
        r"""Gets the limit of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：数据转发流控大小。单位为tps，取值范围为1~1000的整数，默认为1000.

        :return: The limit of this ShowRoutingFlowControlPolicyResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowRoutingFlowControlPolicyResponse.

        **参数说明**：数据转发流控大小。单位为tps，取值范围为1~1000的整数，默认为1000.

        :param limit: The limit of this ShowRoutingFlowControlPolicyResponse.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowRoutingFlowControlPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
