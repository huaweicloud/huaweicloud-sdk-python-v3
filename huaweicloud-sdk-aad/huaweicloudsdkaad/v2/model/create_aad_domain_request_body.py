# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAadDomainRequestBody:

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
        'enterprise_project_id': 'str',
        'ips': 'list[str]',
        'real_server_type': 'int',
        'port_http': 'list[int]',
        'port_https': 'list[int]',
        'real_server': 'str',
        'overseas_type': 'str',
        'cert_name': 'str',
        'waf_switch': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'ips': 'ips',
        'real_server_type': 'real_server_type',
        'port_http': 'port_http',
        'port_https': 'port_https',
        'real_server': 'real_server',
        'overseas_type': 'overseas_type',
        'cert_name': 'cert_name',
        'waf_switch': 'waf_switch'
    }

    def __init__(self, domain_name=None, enterprise_project_id=None, ips=None, real_server_type=None, port_http=None, port_https=None, real_server=None, overseas_type=None, cert_name=None, waf_switch=None):
        r"""CreateAadDomainRequestBody

        The model defined in huaweicloud sdk

        :param domain_name: 域名
        :type domain_name: str
        :param enterprise_project_id: 企业项目id，与接入的高防实例所属企业项目保持一致。可在华为云EPS服务中查看企业项目id，default企业项目id为\&quot;0\&quot;。
        :type enterprise_project_id: str
        :param ips: 高防实例ip列表。多个高防实例ip必须属于同一企业项目。
        :type ips: list[str]
        :param real_server_type: 源站类型。 0 - 源站IP， 1 - 源站域名。
        :type real_server_type: int
        :param port_http: HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可在控制台查看。
        :type port_http: list[int]
        :param port_https: HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可在控制台查看。
        :type port_https: list[int]
        :param real_server: 源站（源站ip/源站域名）
        :type real_server: str
        :param overseas_type: 防护区域，0-大陆，1-海外
        :type overseas_type: str
        :param cert_name: 证书名称（必须是已经存在的证书）
        :type cert_name: str
        :param waf_switch: 开启0，关闭1
        :type waf_switch: str
        """
        
        

        self._domain_name = None
        self._enterprise_project_id = None
        self._ips = None
        self._real_server_type = None
        self._port_http = None
        self._port_https = None
        self._real_server = None
        self._overseas_type = None
        self._cert_name = None
        self._waf_switch = None
        self.discriminator = None

        self.domain_name = domain_name
        self.enterprise_project_id = enterprise_project_id
        self.ips = ips
        self.real_server_type = real_server_type
        self.port_http = port_http
        if port_https is not None:
            self.port_https = port_https
        self.real_server = real_server
        self.overseas_type = overseas_type
        if cert_name is not None:
            self.cert_name = cert_name
        if waf_switch is not None:
            self.waf_switch = waf_switch

    @property
    def domain_name(self):
        r"""Gets the domain_name of this CreateAadDomainRequestBody.

        域名

        :return: The domain_name of this CreateAadDomainRequestBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this CreateAadDomainRequestBody.

        域名

        :param domain_name: The domain_name of this CreateAadDomainRequestBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateAadDomainRequestBody.

        企业项目id，与接入的高防实例所属企业项目保持一致。可在华为云EPS服务中查看企业项目id，default企业项目id为\"0\"。

        :return: The enterprise_project_id of this CreateAadDomainRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateAadDomainRequestBody.

        企业项目id，与接入的高防实例所属企业项目保持一致。可在华为云EPS服务中查看企业项目id，default企业项目id为\"0\"。

        :param enterprise_project_id: The enterprise_project_id of this CreateAadDomainRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ips(self):
        r"""Gets the ips of this CreateAadDomainRequestBody.

        高防实例ip列表。多个高防实例ip必须属于同一企业项目。

        :return: The ips of this CreateAadDomainRequestBody.
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        r"""Sets the ips of this CreateAadDomainRequestBody.

        高防实例ip列表。多个高防实例ip必须属于同一企业项目。

        :param ips: The ips of this CreateAadDomainRequestBody.
        :type ips: list[str]
        """
        self._ips = ips

    @property
    def real_server_type(self):
        r"""Gets the real_server_type of this CreateAadDomainRequestBody.

        源站类型。 0 - 源站IP， 1 - 源站域名。

        :return: The real_server_type of this CreateAadDomainRequestBody.
        :rtype: int
        """
        return self._real_server_type

    @real_server_type.setter
    def real_server_type(self, real_server_type):
        r"""Sets the real_server_type of this CreateAadDomainRequestBody.

        源站类型。 0 - 源站IP， 1 - 源站域名。

        :param real_server_type: The real_server_type of this CreateAadDomainRequestBody.
        :type real_server_type: int
        """
        self._real_server_type = real_server_type

    @property
    def port_http(self):
        r"""Gets the port_http of this CreateAadDomainRequestBody.

        HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可在控制台查看。

        :return: The port_http of this CreateAadDomainRequestBody.
        :rtype: list[int]
        """
        return self._port_http

    @port_http.setter
    def port_http(self, port_http):
        r"""Sets the port_http of this CreateAadDomainRequestBody.

        HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可在控制台查看。

        :param port_http: The port_http of this CreateAadDomainRequestBody.
        :type port_http: list[int]
        """
        self._port_http = port_http

    @property
    def port_https(self):
        r"""Gets the port_https of this CreateAadDomainRequestBody.

        HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可在控制台查看。

        :return: The port_https of this CreateAadDomainRequestBody.
        :rtype: list[int]
        """
        return self._port_https

    @port_https.setter
    def port_https(self, port_https):
        r"""Sets the port_https of this CreateAadDomainRequestBody.

        HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可在控制台查看。

        :param port_https: The port_https of this CreateAadDomainRequestBody.
        :type port_https: list[int]
        """
        self._port_https = port_https

    @property
    def real_server(self):
        r"""Gets the real_server of this CreateAadDomainRequestBody.

        源站（源站ip/源站域名）

        :return: The real_server of this CreateAadDomainRequestBody.
        :rtype: str
        """
        return self._real_server

    @real_server.setter
    def real_server(self, real_server):
        r"""Sets the real_server of this CreateAadDomainRequestBody.

        源站（源站ip/源站域名）

        :param real_server: The real_server of this CreateAadDomainRequestBody.
        :type real_server: str
        """
        self._real_server = real_server

    @property
    def overseas_type(self):
        r"""Gets the overseas_type of this CreateAadDomainRequestBody.

        防护区域，0-大陆，1-海外

        :return: The overseas_type of this CreateAadDomainRequestBody.
        :rtype: str
        """
        return self._overseas_type

    @overseas_type.setter
    def overseas_type(self, overseas_type):
        r"""Sets the overseas_type of this CreateAadDomainRequestBody.

        防护区域，0-大陆，1-海外

        :param overseas_type: The overseas_type of this CreateAadDomainRequestBody.
        :type overseas_type: str
        """
        self._overseas_type = overseas_type

    @property
    def cert_name(self):
        r"""Gets the cert_name of this CreateAadDomainRequestBody.

        证书名称（必须是已经存在的证书）

        :return: The cert_name of this CreateAadDomainRequestBody.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this CreateAadDomainRequestBody.

        证书名称（必须是已经存在的证书）

        :param cert_name: The cert_name of this CreateAadDomainRequestBody.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def waf_switch(self):
        r"""Gets the waf_switch of this CreateAadDomainRequestBody.

        开启0，关闭1

        :return: The waf_switch of this CreateAadDomainRequestBody.
        :rtype: str
        """
        return self._waf_switch

    @waf_switch.setter
    def waf_switch(self, waf_switch):
        r"""Sets the waf_switch of this CreateAadDomainRequestBody.

        开启0，关闭1

        :param waf_switch: The waf_switch of this CreateAadDomainRequestBody.
        :type waf_switch: str
        """
        self._waf_switch = waf_switch

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
        if not isinstance(other, CreateAadDomainRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
