# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcDomain:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'expire_date': 'str',
        'status': 'str',
        'audit_status': 'str',
        'audit_unpass_reason': 'str',
        'transfer_status': 'str',
        'reg_type': 'str',
        'privacy_protection': 'str',
        'name_server': 'list[str]',
        'credential_type': 'str',
        'credential_id': 'str',
        'registrar': 'str',
        'contact': 'list[HwcDomainContact]'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'expire_date': 'expire_date',
        'status': 'status',
        'audit_status': 'audit_status',
        'audit_unpass_reason': 'audit_unpass_reason',
        'transfer_status': 'transfer_status',
        'reg_type': 'reg_type',
        'privacy_protection': 'privacy_protection',
        'name_server': 'name_server',
        'credential_type': 'credential_type',
        'credential_id': 'credential_id',
        'registrar': 'registrar',
        'contact': 'contact'
    }

    def __init__(self, domain_name=None, expire_date=None, status=None, audit_status=None, audit_unpass_reason=None, transfer_status=None, reg_type=None, privacy_protection=None, name_server=None, credential_type=None, credential_id=None, registrar=None, contact=None):
        r"""HwcDomain

        The model defined in huaweicloud sdk

        :param domain_name: 域名名称
        :type domain_name: str
        :param expire_date: 域名到期时间，eg：2023-01-10
        :type expire_date: str
        :param status: 域名服务状态
        :type status: str
        :param audit_status: 域名实名认证状态。 取值范围： NONAUDIT：未实名认证 SUCCEED：已实名认证 FAILED：实名认证失败 AUDITING：实名认证审核中
        :type audit_status: str
        :param audit_unpass_reason: 域名实名认证失败原因
        :type audit_unpass_reason: str
        :param transfer_status: 过户状态
        :type transfer_status: str
        :param reg_type: 注册类型 取值范围： PERSONAL：个人 COMPANY：企业
        :type reg_type: str
        :param privacy_protection: 是否开启隐私保护
        :type privacy_protection: str
        :param name_server: 域名服务器列表
        :type name_server: list[str]
        :param credential_type: 证件类型
        :type credential_type: str
        :param credential_id: 证件号码
        :type credential_id: str
        :param registrar: 域名所属注册商
        :type registrar: str
        :param contact: 联系人信息
        :type contact: list[:class:`huaweicloudsdksecmaster.v1.HwcDomainContact`]
        """
        
        

        self._domain_name = None
        self._expire_date = None
        self._status = None
        self._audit_status = None
        self._audit_unpass_reason = None
        self._transfer_status = None
        self._reg_type = None
        self._privacy_protection = None
        self._name_server = None
        self._credential_type = None
        self._credential_id = None
        self._registrar = None
        self._contact = None
        self.discriminator = None

        self.domain_name = domain_name
        self.expire_date = expire_date
        self.status = status
        self.audit_status = audit_status
        self.audit_unpass_reason = audit_unpass_reason
        if transfer_status is not None:
            self.transfer_status = transfer_status
        self.reg_type = reg_type
        self.privacy_protection = privacy_protection
        self.name_server = name_server
        self.credential_type = credential_type
        self.credential_id = credential_id
        self.registrar = registrar
        self.contact = contact

    @property
    def domain_name(self):
        r"""Gets the domain_name of this HwcDomain.

        域名名称

        :return: The domain_name of this HwcDomain.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this HwcDomain.

        域名名称

        :param domain_name: The domain_name of this HwcDomain.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def expire_date(self):
        r"""Gets the expire_date of this HwcDomain.

        域名到期时间，eg：2023-01-10

        :return: The expire_date of this HwcDomain.
        :rtype: str
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        r"""Sets the expire_date of this HwcDomain.

        域名到期时间，eg：2023-01-10

        :param expire_date: The expire_date of this HwcDomain.
        :type expire_date: str
        """
        self._expire_date = expire_date

    @property
    def status(self):
        r"""Gets the status of this HwcDomain.

        域名服务状态

        :return: The status of this HwcDomain.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HwcDomain.

        域名服务状态

        :param status: The status of this HwcDomain.
        :type status: str
        """
        self._status = status

    @property
    def audit_status(self):
        r"""Gets the audit_status of this HwcDomain.

        域名实名认证状态。 取值范围： NONAUDIT：未实名认证 SUCCEED：已实名认证 FAILED：实名认证失败 AUDITING：实名认证审核中

        :return: The audit_status of this HwcDomain.
        :rtype: str
        """
        return self._audit_status

    @audit_status.setter
    def audit_status(self, audit_status):
        r"""Sets the audit_status of this HwcDomain.

        域名实名认证状态。 取值范围： NONAUDIT：未实名认证 SUCCEED：已实名认证 FAILED：实名认证失败 AUDITING：实名认证审核中

        :param audit_status: The audit_status of this HwcDomain.
        :type audit_status: str
        """
        self._audit_status = audit_status

    @property
    def audit_unpass_reason(self):
        r"""Gets the audit_unpass_reason of this HwcDomain.

        域名实名认证失败原因

        :return: The audit_unpass_reason of this HwcDomain.
        :rtype: str
        """
        return self._audit_unpass_reason

    @audit_unpass_reason.setter
    def audit_unpass_reason(self, audit_unpass_reason):
        r"""Sets the audit_unpass_reason of this HwcDomain.

        域名实名认证失败原因

        :param audit_unpass_reason: The audit_unpass_reason of this HwcDomain.
        :type audit_unpass_reason: str
        """
        self._audit_unpass_reason = audit_unpass_reason

    @property
    def transfer_status(self):
        r"""Gets the transfer_status of this HwcDomain.

        过户状态

        :return: The transfer_status of this HwcDomain.
        :rtype: str
        """
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, transfer_status):
        r"""Sets the transfer_status of this HwcDomain.

        过户状态

        :param transfer_status: The transfer_status of this HwcDomain.
        :type transfer_status: str
        """
        self._transfer_status = transfer_status

    @property
    def reg_type(self):
        r"""Gets the reg_type of this HwcDomain.

        注册类型 取值范围： PERSONAL：个人 COMPANY：企业

        :return: The reg_type of this HwcDomain.
        :rtype: str
        """
        return self._reg_type

    @reg_type.setter
    def reg_type(self, reg_type):
        r"""Sets the reg_type of this HwcDomain.

        注册类型 取值范围： PERSONAL：个人 COMPANY：企业

        :param reg_type: The reg_type of this HwcDomain.
        :type reg_type: str
        """
        self._reg_type = reg_type

    @property
    def privacy_protection(self):
        r"""Gets the privacy_protection of this HwcDomain.

        是否开启隐私保护

        :return: The privacy_protection of this HwcDomain.
        :rtype: str
        """
        return self._privacy_protection

    @privacy_protection.setter
    def privacy_protection(self, privacy_protection):
        r"""Sets the privacy_protection of this HwcDomain.

        是否开启隐私保护

        :param privacy_protection: The privacy_protection of this HwcDomain.
        :type privacy_protection: str
        """
        self._privacy_protection = privacy_protection

    @property
    def name_server(self):
        r"""Gets the name_server of this HwcDomain.

        域名服务器列表

        :return: The name_server of this HwcDomain.
        :rtype: list[str]
        """
        return self._name_server

    @name_server.setter
    def name_server(self, name_server):
        r"""Sets the name_server of this HwcDomain.

        域名服务器列表

        :param name_server: The name_server of this HwcDomain.
        :type name_server: list[str]
        """
        self._name_server = name_server

    @property
    def credential_type(self):
        r"""Gets the credential_type of this HwcDomain.

        证件类型

        :return: The credential_type of this HwcDomain.
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        r"""Sets the credential_type of this HwcDomain.

        证件类型

        :param credential_type: The credential_type of this HwcDomain.
        :type credential_type: str
        """
        self._credential_type = credential_type

    @property
    def credential_id(self):
        r"""Gets the credential_id of this HwcDomain.

        证件号码

        :return: The credential_id of this HwcDomain.
        :rtype: str
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        r"""Sets the credential_id of this HwcDomain.

        证件号码

        :param credential_id: The credential_id of this HwcDomain.
        :type credential_id: str
        """
        self._credential_id = credential_id

    @property
    def registrar(self):
        r"""Gets the registrar of this HwcDomain.

        域名所属注册商

        :return: The registrar of this HwcDomain.
        :rtype: str
        """
        return self._registrar

    @registrar.setter
    def registrar(self, registrar):
        r"""Sets the registrar of this HwcDomain.

        域名所属注册商

        :param registrar: The registrar of this HwcDomain.
        :type registrar: str
        """
        self._registrar = registrar

    @property
    def contact(self):
        r"""Gets the contact of this HwcDomain.

        联系人信息

        :return: The contact of this HwcDomain.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.HwcDomainContact`]
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        r"""Sets the contact of this HwcDomain.

        联系人信息

        :param contact: The contact of this HwcDomain.
        :type contact: list[:class:`huaweicloudsdksecmaster.v1.HwcDomainContact`]
        """
        self._contact = contact

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HwcDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
