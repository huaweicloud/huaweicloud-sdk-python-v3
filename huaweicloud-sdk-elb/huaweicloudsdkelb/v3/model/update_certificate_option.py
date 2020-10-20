# coding: utf-8

import pprint
import re

import six





class UpdateCertificateOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'certificate': 'str',
        'description': 'str',
        'name': 'str',
        'private_key': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'description': 'description',
        'name': 'name',
        'private_key': 'private_key',
        'domain': 'domain'
    }

    def __init__(self, certificate=None, description=None, name=None, private_key=None, domain=None):
        """UpdateCertificateOption - a model defined in huaweicloud sdk"""
        
        

        self._certificate = None
        self._description = None
        self._name = None
        self._private_key = None
        self._domain = None
        self.discriminator = None

        if certificate is not None:
            self.certificate = certificate
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if private_key is not None:
            self.private_key = private_key
        if domain is not None:
            self.domain = domain

    @property
    def certificate(self):
        """Gets the certificate of this UpdateCertificateOption.

        HTTPS协议使用的证书内容。 取值范围：PEM编码格式。

        :return: The certificate of this UpdateCertificateOption.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this UpdateCertificateOption.

        HTTPS协议使用的证书内容。 取值范围：PEM编码格式。

        :param certificate: The certificate of this UpdateCertificateOption.
        :type: str
        """
        self._certificate = certificate

    @property
    def description(self):
        """Gets the description of this UpdateCertificateOption.

        SSL证书的描述。

        :return: The description of this UpdateCertificateOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCertificateOption.

        SSL证书的描述。

        :param description: The description of this UpdateCertificateOption.
        :type: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this UpdateCertificateOption.

        SSL证书的名称。

        :return: The name of this UpdateCertificateOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCertificateOption.

        SSL证书的名称。

        :param name: The name of this UpdateCertificateOption.
        :type: str
        """
        self._name = name

    @property
    def private_key(self):
        """Gets the private_key of this UpdateCertificateOption.

        HTTPS协议使用的私钥。仅type为server时有效。type为server时必选。 取值范围：PEM编码格式。

        :return: The private_key of this UpdateCertificateOption.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this UpdateCertificateOption.

        HTTPS协议使用的私钥。仅type为server时有效。type为server时必选。 取值范围：PEM编码格式。

        :param private_key: The private_key of this UpdateCertificateOption.
        :type: str
        """
        self._private_key = private_key

    @property
    def domain(self):
        """Gets the domain of this UpdateCertificateOption.

        服务器证书所签域名。该字段仅type为server时有效。 总长度为0-1024，由若干普通域名或泛域名组成，域名之间以\",\"分割，不超过30个域名。 普通域名：由若干字符串组成，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。例：www.test.com； 泛域名：在普通域名的基础上仅允许首字母为\"*\"。例：*.test.com

        :return: The domain of this UpdateCertificateOption.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this UpdateCertificateOption.

        服务器证书所签域名。该字段仅type为server时有效。 总长度为0-1024，由若干普通域名或泛域名组成，域名之间以\",\"分割，不超过30个域名。 普通域名：由若干字符串组成，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。例：www.test.com； 泛域名：在普通域名的基础上仅允许首字母为\"*\"。例：*.test.com

        :param domain: The domain of this UpdateCertificateOption.
        :type: str
        """
        self._domain = domain

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateCertificateOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
