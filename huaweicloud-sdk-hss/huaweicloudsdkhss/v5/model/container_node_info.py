# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerNodeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'host_status': 'str',
        'agent_status': 'str',
        'protect_status': 'str',
        'protect_interrupt': 'bool',
        'container_tags': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'resource_id': 'str',
        'group_name': 'str',
        'enterprise_project_name': 'str',
        'detect_result': 'str',
        'asset': 'int',
        'vulnerability': 'int',
        'intrusion': 'int',
        'policy_group_id': 'str',
        'policy_group_name': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'protect_status': 'protect_status',
        'protect_interrupt': 'protect_interrupt',
        'container_tags': 'container_tags',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'resource_id': 'resource_id',
        'group_name': 'group_name',
        'enterprise_project_name': 'enterprise_project_name',
        'detect_result': 'detect_result',
        'asset': 'asset',
        'vulnerability': 'vulnerability',
        'intrusion': 'intrusion',
        'policy_group_id': 'policy_group_id',
        'policy_group_name': 'policy_group_name'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, host_status=None, agent_status=None, protect_status=None, protect_interrupt=None, container_tags=None, private_ip=None, public_ip=None, resource_id=None, group_name=None, enterprise_project_name=None, detect_result=None, asset=None, vulnerability=None, intrusion=None, policy_group_id=None, policy_group_name=None):
        """ContainerNodeInfo

        The model defined in huaweicloud sdk

        :param agent_id: Agent ID
        :type agent_id: str
        :param host_id: 服务器ID
        :type host_id: str
        :param host_name: 节点名称
        :type host_name: str
        :param host_status: 服务器状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。
        :type host_status: str
        :param agent_status: Agent状态，包含如下3种。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。
        :type agent_status: str
        :param protect_status: 防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。
        :type protect_status: str
        :param protect_interrupt: 防护是否中断
        :type protect_interrupt: bool
        :param container_tags: 标签：用来识别cce容器节点和自建  - cce：cce节点  - self：自建节点  - other：其他节点
        :type container_tags: str
        :param private_ip: 私有IP地址
        :type private_ip: str
        :param public_ip: 弹性公网IP地址
        :type public_ip: str
        :param resource_id: 主机安全配额ID（UUID）
        :type resource_id: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param enterprise_project_name: 所属企业项目名称
        :type enterprise_project_name: str
        :param detect_result: 云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。
        :type detect_result: str
        :param asset: 资产风险
        :type asset: int
        :param vulnerability: 漏洞风险
        :type vulnerability: int
        :param intrusion: 入侵风险
        :type intrusion: int
        :param policy_group_id: 策略组ID
        :type policy_group_id: str
        :param policy_group_name: 策略组名称
        :type policy_group_name: str
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._host_status = None
        self._agent_status = None
        self._protect_status = None
        self._protect_interrupt = None
        self._container_tags = None
        self._private_ip = None
        self._public_ip = None
        self._resource_id = None
        self._group_name = None
        self._enterprise_project_name = None
        self._detect_result = None
        self._asset = None
        self._vulnerability = None
        self._intrusion = None
        self._policy_group_id = None
        self._policy_group_name = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_status is not None:
            self.host_status = host_status
        if agent_status is not None:
            self.agent_status = agent_status
        if protect_status is not None:
            self.protect_status = protect_status
        if protect_interrupt is not None:
            self.protect_interrupt = protect_interrupt
        if container_tags is not None:
            self.container_tags = container_tags
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if resource_id is not None:
            self.resource_id = resource_id
        if group_name is not None:
            self.group_name = group_name
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if detect_result is not None:
            self.detect_result = detect_result
        if asset is not None:
            self.asset = asset
        if vulnerability is not None:
            self.vulnerability = vulnerability
        if intrusion is not None:
            self.intrusion = intrusion
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name

    @property
    def agent_id(self):
        """Gets the agent_id of this ContainerNodeInfo.

        Agent ID

        :return: The agent_id of this ContainerNodeInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this ContainerNodeInfo.

        Agent ID

        :param agent_id: The agent_id of this ContainerNodeInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        """Gets the host_id of this ContainerNodeInfo.

        服务器ID

        :return: The host_id of this ContainerNodeInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ContainerNodeInfo.

        服务器ID

        :param host_id: The host_id of this ContainerNodeInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this ContainerNodeInfo.

        节点名称

        :return: The host_name of this ContainerNodeInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ContainerNodeInfo.

        节点名称

        :param host_name: The host_name of this ContainerNodeInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_status(self):
        """Gets the host_status of this ContainerNodeInfo.

        服务器状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :return: The host_status of this ContainerNodeInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this ContainerNodeInfo.

        服务器状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :param host_status: The host_status of this ContainerNodeInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        """Gets the agent_status of this ContainerNodeInfo.

        Agent状态，包含如下3种。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。

        :return: The agent_status of this ContainerNodeInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this ContainerNodeInfo.

        Agent状态，包含如下3种。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。

        :param agent_status: The agent_status of this ContainerNodeInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def protect_status(self):
        """Gets the protect_status of this ContainerNodeInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :return: The protect_status of this ContainerNodeInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ContainerNodeInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :param protect_status: The protect_status of this ContainerNodeInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def protect_interrupt(self):
        """Gets the protect_interrupt of this ContainerNodeInfo.

        防护是否中断

        :return: The protect_interrupt of this ContainerNodeInfo.
        :rtype: bool
        """
        return self._protect_interrupt

    @protect_interrupt.setter
    def protect_interrupt(self, protect_interrupt):
        """Sets the protect_interrupt of this ContainerNodeInfo.

        防护是否中断

        :param protect_interrupt: The protect_interrupt of this ContainerNodeInfo.
        :type protect_interrupt: bool
        """
        self._protect_interrupt = protect_interrupt

    @property
    def container_tags(self):
        """Gets the container_tags of this ContainerNodeInfo.

        标签：用来识别cce容器节点和自建  - cce：cce节点  - self：自建节点  - other：其他节点

        :return: The container_tags of this ContainerNodeInfo.
        :rtype: str
        """
        return self._container_tags

    @container_tags.setter
    def container_tags(self, container_tags):
        """Sets the container_tags of this ContainerNodeInfo.

        标签：用来识别cce容器节点和自建  - cce：cce节点  - self：自建节点  - other：其他节点

        :param container_tags: The container_tags of this ContainerNodeInfo.
        :type container_tags: str
        """
        self._container_tags = container_tags

    @property
    def private_ip(self):
        """Gets the private_ip of this ContainerNodeInfo.

        私有IP地址

        :return: The private_ip of this ContainerNodeInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ContainerNodeInfo.

        私有IP地址

        :param private_ip: The private_ip of this ContainerNodeInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this ContainerNodeInfo.

        弹性公网IP地址

        :return: The public_ip of this ContainerNodeInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ContainerNodeInfo.

        弹性公网IP地址

        :param public_ip: The public_ip of this ContainerNodeInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def resource_id(self):
        """Gets the resource_id of this ContainerNodeInfo.

        主机安全配额ID（UUID）

        :return: The resource_id of this ContainerNodeInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ContainerNodeInfo.

        主机安全配额ID（UUID）

        :param resource_id: The resource_id of this ContainerNodeInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def group_name(self):
        """Gets the group_name of this ContainerNodeInfo.

        服务器组名称

        :return: The group_name of this ContainerNodeInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ContainerNodeInfo.

        服务器组名称

        :param group_name: The group_name of this ContainerNodeInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this ContainerNodeInfo.

        所属企业项目名称

        :return: The enterprise_project_name of this ContainerNodeInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this ContainerNodeInfo.

        所属企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this ContainerNodeInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def detect_result(self):
        """Gets the detect_result of this ContainerNodeInfo.

        云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。

        :return: The detect_result of this ContainerNodeInfo.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        """Sets the detect_result of this ContainerNodeInfo.

        云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。

        :param detect_result: The detect_result of this ContainerNodeInfo.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def asset(self):
        """Gets the asset of this ContainerNodeInfo.

        资产风险

        :return: The asset of this ContainerNodeInfo.
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this ContainerNodeInfo.

        资产风险

        :param asset: The asset of this ContainerNodeInfo.
        :type asset: int
        """
        self._asset = asset

    @property
    def vulnerability(self):
        """Gets the vulnerability of this ContainerNodeInfo.

        漏洞风险

        :return: The vulnerability of this ContainerNodeInfo.
        :rtype: int
        """
        return self._vulnerability

    @vulnerability.setter
    def vulnerability(self, vulnerability):
        """Sets the vulnerability of this ContainerNodeInfo.

        漏洞风险

        :param vulnerability: The vulnerability of this ContainerNodeInfo.
        :type vulnerability: int
        """
        self._vulnerability = vulnerability

    @property
    def intrusion(self):
        """Gets the intrusion of this ContainerNodeInfo.

        入侵风险

        :return: The intrusion of this ContainerNodeInfo.
        :rtype: int
        """
        return self._intrusion

    @intrusion.setter
    def intrusion(self, intrusion):
        """Sets the intrusion of this ContainerNodeInfo.

        入侵风险

        :param intrusion: The intrusion of this ContainerNodeInfo.
        :type intrusion: int
        """
        self._intrusion = intrusion

    @property
    def policy_group_id(self):
        """Gets the policy_group_id of this ContainerNodeInfo.

        策略组ID

        :return: The policy_group_id of this ContainerNodeInfo.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        """Sets the policy_group_id of this ContainerNodeInfo.

        策略组ID

        :param policy_group_id: The policy_group_id of this ContainerNodeInfo.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        """Gets the policy_group_name of this ContainerNodeInfo.

        策略组名称

        :return: The policy_group_name of this ContainerNodeInfo.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        """Sets the policy_group_name of this ContainerNodeInfo.

        策略组名称

        :param policy_group_name: The policy_group_name of this ContainerNodeInfo.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

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
        if not isinstance(other, ContainerNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
