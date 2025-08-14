# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRansomwareProtectionNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'host_name': 'str',
        'host_id': 'str',
        'os_type': 'str',
        'host_ip': 'str',
        'private_ip': 'str',
        'host_status': 'str',
        'ransom_protection_status': 'str',
        'protect_policy_name': 'str',
        'policy_name': 'str',
        'policy_id': 'str',
        'agent_status': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'last_days': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'os_type': 'os_type',
        'host_ip': 'host_ip',
        'private_ip': 'private_ip',
        'host_status': 'host_status',
        'ransom_protection_status': 'ransom_protection_status',
        'protect_policy_name': 'protect_policy_name',
        'policy_name': 'policy_name',
        'policy_id': 'policy_id',
        'agent_status': 'agent_status',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'last_days': 'last_days'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, host_name=None, host_id=None, os_type=None, host_ip=None, private_ip=None, host_status=None, ransom_protection_status=None, protect_policy_name=None, policy_name=None, policy_id=None, agent_status=None, group_id=None, group_name=None, last_days=None):
        r"""ListRansomwareProtectionNodesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 服务器ID
        :type host_id: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。
        :type os_type: str
        :param host_ip: 服务器IP地址，服务器公网IP地址
        :type host_ip: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param host_status: 主机状态，包含如下3种。   - 不传参默认为全部。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。
        :type host_status: str
        :param ransom_protection_status: 勒索防护状态，包含如下6种。   - closed ：未开启。   - opened ：防护中。   - opening ：开启中。   - closing ：关闭中。   - protect_failed：防护失败。   - protect_degraded：防护降级。
        :type ransom_protection_status: str
        :param protect_policy_name: 勒索防护策略名称
        :type protect_policy_name: str
        :param policy_name: 防护策略名称
        :type policy_name: str
        :param policy_id: 防护策略id
        :type policy_id: str
        :param agent_status: Agent状态
        :type agent_status: str
        :param group_id: 服务器组ID
        :type group_id: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param last_days: 查询时间范围天数，1~30天，若不填，则默认查询一天
        :type last_days: int
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._host_name = None
        self._host_id = None
        self._os_type = None
        self._host_ip = None
        self._private_ip = None
        self._host_status = None
        self._ransom_protection_status = None
        self._protect_policy_name = None
        self._policy_name = None
        self._policy_id = None
        self._agent_status = None
        self._group_id = None
        self._group_name = None
        self._last_days = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if os_type is not None:
            self.os_type = os_type
        if host_ip is not None:
            self.host_ip = host_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if host_status is not None:
            self.host_status = host_status
        if ransom_protection_status is not None:
            self.ransom_protection_status = ransom_protection_status
        if protect_policy_name is not None:
            self.protect_policy_name = protect_policy_name
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_id is not None:
            self.policy_id = policy_id
        if agent_status is not None:
            self.agent_status = agent_status
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if last_days is not None:
            self.last_days = last_days

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListRansomwareProtectionNodesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListRansomwareProtectionNodesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListRansomwareProtectionNodesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListRansomwareProtectionNodesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListRansomwareProtectionNodesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRansomwareProtectionNodesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListRansomwareProtectionNodesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRansomwareProtectionNodesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListRansomwareProtectionNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRansomwareProtectionNodesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListRansomwareProtectionNodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host_name(self):
        r"""Gets the host_name of this ListRansomwareProtectionNodesRequest.

        服务器名称

        :return: The host_name of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListRansomwareProtectionNodesRequest.

        服务器名称

        :param host_name: The host_name of this ListRansomwareProtectionNodesRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListRansomwareProtectionNodesRequest.

        服务器ID

        :return: The host_id of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListRansomwareProtectionNodesRequest.

        服务器ID

        :param host_id: The host_id of this ListRansomwareProtectionNodesRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def os_type(self):
        r"""Gets the os_type of this ListRansomwareProtectionNodesRequest.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :return: The os_type of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListRansomwareProtectionNodesRequest.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :param os_type: The os_type of this ListRansomwareProtectionNodesRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListRansomwareProtectionNodesRequest.

        服务器IP地址，服务器公网IP地址

        :return: The host_ip of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListRansomwareProtectionNodesRequest.

        服务器IP地址，服务器公网IP地址

        :param host_ip: The host_ip of this ListRansomwareProtectionNodesRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListRansomwareProtectionNodesRequest.

        服务器私有IP

        :return: The private_ip of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListRansomwareProtectionNodesRequest.

        服务器私有IP

        :param private_ip: The private_ip of this ListRansomwareProtectionNodesRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def host_status(self):
        r"""Gets the host_status of this ListRansomwareProtectionNodesRequest.

        主机状态，包含如下3种。   - 不传参默认为全部。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。

        :return: The host_status of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ListRansomwareProtectionNodesRequest.

        主机状态，包含如下3种。   - 不传参默认为全部。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。

        :param host_status: The host_status of this ListRansomwareProtectionNodesRequest.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def ransom_protection_status(self):
        r"""Gets the ransom_protection_status of this ListRansomwareProtectionNodesRequest.

        勒索防护状态，包含如下6种。   - closed ：未开启。   - opened ：防护中。   - opening ：开启中。   - closing ：关闭中。   - protect_failed：防护失败。   - protect_degraded：防护降级。

        :return: The ransom_protection_status of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._ransom_protection_status

    @ransom_protection_status.setter
    def ransom_protection_status(self, ransom_protection_status):
        r"""Sets the ransom_protection_status of this ListRansomwareProtectionNodesRequest.

        勒索防护状态，包含如下6种。   - closed ：未开启。   - opened ：防护中。   - opening ：开启中。   - closing ：关闭中。   - protect_failed：防护失败。   - protect_degraded：防护降级。

        :param ransom_protection_status: The ransom_protection_status of this ListRansomwareProtectionNodesRequest.
        :type ransom_protection_status: str
        """
        self._ransom_protection_status = ransom_protection_status

    @property
    def protect_policy_name(self):
        r"""Gets the protect_policy_name of this ListRansomwareProtectionNodesRequest.

        勒索防护策略名称

        :return: The protect_policy_name of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._protect_policy_name

    @protect_policy_name.setter
    def protect_policy_name(self, protect_policy_name):
        r"""Sets the protect_policy_name of this ListRansomwareProtectionNodesRequest.

        勒索防护策略名称

        :param protect_policy_name: The protect_policy_name of this ListRansomwareProtectionNodesRequest.
        :type protect_policy_name: str
        """
        self._protect_policy_name = protect_policy_name

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ListRansomwareProtectionNodesRequest.

        防护策略名称

        :return: The policy_name of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ListRansomwareProtectionNodesRequest.

        防护策略名称

        :param policy_name: The policy_name of this ListRansomwareProtectionNodesRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListRansomwareProtectionNodesRequest.

        防护策略id

        :return: The policy_id of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListRansomwareProtectionNodesRequest.

        防护策略id

        :param policy_id: The policy_id of this ListRansomwareProtectionNodesRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ListRansomwareProtectionNodesRequest.

        Agent状态

        :return: The agent_status of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ListRansomwareProtectionNodesRequest.

        Agent状态

        :param agent_status: The agent_status of this ListRansomwareProtectionNodesRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def group_id(self):
        r"""Gets the group_id of this ListRansomwareProtectionNodesRequest.

        服务器组ID

        :return: The group_id of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListRansomwareProtectionNodesRequest.

        服务器组ID

        :param group_id: The group_id of this ListRansomwareProtectionNodesRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ListRansomwareProtectionNodesRequest.

        服务器组名称

        :return: The group_name of this ListRansomwareProtectionNodesRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListRansomwareProtectionNodesRequest.

        服务器组名称

        :param group_name: The group_name of this ListRansomwareProtectionNodesRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def last_days(self):
        r"""Gets the last_days of this ListRansomwareProtectionNodesRequest.

        查询时间范围天数，1~30天，若不填，则默认查询一天

        :return: The last_days of this ListRansomwareProtectionNodesRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListRansomwareProtectionNodesRequest.

        查询时间范围天数，1~30天，若不填，则默认查询一天

        :param last_days: The last_days of this ListRansomwareProtectionNodesRequest.
        :type last_days: int
        """
        self._last_days = last_days

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
        if not isinstance(other, ListRansomwareProtectionNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
