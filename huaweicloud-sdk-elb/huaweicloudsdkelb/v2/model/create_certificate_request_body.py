# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'enterprise_project_id': 'str',
        'source': 'str',
        'protection_status': 'str',
        'protection_reason': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'private_key': 'private_key',
        'description': 'description',
        'domain': 'domain',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'source': 'source',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason'
    }

    def __init__(self, certificate=None, private_key=None, description=None, domain=None, name=None, admin_state_up=None, type=None, enterprise_project_id=None, source=None, protection_status=None, protection_reason=None):
        r"""CreateCertificateRequestBody

        The model defined in huaweicloud sdk

        :param certificate: 服务端公有密钥证书或者用于认证客户端证书的CA证书，由type字段区分。 格式：证书为PEM格式。
        :type certificate: str
        :param private_key: 服务端的私有密钥。 格式：私钥为PEM格式。 该字段仅type为server时有效且为必选。 该字段在type为client时无效。
        :type private_key: str
        :param description: SSL证书的描述信息。支持的最大字符长度：255
        :type description: str
        :param domain: 服务端证书所签的域名。  取值：总长度为0-1024。  普通域名由若干字符串组成，字符串间以\&quot;.\&quot;分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\&quot;-\&quot;，且必须以字母或数字开头和结尾。  泛域名仅允许首段为\&quot;*\&quot;，其他取值限制与普通域名一致。如：*.domain.com，但不能是：*my.domain.com  该字段仅type为server时有效。
        :type domain: str
        :param name: SSL证书的名称。支持的最大字符长度：255
        :type name: str
        :param admin_state_up: SSL证书的管理状态； 取值范围： true/false。 该字段为预留字段，暂未启用。只支持设定为true。
        :type admin_state_up: bool
        :param type: SSL证书的类型。默认值：server； 取值范围： server：服务端证书； client：客户端证书；
        :type type: str
        :param enterprise_project_id: 企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\&quot;0\&quot;表示查询默认企业项目资源；或者指定的企业项目ID下的资源。
        :type enterprise_project_id: str
        :param source: 参数解释： 证书来源  约束限制： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”。  取值范围： 无  默认取值： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”； 其他情况下默认为空。
        :type source: str
        :param protection_status: 参数解释： 修改保护状态  约束限制： 无  取值范围：  - nonProtection: 不保护 - consoleProtection: 控制台修改保护  默认取值： nonProtection
        :type protection_status: str
        :param protection_reason: 参数解释： 设置修改保护的原因  约束限制： 仅当protection_status为consoleProtection时有效  取值范围： 无  默认取值： 空
        :type protection_reason: str
        """
        
        

        self._certificate = None
        self._private_key = None
        self._description = None
        self._domain = None
        self._name = None
        self._admin_state_up = None
        self._type = None
        self._enterprise_project_id = None
        self._source = None
        self._protection_status = None
        self._protection_reason = None
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
        if source is not None:
            self.source = source
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason

    @property
    def certificate(self):
        r"""Gets the certificate of this CreateCertificateRequestBody.

        服务端公有密钥证书或者用于认证客户端证书的CA证书，由type字段区分。 格式：证书为PEM格式。

        :return: The certificate of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this CreateCertificateRequestBody.

        服务端公有密钥证书或者用于认证客户端证书的CA证书，由type字段区分。 格式：证书为PEM格式。

        :param certificate: The certificate of this CreateCertificateRequestBody.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        r"""Gets the private_key of this CreateCertificateRequestBody.

        服务端的私有密钥。 格式：私钥为PEM格式。 该字段仅type为server时有效且为必选。 该字段在type为client时无效。

        :return: The private_key of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this CreateCertificateRequestBody.

        服务端的私有密钥。 格式：私钥为PEM格式。 该字段仅type为server时有效且为必选。 该字段在type为client时无效。

        :param private_key: The private_key of this CreateCertificateRequestBody.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def description(self):
        r"""Gets the description of this CreateCertificateRequestBody.

        SSL证书的描述信息。支持的最大字符长度：255

        :return: The description of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCertificateRequestBody.

        SSL证书的描述信息。支持的最大字符长度：255

        :param description: The description of this CreateCertificateRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def domain(self):
        r"""Gets the domain of this CreateCertificateRequestBody.

        服务端证书所签的域名。  取值：总长度为0-1024。  普通域名由若干字符串组成，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。  泛域名仅允许首段为\"*\"，其他取值限制与普通域名一致。如：*.domain.com，但不能是：*my.domain.com  该字段仅type为server时有效。

        :return: The domain of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this CreateCertificateRequestBody.

        服务端证书所签的域名。  取值：总长度为0-1024。  普通域名由若干字符串组成，字符串间以\".\"分割，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。  泛域名仅允许首段为\"*\"，其他取值限制与普通域名一致。如：*.domain.com，但不能是：*my.domain.com  该字段仅type为server时有效。

        :param domain: The domain of this CreateCertificateRequestBody.
        :type domain: str
        """
        self._domain = domain

    @property
    def name(self):
        r"""Gets the name of this CreateCertificateRequestBody.

        SSL证书的名称。支持的最大字符长度：255

        :return: The name of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCertificateRequestBody.

        SSL证书的名称。支持的最大字符长度：255

        :param name: The name of this CreateCertificateRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this CreateCertificateRequestBody.

        SSL证书的管理状态； 取值范围： true/false。 该字段为预留字段，暂未启用。只支持设定为true。

        :return: The admin_state_up of this CreateCertificateRequestBody.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this CreateCertificateRequestBody.

        SSL证书的管理状态； 取值范围： true/false。 该字段为预留字段，暂未启用。只支持设定为true。

        :param admin_state_up: The admin_state_up of this CreateCertificateRequestBody.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def type(self):
        r"""Gets the type of this CreateCertificateRequestBody.

        SSL证书的类型。默认值：server； 取值范围： server：服务端证书； client：客户端证书；

        :return: The type of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateCertificateRequestBody.

        SSL证书的类型。默认值：server； 取值范围： server：服务端证书； client：客户端证书；

        :param type: The type of this CreateCertificateRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateCertificateRequestBody.

        企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\"0\"表示查询默认企业项目资源；或者指定的企业项目ID下的资源。

        :return: The enterprise_project_id of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateCertificateRequestBody.

        企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\"0\"表示查询默认企业项目资源；或者指定的企业项目ID下的资源。

        :param enterprise_project_id: The enterprise_project_id of this CreateCertificateRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def source(self):
        r"""Gets the source of this CreateCertificateRequestBody.

        参数解释： 证书来源  约束限制： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”。  取值范围： 无  默认取值： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”； 其他情况下默认为空。

        :return: The source of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateCertificateRequestBody.

        参数解释： 证书来源  约束限制： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”。  取值范围： 无  默认取值： 当scm_certificate_id不为空，且未传入source时，默认取值为“scm”； 其他情况下默认为空。

        :param source: The source of this CreateCertificateRequestBody.
        :type source: str
        """
        self._source = source

    @property
    def protection_status(self):
        r"""Gets the protection_status of this CreateCertificateRequestBody.

        参数解释： 修改保护状态  约束限制： 无  取值范围：  - nonProtection: 不保护 - consoleProtection: 控制台修改保护  默认取值： nonProtection

        :return: The protection_status of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this CreateCertificateRequestBody.

        参数解释： 修改保护状态  约束限制： 无  取值范围：  - nonProtection: 不保护 - consoleProtection: 控制台修改保护  默认取值： nonProtection

        :param protection_status: The protection_status of this CreateCertificateRequestBody.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this CreateCertificateRequestBody.

        参数解释： 设置修改保护的原因  约束限制： 仅当protection_status为consoleProtection时有效  取值范围： 无  默认取值： 空

        :return: The protection_reason of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this CreateCertificateRequestBody.

        参数解释： 设置修改保护的原因  约束限制： 仅当protection_status为consoleProtection时有效  取值范围： 无  默认取值： 空

        :param protection_reason: The protection_reason of this CreateCertificateRequestBody.
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
        if not isinstance(other, CreateCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
