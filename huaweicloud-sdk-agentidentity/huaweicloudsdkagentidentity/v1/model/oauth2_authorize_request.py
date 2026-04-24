# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Oauth2AuthorizeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_uri': 'str'
    }

    attribute_map = {
        'request_uri': 'request_uri'
    }

    def __init__(self, request_uri=None):
        r"""Oauth2AuthorizeRequest

        The model defined in huaweicloud sdk

        :param request_uri: OAuth 2.0 PAR standard request URI, references authorization parameters for the OAuth2 flow
        :type request_uri: str
        """
        
        

        self._request_uri = None
        self.discriminator = None

        self.request_uri = request_uri

    @property
    def request_uri(self):
        r"""Gets the request_uri of this Oauth2AuthorizeRequest.

        OAuth 2.0 PAR standard request URI, references authorization parameters for the OAuth2 flow

        :return: The request_uri of this Oauth2AuthorizeRequest.
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        r"""Sets the request_uri of this Oauth2AuthorizeRequest.

        OAuth 2.0 PAR standard request URI, references authorization parameters for the OAuth2 flow

        :param request_uri: The request_uri of this Oauth2AuthorizeRequest.
        :type request_uri: str
        """
        self._request_uri = request_uri

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Oauth2AuthorizeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
