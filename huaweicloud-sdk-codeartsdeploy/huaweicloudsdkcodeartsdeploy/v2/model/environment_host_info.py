# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvironmentHostInfo:

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
        'port': 'int',
        'permission': 'EnvironmentHostPermission',
        'group_id': 'str',
        'host_name': 'str',
        'as_proxy': 'bool',
        'proxy_host_id': 'str',
        'proxy_host_name': 'str',
        'owner_id': 'str',
        'owner_name': 'str',
        'connection_status': 'str',
        'lastest_connection_time': 'str',
        'connection_result': 'str',
        'nick_name': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'ip': 'ip',
        'port': 'port',
        'permission': 'permission',
        'group_id': 'group_id',
        'host_name': 'host_name',
        'as_proxy': 'as_proxy',
        'proxy_host_id': 'proxy_host_id',
        'proxy_host_name': 'proxy_host_name',
        'owner_id': 'owner_id',
        'owner_name': 'owner_name',
        'connection_status': 'connection_status',
        'lastest_connection_time': 'lastest_connection_time',
        'connection_result': 'connection_result',
        'nick_name': 'nick_name'
    }

    def __init__(self, host_id=None, ip=None, port=None, permission=None, group_id=None, host_name=None, as_proxy=None, proxy_host_id=None, proxy_host_name=None, owner_id=None, owner_name=None, connection_status=None, lastest_connection_time=None, connection_result=None, nick_name=None):
        r"""EnvironmentHostInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param ip: 主机ip，如：161.17.101.12
        :type ip: str
        :param port: ssh端口，如：22
        :type port: int
        :param permission: 
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.EnvironmentHostPermission`
        :param group_id: 主机集群id
        :type group_id: str
        :param host_name: 主机名
        :type host_name: str
        :param as_proxy: 是否为代理机
        :type as_proxy: bool
        :param proxy_host_id: 代理机id
        :type proxy_host_id: str
        :param proxy_host_name: 代理机名称
        :type proxy_host_name: str
        :param owner_id: 主机所属人id
        :type owner_id: str
        :param owner_name: 主机所属人名称
        :type owner_name: str
        :param connection_status: 连通性状态
        :type connection_status: str
        :param lastest_connection_time: 上次连通时间
        :type lastest_connection_time: str
        :param connection_result: 连通性验证结果
        :type connection_result: str
        :param nick_name: 创建人昵称
        :type nick_name: str
        """
        
        

        self._host_id = None
        self._ip = None
        self._port = None
        self._permission = None
        self._group_id = None
        self._host_name = None
        self._as_proxy = None
        self._proxy_host_id = None
        self._proxy_host_name = None
        self._owner_id = None
        self._owner_name = None
        self._connection_status = None
        self._lastest_connection_time = None
        self._connection_result = None
        self._nick_name = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
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
        if proxy_host_name is not None:
            self.proxy_host_name = proxy_host_name
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_name is not None:
            self.owner_name = owner_name
        if connection_status is not None:
            self.connection_status = connection_status
        if lastest_connection_time is not None:
            self.lastest_connection_time = lastest_connection_time
        if connection_result is not None:
            self.connection_result = connection_result
        if nick_name is not None:
            self.nick_name = nick_name

    @property
    def host_id(self):
        r"""Gets the host_id of this EnvironmentHostInfo.

        主机id

        :return: The host_id of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this EnvironmentHostInfo.

        主机id

        :param host_id: The host_id of this EnvironmentHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def ip(self):
        r"""Gets the ip of this EnvironmentHostInfo.

        主机ip，如：161.17.101.12

        :return: The ip of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this EnvironmentHostInfo.

        主机ip，如：161.17.101.12

        :param ip: The ip of this EnvironmentHostInfo.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this EnvironmentHostInfo.

        ssh端口，如：22

        :return: The port of this EnvironmentHostInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this EnvironmentHostInfo.

        ssh端口，如：22

        :param port: The port of this EnvironmentHostInfo.
        :type port: int
        """
        self._port = port

    @property
    def permission(self):
        r"""Gets the permission of this EnvironmentHostInfo.

        :return: The permission of this EnvironmentHostInfo.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.EnvironmentHostPermission`
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this EnvironmentHostInfo.

        :param permission: The permission of this EnvironmentHostInfo.
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.EnvironmentHostPermission`
        """
        self._permission = permission

    @property
    def group_id(self):
        r"""Gets the group_id of this EnvironmentHostInfo.

        主机集群id

        :return: The group_id of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this EnvironmentHostInfo.

        主机集群id

        :param group_id: The group_id of this EnvironmentHostInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def host_name(self):
        r"""Gets the host_name of this EnvironmentHostInfo.

        主机名

        :return: The host_name of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this EnvironmentHostInfo.

        主机名

        :param host_name: The host_name of this EnvironmentHostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def as_proxy(self):
        r"""Gets the as_proxy of this EnvironmentHostInfo.

        是否为代理机

        :return: The as_proxy of this EnvironmentHostInfo.
        :rtype: bool
        """
        return self._as_proxy

    @as_proxy.setter
    def as_proxy(self, as_proxy):
        r"""Sets the as_proxy of this EnvironmentHostInfo.

        是否为代理机

        :param as_proxy: The as_proxy of this EnvironmentHostInfo.
        :type as_proxy: bool
        """
        self._as_proxy = as_proxy

    @property
    def proxy_host_id(self):
        r"""Gets the proxy_host_id of this EnvironmentHostInfo.

        代理机id

        :return: The proxy_host_id of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._proxy_host_id

    @proxy_host_id.setter
    def proxy_host_id(self, proxy_host_id):
        r"""Sets the proxy_host_id of this EnvironmentHostInfo.

        代理机id

        :param proxy_host_id: The proxy_host_id of this EnvironmentHostInfo.
        :type proxy_host_id: str
        """
        self._proxy_host_id = proxy_host_id

    @property
    def proxy_host_name(self):
        r"""Gets the proxy_host_name of this EnvironmentHostInfo.

        代理机名称

        :return: The proxy_host_name of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._proxy_host_name

    @proxy_host_name.setter
    def proxy_host_name(self, proxy_host_name):
        r"""Sets the proxy_host_name of this EnvironmentHostInfo.

        代理机名称

        :param proxy_host_name: The proxy_host_name of this EnvironmentHostInfo.
        :type proxy_host_name: str
        """
        self._proxy_host_name = proxy_host_name

    @property
    def owner_id(self):
        r"""Gets the owner_id of this EnvironmentHostInfo.

        主机所属人id

        :return: The owner_id of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this EnvironmentHostInfo.

        主机所属人id

        :param owner_id: The owner_id of this EnvironmentHostInfo.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def owner_name(self):
        r"""Gets the owner_name of this EnvironmentHostInfo.

        主机所属人名称

        :return: The owner_name of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this EnvironmentHostInfo.

        主机所属人名称

        :param owner_name: The owner_name of this EnvironmentHostInfo.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def connection_status(self):
        r"""Gets the connection_status of this EnvironmentHostInfo.

        连通性状态

        :return: The connection_status of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        r"""Sets the connection_status of this EnvironmentHostInfo.

        连通性状态

        :param connection_status: The connection_status of this EnvironmentHostInfo.
        :type connection_status: str
        """
        self._connection_status = connection_status

    @property
    def lastest_connection_time(self):
        r"""Gets the lastest_connection_time of this EnvironmentHostInfo.

        上次连通时间

        :return: The lastest_connection_time of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._lastest_connection_time

    @lastest_connection_time.setter
    def lastest_connection_time(self, lastest_connection_time):
        r"""Sets the lastest_connection_time of this EnvironmentHostInfo.

        上次连通时间

        :param lastest_connection_time: The lastest_connection_time of this EnvironmentHostInfo.
        :type lastest_connection_time: str
        """
        self._lastest_connection_time = lastest_connection_time

    @property
    def connection_result(self):
        r"""Gets the connection_result of this EnvironmentHostInfo.

        连通性验证结果

        :return: The connection_result of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._connection_result

    @connection_result.setter
    def connection_result(self, connection_result):
        r"""Sets the connection_result of this EnvironmentHostInfo.

        连通性验证结果

        :param connection_result: The connection_result of this EnvironmentHostInfo.
        :type connection_result: str
        """
        self._connection_result = connection_result

    @property
    def nick_name(self):
        r"""Gets the nick_name of this EnvironmentHostInfo.

        创建人昵称

        :return: The nick_name of this EnvironmentHostInfo.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this EnvironmentHostInfo.

        创建人昵称

        :param nick_name: The nick_name of this EnvironmentHostInfo.
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
        if not isinstance(other, EnvironmentHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
