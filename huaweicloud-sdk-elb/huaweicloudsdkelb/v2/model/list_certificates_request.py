# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'str',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'domain': 'str',
        'private_key': 'str',
        'certificate': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'domain': 'domain',
        'private_key': 'private_key',
        'certificate': 'certificate'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, name=None, description=None, type=None, domain=None, private_key=None, certificate=None):
        """ListCertificatesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：0~intmax。
        :type limit: int
        :param marker: 分页查询起始的证书id，为空时为查询第一页。 仅当和limit一起使用时生效
        :type marker: str
        :param page_reverse: 分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。 仅当和limit一起使用时生效。
        :type page_reverse: str
        :param id: SSL证书ID。
        :type id: str
        :param name: SSL证书的名称。
        :type name: str
        :param description: 证书描述SSL证书描述。
        :type description: str
        :param type: SSL证书的类型。默认值：server；取值范围：server：服务端证书；client：客户端证书；
        :type type: str
        :param domain: 服务端证书所签的域名。 取值：总长度为0-1024。  普通域名由若干字符串组成，字符串间以\&quot;.\&quot;分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\&quot;-\&quot;，且必须以字母或数字开头和结尾。  泛域名仅允许首段为\&quot;*\&quot;，其他取值限制与普通域名一致。如：*.domain.com，但不能是：*my.domain.com   该字段仅type为server时有效。
        :type domain: str
        :param private_key: PEM格式的服务端私有密钥。
        :type private_key: str
        :param certificate: PEM格式的服务端公有密钥或者用于认证客户端证书的CA证书，由type字段区分。
        :type certificate: str
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._domain = None
        self._private_key = None
        self._certificate = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if domain is not None:
            self.domain = domain
        if private_key is not None:
            self.private_key = private_key
        if certificate is not None:
            self.certificate = certificate

    @property
    def limit(self):
        """Gets the limit of this ListCertificatesRequest.

        每页返回的个数。 取值范围：0~intmax。

        :return: The limit of this ListCertificatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCertificatesRequest.

        每页返回的个数。 取值范围：0~intmax。

        :param limit: The limit of this ListCertificatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListCertificatesRequest.

        分页查询起始的证书id，为空时为查询第一页。 仅当和limit一起使用时生效

        :return: The marker of this ListCertificatesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListCertificatesRequest.

        分页查询起始的证书id，为空时为查询第一页。 仅当和limit一起使用时生效

        :param marker: The marker of this ListCertificatesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListCertificatesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。 仅当和limit一起使用时生效。

        :return: The page_reverse of this ListCertificatesRequest.
        :rtype: str
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListCertificatesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。 仅当和limit一起使用时生效。

        :param page_reverse: The page_reverse of this ListCertificatesRequest.
        :type page_reverse: str
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListCertificatesRequest.

        SSL证书ID。

        :return: The id of this ListCertificatesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListCertificatesRequest.

        SSL证书ID。

        :param id: The id of this ListCertificatesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListCertificatesRequest.

        SSL证书的名称。

        :return: The name of this ListCertificatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCertificatesRequest.

        SSL证书的名称。

        :param name: The name of this ListCertificatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListCertificatesRequest.

        证书描述SSL证书描述。

        :return: The description of this ListCertificatesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListCertificatesRequest.

        证书描述SSL证书描述。

        :param description: The description of this ListCertificatesRequest.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this ListCertificatesRequest.

        SSL证书的类型。默认值：server；取值范围：server：服务端证书；client：客户端证书；

        :return: The type of this ListCertificatesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListCertificatesRequest.

        SSL证书的类型。默认值：server；取值范围：server：服务端证书；client：客户端证书；

        :param type: The type of this ListCertificatesRequest.
        :type type: str
        """
        self._type = type

    @property
    def domain(self):
        """Gets the domain of this ListCertificatesRequest.

        服务端证书所签的域名。 取值：总长度为0-1024。  普通域名由若干字符串组成，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。  泛域名仅允许首段为\"*\"，其他取值限制与普通域名一致。如：*.domain.com，但不能是：*my.domain.com   该字段仅type为server时有效。

        :return: The domain of this ListCertificatesRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListCertificatesRequest.

        服务端证书所签的域名。 取值：总长度为0-1024。  普通域名由若干字符串组成，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。  泛域名仅允许首段为\"*\"，其他取值限制与普通域名一致。如：*.domain.com，但不能是：*my.domain.com   该字段仅type为server时有效。

        :param domain: The domain of this ListCertificatesRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def private_key(self):
        """Gets the private_key of this ListCertificatesRequest.

        PEM格式的服务端私有密钥。

        :return: The private_key of this ListCertificatesRequest.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this ListCertificatesRequest.

        PEM格式的服务端私有密钥。

        :param private_key: The private_key of this ListCertificatesRequest.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate(self):
        """Gets the certificate of this ListCertificatesRequest.

        PEM格式的服务端公有密钥或者用于认证客户端证书的CA证书，由type字段区分。

        :return: The certificate of this ListCertificatesRequest.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this ListCertificatesRequest.

        PEM格式的服务端公有密钥或者用于认证客户端证书的CA证书，由type字段区分。

        :param certificate: The certificate of this ListCertificatesRequest.
        :type certificate: str
        """
        self._certificate = certificate

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
        if not isinstance(other, ListCertificatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
