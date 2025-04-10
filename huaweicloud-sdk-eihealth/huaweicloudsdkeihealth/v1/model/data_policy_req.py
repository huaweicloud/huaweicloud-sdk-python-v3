# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataPolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_policy': 'PolicyType'
    }

    attribute_map = {
        'delete_policy': 'delete_policy'
    }

    def __init__(self, delete_policy=None):
        r"""DataPolicyReq

        The model defined in huaweicloud sdk

        :param delete_policy: 
        :type delete_policy: :class:`huaweicloudsdkeihealth.v1.PolicyType`
        """
        
        

        self._delete_policy = None
        self.discriminator = None

        self.delete_policy = delete_policy

    @property
    def delete_policy(self):
        r"""Gets the delete_policy of this DataPolicyReq.

        :return: The delete_policy of this DataPolicyReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.PolicyType`
        """
        return self._delete_policy

    @delete_policy.setter
    def delete_policy(self, delete_policy):
        r"""Sets the delete_policy of this DataPolicyReq.

        :param delete_policy: The delete_policy of this DataPolicyReq.
        :type delete_policy: :class:`huaweicloudsdkeihealth.v1.PolicyType`
        """
        self._delete_policy = delete_policy

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
        if not isinstance(other, DataPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
