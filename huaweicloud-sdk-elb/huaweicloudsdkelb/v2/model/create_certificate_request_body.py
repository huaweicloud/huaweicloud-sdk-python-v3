# coding: utf-8

import pprint
import re

import six





class CreateCertificateRequestBody:


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
        'private_key': 'str',
        'description': 'str',
        'domain': 'str',
        'name': 'str',
        'admin_state_up': 'bool',
        'type': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'private_key': 'private_key',
        'description': 'description',
        'domain': 'domain',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, certificate=None, private_key=None, description=None, domain=None, name=None, admin_state_up=None, type=None, enterprise_project_id=None):
        """CreateCertificateRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._certificate = None
        self._private_key = None
        self._description = None
        self._domain = None
        self._name = None
        self._admin_state_up = None
        self._type = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key
        if description is not None:
            self.description = description
        if domain is not None:
            self.domain = domain
        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def certificate(self):
        """Gets the certificate of this CreateCertificateRequestBody.

        服务端公有密钥证书或者用于认证客户端证书的CA证书，由type字段区分。 格式：证书为PEM格式。

        :return: The certificate of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this CreateCertificateRequestBody.

        服务端公有密钥证书或者用于认证客户端证书的CA证书，由type字段区分。 格式：证书为PEM格式。

        :param certificate: The certificate of this CreateCertificateRequestBody.
        :type: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        """Gets the private_key of this CreateCertificateRequestBody.

        服务端的私有密钥。 格式：私钥为PEM格式。 该字段仅type为server时有效且为必选。 该字段在type为client时无效。

        :return: The private_key of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CreateCertificateRequestBody.

        服务端的私有密钥。 格式：私钥为PEM格式。 该字段仅type为server时有效且为必选。 该字段在type为client时无效。

        :param private_key: The private_key of this CreateCertificateRequestBody.
        :type: str
        """
        self._private_key = private_key

    @property
    def description(self):
        """Gets the description of this CreateCertificateRequestBody.

        SSL证书的描述信息。支持的最大字符长度：255

        :return: The description of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCertificateRequestBody.

        SSL证书的描述信息。支持的最大字符长度：255

        :param description: The description of this CreateCertificateRequestBody.
        :type: str
        """
        self._description = description

    @property
    def domain(self):
        """Gets the domain of this CreateCertificateRequestBody.

        服务端证书所签的域名。默认值：null；支持的最大字符长度：100 取值范围： 普通域名由若干字符串组成，总长度为0-100，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。 泛域名在普通域名的基础上仅允许首字母为\"*\"。 该字段仅type为server时有效。

        :return: The domain of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateCertificateRequestBody.

        服务端证书所签的域名。默认值：null；支持的最大字符长度：100 取值范围： 普通域名由若干字符串组成，总长度为0-100，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。 泛域名在普通域名的基础上仅允许首字母为\"*\"。 该字段仅type为server时有效。

        :param domain: The domain of this CreateCertificateRequestBody.
        :type: str
        """
        self._domain = domain

    @property
    def name(self):
        """Gets the name of this CreateCertificateRequestBody.

        SSL证书的名称。支持的最大字符长度：255

        :return: The name of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCertificateRequestBody.

        SSL证书的名称。支持的最大字符长度：255

        :param name: The name of this CreateCertificateRequestBody.
        :type: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateCertificateRequestBody.

        SSL证书的管理状态； 取值范围： true/false。 该字段为预留字段，暂未启用。只支持设定为true。

        :return: The admin_state_up of this CreateCertificateRequestBody.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateCertificateRequestBody.

        SSL证书的管理状态； 取值范围： true/false。 该字段为预留字段，暂未启用。只支持设定为true。

        :param admin_state_up: The admin_state_up of this CreateCertificateRequestBody.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def type(self):
        """Gets the type of this CreateCertificateRequestBody.

        SSL证书的类型。默认值：server； 取值范围： server：服务端证书； client：客户端证书；

        :return: The type of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateCertificateRequestBody.

        SSL证书的类型。默认值：server； 取值范围： server：服务端证书； client：客户端证书；

        :param type: The type of this CreateCertificateRequestBody.
        :type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateCertificateRequestBody.

        企业项目ID。创建负载均衡器时，给负载均衡器绑定企业项目ID。取值范围：带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。默认值：\"0\"

        :return: The enterprise_project_id of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateCertificateRequestBody.

        企业项目ID。创建负载均衡器时，给负载均衡器绑定企业项目ID。取值范围：带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。默认值：\"0\"

        :param enterprise_project_id: The enterprise_project_id of this CreateCertificateRequestBody.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
