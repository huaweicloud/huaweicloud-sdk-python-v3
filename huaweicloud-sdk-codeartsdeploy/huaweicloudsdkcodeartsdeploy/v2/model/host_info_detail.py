# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostInfoDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'ip': 'str',
        'os': 'str',
        'port': 'int',
        'authorization': 'HostAuthorizationBody',
        'permission': 'PermissionHostDetailNew',
        'group_id': 'str',
        'host_name': 'str',
        'as_proxy': 'bool',
        'proxy_host_id': 'str',
        'owner_name': 'str',
        'proxy_host': 'HostInfoDetail',
        'connection_status': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'lastest_connection_time': 'str',
        'connection_result': 'str',
        'install_icagent': 'bool',
        'nick_name': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'ip': 'ip',
        'os': 'os',
        'port': 'port',
        'authorization': 'authorization',
        'permission': 'permission',
        'group_id': 'group_id',
        'host_name': 'host_name',
        'as_proxy': 'as_proxy',
        'proxy_host_id': 'proxy_host_id',
        'owner_name': 'owner_name',
        'proxy_host': 'proxy_host',
        'connection_status': 'connection_status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'lastest_connection_time': 'lastest_connection_time',
        'connection_result': 'connection_result',
        'install_icagent': 'install_icagent',
        'nick_name': 'nick_name'
    }

    def __init__(self, host_id=None, ip=None, os=None, port=None, authorization=None, permission=None, group_id=None, host_name=None, as_proxy=None, proxy_host_id=None, owner_name=None, proxy_host=None, connection_status=None, create_time=None, update_time=None, lastest_connection_time=None, connection_result=None, install_icagent=None, nick_name=None):
        r"""HostInfoDetail

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param ip: 主机IP
        :type ip: str
        :param os: 主机操作系统
        :type os: str
        :param port: 端口号
        :type port: int
        :param authorization: 
        :type authorization: :class:`huaweicloudsdkcodeartsdeploy.v2.HostAuthorizationBody`
        :param permission: 
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionHostDetailNew`
        :param group_id: 主机集群id
        :type group_id: str
        :param host_name: 主机名
        :type host_name: str
        :param as_proxy: 是否为代理机
        :type as_proxy: bool
        :param proxy_host_id: 代理机id
        :type proxy_host_id: str
        :param owner_name: 主机所属人名称
        :type owner_name: str
        :param proxy_host: 
        :type proxy_host: :class:`huaweicloudsdkcodeartsdeploy.v2.HostInfoDetail`
        :param connection_status: 连通性状态
        :type connection_status: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param lastest_connection_time: 上次连通时间
        :type lastest_connection_time: str
        :param connection_result: 连通性验证结果
        :type connection_result: str
        :param install_icagent: 免费启用应用运维服务（AOM），提供指标监控、日志查询、告警功能（自动安装数据采集器 ICAgent，仅支持华为云linux主机）
        :type install_icagent: bool
        :param nick_name: 创建人昵称
        :type nick_name: str
        """
        
        

        self._host_id = None
        self._ip = None
        self._os = None
        self._port = None
        self._authorization = None
        self._permission = None
        self._group_id = None
        self._host_name = None
        self._as_proxy = None
        self._proxy_host_id = None
        self._owner_name = None
        self._proxy_host = None
        self._connection_status = None
        self._create_time = None
        self._update_time = None
        self._lastest_connection_time = None
        self._connection_result = None
        self._install_icagent = None
        self._nick_name = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if ip is not None:
            self.ip = ip
        if os is not None:
            self.os = os
        if port is not None:
            self.port = port
        if authorization is not None:
            self.authorization = authorization
        if permission is not None:
            self.permission = permission
        if group_id is not None:
            self.group_id = group_id
        if host_name is not None:
            self.host_name = host_name
        if as_proxy is not None:
            self.as_proxy = as_proxy
        if proxy_host_id is not None:
            self.proxy_host_id = proxy_host_id
        if owner_name is not None:
            self.owner_name = owner_name
        if proxy_host is not None:
            self.proxy_host = proxy_host
        if connection_status is not None:
            self.connection_status = connection_status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if lastest_connection_time is not None:
            self.lastest_connection_time = lastest_connection_time
        if connection_result is not None:
            self.connection_result = connection_result
        if install_icagent is not None:
            self.install_icagent = install_icagent
        if nick_name is not None:
            self.nick_name = nick_name

    @property
    def host_id(self):
        r"""Gets the host_id of this HostInfoDetail.

        主机id

        :return: The host_id of this HostInfoDetail.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this HostInfoDetail.

        主机id

        :param host_id: The host_id of this HostInfoDetail.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def ip(self):
        r"""Gets the ip of this HostInfoDetail.

        主机IP

        :return: The ip of this HostInfoDetail.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this HostInfoDetail.

        主机IP

        :param ip: The ip of this HostInfoDetail.
        :type ip: str
        """
        self._ip = ip

    @property
    def os(self):
        r"""Gets the os of this HostInfoDetail.

        主机操作系统

        :return: The os of this HostInfoDetail.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this HostInfoDetail.

        主机操作系统

        :param os: The os of this HostInfoDetail.
        :type os: str
        """
        self._os = os

    @property
    def port(self):
        r"""Gets the port of this HostInfoDetail.

        端口号

        :return: The port of this HostInfoDetail.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this HostInfoDetail.

        端口号

        :param port: The port of this HostInfoDetail.
        :type port: int
        """
        self._port = port

    @property
    def authorization(self):
        r"""Gets the authorization of this HostInfoDetail.

        :return: The authorization of this HostInfoDetail.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.HostAuthorizationBody`
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        r"""Sets the authorization of this HostInfoDetail.

        :param authorization: The authorization of this HostInfoDetail.
        :type authorization: :class:`huaweicloudsdkcodeartsdeploy.v2.HostAuthorizationBody`
        """
        self._authorization = authorization

    @property
    def permission(self):
        r"""Gets the permission of this HostInfoDetail.

        :return: The permission of this HostInfoDetail.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionHostDetailNew`
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this HostInfoDetail.

        :param permission: The permission of this HostInfoDetail.
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionHostDetailNew`
        """
        self._permission = permission

    @property
    def group_id(self):
        r"""Gets the group_id of this HostInfoDetail.

        主机集群id

        :return: The group_id of this HostInfoDetail.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this HostInfoDetail.

        主机集群id

        :param group_id: The group_id of this HostInfoDetail.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def host_name(self):
        r"""Gets the host_name of this HostInfoDetail.

        主机名

        :return: The host_name of this HostInfoDetail.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this HostInfoDetail.

        主机名

        :param host_name: The host_name of this HostInfoDetail.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def as_proxy(self):
        r"""Gets the as_proxy of this HostInfoDetail.

        是否为代理机

        :return: The as_proxy of this HostInfoDetail.
        :rtype: bool
        """
        return self._as_proxy

    @as_proxy.setter
    def as_proxy(self, as_proxy):
        r"""Sets the as_proxy of this HostInfoDetail.

        是否为代理机

        :param as_proxy: The as_proxy of this HostInfoDetail.
        :type as_proxy: bool
        """
        self._as_proxy = as_proxy

    @property
    def proxy_host_id(self):
        r"""Gets the proxy_host_id of this HostInfoDetail.

        代理机id

        :return: The proxy_host_id of this HostInfoDetail.
        :rtype: str
        """
        return self._proxy_host_id

    @proxy_host_id.setter
    def proxy_host_id(self, proxy_host_id):
        r"""Sets the proxy_host_id of this HostInfoDetail.

        代理机id

        :param proxy_host_id: The proxy_host_id of this HostInfoDetail.
        :type proxy_host_id: str
        """
        self._proxy_host_id = proxy_host_id

    @property
    def owner_name(self):
        r"""Gets the owner_name of this HostInfoDetail.

        主机所属人名称

        :return: The owner_name of this HostInfoDetail.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this HostInfoDetail.

        主机所属人名称

        :param owner_name: The owner_name of this HostInfoDetail.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def proxy_host(self):
        r"""Gets the proxy_host of this HostInfoDetail.

        :return: The proxy_host of this HostInfoDetail.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.HostInfoDetail`
        """
        return self._proxy_host

    @proxy_host.setter
    def proxy_host(self, proxy_host):
        r"""Sets the proxy_host of this HostInfoDetail.

        :param proxy_host: The proxy_host of this HostInfoDetail.
        :type proxy_host: :class:`huaweicloudsdkcodeartsdeploy.v2.HostInfoDetail`
        """
        self._proxy_host = proxy_host

    @property
    def connection_status(self):
        r"""Gets the connection_status of this HostInfoDetail.

        连通性状态

        :return: The connection_status of this HostInfoDetail.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        r"""Sets the connection_status of this HostInfoDetail.

        连通性状态

        :param connection_status: The connection_status of this HostInfoDetail.
        :type connection_status: str
        """
        self._connection_status = connection_status

    @property
    def create_time(self):
        r"""Gets the create_time of this HostInfoDetail.

        创建时间

        :return: The create_time of this HostInfoDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this HostInfoDetail.

        创建时间

        :param create_time: The create_time of this HostInfoDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this HostInfoDetail.

        更新时间

        :return: The update_time of this HostInfoDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this HostInfoDetail.

        更新时间

        :param update_time: The update_time of this HostInfoDetail.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def lastest_connection_time(self):
        r"""Gets the lastest_connection_time of this HostInfoDetail.

        上次连通时间

        :return: The lastest_connection_time of this HostInfoDetail.
        :rtype: str
        """
        return self._lastest_connection_time

    @lastest_connection_time.setter
    def lastest_connection_time(self, lastest_connection_time):
        r"""Sets the lastest_connection_time of this HostInfoDetail.

        上次连通时间

        :param lastest_connection_time: The lastest_connection_time of this HostInfoDetail.
        :type lastest_connection_time: str
        """
        self._lastest_connection_time = lastest_connection_time

    @property
    def connection_result(self):
        r"""Gets the connection_result of this HostInfoDetail.

        连通性验证结果

        :return: The connection_result of this HostInfoDetail.
        :rtype: str
        """
        return self._connection_result

    @connection_result.setter
    def connection_result(self, connection_result):
        r"""Sets the connection_result of this HostInfoDetail.

        连通性验证结果

        :param connection_result: The connection_result of this HostInfoDetail.
        :type connection_result: str
        """
        self._connection_result = connection_result

    @property
    def install_icagent(self):
        r"""Gets the install_icagent of this HostInfoDetail.

        免费启用应用运维服务（AOM），提供指标监控、日志查询、告警功能（自动安装数据采集器 ICAgent，仅支持华为云linux主机）

        :return: The install_icagent of this HostInfoDetail.
        :rtype: bool
        """
        return self._install_icagent

    @install_icagent.setter
    def install_icagent(self, install_icagent):
        r"""Sets the install_icagent of this HostInfoDetail.

        免费启用应用运维服务（AOM），提供指标监控、日志查询、告警功能（自动安装数据采集器 ICAgent，仅支持华为云linux主机）

        :param install_icagent: The install_icagent of this HostInfoDetail.
        :type install_icagent: bool
        """
        self._install_icagent = install_icagent

    @property
    def nick_name(self):
        r"""Gets the nick_name of this HostInfoDetail.

        创建人昵称

        :return: The nick_name of this HostInfoDetail.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this HostInfoDetail.

        创建人昵称

        :param nick_name: The nick_name of this HostInfoDetail.
        :type nick_name: str
        """
        self._nick_name = nick_name

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
        if not isinstance(other, HostInfoDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
