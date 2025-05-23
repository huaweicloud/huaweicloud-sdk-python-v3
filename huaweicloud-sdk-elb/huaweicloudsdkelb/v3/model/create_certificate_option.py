# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificateOption:

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
        'name': 'str',
        'private_key': 'str',
        'project_id': 'str',
        'type': 'str',
        'enterprise_project_id': 'str',
        'enc_certificate': 'str',
        'enc_private_key': 'str',
        'scm_certificate_id': 'str',
        'source': 'str',
        'protection_status': 'str',
        'protection_reason': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'certificate': 'certificate',
        'description': 'description',
        'domain': 'domain',
        'name': 'name',
        'private_key': 'private_key',
        'project_id': 'project_id',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'enc_certificate': 'enc_certificate',
        'enc_private_key': 'enc_private_key',
        'scm_certificate_id': 'scm_certificate_id',
        'source': 'source',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason'
    }

    def __init__(self, admin_state_up=None, certificate=None, description=None, domain=None, name=None, private_key=None, project_id=None, type=None, enterprise_project_id=None, enc_certificate=None, enc_private_key=None, scm_certificate_id=None, source=None, protection_status=None, protection_reason=None):
        r"""CreateCertificateOption

        The model defined in huaweicloud sdk

        :param admin_state_up: 证书的管理状态。  不支持该字段，请勿使用。
        :type admin_state_up: bool
        :param certificate: HTTPS协议使用的证书内容。 取值范围：PEM编码格式。 最大长度65536字符。 支持证书链，最大11层(含证书和证书链)。
        :type certificate: str
        :param description: 证书的描述。
        :type description: str
        :param domain: 服务器证书所签域名。该字段仅type为server时有效。  总长度为0-10000，由若干普通域名或泛域名组成，域名之间以\&quot;,\&quot;分隔，不超过100个域名。  普通域名：由若干字符串组成，字符串间以\&quot;.\&quot;分隔，单个字符串长度不超过63个字符， 只能包含英文字母、数字或\&quot;-\&quot;，且必须以字母或数字开头和结尾。例：www.test.com；  泛域名：在普通域名的基础上仅允许首字母为\&quot;\\*\&quot;。例：\\*.test.com
        :type domain: str
        :param name: 证书的名称。
        :type name: str
        :param private_key: HTTPS协议使用的私钥。当type为server时有效且必选。当type为client时，可以传或也可以不传，但都会被忽略；若传入则必须符合PEM格式。 取值范围：PEM编码格式。 最大长度8192字符。
        :type private_key: str
        :param project_id: 证书所在的项目ID。
        :type project_id: str
        :param type: SSL证书的类型。分为服务器证书(server)、CA证书(client)。 默认值：server
        :type type: str
        :param enterprise_project_id: 证书所属的企业项目ID。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: str
        :param enc_certificate: HTTPS协议使用的SM加密证书内容。支持证书链，最大11层(含证书和证书链)。  取值：PEM编码格式。最大长度65536字符。  使用说明：仅type为server_sm时有效且必选。
        :type enc_certificate: str
        :param enc_private_key: HTTPS协议使用的SM加密证书私钥。  取值：PEM编码格式。最大长度8192字符。  使用说明：仅type为server_sm时有效且必选。
        :type enc_private_key: str
        :param scm_certificate_id: SM证书ID。
        :type scm_certificate_id: str
        :param source: 参数解释：证书来源 取值范围：无  默认取值：当scm_certificate_id不为空，且未传入source时，默认取值为“scm”； 其他情况下默认为空。
        :type source: str
        :param protection_status: 参数解释：修改保护状态  约束限制：无  取值范围： - nonProtection: 不保护  - consoleProtection: 控制台修改保护  默认取值：nonProtection
        :type protection_status: str
        :param protection_reason: 参数解释：设置修改保护的原因  约束限制：仅当protection_status为consoleProtection时有效  取值范围：无  默认取值：空
        :type protection_reason: str
        """
        
        

        self._admin_state_up = None
        self._certificate = None
        self._description = None
        self._domain = None
        self._name = None
        self._private_key = None
        self._project_id = None
        self._type = None
        self._enterprise_project_id = None
        self._enc_certificate = None
        self._enc_private_key = None
        self._scm_certificate_id = None
        self._source = None
        self._protection_status = None
        self._protection_reason = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if certificate is not None:
            self.certificate = certificate
        if description is not None:
            self.description = description
        if domain is not None:
            self.domain = domain
        if name is not None:
            self.name = name
        if private_key is not None:
            self.private_key = private_key
        if project_id is not None:
            self.project_id = project_id
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enc_certificate is not None:
            self.enc_certificate = enc_certificate
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key
        if scm_certificate_id is not None:
            self.scm_certificate_id = scm_certificate_id
        if source is not None:
            self.source = source
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this CreateCertificateOption.

        证书的管理状态。  不支持该字段，请勿使用。

        :return: The admin_state_up of this CreateCertificateOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this CreateCertificateOption.

        证书的管理状态。  不支持该字段，请勿使用。

        :param admin_state_up: The admin_state_up of this CreateCertificateOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def certificate(self):
        r"""Gets the certificate of this CreateCertificateOption.

        HTTPS协议使用的证书内容。 取值范围：PEM编码格式。 最大长度65536字符。 支持证书链，最大11层(含证书和证书链)。

        :return: The certificate of this CreateCertificateOption.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this CreateCertificateOption.

        HTTPS协议使用的证书内容。 取值范围：PEM编码格式。 最大长度65536字符。 支持证书链，最大11层(含证书和证书链)。

        :param certificate: The certificate of this CreateCertificateOption.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def description(self):
        r"""Gets the description of this CreateCertificateOption.

        证书的描述。

        :return: The description of this CreateCertificateOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCertificateOption.

        证书的描述。

        :param description: The description of this CreateCertificateOption.
        :type description: str
        """
        self._description = description

    @property
    def domain(self):
        r"""Gets the domain of this CreateCertificateOption.

        服务器证书所签域名。该字段仅type为server时有效。  总长度为0-10000，由若干普通域名或泛域名组成，域名之间以\",\"分隔，不超过100个域名。  普通域名：由若干字符串组成，字符串间以\".\"分隔，单个字符串长度不超过63个字符， 只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。例：www.test.com；  泛域名：在普通域名的基础上仅允许首字母为\"\\*\"。例：\\*.test.com

        :return: The domain of this CreateCertificateOption.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this CreateCertificateOption.

        服务器证书所签域名。该字段仅type为server时有效。  总长度为0-10000，由若干普通域名或泛域名组成，域名之间以\",\"分隔，不超过100个域名。  普通域名：由若干字符串组成，字符串间以\".\"分隔，单个字符串长度不超过63个字符， 只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。例：www.test.com；  泛域名：在普通域名的基础上仅允许首字母为\"\\*\"。例：\\*.test.com

        :param domain: The domain of this CreateCertificateOption.
        :type domain: str
        """
        self._domain = domain

    @property
    def name(self):
        r"""Gets the name of this CreateCertificateOption.

        证书的名称。

        :return: The name of this CreateCertificateOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCertificateOption.

        证书的名称。

        :param name: The name of this CreateCertificateOption.
        :type name: str
        """
        self._name = name

    @property
    def private_key(self):
        r"""Gets the private_key of this CreateCertificateOption.

        HTTPS协议使用的私钥。当type为server时有效且必选。当type为client时，可以传或也可以不传，但都会被忽略；若传入则必须符合PEM格式。 取值范围：PEM编码格式。 最大长度8192字符。

        :return: The private_key of this CreateCertificateOption.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this CreateCertificateOption.

        HTTPS协议使用的私钥。当type为server时有效且必选。当type为client时，可以传或也可以不传，但都会被忽略；若传入则必须符合PEM格式。 取值范围：PEM编码格式。 最大长度8192字符。

        :param private_key: The private_key of this CreateCertificateOption.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateCertificateOption.

        证书所在的项目ID。

        :return: The project_id of this CreateCertificateOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateCertificateOption.

        证书所在的项目ID。

        :param project_id: The project_id of this CreateCertificateOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        r"""Gets the type of this CreateCertificateOption.

        SSL证书的类型。分为服务器证书(server)、CA证书(client)。 默认值：server

        :return: The type of this CreateCertificateOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateCertificateOption.

        SSL证书的类型。分为服务器证书(server)、CA证书(client)。 默认值：server

        :param type: The type of this CreateCertificateOption.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateCertificateOption.

        证书所属的企业项目ID。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this CreateCertificateOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateCertificateOption.

        证书所属的企业项目ID。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this CreateCertificateOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enc_certificate(self):
        r"""Gets the enc_certificate of this CreateCertificateOption.

        HTTPS协议使用的SM加密证书内容。支持证书链，最大11层(含证书和证书链)。  取值：PEM编码格式。最大长度65536字符。  使用说明：仅type为server_sm时有效且必选。

        :return: The enc_certificate of this CreateCertificateOption.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        r"""Sets the enc_certificate of this CreateCertificateOption.

        HTTPS协议使用的SM加密证书内容。支持证书链，最大11层(含证书和证书链)。  取值：PEM编码格式。最大长度65536字符。  使用说明：仅type为server_sm时有效且必选。

        :param enc_certificate: The enc_certificate of this CreateCertificateOption.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_private_key(self):
        r"""Gets the enc_private_key of this CreateCertificateOption.

        HTTPS协议使用的SM加密证书私钥。  取值：PEM编码格式。最大长度8192字符。  使用说明：仅type为server_sm时有效且必选。

        :return: The enc_private_key of this CreateCertificateOption.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        r"""Sets the enc_private_key of this CreateCertificateOption.

        HTTPS协议使用的SM加密证书私钥。  取值：PEM编码格式。最大长度8192字符。  使用说明：仅type为server_sm时有效且必选。

        :param enc_private_key: The enc_private_key of this CreateCertificateOption.
        :type enc_private_key: str
        """
        self._enc_private_key = enc_private_key

    @property
    def scm_certificate_id(self):
        r"""Gets the scm_certificate_id of this CreateCertificateOption.

        SM证书ID。

        :return: The scm_certificate_id of this CreateCertificateOption.
        :rtype: str
        """
        return self._scm_certificate_id

    @scm_certificate_id.setter
    def scm_certificate_id(self, scm_certificate_id):
        r"""Sets the scm_certificate_id of this CreateCertificateOption.

        SM证书ID。

        :param scm_certificate_id: The scm_certificate_id of this CreateCertificateOption.
        :type scm_certificate_id: str
        """
        self._scm_certificate_id = scm_certificate_id

    @property
    def source(self):
        r"""Gets the source of this CreateCertificateOption.

        参数解释：证书来源 取值范围：无  默认取值：当scm_certificate_id不为空，且未传入source时，默认取值为“scm”； 其他情况下默认为空。

        :return: The source of this CreateCertificateOption.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateCertificateOption.

        参数解释：证书来源 取值范围：无  默认取值：当scm_certificate_id不为空，且未传入source时，默认取值为“scm”； 其他情况下默认为空。

        :param source: The source of this CreateCertificateOption.
        :type source: str
        """
        self._source = source

    @property
    def protection_status(self):
        r"""Gets the protection_status of this CreateCertificateOption.

        参数解释：修改保护状态  约束限制：无  取值范围： - nonProtection: 不保护  - consoleProtection: 控制台修改保护  默认取值：nonProtection

        :return: The protection_status of this CreateCertificateOption.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this CreateCertificateOption.

        参数解释：修改保护状态  约束限制：无  取值范围： - nonProtection: 不保护  - consoleProtection: 控制台修改保护  默认取值：nonProtection

        :param protection_status: The protection_status of this CreateCertificateOption.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this CreateCertificateOption.

        参数解释：设置修改保护的原因  约束限制：仅当protection_status为consoleProtection时有效  取值范围：无  默认取值：空

        :return: The protection_reason of this CreateCertificateOption.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this CreateCertificateOption.

        参数解释：设置修改保护的原因  约束限制：仅当protection_status为consoleProtection时有效  取值范围：无  默认取值：空

        :param protection_reason: The protection_reason of this CreateCertificateOption.
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
        if not isinstance(other, CreateCertificateOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
