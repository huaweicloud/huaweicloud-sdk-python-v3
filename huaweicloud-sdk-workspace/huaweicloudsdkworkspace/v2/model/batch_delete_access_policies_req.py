# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteAccessPoliciesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id_list': 'list[str]'
    }

    attribute_map = {
        'policy_id_list': 'policy_id_list'
    }

    def __init__(self, policy_id_list=None):
        """BatchDeleteAccessPoliciesReq

        The model defined in huaweicloud sdk

        :param policy_id_list: 策略ID列表。
        :type policy_id_list: list[str]
        """
        
        

        self._policy_id_list = None
        self.discriminator = None

        if policy_id_list is not None:
            self.policy_id_list = policy_id_list

    @property
    def policy_id_list(self):
        """Gets the policy_id_list of this BatchDeleteAccessPoliciesReq.

        策略ID列表。

        :return: The policy_id_list of this BatchDeleteAccessPoliciesReq.
        :rtype: list[str]
        """
        return self._policy_id_list

    @policy_id_list.setter
    def policy_id_list(self, policy_id_list):
        """Sets the policy_id_list of this BatchDeleteAccessPoliciesReq.

        策略ID列表。

        :param policy_id_list: The policy_id_list of this BatchDeleteAccessPoliciesReq.
        :type policy_id_list: list[str]
        """
        self._policy_id_list = policy_id_list

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
        if not isinstance(other, BatchDeleteAccessPoliciesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
