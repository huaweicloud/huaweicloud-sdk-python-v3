# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentHostDetail:


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
        'permission': 'PermissionHostDetail'
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
        'permission': 'permission'
    }

    def __init__(self, group_id=None, host_name=None, ip=None, port=None, os=None, as_proxy=None, proxy_host_id=None, authorization=None, install_icagent=None, host_id=None, proxy_host=None, group_name=None, project_id=None, project_name=None, permission=None):
        """DeploymentHostDetail - a model defined in huaweicloud sdk"""
        
        

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

    @property
    def group_id(self):
        """Gets the group_id of this DeploymentHostDetail.

        主机组id

        :return: The group_id of this DeploymentHostDetail.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DeploymentHostDetail.

        主机组id

        :param group_id: The group_id of this DeploymentHostDetail.
        :type: str
        """
        self._group_id = group_id

    @property
    def host_name(self):
        """Gets the host_name of this DeploymentHostDetail.

        主机名称

        :return: The host_name of this DeploymentHostDetail.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this DeploymentHostDetail.

        主机名称

        :param host_name: The host_name of this DeploymentHostDetail.
        :type: str
        """
        self._host_name = host_name

    @property
    def ip(self):
        """Gets the ip of this DeploymentHostDetail.

        IP，请输入弹性ip格式：161.17.101.12

        :return: The ip of this DeploymentHostDetail.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this DeploymentHostDetail.

        IP，请输入弹性ip格式：161.17.101.12

        :param ip: The ip of this DeploymentHostDetail.
        :type: str
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this DeploymentHostDetail.

        ssh端口，如：22

        :return: The port of this DeploymentHostDetail.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DeploymentHostDetail.

        ssh端口，如：22

        :param port: The port of this DeploymentHostDetail.
        :type: int
        """
        self._port = port

    @property
    def os(self):
        """Gets the os of this DeploymentHostDetail.

        操作系统：windows|linux，需要和主机组保持一致

        :return: The os of this DeploymentHostDetail.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this DeploymentHostDetail.

        操作系统：windows|linux，需要和主机组保持一致

        :param os: The os of this DeploymentHostDetail.
        :type: str
        """
        self._os = os

    @property
    def as_proxy(self):
        """Gets the as_proxy of this DeploymentHostDetail.

        是否为代理机

        :return: The as_proxy of this DeploymentHostDetail.
        :rtype: bool
        """
        return self._as_proxy

    @as_proxy.setter
    def as_proxy(self, as_proxy):
        """Sets the as_proxy of this DeploymentHostDetail.

        是否为代理机

        :param as_proxy: The as_proxy of this DeploymentHostDetail.
        :type: bool
        """
        self._as_proxy = as_proxy

    @property
    def proxy_host_id(self):
        """Gets the proxy_host_id of this DeploymentHostDetail.

        代理机id

        :return: The proxy_host_id of this DeploymentHostDetail.
        :rtype: str
        """
        return self._proxy_host_id

    @proxy_host_id.setter
    def proxy_host_id(self, proxy_host_id):
        """Sets the proxy_host_id of this DeploymentHostDetail.

        代理机id

        :param proxy_host_id: The proxy_host_id of this DeploymentHostDetail.
        :type: str
        """
        self._proxy_host_id = proxy_host_id

    @property
    def authorization(self):
        """Gets the authorization of this DeploymentHostDetail.


        :return: The authorization of this DeploymentHostDetail.
        :rtype: DeploymentHostAuthorizationBody
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this DeploymentHostDetail.


        :param authorization: The authorization of this DeploymentHostDetail.
        :type: DeploymentHostAuthorizationBody
        """
        self._authorization = authorization

    @property
    def install_icagent(self):
        """Gets the install_icagent of this DeploymentHostDetail.

        免费启用应用运维服务（AOM），提供指标监控、日志查询、告警功能（自动安装数据采集器 ICAgent，仅支持华为云linux主机）

        :return: The install_icagent of this DeploymentHostDetail.
        :rtype: bool
        """
        return self._install_icagent

    @install_icagent.setter
    def install_icagent(self, install_icagent):
        """Sets the install_icagent of this DeploymentHostDetail.

        免费启用应用运维服务（AOM），提供指标监控、日志查询、告警功能（自动安装数据采集器 ICAgent，仅支持华为云linux主机）

        :param install_icagent: The install_icagent of this DeploymentHostDetail.
        :type: bool
        """
        self._install_icagent = install_icagent

    @property
    def host_id(self):
        """Gets the host_id of this DeploymentHostDetail.

        主机ID

        :return: The host_id of this DeploymentHostDetail.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this DeploymentHostDetail.

        主机ID

        :param host_id: The host_id of this DeploymentHostDetail.
        :type: str
        """
        self._host_id = host_id

    @property
    def proxy_host(self):
        """Gets the proxy_host of this DeploymentHostDetail.


        :return: The proxy_host of this DeploymentHostDetail.
        :rtype: DeploymentHostDetail
        """
        return self._proxy_host

    @proxy_host.setter
    def proxy_host(self, proxy_host):
        """Sets the proxy_host of this DeploymentHostDetail.


        :param proxy_host: The proxy_host of this DeploymentHostDetail.
        :type: DeploymentHostDetail
        """
        self._proxy_host = proxy_host

    @property
    def group_name(self):
        """Gets the group_name of this DeploymentHostDetail.

        主机组名

        :return: The group_name of this DeploymentHostDetail.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this DeploymentHostDetail.

        主机组名

        :param group_name: The group_name of this DeploymentHostDetail.
        :type: str
        """
        self._group_name = group_name

    @property
    def project_id(self):
        """Gets the project_id of this DeploymentHostDetail.

        devcloud项目id

        :return: The project_id of this DeploymentHostDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DeploymentHostDetail.

        devcloud项目id

        :param project_id: The project_id of this DeploymentHostDetail.
        :type: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this DeploymentHostDetail.

        devcloud项目名称

        :return: The project_name of this DeploymentHostDetail.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DeploymentHostDetail.

        devcloud项目名称

        :param project_name: The project_name of this DeploymentHostDetail.
        :type: str
        """
        self._project_name = project_name

    @property
    def permission(self):
        """Gets the permission of this DeploymentHostDetail.


        :return: The permission of this DeploymentHostDetail.
        :rtype: PermissionHostDetail
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this DeploymentHostDetail.


        :param permission: The permission of this DeploymentHostDetail.
        :type: PermissionHostDetail
        """
        self._permission = permission

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
        if not isinstance(other, DeploymentHostDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
