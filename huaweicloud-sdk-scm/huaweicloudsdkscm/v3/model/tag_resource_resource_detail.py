# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagResourceResourceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_id': 'str',
        'cert_name': 'str',
        'domain': 'str',
        'cert_type': 'str',
        'cert_brand': 'str',
        'domain_type': 'str',
        'purchase_period': 'int',
        'expired_time': 'str',
        'order_status': 'str',
        'domain_num': 'int',
        'wildcard_number': 'int',
        'sans': 'str',
        'cert_des': 'str',
        'signature_algorithm': 'str',
        'fail_reason': 'str',
        'partner_order_id': 'str',
        'push_support': 'bool',
        'cert_issued_time': 'str',
        'resource_id': 'str',
        'unsubscribe_support': 'bool',
        'enterprise_project_id': 'str',
        'origin_cert_id': 'str',
        'renewal_cert_id': 'str',
        'auto_renew_status': 'int',
        'remain_cert_number': 'int',
        'auto_deploy_support': 'bool'
    }

    attribute_map = {
        'cert_id': 'cert_id',
        'cert_name': 'cert_name',
        'domain': 'domain',
        'cert_type': 'cert_type',
        'cert_brand': 'cert_brand',
        'domain_type': 'domain_type',
        'purchase_period': 'purchase_period',
        'expired_time': 'expired_time',
        'order_status': 'order_status',
        'domain_num': 'domain_num',
        'wildcard_number': 'wildcard_number',
        'sans': 'sans',
        'cert_des': 'cert_des',
        'signature_algorithm': 'signature_algorithm',
        'fail_reason': 'fail_reason',
        'partner_order_id': 'partner_order_id',
        'push_support': 'push_support',
        'cert_issued_time': 'cert_issued_time',
        'resource_id': 'resource_id',
        'unsubscribe_support': 'unsubscribe_support',
        'enterprise_project_id': 'enterprise_project_id',
        'origin_cert_id': 'origin_cert_id',
        'renewal_cert_id': 'renewal_cert_id',
        'auto_renew_status': 'auto_renew_status',
        'remain_cert_number': 'remain_cert_number',
        'auto_deploy_support': 'auto_deploy_support'
    }

    def __init__(self, cert_id=None, cert_name=None, domain=None, cert_type=None, cert_brand=None, domain_type=None, purchase_period=None, expired_time=None, order_status=None, domain_num=None, wildcard_number=None, sans=None, cert_des=None, signature_algorithm=None, fail_reason=None, partner_order_id=None, push_support=None, cert_issued_time=None, resource_id=None, unsubscribe_support=None, enterprise_project_id=None, origin_cert_id=None, renewal_cert_id=None, auto_renew_status=None, remain_cert_number=None, auto_deploy_support=None):
        r"""TagResourceResourceDetail

        The model defined in huaweicloud sdk

        :param cert_id: 证书ID。
        :type cert_id: str
        :param cert_name: 证书名称。字符长度为3~63位。
        :type cert_name: str
        :param domain: 该证书绑定的域名。 - 当购买的证书为“单域名”或“泛域名”类型的证书时，请直接填写单域名或泛域名即可。 - 当购买的证书为“多域名”类型的证书时，需要选择1个域名作为主域名。 示例：www.example.com
        :type domain: str
        :param cert_type: 证书类型。 - OV_SSL_CERT：企业型SSL证书。 - EV_SSL_CERT：增强型SSL证书。
        :type cert_type: str
        :param cert_brand: 证书品牌。GLOBALSIGN：GlobalSign品牌。
        :type cert_brand: str
        :param domain_type: 域名类型。 - SINGLE_DOMAIN：单域名类型。 - MULTI_DOMAIN：多域名类型。 - WILDCARD：泛域名类型。
        :type domain_type: str
        :param purchase_period: 证书有效期（年）。
        :type purchase_period: int
        :param expired_time: 证书到期时间，毫秒级时间戳。
        :type expired_time: str
        :param order_status: 订单状态。
        :type order_status: str
        :param domain_num: 域名数量。 - 当“domain_type”选择的是“SINGLE_DOMAIN”或“WILDCARD”类型的证书时，域名数量取值为“1”。 - 当“domain_type”选择的是“MULTI_DOMAIN”类型的证书时，域名数量取值范围为“2~250”。
        :type domain_num: int
        :param wildcard_number: 泛域名数量。
        :type wildcard_number: int
        :param sans: 证书绑定的附加域名信息。
        :type sans: str
        :param cert_des: 证书描述。
        :type cert_des: str
        :param signature_algorithm: 签名算法。
        :type signature_algorithm: str
        :param fail_reason: 失败原因。
        :type fail_reason: str
        :param partner_order_id: 订单流水号。
        :type partner_order_id: str
        :param push_support: 证书是否支持推送。
        :type push_support: bool
        :param cert_issued_time: 证书签发时间，毫秒级时间戳。
        :type cert_issued_time: str
        :param resource_id: 资源id。
        :type resource_id: str
        :param unsubscribe_support: 证书是否支持退订。
        :type unsubscribe_support: bool
        :param enterprise_project_id: 企业项目ID，默认为“0”。 对于开通企业项目的用户，表示资源处于默认企业项目下。 对于未开通企业项目的用户，表示资源未处于企业项目下。
        :type enterprise_project_id: str
        :param origin_cert_id: 初始证书id。
        :type origin_cert_id: str
        :param renewal_cert_id: 续费购买证书id。
        :type renewal_cert_id: str
        :param auto_renew_status: 自动续费状态。
        :type auto_renew_status: int
        :param remain_cert_number: 剩余证书有效个数。
        :type remain_cert_number: int
        :param auto_deploy_support: 证书是否支持自动部署。
        :type auto_deploy_support: bool
        """
        
        

        self._cert_id = None
        self._cert_name = None
        self._domain = None
        self._cert_type = None
        self._cert_brand = None
        self._domain_type = None
        self._purchase_period = None
        self._expired_time = None
        self._order_status = None
        self._domain_num = None
        self._wildcard_number = None
        self._sans = None
        self._cert_des = None
        self._signature_algorithm = None
        self._fail_reason = None
        self._partner_order_id = None
        self._push_support = None
        self._cert_issued_time = None
        self._resource_id = None
        self._unsubscribe_support = None
        self._enterprise_project_id = None
        self._origin_cert_id = None
        self._renewal_cert_id = None
        self._auto_renew_status = None
        self._remain_cert_number = None
        self._auto_deploy_support = None
        self.discriminator = None

        if cert_id is not None:
            self.cert_id = cert_id
        if cert_name is not None:
            self.cert_name = cert_name
        if domain is not None:
            self.domain = domain
        if cert_type is not None:
            self.cert_type = cert_type
        if cert_brand is not None:
            self.cert_brand = cert_brand
        if domain_type is not None:
            self.domain_type = domain_type
        if purchase_period is not None:
            self.purchase_period = purchase_period
        if expired_time is not None:
            self.expired_time = expired_time
        if order_status is not None:
            self.order_status = order_status
        if domain_num is not None:
            self.domain_num = domain_num
        if wildcard_number is not None:
            self.wildcard_number = wildcard_number
        if sans is not None:
            self.sans = sans
        if cert_des is not None:
            self.cert_des = cert_des
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if partner_order_id is not None:
            self.partner_order_id = partner_order_id
        if push_support is not None:
            self.push_support = push_support
        if cert_issued_time is not None:
            self.cert_issued_time = cert_issued_time
        if resource_id is not None:
            self.resource_id = resource_id
        if unsubscribe_support is not None:
            self.unsubscribe_support = unsubscribe_support
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if origin_cert_id is not None:
            self.origin_cert_id = origin_cert_id
        if renewal_cert_id is not None:
            self.renewal_cert_id = renewal_cert_id
        if auto_renew_status is not None:
            self.auto_renew_status = auto_renew_status
        if remain_cert_number is not None:
            self.remain_cert_number = remain_cert_number
        if auto_deploy_support is not None:
            self.auto_deploy_support = auto_deploy_support

    @property
    def cert_id(self):
        r"""Gets the cert_id of this TagResourceResourceDetail.

        证书ID。

        :return: The cert_id of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this TagResourceResourceDetail.

        证书ID。

        :param cert_id: The cert_id of this TagResourceResourceDetail.
        :type cert_id: str
        """
        self._cert_id = cert_id

    @property
    def cert_name(self):
        r"""Gets the cert_name of this TagResourceResourceDetail.

        证书名称。字符长度为3~63位。

        :return: The cert_name of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this TagResourceResourceDetail.

        证书名称。字符长度为3~63位。

        :param cert_name: The cert_name of this TagResourceResourceDetail.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def domain(self):
        r"""Gets the domain of this TagResourceResourceDetail.

        该证书绑定的域名。 - 当购买的证书为“单域名”或“泛域名”类型的证书时，请直接填写单域名或泛域名即可。 - 当购买的证书为“多域名”类型的证书时，需要选择1个域名作为主域名。 示例：www.example.com

        :return: The domain of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this TagResourceResourceDetail.

        该证书绑定的域名。 - 当购买的证书为“单域名”或“泛域名”类型的证书时，请直接填写单域名或泛域名即可。 - 当购买的证书为“多域名”类型的证书时，需要选择1个域名作为主域名。 示例：www.example.com

        :param domain: The domain of this TagResourceResourceDetail.
        :type domain: str
        """
        self._domain = domain

    @property
    def cert_type(self):
        r"""Gets the cert_type of this TagResourceResourceDetail.

        证书类型。 - OV_SSL_CERT：企业型SSL证书。 - EV_SSL_CERT：增强型SSL证书。

        :return: The cert_type of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._cert_type

    @cert_type.setter
    def cert_type(self, cert_type):
        r"""Sets the cert_type of this TagResourceResourceDetail.

        证书类型。 - OV_SSL_CERT：企业型SSL证书。 - EV_SSL_CERT：增强型SSL证书。

        :param cert_type: The cert_type of this TagResourceResourceDetail.
        :type cert_type: str
        """
        self._cert_type = cert_type

    @property
    def cert_brand(self):
        r"""Gets the cert_brand of this TagResourceResourceDetail.

        证书品牌。GLOBALSIGN：GlobalSign品牌。

        :return: The cert_brand of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._cert_brand

    @cert_brand.setter
    def cert_brand(self, cert_brand):
        r"""Sets the cert_brand of this TagResourceResourceDetail.

        证书品牌。GLOBALSIGN：GlobalSign品牌。

        :param cert_brand: The cert_brand of this TagResourceResourceDetail.
        :type cert_brand: str
        """
        self._cert_brand = cert_brand

    @property
    def domain_type(self):
        r"""Gets the domain_type of this TagResourceResourceDetail.

        域名类型。 - SINGLE_DOMAIN：单域名类型。 - MULTI_DOMAIN：多域名类型。 - WILDCARD：泛域名类型。

        :return: The domain_type of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this TagResourceResourceDetail.

        域名类型。 - SINGLE_DOMAIN：单域名类型。 - MULTI_DOMAIN：多域名类型。 - WILDCARD：泛域名类型。

        :param domain_type: The domain_type of this TagResourceResourceDetail.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def purchase_period(self):
        r"""Gets the purchase_period of this TagResourceResourceDetail.

        证书有效期（年）。

        :return: The purchase_period of this TagResourceResourceDetail.
        :rtype: int
        """
        return self._purchase_period

    @purchase_period.setter
    def purchase_period(self, purchase_period):
        r"""Sets the purchase_period of this TagResourceResourceDetail.

        证书有效期（年）。

        :param purchase_period: The purchase_period of this TagResourceResourceDetail.
        :type purchase_period: int
        """
        self._purchase_period = purchase_period

    @property
    def expired_time(self):
        r"""Gets the expired_time of this TagResourceResourceDetail.

        证书到期时间，毫秒级时间戳。

        :return: The expired_time of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        r"""Sets the expired_time of this TagResourceResourceDetail.

        证书到期时间，毫秒级时间戳。

        :param expired_time: The expired_time of this TagResourceResourceDetail.
        :type expired_time: str
        """
        self._expired_time = expired_time

    @property
    def order_status(self):
        r"""Gets the order_status of this TagResourceResourceDetail.

        订单状态。

        :return: The order_status of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        r"""Sets the order_status of this TagResourceResourceDetail.

        订单状态。

        :param order_status: The order_status of this TagResourceResourceDetail.
        :type order_status: str
        """
        self._order_status = order_status

    @property
    def domain_num(self):
        r"""Gets the domain_num of this TagResourceResourceDetail.

        域名数量。 - 当“domain_type”选择的是“SINGLE_DOMAIN”或“WILDCARD”类型的证书时，域名数量取值为“1”。 - 当“domain_type”选择的是“MULTI_DOMAIN”类型的证书时，域名数量取值范围为“2~250”。

        :return: The domain_num of this TagResourceResourceDetail.
        :rtype: int
        """
        return self._domain_num

    @domain_num.setter
    def domain_num(self, domain_num):
        r"""Sets the domain_num of this TagResourceResourceDetail.

        域名数量。 - 当“domain_type”选择的是“SINGLE_DOMAIN”或“WILDCARD”类型的证书时，域名数量取值为“1”。 - 当“domain_type”选择的是“MULTI_DOMAIN”类型的证书时，域名数量取值范围为“2~250”。

        :param domain_num: The domain_num of this TagResourceResourceDetail.
        :type domain_num: int
        """
        self._domain_num = domain_num

    @property
    def wildcard_number(self):
        r"""Gets the wildcard_number of this TagResourceResourceDetail.

        泛域名数量。

        :return: The wildcard_number of this TagResourceResourceDetail.
        :rtype: int
        """
        return self._wildcard_number

    @wildcard_number.setter
    def wildcard_number(self, wildcard_number):
        r"""Sets the wildcard_number of this TagResourceResourceDetail.

        泛域名数量。

        :param wildcard_number: The wildcard_number of this TagResourceResourceDetail.
        :type wildcard_number: int
        """
        self._wildcard_number = wildcard_number

    @property
    def sans(self):
        r"""Gets the sans of this TagResourceResourceDetail.

        证书绑定的附加域名信息。

        :return: The sans of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._sans

    @sans.setter
    def sans(self, sans):
        r"""Sets the sans of this TagResourceResourceDetail.

        证书绑定的附加域名信息。

        :param sans: The sans of this TagResourceResourceDetail.
        :type sans: str
        """
        self._sans = sans

    @property
    def cert_des(self):
        r"""Gets the cert_des of this TagResourceResourceDetail.

        证书描述。

        :return: The cert_des of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._cert_des

    @cert_des.setter
    def cert_des(self, cert_des):
        r"""Sets the cert_des of this TagResourceResourceDetail.

        证书描述。

        :param cert_des: The cert_des of this TagResourceResourceDetail.
        :type cert_des: str
        """
        self._cert_des = cert_des

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this TagResourceResourceDetail.

        签名算法。

        :return: The signature_algorithm of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this TagResourceResourceDetail.

        签名算法。

        :param signature_algorithm: The signature_algorithm of this TagResourceResourceDetail.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this TagResourceResourceDetail.

        失败原因。

        :return: The fail_reason of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this TagResourceResourceDetail.

        失败原因。

        :param fail_reason: The fail_reason of this TagResourceResourceDetail.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def partner_order_id(self):
        r"""Gets the partner_order_id of this TagResourceResourceDetail.

        订单流水号。

        :return: The partner_order_id of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._partner_order_id

    @partner_order_id.setter
    def partner_order_id(self, partner_order_id):
        r"""Sets the partner_order_id of this TagResourceResourceDetail.

        订单流水号。

        :param partner_order_id: The partner_order_id of this TagResourceResourceDetail.
        :type partner_order_id: str
        """
        self._partner_order_id = partner_order_id

    @property
    def push_support(self):
        r"""Gets the push_support of this TagResourceResourceDetail.

        证书是否支持推送。

        :return: The push_support of this TagResourceResourceDetail.
        :rtype: bool
        """
        return self._push_support

    @push_support.setter
    def push_support(self, push_support):
        r"""Sets the push_support of this TagResourceResourceDetail.

        证书是否支持推送。

        :param push_support: The push_support of this TagResourceResourceDetail.
        :type push_support: bool
        """
        self._push_support = push_support

    @property
    def cert_issued_time(self):
        r"""Gets the cert_issued_time of this TagResourceResourceDetail.

        证书签发时间，毫秒级时间戳。

        :return: The cert_issued_time of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._cert_issued_time

    @cert_issued_time.setter
    def cert_issued_time(self, cert_issued_time):
        r"""Sets the cert_issued_time of this TagResourceResourceDetail.

        证书签发时间，毫秒级时间戳。

        :param cert_issued_time: The cert_issued_time of this TagResourceResourceDetail.
        :type cert_issued_time: str
        """
        self._cert_issued_time = cert_issued_time

    @property
    def resource_id(self):
        r"""Gets the resource_id of this TagResourceResourceDetail.

        资源id。

        :return: The resource_id of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this TagResourceResourceDetail.

        资源id。

        :param resource_id: The resource_id of this TagResourceResourceDetail.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def unsubscribe_support(self):
        r"""Gets the unsubscribe_support of this TagResourceResourceDetail.

        证书是否支持退订。

        :return: The unsubscribe_support of this TagResourceResourceDetail.
        :rtype: bool
        """
        return self._unsubscribe_support

    @unsubscribe_support.setter
    def unsubscribe_support(self, unsubscribe_support):
        r"""Sets the unsubscribe_support of this TagResourceResourceDetail.

        证书是否支持退订。

        :param unsubscribe_support: The unsubscribe_support of this TagResourceResourceDetail.
        :type unsubscribe_support: bool
        """
        self._unsubscribe_support = unsubscribe_support

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this TagResourceResourceDetail.

        企业项目ID，默认为“0”。 对于开通企业项目的用户，表示资源处于默认企业项目下。 对于未开通企业项目的用户，表示资源未处于企业项目下。

        :return: The enterprise_project_id of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this TagResourceResourceDetail.

        企业项目ID，默认为“0”。 对于开通企业项目的用户，表示资源处于默认企业项目下。 对于未开通企业项目的用户，表示资源未处于企业项目下。

        :param enterprise_project_id: The enterprise_project_id of this TagResourceResourceDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def origin_cert_id(self):
        r"""Gets the origin_cert_id of this TagResourceResourceDetail.

        初始证书id。

        :return: The origin_cert_id of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._origin_cert_id

    @origin_cert_id.setter
    def origin_cert_id(self, origin_cert_id):
        r"""Sets the origin_cert_id of this TagResourceResourceDetail.

        初始证书id。

        :param origin_cert_id: The origin_cert_id of this TagResourceResourceDetail.
        :type origin_cert_id: str
        """
        self._origin_cert_id = origin_cert_id

    @property
    def renewal_cert_id(self):
        r"""Gets the renewal_cert_id of this TagResourceResourceDetail.

        续费购买证书id。

        :return: The renewal_cert_id of this TagResourceResourceDetail.
        :rtype: str
        """
        return self._renewal_cert_id

    @renewal_cert_id.setter
    def renewal_cert_id(self, renewal_cert_id):
        r"""Sets the renewal_cert_id of this TagResourceResourceDetail.

        续费购买证书id。

        :param renewal_cert_id: The renewal_cert_id of this TagResourceResourceDetail.
        :type renewal_cert_id: str
        """
        self._renewal_cert_id = renewal_cert_id

    @property
    def auto_renew_status(self):
        r"""Gets the auto_renew_status of this TagResourceResourceDetail.

        自动续费状态。

        :return: The auto_renew_status of this TagResourceResourceDetail.
        :rtype: int
        """
        return self._auto_renew_status

    @auto_renew_status.setter
    def auto_renew_status(self, auto_renew_status):
        r"""Sets the auto_renew_status of this TagResourceResourceDetail.

        自动续费状态。

        :param auto_renew_status: The auto_renew_status of this TagResourceResourceDetail.
        :type auto_renew_status: int
        """
        self._auto_renew_status = auto_renew_status

    @property
    def remain_cert_number(self):
        r"""Gets the remain_cert_number of this TagResourceResourceDetail.

        剩余证书有效个数。

        :return: The remain_cert_number of this TagResourceResourceDetail.
        :rtype: int
        """
        return self._remain_cert_number

    @remain_cert_number.setter
    def remain_cert_number(self, remain_cert_number):
        r"""Sets the remain_cert_number of this TagResourceResourceDetail.

        剩余证书有效个数。

        :param remain_cert_number: The remain_cert_number of this TagResourceResourceDetail.
        :type remain_cert_number: int
        """
        self._remain_cert_number = remain_cert_number

    @property
    def auto_deploy_support(self):
        r"""Gets the auto_deploy_support of this TagResourceResourceDetail.

        证书是否支持自动部署。

        :return: The auto_deploy_support of this TagResourceResourceDetail.
        :rtype: bool
        """
        return self._auto_deploy_support

    @auto_deploy_support.setter
    def auto_deploy_support(self, auto_deploy_support):
        r"""Sets the auto_deploy_support of this TagResourceResourceDetail.

        证书是否支持自动部署。

        :param auto_deploy_support: The auto_deploy_support of this TagResourceResourceDetail.
        :type auto_deploy_support: bool
        """
        self._auto_deploy_support = auto_deploy_support

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
        if not isinstance(other, TagResourceResourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
