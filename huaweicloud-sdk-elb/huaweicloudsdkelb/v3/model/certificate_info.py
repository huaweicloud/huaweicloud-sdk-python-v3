# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'project_id': 'str',
        'enc_certificate': 'str',
        'enc_private_key': 'str',
        'scm_certificate_id': 'str',
        'common_name': 'str',
        'fingerprint': 'str',
        'subject_alternative_names': 'list[str]',
        'source': 'str',
        'protection_status': 'str',
        'protection_reason': 'str'
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
        'project_id': 'project_id',
        'enc_certificate': 'enc_certificate',
        'enc_private_key': 'enc_private_key',
        'scm_certificate_id': 'scm_certificate_id',
        'common_name': 'common_name',
        'fingerprint': 'fingerprint',
        'subject_alternative_names': 'subject_alternative_names',
        'source': 'source',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason'
    }

    def __init__(self, admin_state_up=None, certificate=None, description=None, domain=None, id=None, name=None, private_key=None, type=None, created_at=None, updated_at=None, expire_time=None, project_id=None, enc_certificate=None, enc_private_key=None, scm_certificate_id=None, common_name=None, fingerprint=None, subject_alternative_names=None, source=None, protection_status=None, protection_reason=None):
        r"""CertificateInfo

        The model defined in huaweicloud sdk

        :param admin_state_up: **参数解释**：证书的管理状态。该字段当前无用，设置为true或者false都不影响证书使用。  **取值范围**： - true：表示证书可用。 - false：表示证书不可用。
        :type admin_state_up: bool
        :param certificate: **参数解释**：证书内容。支持最大11层证书链(含证书和证书链)。  **取值范围**：PEM编码格式，最大长度65536个字符。
        :type certificate: str
        :param description: **参数解释**：证书的描述。  **取值范围**：0-255个字符。
        :type description: str
        :param domain: **参数解释**：服务器证书所签域名。  **取值范围**：总长度为0-10000，由若干普通域名或泛域名组成，域名之间以\&quot;,\&quot;分隔，不超过100个域名。 - 普通域名：由若干字符串组成，字符串间以\&quot;.\&quot;分隔，单个字符串长度不超过63个字符，只能包含英文字母、数字或\&quot;-\&quot;，且必须以字母或数字开头和结尾。例：www.test.com。 - 泛域名：在普通域名的基础上仅允许首字母为\&quot;\\*\&quot;。例：\\*.test.com。
        :type domain: str
        :param id: **参数解释**：ELB证书管理对象ID。  **取值范围**：由32位数字和小写字母组成。
        :type id: str
        :param name: **参数解释**：证书的名称。  **取值范围**：0-255个字符。
        :type name: str
        :param private_key: **参数解释**：服务器证书的私钥。  **取值范围**：PEM编码格式，最大长度8192个字符。
        :type private_key: str
        :param type: **参数解释**：证书的类型。  **取值范围**： - server：服务器证书。 - client：CA证书。 - server_sm：服务器SM双证书。
        :type type: str
        :param created_at: **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。
        :type created_at: str
        :param updated_at: **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。
        :type updated_at: str
        :param expire_time: **参数解释**：证书有效期的截止时间。  **取值范围**：格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。
        :type expire_time: str
        :param project_id: **参数解释**：项目ID。获取方式请参见[获取项目ID](elb_fl_0008.xml)。  **取值范围**：长度为32个字符，由小写字母和数字组成。
        :type project_id: str
        :param enc_certificate: **参数解释**：服务器SM双证书的证书内容。 支持最大11层证书链(含证书和证书链)。  **取值范围**：PEM编码格式。最大长度65536字符。
        :type enc_certificate: str
        :param enc_private_key: **参数解释**：服务器SM双证书的私钥。  **取值范围**：PEM编码格式，最大长度8192个字符。
        :type enc_private_key: str
        :param scm_certificate_id: **参数解释**：云证书管理服务（CCM）中的证书ID。  **取值范围**：不涉及
        :type scm_certificate_id: str
        :param common_name: **参数解释**：证书绑定的主域名。  **取值范围**：不涉及
        :type common_name: str
        :param fingerprint: **参数解释**：证书指纹。  **取值范围**：不涉及
        :type fingerprint: str
        :param subject_alternative_names: **参数解释**：证书绑定的域名列表。  **取值范围**：不涉及
        :type subject_alternative_names: list[str]
        :param source: **参数解释**：标记当前证书来源。  **取值范围**： - scm：表示关联云证书管理服务（CCM）中的证书。 - 空值：表示自有证书。
        :type source: str
        :param protection_status: **参数解释**：修改保护状态。  **取值范围**：  - nonProtection: 不保护  - consoleProtection: 控制台修改保护，即禁止通过控制台修改。
        :type protection_status: str
        :param protection_reason: **参数解释**：修改保护的原因。  **取值范围**：不涉及
        :type protection_reason: str
        """
        
        

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
        self._enc_certificate = None
        self._enc_private_key = None
        self._scm_certificate_id = None
        self._common_name = None
        self._fingerprint = None
        self._subject_alternative_names = None
        self._source = None
        self._protection_status = None
        self._protection_reason = None
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
        if enc_certificate is not None:
            self.enc_certificate = enc_certificate
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key
        if scm_certificate_id is not None:
            self.scm_certificate_id = scm_certificate_id
        if common_name is not None:
            self.common_name = common_name
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if subject_alternative_names is not None:
            self.subject_alternative_names = subject_alternative_names
        if source is not None:
            self.source = source
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this CertificateInfo.

        **参数解释**：证书的管理状态。该字段当前无用，设置为true或者false都不影响证书使用。  **取值范围**： - true：表示证书可用。 - false：表示证书不可用。

        :return: The admin_state_up of this CertificateInfo.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this CertificateInfo.

        **参数解释**：证书的管理状态。该字段当前无用，设置为true或者false都不影响证书使用。  **取值范围**： - true：表示证书可用。 - false：表示证书不可用。

        :param admin_state_up: The admin_state_up of this CertificateInfo.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def certificate(self):
        r"""Gets the certificate of this CertificateInfo.

        **参数解释**：证书内容。支持最大11层证书链(含证书和证书链)。  **取值范围**：PEM编码格式，最大长度65536个字符。

        :return: The certificate of this CertificateInfo.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this CertificateInfo.

        **参数解释**：证书内容。支持最大11层证书链(含证书和证书链)。  **取值范围**：PEM编码格式，最大长度65536个字符。

        :param certificate: The certificate of this CertificateInfo.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def description(self):
        r"""Gets the description of this CertificateInfo.

        **参数解释**：证书的描述。  **取值范围**：0-255个字符。

        :return: The description of this CertificateInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CertificateInfo.

        **参数解释**：证书的描述。  **取值范围**：0-255个字符。

        :param description: The description of this CertificateInfo.
        :type description: str
        """
        self._description = description

    @property
    def domain(self):
        r"""Gets the domain of this CertificateInfo.

        **参数解释**：服务器证书所签域名。  **取值范围**：总长度为0-10000，由若干普通域名或泛域名组成，域名之间以\",\"分隔，不超过100个域名。 - 普通域名：由若干字符串组成，字符串间以\".\"分隔，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。例：www.test.com。 - 泛域名：在普通域名的基础上仅允许首字母为\"\\*\"。例：\\*.test.com。

        :return: The domain of this CertificateInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this CertificateInfo.

        **参数解释**：服务器证书所签域名。  **取值范围**：总长度为0-10000，由若干普通域名或泛域名组成，域名之间以\",\"分隔，不超过100个域名。 - 普通域名：由若干字符串组成，字符串间以\".\"分隔，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。例：www.test.com。 - 泛域名：在普通域名的基础上仅允许首字母为\"\\*\"。例：\\*.test.com。

        :param domain: The domain of this CertificateInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def id(self):
        r"""Gets the id of this CertificateInfo.

        **参数解释**：ELB证书管理对象ID。  **取值范围**：由32位数字和小写字母组成。

        :return: The id of this CertificateInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CertificateInfo.

        **参数解释**：ELB证书管理对象ID。  **取值范围**：由32位数字和小写字母组成。

        :param id: The id of this CertificateInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CertificateInfo.

        **参数解释**：证书的名称。  **取值范围**：0-255个字符。

        :return: The name of this CertificateInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CertificateInfo.

        **参数解释**：证书的名称。  **取值范围**：0-255个字符。

        :param name: The name of this CertificateInfo.
        :type name: str
        """
        self._name = name

    @property
    def private_key(self):
        r"""Gets the private_key of this CertificateInfo.

        **参数解释**：服务器证书的私钥。  **取值范围**：PEM编码格式，最大长度8192个字符。

        :return: The private_key of this CertificateInfo.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this CertificateInfo.

        **参数解释**：服务器证书的私钥。  **取值范围**：PEM编码格式，最大长度8192个字符。

        :param private_key: The private_key of this CertificateInfo.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def type(self):
        r"""Gets the type of this CertificateInfo.

        **参数解释**：证书的类型。  **取值范围**： - server：服务器证书。 - client：CA证书。 - server_sm：服务器SM双证书。

        :return: The type of this CertificateInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CertificateInfo.

        **参数解释**：证书的类型。  **取值范围**： - server：服务器证书。 - client：CA证书。 - server_sm：服务器SM双证书。

        :param type: The type of this CertificateInfo.
        :type type: str
        """
        self._type = type

    @property
    def created_at(self):
        r"""Gets the created_at of this CertificateInfo.

        **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :return: The created_at of this CertificateInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CertificateInfo.

        **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :param created_at: The created_at of this CertificateInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CertificateInfo.

        **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :return: The updated_at of this CertificateInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CertificateInfo.

        **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :param updated_at: The updated_at of this CertificateInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CertificateInfo.

        **参数解释**：证书有效期的截止时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :return: The expire_time of this CertificateInfo.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CertificateInfo.

        **参数解释**：证书有效期的截止时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :param expire_time: The expire_time of this CertificateInfo.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def project_id(self):
        r"""Gets the project_id of this CertificateInfo.

        **参数解释**：项目ID。获取方式请参见[获取项目ID](elb_fl_0008.xml)。  **取值范围**：长度为32个字符，由小写字母和数字组成。

        :return: The project_id of this CertificateInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CertificateInfo.

        **参数解释**：项目ID。获取方式请参见[获取项目ID](elb_fl_0008.xml)。  **取值范围**：长度为32个字符，由小写字母和数字组成。

        :param project_id: The project_id of this CertificateInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enc_certificate(self):
        r"""Gets the enc_certificate of this CertificateInfo.

        **参数解释**：服务器SM双证书的证书内容。 支持最大11层证书链(含证书和证书链)。  **取值范围**：PEM编码格式。最大长度65536字符。

        :return: The enc_certificate of this CertificateInfo.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        r"""Sets the enc_certificate of this CertificateInfo.

        **参数解释**：服务器SM双证书的证书内容。 支持最大11层证书链(含证书和证书链)。  **取值范围**：PEM编码格式。最大长度65536字符。

        :param enc_certificate: The enc_certificate of this CertificateInfo.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_private_key(self):
        r"""Gets the enc_private_key of this CertificateInfo.

        **参数解释**：服务器SM双证书的私钥。  **取值范围**：PEM编码格式，最大长度8192个字符。

        :return: The enc_private_key of this CertificateInfo.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        r"""Sets the enc_private_key of this CertificateInfo.

        **参数解释**：服务器SM双证书的私钥。  **取值范围**：PEM编码格式，最大长度8192个字符。

        :param enc_private_key: The enc_private_key of this CertificateInfo.
        :type enc_private_key: str
        """
        self._enc_private_key = enc_private_key

    @property
    def scm_certificate_id(self):
        r"""Gets the scm_certificate_id of this CertificateInfo.

        **参数解释**：云证书管理服务（CCM）中的证书ID。  **取值范围**：不涉及

        :return: The scm_certificate_id of this CertificateInfo.
        :rtype: str
        """
        return self._scm_certificate_id

    @scm_certificate_id.setter
    def scm_certificate_id(self, scm_certificate_id):
        r"""Sets the scm_certificate_id of this CertificateInfo.

        **参数解释**：云证书管理服务（CCM）中的证书ID。  **取值范围**：不涉及

        :param scm_certificate_id: The scm_certificate_id of this CertificateInfo.
        :type scm_certificate_id: str
        """
        self._scm_certificate_id = scm_certificate_id

    @property
    def common_name(self):
        r"""Gets the common_name of this CertificateInfo.

        **参数解释**：证书绑定的主域名。  **取值范围**：不涉及

        :return: The common_name of this CertificateInfo.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        r"""Sets the common_name of this CertificateInfo.

        **参数解释**：证书绑定的主域名。  **取值范围**：不涉及

        :param common_name: The common_name of this CertificateInfo.
        :type common_name: str
        """
        self._common_name = common_name

    @property
    def fingerprint(self):
        r"""Gets the fingerprint of this CertificateInfo.

        **参数解释**：证书指纹。  **取值范围**：不涉及

        :return: The fingerprint of this CertificateInfo.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        r"""Sets the fingerprint of this CertificateInfo.

        **参数解释**：证书指纹。  **取值范围**：不涉及

        :param fingerprint: The fingerprint of this CertificateInfo.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def subject_alternative_names(self):
        r"""Gets the subject_alternative_names of this CertificateInfo.

        **参数解释**：证书绑定的域名列表。  **取值范围**：不涉及

        :return: The subject_alternative_names of this CertificateInfo.
        :rtype: list[str]
        """
        return self._subject_alternative_names

    @subject_alternative_names.setter
    def subject_alternative_names(self, subject_alternative_names):
        r"""Sets the subject_alternative_names of this CertificateInfo.

        **参数解释**：证书绑定的域名列表。  **取值范围**：不涉及

        :param subject_alternative_names: The subject_alternative_names of this CertificateInfo.
        :type subject_alternative_names: list[str]
        """
        self._subject_alternative_names = subject_alternative_names

    @property
    def source(self):
        r"""Gets the source of this CertificateInfo.

        **参数解释**：标记当前证书来源。  **取值范围**： - scm：表示关联云证书管理服务（CCM）中的证书。 - 空值：表示自有证书。

        :return: The source of this CertificateInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CertificateInfo.

        **参数解释**：标记当前证书来源。  **取值范围**： - scm：表示关联云证书管理服务（CCM）中的证书。 - 空值：表示自有证书。

        :param source: The source of this CertificateInfo.
        :type source: str
        """
        self._source = source

    @property
    def protection_status(self):
        r"""Gets the protection_status of this CertificateInfo.

        **参数解释**：修改保护状态。  **取值范围**：  - nonProtection: 不保护  - consoleProtection: 控制台修改保护，即禁止通过控制台修改。

        :return: The protection_status of this CertificateInfo.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this CertificateInfo.

        **参数解释**：修改保护状态。  **取值范围**：  - nonProtection: 不保护  - consoleProtection: 控制台修改保护，即禁止通过控制台修改。

        :param protection_status: The protection_status of this CertificateInfo.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this CertificateInfo.

        **参数解释**：修改保护的原因。  **取值范围**：不涉及

        :return: The protection_reason of this CertificateInfo.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this CertificateInfo.

        **参数解释**：修改保护的原因。  **取值范围**：不涉及

        :param protection_reason: The protection_reason of this CertificateInfo.
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
        if not isinstance(other, CertificateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
