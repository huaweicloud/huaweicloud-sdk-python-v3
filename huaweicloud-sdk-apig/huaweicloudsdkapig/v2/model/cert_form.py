# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertForm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_content': 'str',
        'name': 'str',
        'private_key': 'str'
    }

    attribute_map = {
        'cert_content': 'cert_content',
        'name': 'name',
        'private_key': 'private_key'
    }

    def __init__(self, cert_content=None, name=None, private_key=None):
        r"""CertForm

        The model defined in huaweicloud sdk

        :param cert_content: 证书内容
        :type cert_content: str
        :param name: 证书名称。长度为4 ~ 50位的字符串，字符串由中文、英文字母、数字、下划线组成，且只能以英文或中文开头。
        :type name: str
        :param private_key: 私钥内容
        :type private_key: str
        """
        
        

        self._cert_content = None
        self._name = None
        self._private_key = None
        self.discriminator = None

        self.cert_content = cert_content
        self.name = name
        self.private_key = private_key

    @property
    def cert_content(self):
        r"""Gets the cert_content of this CertForm.

        证书内容

        :return: The cert_content of this CertForm.
        :rtype: str
        """
        return self._cert_content

    @cert_content.setter
    def cert_content(self, cert_content):
        r"""Sets the cert_content of this CertForm.

        证书内容

        :param cert_content: The cert_content of this CertForm.
        :type cert_content: str
        """
        self._cert_content = cert_content

    @property
    def name(self):
        r"""Gets the name of this CertForm.

        证书名称。长度为4 ~ 50位的字符串，字符串由中文、英文字母、数字、下划线组成，且只能以英文或中文开头。

        :return: The name of this CertForm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CertForm.

        证书名称。长度为4 ~ 50位的字符串，字符串由中文、英文字母、数字、下划线组成，且只能以英文或中文开头。

        :param name: The name of this CertForm.
        :type name: str
        """
        self._name = name

    @property
    def private_key(self):
        r"""Gets the private_key of this CertForm.

        私钥内容

        :return: The private_key of this CertForm.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this CertForm.

        私钥内容

        :param private_key: The private_key of this CertForm.
        :type private_key: str
        """
        self._private_key = private_key

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
        if not isinstance(other, CertForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
