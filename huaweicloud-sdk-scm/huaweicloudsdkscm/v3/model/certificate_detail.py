# coding: utf-8

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
        'sans': 'str',
        'signature_algorithm': 'str',
        'deploy_support': 'bool',
        'type': 'str',
        'brand': 'str',
        'expire_time': 'str',
        'domain_type': 'str',
        'validity_period': 'int',
        'status': 'str',
        'domain_count': 'int',
        'wildcard_count': 'int',
        'description': 'str',
        'domain_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'domain': 'domain',
        'sans': 'sans',
        'signature_algorithm': 'signature_algorithm',
        'deploy_support': 'deploy_support',
        'type': 'type',
        'brand': 'brand',
        'expire_time': 'expire_time',
        'domain_type': 'domain_type',
        'validity_period': 'validity_period',
        'status': 'status',
        'domain_count': 'domain_count',
        'wildcard_count': 'wildcard_count',
        'description': 'description',
        'domain_id': 'domain_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, domain=None, sans=None, signature_algorithm=None, deploy_support=None, type=None, brand=None, expire_time=None, domain_type=None, validity_period=None, status=None, domain_count=None, wildcard_count=None, description=None, domain_id=None, enterprise_project_id=None):
        r"""CertificateDetail

        The model defined in huaweicloud sdk

        :param id: 证书id。
        :type id: str
        :param name: 证书名称。
        :type name: str
        :param domain: 证书绑定的域名。
        :type domain: str
        :param sans: 多域名证书绑定的附加域名。
        :type sans: str
        :param signature_algorithm: 签名算法。
        :type signature_algorithm: str
        :param deploy_support: 是否支持部署。
        :type deploy_support: bool
        :param type: 证书类型。取值如下： DV_SSL_CERT、DV_SSL_CERT_BASIC、EV_SSL_CERT、 EV_SSL_CERT_PRO、OV_SSL_CERT、OV_SSL_CERT_PRO
        :type type: str
        :param brand: 证书品牌。取值如下：GLOBALSIGN、SYMANTEC、GEOTRUST、CFCA
        :type brand: str
        :param expire_time: 证书过期时间。
        :type expire_time: str
        :param domain_type: 域名类型。取值如下： - SINGLE_DOMAIN：单域名 - WILDCARD：通配符 - MULTI_DOMAIN：多域名
        :type domain_type: str
        :param validity_period: 证书有效期，按月为单位。[云证书管理服务提供了一种购买多年有效期证书的解决方案，这种多年有效期证书生效方式为多张有效期为1年的SSL证书叠加生效，例如：有效期为“3年”的证书实际包含3张有效期为1年且规格相同的SSL证书，在第一张证书到期前30天，系统自动以第一张证书的信息申请第二张证书，在第二张证书到期前30天，系统自动以第一张证书的信息申请第三张证书。](tag:hws)
        :type validity_period: int
        :param status: 证书状态，取值如下： - PAID：证书已支付；待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - CANCLEREVOKING：证书取消吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。 - CANCELSUPPLEMENTING：取消新增附加域名审核中。
        :type status: str
        :param domain_count: 证书可绑定域名个数。
        :type domain_count: int
        :param wildcard_count: 证书可绑定泛域名个数。
        :type wildcard_count: int
        :param description: 证书描述。
        :type description: str
        :param domain_id: 账号ID。
        :type domain_id: str
        :param enterprise_project_id: 企业项目ID，默认为“0”。 对于开通企业项目的用户，表示资源处于默认企业项目下。 对于未开通企业项目的用户，表示资源未处于企业项目下。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._domain = None
        self._sans = None
        self._signature_algorithm = None
        self._deploy_support = None
        self._type = None
        self._brand = None
        self._expire_time = None
        self._domain_type = None
        self._validity_period = None
        self._status = None
        self._domain_count = None
        self._wildcard_count = None
        self._description = None
        self._domain_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.domain = domain
        self.sans = sans
        self.signature_algorithm = signature_algorithm
        self.deploy_support = deploy_support
        self.type = type
        self.brand = brand
        self.expire_time = expire_time
        self.domain_type = domain_type
        self.validity_period = validity_period
        self.status = status
        self.domain_count = domain_count
        self.wildcard_count = wildcard_count
        self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this CertificateDetail.

        证书id。

        :return: The id of this CertificateDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CertificateDetail.

        证书id。

        :param id: The id of this CertificateDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CertificateDetail.

        证书名称。

        :return: The name of this CertificateDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CertificateDetail.

        证书名称。

        :param name: The name of this CertificateDetail.
        :type name: str
        """
        self._name = name

    @property
    def domain(self):
        r"""Gets the domain of this CertificateDetail.

        证书绑定的域名。

        :return: The domain of this CertificateDetail.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this CertificateDetail.

        证书绑定的域名。

        :param domain: The domain of this CertificateDetail.
        :type domain: str
        """
        self._domain = domain

    @property
    def sans(self):
        r"""Gets the sans of this CertificateDetail.

        多域名证书绑定的附加域名。

        :return: The sans of this CertificateDetail.
        :rtype: str
        """
        return self._sans

    @sans.setter
    def sans(self, sans):
        r"""Sets the sans of this CertificateDetail.

        多域名证书绑定的附加域名。

        :param sans: The sans of this CertificateDetail.
        :type sans: str
        """
        self._sans = sans

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this CertificateDetail.

        签名算法。

        :return: The signature_algorithm of this CertificateDetail.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this CertificateDetail.

        签名算法。

        :param signature_algorithm: The signature_algorithm of this CertificateDetail.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def deploy_support(self):
        r"""Gets the deploy_support of this CertificateDetail.

        是否支持部署。

        :return: The deploy_support of this CertificateDetail.
        :rtype: bool
        """
        return self._deploy_support

    @deploy_support.setter
    def deploy_support(self, deploy_support):
        r"""Sets the deploy_support of this CertificateDetail.

        是否支持部署。

        :param deploy_support: The deploy_support of this CertificateDetail.
        :type deploy_support: bool
        """
        self._deploy_support = deploy_support

    @property
    def type(self):
        r"""Gets the type of this CertificateDetail.

        证书类型。取值如下： DV_SSL_CERT、DV_SSL_CERT_BASIC、EV_SSL_CERT、 EV_SSL_CERT_PRO、OV_SSL_CERT、OV_SSL_CERT_PRO

        :return: The type of this CertificateDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CertificateDetail.

        证书类型。取值如下： DV_SSL_CERT、DV_SSL_CERT_BASIC、EV_SSL_CERT、 EV_SSL_CERT_PRO、OV_SSL_CERT、OV_SSL_CERT_PRO

        :param type: The type of this CertificateDetail.
        :type type: str
        """
        self._type = type

    @property
    def brand(self):
        r"""Gets the brand of this CertificateDetail.

        证书品牌。取值如下：GLOBALSIGN、SYMANTEC、GEOTRUST、CFCA

        :return: The brand of this CertificateDetail.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        r"""Sets the brand of this CertificateDetail.

        证书品牌。取值如下：GLOBALSIGN、SYMANTEC、GEOTRUST、CFCA

        :param brand: The brand of this CertificateDetail.
        :type brand: str
        """
        self._brand = brand

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CertificateDetail.

        证书过期时间。

        :return: The expire_time of this CertificateDetail.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CertificateDetail.

        证书过期时间。

        :param expire_time: The expire_time of this CertificateDetail.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def domain_type(self):
        r"""Gets the domain_type of this CertificateDetail.

        域名类型。取值如下： - SINGLE_DOMAIN：单域名 - WILDCARD：通配符 - MULTI_DOMAIN：多域名

        :return: The domain_type of this CertificateDetail.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this CertificateDetail.

        域名类型。取值如下： - SINGLE_DOMAIN：单域名 - WILDCARD：通配符 - MULTI_DOMAIN：多域名

        :param domain_type: The domain_type of this CertificateDetail.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def validity_period(self):
        r"""Gets the validity_period of this CertificateDetail.

        证书有效期，按月为单位。[云证书管理服务提供了一种购买多年有效期证书的解决方案，这种多年有效期证书生效方式为多张有效期为1年的SSL证书叠加生效，例如：有效期为“3年”的证书实际包含3张有效期为1年且规格相同的SSL证书，在第一张证书到期前30天，系统自动以第一张证书的信息申请第二张证书，在第二张证书到期前30天，系统自动以第一张证书的信息申请第三张证书。](tag:hws)

        :return: The validity_period of this CertificateDetail.
        :rtype: int
        """
        return self._validity_period

    @validity_period.setter
    def validity_period(self, validity_period):
        r"""Sets the validity_period of this CertificateDetail.

        证书有效期，按月为单位。[云证书管理服务提供了一种购买多年有效期证书的解决方案，这种多年有效期证书生效方式为多张有效期为1年的SSL证书叠加生效，例如：有效期为“3年”的证书实际包含3张有效期为1年且规格相同的SSL证书，在第一张证书到期前30天，系统自动以第一张证书的信息申请第二张证书，在第二张证书到期前30天，系统自动以第一张证书的信息申请第三张证书。](tag:hws)

        :param validity_period: The validity_period of this CertificateDetail.
        :type validity_period: int
        """
        self._validity_period = validity_period

    @property
    def status(self):
        r"""Gets the status of this CertificateDetail.

        证书状态，取值如下： - PAID：证书已支付；待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - CANCLEREVOKING：证书取消吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。 - CANCELSUPPLEMENTING：取消新增附加域名审核中。

        :return: The status of this CertificateDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CertificateDetail.

        证书状态，取值如下： - PAID：证书已支付；待申请证书。 - ISSUED：证书已签发。 - CHECKING：证书申请审核中。 - CANCELCHECKING：取消证书申请审核中。 - UNPASSED：证书申请未通过。 - EXPIRED：证书已过期。 - REVOKING：证书吊销申请审核中。 - CANCLEREVOKING：证书取消吊销申请审核中。 - REVOKED：证书已吊销。 - UPLOAD：证书托管中。 - SUPPLEMENTCHECKING：多域名证书新增附加域名审核中。 - CANCELSUPPLEMENTING：取消新增附加域名审核中。

        :param status: The status of this CertificateDetail.
        :type status: str
        """
        self._status = status

    @property
    def domain_count(self):
        r"""Gets the domain_count of this CertificateDetail.

        证书可绑定域名个数。

        :return: The domain_count of this CertificateDetail.
        :rtype: int
        """
        return self._domain_count

    @domain_count.setter
    def domain_count(self, domain_count):
        r"""Sets the domain_count of this CertificateDetail.

        证书可绑定域名个数。

        :param domain_count: The domain_count of this CertificateDetail.
        :type domain_count: int
        """
        self._domain_count = domain_count

    @property
    def wildcard_count(self):
        r"""Gets the wildcard_count of this CertificateDetail.

        证书可绑定泛域名个数。

        :return: The wildcard_count of this CertificateDetail.
        :rtype: int
        """
        return self._wildcard_count

    @wildcard_count.setter
    def wildcard_count(self, wildcard_count):
        r"""Sets the wildcard_count of this CertificateDetail.

        证书可绑定泛域名个数。

        :param wildcard_count: The wildcard_count of this CertificateDetail.
        :type wildcard_count: int
        """
        self._wildcard_count = wildcard_count

    @property
    def description(self):
        r"""Gets the description of this CertificateDetail.

        证书描述。

        :return: The description of this CertificateDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CertificateDetail.

        证书描述。

        :param description: The description of this CertificateDetail.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CertificateDetail.

        账号ID。

        :return: The domain_id of this CertificateDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CertificateDetail.

        账号ID。

        :param domain_id: The domain_id of this CertificateDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CertificateDetail.

        企业项目ID，默认为“0”。 对于开通企业项目的用户，表示资源处于默认企业项目下。 对于未开通企业项目的用户，表示资源未处于企业项目下。

        :return: The enterprise_project_id of this CertificateDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CertificateDetail.

        企业项目ID，默认为“0”。 对于开通企业项目的用户，表示资源处于默认企业项目下。 对于未开通企业项目的用户，表示资源未处于企业项目下。

        :param enterprise_project_id: The enterprise_project_id of this CertificateDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
