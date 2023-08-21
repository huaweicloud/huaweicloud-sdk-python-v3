# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCdnDomainResponseBody:

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
        'domain_status': 'str',
        'domain_id': 'str',
        'certificate_id': 'str',
        'service_area': 'str',
        'ipv6_accelerate': 'int',
        'business_type': 'str',
        'https_status': 'int',
        'force_redirect': 'int',
        'extended_tags': 'CdnDomainTags',
        'is_added': 'bool'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'domain_status': 'domain_status',
        'domain_id': 'domain_id',
        'certificate_id': 'certificate_id',
        'service_area': 'service_area',
        'ipv6_accelerate': 'ipv6_accelerate',
        'business_type': 'business_type',
        'https_status': 'https_status',
        'force_redirect': 'force_redirect',
        'extended_tags': 'extended_tags',
        'is_added': 'is_added'
    }

    def __init__(self, domain_name=None, domain_status=None, domain_id=None, certificate_id=None, service_area=None, ipv6_accelerate=None, business_type=None, https_status=None, force_redirect=None, extended_tags=None, is_added=None):
        """ShowCdnDomainResponseBody

        The model defined in huaweicloud sdk

        :param domain_name: 域名
        :type domain_name: str
        :param domain_status: 加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。
        :type domain_status: str
        :param domain_id: 域名id
        :type domain_id: str
        :param certificate_id: 域名使用的证书id
        :type certificate_id: str
        :param service_area: 域名业务区域
        :type service_area: str
        :param ipv6_accelerate: 是否开启ipv6加速：0关闭/1开启
        :type ipv6_accelerate: int
        :param business_type: 域名业务类型。取值意义： - web表示“网站加速” - download表示“文件下载加速” - video表示“点播加速” - wholeSite表示“全站加速”
        :type business_type: str
        :param https_status: 是否启用https：0关闭/1开启
        :type https_status: int
        :param force_redirect: 强制重定向：0不开启重定向/1强制重定向为HTTP/2强制重定向为HTTPS
        :type force_redirect: int
        :param extended_tags: 
        :type extended_tags: :class:`huaweicloudsdkedgesec.v1.CdnDomainTags`
        :param is_added: 是否为waf防护域名
        :type is_added: bool
        """
        
        

        self._domain_name = None
        self._domain_status = None
        self._domain_id = None
        self._certificate_id = None
        self._service_area = None
        self._ipv6_accelerate = None
        self._business_type = None
        self._https_status = None
        self._force_redirect = None
        self._extended_tags = None
        self._is_added = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if domain_status is not None:
            self.domain_status = domain_status
        if domain_id is not None:
            self.domain_id = domain_id
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if service_area is not None:
            self.service_area = service_area
        if ipv6_accelerate is not None:
            self.ipv6_accelerate = ipv6_accelerate
        if business_type is not None:
            self.business_type = business_type
        if https_status is not None:
            self.https_status = https_status
        if force_redirect is not None:
            self.force_redirect = force_redirect
        if extended_tags is not None:
            self.extended_tags = extended_tags
        if is_added is not None:
            self.is_added = is_added

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowCdnDomainResponseBody.

        域名

        :return: The domain_name of this ShowCdnDomainResponseBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowCdnDomainResponseBody.

        域名

        :param domain_name: The domain_name of this ShowCdnDomainResponseBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def domain_status(self):
        """Gets the domain_status of this ShowCdnDomainResponseBody.

        加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。

        :return: The domain_status of this ShowCdnDomainResponseBody.
        :rtype: str
        """
        return self._domain_status

    @domain_status.setter
    def domain_status(self, domain_status):
        """Sets the domain_status of this ShowCdnDomainResponseBody.

        加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。

        :param domain_status: The domain_status of this ShowCdnDomainResponseBody.
        :type domain_status: str
        """
        self._domain_status = domain_status

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowCdnDomainResponseBody.

        域名id

        :return: The domain_id of this ShowCdnDomainResponseBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowCdnDomainResponseBody.

        域名id

        :param domain_id: The domain_id of this ShowCdnDomainResponseBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this ShowCdnDomainResponseBody.

        域名使用的证书id

        :return: The certificate_id of this ShowCdnDomainResponseBody.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this ShowCdnDomainResponseBody.

        域名使用的证书id

        :param certificate_id: The certificate_id of this ShowCdnDomainResponseBody.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def service_area(self):
        """Gets the service_area of this ShowCdnDomainResponseBody.

        域名业务区域

        :return: The service_area of this ShowCdnDomainResponseBody.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this ShowCdnDomainResponseBody.

        域名业务区域

        :param service_area: The service_area of this ShowCdnDomainResponseBody.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def ipv6_accelerate(self):
        """Gets the ipv6_accelerate of this ShowCdnDomainResponseBody.

        是否开启ipv6加速：0关闭/1开启

        :return: The ipv6_accelerate of this ShowCdnDomainResponseBody.
        :rtype: int
        """
        return self._ipv6_accelerate

    @ipv6_accelerate.setter
    def ipv6_accelerate(self, ipv6_accelerate):
        """Sets the ipv6_accelerate of this ShowCdnDomainResponseBody.

        是否开启ipv6加速：0关闭/1开启

        :param ipv6_accelerate: The ipv6_accelerate of this ShowCdnDomainResponseBody.
        :type ipv6_accelerate: int
        """
        self._ipv6_accelerate = ipv6_accelerate

    @property
    def business_type(self):
        """Gets the business_type of this ShowCdnDomainResponseBody.

        域名业务类型。取值意义： - web表示“网站加速” - download表示“文件下载加速” - video表示“点播加速” - wholeSite表示“全站加速”

        :return: The business_type of this ShowCdnDomainResponseBody.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this ShowCdnDomainResponseBody.

        域名业务类型。取值意义： - web表示“网站加速” - download表示“文件下载加速” - video表示“点播加速” - wholeSite表示“全站加速”

        :param business_type: The business_type of this ShowCdnDomainResponseBody.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def https_status(self):
        """Gets the https_status of this ShowCdnDomainResponseBody.

        是否启用https：0关闭/1开启

        :return: The https_status of this ShowCdnDomainResponseBody.
        :rtype: int
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        """Sets the https_status of this ShowCdnDomainResponseBody.

        是否启用https：0关闭/1开启

        :param https_status: The https_status of this ShowCdnDomainResponseBody.
        :type https_status: int
        """
        self._https_status = https_status

    @property
    def force_redirect(self):
        """Gets the force_redirect of this ShowCdnDomainResponseBody.

        强制重定向：0不开启重定向/1强制重定向为HTTP/2强制重定向为HTTPS

        :return: The force_redirect of this ShowCdnDomainResponseBody.
        :rtype: int
        """
        return self._force_redirect

    @force_redirect.setter
    def force_redirect(self, force_redirect):
        """Sets the force_redirect of this ShowCdnDomainResponseBody.

        强制重定向：0不开启重定向/1强制重定向为HTTP/2强制重定向为HTTPS

        :param force_redirect: The force_redirect of this ShowCdnDomainResponseBody.
        :type force_redirect: int
        """
        self._force_redirect = force_redirect

    @property
    def extended_tags(self):
        """Gets the extended_tags of this ShowCdnDomainResponseBody.

        :return: The extended_tags of this ShowCdnDomainResponseBody.
        :rtype: :class:`huaweicloudsdkedgesec.v1.CdnDomainTags`
        """
        return self._extended_tags

    @extended_tags.setter
    def extended_tags(self, extended_tags):
        """Sets the extended_tags of this ShowCdnDomainResponseBody.

        :param extended_tags: The extended_tags of this ShowCdnDomainResponseBody.
        :type extended_tags: :class:`huaweicloudsdkedgesec.v1.CdnDomainTags`
        """
        self._extended_tags = extended_tags

    @property
    def is_added(self):
        """Gets the is_added of this ShowCdnDomainResponseBody.

        是否为waf防护域名

        :return: The is_added of this ShowCdnDomainResponseBody.
        :rtype: bool
        """
        return self._is_added

    @is_added.setter
    def is_added(self, is_added):
        """Sets the is_added of this ShowCdnDomainResponseBody.

        是否为waf防护域名

        :param is_added: The is_added of this ShowCdnDomainResponseBody.
        :type is_added: bool
        """
        self._is_added = is_added

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
        if not isinstance(other, ShowCdnDomainResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
