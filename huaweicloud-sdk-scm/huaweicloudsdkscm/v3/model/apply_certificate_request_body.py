# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyCertificateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'sans': 'str',
        'csr': 'str',
        'company_name': 'str',
        'company_unit': 'str',
        'company_province': 'str',
        'company_city': 'str',
        'country': 'str',
        'applicant_name': 'str',
        'applicant_phone': 'str',
        'applicant_email': 'str',
        'contact_name': 'str',
        'contact_phone': 'str',
        'contact_email': 'str',
        'auto_dns_auth': 'bool',
        'agree_privacy_protection': 'bool',
        'domain_method': 'str',
        'key_algorithm': 'str',
        'ca_hash_algorithm': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'sans': 'sans',
        'csr': 'csr',
        'company_name': 'company_name',
        'company_unit': 'company_unit',
        'company_province': 'company_province',
        'company_city': 'company_city',
        'country': 'country',
        'applicant_name': 'applicant_name',
        'applicant_phone': 'applicant_phone',
        'applicant_email': 'applicant_email',
        'contact_name': 'contact_name',
        'contact_phone': 'contact_phone',
        'contact_email': 'contact_email',
        'auto_dns_auth': 'auto_dns_auth',
        'agree_privacy_protection': 'agree_privacy_protection',
        'domain_method': 'domain_method',
        'key_algorithm': 'key_algorithm',
        'ca_hash_algorithm': 'ca_hash_algorithm'
    }

    def __init__(self, domain=None, sans=None, csr=None, company_name=None, company_unit=None, company_province=None, company_city=None, country=None, applicant_name=None, applicant_phone=None, applicant_email=None, contact_name=None, contact_phone=None, contact_email=None, auto_dns_auth=None, agree_privacy_protection=None, domain_method=None, key_algorithm=None, ca_hash_algorithm=None):
        r"""ApplyCertificateRequestBody

        The model defined in huaweicloud sdk

        :param domain: 该证书绑定的域名。 - 当购买的证书为“单域名”或“泛域名”类型的证书时，请直接填写单域名或泛域名即可。 - 当购买的证书为“多域名”类型的证书时，需要选择1个域名作为主域名。 示例：www.example.com
        :type domain: str
        :param sans: 绑定多域名类型证书的附加域名。 当购买的证书为“多域名”类型的证书，且有可增加附加域名的额度时，才需要设置该值。 多个域名需要以“;”隔开。 示例：www.example.com;www.example1.com;www.example2.com
        :type sans: str
        :param csr: 证书CSR串，与域名必须匹配。
        :type csr: str
        :param company_name: 公司名称，OV和EV型证书必填。字符长度为0~63位。
        :type company_name: str
        :param company_unit: 部门名称。字符长度为0~63位。
        :type company_unit: str
        :param company_province: 公司所在省份，OV和EV型证书必填。字符长度为0~63位。
        :type company_province: str
        :param company_city: 公司所在市区，OV和EV型证书必填。字符长度为0~63位。
        :type company_city: str
        :param country: OV和EV型证书必填,国家编码，需符合正则\&quot;**[A-Za-z]{2}**\&quot;。
        :type country: str
        :param applicant_name: 申请人的姓名。请输入中文、英文字符，下划线，中划线，英文逗号，英文句点，且长度为4到100字节。
        :type applicant_name: str
        :param applicant_phone: 申请人的电话号码。示例：13212345678
        :type applicant_phone: str
        :param applicant_email: 申请人的邮箱。示例：example@huawei.com
        :type applicant_email: str
        :param contact_name: 技术联系人的姓名。字符长度为0~63位。
        :type contact_name: str
        :param contact_phone: 技术联系人的电话号码。示例：13212345678
        :type contact_phone: str
        :param contact_email: 技术联系人的邮箱。示例：example@huawei.com
        :type contact_email: str
        :param auto_dns_auth: 是否将DNS验证信息推送到华为云解析服务。 - true：推送。 - false：不推送。
        :type auto_dns_auth: bool
        :param agree_privacy_protection: 是否同意授权隐私协议。此处仅能设置为true才能成功申请证书。 - true：同意隐私协议。 - false：不同意隐私协议。
        :type agree_privacy_protection: bool
        :param domain_method: 域名验证方式。 - DNS：DNS验证，指在域名管理平台通过解析指定的DNS记录，验证域名所有权。 - FILE：文件验证，指通过在服务器上创建指定文件的方式来验证域名所有权。 - EMAIL：邮箱验证，指登录域名管理员邮箱，接收域名确认邮件并根据提示进行操作来验证域名所有权。 DV域名型和DV基础版证书（GeoTrust入门级SSL证书和DigiCert免费SSL证书）默认通过“DNS验证”方式进行验证。 纯IP（公网IP）的证书仅支持通过“文件验证”方式进行验证，且仅纯IP证书支持“文件验证”方式验证。
        :type domain_method: str
        :param key_algorithm: 密钥算法。默认RSA_2048
        :type key_algorithm: str
        :param ca_hash_algorithm: 签名算法。Geo OV证书必填。 - DEFAULT - SHA-256
        :type ca_hash_algorithm: str
        """
        
        

        self._domain = None
        self._sans = None
        self._csr = None
        self._company_name = None
        self._company_unit = None
        self._company_province = None
        self._company_city = None
        self._country = None
        self._applicant_name = None
        self._applicant_phone = None
        self._applicant_email = None
        self._contact_name = None
        self._contact_phone = None
        self._contact_email = None
        self._auto_dns_auth = None
        self._agree_privacy_protection = None
        self._domain_method = None
        self._key_algorithm = None
        self._ca_hash_algorithm = None
        self.discriminator = None

        self.domain = domain
        if sans is not None:
            self.sans = sans
        if csr is not None:
            self.csr = csr
        if company_name is not None:
            self.company_name = company_name
        if company_unit is not None:
            self.company_unit = company_unit
        if company_province is not None:
            self.company_province = company_province
        if company_city is not None:
            self.company_city = company_city
        if country is not None:
            self.country = country
        self.applicant_name = applicant_name
        self.applicant_phone = applicant_phone
        self.applicant_email = applicant_email
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_phone is not None:
            self.contact_phone = contact_phone
        if contact_email is not None:
            self.contact_email = contact_email
        if auto_dns_auth is not None:
            self.auto_dns_auth = auto_dns_auth
        self.agree_privacy_protection = agree_privacy_protection
        self.domain_method = domain_method
        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        if ca_hash_algorithm is not None:
            self.ca_hash_algorithm = ca_hash_algorithm

    @property
    def domain(self):
        r"""Gets the domain of this ApplyCertificateRequestBody.

        该证书绑定的域名。 - 当购买的证书为“单域名”或“泛域名”类型的证书时，请直接填写单域名或泛域名即可。 - 当购买的证书为“多域名”类型的证书时，需要选择1个域名作为主域名。 示例：www.example.com

        :return: The domain of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ApplyCertificateRequestBody.

        该证书绑定的域名。 - 当购买的证书为“单域名”或“泛域名”类型的证书时，请直接填写单域名或泛域名即可。 - 当购买的证书为“多域名”类型的证书时，需要选择1个域名作为主域名。 示例：www.example.com

        :param domain: The domain of this ApplyCertificateRequestBody.
        :type domain: str
        """
        self._domain = domain

    @property
    def sans(self):
        r"""Gets the sans of this ApplyCertificateRequestBody.

        绑定多域名类型证书的附加域名。 当购买的证书为“多域名”类型的证书，且有可增加附加域名的额度时，才需要设置该值。 多个域名需要以“;”隔开。 示例：www.example.com;www.example1.com;www.example2.com

        :return: The sans of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._sans

    @sans.setter
    def sans(self, sans):
        r"""Sets the sans of this ApplyCertificateRequestBody.

        绑定多域名类型证书的附加域名。 当购买的证书为“多域名”类型的证书，且有可增加附加域名的额度时，才需要设置该值。 多个域名需要以“;”隔开。 示例：www.example.com;www.example1.com;www.example2.com

        :param sans: The sans of this ApplyCertificateRequestBody.
        :type sans: str
        """
        self._sans = sans

    @property
    def csr(self):
        r"""Gets the csr of this ApplyCertificateRequestBody.

        证书CSR串，与域名必须匹配。

        :return: The csr of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._csr

    @csr.setter
    def csr(self, csr):
        r"""Sets the csr of this ApplyCertificateRequestBody.

        证书CSR串，与域名必须匹配。

        :param csr: The csr of this ApplyCertificateRequestBody.
        :type csr: str
        """
        self._csr = csr

    @property
    def company_name(self):
        r"""Gets the company_name of this ApplyCertificateRequestBody.

        公司名称，OV和EV型证书必填。字符长度为0~63位。

        :return: The company_name of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        r"""Sets the company_name of this ApplyCertificateRequestBody.

        公司名称，OV和EV型证书必填。字符长度为0~63位。

        :param company_name: The company_name of this ApplyCertificateRequestBody.
        :type company_name: str
        """
        self._company_name = company_name

    @property
    def company_unit(self):
        r"""Gets the company_unit of this ApplyCertificateRequestBody.

        部门名称。字符长度为0~63位。

        :return: The company_unit of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._company_unit

    @company_unit.setter
    def company_unit(self, company_unit):
        r"""Sets the company_unit of this ApplyCertificateRequestBody.

        部门名称。字符长度为0~63位。

        :param company_unit: The company_unit of this ApplyCertificateRequestBody.
        :type company_unit: str
        """
        self._company_unit = company_unit

    @property
    def company_province(self):
        r"""Gets the company_province of this ApplyCertificateRequestBody.

        公司所在省份，OV和EV型证书必填。字符长度为0~63位。

        :return: The company_province of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._company_province

    @company_province.setter
    def company_province(self, company_province):
        r"""Sets the company_province of this ApplyCertificateRequestBody.

        公司所在省份，OV和EV型证书必填。字符长度为0~63位。

        :param company_province: The company_province of this ApplyCertificateRequestBody.
        :type company_province: str
        """
        self._company_province = company_province

    @property
    def company_city(self):
        r"""Gets the company_city of this ApplyCertificateRequestBody.

        公司所在市区，OV和EV型证书必填。字符长度为0~63位。

        :return: The company_city of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._company_city

    @company_city.setter
    def company_city(self, company_city):
        r"""Sets the company_city of this ApplyCertificateRequestBody.

        公司所在市区，OV和EV型证书必填。字符长度为0~63位。

        :param company_city: The company_city of this ApplyCertificateRequestBody.
        :type company_city: str
        """
        self._company_city = company_city

    @property
    def country(self):
        r"""Gets the country of this ApplyCertificateRequestBody.

        OV和EV型证书必填,国家编码，需符合正则\"**[A-Za-z]{2}**\"。

        :return: The country of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this ApplyCertificateRequestBody.

        OV和EV型证书必填,国家编码，需符合正则\"**[A-Za-z]{2}**\"。

        :param country: The country of this ApplyCertificateRequestBody.
        :type country: str
        """
        self._country = country

    @property
    def applicant_name(self):
        r"""Gets the applicant_name of this ApplyCertificateRequestBody.

        申请人的姓名。请输入中文、英文字符，下划线，中划线，英文逗号，英文句点，且长度为4到100字节。

        :return: The applicant_name of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._applicant_name

    @applicant_name.setter
    def applicant_name(self, applicant_name):
        r"""Sets the applicant_name of this ApplyCertificateRequestBody.

        申请人的姓名。请输入中文、英文字符，下划线，中划线，英文逗号，英文句点，且长度为4到100字节。

        :param applicant_name: The applicant_name of this ApplyCertificateRequestBody.
        :type applicant_name: str
        """
        self._applicant_name = applicant_name

    @property
    def applicant_phone(self):
        r"""Gets the applicant_phone of this ApplyCertificateRequestBody.

        申请人的电话号码。示例：13212345678

        :return: The applicant_phone of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._applicant_phone

    @applicant_phone.setter
    def applicant_phone(self, applicant_phone):
        r"""Sets the applicant_phone of this ApplyCertificateRequestBody.

        申请人的电话号码。示例：13212345678

        :param applicant_phone: The applicant_phone of this ApplyCertificateRequestBody.
        :type applicant_phone: str
        """
        self._applicant_phone = applicant_phone

    @property
    def applicant_email(self):
        r"""Gets the applicant_email of this ApplyCertificateRequestBody.

        申请人的邮箱。示例：example@huawei.com

        :return: The applicant_email of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._applicant_email

    @applicant_email.setter
    def applicant_email(self, applicant_email):
        r"""Sets the applicant_email of this ApplyCertificateRequestBody.

        申请人的邮箱。示例：example@huawei.com

        :param applicant_email: The applicant_email of this ApplyCertificateRequestBody.
        :type applicant_email: str
        """
        self._applicant_email = applicant_email

    @property
    def contact_name(self):
        r"""Gets the contact_name of this ApplyCertificateRequestBody.

        技术联系人的姓名。字符长度为0~63位。

        :return: The contact_name of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        r"""Sets the contact_name of this ApplyCertificateRequestBody.

        技术联系人的姓名。字符长度为0~63位。

        :param contact_name: The contact_name of this ApplyCertificateRequestBody.
        :type contact_name: str
        """
        self._contact_name = contact_name

    @property
    def contact_phone(self):
        r"""Gets the contact_phone of this ApplyCertificateRequestBody.

        技术联系人的电话号码。示例：13212345678

        :return: The contact_phone of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        r"""Sets the contact_phone of this ApplyCertificateRequestBody.

        技术联系人的电话号码。示例：13212345678

        :param contact_phone: The contact_phone of this ApplyCertificateRequestBody.
        :type contact_phone: str
        """
        self._contact_phone = contact_phone

    @property
    def contact_email(self):
        r"""Gets the contact_email of this ApplyCertificateRequestBody.

        技术联系人的邮箱。示例：example@huawei.com

        :return: The contact_email of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        r"""Sets the contact_email of this ApplyCertificateRequestBody.

        技术联系人的邮箱。示例：example@huawei.com

        :param contact_email: The contact_email of this ApplyCertificateRequestBody.
        :type contact_email: str
        """
        self._contact_email = contact_email

    @property
    def auto_dns_auth(self):
        r"""Gets the auto_dns_auth of this ApplyCertificateRequestBody.

        是否将DNS验证信息推送到华为云解析服务。 - true：推送。 - false：不推送。

        :return: The auto_dns_auth of this ApplyCertificateRequestBody.
        :rtype: bool
        """
        return self._auto_dns_auth

    @auto_dns_auth.setter
    def auto_dns_auth(self, auto_dns_auth):
        r"""Sets the auto_dns_auth of this ApplyCertificateRequestBody.

        是否将DNS验证信息推送到华为云解析服务。 - true：推送。 - false：不推送。

        :param auto_dns_auth: The auto_dns_auth of this ApplyCertificateRequestBody.
        :type auto_dns_auth: bool
        """
        self._auto_dns_auth = auto_dns_auth

    @property
    def agree_privacy_protection(self):
        r"""Gets the agree_privacy_protection of this ApplyCertificateRequestBody.

        是否同意授权隐私协议。此处仅能设置为true才能成功申请证书。 - true：同意隐私协议。 - false：不同意隐私协议。

        :return: The agree_privacy_protection of this ApplyCertificateRequestBody.
        :rtype: bool
        """
        return self._agree_privacy_protection

    @agree_privacy_protection.setter
    def agree_privacy_protection(self, agree_privacy_protection):
        r"""Sets the agree_privacy_protection of this ApplyCertificateRequestBody.

        是否同意授权隐私协议。此处仅能设置为true才能成功申请证书。 - true：同意隐私协议。 - false：不同意隐私协议。

        :param agree_privacy_protection: The agree_privacy_protection of this ApplyCertificateRequestBody.
        :type agree_privacy_protection: bool
        """
        self._agree_privacy_protection = agree_privacy_protection

    @property
    def domain_method(self):
        r"""Gets the domain_method of this ApplyCertificateRequestBody.

        域名验证方式。 - DNS：DNS验证，指在域名管理平台通过解析指定的DNS记录，验证域名所有权。 - FILE：文件验证，指通过在服务器上创建指定文件的方式来验证域名所有权。 - EMAIL：邮箱验证，指登录域名管理员邮箱，接收域名确认邮件并根据提示进行操作来验证域名所有权。 DV域名型和DV基础版证书（GeoTrust入门级SSL证书和DigiCert免费SSL证书）默认通过“DNS验证”方式进行验证。 纯IP（公网IP）的证书仅支持通过“文件验证”方式进行验证，且仅纯IP证书支持“文件验证”方式验证。

        :return: The domain_method of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._domain_method

    @domain_method.setter
    def domain_method(self, domain_method):
        r"""Sets the domain_method of this ApplyCertificateRequestBody.

        域名验证方式。 - DNS：DNS验证，指在域名管理平台通过解析指定的DNS记录，验证域名所有权。 - FILE：文件验证，指通过在服务器上创建指定文件的方式来验证域名所有权。 - EMAIL：邮箱验证，指登录域名管理员邮箱，接收域名确认邮件并根据提示进行操作来验证域名所有权。 DV域名型和DV基础版证书（GeoTrust入门级SSL证书和DigiCert免费SSL证书）默认通过“DNS验证”方式进行验证。 纯IP（公网IP）的证书仅支持通过“文件验证”方式进行验证，且仅纯IP证书支持“文件验证”方式验证。

        :param domain_method: The domain_method of this ApplyCertificateRequestBody.
        :type domain_method: str
        """
        self._domain_method = domain_method

    @property
    def key_algorithm(self):
        r"""Gets the key_algorithm of this ApplyCertificateRequestBody.

        密钥算法。默认RSA_2048

        :return: The key_algorithm of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        r"""Sets the key_algorithm of this ApplyCertificateRequestBody.

        密钥算法。默认RSA_2048

        :param key_algorithm: The key_algorithm of this ApplyCertificateRequestBody.
        :type key_algorithm: str
        """
        self._key_algorithm = key_algorithm

    @property
    def ca_hash_algorithm(self):
        r"""Gets the ca_hash_algorithm of this ApplyCertificateRequestBody.

        签名算法。Geo OV证书必填。 - DEFAULT - SHA-256

        :return: The ca_hash_algorithm of this ApplyCertificateRequestBody.
        :rtype: str
        """
        return self._ca_hash_algorithm

    @ca_hash_algorithm.setter
    def ca_hash_algorithm(self, ca_hash_algorithm):
        r"""Sets the ca_hash_algorithm of this ApplyCertificateRequestBody.

        签名算法。Geo OV证书必填。 - DEFAULT - SHA-256

        :param ca_hash_algorithm: The ca_hash_algorithm of this ApplyCertificateRequestBody.
        :type ca_hash_algorithm: str
        """
        self._ca_hash_algorithm = ca_hash_algorithm

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
        if not isinstance(other, ApplyCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
