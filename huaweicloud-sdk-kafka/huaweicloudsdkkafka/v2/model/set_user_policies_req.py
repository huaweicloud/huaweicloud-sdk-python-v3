# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetUserPoliciesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'policies': 'list[UserPolicyEntity]'
    }

    attribute_map = {
        'action': 'action',
        'policies': 'policies'
    }

    def __init__(self, action=None, policies=None):
        r"""SetUserPoliciesReq

        The model defined in huaweicloud sdk

        :param action: **参数解释**： 操作名称。 **约束限制**： 不涉及。 **取值范围**： - create：提交创建用户策略任务。 - delete：提交删除用户策略任务。 **默认取值**： 不涉及。
        :type action: str
        :param policies: **参数解释**： 用户权限列表。 **约束限制**： 不涉及。
        :type policies: list[:class:`huaweicloudsdkkafka.v2.UserPolicyEntity`]
        """
        
        

        self._action = None
        self._policies = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if policies is not None:
            self.policies = policies

    @property
    def action(self):
        r"""Gets the action of this SetUserPoliciesReq.

        **参数解释**： 操作名称。 **约束限制**： 不涉及。 **取值范围**： - create：提交创建用户策略任务。 - delete：提交删除用户策略任务。 **默认取值**： 不涉及。

        :return: The action of this SetUserPoliciesReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this SetUserPoliciesReq.

        **参数解释**： 操作名称。 **约束限制**： 不涉及。 **取值范围**： - create：提交创建用户策略任务。 - delete：提交删除用户策略任务。 **默认取值**： 不涉及。

        :param action: The action of this SetUserPoliciesReq.
        :type action: str
        """
        self._action = action

    @property
    def policies(self):
        r"""Gets the policies of this SetUserPoliciesReq.

        **参数解释**： 用户权限列表。 **约束限制**： 不涉及。

        :return: The policies of this SetUserPoliciesReq.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.UserPolicyEntity`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this SetUserPoliciesReq.

        **参数解释**： 用户权限列表。 **约束限制**： 不涉及。

        :param policies: The policies of this SetUserPoliciesReq.
        :type policies: list[:class:`huaweicloudsdkkafka.v2.UserPolicyEntity`]
        """
        self._policies = policies

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
        if not isinstance(other, SetUserPoliciesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
