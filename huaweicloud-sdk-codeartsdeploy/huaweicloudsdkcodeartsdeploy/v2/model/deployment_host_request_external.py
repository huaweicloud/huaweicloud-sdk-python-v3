# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentHostRequestExternal:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'as_proxy': 'bool',
        'authorization': 'DeploymentHostAuthorizationBody',
        'host_name': 'str',
        'ip': 'str',
        'port': 'int',
        'proxy_host_id': 'str',
        'sync': 'bool',
        'install_icagent': 'bool'
    }

    attribute_map = {
        'as_proxy': 'as_proxy',
        'authorization': 'authorization',
        'host_name': 'host_name',
        'ip': 'ip',
        'port': 'port',
        'proxy_host_id': 'proxy_host_id',
        'sync': 'sync',
        'install_icagent': 'install_icagent'
    }

    def __init__(self, as_proxy=None, authorization=None, host_name=None, ip=None, port=None, proxy_host_id=None, sync=None, install_icagent=None):
        r"""DeploymentHostRequestExternal

        The model defined in huaweicloud sdk

        :param as_proxy: 是否为代理主机
        :type as_proxy: bool
        :param authorization: 
        :type authorization: :class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentHostAuthorizationBody`
        :param host_name: 主机名称
        :type host_name: str
        :param ip: 主机ip，如：161.17.101.12
        :type ip: str
        :param port: ssh端口，如：22
        :type port: int
        :param proxy_host_id: 代理主机id
        :type proxy_host_id: str
        :param sync: 是否同步主机信息
        :type sync: bool
        :param install_icagent: 是否安装icAgent
        :type install_icagent: bool
        """
        
        

        self._as_proxy = None
        self._authorization = None
        self._host_name = None
        self._ip = None
        self._port = None
        self._proxy_host_id = None
        self._sync = None
        self._install_icagent = None
        self.discriminator = None

        if as_proxy is not None:
            self.as_proxy = as_proxy
        if authorization is not None:
            self.authorization = authorization
        self.host_name = host_name
        self.ip = ip
        self.port = port
        if proxy_host_id is not None:
            self.proxy_host_id = proxy_host_id
        if sync is not None:
            self.sync = sync
        if install_icagent is not None:
            self.install_icagent = install_icagent

    @property
    def as_proxy(self):
        r"""Gets the as_proxy of this DeploymentHostRequestExternal.

        是否为代理主机

        :return: The as_proxy of this DeploymentHostRequestExternal.
        :rtype: bool
        """
        return self._as_proxy

    @as_proxy.setter
    def as_proxy(self, as_proxy):
        r"""Sets the as_proxy of this DeploymentHostRequestExternal.

        是否为代理主机

        :param as_proxy: The as_proxy of this DeploymentHostRequestExternal.
        :type as_proxy: bool
        """
        self._as_proxy = as_proxy

    @property
    def authorization(self):
        r"""Gets the authorization of this DeploymentHostRequestExternal.

        :return: The authorization of this DeploymentHostRequestExternal.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentHostAuthorizationBody`
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        r"""Sets the authorization of this DeploymentHostRequestExternal.

        :param authorization: The authorization of this DeploymentHostRequestExternal.
        :type authorization: :class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentHostAuthorizationBody`
        """
        self._authorization = authorization

    @property
    def host_name(self):
        r"""Gets the host_name of this DeploymentHostRequestExternal.

        主机名称

        :return: The host_name of this DeploymentHostRequestExternal.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this DeploymentHostRequestExternal.

        主机名称

        :param host_name: The host_name of this DeploymentHostRequestExternal.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def ip(self):
        r"""Gets the ip of this DeploymentHostRequestExternal.

        主机ip，如：161.17.101.12

        :return: The ip of this DeploymentHostRequestExternal.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this DeploymentHostRequestExternal.

        主机ip，如：161.17.101.12

        :param ip: The ip of this DeploymentHostRequestExternal.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this DeploymentHostRequestExternal.

        ssh端口，如：22

        :return: The port of this DeploymentHostRequestExternal.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this DeploymentHostRequestExternal.

        ssh端口，如：22

        :param port: The port of this DeploymentHostRequestExternal.
        :type port: int
        """
        self._port = port

    @property
    def proxy_host_id(self):
        r"""Gets the proxy_host_id of this DeploymentHostRequestExternal.

        代理主机id

        :return: The proxy_host_id of this DeploymentHostRequestExternal.
        :rtype: str
        """
        return self._proxy_host_id

    @proxy_host_id.setter
    def proxy_host_id(self, proxy_host_id):
        r"""Sets the proxy_host_id of this DeploymentHostRequestExternal.

        代理主机id

        :param proxy_host_id: The proxy_host_id of this DeploymentHostRequestExternal.
        :type proxy_host_id: str
        """
        self._proxy_host_id = proxy_host_id

    @property
    def sync(self):
        r"""Gets the sync of this DeploymentHostRequestExternal.

        是否同步主机信息

        :return: The sync of this DeploymentHostRequestExternal.
        :rtype: bool
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        r"""Sets the sync of this DeploymentHostRequestExternal.

        是否同步主机信息

        :param sync: The sync of this DeploymentHostRequestExternal.
        :type sync: bool
        """
        self._sync = sync

    @property
    def install_icagent(self):
        r"""Gets the install_icagent of this DeploymentHostRequestExternal.

        是否安装icAgent

        :return: The install_icagent of this DeploymentHostRequestExternal.
        :rtype: bool
        """
        return self._install_icagent

    @install_icagent.setter
    def install_icagent(self, install_icagent):
        r"""Sets the install_icagent of this DeploymentHostRequestExternal.

        是否安装icAgent

        :param install_icagent: The install_icagent of this DeploymentHostRequestExternal.
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
        if not isinstance(other, DeploymentHostRequestExternal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
