# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePolicyGroupReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_group': 'PolicyGroupForCreate'
    }

    attribute_map = {
        'policy_group': 'policy_group'
    }

    def __init__(self, policy_group=None):
        """CreatePolicyGroupReq

        The model defined in huaweicloud sdk

        :param policy_group: 
        :type policy_group: :class:`huaweicloudsdkworkspaceapp.v1.PolicyGroupForCreate`
        """
        
        

        self._policy_group = None
        self.discriminator = None

        self.policy_group = policy_group

    @property
    def policy_group(self):
        """Gets the policy_group of this CreatePolicyGroupReq.

        :return: The policy_group of this CreatePolicyGroupReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PolicyGroupForCreate`
        """
        return self._policy_group

    @policy_group.setter
    def policy_group(self, policy_group):
        """Sets the policy_group of this CreatePolicyGroupReq.

        :param policy_group: The policy_group of this CreatePolicyGroupReq.
        :type policy_group: :class:`huaweicloudsdkworkspaceapp.v1.PolicyGroupForCreate`
        """
        self._policy_group = policy_group

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
        if not isinstance(other, CreatePolicyGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
