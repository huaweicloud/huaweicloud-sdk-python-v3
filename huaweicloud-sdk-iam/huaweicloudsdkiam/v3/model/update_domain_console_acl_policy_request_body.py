# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainConsoleAclPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'console_acl_policy': 'AclPolicyOption'
    }

    attribute_map = {
        'console_acl_policy': 'console_acl_policy'
    }

    def __init__(self, console_acl_policy=None):
        """UpdateDomainConsoleAclPolicyRequestBody

        The model defined in huaweicloud sdk

        :param console_acl_policy: 
        :type console_acl_policy: :class:`huaweicloudsdkiam.v3.AclPolicyOption`
        """
        
        

        self._console_acl_policy = None
        self.discriminator = None

        self.console_acl_policy = console_acl_policy

    @property
    def console_acl_policy(self):
        """Gets the console_acl_policy of this UpdateDomainConsoleAclPolicyRequestBody.


        :return: The console_acl_policy of this UpdateDomainConsoleAclPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkiam.v3.AclPolicyOption`
        """
        return self._console_acl_policy

    @console_acl_policy.setter
    def console_acl_policy(self, console_acl_policy):
        """Sets the console_acl_policy of this UpdateDomainConsoleAclPolicyRequestBody.


        :param console_acl_policy: The console_acl_policy of this UpdateDomainConsoleAclPolicyRequestBody.
        :type console_acl_policy: :class:`huaweicloudsdkiam.v3.AclPolicyOption`
        """
        self._console_acl_policy = console_acl_policy

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
        if not isinstance(other, UpdateDomainConsoleAclPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
