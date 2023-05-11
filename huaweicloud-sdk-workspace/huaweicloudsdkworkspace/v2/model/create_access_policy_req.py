# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccessPolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy': 'AccessPolicyInfo',
        'policy_objects_list': 'list[AccessPolicyObjectInfo]'
    }

    attribute_map = {
        'policy': 'policy',
        'policy_objects_list': 'policy_objects_list'
    }

    def __init__(self, policy=None, policy_objects_list=None):
        """CreateAccessPolicyReq

        The model defined in huaweicloud sdk

        :param policy: 
        :type policy: :class:`huaweicloudsdkworkspace.v2.AccessPolicyInfo`
        :param policy_objects_list: 策略应用对象列表。
        :type policy_objects_list: list[:class:`huaweicloudsdkworkspace.v2.AccessPolicyObjectInfo`]
        """
        
        

        self._policy = None
        self._policy_objects_list = None
        self.discriminator = None

        self.policy = policy
        if policy_objects_list is not None:
            self.policy_objects_list = policy_objects_list

    @property
    def policy(self):
        """Gets the policy of this CreateAccessPolicyReq.

        :return: The policy of this CreateAccessPolicyReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AccessPolicyInfo`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this CreateAccessPolicyReq.

        :param policy: The policy of this CreateAccessPolicyReq.
        :type policy: :class:`huaweicloudsdkworkspace.v2.AccessPolicyInfo`
        """
        self._policy = policy

    @property
    def policy_objects_list(self):
        """Gets the policy_objects_list of this CreateAccessPolicyReq.

        策略应用对象列表。

        :return: The policy_objects_list of this CreateAccessPolicyReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AccessPolicyObjectInfo`]
        """
        return self._policy_objects_list

    @policy_objects_list.setter
    def policy_objects_list(self, policy_objects_list):
        """Sets the policy_objects_list of this CreateAccessPolicyReq.

        策略应用对象列表。

        :param policy_objects_list: The policy_objects_list of this CreateAccessPolicyReq.
        :type policy_objects_list: list[:class:`huaweicloudsdkworkspace.v2.AccessPolicyObjectInfo`]
        """
        self._policy_objects_list = policy_objects_list

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
        if not isinstance(other, CreateAccessPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
