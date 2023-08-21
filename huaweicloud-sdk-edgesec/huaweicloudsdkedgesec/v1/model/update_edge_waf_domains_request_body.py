# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEdgeWafDomainsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_status': 'int',
        'access_status': 'int',
        'web_tag': 'str',
        'description': 'str',
        'certificate_id': 'str',
        'enterprise_project_id': 'str',
        'tls': 'str',
        'cipher': 'str',
        'block_page': 'WafBlockPage',
        'traffic_mark': 'WafTrafficMark',
        'flag': 'Flag',
        'extend': 'dict(str, str)'
    }

    attribute_map = {
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'web_tag': 'web_tag',
        'description': 'description',
        'certificate_id': 'certificate_id',
        'enterprise_project_id': 'enterprise_project_id',
        'tls': 'tls',
        'cipher': 'cipher',
        'block_page': 'block_page',
        'traffic_mark': 'traffic_mark',
        'flag': 'flag',
        'extend': 'extend'
    }

    def __init__(self, protect_status=None, access_status=None, web_tag=None, description=None, certificate_id=None, enterprise_project_id=None, tls=None, cipher=None, block_page=None, traffic_mark=None, flag=None, extend=None):
        """UpdateEdgeWafDomainsRequestBody

        The model defined in huaweicloud sdk

        :param protect_status: 防护状态
        :type protect_status: int
        :param access_status: 接入状态
        :type access_status: int
        :param web_tag: 域名名称
        :type web_tag: str
        :param description: 域名描述
        :type description: str
        :param certificate_id: 证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数   - 查询证书列表接口未开放时，从边缘安全控制台-&gt;边缘WAF-&gt;证书管理获取
        :type certificate_id: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param tls: 配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对外协议为https时才有tls参数
        :type tls: str
        :param cipher: 对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM
        :type cipher: str
        :param block_page: 
        :type block_page: :class:`huaweicloudsdkedgesec.v1.WafBlockPage`
        :param traffic_mark: 
        :type traffic_mark: :class:`huaweicloudsdkedgesec.v1.WafTrafficMark`
        :param flag: 
        :type flag: :class:`huaweicloudsdkedgesec.v1.Flag`
        :param extend: 域名可扩展字段
        :type extend: dict(str, str)
        """
        
        

        self._protect_status = None
        self._access_status = None
        self._web_tag = None
        self._description = None
        self._certificate_id = None
        self._enterprise_project_id = None
        self._tls = None
        self._cipher = None
        self._block_page = None
        self._traffic_mark = None
        self._flag = None
        self._extend = None
        self.discriminator = None

        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if web_tag is not None:
            self.web_tag = web_tag
        if description is not None:
            self.description = description
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tls is not None:
            self.tls = tls
        if cipher is not None:
            self.cipher = cipher
        if block_page is not None:
            self.block_page = block_page
        if traffic_mark is not None:
            self.traffic_mark = traffic_mark
        if flag is not None:
            self.flag = flag
        if extend is not None:
            self.extend = extend

    @property
    def protect_status(self):
        """Gets the protect_status of this UpdateEdgeWafDomainsRequestBody.

        防护状态

        :return: The protect_status of this UpdateEdgeWafDomainsRequestBody.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this UpdateEdgeWafDomainsRequestBody.

        防护状态

        :param protect_status: The protect_status of this UpdateEdgeWafDomainsRequestBody.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this UpdateEdgeWafDomainsRequestBody.

        接入状态

        :return: The access_status of this UpdateEdgeWafDomainsRequestBody.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this UpdateEdgeWafDomainsRequestBody.

        接入状态

        :param access_status: The access_status of this UpdateEdgeWafDomainsRequestBody.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def web_tag(self):
        """Gets the web_tag of this UpdateEdgeWafDomainsRequestBody.

        域名名称

        :return: The web_tag of this UpdateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this UpdateEdgeWafDomainsRequestBody.

        域名名称

        :param web_tag: The web_tag of this UpdateEdgeWafDomainsRequestBody.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def description(self):
        """Gets the description of this UpdateEdgeWafDomainsRequestBody.

        域名描述

        :return: The description of this UpdateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateEdgeWafDomainsRequestBody.

        域名描述

        :param description: The description of this UpdateEdgeWafDomainsRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def certificate_id(self):
        """Gets the certificate_id of this UpdateEdgeWafDomainsRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数   - 查询证书列表接口未开放时，从边缘安全控制台->边缘WAF->证书管理获取

        :return: The certificate_id of this UpdateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this UpdateEdgeWafDomainsRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数   - 查询证书列表接口未开放时，从边缘安全控制台->边缘WAF->证书管理获取

        :param certificate_id: The certificate_id of this UpdateEdgeWafDomainsRequestBody.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this UpdateEdgeWafDomainsRequestBody.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this UpdateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this UpdateEdgeWafDomainsRequestBody.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this UpdateEdgeWafDomainsRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tls(self):
        """Gets the tls of this UpdateEdgeWafDomainsRequestBody.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对外协议为https时才有tls参数

        :return: The tls of this UpdateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this UpdateEdgeWafDomainsRequestBody.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对外协议为https时才有tls参数

        :param tls: The tls of this UpdateEdgeWafDomainsRequestBody.
        :type tls: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this UpdateEdgeWafDomainsRequestBody.

        对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :return: The cipher of this UpdateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this UpdateEdgeWafDomainsRequestBody.

        对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :param cipher: The cipher of this UpdateEdgeWafDomainsRequestBody.
        :type cipher: str
        """
        self._cipher = cipher

    @property
    def block_page(self):
        """Gets the block_page of this UpdateEdgeWafDomainsRequestBody.

        :return: The block_page of this UpdateEdgeWafDomainsRequestBody.
        :rtype: :class:`huaweicloudsdkedgesec.v1.WafBlockPage`
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        """Sets the block_page of this UpdateEdgeWafDomainsRequestBody.

        :param block_page: The block_page of this UpdateEdgeWafDomainsRequestBody.
        :type block_page: :class:`huaweicloudsdkedgesec.v1.WafBlockPage`
        """
        self._block_page = block_page

    @property
    def traffic_mark(self):
        """Gets the traffic_mark of this UpdateEdgeWafDomainsRequestBody.

        :return: The traffic_mark of this UpdateEdgeWafDomainsRequestBody.
        :rtype: :class:`huaweicloudsdkedgesec.v1.WafTrafficMark`
        """
        return self._traffic_mark

    @traffic_mark.setter
    def traffic_mark(self, traffic_mark):
        """Sets the traffic_mark of this UpdateEdgeWafDomainsRequestBody.

        :param traffic_mark: The traffic_mark of this UpdateEdgeWafDomainsRequestBody.
        :type traffic_mark: :class:`huaweicloudsdkedgesec.v1.WafTrafficMark`
        """
        self._traffic_mark = traffic_mark

    @property
    def flag(self):
        """Gets the flag of this UpdateEdgeWafDomainsRequestBody.

        :return: The flag of this UpdateEdgeWafDomainsRequestBody.
        :rtype: :class:`huaweicloudsdkedgesec.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this UpdateEdgeWafDomainsRequestBody.

        :param flag: The flag of this UpdateEdgeWafDomainsRequestBody.
        :type flag: :class:`huaweicloudsdkedgesec.v1.Flag`
        """
        self._flag = flag

    @property
    def extend(self):
        """Gets the extend of this UpdateEdgeWafDomainsRequestBody.

        域名可扩展字段

        :return: The extend of this UpdateEdgeWafDomainsRequestBody.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this UpdateEdgeWafDomainsRequestBody.

        域名可扩展字段

        :param extend: The extend of this UpdateEdgeWafDomainsRequestBody.
        :type extend: dict(str, str)
        """
        self._extend = extend

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
        if not isinstance(other, UpdateEdgeWafDomainsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
