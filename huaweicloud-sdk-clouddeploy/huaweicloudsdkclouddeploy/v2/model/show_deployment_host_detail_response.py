# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeploymentHostDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'host_name': 'str',
        'ip': 'str',
        'port': 'int',
        'os': 'str',
        'as_proxy': 'bool',
        'proxy_host_id': 'str',
        'authorization': 'DeploymentHostAuthorizationBody',
        'install_icagent': 'bool',
        'host_id': 'str',
        'proxy_host': 'DeploymentHostDetail',
        'group_name': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'permission': 'PermissionHostDetail',
        'update_time': 'str',
        'lastest_connection_time': 'str',
        'connection_status': 'str',
        'owner_name': 'str',
        'updator_id': 'str',
        'create_time': 'str',
        'nick_name': 'str',
        'owner_id': 'str',
        'updator_name': 'str',
        'connection_result': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'host_name': 'host_name',
        'ip': 'ip',
        'port': 'port',
        'os': 'os',
        'as_proxy': 'as_proxy',
        'proxy_host_id': 'proxy_host_id',
        'authorization': 'authorization',
        'install_icagent': 'install_icagent',
        'host_id': 'host_id',
        'proxy_host': 'proxy_host',
        'group_name': 'group_name',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'permission': 'permission',
        'update_time': 'update_time',
        'lastest_connection_time': 'lastest_connection_time',
        'connection_status': 'connection_status',
        'owner_name': 'owner_name',
        'updator_id': 'updator_id',
        'create_time': 'create_time',
        'nick_name': 'nick_name',
        'owner_id': 'owner_id',
        'updator_name': 'updator_name',
        'connection_result': 'connection_result'
    }

    def __init__(self, group_id=None, host_name=None, ip=None, port=None, os=None, as_proxy=None, proxy_host_id=None, authorization=None, install_icagent=None, host_id=None, proxy_host=None, group_name=None, project_id=None, project_name=None, permission=None, update_time=None, lastest_connection_time=None, connection_status=None, owner_name=None, updator_id=None, create_time=None, nick_name=None, owner_id=None, updator_name=None, connection_result=None):
        """ShowDeploymentHostDetailResponse

        The model defined in huaweicloud sdk

        :param group_id: 主机组id
        :type group_id: str
        :param host_name: 主机名称
        :type host_name: str
        :param ip: IP，请输入弹性ip格式：161.17.101.12
        :type ip: str
        :param port: ssh端口，如：22
        :type port: int
        :param os: 操作系统：windows|linux，需要和主机组保持一致
        :type os: str
        :param as_proxy: 是否为代理机
        :type as_proxy: bool
        :param proxy_host_id: 代理机id
        :type proxy_host_id: str
        :param authorization: 
        :type authorization: :class:`huaweicloudsdkclouddeploy.v2.DeploymentHostAuthorizationBody`
        :param install_icagent: 免费启用应用运维服务（AOM），提供指标监控、日志查询、告警功能（自动安装数据采集器 ICAgent，仅支持华为云linux主机）
        :type install_icagent: bool
        :param host_id: 主机ID
        :type host_id: str
        :param proxy_host: 
        :type proxy_host: :class:`huaweicloudsdkclouddeploy.v2.DeploymentHostDetail`
        :param group_name: 主机组名
        :type group_name: str
        :param project_id: devcloud项目id
        :type project_id: str
        :param project_name: devcloud项目名称
        :type project_name: str
        :param permission: 
        :type permission: :class:`huaweicloudsdkclouddeploy.v2.PermissionHostDetail`
        :param update_time: 更新时间
        :type update_time: str
        :param lastest_connection_time: 最后连接时间
        :type lastest_connection_time: str
        :param connection_status: 连接状态
        :type connection_status: str
        :param owner_name: 拥有者名称
        :type owner_name: str
        :param updator_id: 维护者id
        :type updator_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param nick_name: 昵称
        :type nick_name: str
        :param owner_id: 拥有者id
        :type owner_id: str
        :param updator_name: 维护者名称
        :type updator_name: str
        :param connection_result: 连接结果
        :type connection_result: str
        """
        
        super(ShowDeploymentHostDetailResponse, self).__init__()

        self._group_id = None
        self._host_name = None
        self._ip = None
        self._port = None
        self._os = None
        self._as_proxy = None
        self._proxy_host_id = None
        self._authorization = None
        self._install_icagent = None
        self._host_id = None
        self._proxy_host = None
        self._group_name = None
        self._project_id = None
        self._project_name = None
        self._permission = None
        self._update_time = None
        self._lastest_connection_time = None
        self._connection_status = None
        self._owner_name = None
        self._updator_id = None
        self._create_time = None
        self._nick_name = None
        self._owner_id = None
        self._updator_name = None
        self._connection_result = None
        self.discriminator = None

        self.group_id = group_id
        self.host_name = host_name
        self.ip = ip
        self.port = port
        self.os = os
        self.as_proxy = as_proxy
        if proxy_host_id is not None:
            self.proxy_host_id = proxy_host_id
        self.authorization = authorization
        if install_icagent is not None:
            self.install_icagent = install_icagent
        if host_id is not None:
            self.host_id = host_id
        if proxy_host is not None:
            self.proxy_host = proxy_host
        if group_name is not None:
            self.group_name = group_name
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if permission is not None:
            self.permission = permission
        if update_time is not None:
            self.update_time = update_time
        if lastest_connection_time is not None:
            self.lastest_connection_time = lastest_connection_time
        if connection_status is not None:
            self.connection_status = connection_status
        if owner_name is not None:
            self.owner_name = owner_name
        if updator_id is not None:
            self.updator_id = updator_id
        if create_time is not None:
            self.create_time = create_time
        if nick_name is not None:
            self.nick_name = nick_name
        if owner_id is not None:
            self.owner_id = owner_id
        if updator_name is not None:
            self.updator_name = updator_name
        if connection_result is not None:
            self.connection_result = connection_result

    @property
    def group_id(self):
        """Gets the group_id of this ShowDeploymentHostDetailResponse.

        主机组id

        :return: The group_id of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowDeploymentHostDetailResponse.

        主机组id

        :param group_id: The group_id of this ShowDeploymentHostDetailResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def host_name(self):
        """Gets the host_name of this ShowDeploymentHostDetailResponse.

        主机名称

        :return: The host_name of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ShowDeploymentHostDetailResponse.

        主机名称

        :param host_name: The host_name of this ShowDeploymentHostDetailResponse.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def ip(self):
        """Gets the ip of this ShowDeploymentHostDetailResponse.

        IP，请输入弹性ip格式：161.17.101.12

        :return: The ip of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ShowDeploymentHostDetailResponse.

        IP，请输入弹性ip格式：161.17.101.12

        :param ip: The ip of this ShowDeploymentHostDetailResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this ShowDeploymentHostDetailResponse.

        ssh端口，如：22

        :return: The port of this ShowDeploymentHostDetailResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ShowDeploymentHostDetailResponse.

        ssh端口，如：22

        :param port: The port of this ShowDeploymentHostDetailResponse.
        :type port: int
        """
        self._port = port

    @property
    def os(self):
        """Gets the os of this ShowDeploymentHostDetailResponse.

        操作系统：windows|linux，需要和主机组保持一致

        :return: The os of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this ShowDeploymentHostDetailResponse.

        操作系统：windows|linux，需要和主机组保持一致

        :param os: The os of this ShowDeploymentHostDetailResponse.
        :type os: str
        """
        self._os = os

    @property
    def as_proxy(self):
        """Gets the as_proxy of this ShowDeploymentHostDetailResponse.

        是否为代理机

        :return: The as_proxy of this ShowDeploymentHostDetailResponse.
        :rtype: bool
        """
        return self._as_proxy

    @as_proxy.setter
    def as_proxy(self, as_proxy):
        """Sets the as_proxy of this ShowDeploymentHostDetailResponse.

        是否为代理机

        :param as_proxy: The as_proxy of this ShowDeploymentHostDetailResponse.
        :type as_proxy: bool
        """
        self._as_proxy = as_proxy

    @property
    def proxy_host_id(self):
        """Gets the proxy_host_id of this ShowDeploymentHostDetailResponse.

        代理机id

        :return: The proxy_host_id of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._proxy_host_id

    @proxy_host_id.setter
    def proxy_host_id(self, proxy_host_id):
        """Sets the proxy_host_id of this ShowDeploymentHostDetailResponse.

        代理机id

        :param proxy_host_id: The proxy_host_id of this ShowDeploymentHostDetailResponse.
        :type proxy_host_id: str
        """
        self._proxy_host_id = proxy_host_id

    @property
    def authorization(self):
        """Gets the authorization of this ShowDeploymentHostDetailResponse.


        :return: The authorization of this ShowDeploymentHostDetailResponse.
        :rtype: :class:`huaweicloudsdkclouddeploy.v2.DeploymentHostAuthorizationBody`
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ShowDeploymentHostDetailResponse.


        :param authorization: The authorization of this ShowDeploymentHostDetailResponse.
        :type authorization: :class:`huaweicloudsdkclouddeploy.v2.DeploymentHostAuthorizationBody`
        """
        self._authorization = authorization

    @property
    def install_icagent(self):
        """Gets the install_icagent of this ShowDeploymentHostDetailResponse.

        免费启用应用运维服务（AOM），提供指标监控、日志查询、告警功能（自动安装数据采集器 ICAgent，仅支持华为云linux主机）

        :return: The install_icagent of this ShowDeploymentHostDetailResponse.
        :rtype: bool
        """
        return self._install_icagent

    @install_icagent.setter
    def install_icagent(self, install_icagent):
        """Sets the install_icagent of this ShowDeploymentHostDetailResponse.

        免费启用应用运维服务（AOM），提供指标监控、日志查询、告警功能（自动安装数据采集器 ICAgent，仅支持华为云linux主机）

        :param install_icagent: The install_icagent of this ShowDeploymentHostDetailResponse.
        :type install_icagent: bool
        """
        self._install_icagent = install_icagent

    @property
    def host_id(self):
        """Gets the host_id of this ShowDeploymentHostDetailResponse.

        主机ID

        :return: The host_id of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ShowDeploymentHostDetailResponse.

        主机ID

        :param host_id: The host_id of this ShowDeploymentHostDetailResponse.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def proxy_host(self):
        """Gets the proxy_host of this ShowDeploymentHostDetailResponse.


        :return: The proxy_host of this ShowDeploymentHostDetailResponse.
        :rtype: :class:`huaweicloudsdkclouddeploy.v2.DeploymentHostDetail`
        """
        return self._proxy_host

    @proxy_host.setter
    def proxy_host(self, proxy_host):
        """Sets the proxy_host of this ShowDeploymentHostDetailResponse.


        :param proxy_host: The proxy_host of this ShowDeploymentHostDetailResponse.
        :type proxy_host: :class:`huaweicloudsdkclouddeploy.v2.DeploymentHostDetail`
        """
        self._proxy_host = proxy_host

    @property
    def group_name(self):
        """Gets the group_name of this ShowDeploymentHostDetailResponse.

        主机组名

        :return: The group_name of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ShowDeploymentHostDetailResponse.

        主机组名

        :param group_name: The group_name of this ShowDeploymentHostDetailResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def project_id(self):
        """Gets the project_id of this ShowDeploymentHostDetailResponse.

        devcloud项目id

        :return: The project_id of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowDeploymentHostDetailResponse.

        devcloud项目id

        :param project_id: The project_id of this ShowDeploymentHostDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ShowDeploymentHostDetailResponse.

        devcloud项目名称

        :return: The project_name of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ShowDeploymentHostDetailResponse.

        devcloud项目名称

        :param project_name: The project_name of this ShowDeploymentHostDetailResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def permission(self):
        """Gets the permission of this ShowDeploymentHostDetailResponse.


        :return: The permission of this ShowDeploymentHostDetailResponse.
        :rtype: :class:`huaweicloudsdkclouddeploy.v2.PermissionHostDetail`
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ShowDeploymentHostDetailResponse.


        :param permission: The permission of this ShowDeploymentHostDetailResponse.
        :type permission: :class:`huaweicloudsdkclouddeploy.v2.PermissionHostDetail`
        """
        self._permission = permission

    @property
    def update_time(self):
        """Gets the update_time of this ShowDeploymentHostDetailResponse.

        更新时间

        :return: The update_time of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowDeploymentHostDetailResponse.

        更新时间

        :param update_time: The update_time of this ShowDeploymentHostDetailResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def lastest_connection_time(self):
        """Gets the lastest_connection_time of this ShowDeploymentHostDetailResponse.

        最后连接时间

        :return: The lastest_connection_time of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._lastest_connection_time

    @lastest_connection_time.setter
    def lastest_connection_time(self, lastest_connection_time):
        """Sets the lastest_connection_time of this ShowDeploymentHostDetailResponse.

        最后连接时间

        :param lastest_connection_time: The lastest_connection_time of this ShowDeploymentHostDetailResponse.
        :type lastest_connection_time: str
        """
        self._lastest_connection_time = lastest_connection_time

    @property
    def connection_status(self):
        """Gets the connection_status of this ShowDeploymentHostDetailResponse.

        连接状态

        :return: The connection_status of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this ShowDeploymentHostDetailResponse.

        连接状态

        :param connection_status: The connection_status of this ShowDeploymentHostDetailResponse.
        :type connection_status: str
        """
        self._connection_status = connection_status

    @property
    def owner_name(self):
        """Gets the owner_name of this ShowDeploymentHostDetailResponse.

        拥有者名称

        :return: The owner_name of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this ShowDeploymentHostDetailResponse.

        拥有者名称

        :param owner_name: The owner_name of this ShowDeploymentHostDetailResponse.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def updator_id(self):
        """Gets the updator_id of this ShowDeploymentHostDetailResponse.

        维护者id

        :return: The updator_id of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._updator_id

    @updator_id.setter
    def updator_id(self, updator_id):
        """Sets the updator_id of this ShowDeploymentHostDetailResponse.

        维护者id

        :param updator_id: The updator_id of this ShowDeploymentHostDetailResponse.
        :type updator_id: str
        """
        self._updator_id = updator_id

    @property
    def create_time(self):
        """Gets the create_time of this ShowDeploymentHostDetailResponse.

        创建时间

        :return: The create_time of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowDeploymentHostDetailResponse.

        创建时间

        :param create_time: The create_time of this ShowDeploymentHostDetailResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def nick_name(self):
        """Gets the nick_name of this ShowDeploymentHostDetailResponse.

        昵称

        :return: The nick_name of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this ShowDeploymentHostDetailResponse.

        昵称

        :param nick_name: The nick_name of this ShowDeploymentHostDetailResponse.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def owner_id(self):
        """Gets the owner_id of this ShowDeploymentHostDetailResponse.

        拥有者id

        :return: The owner_id of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ShowDeploymentHostDetailResponse.

        拥有者id

        :param owner_id: The owner_id of this ShowDeploymentHostDetailResponse.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def updator_name(self):
        """Gets the updator_name of this ShowDeploymentHostDetailResponse.

        维护者名称

        :return: The updator_name of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._updator_name

    @updator_name.setter
    def updator_name(self, updator_name):
        """Sets the updator_name of this ShowDeploymentHostDetailResponse.

        维护者名称

        :param updator_name: The updator_name of this ShowDeploymentHostDetailResponse.
        :type updator_name: str
        """
        self._updator_name = updator_name

    @property
    def connection_result(self):
        """Gets the connection_result of this ShowDeploymentHostDetailResponse.

        连接结果

        :return: The connection_result of this ShowDeploymentHostDetailResponse.
        :rtype: str
        """
        return self._connection_result

    @connection_result.setter
    def connection_result(self, connection_result):
        """Sets the connection_result of this ShowDeploymentHostDetailResponse.

        连接结果

        :param connection_result: The connection_result of this ShowDeploymentHostDetailResponse.
        :type connection_result: str
        """
        self._connection_result = connection_result

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
        if not isinstance(other, ShowDeploymentHostDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
