# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Cause:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'condition': 'list[Conditions]'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'condition': 'condition'
    }

    def __init__(self, policy_name=None, condition=None):
        r"""Cause

        The model defined in huaweicloud sdk

        :param policy_name: **参数解释**：策略名称。 **取值范围**：不涉及。
        :type policy_name: str
        :param condition: **参数解释**：策略条件。
        :type condition: list[:class:`huaweicloudsdkmodelarts.v1.Conditions`]
        """
        
        

        self._policy_name = None
        self._condition = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if condition is not None:
            self.condition = condition

    @property
    def policy_name(self):
        r"""Gets the policy_name of this Cause.

        **参数解释**：策略名称。 **取值范围**：不涉及。

        :return: The policy_name of this Cause.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this Cause.

        **参数解释**：策略名称。 **取值范围**：不涉及。

        :param policy_name: The policy_name of this Cause.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def condition(self):
        r"""Gets the condition of this Cause.

        **参数解释**：策略条件。

        :return: The condition of this Cause.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Conditions`]
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this Cause.

        **参数解释**：策略条件。

        :param condition: The condition of this Cause.
        :type condition: list[:class:`huaweicloudsdkmodelarts.v1.Conditions`]
        """
        self._condition = condition

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
        if not isinstance(other, Cause):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
