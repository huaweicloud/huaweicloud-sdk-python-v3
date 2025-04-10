# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PurchaseCertificateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_brand': 'str',
        'cert_type': 'str',
        'domain_type': 'str',
        'effective_time': 'int',
        'domain_numbers': 'int',
        'order_number': 'int',
        'agree_privacy_protection': 'bool',
        'primary_domain_type': 'str',
        'single_domain_number': 'int',
        'wildcard_domain_number': 'int',
        'is_auto_pay': 'bool',
        'enterprise_project_id': 'str',
        'order_id': 'str',
        'tags': 'list[ScsResourceTag]'
    }

    attribute_map = {
        'cert_brand': 'cert_brand',
        'cert_type': 'cert_type',
        'domain_type': 'domain_type',
        'effective_time': 'effective_time',
        'domain_numbers': 'domain_numbers',
        'order_number': 'order_number',
        'agree_privacy_protection': 'agree_privacy_protection',
        'primary_domain_type': 'primary_domain_type',
        'single_domain_number': 'single_domain_number',
        'wildcard_domain_number': 'wildcard_domain_number',
        'is_auto_pay': 'is_auto_pay',
        'enterprise_project_id': 'enterprise_project_id',
        'order_id': 'order_id',
        'tags': 'tags'
    }

    def __init__(self, cert_brand=None, cert_type=None, domain_type=None, effective_time=None, domain_numbers=None, order_number=None, agree_privacy_protection=None, primary_domain_type=None, single_domain_number=None, wildcard_domain_number=None, is_auto_pay=None, enterprise_project_id=None, order_id=None, tags=None):
        r"""PurchaseCertificateRequestBody

        The model defined in huaweicloud sdk

        :param cert_brand: 证书品牌，取值如下： - GEOTRUST - GLOBALSIGN - SYMANTEC - CFCA - TRUSTASIA - VTRUS
        :type cert_brand: str
        :param cert_type: 证书类型，取值如下： - DV_SSL_CERT - DV_SSL_CERT_BASIC - EV_SSL_CERT - EV_SSL_CERT_PRO - OV_SSL_CERT - OV_SSL_CERT_PRO
        :type cert_type: str
        :param domain_type: 域名类型，取值如下： - SINGLE_DOMAIN：单域名类型。 - MULTI_DOMAIN：多域名类型。 - WILDCARD：泛域名类型。
        :type domain_type: str
        :param effective_time: 证书有效期（年）。
        :type effective_time: int
        :param domain_numbers: 域名数量。 - 当“domain_type”选择的是“SINGLE_DOMAIN”或“WILDCARD”类型的证书时，域名数量取值为“1”。 - 当“domain_type”选择的是“MULTI_DOMAIN”类型的证书时，域名数量取值范围为“2~100”。
        :type domain_numbers: int
        :param order_number: 购买的证书数量。取值范围为1~100。
        :type order_number: int
        :param agree_privacy_protection: 是否同意隐私协议，此处仅能设置为true才能成功购买证书。 - true：同意隐私协议。 - false：不同意隐私协议。
        :type agree_privacy_protection: bool
        :param primary_domain_type: 多域名中的主域名类型。 - SINGLE_DOMAIN：主单域名 - WILDCARD_DOMAIN：主泛域名
        :type primary_domain_type: str
        :param single_domain_number: 附加单域名数量。
        :type single_domain_number: int
        :param wildcard_domain_number: 附加泛域名数量。
        :type wildcard_domain_number: int
        :param is_auto_pay: 是否开启自动支付。 - true：开启自动支付。 - false：不开启自动支付。
        :type is_auto_pay: bool
        :param enterprise_project_id: 企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件。 - 取值为“all” - 取值为“0” - 满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”
        :type enterprise_project_id: str
        :param order_id: 订单号。仅组合购买场景使用。
        :type order_id: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkscm.v3.ScsResourceTag`]
        """
        
        

        self._cert_brand = None
        self._cert_type = None
        self._domain_type = None
        self._effective_time = None
        self._domain_numbers = None
        self._order_number = None
        self._agree_privacy_protection = None
        self._primary_domain_type = None
        self._single_domain_number = None
        self._wildcard_domain_number = None
        self._is_auto_pay = None
        self._enterprise_project_id = None
        self._order_id = None
        self._tags = None
        self.discriminator = None

        self.cert_brand = cert_brand
        self.cert_type = cert_type
        self.domain_type = domain_type
        self.effective_time = effective_time
        self.domain_numbers = domain_numbers
        self.order_number = order_number
        self.agree_privacy_protection = agree_privacy_protection
        if primary_domain_type is not None:
            self.primary_domain_type = primary_domain_type
        if single_domain_number is not None:
            self.single_domain_number = single_domain_number
        if wildcard_domain_number is not None:
            self.wildcard_domain_number = wildcard_domain_number
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if order_id is not None:
            self.order_id = order_id
        if tags is not None:
            self.tags = tags

    @property
    def cert_brand(self):
        r"""Gets the cert_brand of this PurchaseCertificateRequestBody.

        证书品牌，取值如下： - GEOTRUST - GLOBALSIGN - SYMANTEC - CFCA - TRUSTASIA - VTRUS

        :return: The cert_brand of this PurchaseCertificateRequestBody.
        :rtype: str
        """
        return self._cert_brand

    @cert_brand.setter
    def cert_brand(self, cert_brand):
        r"""Sets the cert_brand of this PurchaseCertificateRequestBody.

        证书品牌，取值如下： - GEOTRUST - GLOBALSIGN - SYMANTEC - CFCA - TRUSTASIA - VTRUS

        :param cert_brand: The cert_brand of this PurchaseCertificateRequestBody.
        :type cert_brand: str
        """
        self._cert_brand = cert_brand

    @property
    def cert_type(self):
        r"""Gets the cert_type of this PurchaseCertificateRequestBody.

        证书类型，取值如下： - DV_SSL_CERT - DV_SSL_CERT_BASIC - EV_SSL_CERT - EV_SSL_CERT_PRO - OV_SSL_CERT - OV_SSL_CERT_PRO

        :return: The cert_type of this PurchaseCertificateRequestBody.
        :rtype: str
        """
        return self._cert_type

    @cert_type.setter
    def cert_type(self, cert_type):
        r"""Sets the cert_type of this PurchaseCertificateRequestBody.

        证书类型，取值如下： - DV_SSL_CERT - DV_SSL_CERT_BASIC - EV_SSL_CERT - EV_SSL_CERT_PRO - OV_SSL_CERT - OV_SSL_CERT_PRO

        :param cert_type: The cert_type of this PurchaseCertificateRequestBody.
        :type cert_type: str
        """
        self._cert_type = cert_type

    @property
    def domain_type(self):
        r"""Gets the domain_type of this PurchaseCertificateRequestBody.

        域名类型，取值如下： - SINGLE_DOMAIN：单域名类型。 - MULTI_DOMAIN：多域名类型。 - WILDCARD：泛域名类型。

        :return: The domain_type of this PurchaseCertificateRequestBody.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this PurchaseCertificateRequestBody.

        域名类型，取值如下： - SINGLE_DOMAIN：单域名类型。 - MULTI_DOMAIN：多域名类型。 - WILDCARD：泛域名类型。

        :param domain_type: The domain_type of this PurchaseCertificateRequestBody.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def effective_time(self):
        r"""Gets the effective_time of this PurchaseCertificateRequestBody.

        证书有效期（年）。

        :return: The effective_time of this PurchaseCertificateRequestBody.
        :rtype: int
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this PurchaseCertificateRequestBody.

        证书有效期（年）。

        :param effective_time: The effective_time of this PurchaseCertificateRequestBody.
        :type effective_time: int
        """
        self._effective_time = effective_time

    @property
    def domain_numbers(self):
        r"""Gets the domain_numbers of this PurchaseCertificateRequestBody.

        域名数量。 - 当“domain_type”选择的是“SINGLE_DOMAIN”或“WILDCARD”类型的证书时，域名数量取值为“1”。 - 当“domain_type”选择的是“MULTI_DOMAIN”类型的证书时，域名数量取值范围为“2~100”。

        :return: The domain_numbers of this PurchaseCertificateRequestBody.
        :rtype: int
        """
        return self._domain_numbers

    @domain_numbers.setter
    def domain_numbers(self, domain_numbers):
        r"""Sets the domain_numbers of this PurchaseCertificateRequestBody.

        域名数量。 - 当“domain_type”选择的是“SINGLE_DOMAIN”或“WILDCARD”类型的证书时，域名数量取值为“1”。 - 当“domain_type”选择的是“MULTI_DOMAIN”类型的证书时，域名数量取值范围为“2~100”。

        :param domain_numbers: The domain_numbers of this PurchaseCertificateRequestBody.
        :type domain_numbers: int
        """
        self._domain_numbers = domain_numbers

    @property
    def order_number(self):
        r"""Gets the order_number of this PurchaseCertificateRequestBody.

        购买的证书数量。取值范围为1~100。

        :return: The order_number of this PurchaseCertificateRequestBody.
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        r"""Sets the order_number of this PurchaseCertificateRequestBody.

        购买的证书数量。取值范围为1~100。

        :param order_number: The order_number of this PurchaseCertificateRequestBody.
        :type order_number: int
        """
        self._order_number = order_number

    @property
    def agree_privacy_protection(self):
        r"""Gets the agree_privacy_protection of this PurchaseCertificateRequestBody.

        是否同意隐私协议，此处仅能设置为true才能成功购买证书。 - true：同意隐私协议。 - false：不同意隐私协议。

        :return: The agree_privacy_protection of this PurchaseCertificateRequestBody.
        :rtype: bool
        """
        return self._agree_privacy_protection

    @agree_privacy_protection.setter
    def agree_privacy_protection(self, agree_privacy_protection):
        r"""Sets the agree_privacy_protection of this PurchaseCertificateRequestBody.

        是否同意隐私协议，此处仅能设置为true才能成功购买证书。 - true：同意隐私协议。 - false：不同意隐私协议。

        :param agree_privacy_protection: The agree_privacy_protection of this PurchaseCertificateRequestBody.
        :type agree_privacy_protection: bool
        """
        self._agree_privacy_protection = agree_privacy_protection

    @property
    def primary_domain_type(self):
        r"""Gets the primary_domain_type of this PurchaseCertificateRequestBody.

        多域名中的主域名类型。 - SINGLE_DOMAIN：主单域名 - WILDCARD_DOMAIN：主泛域名

        :return: The primary_domain_type of this PurchaseCertificateRequestBody.
        :rtype: str
        """
        return self._primary_domain_type

    @primary_domain_type.setter
    def primary_domain_type(self, primary_domain_type):
        r"""Sets the primary_domain_type of this PurchaseCertificateRequestBody.

        多域名中的主域名类型。 - SINGLE_DOMAIN：主单域名 - WILDCARD_DOMAIN：主泛域名

        :param primary_domain_type: The primary_domain_type of this PurchaseCertificateRequestBody.
        :type primary_domain_type: str
        """
        self._primary_domain_type = primary_domain_type

    @property
    def single_domain_number(self):
        r"""Gets the single_domain_number of this PurchaseCertificateRequestBody.

        附加单域名数量。

        :return: The single_domain_number of this PurchaseCertificateRequestBody.
        :rtype: int
        """
        return self._single_domain_number

    @single_domain_number.setter
    def single_domain_number(self, single_domain_number):
        r"""Sets the single_domain_number of this PurchaseCertificateRequestBody.

        附加单域名数量。

        :param single_domain_number: The single_domain_number of this PurchaseCertificateRequestBody.
        :type single_domain_number: int
        """
        self._single_domain_number = single_domain_number

    @property
    def wildcard_domain_number(self):
        r"""Gets the wildcard_domain_number of this PurchaseCertificateRequestBody.

        附加泛域名数量。

        :return: The wildcard_domain_number of this PurchaseCertificateRequestBody.
        :rtype: int
        """
        return self._wildcard_domain_number

    @wildcard_domain_number.setter
    def wildcard_domain_number(self, wildcard_domain_number):
        r"""Sets the wildcard_domain_number of this PurchaseCertificateRequestBody.

        附加泛域名数量。

        :param wildcard_domain_number: The wildcard_domain_number of this PurchaseCertificateRequestBody.
        :type wildcard_domain_number: int
        """
        self._wildcard_domain_number = wildcard_domain_number

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this PurchaseCertificateRequestBody.

        是否开启自动支付。 - true：开启自动支付。 - false：不开启自动支付。

        :return: The is_auto_pay of this PurchaseCertificateRequestBody.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this PurchaseCertificateRequestBody.

        是否开启自动支付。 - true：开启自动支付。 - false：不开启自动支付。

        :param is_auto_pay: The is_auto_pay of this PurchaseCertificateRequestBody.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this PurchaseCertificateRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件。 - 取值为“all” - 取值为“0” - 满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :return: The enterprise_project_id of this PurchaseCertificateRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this PurchaseCertificateRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件。 - 取值为“all” - 取值为“0” - 满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :param enterprise_project_id: The enterprise_project_id of this PurchaseCertificateRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def order_id(self):
        r"""Gets the order_id of this PurchaseCertificateRequestBody.

        订单号。仅组合购买场景使用。

        :return: The order_id of this PurchaseCertificateRequestBody.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this PurchaseCertificateRequestBody.

        订单号。仅组合购买场景使用。

        :param order_id: The order_id of this PurchaseCertificateRequestBody.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def tags(self):
        r"""Gets the tags of this PurchaseCertificateRequestBody.

        标签列表。

        :return: The tags of this PurchaseCertificateRequestBody.
        :rtype: list[:class:`huaweicloudsdkscm.v3.ScsResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this PurchaseCertificateRequestBody.

        标签列表。

        :param tags: The tags of this PurchaseCertificateRequestBody.
        :type tags: list[:class:`huaweicloudsdkscm.v3.ScsResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, PurchaseCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
