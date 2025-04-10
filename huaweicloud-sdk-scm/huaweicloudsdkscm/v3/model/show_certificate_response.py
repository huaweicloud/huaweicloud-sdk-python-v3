# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'order_id': 'str',
        'name': 'str',
        'type': 'str',
        'brand': 'str',
        'push_support': 'str',
        'revoke_reason': 'str',
        'signature_algorithm': 'str',
        'issue_time': 'str',
        'not_before': 'str',
        'not_after': 'str',
        'validity_period': 'int',
        'validation_method': 'str',
        'domain_type': 'str',
        'multi_domain_type': 'str',
        'domain': 'str',
        'sans': 'str',
        'domain_count': 'int',
        'wildcard_count': 'int',
        'fingerprint': 'str',
        'shared': 'bool',
        'application_info': 'ShowCertificateResponseBodyApplicationInfo',
        'description': 'str',
        'enterprise_project_id': 'str',
        'authentification': 'list[Authentification]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'order_id': 'order_id',
        'name': 'name',
        'type': 'type',
        'brand': 'brand',
        'push_support': 'push_support',
        'revoke_reason': 'revoke_reason',
        'signature_algorithm': 'signature_algorithm',
        'issue_time': 'issue_time',
        'not_before': 'not_before',
        'not_after': 'not_after',
        'validity_period': 'validity_period',
        'validation_method': 'validation_method',
        'domain_type': 'domain_type',
        'multi_domain_type': 'multi_domain_type',
        'domain': 'domain',
        'sans': 'sans',
        'domain_count': 'domain_count',
        'wildcard_count': 'wildcard_count',
        'fingerprint': 'fingerprint',
        'shared': 'shared',
        'application_info': 'application_info',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'authentification': 'authentification'
    }

    def __init__(self, id=None, status=None, order_id=None, name=None, type=None, brand=None, push_support=None, revoke_reason=None, signature_algorithm=None, issue_time=None, not_before=None, not_after=None, validity_period=None, validation_method=None, domain_type=None, multi_domain_type=None, domain=None, sans=None, domain_count=None, wildcard_count=None, fingerprint=None, shared=None, application_info=None, description=None, enterprise_project_id=None, authentification=None):
        r"""ShowCertificateResponse

        The model defined in huaweicloud sdk

        :param id: 证书id。
        :type id: str
        :param status: 证书状态。取值如下： - PAID：证书已支付，待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。 - CANCELSUPPLEMENTING：取消新增附加域名审核中。
        :type status: str
        :param order_id: 订单id。
        :type order_id: str
        :param name: 证书名称。
        :type name: str
        :param type: 证书类型。取值如下： DV_SSL_CERT、DV_SSL_CERT_BASIC、EV_SSL_CERT、 EV_SSL_CERT_PRO、OV_SSL_CERT、OV_SSL_CERT_PRO。
        :type type: str
        :param brand: 证书品牌。取值如下： GLOBALSIGN、SYMANTEC、GEOTRUST、CFCA。
        :type brand: str
        :param push_support: 证书是否支持推送。
        :type push_support: str
        :param revoke_reason: 证书吊销原因。
        :type revoke_reason: str
        :param signature_algorithm: 签名算法。
        :type signature_algorithm: str
        :param issue_time: 证书签发时间，没有获取到有效值时为空。
        :type issue_time: str
        :param not_before: 证书生效时间，没有获取到有效值时为空。
        :type not_before: str
        :param not_after: 证书失效时间，没有获取到有效值时为空。
        :type not_after: str
        :param validity_period: 证书有效期，按月为单位。[云证书管理服务提供了一种购买多年有效期证书的解决方案，这种多年有效期证书生效方式为多张有效期为1年的SSL证书叠加生效，例如：有效期为“3年”的证书实际包含3张有效期为1年且规格相同的SSL证书，在第一张证书到期前30天，系统自动以第一张证书的信息申请第二张证书，在第二张证书到期前30天，系统自动以第一张证书的信息申请第三张证书。](tag:hws)
        :type validity_period: int
        :param validation_method: 域名认证方式，取值如下：DNS、FILE、EMAIL。
        :type validation_method: str
        :param domain_type: 域名类型，取值如下： - SINGLE_DOMAIN：单域名 - WILDCARD：通配符 - MULTI_DOMAIN：多域名
        :type domain_type: str
        :param multi_domain_type: 多域名类型，取值如下： - primary_single：主单域名 - primary_wildcard：主泛域名
        :type multi_domain_type: str
        :param domain: 证书绑定域名。
        :type domain: str
        :param sans: 证书绑定的附加域名信息。
        :type sans: str
        :param domain_count: 证书可绑定域名个数。
        :type domain_count: int
        :param wildcard_count: 证书可绑定附加域名个数。
        :type wildcard_count: int
        :param fingerprint: 证书的SHA-1指纹。
        :type fingerprint: str
        :param shared: 是否是共享资源。
        :type shared: bool
        :param application_info: 
        :type application_info: :class:`huaweicloudsdkscm.v3.ShowCertificateResponseBodyApplicationInfo`
        :param description: 证书的描述。
        :type description: str
        :param enterprise_project_id: 企业项目ID，默认为“0”。 对于开通企业项目的用户，表示资源处于默认企业项目下。 对于未开通企业项目的用户，表示资源未处于企业项目下。
        :type enterprise_project_id: str
        :param authentification: 域名所有权认证信息，详情请参见Authentification字段数据结构说明。
        :type authentification: list[:class:`huaweicloudsdkscm.v3.Authentification`]
        """
        
        super(ShowCertificateResponse, self).__init__()

        self._id = None
        self._status = None
        self._order_id = None
        self._name = None
        self._type = None
        self._brand = None
        self._push_support = None
        self._revoke_reason = None
        self._signature_algorithm = None
        self._issue_time = None
        self._not_before = None
        self._not_after = None
        self._validity_period = None
        self._validation_method = None
        self._domain_type = None
        self._multi_domain_type = None
        self._domain = None
        self._sans = None
        self._domain_count = None
        self._wildcard_count = None
        self._fingerprint = None
        self._shared = None
        self._application_info = None
        self._description = None
        self._enterprise_project_id = None
        self._authentification = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if order_id is not None:
            self.order_id = order_id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if brand is not None:
            self.brand = brand
        if push_support is not None:
            self.push_support = push_support
        if revoke_reason is not None:
            self.revoke_reason = revoke_reason
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if issue_time is not None:
            self.issue_time = issue_time
        if not_before is not None:
            self.not_before = not_before
        if not_after is not None:
            self.not_after = not_after
        if validity_period is not None:
            self.validity_period = validity_period
        if validation_method is not None:
            self.validation_method = validation_method
        if domain_type is not None:
            self.domain_type = domain_type
        if multi_domain_type is not None:
            self.multi_domain_type = multi_domain_type
        if domain is not None:
            self.domain = domain
        if sans is not None:
            self.sans = sans
        if domain_count is not None:
            self.domain_count = domain_count
        if wildcard_count is not None:
            self.wildcard_count = wildcard_count
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if shared is not None:
            self.shared = shared
        if application_info is not None:
            self.application_info = application_info
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if authentification is not None:
            self.authentification = authentification

    @property
    def id(self):
        r"""Gets the id of this ShowCertificateResponse.

        证书id。

        :return: The id of this ShowCertificateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowCertificateResponse.

        证书id。

        :param id: The id of this ShowCertificateResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ShowCertificateResponse.

        证书状态。取值如下： - PAID：证书已支付，待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。 - CANCELSUPPLEMENTING：取消新增附加域名审核中。

        :return: The status of this ShowCertificateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowCertificateResponse.

        证书状态。取值如下： - PAID：证书已支付，待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。 - CANCELSUPPLEMENTING：取消新增附加域名审核中。

        :param status: The status of this ShowCertificateResponse.
        :type status: str
        """
        self._status = status

    @property
    def order_id(self):
        r"""Gets the order_id of this ShowCertificateResponse.

        订单id。

        :return: The order_id of this ShowCertificateResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ShowCertificateResponse.

        订单id。

        :param order_id: The order_id of this ShowCertificateResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def name(self):
        r"""Gets the name of this ShowCertificateResponse.

        证书名称。

        :return: The name of this ShowCertificateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowCertificateResponse.

        证书名称。

        :param name: The name of this ShowCertificateResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ShowCertificateResponse.

        证书类型。取值如下： DV_SSL_CERT、DV_SSL_CERT_BASIC、EV_SSL_CERT、 EV_SSL_CERT_PRO、OV_SSL_CERT、OV_SSL_CERT_PRO。

        :return: The type of this ShowCertificateResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowCertificateResponse.

        证书类型。取值如下： DV_SSL_CERT、DV_SSL_CERT_BASIC、EV_SSL_CERT、 EV_SSL_CERT_PRO、OV_SSL_CERT、OV_SSL_CERT_PRO。

        :param type: The type of this ShowCertificateResponse.
        :type type: str
        """
        self._type = type

    @property
    def brand(self):
        r"""Gets the brand of this ShowCertificateResponse.

        证书品牌。取值如下： GLOBALSIGN、SYMANTEC、GEOTRUST、CFCA。

        :return: The brand of this ShowCertificateResponse.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        r"""Sets the brand of this ShowCertificateResponse.

        证书品牌。取值如下： GLOBALSIGN、SYMANTEC、GEOTRUST、CFCA。

        :param brand: The brand of this ShowCertificateResponse.
        :type brand: str
        """
        self._brand = brand

    @property
    def push_support(self):
        r"""Gets the push_support of this ShowCertificateResponse.

        证书是否支持推送。

        :return: The push_support of this ShowCertificateResponse.
        :rtype: str
        """
        return self._push_support

    @push_support.setter
    def push_support(self, push_support):
        r"""Sets the push_support of this ShowCertificateResponse.

        证书是否支持推送。

        :param push_support: The push_support of this ShowCertificateResponse.
        :type push_support: str
        """
        self._push_support = push_support

    @property
    def revoke_reason(self):
        r"""Gets the revoke_reason of this ShowCertificateResponse.

        证书吊销原因。

        :return: The revoke_reason of this ShowCertificateResponse.
        :rtype: str
        """
        return self._revoke_reason

    @revoke_reason.setter
    def revoke_reason(self, revoke_reason):
        r"""Sets the revoke_reason of this ShowCertificateResponse.

        证书吊销原因。

        :param revoke_reason: The revoke_reason of this ShowCertificateResponse.
        :type revoke_reason: str
        """
        self._revoke_reason = revoke_reason

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this ShowCertificateResponse.

        签名算法。

        :return: The signature_algorithm of this ShowCertificateResponse.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this ShowCertificateResponse.

        签名算法。

        :param signature_algorithm: The signature_algorithm of this ShowCertificateResponse.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def issue_time(self):
        r"""Gets the issue_time of this ShowCertificateResponse.

        证书签发时间，没有获取到有效值时为空。

        :return: The issue_time of this ShowCertificateResponse.
        :rtype: str
        """
        return self._issue_time

    @issue_time.setter
    def issue_time(self, issue_time):
        r"""Sets the issue_time of this ShowCertificateResponse.

        证书签发时间，没有获取到有效值时为空。

        :param issue_time: The issue_time of this ShowCertificateResponse.
        :type issue_time: str
        """
        self._issue_time = issue_time

    @property
    def not_before(self):
        r"""Gets the not_before of this ShowCertificateResponse.

        证书生效时间，没有获取到有效值时为空。

        :return: The not_before of this ShowCertificateResponse.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        r"""Sets the not_before of this ShowCertificateResponse.

        证书生效时间，没有获取到有效值时为空。

        :param not_before: The not_before of this ShowCertificateResponse.
        :type not_before: str
        """
        self._not_before = not_before

    @property
    def not_after(self):
        r"""Gets the not_after of this ShowCertificateResponse.

        证书失效时间，没有获取到有效值时为空。

        :return: The not_after of this ShowCertificateResponse.
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        r"""Sets the not_after of this ShowCertificateResponse.

        证书失效时间，没有获取到有效值时为空。

        :param not_after: The not_after of this ShowCertificateResponse.
        :type not_after: str
        """
        self._not_after = not_after

    @property
    def validity_period(self):
        r"""Gets the validity_period of this ShowCertificateResponse.

        证书有效期，按月为单位。[云证书管理服务提供了一种购买多年有效期证书的解决方案，这种多年有效期证书生效方式为多张有效期为1年的SSL证书叠加生效，例如：有效期为“3年”的证书实际包含3张有效期为1年且规格相同的SSL证书，在第一张证书到期前30天，系统自动以第一张证书的信息申请第二张证书，在第二张证书到期前30天，系统自动以第一张证书的信息申请第三张证书。](tag:hws)

        :return: The validity_period of this ShowCertificateResponse.
        :rtype: int
        """
        return self._validity_period

    @validity_period.setter
    def validity_period(self, validity_period):
        r"""Sets the validity_period of this ShowCertificateResponse.

        证书有效期，按月为单位。[云证书管理服务提供了一种购买多年有效期证书的解决方案，这种多年有效期证书生效方式为多张有效期为1年的SSL证书叠加生效，例如：有效期为“3年”的证书实际包含3张有效期为1年且规格相同的SSL证书，在第一张证书到期前30天，系统自动以第一张证书的信息申请第二张证书，在第二张证书到期前30天，系统自动以第一张证书的信息申请第三张证书。](tag:hws)

        :param validity_period: The validity_period of this ShowCertificateResponse.
        :type validity_period: int
        """
        self._validity_period = validity_period

    @property
    def validation_method(self):
        r"""Gets the validation_method of this ShowCertificateResponse.

        域名认证方式，取值如下：DNS、FILE、EMAIL。

        :return: The validation_method of this ShowCertificateResponse.
        :rtype: str
        """
        return self._validation_method

    @validation_method.setter
    def validation_method(self, validation_method):
        r"""Sets the validation_method of this ShowCertificateResponse.

        域名认证方式，取值如下：DNS、FILE、EMAIL。

        :param validation_method: The validation_method of this ShowCertificateResponse.
        :type validation_method: str
        """
        self._validation_method = validation_method

    @property
    def domain_type(self):
        r"""Gets the domain_type of this ShowCertificateResponse.

        域名类型，取值如下： - SINGLE_DOMAIN：单域名 - WILDCARD：通配符 - MULTI_DOMAIN：多域名

        :return: The domain_type of this ShowCertificateResponse.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this ShowCertificateResponse.

        域名类型，取值如下： - SINGLE_DOMAIN：单域名 - WILDCARD：通配符 - MULTI_DOMAIN：多域名

        :param domain_type: The domain_type of this ShowCertificateResponse.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def multi_domain_type(self):
        r"""Gets the multi_domain_type of this ShowCertificateResponse.

        多域名类型，取值如下： - primary_single：主单域名 - primary_wildcard：主泛域名

        :return: The multi_domain_type of this ShowCertificateResponse.
        :rtype: str
        """
        return self._multi_domain_type

    @multi_domain_type.setter
    def multi_domain_type(self, multi_domain_type):
        r"""Sets the multi_domain_type of this ShowCertificateResponse.

        多域名类型，取值如下： - primary_single：主单域名 - primary_wildcard：主泛域名

        :param multi_domain_type: The multi_domain_type of this ShowCertificateResponse.
        :type multi_domain_type: str
        """
        self._multi_domain_type = multi_domain_type

    @property
    def domain(self):
        r"""Gets the domain of this ShowCertificateResponse.

        证书绑定域名。

        :return: The domain of this ShowCertificateResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ShowCertificateResponse.

        证书绑定域名。

        :param domain: The domain of this ShowCertificateResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def sans(self):
        r"""Gets the sans of this ShowCertificateResponse.

        证书绑定的附加域名信息。

        :return: The sans of this ShowCertificateResponse.
        :rtype: str
        """
        return self._sans

    @sans.setter
    def sans(self, sans):
        r"""Sets the sans of this ShowCertificateResponse.

        证书绑定的附加域名信息。

        :param sans: The sans of this ShowCertificateResponse.
        :type sans: str
        """
        self._sans = sans

    @property
    def domain_count(self):
        r"""Gets the domain_count of this ShowCertificateResponse.

        证书可绑定域名个数。

        :return: The domain_count of this ShowCertificateResponse.
        :rtype: int
        """
        return self._domain_count

    @domain_count.setter
    def domain_count(self, domain_count):
        r"""Sets the domain_count of this ShowCertificateResponse.

        证书可绑定域名个数。

        :param domain_count: The domain_count of this ShowCertificateResponse.
        :type domain_count: int
        """
        self._domain_count = domain_count

    @property
    def wildcard_count(self):
        r"""Gets the wildcard_count of this ShowCertificateResponse.

        证书可绑定附加域名个数。

        :return: The wildcard_count of this ShowCertificateResponse.
        :rtype: int
        """
        return self._wildcard_count

    @wildcard_count.setter
    def wildcard_count(self, wildcard_count):
        r"""Sets the wildcard_count of this ShowCertificateResponse.

        证书可绑定附加域名个数。

        :param wildcard_count: The wildcard_count of this ShowCertificateResponse.
        :type wildcard_count: int
        """
        self._wildcard_count = wildcard_count

    @property
    def fingerprint(self):
        r"""Gets the fingerprint of this ShowCertificateResponse.

        证书的SHA-1指纹。

        :return: The fingerprint of this ShowCertificateResponse.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        r"""Sets the fingerprint of this ShowCertificateResponse.

        证书的SHA-1指纹。

        :param fingerprint: The fingerprint of this ShowCertificateResponse.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def shared(self):
        r"""Gets the shared of this ShowCertificateResponse.

        是否是共享资源。

        :return: The shared of this ShowCertificateResponse.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        r"""Sets the shared of this ShowCertificateResponse.

        是否是共享资源。

        :param shared: The shared of this ShowCertificateResponse.
        :type shared: bool
        """
        self._shared = shared

    @property
    def application_info(self):
        r"""Gets the application_info of this ShowCertificateResponse.

        :return: The application_info of this ShowCertificateResponse.
        :rtype: :class:`huaweicloudsdkscm.v3.ShowCertificateResponseBodyApplicationInfo`
        """
        return self._application_info

    @application_info.setter
    def application_info(self, application_info):
        r"""Sets the application_info of this ShowCertificateResponse.

        :param application_info: The application_info of this ShowCertificateResponse.
        :type application_info: :class:`huaweicloudsdkscm.v3.ShowCertificateResponseBodyApplicationInfo`
        """
        self._application_info = application_info

    @property
    def description(self):
        r"""Gets the description of this ShowCertificateResponse.

        证书的描述。

        :return: The description of this ShowCertificateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowCertificateResponse.

        证书的描述。

        :param description: The description of this ShowCertificateResponse.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowCertificateResponse.

        企业项目ID，默认为“0”。 对于开通企业项目的用户，表示资源处于默认企业项目下。 对于未开通企业项目的用户，表示资源未处于企业项目下。

        :return: The enterprise_project_id of this ShowCertificateResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowCertificateResponse.

        企业项目ID，默认为“0”。 对于开通企业项目的用户，表示资源处于默认企业项目下。 对于未开通企业项目的用户，表示资源未处于企业项目下。

        :param enterprise_project_id: The enterprise_project_id of this ShowCertificateResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def authentification(self):
        r"""Gets the authentification of this ShowCertificateResponse.

        域名所有权认证信息，详情请参见Authentification字段数据结构说明。

        :return: The authentification of this ShowCertificateResponse.
        :rtype: list[:class:`huaweicloudsdkscm.v3.Authentification`]
        """
        return self._authentification

    @authentification.setter
    def authentification(self, authentification):
        r"""Sets the authentification of this ShowCertificateResponse.

        域名所有权认证信息，详情请参见Authentification字段数据结构说明。

        :param authentification: The authentification of this ShowCertificateResponse.
        :type authentification: list[:class:`huaweicloudsdkscm.v3.Authentification`]
        """
        self._authentification = authentification

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
        if not isinstance(other, ShowCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
