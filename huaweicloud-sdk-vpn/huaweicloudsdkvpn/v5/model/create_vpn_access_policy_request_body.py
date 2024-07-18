# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpnAccessPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_policy': 'CreateVpnAccessPolicyRequestBodyContent'
    }

    attribute_map = {
        'access_policy': 'access_policy'
    }

    def __init__(self, access_policy=None):
        """CreateVpnAccessPolicyRequestBody

        The model defined in huaweicloud sdk

        :param access_policy: 
        :type access_policy: :class:`huaweicloudsdkvpn.v5.CreateVpnAccessPolicyRequestBodyContent`
        """
        
        

        self._access_policy = None
        self.discriminator = None

        self.access_policy = access_policy

    @property
    def access_policy(self):
        """Gets the access_policy of this CreateVpnAccessPolicyRequestBody.

        :return: The access_policy of this CreateVpnAccessPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVpnAccessPolicyRequestBodyContent`
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        """Sets the access_policy of this CreateVpnAccessPolicyRequestBody.

        :param access_policy: The access_policy of this CreateVpnAccessPolicyRequestBody.
        :type access_policy: :class:`huaweicloudsdkvpn.v5.CreateVpnAccessPolicyRequestBodyContent`
        """
        self._access_policy = access_policy

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
        if not isinstance(other, CreateVpnAccessPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
