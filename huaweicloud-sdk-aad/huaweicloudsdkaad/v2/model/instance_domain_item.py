# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDomainItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'domain_name': 'str',
        'cname': 'str',
        'domain_status': 'str',
        'cc_status': 'int',
        'https_cert_status': 'int',
        'cert_name': 'str',
        'protocol_type': 'list[str]',
        'real_server_type': 'int',
        'real_servers': 'str',
        'waf_status': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'cname': 'cname',
        'domain_status': 'domain_status',
        'cc_status': 'cc_status',
        'https_cert_status': 'https_cert_status',
        'cert_name': 'cert_name',
        'protocol_type': 'protocol_type',
        'real_server_type': 'real_server_type',
        'real_servers': 'real_servers',
        'waf_status': 'waf_status'
    }

    def __init__(self, domain_id=None, domain_name=None, cname=None, domain_status=None, cc_status=None, https_cert_status=None, cert_name=None, protocol_type=None, real_server_type=None, real_servers=None, waf_status=None):
        r"""InstanceDomainItem

        The model defined in huaweicloud sdk

        :param domain_id: 域名ID
        :type domain_id: str
        :param domain_name: 域名
        :type domain_name: str
        :param cname: 域名cname
        :type cname: str
        :param domain_status: 域名状态 NORMAL &#x3D; &#39;0&#39;, FREEZE &#x3D; &#39;1&#39;
        :type domain_status: str
        :param cc_status: cc防护状态
        :type cc_status: int
        :param https_cert_status: 证书状态：1---已上传  2---未上传
        :type https_cert_status: int
        :param cert_name: 证书名称
        :type cert_name: str
        :param protocol_type: 域名协议
        :type protocol_type: list[str]
        :param real_server_type: 源站类型
        :type real_server_type: int
        :param real_servers: 源站
        :type real_servers: str
        :param waf_status: waf防护状态
        :type waf_status: int
        """
        
        

        self._domain_id = None
        self._domain_name = None
        self._cname = None
        self._domain_status = None
        self._cc_status = None
        self._https_cert_status = None
        self._cert_name = None
        self._protocol_type = None
        self._real_server_type = None
        self._real_servers = None
        self._waf_status = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if cname is not None:
            self.cname = cname
        if domain_status is not None:
            self.domain_status = domain_status
        if cc_status is not None:
            self.cc_status = cc_status
        if https_cert_status is not None:
            self.https_cert_status = https_cert_status
        if cert_name is not None:
            self.cert_name = cert_name
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if real_server_type is not None:
            self.real_server_type = real_server_type
        if real_servers is not None:
            self.real_servers = real_servers
        if waf_status is not None:
            self.waf_status = waf_status

    @property
    def domain_id(self):
        r"""Gets the domain_id of this InstanceDomainItem.

        域名ID

        :return: The domain_id of this InstanceDomainItem.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this InstanceDomainItem.

        域名ID

        :param domain_id: The domain_id of this InstanceDomainItem.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this InstanceDomainItem.

        域名

        :return: The domain_name of this InstanceDomainItem.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this InstanceDomainItem.

        域名

        :param domain_name: The domain_name of this InstanceDomainItem.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def cname(self):
        r"""Gets the cname of this InstanceDomainItem.

        域名cname

        :return: The cname of this InstanceDomainItem.
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        r"""Sets the cname of this InstanceDomainItem.

        域名cname

        :param cname: The cname of this InstanceDomainItem.
        :type cname: str
        """
        self._cname = cname

    @property
    def domain_status(self):
        r"""Gets the domain_status of this InstanceDomainItem.

        域名状态 NORMAL = '0', FREEZE = '1'

        :return: The domain_status of this InstanceDomainItem.
        :rtype: str
        """
        return self._domain_status

    @domain_status.setter
    def domain_status(self, domain_status):
        r"""Sets the domain_status of this InstanceDomainItem.

        域名状态 NORMAL = '0', FREEZE = '1'

        :param domain_status: The domain_status of this InstanceDomainItem.
        :type domain_status: str
        """
        self._domain_status = domain_status

    @property
    def cc_status(self):
        r"""Gets the cc_status of this InstanceDomainItem.

        cc防护状态

        :return: The cc_status of this InstanceDomainItem.
        :rtype: int
        """
        return self._cc_status

    @cc_status.setter
    def cc_status(self, cc_status):
        r"""Sets the cc_status of this InstanceDomainItem.

        cc防护状态

        :param cc_status: The cc_status of this InstanceDomainItem.
        :type cc_status: int
        """
        self._cc_status = cc_status

    @property
    def https_cert_status(self):
        r"""Gets the https_cert_status of this InstanceDomainItem.

        证书状态：1---已上传  2---未上传

        :return: The https_cert_status of this InstanceDomainItem.
        :rtype: int
        """
        return self._https_cert_status

    @https_cert_status.setter
    def https_cert_status(self, https_cert_status):
        r"""Sets the https_cert_status of this InstanceDomainItem.

        证书状态：1---已上传  2---未上传

        :param https_cert_status: The https_cert_status of this InstanceDomainItem.
        :type https_cert_status: int
        """
        self._https_cert_status = https_cert_status

    @property
    def cert_name(self):
        r"""Gets the cert_name of this InstanceDomainItem.

        证书名称

        :return: The cert_name of this InstanceDomainItem.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this InstanceDomainItem.

        证书名称

        :param cert_name: The cert_name of this InstanceDomainItem.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def protocol_type(self):
        r"""Gets the protocol_type of this InstanceDomainItem.

        域名协议

        :return: The protocol_type of this InstanceDomainItem.
        :rtype: list[str]
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        r"""Sets the protocol_type of this InstanceDomainItem.

        域名协议

        :param protocol_type: The protocol_type of this InstanceDomainItem.
        :type protocol_type: list[str]
        """
        self._protocol_type = protocol_type

    @property
    def real_server_type(self):
        r"""Gets the real_server_type of this InstanceDomainItem.

        源站类型

        :return: The real_server_type of this InstanceDomainItem.
        :rtype: int
        """
        return self._real_server_type

    @real_server_type.setter
    def real_server_type(self, real_server_type):
        r"""Sets the real_server_type of this InstanceDomainItem.

        源站类型

        :param real_server_type: The real_server_type of this InstanceDomainItem.
        :type real_server_type: int
        """
        self._real_server_type = real_server_type

    @property
    def real_servers(self):
        r"""Gets the real_servers of this InstanceDomainItem.

        源站

        :return: The real_servers of this InstanceDomainItem.
        :rtype: str
        """
        return self._real_servers

    @real_servers.setter
    def real_servers(self, real_servers):
        r"""Sets the real_servers of this InstanceDomainItem.

        源站

        :param real_servers: The real_servers of this InstanceDomainItem.
        :type real_servers: str
        """
        self._real_servers = real_servers

    @property
    def waf_status(self):
        r"""Gets the waf_status of this InstanceDomainItem.

        waf防护状态

        :return: The waf_status of this InstanceDomainItem.
        :rtype: int
        """
        return self._waf_status

    @waf_status.setter
    def waf_status(self, waf_status):
        r"""Sets the waf_status of this InstanceDomainItem.

        waf防护状态

        :param waf_status: The waf_status of this InstanceDomainItem.
        :type waf_status: int
        """
        self._waf_status = waf_status

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
        if not isinstance(other, InstanceDomainItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
