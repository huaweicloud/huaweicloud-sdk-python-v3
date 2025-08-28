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
        'protect_degradation': 'bool',
        'degradation_reason': 'str',
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
        'protect_degradation': 'protect_degradation',
        'degradation_reason': 'degradation_reason',
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

    def __init__(self, agent_id=None, host_id=None, host_name=None, host_status=None, agent_status=None, protect_status=None, protect_interrupt=None, protect_degradation=None, degradation_reason=None, container_tags=None, private_ip=None, public_ip=None, resource_id=None, group_name=None, enterprise_project_name=None, detect_result=None, asset=None, vulnerability=None, intrusion=None, policy_group_id=None, policy_group_name=None):
        r"""ContainerNodeInfo

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释**: Agent ID **取值范围**: 字符长度0-64位 
        :type agent_id: str
        :param host_id: **参数解释**: 服务器ID **取值范围**: 字符长度0-128位 
        :type host_id: str
        :param host_name: **参数解释**: 节点名称 **取值范围**: 字符长度0-128位 
        :type host_name: str
        :param host_status: **参数解释**: 服务器状态 **取值范围**: 包含如下4种。   - ACTIVE：正在运行。   - SHUTOFF：关机。   - BUILDING：创建中。   - ERROR：故障。 
        :type host_status: str
        :param agent_status: **参数解释**: Agent状态 **取值范围**: 包含如下3种。   - not_installed：未安装。   - online：在线。   - offline：离线。 
        :type agent_status: str
        :param protect_status: **参数解释**: 防护状态 **取值范围**: 包含如下2种。   - closed ：关闭。   - opened ：开启。 
        :type protect_status: str
        :param protect_interrupt: **参数解释**: 防护是否中断 **取值范围**:   - true：防护中断。   - false：防护未中断。 
        :type protect_interrupt: bool
        :param protect_degradation: **参数解释**: 防护是否降级 **取值范围**:   - true：防护降级。   - false：防护未降级。 
        :type protect_degradation: bool
        :param degradation_reason: **参数解释**: 防护降级原因 **取值范围**: 字符长度1-32位 
        :type degradation_reason: str
        :param container_tags: **参数解释**: 用来识别cce容器节点和自建节点的标签 **取值范围**: 包含如下3种。 - cce：cce节点 - self：自建节点 - other：其他节点 
        :type container_tags: str
        :param private_ip: **参数解释**: 私有IP地址 **取值范围**: 字符长度0-128位 
        :type private_ip: str
        :param public_ip: **参数解释**: 弹性公网IP地址 **取值范围**: 字符长度0-128位 
        :type public_ip: str
        :param resource_id: **参数解释**: 主机安全配额ID（UUID） **取值范围**: 字符长度0-128位 
        :type resource_id: str
        :param group_name: **参数解释**: 服务器组名称 **取值范围**: 字符长度1-128位 
        :type group_name: str
        :param enterprise_project_name: **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-256位 
        :type enterprise_project_name: str
        :param detect_result: **参数解释**: 云主机安全检测结果 **取值范围**: 包含如下4种。 - undetected：未检测。 - clean：无风险。 - risk：有风险。 - scanning：检测中。 
        :type detect_result: str
        :param asset: **参数解释**: 资产风险 **取值范围**: 取值0-2097152 
        :type asset: int
        :param vulnerability: **参数解释**: 漏洞风险 **取值范围**: 取值0-2097152 
        :type vulnerability: int
        :param intrusion: **参数解释**: 入侵风险 **取值范围**: 取值0-2097152 
        :type intrusion: int
        :param policy_group_id: **参数解释**: 策略组ID **取值范围**: 字符长度1-128位 
        :type policy_group_id: str
        :param policy_group_name: **参数解释**: 策略组名称 **取值范围**: 字符长度1-128位 
        :type policy_group_name: str
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._host_status = None
        self._agent_status = None
        self._protect_status = None
        self._protect_interrupt = None
        self._protect_degradation = None
        self._degradation_reason = None
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
        if protect_degradation is not None:
            self.protect_degradation = protect_degradation
        if degradation_reason is not None:
            self.degradation_reason = degradation_reason
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
        r"""Gets the agent_id of this ContainerNodeInfo.

        **参数解释**: Agent ID **取值范围**: 字符长度0-64位 

        :return: The agent_id of this ContainerNodeInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ContainerNodeInfo.

        **参数解释**: Agent ID **取值范围**: 字符长度0-64位 

        :param agent_id: The agent_id of this ContainerNodeInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ContainerNodeInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度0-128位 

        :return: The host_id of this ContainerNodeInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ContainerNodeInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度0-128位 

        :param host_id: The host_id of this ContainerNodeInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ContainerNodeInfo.

        **参数解释**: 节点名称 **取值范围**: 字符长度0-128位 

        :return: The host_name of this ContainerNodeInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ContainerNodeInfo.

        **参数解释**: 节点名称 **取值范围**: 字符长度0-128位 

        :param host_name: The host_name of this ContainerNodeInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_status(self):
        r"""Gets the host_status of this ContainerNodeInfo.

        **参数解释**: 服务器状态 **取值范围**: 包含如下4种。   - ACTIVE：正在运行。   - SHUTOFF：关机。   - BUILDING：创建中。   - ERROR：故障。 

        :return: The host_status of this ContainerNodeInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ContainerNodeInfo.

        **参数解释**: 服务器状态 **取值范围**: 包含如下4种。   - ACTIVE：正在运行。   - SHUTOFF：关机。   - BUILDING：创建中。   - ERROR：故障。 

        :param host_status: The host_status of this ContainerNodeInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ContainerNodeInfo.

        **参数解释**: Agent状态 **取值范围**: 包含如下3种。   - not_installed：未安装。   - online：在线。   - offline：离线。 

        :return: The agent_status of this ContainerNodeInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ContainerNodeInfo.

        **参数解释**: Agent状态 **取值范围**: 包含如下3种。   - not_installed：未安装。   - online：在线。   - offline：离线。 

        :param agent_status: The agent_status of this ContainerNodeInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ContainerNodeInfo.

        **参数解释**: 防护状态 **取值范围**: 包含如下2种。   - closed ：关闭。   - opened ：开启。 

        :return: The protect_status of this ContainerNodeInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ContainerNodeInfo.

        **参数解释**: 防护状态 **取值范围**: 包含如下2种。   - closed ：关闭。   - opened ：开启。 

        :param protect_status: The protect_status of this ContainerNodeInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def protect_interrupt(self):
        r"""Gets the protect_interrupt of this ContainerNodeInfo.

        **参数解释**: 防护是否中断 **取值范围**:   - true：防护中断。   - false：防护未中断。 

        :return: The protect_interrupt of this ContainerNodeInfo.
        :rtype: bool
        """
        return self._protect_interrupt

    @protect_interrupt.setter
    def protect_interrupt(self, protect_interrupt):
        r"""Sets the protect_interrupt of this ContainerNodeInfo.

        **参数解释**: 防护是否中断 **取值范围**:   - true：防护中断。   - false：防护未中断。 

        :param protect_interrupt: The protect_interrupt of this ContainerNodeInfo.
        :type protect_interrupt: bool
        """
        self._protect_interrupt = protect_interrupt

    @property
    def protect_degradation(self):
        r"""Gets the protect_degradation of this ContainerNodeInfo.

        **参数解释**: 防护是否降级 **取值范围**:   - true：防护降级。   - false：防护未降级。 

        :return: The protect_degradation of this ContainerNodeInfo.
        :rtype: bool
        """
        return self._protect_degradation

    @protect_degradation.setter
    def protect_degradation(self, protect_degradation):
        r"""Sets the protect_degradation of this ContainerNodeInfo.

        **参数解释**: 防护是否降级 **取值范围**:   - true：防护降级。   - false：防护未降级。 

        :param protect_degradation: The protect_degradation of this ContainerNodeInfo.
        :type protect_degradation: bool
        """
        self._protect_degradation = protect_degradation

    @property
    def degradation_reason(self):
        r"""Gets the degradation_reason of this ContainerNodeInfo.

        **参数解释**: 防护降级原因 **取值范围**: 字符长度1-32位 

        :return: The degradation_reason of this ContainerNodeInfo.
        :rtype: str
        """
        return self._degradation_reason

    @degradation_reason.setter
    def degradation_reason(self, degradation_reason):
        r"""Sets the degradation_reason of this ContainerNodeInfo.

        **参数解释**: 防护降级原因 **取值范围**: 字符长度1-32位 

        :param degradation_reason: The degradation_reason of this ContainerNodeInfo.
        :type degradation_reason: str
        """
        self._degradation_reason = degradation_reason

    @property
    def container_tags(self):
        r"""Gets the container_tags of this ContainerNodeInfo.

        **参数解释**: 用来识别cce容器节点和自建节点的标签 **取值范围**: 包含如下3种。 - cce：cce节点 - self：自建节点 - other：其他节点 

        :return: The container_tags of this ContainerNodeInfo.
        :rtype: str
        """
        return self._container_tags

    @container_tags.setter
    def container_tags(self, container_tags):
        r"""Sets the container_tags of this ContainerNodeInfo.

        **参数解释**: 用来识别cce容器节点和自建节点的标签 **取值范围**: 包含如下3种。 - cce：cce节点 - self：自建节点 - other：其他节点 

        :param container_tags: The container_tags of this ContainerNodeInfo.
        :type container_tags: str
        """
        self._container_tags = container_tags

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ContainerNodeInfo.

        **参数解释**: 私有IP地址 **取值范围**: 字符长度0-128位 

        :return: The private_ip of this ContainerNodeInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ContainerNodeInfo.

        **参数解释**: 私有IP地址 **取值范围**: 字符长度0-128位 

        :param private_ip: The private_ip of this ContainerNodeInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ContainerNodeInfo.

        **参数解释**: 弹性公网IP地址 **取值范围**: 字符长度0-128位 

        :return: The public_ip of this ContainerNodeInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ContainerNodeInfo.

        **参数解释**: 弹性公网IP地址 **取值范围**: 字符长度0-128位 

        :param public_ip: The public_ip of this ContainerNodeInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ContainerNodeInfo.

        **参数解释**: 主机安全配额ID（UUID） **取值范围**: 字符长度0-128位 

        :return: The resource_id of this ContainerNodeInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ContainerNodeInfo.

        **参数解释**: 主机安全配额ID（UUID） **取值范围**: 字符长度0-128位 

        :param resource_id: The resource_id of this ContainerNodeInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ContainerNodeInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符长度1-128位 

        :return: The group_name of this ContainerNodeInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ContainerNodeInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符长度1-128位 

        :param group_name: The group_name of this ContainerNodeInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this ContainerNodeInfo.

        **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-256位 

        :return: The enterprise_project_name of this ContainerNodeInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this ContainerNodeInfo.

        **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-256位 

        :param enterprise_project_name: The enterprise_project_name of this ContainerNodeInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def detect_result(self):
        r"""Gets the detect_result of this ContainerNodeInfo.

        **参数解释**: 云主机安全检测结果 **取值范围**: 包含如下4种。 - undetected：未检测。 - clean：无风险。 - risk：有风险。 - scanning：检测中。 

        :return: The detect_result of this ContainerNodeInfo.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        r"""Sets the detect_result of this ContainerNodeInfo.

        **参数解释**: 云主机安全检测结果 **取值范围**: 包含如下4种。 - undetected：未检测。 - clean：无风险。 - risk：有风险。 - scanning：检测中。 

        :param detect_result: The detect_result of this ContainerNodeInfo.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def asset(self):
        r"""Gets the asset of this ContainerNodeInfo.

        **参数解释**: 资产风险 **取值范围**: 取值0-2097152 

        :return: The asset of this ContainerNodeInfo.
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        r"""Sets the asset of this ContainerNodeInfo.

        **参数解释**: 资产风险 **取值范围**: 取值0-2097152 

        :param asset: The asset of this ContainerNodeInfo.
        :type asset: int
        """
        self._asset = asset

    @property
    def vulnerability(self):
        r"""Gets the vulnerability of this ContainerNodeInfo.

        **参数解释**: 漏洞风险 **取值范围**: 取值0-2097152 

        :return: The vulnerability of this ContainerNodeInfo.
        :rtype: int
        """
        return self._vulnerability

    @vulnerability.setter
    def vulnerability(self, vulnerability):
        r"""Sets the vulnerability of this ContainerNodeInfo.

        **参数解释**: 漏洞风险 **取值范围**: 取值0-2097152 

        :param vulnerability: The vulnerability of this ContainerNodeInfo.
        :type vulnerability: int
        """
        self._vulnerability = vulnerability

    @property
    def intrusion(self):
        r"""Gets the intrusion of this ContainerNodeInfo.

        **参数解释**: 入侵风险 **取值范围**: 取值0-2097152 

        :return: The intrusion of this ContainerNodeInfo.
        :rtype: int
        """
        return self._intrusion

    @intrusion.setter
    def intrusion(self, intrusion):
        r"""Sets the intrusion of this ContainerNodeInfo.

        **参数解释**: 入侵风险 **取值范围**: 取值0-2097152 

        :param intrusion: The intrusion of this ContainerNodeInfo.
        :type intrusion: int
        """
        self._intrusion = intrusion

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this ContainerNodeInfo.

        **参数解释**: 策略组ID **取值范围**: 字符长度1-128位 

        :return: The policy_group_id of this ContainerNodeInfo.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this ContainerNodeInfo.

        **参数解释**: 策略组ID **取值范围**: 字符长度1-128位 

        :param policy_group_id: The policy_group_id of this ContainerNodeInfo.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this ContainerNodeInfo.

        **参数解释**: 策略组名称 **取值范围**: 字符长度1-128位 

        :return: The policy_group_name of this ContainerNodeInfo.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this ContainerNodeInfo.

        **参数解释**: 策略组名称 **取值范围**: 字符长度1-128位 

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
