# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'ip': 'str',
        'os': 'str',
        'port': 'int',
        'authorization': 'HostAuthorizationBody',
        'permission': 'PermissionHostDetailNew',
        'host_name': 'str',
        'as_proxy': 'bool',
        'group_id': 'str',
        'proxy_host_id': 'str',
        'owner_id': 'str',
        'owner_name': 'str',
        'proxy_host': 'HostInfo',
        'connection_status': 'str',
        'create_time': 'str',
        'lastest_connection_time': 'str',
        'connection_result': 'str',
        'nick_name': 'str',
        'import_status': 'str',
        'env_count': 'int'
    }

    attribute_map = {
        'uuid': 'uuid',
        'ip': 'ip',
        'os': 'os',
        'port': 'port',
        'authorization': 'authorization',
        'permission': 'permission',
        'host_name': 'host_name',
        'as_proxy': 'as_proxy',
        'group_id': 'group_id',
        'proxy_host_id': 'proxy_host_id',
        'owner_id': 'owner_id',
        'owner_name': 'owner_name',
        'proxy_host': 'proxy_host',
        'connection_status': 'connection_status',
        'create_time': 'create_time',
        'lastest_connection_time': 'lastest_connection_time',
        'connection_result': 'connection_result',
        'nick_name': 'nick_name',
        'import_status': 'import_status',
        'env_count': 'env_count'
    }

    def __init__(self, uuid=None, ip=None, os=None, port=None, authorization=None, permission=None, host_name=None, as_proxy=None, group_id=None, proxy_host_id=None, owner_id=None, owner_name=None, proxy_host=None, connection_status=None, create_time=None, lastest_connection_time=None, connection_result=None, nick_name=None, import_status=None, env_count=None):
        r"""HostInfo

        The model defined in huaweicloud sdk

        :param uuid: 主机id
        :type uuid: str
        :param ip: 主机IP
        :type ip: str
        :param os: 主机操作系统
        :type os: str
        :param port: 端口
        :type port: int
        :param authorization: 
        :type authorization: :class:`huaweicloudsdkcodeartsdeploy.v2.HostAuthorizationBody`
        :param permission: 
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionHostDetailNew`
        :param host_name: 主机名称
        :type host_name: str
        :param as_proxy: 是否为代理机
        :type as_proxy: bool
        :param group_id: 主机集群id
        :type group_id: str
        :param proxy_host_id: 代理机id
        :type proxy_host_id: str
        :param owner_id: 主机所属人id
        :type owner_id: str
        :param owner_name: 主机所属人名称
        :type owner_name: str
        :param proxy_host: 
        :type proxy_host: :class:`huaweicloudsdkcodeartsdeploy.v2.HostInfo`
        :param connection_status: 连通性状态
        :type connection_status: str
        :param create_time: 创建时间
        :type create_time: str
        :param lastest_connection_time: 上次连通时间
        :type lastest_connection_time: str
        :param connection_result: 连通性验证结果
        :type connection_result: str
        :param nick_name: 主机所属人昵称
        :type nick_name: str
        :param import_status: 导入状态
        :type import_status: str
        :param env_count: 关联环境数量
        :type env_count: int
        """
        
        

        self._uuid = None
        self._ip = None
        self._os = None
        self._port = None
        self._authorization = None
        self._permission = None
        self._host_name = None
        self._as_proxy = None
        self._group_id = None
        self._proxy_host_id = None
        self._owner_id = None
        self._owner_name = None
        self._proxy_host = None
        self._connection_status = None
        self._create_time = None
        self._lastest_connection_time = None
        self._connection_result = None
        self._nick_name = None
        self._import_status = None
        self._env_count = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
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
        if host_name is not None:
            self.host_name = host_name
        if as_proxy is not None:
            self.as_proxy = as_proxy
        if group_id is not None:
            self.group_id = group_id
        if proxy_host_id is not None:
            self.proxy_host_id = proxy_host_id
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_name is not None:
            self.owner_name = owner_name
        if proxy_host is not None:
            self.proxy_host = proxy_host
        if connection_status is not None:
            self.connection_status = connection_status
        if create_time is not None:
            self.create_time = create_time
        if lastest_connection_time is not None:
            self.lastest_connection_time = lastest_connection_time
        if connection_result is not None:
            self.connection_result = connection_result
        if nick_name is not None:
            self.nick_name = nick_name
        if import_status is not None:
            self.import_status = import_status
        if env_count is not None:
            self.env_count = env_count

    @property
    def uuid(self):
        r"""Gets the uuid of this HostInfo.

        主机id

        :return: The uuid of this HostInfo.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this HostInfo.

        主机id

        :param uuid: The uuid of this HostInfo.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def ip(self):
        r"""Gets the ip of this HostInfo.

        主机IP

        :return: The ip of this HostInfo.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this HostInfo.

        主机IP

        :param ip: The ip of this HostInfo.
        :type ip: str
        """
        self._ip = ip

    @property
    def os(self):
        r"""Gets the os of this HostInfo.

        主机操作系统

        :return: The os of this HostInfo.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this HostInfo.

        主机操作系统

        :param os: The os of this HostInfo.
        :type os: str
        """
        self._os = os

    @property
    def port(self):
        r"""Gets the port of this HostInfo.

        端口

        :return: The port of this HostInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this HostInfo.

        端口

        :param port: The port of this HostInfo.
        :type port: int
        """
        self._port = port

    @property
    def authorization(self):
        r"""Gets the authorization of this HostInfo.

        :return: The authorization of this HostInfo.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.HostAuthorizationBody`
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        r"""Sets the authorization of this HostInfo.

        :param authorization: The authorization of this HostInfo.
        :type authorization: :class:`huaweicloudsdkcodeartsdeploy.v2.HostAuthorizationBody`
        """
        self._authorization = authorization

    @property
    def permission(self):
        r"""Gets the permission of this HostInfo.

        :return: The permission of this HostInfo.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionHostDetailNew`
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this HostInfo.

        :param permission: The permission of this HostInfo.
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionHostDetailNew`
        """
        self._permission = permission

    @property
    def host_name(self):
        r"""Gets the host_name of this HostInfo.

        主机名称

        :return: The host_name of this HostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this HostInfo.

        主机名称

        :param host_name: The host_name of this HostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def as_proxy(self):
        r"""Gets the as_proxy of this HostInfo.

        是否为代理机

        :return: The as_proxy of this HostInfo.
        :rtype: bool
        """
        return self._as_proxy

    @as_proxy.setter
    def as_proxy(self, as_proxy):
        r"""Sets the as_proxy of this HostInfo.

        是否为代理机

        :param as_proxy: The as_proxy of this HostInfo.
        :type as_proxy: bool
        """
        self._as_proxy = as_proxy

    @property
    def group_id(self):
        r"""Gets the group_id of this HostInfo.

        主机集群id

        :return: The group_id of this HostInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this HostInfo.

        主机集群id

        :param group_id: The group_id of this HostInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def proxy_host_id(self):
        r"""Gets the proxy_host_id of this HostInfo.

        代理机id

        :return: The proxy_host_id of this HostInfo.
        :rtype: str
        """
        return self._proxy_host_id

    @proxy_host_id.setter
    def proxy_host_id(self, proxy_host_id):
        r"""Sets the proxy_host_id of this HostInfo.

        代理机id

        :param proxy_host_id: The proxy_host_id of this HostInfo.
        :type proxy_host_id: str
        """
        self._proxy_host_id = proxy_host_id

    @property
    def owner_id(self):
        r"""Gets the owner_id of this HostInfo.

        主机所属人id

        :return: The owner_id of this HostInfo.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this HostInfo.

        主机所属人id

        :param owner_id: The owner_id of this HostInfo.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def owner_name(self):
        r"""Gets the owner_name of this HostInfo.

        主机所属人名称

        :return: The owner_name of this HostInfo.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this HostInfo.

        主机所属人名称

        :param owner_name: The owner_name of this HostInfo.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def proxy_host(self):
        r"""Gets the proxy_host of this HostInfo.

        :return: The proxy_host of this HostInfo.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.HostInfo`
        """
        return self._proxy_host

    @proxy_host.setter
    def proxy_host(self, proxy_host):
        r"""Sets the proxy_host of this HostInfo.

        :param proxy_host: The proxy_host of this HostInfo.
        :type proxy_host: :class:`huaweicloudsdkcodeartsdeploy.v2.HostInfo`
        """
        self._proxy_host = proxy_host

    @property
    def connection_status(self):
        r"""Gets the connection_status of this HostInfo.

        连通性状态

        :return: The connection_status of this HostInfo.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        r"""Sets the connection_status of this HostInfo.

        连通性状态

        :param connection_status: The connection_status of this HostInfo.
        :type connection_status: str
        """
        self._connection_status = connection_status

    @property
    def create_time(self):
        r"""Gets the create_time of this HostInfo.

        创建时间

        :return: The create_time of this HostInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this HostInfo.

        创建时间

        :param create_time: The create_time of this HostInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def lastest_connection_time(self):
        r"""Gets the lastest_connection_time of this HostInfo.

        上次连通时间

        :return: The lastest_connection_time of this HostInfo.
        :rtype: str
        """
        return self._lastest_connection_time

    @lastest_connection_time.setter
    def lastest_connection_time(self, lastest_connection_time):
        r"""Sets the lastest_connection_time of this HostInfo.

        上次连通时间

        :param lastest_connection_time: The lastest_connection_time of this HostInfo.
        :type lastest_connection_time: str
        """
        self._lastest_connection_time = lastest_connection_time

    @property
    def connection_result(self):
        r"""Gets the connection_result of this HostInfo.

        连通性验证结果

        :return: The connection_result of this HostInfo.
        :rtype: str
        """
        return self._connection_result

    @connection_result.setter
    def connection_result(self, connection_result):
        r"""Sets the connection_result of this HostInfo.

        连通性验证结果

        :param connection_result: The connection_result of this HostInfo.
        :type connection_result: str
        """
        self._connection_result = connection_result

    @property
    def nick_name(self):
        r"""Gets the nick_name of this HostInfo.

        主机所属人昵称

        :return: The nick_name of this HostInfo.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this HostInfo.

        主机所属人昵称

        :param nick_name: The nick_name of this HostInfo.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def import_status(self):
        r"""Gets the import_status of this HostInfo.

        导入状态

        :return: The import_status of this HostInfo.
        :rtype: str
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status):
        r"""Sets the import_status of this HostInfo.

        导入状态

        :param import_status: The import_status of this HostInfo.
        :type import_status: str
        """
        self._import_status = import_status

    @property
    def env_count(self):
        r"""Gets the env_count of this HostInfo.

        关联环境数量

        :return: The env_count of this HostInfo.
        :rtype: int
        """
        return self._env_count

    @env_count.setter
    def env_count(self, env_count):
        r"""Sets the env_count of this HostInfo.

        关联环境数量

        :param env_count: The env_count of this HostInfo.
        :type env_count: int
        """
        self._env_count = env_count

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
        if not isinstance(other, HostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
