# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainApiAclPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_acl_policy': 'AclPolicyOption'
    }

    attribute_map = {
        'api_acl_policy': 'api_acl_policy'
    }

    def __init__(self, api_acl_policy=None):
        r"""UpdateDomainApiAclPolicyRequestBody

        The model defined in huaweicloud sdk

        :param api_acl_policy: 
        :type api_acl_policy: :class:`huaweicloudsdkiam.v3.AclPolicyOption`
        """
        
        

        self._api_acl_policy = None
        self.discriminator = None

        self.api_acl_policy = api_acl_policy

    @property
    def api_acl_policy(self):
        r"""Gets the api_acl_policy of this UpdateDomainApiAclPolicyRequestBody.

        :return: The api_acl_policy of this UpdateDomainApiAclPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkiam.v3.AclPolicyOption`
        """
        return self._api_acl_policy

    @api_acl_policy.setter
    def api_acl_policy(self, api_acl_policy):
        r"""Sets the api_acl_policy of this UpdateDomainApiAclPolicyRequestBody.

        :param api_acl_policy: The api_acl_policy of this UpdateDomainApiAclPolicyRequestBody.
        :type api_acl_policy: :class:`huaweicloudsdkiam.v3.AclPolicyOption`
        """
        self._api_acl_policy = api_acl_policy

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
        if not isinstance(other, UpdateDomainApiAclPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
