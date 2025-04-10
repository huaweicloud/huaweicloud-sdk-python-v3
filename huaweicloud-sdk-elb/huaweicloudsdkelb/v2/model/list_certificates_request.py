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
        'certificate': 'str',
        'source': 'str',
        'protection_status': 'str',
        'protection_reason': 'str'
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
        'certificate': 'certificate',
        'source': 'source',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, name=None, description=None, type=None, domain=None, private_key=None, certificate=None, source=None, protection_status=None, protection_reason=None):
        r"""ListCertificatesRequest

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
        :param source: 参数解释： 证书来源  约束限制： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”。  取值范围： 无  默认取值： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”； 其他情况下默认为空。
        :type source: str
        :param protection_status: 参数解释： 修改保护状态  约束限制： 无  取值范围：  - nonProtection: 不保护  - consoleProtection: 控制台修改保护  默认取值： nonProtection
        :type protection_status: str
        :param protection_reason: 参数解释： 设置修改保护的原因  约束限制： 仅当protection_status为consoleProtection时有效  取值范围： 无  默认取值： 空
        :type protection_reason: str
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
        self._source = None
        self._protection_status = None
        self._protection_reason = None
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
        if source is not None:
            self.source = source
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason

    @property
    def limit(self):
        r"""Gets the limit of this ListCertificatesRequest.

        每页返回的个数。 取值范围：0~intmax。

        :return: The limit of this ListCertificatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCertificatesRequest.

        每页返回的个数。 取值范围：0~intmax。

        :param limit: The limit of this ListCertificatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListCertificatesRequest.

        分页查询起始的证书id，为空时为查询第一页。 仅当和limit一起使用时生效

        :return: The marker of this ListCertificatesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListCertificatesRequest.

        分页查询起始的证书id，为空时为查询第一页。 仅当和limit一起使用时生效

        :param marker: The marker of this ListCertificatesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListCertificatesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。 仅当和limit一起使用时生效。

        :return: The page_reverse of this ListCertificatesRequest.
        :rtype: str
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListCertificatesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。 仅当和limit一起使用时生效。

        :param page_reverse: The page_reverse of this ListCertificatesRequest.
        :type page_reverse: str
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListCertificatesRequest.

        SSL证书ID。

        :return: The id of this ListCertificatesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListCertificatesRequest.

        SSL证书ID。

        :param id: The id of this ListCertificatesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListCertificatesRequest.

        SSL证书的名称。

        :return: The name of this ListCertificatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCertificatesRequest.

        SSL证书的名称。

        :param name: The name of this ListCertificatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListCertificatesRequest.

        证书描述SSL证书描述。

        :return: The description of this ListCertificatesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListCertificatesRequest.

        证书描述SSL证书描述。

        :param description: The description of this ListCertificatesRequest.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this ListCertificatesRequest.

        SSL证书的类型。默认值：server；取值范围：server：服务端证书；client：客户端证书；

        :return: The type of this ListCertificatesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListCertificatesRequest.

        SSL证书的类型。默认值：server；取值范围：server：服务端证书；client：客户端证书；

        :param type: The type of this ListCertificatesRequest.
        :type type: str
        """
        self._type = type

    @property
    def domain(self):
        r"""Gets the domain of this ListCertificatesRequest.

        服务端证书所签的域名。 取值：总长度为0-1024。  普通域名由若干字符串组成，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。  泛域名仅允许首段为\"*\"，其他取值限制与普通域名一致。如：*.domain.com，但不能是：*my.domain.com   该字段仅type为server时有效。

        :return: The domain of this ListCertificatesRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListCertificatesRequest.

        服务端证书所签的域名。 取值：总长度为0-1024。  普通域名由若干字符串组成，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。  泛域名仅允许首段为\"*\"，其他取值限制与普通域名一致。如：*.domain.com，但不能是：*my.domain.com   该字段仅type为server时有效。

        :param domain: The domain of this ListCertificatesRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def private_key(self):
        r"""Gets the private_key of this ListCertificatesRequest.

        PEM格式的服务端私有密钥。

        :return: The private_key of this ListCertificatesRequest.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this ListCertificatesRequest.

        PEM格式的服务端私有密钥。

        :param private_key: The private_key of this ListCertificatesRequest.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate(self):
        r"""Gets the certificate of this ListCertificatesRequest.

        PEM格式的服务端公有密钥或者用于认证客户端证书的CA证书，由type字段区分。

        :return: The certificate of this ListCertificatesRequest.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this ListCertificatesRequest.

        PEM格式的服务端公有密钥或者用于认证客户端证书的CA证书，由type字段区分。

        :param certificate: The certificate of this ListCertificatesRequest.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def source(self):
        r"""Gets the source of this ListCertificatesRequest.

        参数解释： 证书来源  约束限制： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”。  取值范围： 无  默认取值： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”； 其他情况下默认为空。

        :return: The source of this ListCertificatesRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ListCertificatesRequest.

        参数解释： 证书来源  约束限制： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”。  取值范围： 无  默认取值： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”； 其他情况下默认为空。

        :param source: The source of this ListCertificatesRequest.
        :type source: str
        """
        self._source = source

    @property
    def protection_status(self):
        r"""Gets the protection_status of this ListCertificatesRequest.

        参数解释： 修改保护状态  约束限制： 无  取值范围：  - nonProtection: 不保护  - consoleProtection: 控制台修改保护  默认取值： nonProtection

        :return: The protection_status of this ListCertificatesRequest.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this ListCertificatesRequest.

        参数解释： 修改保护状态  约束限制： 无  取值范围：  - nonProtection: 不保护  - consoleProtection: 控制台修改保护  默认取值： nonProtection

        :param protection_status: The protection_status of this ListCertificatesRequest.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this ListCertificatesRequest.

        参数解释： 设置修改保护的原因  约束限制： 仅当protection_status为consoleProtection时有效  取值范围： 无  默认取值： 空

        :return: The protection_reason of this ListCertificatesRequest.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this ListCertificatesRequest.

        参数解释： 设置修改保护的原因  约束限制： 仅当protection_status为consoleProtection时有效  取值范围： 无  默认取值： 空

        :param protection_reason: The protection_reason of this ListCertificatesRequest.
        :type protection_reason: str
        """
        self._protection_reason = protection_reason

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
