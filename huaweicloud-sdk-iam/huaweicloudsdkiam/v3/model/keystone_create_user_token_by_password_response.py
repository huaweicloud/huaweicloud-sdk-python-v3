# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneCreateUserTokenByPasswordResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token': 'TokenResult',
        'x_subject_token': 'str'
    }

    attribute_map = {
        'token': 'token',
        'x_subject_token': 'X-Subject-Token'
    }

    def __init__(self, token=None, x_subject_token=None):
        r"""KeystoneCreateUserTokenByPasswordResponse

        The model defined in huaweicloud sdk

        :param token: 
        :type token: :class:`huaweicloudsdkiam.v3.TokenResult`
        :param x_subject_token: 
        :type x_subject_token: str
        """
        
        super(KeystoneCreateUserTokenByPasswordResponse, self).__init__()

        self._token = None
        self._x_subject_token = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if x_subject_token is not None:
            self.x_subject_token = x_subject_token

    @property
    def token(self):
        r"""Gets the token of this KeystoneCreateUserTokenByPasswordResponse.

        :return: The token of this KeystoneCreateUserTokenByPasswordResponse.
        :rtype: :class:`huaweicloudsdkiam.v3.TokenResult`
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this KeystoneCreateUserTokenByPasswordResponse.

        :param token: The token of this KeystoneCreateUserTokenByPasswordResponse.
        :type token: :class:`huaweicloudsdkiam.v3.TokenResult`
        """
        self._token = token

    @property
    def x_subject_token(self):
        r"""Gets the x_subject_token of this KeystoneCreateUserTokenByPasswordResponse.

        :return: The x_subject_token of this KeystoneCreateUserTokenByPasswordResponse.
        :rtype: str
        """
        return self._x_subject_token

    @x_subject_token.setter
    def x_subject_token(self, x_subject_token):
        r"""Sets the x_subject_token of this KeystoneCreateUserTokenByPasswordResponse.

        :param x_subject_token: The x_subject_token of this KeystoneCreateUserTokenByPasswordResponse.
        :type x_subject_token: str
        """
        self._x_subject_token = x_subject_token

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
        if not isinstance(other, KeystoneCreateUserTokenByPasswordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
