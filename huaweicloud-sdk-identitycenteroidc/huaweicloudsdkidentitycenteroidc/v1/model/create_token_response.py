# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTokenResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token_info': 'TokenInfoDto'
    }

    attribute_map = {
        'token_info': 'token_info'
    }

    def __init__(self, token_info=None):
        r"""CreateTokenResponse

        The model defined in huaweicloud sdk

        :param token_info: 
        :type token_info: :class:`huaweicloudsdkidentitycenteroidc.v1.TokenInfoDto`
        """
        
        super(CreateTokenResponse, self).__init__()

        self._token_info = None
        self.discriminator = None

        if token_info is not None:
            self.token_info = token_info

    @property
    def token_info(self):
        r"""Gets the token_info of this CreateTokenResponse.

        :return: The token_info of this CreateTokenResponse.
        :rtype: :class:`huaweicloudsdkidentitycenteroidc.v1.TokenInfoDto`
        """
        return self._token_info

    @token_info.setter
    def token_info(self, token_info):
        r"""Sets the token_info of this CreateTokenResponse.

        :param token_info: The token_info of this CreateTokenResponse.
        :type token_info: :class:`huaweicloudsdkidentitycenteroidc.v1.TokenInfoDto`
        """
        self._token_info = token_info

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
        if not isinstance(other, CreateTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
