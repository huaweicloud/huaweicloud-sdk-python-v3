# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'domain': 'str',
        'enc_certificate': 'str',
        'enc_private_key': 'str',
        'scm_certificate_id': 'str',
        'source': 'str',
        'protection_status': 'str',
        'protection_reason': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'description': 'description',
        'name': 'name',
        'private_key': 'private_key',
        'domain': 'domain',
        'enc_certificate': 'enc_certificate',
        'enc_private_key': 'enc_private_key',
        'scm_certificate_id': 'scm_certificate_id',
        'source': 'source',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason'
    }

    def __init__(self, certificate=None, description=None, name=None, private_key=None, domain=None, enc_certificate=None, enc_private_key=None, scm_certificate_id=None, source=None, protection_status=None, protection_reason=None):
        r"""UpdateCertificateOption

        The model defined in huaweicloud sdk

        :param certificate: **参数解释**：证书内容。 支持最大11层证书链(含证书和证书链)。  **约束限制**：不涉及  **取值范围**：PEM编码格式，最大长度65536个字符。  **默认取值**：不涉及
        :type certificate: str
        :param description: **参数解释**：证书的描述。  **约束限制**：不涉及  **取值范围**：0-255个字符。  **默认取值**：不涉及
        :type description: str
        :param name: **参数解释**：证书的名称。  **约束限制**：不涉及  **取值范围**：0-255个字符。  **默认取值**：不涉及
        :type name: str
        :param private_key: **参数解释**：服务器证书的私钥。  **约束限制**：不涉及  **取值范围**：PEM编码格式，最大长度8192个字符。  **默认取值**：不涉及
        :type private_key: str
        :param domain: **参数解释**：服务器证书所签域名。  **约束限制**：该字段仅type为server时有效（其他类型证书，字段可传入，但不会生效）。  **取值范围**：总长度为0-10000，由若干普通域名或泛域名组成，域名之间以\&quot;,\&quot;分隔，不超过100个域名。 - 普通域名：由若干字符串组成，字符串间以\&quot;.\&quot;分隔，单个字符串长度不超过63个字符，只能包含英文字母、数字或\&quot;-\&quot;，且必须以字母或数字开头和结尾。例：www.test.com。 - 泛域名：在普通域名的基础上仅允许首字母为\&quot;\\*\&quot;。例：\\*.test.com。  **默认取值**：不涉及
        :type domain: str
        :param enc_certificate: **参数解释**：服务器SM双证书的证书内容。 支持最大11层证书链(含证书和证书链)。  **约束限制**：仅当type为server_sm时，才支持传入。  **取值范围**：PEM编码格式。最大长度65536字符。  **默认取值**：不涉及
        :type enc_certificate: str
        :param enc_private_key: **参数解释**：服务器SM双证书的私钥。  **约束限制**：仅当type为server_sm时，才支持传入。  **取值范围**：PEM编码格式，最大长度8192个字符。  **默认取值**：不涉及
        :type enc_private_key: str
        :param scm_certificate_id: **参数解释**：云证书管理服务（CCM）中的证书ID。  **约束限制**：仅记录证书ID，不验证其是否真实存在云证书管理服务中。并且需要将云证书管理服务中对应证书的内容手动设置到当前接口相应字段中（可能涉及字段certificate、private_key、enc_certificate和enc_private_key）  **取值范围**：不涉及  **默认取值**：不涉及
        :type scm_certificate_id: str
        :param source: **参数解释**：标记当前证书来源。  **约束限制**：无  **取值范围**： - scm：表示关联云证书管理服务（CCM）中的证书。 - 空值：表示自有证书。  **默认取值**：不涉及
        :type source: str
        :param protection_status: **参数解释**：修改保护状态   **约束限制**：不涉及   **取值范围**：  - nonProtection: 不保护  - consoleProtection: 控制台修改保护   **默认取值**：不涉及
        :type protection_status: str
        :param protection_reason: **参数解释**：设置修改保护的原因   **约束限制**：仅当protection_status为consoleProtection时有效   **取值范围**：不涉及   **默认取值**：空
        :type protection_reason: str
        """
        
        

        self._certificate = None
        self._description = None
        self._name = None
        self._private_key = None
        self._domain = None
        self._enc_certificate = None
        self._enc_private_key = None
        self._scm_certificate_id = None
        self._source = None
        self._protection_status = None
        self._protection_reason = None
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
    def certificate(self):
        r"""Gets the certificate of this UpdateCertificateOption.

        **参数解释**：证书内容。 支持最大11层证书链(含证书和证书链)。  **约束限制**：不涉及  **取值范围**：PEM编码格式，最大长度65536个字符。  **默认取值**：不涉及

        :return: The certificate of this UpdateCertificateOption.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this UpdateCertificateOption.

        **参数解释**：证书内容。 支持最大11层证书链(含证书和证书链)。  **约束限制**：不涉及  **取值范围**：PEM编码格式，最大长度65536个字符。  **默认取值**：不涉及

        :param certificate: The certificate of this UpdateCertificateOption.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def description(self):
        r"""Gets the description of this UpdateCertificateOption.

        **参数解释**：证书的描述。  **约束限制**：不涉及  **取值范围**：0-255个字符。  **默认取值**：不涉及

        :return: The description of this UpdateCertificateOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateCertificateOption.

        **参数解释**：证书的描述。  **约束限制**：不涉及  **取值范围**：0-255个字符。  **默认取值**：不涉及

        :param description: The description of this UpdateCertificateOption.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this UpdateCertificateOption.

        **参数解释**：证书的名称。  **约束限制**：不涉及  **取值范围**：0-255个字符。  **默认取值**：不涉及

        :return: The name of this UpdateCertificateOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateCertificateOption.

        **参数解释**：证书的名称。  **约束限制**：不涉及  **取值范围**：0-255个字符。  **默认取值**：不涉及

        :param name: The name of this UpdateCertificateOption.
        :type name: str
        """
        self._name = name

    @property
    def private_key(self):
        r"""Gets the private_key of this UpdateCertificateOption.

        **参数解释**：服务器证书的私钥。  **约束限制**：不涉及  **取值范围**：PEM编码格式，最大长度8192个字符。  **默认取值**：不涉及

        :return: The private_key of this UpdateCertificateOption.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this UpdateCertificateOption.

        **参数解释**：服务器证书的私钥。  **约束限制**：不涉及  **取值范围**：PEM编码格式，最大长度8192个字符。  **默认取值**：不涉及

        :param private_key: The private_key of this UpdateCertificateOption.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def domain(self):
        r"""Gets the domain of this UpdateCertificateOption.

        **参数解释**：服务器证书所签域名。  **约束限制**：该字段仅type为server时有效（其他类型证书，字段可传入，但不会生效）。  **取值范围**：总长度为0-10000，由若干普通域名或泛域名组成，域名之间以\",\"分隔，不超过100个域名。 - 普通域名：由若干字符串组成，字符串间以\".\"分隔，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。例：www.test.com。 - 泛域名：在普通域名的基础上仅允许首字母为\"\\*\"。例：\\*.test.com。  **默认取值**：不涉及

        :return: The domain of this UpdateCertificateOption.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this UpdateCertificateOption.

        **参数解释**：服务器证书所签域名。  **约束限制**：该字段仅type为server时有效（其他类型证书，字段可传入，但不会生效）。  **取值范围**：总长度为0-10000，由若干普通域名或泛域名组成，域名之间以\",\"分隔，不超过100个域名。 - 普通域名：由若干字符串组成，字符串间以\".\"分隔，单个字符串长度不超过63个字符，只能包含英文字母、数字或\"-\"，且必须以字母或数字开头和结尾。例：www.test.com。 - 泛域名：在普通域名的基础上仅允许首字母为\"\\*\"。例：\\*.test.com。  **默认取值**：不涉及

        :param domain: The domain of this UpdateCertificateOption.
        :type domain: str
        """
        self._domain = domain

    @property
    def enc_certificate(self):
        r"""Gets the enc_certificate of this UpdateCertificateOption.

        **参数解释**：服务器SM双证书的证书内容。 支持最大11层证书链(含证书和证书链)。  **约束限制**：仅当type为server_sm时，才支持传入。  **取值范围**：PEM编码格式。最大长度65536字符。  **默认取值**：不涉及

        :return: The enc_certificate of this UpdateCertificateOption.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        r"""Sets the enc_certificate of this UpdateCertificateOption.

        **参数解释**：服务器SM双证书的证书内容。 支持最大11层证书链(含证书和证书链)。  **约束限制**：仅当type为server_sm时，才支持传入。  **取值范围**：PEM编码格式。最大长度65536字符。  **默认取值**：不涉及

        :param enc_certificate: The enc_certificate of this UpdateCertificateOption.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_private_key(self):
        r"""Gets the enc_private_key of this UpdateCertificateOption.

        **参数解释**：服务器SM双证书的私钥。  **约束限制**：仅当type为server_sm时，才支持传入。  **取值范围**：PEM编码格式，最大长度8192个字符。  **默认取值**：不涉及

        :return: The enc_private_key of this UpdateCertificateOption.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        r"""Sets the enc_private_key of this UpdateCertificateOption.

        **参数解释**：服务器SM双证书的私钥。  **约束限制**：仅当type为server_sm时，才支持传入。  **取值范围**：PEM编码格式，最大长度8192个字符。  **默认取值**：不涉及

        :param enc_private_key: The enc_private_key of this UpdateCertificateOption.
        :type enc_private_key: str
        """
        self._enc_private_key = enc_private_key

    @property
    def scm_certificate_id(self):
        r"""Gets the scm_certificate_id of this UpdateCertificateOption.

        **参数解释**：云证书管理服务（CCM）中的证书ID。  **约束限制**：仅记录证书ID，不验证其是否真实存在云证书管理服务中。并且需要将云证书管理服务中对应证书的内容手动设置到当前接口相应字段中（可能涉及字段certificate、private_key、enc_certificate和enc_private_key）  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The scm_certificate_id of this UpdateCertificateOption.
        :rtype: str
        """
        return self._scm_certificate_id

    @scm_certificate_id.setter
    def scm_certificate_id(self, scm_certificate_id):
        r"""Sets the scm_certificate_id of this UpdateCertificateOption.

        **参数解释**：云证书管理服务（CCM）中的证书ID。  **约束限制**：仅记录证书ID，不验证其是否真实存在云证书管理服务中。并且需要将云证书管理服务中对应证书的内容手动设置到当前接口相应字段中（可能涉及字段certificate、private_key、enc_certificate和enc_private_key）  **取值范围**：不涉及  **默认取值**：不涉及

        :param scm_certificate_id: The scm_certificate_id of this UpdateCertificateOption.
        :type scm_certificate_id: str
        """
        self._scm_certificate_id = scm_certificate_id

    @property
    def source(self):
        r"""Gets the source of this UpdateCertificateOption.

        **参数解释**：标记当前证书来源。  **约束限制**：无  **取值范围**： - scm：表示关联云证书管理服务（CCM）中的证书。 - 空值：表示自有证书。  **默认取值**：不涉及

        :return: The source of this UpdateCertificateOption.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this UpdateCertificateOption.

        **参数解释**：标记当前证书来源。  **约束限制**：无  **取值范围**： - scm：表示关联云证书管理服务（CCM）中的证书。 - 空值：表示自有证书。  **默认取值**：不涉及

        :param source: The source of this UpdateCertificateOption.
        :type source: str
        """
        self._source = source

    @property
    def protection_status(self):
        r"""Gets the protection_status of this UpdateCertificateOption.

        **参数解释**：修改保护状态   **约束限制**：不涉及   **取值范围**：  - nonProtection: 不保护  - consoleProtection: 控制台修改保护   **默认取值**：不涉及

        :return: The protection_status of this UpdateCertificateOption.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this UpdateCertificateOption.

        **参数解释**：修改保护状态   **约束限制**：不涉及   **取值范围**：  - nonProtection: 不保护  - consoleProtection: 控制台修改保护   **默认取值**：不涉及

        :param protection_status: The protection_status of this UpdateCertificateOption.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this UpdateCertificateOption.

        **参数解释**：设置修改保护的原因   **约束限制**：仅当protection_status为consoleProtection时有效   **取值范围**：不涉及   **默认取值**：空

        :return: The protection_reason of this UpdateCertificateOption.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this UpdateCertificateOption.

        **参数解释**：设置修改保护的原因   **约束限制**：仅当protection_status为consoleProtection时有效   **取值范围**：不涉及   **默认取值**：空

        :param protection_reason: The protection_reason of this UpdateCertificateOption.
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
        if not isinstance(other, UpdateCertificateOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
