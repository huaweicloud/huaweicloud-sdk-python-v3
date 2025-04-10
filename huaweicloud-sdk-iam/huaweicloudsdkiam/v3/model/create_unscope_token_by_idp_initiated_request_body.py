# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUnscopeTokenByIdpInitiatedRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'saml_response': 'str'
    }

    attribute_map = {
        'saml_response': 'SAMLResponse'
    }

    def __init__(self, saml_response=None):
        r"""CreateUnscopeTokenByIdpInitiatedRequestBody

        The model defined in huaweicloud sdk

        :param saml_response: 在IdP认证成功后返回的响应体。详情请参见：[获取联邦认证unscoped token(IdP initiated)](https://support.huaweicloud.com/api-iam/iam_02_0003.html)。
        :type saml_response: str
        """
        
        

        self._saml_response = None
        self.discriminator = None

        self.saml_response = saml_response

    @property
    def saml_response(self):
        r"""Gets the saml_response of this CreateUnscopeTokenByIdpInitiatedRequestBody.

        在IdP认证成功后返回的响应体。详情请参见：[获取联邦认证unscoped token(IdP initiated)](https://support.huaweicloud.com/api-iam/iam_02_0003.html)。

        :return: The saml_response of this CreateUnscopeTokenByIdpInitiatedRequestBody.
        :rtype: str
        """
        return self._saml_response

    @saml_response.setter
    def saml_response(self, saml_response):
        r"""Sets the saml_response of this CreateUnscopeTokenByIdpInitiatedRequestBody.

        在IdP认证成功后返回的响应体。详情请参见：[获取联邦认证unscoped token(IdP initiated)](https://support.huaweicloud.com/api-iam/iam_02_0003.html)。

        :param saml_response: The saml_response of this CreateUnscopeTokenByIdpInitiatedRequestBody.
        :type saml_response: str
        """
        self._saml_response = saml_response

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
        if not isinstance(other, CreateUnscopeTokenByIdpInitiatedRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
