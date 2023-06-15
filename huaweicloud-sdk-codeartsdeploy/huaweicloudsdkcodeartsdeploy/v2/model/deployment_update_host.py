# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentUpdateHost:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'ip': 'str',
        'port': 'int',
        'as_proxy': 'bool',
        'proxy_host_id': 'str',
        'authorization': 'DeploymentHostAuthorizationBody',
        'install_icagent': 'bool'
    }

    attribute_map = {
        'host_name': 'host_name',
        'ip': 'ip',
        'port': 'port',
        'as_proxy': 'as_proxy',
        'proxy_host_id': 'proxy_host_id',
        'authorization': 'authorization',
        'install_icagent': 'install_icagent'
    }

    def __init__(self, host_name=None, ip=None, port=None, as_proxy=None, proxy_host_id=None, authorization=None, install_icagent=None):
        """DeploymentUpdateHost

        The model defined in huaweicloud sdk

        :param host_name: 主机名称
        :type host_name: str
        :param ip: IP，请输入弹性ip格式：161.17.101.12
        :type ip: str
        :param port: ssh端口，如：22
        :type port: int
        :param as_proxy: 是否为代理机
        :type as_proxy: bool
        :param proxy_host_id: 代理机id
        :type proxy_host_id: str
        :param authorization: 
        :type authorization: :class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentHostAuthorizationBody`
        :param install_icagent: 免费启用应用运维服务（AOM），提供指标监控、日志查询、告警功能（自动安装数据采集器 ICAgent，仅支持华为云linux主机）
        :type install_icagent: bool
        """
        
        

        self._host_name = None
        self._ip = None
        self._port = None
        self._as_proxy = None
        self._proxy_host_id = None
        self._authorization = None
        self._install_icagent = None
        self.discriminator = None

        self.host_name = host_name
        self.ip = ip
        self.port = port
        self.as_proxy = as_proxy
        if proxy_host_id is not None:
            self.proxy_host_id = proxy_host_id
        self.authorization = authorization
        if install_icagent is not None:
            self.install_icagent = install_icagent

    @property
    def host_name(self):
        """Gets the host_name of this DeploymentUpdateHost.

        主机名称

        :return: The host_name of this DeploymentUpdateHost.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this DeploymentUpdateHost.

        主机名称

        :param host_name: The host_name of this DeploymentUpdateHost.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def ip(self):
        """Gets the ip of this DeploymentUpdateHost.

        IP，请输入弹性ip格式：161.17.101.12

        :return: The ip of this DeploymentUpdateHost.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this DeploymentUpdateHost.

        IP，请输入弹性ip格式：161.17.101.12

        :param ip: The ip of this DeploymentUpdateHost.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this DeploymentUpdateHost.

        ssh端口，如：22

        :return: The port of this DeploymentUpdateHost.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DeploymentUpdateHost.

        ssh端口，如：22

        :param port: The port of this DeploymentUpdateHost.
        :type port: int
        """
        self._port = port

    @property
    def as_proxy(self):
        """Gets the as_proxy of this DeploymentUpdateHost.

        是否为代理机

        :return: The as_proxy of this DeploymentUpdateHost.
        :rtype: bool
        """
        return self._as_proxy

    @as_proxy.setter
    def as_proxy(self, as_proxy):
        """Sets the as_proxy of this DeploymentUpdateHost.

        是否为代理机

        :param as_proxy: The as_proxy of this DeploymentUpdateHost.
        :type as_proxy: bool
        """
        self._as_proxy = as_proxy

    @property
    def proxy_host_id(self):
        """Gets the proxy_host_id of this DeploymentUpdateHost.

        代理机id

        :return: The proxy_host_id of this DeploymentUpdateHost.
        :rtype: str
        """
        return self._proxy_host_id

    @proxy_host_id.setter
    def proxy_host_id(self, proxy_host_id):
        """Sets the proxy_host_id of this DeploymentUpdateHost.

        代理机id

        :param proxy_host_id: The proxy_host_id of this DeploymentUpdateHost.
        :type proxy_host_id: str
        """
        self._proxy_host_id = proxy_host_id

    @property
    def authorization(self):
        """Gets the authorization of this DeploymentUpdateHost.

        :return: The authorization of this DeploymentUpdateHost.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentHostAuthorizationBody`
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this DeploymentUpdateHost.

        :param authorization: The authorization of this DeploymentUpdateHost.
        :type authorization: :class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentHostAuthorizationBody`
        """
        self._authorization = authorization

    @property
    def install_icagent(self):
        """Gets the install_icagent of this DeploymentUpdateHost.

        免费启用应用运维服务（AOM），提供指标监控、日志查询、告警功能（自动安装数据采集器 ICAgent，仅支持华为云linux主机）

        :return: The install_icagent of this DeploymentUpdateHost.
        :rtype: bool
        """
        return self._install_icagent

    @install_icagent.setter
    def install_icagent(self, install_icagent):
        """Sets the install_icagent of this DeploymentUpdateHost.

        免费启用应用运维服务（AOM），提供指标监控、日志查询、告警功能（自动安装数据采集器 ICAgent，仅支持华为云linux主机）

        :param install_icagent: The install_icagent of this DeploymentUpdateHost.
        :type install_icagent: bool
        """
        self._install_icagent = install_icagent

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
        if not isinstance(other, DeploymentUpdateHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
