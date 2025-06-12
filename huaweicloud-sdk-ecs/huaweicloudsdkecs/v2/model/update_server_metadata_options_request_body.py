# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerMetadataOptionsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'http_endpoint': 'str',
        'http_tokens': 'str'
    }

    attribute_map = {
        'http_endpoint': 'http_endpoint',
        'http_tokens': 'http_tokens'
    }

    def __init__(self, http_endpoint=None, http_tokens=None):
        r"""UpdateServerMetadataOptionsRequestBody

        The model defined in huaweicloud sdk

        :param http_endpoint: 是否禁用IMDS服务。
        :type http_endpoint: str
        :param http_tokens: 是否要求携带token。
        :type http_tokens: str
        """
        
        

        self._http_endpoint = None
        self._http_tokens = None
        self.discriminator = None

        if http_endpoint is not None:
            self.http_endpoint = http_endpoint
        if http_tokens is not None:
            self.http_tokens = http_tokens

    @property
    def http_endpoint(self):
        r"""Gets the http_endpoint of this UpdateServerMetadataOptionsRequestBody.

        是否禁用IMDS服务。

        :return: The http_endpoint of this UpdateServerMetadataOptionsRequestBody.
        :rtype: str
        """
        return self._http_endpoint

    @http_endpoint.setter
    def http_endpoint(self, http_endpoint):
        r"""Sets the http_endpoint of this UpdateServerMetadataOptionsRequestBody.

        是否禁用IMDS服务。

        :param http_endpoint: The http_endpoint of this UpdateServerMetadataOptionsRequestBody.
        :type http_endpoint: str
        """
        self._http_endpoint = http_endpoint

    @property
    def http_tokens(self):
        r"""Gets the http_tokens of this UpdateServerMetadataOptionsRequestBody.

        是否要求携带token。

        :return: The http_tokens of this UpdateServerMetadataOptionsRequestBody.
        :rtype: str
        """
        return self._http_tokens

    @http_tokens.setter
    def http_tokens(self, http_tokens):
        r"""Sets the http_tokens of this UpdateServerMetadataOptionsRequestBody.

        是否要求携带token。

        :param http_tokens: The http_tokens of this UpdateServerMetadataOptionsRequestBody.
        :type http_tokens: str
        """
        self._http_tokens = http_tokens

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
        if not isinstance(other, UpdateServerMetadataOptionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
