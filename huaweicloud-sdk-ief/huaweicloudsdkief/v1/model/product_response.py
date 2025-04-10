# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'attributes': 'dict(str, ProductAttributes)',
        'project_id': 'str',
        'created_at': 'int',
        'tags': 'list[Attributes]',
        'private_key': 'str',
        'certificate': 'str',
        'ca': 'str',
        'package': 'str',
        'identifier': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'attributes': 'attributes',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'tags': 'tags',
        'private_key': 'private_key',
        'certificate': 'certificate',
        'ca': 'ca',
        'package': 'package',
        'identifier': 'identifier'
    }

    def __init__(self, id=None, name=None, description=None, attributes=None, project_id=None, created_at=None, tags=None, private_key=None, certificate=None, ca=None, package=None, identifier=None):
        r"""ProductResponse

        The model defined in huaweicloud sdk

        :param id: 产品id
        :type id: str
        :param name: 产品名称
        :type name: str
        :param description: 产品描述
        :type description: str
        :param attributes: 产品属性值
        :type attributes: dict(str, ProductAttributes)
        :param project_id: 产品所属账号的项目ID
        :type project_id: str
        :param created_at: 产品创建时间戳
        :type created_at: int
        :param tags: 产品标签
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        :param private_key: 产品私钥
        :type private_key: str
        :param certificate: 产品证书
        :type certificate: str
        :param ca: 产品根证书
        :type ca: str
        :param package: 将产品证书文件certificate/ca/private_key打成.tar.gz包后用base64编码的字符串。 使用时请使用base64解码成.tar.gz包。
        :type package: str
        :param identifier: 产品使用token注册时的凭证
        :type identifier: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._attributes = None
        self._project_id = None
        self._created_at = None
        self._tags = None
        self._private_key = None
        self._certificate = None
        self._ca = None
        self._package = None
        self._identifier = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if attributes is not None:
            self.attributes = attributes
        self.project_id = project_id
        if created_at is not None:
            self.created_at = created_at
        if tags is not None:
            self.tags = tags
        if private_key is not None:
            self.private_key = private_key
        if certificate is not None:
            self.certificate = certificate
        if ca is not None:
            self.ca = ca
        if package is not None:
            self.package = package
        if identifier is not None:
            self.identifier = identifier

    @property
    def id(self):
        r"""Gets the id of this ProductResponse.

        产品id

        :return: The id of this ProductResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProductResponse.

        产品id

        :param id: The id of this ProductResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ProductResponse.

        产品名称

        :return: The name of this ProductResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProductResponse.

        产品名称

        :param name: The name of this ProductResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ProductResponse.

        产品描述

        :return: The description of this ProductResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProductResponse.

        产品描述

        :param description: The description of this ProductResponse.
        :type description: str
        """
        self._description = description

    @property
    def attributes(self):
        r"""Gets the attributes of this ProductResponse.

        产品属性值

        :return: The attributes of this ProductResponse.
        :rtype: dict(str, ProductAttributes)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this ProductResponse.

        产品属性值

        :param attributes: The attributes of this ProductResponse.
        :type attributes: dict(str, ProductAttributes)
        """
        self._attributes = attributes

    @property
    def project_id(self):
        r"""Gets the project_id of this ProductResponse.

        产品所属账号的项目ID

        :return: The project_id of this ProductResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ProductResponse.

        产品所属账号的项目ID

        :param project_id: The project_id of this ProductResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this ProductResponse.

        产品创建时间戳

        :return: The created_at of this ProductResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ProductResponse.

        产品创建时间戳

        :param created_at: The created_at of this ProductResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def tags(self):
        r"""Gets the tags of this ProductResponse.

        产品标签

        :return: The tags of this ProductResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ProductResponse.

        产品标签

        :param tags: The tags of this ProductResponse.
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        self._tags = tags

    @property
    def private_key(self):
        r"""Gets the private_key of this ProductResponse.

        产品私钥

        :return: The private_key of this ProductResponse.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this ProductResponse.

        产品私钥

        :param private_key: The private_key of this ProductResponse.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate(self):
        r"""Gets the certificate of this ProductResponse.

        产品证书

        :return: The certificate of this ProductResponse.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this ProductResponse.

        产品证书

        :param certificate: The certificate of this ProductResponse.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def ca(self):
        r"""Gets the ca of this ProductResponse.

        产品根证书

        :return: The ca of this ProductResponse.
        :rtype: str
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        r"""Sets the ca of this ProductResponse.

        产品根证书

        :param ca: The ca of this ProductResponse.
        :type ca: str
        """
        self._ca = ca

    @property
    def package(self):
        r"""Gets the package of this ProductResponse.

        将产品证书文件certificate/ca/private_key打成.tar.gz包后用base64编码的字符串。 使用时请使用base64解码成.tar.gz包。

        :return: The package of this ProductResponse.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        r"""Sets the package of this ProductResponse.

        将产品证书文件certificate/ca/private_key打成.tar.gz包后用base64编码的字符串。 使用时请使用base64解码成.tar.gz包。

        :param package: The package of this ProductResponse.
        :type package: str
        """
        self._package = package

    @property
    def identifier(self):
        r"""Gets the identifier of this ProductResponse.

        产品使用token注册时的凭证

        :return: The identifier of this ProductResponse.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this ProductResponse.

        产品使用token注册时的凭证

        :param identifier: The identifier of this ProductResponse.
        :type identifier: str
        """
        self._identifier = identifier

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
        if not isinstance(other, ProductResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
