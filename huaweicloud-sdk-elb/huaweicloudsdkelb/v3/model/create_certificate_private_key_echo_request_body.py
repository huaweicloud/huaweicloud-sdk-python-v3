# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificatePrivateKeyEchoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'private_key_echo': 'bool'
    }

    attribute_map = {
        'private_key_echo': 'private_key_echo'
    }

    def __init__(self, private_key_echo=None):
        r"""CreateCertificatePrivateKeyEchoRequestBody

        The model defined in huaweicloud sdk

        :param private_key_echo: 证书回显开关，项目粒度的,默认情况下,\&quot;private_key_echo\&quot;是true,证书的返回体中展示私钥。 当值为false时,证书的返回体中不展示私钥。
        :type private_key_echo: bool
        """
        
        

        self._private_key_echo = None
        self.discriminator = None

        self.private_key_echo = private_key_echo

    @property
    def private_key_echo(self):
        r"""Gets the private_key_echo of this CreateCertificatePrivateKeyEchoRequestBody.

        证书回显开关，项目粒度的,默认情况下,\"private_key_echo\"是true,证书的返回体中展示私钥。 当值为false时,证书的返回体中不展示私钥。

        :return: The private_key_echo of this CreateCertificatePrivateKeyEchoRequestBody.
        :rtype: bool
        """
        return self._private_key_echo

    @private_key_echo.setter
    def private_key_echo(self, private_key_echo):
        r"""Sets the private_key_echo of this CreateCertificatePrivateKeyEchoRequestBody.

        证书回显开关，项目粒度的,默认情况下,\"private_key_echo\"是true,证书的返回体中展示私钥。 当值为false时,证书的返回体中不展示私钥。

        :param private_key_echo: The private_key_echo of this CreateCertificatePrivateKeyEchoRequestBody.
        :type private_key_echo: bool
        """
        self._private_key_echo = private_key_echo

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
        if not isinstance(other, CreateCertificatePrivateKeyEchoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
