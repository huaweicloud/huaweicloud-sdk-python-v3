# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEndpointPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_statement': 'list[PolicyStatement]'
    }

    attribute_map = {
        'policy_statement': 'policy_statement'
    }

    def __init__(self, policy_statement=None):
        """UpdateEndpointPolicyRequestBody

        The model defined in huaweicloud sdk

        :param policy_statement: 只涉及开启双端固定的网关型终端节点
        :type policy_statement: list[:class:`huaweicloudsdkvpcep.v1.PolicyStatement`]
        """
        
        

        self._policy_statement = None
        self.discriminator = None

        self.policy_statement = policy_statement

    @property
    def policy_statement(self):
        """Gets the policy_statement of this UpdateEndpointPolicyRequestBody.

        只涉及开启双端固定的网关型终端节点

        :return: The policy_statement of this UpdateEndpointPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.PolicyStatement`]
        """
        return self._policy_statement

    @policy_statement.setter
    def policy_statement(self, policy_statement):
        """Sets the policy_statement of this UpdateEndpointPolicyRequestBody.

        只涉及开启双端固定的网关型终端节点

        :param policy_statement: The policy_statement of this UpdateEndpointPolicyRequestBody.
        :type policy_statement: list[:class:`huaweicloudsdkvpcep.v1.PolicyStatement`]
        """
        self._policy_statement = policy_statement

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
        if not isinstance(other, UpdateEndpointPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
