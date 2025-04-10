# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_policy_id': 'str',
        'body': 'UpdateSecurityPolicyRequestBody'
    }

    attribute_map = {
        'security_policy_id': 'security_policy_id',
        'body': 'body'
    }

    def __init__(self, security_policy_id=None, body=None):
        r"""UpdateSecurityPolicyRequest

        The model defined in huaweicloud sdk

        :param security_policy_id: 自定义安全策略的ID。
        :type security_policy_id: str
        :param body: Body of the UpdateSecurityPolicyRequest
        :type body: :class:`huaweicloudsdkelb.v3.UpdateSecurityPolicyRequestBody`
        """
        
        

        self._security_policy_id = None
        self._body = None
        self.discriminator = None

        self.security_policy_id = security_policy_id
        if body is not None:
            self.body = body

    @property
    def security_policy_id(self):
        r"""Gets the security_policy_id of this UpdateSecurityPolicyRequest.

        自定义安全策略的ID。

        :return: The security_policy_id of this UpdateSecurityPolicyRequest.
        :rtype: str
        """
        return self._security_policy_id

    @security_policy_id.setter
    def security_policy_id(self, security_policy_id):
        r"""Sets the security_policy_id of this UpdateSecurityPolicyRequest.

        自定义安全策略的ID。

        :param security_policy_id: The security_policy_id of this UpdateSecurityPolicyRequest.
        :type security_policy_id: str
        """
        self._security_policy_id = security_policy_id

    @property
    def body(self):
        r"""Gets the body of this UpdateSecurityPolicyRequest.

        :return: The body of this UpdateSecurityPolicyRequest.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateSecurityPolicyRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateSecurityPolicyRequest.

        :param body: The body of this UpdateSecurityPolicyRequest.
        :type body: :class:`huaweicloudsdkelb.v3.UpdateSecurityPolicyRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateSecurityPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
