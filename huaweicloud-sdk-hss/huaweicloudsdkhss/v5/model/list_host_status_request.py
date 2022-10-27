# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'version': 'str',
        'agent_status': 'str',
        'detect_result': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'host_status': 'str',
        'os_type': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'ip_addr': 'str',
        'protect_status': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'policy_group_id': 'str',
        'policy_group_name': 'str',
        'charging_mode': 'str',
        'refresh': 'bool',
        'above_version': 'bool',
        'outside_host': 'bool',
        'asset_value': 'str',
        'label': 'str',
        'server_group': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'version': 'version',
        'agent_status': 'agent_status',
        'detect_result': 'detect_result',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'host_status': 'host_status',
        'os_type': 'os_type',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'ip_addr': 'ip_addr',
        'protect_status': 'protect_status',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'policy_group_id': 'policy_group_id',
        'policy_group_name': 'policy_group_name',
        'charging_mode': 'charging_mode',
        'refresh': 'refresh',
        'above_version': 'above_version',
        'outside_host': 'outside_host',
        'asset_value': 'asset_value',
        'label': 'label',
        'server_group': 'server_group',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, region=None, enterprise_project_id=None, version=None, agent_status=None, detect_result=None, host_name=None, host_id=None, host_status=None, os_type=None, private_ip=None, public_ip=None, ip_addr=None, protect_status=None, group_id=None, group_name=None, policy_group_id=None, policy_group_name=None, charging_mode=None, refresh=None, above_version=None, outside_host=None, asset_value=None, label=None, server_group=None, limit=None, offset=None):
        """ListHostStatusRequest

        The model defined in huaweicloud sdk

        :param region: region id
        :type region: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param version: 主机开通的版本，包含如下6种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。
        :type version: str
        :param agent_status: Agent状态，包含如下5种。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。
        :type agent_status: str
        :param detect_result: 检测结果，包含如下4种。   - undetected ：未检测。   - clean ：无风险。   - risk ：有风险。   - scanning ：检测中。
        :type detect_result: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 服务器ID
        :type host_id: str
        :param host_status: 主机状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。
        :type host_status: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。
        :type os_type: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param ip_addr: 公网或私网IP
        :type ip_addr: str
        :param protect_status: 防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。
        :type protect_status: str
        :param group_id: 服务器组ID
        :type group_id: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param policy_group_id: 策略组ID
        :type policy_group_id: str
        :param policy_group_name: 策略组名称
        :type policy_group_name: str
        :param charging_mode: 收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。
        :type charging_mode: str
        :param refresh: 是否强制从ECS同步主机
        :type refresh: bool
        :param above_version: 是否返回比当前版本高的所有版本
        :type above_version: bool
        :param outside_host: 是否华为云主机
        :type outside_host: bool
        :param asset_value: 资产重要性，包含如下4种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param label: 资产标签
        :type label: str
        :param server_group: 资产服务器组
        :type server_group: str
        :param limit: 每页显示个数，默认10
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._version = None
        self._agent_status = None
        self._detect_result = None
        self._host_name = None
        self._host_id = None
        self._host_status = None
        self._os_type = None
        self._private_ip = None
        self._public_ip = None
        self._ip_addr = None
        self._protect_status = None
        self._group_id = None
        self._group_name = None
        self._policy_group_id = None
        self._policy_group_name = None
        self._charging_mode = None
        self._refresh = None
        self._above_version = None
        self._outside_host = None
        self._asset_value = None
        self._label = None
        self._server_group = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if version is not None:
            self.version = version
        if agent_status is not None:
            self.agent_status = agent_status
        if detect_result is not None:
            self.detect_result = detect_result
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if host_status is not None:
            self.host_status = host_status
        if os_type is not None:
            self.os_type = os_type
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if ip_addr is not None:
            self.ip_addr = ip_addr
        if protect_status is not None:
            self.protect_status = protect_status
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if refresh is not None:
            self.refresh = refresh
        if above_version is not None:
            self.above_version = above_version
        if outside_host is not None:
            self.outside_host = outside_host
        if asset_value is not None:
            self.asset_value = asset_value
        if label is not None:
            self.label = label
        if server_group is not None:
            self.server_group = server_group
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def region(self):
        """Gets the region of this ListHostStatusRequest.

        region id

        :return: The region of this ListHostStatusRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListHostStatusRequest.

        region id

        :param region: The region of this ListHostStatusRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListHostStatusRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListHostStatusRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListHostStatusRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListHostStatusRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def version(self):
        """Gets the version of this ListHostStatusRequest.

        主机开通的版本，包含如下6种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。

        :return: The version of this ListHostStatusRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListHostStatusRequest.

        主机开通的版本，包含如下6种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。

        :param version: The version of this ListHostStatusRequest.
        :type version: str
        """
        self._version = version

    @property
    def agent_status(self):
        """Gets the agent_status of this ListHostStatusRequest.

        Agent状态，包含如下5种。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。

        :return: The agent_status of this ListHostStatusRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this ListHostStatusRequest.

        Agent状态，包含如下5种。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。

        :param agent_status: The agent_status of this ListHostStatusRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def detect_result(self):
        """Gets the detect_result of this ListHostStatusRequest.

        检测结果，包含如下4种。   - undetected ：未检测。   - clean ：无风险。   - risk ：有风险。   - scanning ：检测中。

        :return: The detect_result of this ListHostStatusRequest.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        """Sets the detect_result of this ListHostStatusRequest.

        检测结果，包含如下4种。   - undetected ：未检测。   - clean ：无风险。   - risk ：有风险。   - scanning ：检测中。

        :param detect_result: The detect_result of this ListHostStatusRequest.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def host_name(self):
        """Gets the host_name of this ListHostStatusRequest.

        服务器名称

        :return: The host_name of this ListHostStatusRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListHostStatusRequest.

        服务器名称

        :param host_name: The host_name of this ListHostStatusRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        """Gets the host_id of this ListHostStatusRequest.

        服务器ID

        :return: The host_id of this ListHostStatusRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListHostStatusRequest.

        服务器ID

        :param host_id: The host_id of this ListHostStatusRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_status(self):
        """Gets the host_status of this ListHostStatusRequest.

        主机状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :return: The host_status of this ListHostStatusRequest.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this ListHostStatusRequest.

        主机状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :param host_status: The host_status of this ListHostStatusRequest.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def os_type(self):
        """Gets the os_type of this ListHostStatusRequest.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :return: The os_type of this ListHostStatusRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListHostStatusRequest.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :param os_type: The os_type of this ListHostStatusRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def private_ip(self):
        """Gets the private_ip of this ListHostStatusRequest.

        服务器私有IP

        :return: The private_ip of this ListHostStatusRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ListHostStatusRequest.

        服务器私有IP

        :param private_ip: The private_ip of this ListHostStatusRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this ListHostStatusRequest.

        服务器公网IP

        :return: The public_ip of this ListHostStatusRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ListHostStatusRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListHostStatusRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def ip_addr(self):
        """Gets the ip_addr of this ListHostStatusRequest.

        公网或私网IP

        :return: The ip_addr of this ListHostStatusRequest.
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        """Sets the ip_addr of this ListHostStatusRequest.

        公网或私网IP

        :param ip_addr: The ip_addr of this ListHostStatusRequest.
        :type ip_addr: str
        """
        self._ip_addr = ip_addr

    @property
    def protect_status(self):
        """Gets the protect_status of this ListHostStatusRequest.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :return: The protect_status of this ListHostStatusRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ListHostStatusRequest.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :param protect_status: The protect_status of this ListHostStatusRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def group_id(self):
        """Gets the group_id of this ListHostStatusRequest.

        服务器组ID

        :return: The group_id of this ListHostStatusRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListHostStatusRequest.

        服务器组ID

        :param group_id: The group_id of this ListHostStatusRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this ListHostStatusRequest.

        服务器组名称

        :return: The group_name of this ListHostStatusRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ListHostStatusRequest.

        服务器组名称

        :param group_name: The group_name of this ListHostStatusRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def policy_group_id(self):
        """Gets the policy_group_id of this ListHostStatusRequest.

        策略组ID

        :return: The policy_group_id of this ListHostStatusRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        """Sets the policy_group_id of this ListHostStatusRequest.

        策略组ID

        :param policy_group_id: The policy_group_id of this ListHostStatusRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        """Gets the policy_group_name of this ListHostStatusRequest.

        策略组名称

        :return: The policy_group_name of this ListHostStatusRequest.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        """Sets the policy_group_name of this ListHostStatusRequest.

        策略组名称

        :param policy_group_name: The policy_group_name of this ListHostStatusRequest.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ListHostStatusRequest.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :return: The charging_mode of this ListHostStatusRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ListHostStatusRequest.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :param charging_mode: The charging_mode of this ListHostStatusRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def refresh(self):
        """Gets the refresh of this ListHostStatusRequest.

        是否强制从ECS同步主机

        :return: The refresh of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this ListHostStatusRequest.

        是否强制从ECS同步主机

        :param refresh: The refresh of this ListHostStatusRequest.
        :type refresh: bool
        """
        self._refresh = refresh

    @property
    def above_version(self):
        """Gets the above_version of this ListHostStatusRequest.

        是否返回比当前版本高的所有版本

        :return: The above_version of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._above_version

    @above_version.setter
    def above_version(self, above_version):
        """Sets the above_version of this ListHostStatusRequest.

        是否返回比当前版本高的所有版本

        :param above_version: The above_version of this ListHostStatusRequest.
        :type above_version: bool
        """
        self._above_version = above_version

    @property
    def outside_host(self):
        """Gets the outside_host of this ListHostStatusRequest.

        是否华为云主机

        :return: The outside_host of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._outside_host

    @outside_host.setter
    def outside_host(self, outside_host):
        """Sets the outside_host of this ListHostStatusRequest.

        是否华为云主机

        :param outside_host: The outside_host of this ListHostStatusRequest.
        :type outside_host: bool
        """
        self._outside_host = outside_host

    @property
    def asset_value(self):
        """Gets the asset_value of this ListHostStatusRequest.

        资产重要性，包含如下4种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ListHostStatusRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        """Sets the asset_value of this ListHostStatusRequest.

        资产重要性，包含如下4种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ListHostStatusRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def label(self):
        """Gets the label of this ListHostStatusRequest.

        资产标签

        :return: The label of this ListHostStatusRequest.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ListHostStatusRequest.

        资产标签

        :param label: The label of this ListHostStatusRequest.
        :type label: str
        """
        self._label = label

    @property
    def server_group(self):
        """Gets the server_group of this ListHostStatusRequest.

        资产服务器组

        :return: The server_group of this ListHostStatusRequest.
        :rtype: str
        """
        return self._server_group

    @server_group.setter
    def server_group(self, server_group):
        """Sets the server_group of this ListHostStatusRequest.

        资产服务器组

        :param server_group: The server_group of this ListHostStatusRequest.
        :type server_group: str
        """
        self._server_group = server_group

    @property
    def limit(self):
        """Gets the limit of this ListHostStatusRequest.

        每页显示个数，默认10

        :return: The limit of this ListHostStatusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHostStatusRequest.

        每页显示个数，默认10

        :param limit: The limit of this ListHostStatusRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListHostStatusRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListHostStatusRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHostStatusRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListHostStatusRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListHostStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
