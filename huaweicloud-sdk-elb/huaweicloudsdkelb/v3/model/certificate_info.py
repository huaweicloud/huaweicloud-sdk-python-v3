# coding: utf-8

import pprint
import re

import six





class CertificateInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'certificate': 'str',
        'description': 'str',
        'domain': 'str',
        'id': 'str',
        'name': 'str',
        'private_key': 'str',
        'type': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'expire_time': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'certificate': 'certificate',
        'description': 'description',
        'domain': 'domain',
        'id': 'id',
        'name': 'name',
        'private_key': 'private_key',
        'type': 'type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'expire_time': 'expire_time',
        'project_id': 'project_id'
    }

    def __init__(self, admin_state_up=None, certificate=None, description=None, domain=None, id=None, name=None, private_key=None, type=None, created_at=None, updated_at=None, expire_time=None, project_id=None):
        """CertificateInfo - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._certificate = None
        self._description = None
        self._domain = None
        self._id = None
        self._name = None
        self._private_key = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._expire_time = None
        self._project_id = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.certificate = certificate
        self.description = description
        self.domain = domain
        self.id = id
        self.name = name
        self.private_key = private_key
        self.type = type
        self.created_at = created_at
        self.updated_at = updated_at
        self.expire_time = expire_time
        self.project_id = project_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CertificateInfo.

        SSL证书的管理状态；暂不支持

        :return: The admin_state_up of this CertificateInfo.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CertificateInfo.

        SSL证书的管理状态；暂不支持

        :param admin_state_up: The admin_state_up of this CertificateInfo.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def certificate(self):
        """Gets the certificate of this CertificateInfo.

        HTTPS协议使用的证书内容。 取值范围：PEM编码格式。

        :return: The certificate of this CertificateInfo.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this CertificateInfo.

        HTTPS协议使用的证书内容。 取值范围：PEM编码格式。

        :param certificate: The certificate of this CertificateInfo.
        :type: str
        """
        self._certificate = certificate

    @property
    def description(self):
        """Gets the description of this CertificateInfo.

        SSL证书的描述。

        :return: The description of this CertificateInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CertificateInfo.

        SSL证书的描述。

        :param description: The description of this CertificateInfo.
        :type: str
        """
        self._description = description

    @property
    def domain(self):
        """Gets the domain of this CertificateInfo.

        服务器证书所签域名。该字段仅type为server时有效。 总长度为0-1024，由若干普通域名或泛域名组成，域名之间以\",\"分割，不超过30个域名。 普通域名：由若干字符串组成，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。例：www.test.com； 泛域名：在普通域名的基础上仅允许首字母为\"*\"。例：*.test.com

        :return: The domain of this CertificateInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CertificateInfo.

        服务器证书所签域名。该字段仅type为server时有效。 总长度为0-1024，由若干普通域名或泛域名组成，域名之间以\",\"分割，不超过30个域名。 普通域名：由若干字符串组成，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。例：www.test.com； 泛域名：在普通域名的基础上仅允许首字母为\"*\"。例：*.test.com

        :param domain: The domain of this CertificateInfo.
        :type: str
        """
        self._domain = domain

    @property
    def id(self):
        """Gets the id of this CertificateInfo.

        证书ID。

        :return: The id of this CertificateInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CertificateInfo.

        证书ID。

        :param id: The id of this CertificateInfo.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CertificateInfo.

        SSL证书的名称。

        :return: The name of this CertificateInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertificateInfo.

        SSL证书的名称。

        :param name: The name of this CertificateInfo.
        :type: str
        """
        self._name = name

    @property
    def private_key(self):
        """Gets the private_key of this CertificateInfo.

        服务器证书的私钥。仅type为server时有效。type为server时必选。

        :return: The private_key of this CertificateInfo.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CertificateInfo.

        服务器证书的私钥。仅type为server时有效。type为server时必选。

        :param private_key: The private_key of this CertificateInfo.
        :type: str
        """
        self._private_key = private_key

    @property
    def type(self):
        """Gets the type of this CertificateInfo.

        SSL证书的类型。分为服务器证书(server)和CA证书(client)。 默认值：server

        :return: The type of this CertificateInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CertificateInfo.

        SSL证书的类型。分为服务器证书(server)和CA证书(client)。 默认值：server

        :param type: The type of this CertificateInfo.
        :type: str
        """
        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this CertificateInfo.

        证书创建时间。

        :return: The created_at of this CertificateInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CertificateInfo.

        证书创建时间。

        :param created_at: The created_at of this CertificateInfo.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CertificateInfo.

        证书更新时间。

        :return: The updated_at of this CertificateInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CertificateInfo.

        证书更新时间。

        :param updated_at: The updated_at of this CertificateInfo.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def expire_time(self):
        """Gets the expire_time of this CertificateInfo.

        证书使用截止时间。

        :return: The expire_time of this CertificateInfo.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CertificateInfo.

        证书使用截止时间。

        :param expire_time: The expire_time of this CertificateInfo.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def project_id(self):
        """Gets the project_id of this CertificateInfo.

        项目ID。

        :return: The project_id of this CertificateInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CertificateInfo.

        项目ID。

        :param project_id: The project_id of this CertificateInfo.
        :type: str
        """
        self._project_id = project_id

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
        if not isinstance(other, CertificateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
