# coding: utf-8

import re
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
        'signature_algrithm': 'str',
        'issue_time': 'str',
        'not_before': 'str',
        'not_after': 'str',
        'validity_period': 'int',
        'validation_method': 'str',
        'domain_type': 'str',
        'domain': 'str',
        'sans': 'str',
        'domain_count': 'int',
        'wildcard_count': 'int',
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
        'signature_algrithm': 'signature_algrithm',
        'issue_time': 'issue_time',
        'not_before': 'not_before',
        'not_after': 'not_after',
        'validity_period': 'validity_period',
        'validation_method': 'validation_method',
        'domain_type': 'domain_type',
        'domain': 'domain',
        'sans': 'sans',
        'domain_count': 'domain_count',
        'wildcard_count': 'wildcard_count',
        'authentification': 'authentification'
    }

    def __init__(self, id=None, status=None, order_id=None, name=None, type=None, brand=None, push_support=None, revoke_reason=None, signature_algrithm=None, issue_time=None, not_before=None, not_after=None, validity_period=None, validation_method=None, domain_type=None, domain=None, sans=None, domain_count=None, wildcard_count=None, authentification=None):
        """ShowCertificateResponse - a model defined in huaweicloud sdk"""
        
        super(ShowCertificateResponse, self).__init__()

        self._id = None
        self._status = None
        self._order_id = None
        self._name = None
        self._type = None
        self._brand = None
        self._push_support = None
        self._revoke_reason = None
        self._signature_algrithm = None
        self._issue_time = None
        self._not_before = None
        self._not_after = None
        self._validity_period = None
        self._validation_method = None
        self._domain_type = None
        self._domain = None
        self._sans = None
        self._domain_count = None
        self._wildcard_count = None
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
        if signature_algrithm is not None:
            self.signature_algrithm = signature_algrithm
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
        if domain is not None:
            self.domain = domain
        if sans is not None:
            self.sans = sans
        if domain_count is not None:
            self.domain_count = domain_count
        if wildcard_count is not None:
            self.wildcard_count = wildcard_count
        if authentification is not None:
            self.authentification = authentification

    @property
    def id(self):
        """Gets the id of this ShowCertificateResponse.

        证书id。

        :return: The id of this ShowCertificateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowCertificateResponse.

        证书id。

        :param id: The id of this ShowCertificateResponse.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ShowCertificateResponse.

        证书状态。取值如下： - PAID：证书已支付，待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。 - CANCELSUPPLEMENTING：取消新增附加域名审核中。

        :return: The status of this ShowCertificateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowCertificateResponse.

        证书状态。取值如下： - PAID：证书已支付，待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。 - CANCELSUPPLEMENTING：取消新增附加域名审核中。

        :param status: The status of this ShowCertificateResponse.
        :type: str
        """
        self._status = status

    @property
    def order_id(self):
        """Gets the order_id of this ShowCertificateResponse.

        订单id。

        :return: The order_id of this ShowCertificateResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ShowCertificateResponse.

        订单id。

        :param order_id: The order_id of this ShowCertificateResponse.
        :type: str
        """
        self._order_id = order_id

    @property
    def name(self):
        """Gets the name of this ShowCertificateResponse.

        证书名称。

        :return: The name of this ShowCertificateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowCertificateResponse.

        证书名称。

        :param name: The name of this ShowCertificateResponse.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ShowCertificateResponse.

        证书类型。取值如下： DV_SSL_CERT、DV_SSL_CERT_BASIC、EV_SSL_CERT、 EV_SSL_CERT_PRO、OV_SSL_CERT、OV_SSL_CERT_PRO。

        :return: The type of this ShowCertificateResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowCertificateResponse.

        证书类型。取值如下： DV_SSL_CERT、DV_SSL_CERT_BASIC、EV_SSL_CERT、 EV_SSL_CERT_PRO、OV_SSL_CERT、OV_SSL_CERT_PRO。

        :param type: The type of this ShowCertificateResponse.
        :type: str
        """
        self._type = type

    @property
    def brand(self):
        """Gets the brand of this ShowCertificateResponse.

        证书品牌。取值如下： GLOBALSIGN、SYMANTEC、GEOTRUST、CFCA。

        :return: The brand of this ShowCertificateResponse.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this ShowCertificateResponse.

        证书品牌。取值如下： GLOBALSIGN、SYMANTEC、GEOTRUST、CFCA。

        :param brand: The brand of this ShowCertificateResponse.
        :type: str
        """
        self._brand = brand

    @property
    def push_support(self):
        """Gets the push_support of this ShowCertificateResponse.

        证书是否支持推送。

        :return: The push_support of this ShowCertificateResponse.
        :rtype: str
        """
        return self._push_support

    @push_support.setter
    def push_support(self, push_support):
        """Sets the push_support of this ShowCertificateResponse.

        证书是否支持推送。

        :param push_support: The push_support of this ShowCertificateResponse.
        :type: str
        """
        self._push_support = push_support

    @property
    def revoke_reason(self):
        """Gets the revoke_reason of this ShowCertificateResponse.

        证书吊销原因。

        :return: The revoke_reason of this ShowCertificateResponse.
        :rtype: str
        """
        return self._revoke_reason

    @revoke_reason.setter
    def revoke_reason(self, revoke_reason):
        """Sets the revoke_reason of this ShowCertificateResponse.

        证书吊销原因。

        :param revoke_reason: The revoke_reason of this ShowCertificateResponse.
        :type: str
        """
        self._revoke_reason = revoke_reason

    @property
    def signature_algrithm(self):
        """Gets the signature_algrithm of this ShowCertificateResponse.

        签名算法。

        :return: The signature_algrithm of this ShowCertificateResponse.
        :rtype: str
        """
        return self._signature_algrithm

    @signature_algrithm.setter
    def signature_algrithm(self, signature_algrithm):
        """Sets the signature_algrithm of this ShowCertificateResponse.

        签名算法。

        :param signature_algrithm: The signature_algrithm of this ShowCertificateResponse.
        :type: str
        """
        self._signature_algrithm = signature_algrithm

    @property
    def issue_time(self):
        """Gets the issue_time of this ShowCertificateResponse.

        证书签发时间，没有获取到有效值时为空。

        :return: The issue_time of this ShowCertificateResponse.
        :rtype: str
        """
        return self._issue_time

    @issue_time.setter
    def issue_time(self, issue_time):
        """Sets the issue_time of this ShowCertificateResponse.

        证书签发时间，没有获取到有效值时为空。

        :param issue_time: The issue_time of this ShowCertificateResponse.
        :type: str
        """
        self._issue_time = issue_time

    @property
    def not_before(self):
        """Gets the not_before of this ShowCertificateResponse.

        证书生效时间，没有获取到有效值时为空。

        :return: The not_before of this ShowCertificateResponse.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this ShowCertificateResponse.

        证书生效时间，没有获取到有效值时为空。

        :param not_before: The not_before of this ShowCertificateResponse.
        :type: str
        """
        self._not_before = not_before

    @property
    def not_after(self):
        """Gets the not_after of this ShowCertificateResponse.

        证书失效时间，没有获取到有效值时为空。

        :return: The not_after of this ShowCertificateResponse.
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this ShowCertificateResponse.

        证书失效时间，没有获取到有效值时为空。

        :param not_after: The not_after of this ShowCertificateResponse.
        :type: str
        """
        self._not_after = not_after

    @property
    def validity_period(self):
        """Gets the validity_period of this ShowCertificateResponse.

        证书有效期，按月为单位。

        :return: The validity_period of this ShowCertificateResponse.
        :rtype: int
        """
        return self._validity_period

    @validity_period.setter
    def validity_period(self, validity_period):
        """Sets the validity_period of this ShowCertificateResponse.

        证书有效期，按月为单位。

        :param validity_period: The validity_period of this ShowCertificateResponse.
        :type: int
        """
        self._validity_period = validity_period

    @property
    def validation_method(self):
        """Gets the validation_method of this ShowCertificateResponse.

        域名认证方式，取值如下：DNS、FILE、EMAIL。

        :return: The validation_method of this ShowCertificateResponse.
        :rtype: str
        """
        return self._validation_method

    @validation_method.setter
    def validation_method(self, validation_method):
        """Sets the validation_method of this ShowCertificateResponse.

        域名认证方式，取值如下：DNS、FILE、EMAIL。

        :param validation_method: The validation_method of this ShowCertificateResponse.
        :type: str
        """
        self._validation_method = validation_method

    @property
    def domain_type(self):
        """Gets the domain_type of this ShowCertificateResponse.

        域名类型，取值如下： - SINGLE_DOMAIN：单域名 - WILDCARD：通配符 - MULTI_DOMAIN：多域名

        :return: The domain_type of this ShowCertificateResponse.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this ShowCertificateResponse.

        域名类型，取值如下： - SINGLE_DOMAIN：单域名 - WILDCARD：通配符 - MULTI_DOMAIN：多域名

        :param domain_type: The domain_type of this ShowCertificateResponse.
        :type: str
        """
        self._domain_type = domain_type

    @property
    def domain(self):
        """Gets the domain of this ShowCertificateResponse.

        证书绑定域名。

        :return: The domain of this ShowCertificateResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ShowCertificateResponse.

        证书绑定域名。

        :param domain: The domain of this ShowCertificateResponse.
        :type: str
        """
        self._domain = domain

    @property
    def sans(self):
        """Gets the sans of this ShowCertificateResponse.

        证书绑定的附加域名信息。

        :return: The sans of this ShowCertificateResponse.
        :rtype: str
        """
        return self._sans

    @sans.setter
    def sans(self, sans):
        """Sets the sans of this ShowCertificateResponse.

        证书绑定的附加域名信息。

        :param sans: The sans of this ShowCertificateResponse.
        :type: str
        """
        self._sans = sans

    @property
    def domain_count(self):
        """Gets the domain_count of this ShowCertificateResponse.

        证书可绑定域名个数。

        :return: The domain_count of this ShowCertificateResponse.
        :rtype: int
        """
        return self._domain_count

    @domain_count.setter
    def domain_count(self, domain_count):
        """Sets the domain_count of this ShowCertificateResponse.

        证书可绑定域名个数。

        :param domain_count: The domain_count of this ShowCertificateResponse.
        :type: int
        """
        self._domain_count = domain_count

    @property
    def wildcard_count(self):
        """Gets the wildcard_count of this ShowCertificateResponse.

        证书可绑定附加域名个数。

        :return: The wildcard_count of this ShowCertificateResponse.
        :rtype: int
        """
        return self._wildcard_count

    @wildcard_count.setter
    def wildcard_count(self, wildcard_count):
        """Sets the wildcard_count of this ShowCertificateResponse.

        证书可绑定附加域名个数。

        :param wildcard_count: The wildcard_count of this ShowCertificateResponse.
        :type: int
        """
        self._wildcard_count = wildcard_count

    @property
    def authentification(self):
        """Gets the authentification of this ShowCertificateResponse.

        域名所有权认证信息，详情请参见Authentification字段数据结构说明。

        :return: The authentification of this ShowCertificateResponse.
        :rtype: list[Authentification]
        """
        return self._authentification

    @authentification.setter
    def authentification(self, authentification):
        """Sets the authentification of this ShowCertificateResponse.

        域名所有权认证信息，详情请参见Authentification字段数据结构说明。

        :param authentification: The authentification of this ShowCertificateResponse.
        :type: list[Authentification]
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
