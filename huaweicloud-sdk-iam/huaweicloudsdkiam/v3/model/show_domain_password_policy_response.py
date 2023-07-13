# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainPasswordPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'password_policy': 'PasswordPolicyResult'
    }

    attribute_map = {
        'password_policy': 'password_policy'
    }

    def __init__(self, password_policy=None):
        """ShowDomainPasswordPolicyResponse

        The model defined in huaweicloud sdk

        :param password_policy: 
        :type password_policy: :class:`huaweicloudsdkiam.v3.PasswordPolicyResult`
        """
        
        super(ShowDomainPasswordPolicyResponse, self).__init__()

        self._password_policy = None
        self.discriminator = None

        if password_policy is not None:
            self.password_policy = password_policy

    @property
    def password_policy(self):
        """Gets the password_policy of this ShowDomainPasswordPolicyResponse.

        :return: The password_policy of this ShowDomainPasswordPolicyResponse.
        :rtype: :class:`huaweicloudsdkiam.v3.PasswordPolicyResult`
        """
        return self._password_policy

    @password_policy.setter
    def password_policy(self, password_policy):
        """Sets the password_policy of this ShowDomainPasswordPolicyResponse.

        :param password_policy: The password_policy of this ShowDomainPasswordPolicyResponse.
        :type password_policy: :class:`huaweicloudsdkiam.v3.PasswordPolicyResult`
        """
        self._password_policy = password_policy

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
        if not isinstance(other, ShowDomainPasswordPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
