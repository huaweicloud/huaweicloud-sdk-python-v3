# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertificateDetail:


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
        'name': 'str',
        'domain': 'str',
        'type': 'str',
        'brand': 'str',
        'expire_time': 'str',
        'domain_type': 'str',
        'validity_period': 'int',
        'status': 'str',
        'domain_count': 'int',
        'wildcard_count': 'int',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'domain': 'domain',
        'type': 'type',
        'brand': 'brand',
        'expire_time': 'expire_time',
        'domain_type': 'domain_type',
        'validity_period': 'validity_period',
        'status': 'status',
        'domain_count': 'domain_count',
        'wildcard_count': 'wildcard_count',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, domain=None, type=None, brand=None, expire_time=None, domain_type=None, validity_period=None, status=None, domain_count=None, wildcard_count=None, description=None):
        """CertificateDetail - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._domain = None
        self._type = None
        self._brand = None
        self._expire_time = None
        self._domain_type = None
        self._validity_period = None
        self._status = None
        self._domain_count = None
        self._wildcard_count = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if domain is not None:
            self.domain = domain
        if type is not None:
            self.type = type
        if brand is not None:
            self.brand = brand
        if expire_time is not None:
            self.expire_time = expire_time
        if domain_type is not None:
            self.domain_type = domain_type
        if validity_period is not None:
            self.validity_period = validity_period
        if status is not None:
            self.status = status
        if domain_count is not None:
            self.domain_count = domain_count
        if wildcard_count is not None:
            self.wildcard_count = wildcard_count
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this CertificateDetail.

        证书id。

        :return: The id of this CertificateDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CertificateDetail.

        证书id。

        :param id: The id of this CertificateDetail.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CertificateDetail.

        证书名称。

        :return: The name of this CertificateDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertificateDetail.

        证书名称。

        :param name: The name of this CertificateDetail.
        :type: str
        """
        self._name = name

    @property
    def domain(self):
        """Gets the domain of this CertificateDetail.

        证书绑定的域名。

        :return: The domain of this CertificateDetail.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CertificateDetail.

        证书绑定的域名。

        :param domain: The domain of this CertificateDetail.
        :type: str
        """
        self._domain = domain

    @property
    def type(self):
        """Gets the type of this CertificateDetail.

        证书类型。取值如下： DV_SSL_CERT、DV_SSL_CERT_BASIC、EV_SSL_CERT、 EV_SSL_CERT_PRO、OV_SSL_CERT、OV_SSL_CERT_PRO

        :return: The type of this CertificateDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CertificateDetail.

        证书类型。取值如下： DV_SSL_CERT、DV_SSL_CERT_BASIC、EV_SSL_CERT、 EV_SSL_CERT_PRO、OV_SSL_CERT、OV_SSL_CERT_PRO

        :param type: The type of this CertificateDetail.
        :type: str
        """
        self._type = type

    @property
    def brand(self):
        """Gets the brand of this CertificateDetail.

        证书品牌。取值如下：GLOBALSIGN、SYMANTEC、GEOTRUST、CFCA

        :return: The brand of this CertificateDetail.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this CertificateDetail.

        证书品牌。取值如下：GLOBALSIGN、SYMANTEC、GEOTRUST、CFCA

        :param brand: The brand of this CertificateDetail.
        :type: str
        """
        self._brand = brand

    @property
    def expire_time(self):
        """Gets the expire_time of this CertificateDetail.

        证书过期时间。

        :return: The expire_time of this CertificateDetail.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CertificateDetail.

        证书过期时间。

        :param expire_time: The expire_time of this CertificateDetail.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def domain_type(self):
        """Gets the domain_type of this CertificateDetail.

        域名类型。取值如下： - SINGLE_DOMAIN：单域名 - WILDCARD：通配符 - MULTI_DOMAIN：多域名

        :return: The domain_type of this CertificateDetail.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this CertificateDetail.

        域名类型。取值如下： - SINGLE_DOMAIN：单域名 - WILDCARD：通配符 - MULTI_DOMAIN：多域名

        :param domain_type: The domain_type of this CertificateDetail.
        :type: str
        """
        self._domain_type = domain_type

    @property
    def validity_period(self):
        """Gets the validity_period of this CertificateDetail.

        证书有效期，以月为单位。

        :return: The validity_period of this CertificateDetail.
        :rtype: int
        """
        return self._validity_period

    @validity_period.setter
    def validity_period(self, validity_period):
        """Sets the validity_period of this CertificateDetail.

        证书有效期，以月为单位。

        :param validity_period: The validity_period of this CertificateDetail.
        :type: int
        """
        self._validity_period = validity_period

    @property
    def status(self):
        """Gets the status of this CertificateDetail.

        证书状态，取值如下： - PAID：证书已支付；待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - CANCLEREVOKING：证书取消吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。 - CANCELSUPPLEMENTING：取消新增附加域名审核中。

        :return: The status of this CertificateDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CertificateDetail.

        证书状态，取值如下： - PAID：证书已支付；待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - CANCLEREVOKING：证书取消吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。 - CANCELSUPPLEMENTING：取消新增附加域名审核中。

        :param status: The status of this CertificateDetail.
        :type: str
        """
        self._status = status

    @property
    def domain_count(self):
        """Gets the domain_count of this CertificateDetail.

        证书可绑定域名个数。

        :return: The domain_count of this CertificateDetail.
        :rtype: int
        """
        return self._domain_count

    @domain_count.setter
    def domain_count(self, domain_count):
        """Sets the domain_count of this CertificateDetail.

        证书可绑定域名个数。

        :param domain_count: The domain_count of this CertificateDetail.
        :type: int
        """
        self._domain_count = domain_count

    @property
    def wildcard_count(self):
        """Gets the wildcard_count of this CertificateDetail.

        证书可绑定泛域名个数。

        :return: The wildcard_count of this CertificateDetail.
        :rtype: int
        """
        return self._wildcard_count

    @wildcard_count.setter
    def wildcard_count(self, wildcard_count):
        """Sets the wildcard_count of this CertificateDetail.

        证书可绑定泛域名个数。

        :param wildcard_count: The wildcard_count of this CertificateDetail.
        :type: int
        """
        self._wildcard_count = wildcard_count

    @property
    def description(self):
        """Gets the description of this CertificateDetail.

        证书描述。

        :return: The description of this CertificateDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CertificateDetail.

        证书描述。

        :param description: The description of this CertificateDetail.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, CertificateDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
