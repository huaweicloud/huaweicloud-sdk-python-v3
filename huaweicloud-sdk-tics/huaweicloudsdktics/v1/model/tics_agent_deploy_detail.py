# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsAgentDeployDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_access_address': 'str',
        'agent_id': 'str',
        'cce_cluster_id': 'str',
        'cce_cluster_name': 'str',
        'console_ip': 'str',
        'console_port': 'int',
        'host_path': 'str',
        'namespace_name': 'str',
        'obs_pvc_name': 'str',
        'persistence_id': 'str',
        'resource_spec_code': 'str',
        'web_port': 'int'
    }

    attribute_map = {
        'agent_access_address': 'agent_access_address',
        'agent_id': 'agent_id',
        'cce_cluster_id': 'cce_cluster_id',
        'cce_cluster_name': 'cce_cluster_name',
        'console_ip': 'console_ip',
        'console_port': 'console_port',
        'host_path': 'host_path',
        'namespace_name': 'namespace_name',
        'obs_pvc_name': 'obs_pvc_name',
        'persistence_id': 'persistence_id',
        'resource_spec_code': 'resource_spec_code',
        'web_port': 'web_port'
    }

    def __init__(self, agent_access_address=None, agent_id=None, cce_cluster_id=None, cce_cluster_name=None, console_ip=None, console_port=None, host_path=None, namespace_name=None, obs_pvc_name=None, persistence_id=None, resource_spec_code=None, web_port=None):
        """TicsAgentDeployDetail

        The model defined in huaweicloud sdk

        :param agent_access_address: 可信节点访问地址
        :type agent_access_address: str
        :param agent_id: 可信节点Id
        :type agent_id: str
        :param cce_cluster_id: 可信节点所在cce集群的Id
        :type cce_cluster_id: str
        :param cce_cluster_name: 可信节点所在cce集群的名称
        :type cce_cluster_name: str
        :param console_ip: 可信节点所在ip
        :type console_ip: str
        :param console_port: 可信节点服务端口
        :type console_port: int
        :param host_path: 主机挂载路径，本地挂载才会有值
        :type host_path: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param obs_pvc_name: 可信节点CCE部署场景，对象文件存储PVC
        :type obs_pvc_name: str
        :param persistence_id: 持久化存储唯一标识
        :type persistence_id: str
        :param resource_spec_code: 代理部署规格
        :type resource_spec_code: str
        :param web_port: 可信节点访问端口
        :type web_port: int
        """
        
        

        self._agent_access_address = None
        self._agent_id = None
        self._cce_cluster_id = None
        self._cce_cluster_name = None
        self._console_ip = None
        self._console_port = None
        self._host_path = None
        self._namespace_name = None
        self._obs_pvc_name = None
        self._persistence_id = None
        self._resource_spec_code = None
        self._web_port = None
        self.discriminator = None

        if agent_access_address is not None:
            self.agent_access_address = agent_access_address
        if agent_id is not None:
            self.agent_id = agent_id
        if cce_cluster_id is not None:
            self.cce_cluster_id = cce_cluster_id
        if cce_cluster_name is not None:
            self.cce_cluster_name = cce_cluster_name
        if console_ip is not None:
            self.console_ip = console_ip
        if console_port is not None:
            self.console_port = console_port
        if host_path is not None:
            self.host_path = host_path
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if obs_pvc_name is not None:
            self.obs_pvc_name = obs_pvc_name
        if persistence_id is not None:
            self.persistence_id = persistence_id
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if web_port is not None:
            self.web_port = web_port

    @property
    def agent_access_address(self):
        """Gets the agent_access_address of this TicsAgentDeployDetail.

        可信节点访问地址

        :return: The agent_access_address of this TicsAgentDeployDetail.
        :rtype: str
        """
        return self._agent_access_address

    @agent_access_address.setter
    def agent_access_address(self, agent_access_address):
        """Sets the agent_access_address of this TicsAgentDeployDetail.

        可信节点访问地址

        :param agent_access_address: The agent_access_address of this TicsAgentDeployDetail.
        :type agent_access_address: str
        """
        self._agent_access_address = agent_access_address

    @property
    def agent_id(self):
        """Gets the agent_id of this TicsAgentDeployDetail.

        可信节点Id

        :return: The agent_id of this TicsAgentDeployDetail.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this TicsAgentDeployDetail.

        可信节点Id

        :param agent_id: The agent_id of this TicsAgentDeployDetail.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def cce_cluster_id(self):
        """Gets the cce_cluster_id of this TicsAgentDeployDetail.

        可信节点所在cce集群的Id

        :return: The cce_cluster_id of this TicsAgentDeployDetail.
        :rtype: str
        """
        return self._cce_cluster_id

    @cce_cluster_id.setter
    def cce_cluster_id(self, cce_cluster_id):
        """Sets the cce_cluster_id of this TicsAgentDeployDetail.

        可信节点所在cce集群的Id

        :param cce_cluster_id: The cce_cluster_id of this TicsAgentDeployDetail.
        :type cce_cluster_id: str
        """
        self._cce_cluster_id = cce_cluster_id

    @property
    def cce_cluster_name(self):
        """Gets the cce_cluster_name of this TicsAgentDeployDetail.

        可信节点所在cce集群的名称

        :return: The cce_cluster_name of this TicsAgentDeployDetail.
        :rtype: str
        """
        return self._cce_cluster_name

    @cce_cluster_name.setter
    def cce_cluster_name(self, cce_cluster_name):
        """Sets the cce_cluster_name of this TicsAgentDeployDetail.

        可信节点所在cce集群的名称

        :param cce_cluster_name: The cce_cluster_name of this TicsAgentDeployDetail.
        :type cce_cluster_name: str
        """
        self._cce_cluster_name = cce_cluster_name

    @property
    def console_ip(self):
        """Gets the console_ip of this TicsAgentDeployDetail.

        可信节点所在ip

        :return: The console_ip of this TicsAgentDeployDetail.
        :rtype: str
        """
        return self._console_ip

    @console_ip.setter
    def console_ip(self, console_ip):
        """Sets the console_ip of this TicsAgentDeployDetail.

        可信节点所在ip

        :param console_ip: The console_ip of this TicsAgentDeployDetail.
        :type console_ip: str
        """
        self._console_ip = console_ip

    @property
    def console_port(self):
        """Gets the console_port of this TicsAgentDeployDetail.

        可信节点服务端口

        :return: The console_port of this TicsAgentDeployDetail.
        :rtype: int
        """
        return self._console_port

    @console_port.setter
    def console_port(self, console_port):
        """Sets the console_port of this TicsAgentDeployDetail.

        可信节点服务端口

        :param console_port: The console_port of this TicsAgentDeployDetail.
        :type console_port: int
        """
        self._console_port = console_port

    @property
    def host_path(self):
        """Gets the host_path of this TicsAgentDeployDetail.

        主机挂载路径，本地挂载才会有值

        :return: The host_path of this TicsAgentDeployDetail.
        :rtype: str
        """
        return self._host_path

    @host_path.setter
    def host_path(self, host_path):
        """Sets the host_path of this TicsAgentDeployDetail.

        主机挂载路径，本地挂载才会有值

        :param host_path: The host_path of this TicsAgentDeployDetail.
        :type host_path: str
        """
        self._host_path = host_path

    @property
    def namespace_name(self):
        """Gets the namespace_name of this TicsAgentDeployDetail.

        命名空间名称

        :return: The namespace_name of this TicsAgentDeployDetail.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """Sets the namespace_name of this TicsAgentDeployDetail.

        命名空间名称

        :param namespace_name: The namespace_name of this TicsAgentDeployDetail.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def obs_pvc_name(self):
        """Gets the obs_pvc_name of this TicsAgentDeployDetail.

        可信节点CCE部署场景，对象文件存储PVC

        :return: The obs_pvc_name of this TicsAgentDeployDetail.
        :rtype: str
        """
        return self._obs_pvc_name

    @obs_pvc_name.setter
    def obs_pvc_name(self, obs_pvc_name):
        """Sets the obs_pvc_name of this TicsAgentDeployDetail.

        可信节点CCE部署场景，对象文件存储PVC

        :param obs_pvc_name: The obs_pvc_name of this TicsAgentDeployDetail.
        :type obs_pvc_name: str
        """
        self._obs_pvc_name = obs_pvc_name

    @property
    def persistence_id(self):
        """Gets the persistence_id of this TicsAgentDeployDetail.

        持久化存储唯一标识

        :return: The persistence_id of this TicsAgentDeployDetail.
        :rtype: str
        """
        return self._persistence_id

    @persistence_id.setter
    def persistence_id(self, persistence_id):
        """Sets the persistence_id of this TicsAgentDeployDetail.

        持久化存储唯一标识

        :param persistence_id: The persistence_id of this TicsAgentDeployDetail.
        :type persistence_id: str
        """
        self._persistence_id = persistence_id

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this TicsAgentDeployDetail.

        代理部署规格

        :return: The resource_spec_code of this TicsAgentDeployDetail.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this TicsAgentDeployDetail.

        代理部署规格

        :param resource_spec_code: The resource_spec_code of this TicsAgentDeployDetail.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def web_port(self):
        """Gets the web_port of this TicsAgentDeployDetail.

        可信节点访问端口

        :return: The web_port of this TicsAgentDeployDetail.
        :rtype: int
        """
        return self._web_port

    @web_port.setter
    def web_port(self, web_port):
        """Sets the web_port of this TicsAgentDeployDetail.

        可信节点访问端口

        :param web_port: The web_port of this TicsAgentDeployDetail.
        :type web_port: int
        """
        self._web_port = web_port

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
        if not isinstance(other, TicsAgentDeployDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
