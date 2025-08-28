# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTokenPolicyV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token_policy': 'TokenPolicy'
    }

    attribute_map = {
        'token_policy': 'token_policy'
    }

    def __init__(self, token_policy=None):
        r"""ShowTokenPolicyV5Response

        The model defined in huaweicloud sdk

        :param token_policy: 
        :type token_policy: :class:`huaweicloudsdkiam.v5.TokenPolicy`
        """
        
        super(ShowTokenPolicyV5Response, self).__init__()

        self._token_policy = None
        self.discriminator = None

        if token_policy is not None:
            self.token_policy = token_policy

    @property
    def token_policy(self):
        r"""Gets the token_policy of this ShowTokenPolicyV5Response.

        :return: The token_policy of this ShowTokenPolicyV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.TokenPolicy`
        """
        return self._token_policy

    @token_policy.setter
    def token_policy(self, token_policy):
        r"""Sets the token_policy of this ShowTokenPolicyV5Response.

        :param token_policy: The token_policy of this ShowTokenPolicyV5Response.
        :type token_policy: :class:`huaweicloudsdkiam.v5.TokenPolicy`
        """
        self._token_policy = token_policy

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
        if not isinstance(other, ShowTokenPolicyV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
