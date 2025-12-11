# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventTypeRequest:

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
        'begin_time': 'int',
        'end_time': 'int',
        'last_days': 'int',
        'category': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'container_name': 'str',
        'handle_status': 'str',
        'severity': 'str',
        'severity_list': 'list[str]',
        'attack_tag': 'str',
        'asset_value': 'str',
        'tag_list': 'list[str]',
        'att_ck': 'str',
        'event_name': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'last_days': 'last_days',
        'category': 'category',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'container_name': 'container_name',
        'handle_status': 'handle_status',
        'severity': 'severity',
        'severity_list': 'severity_list',
        'attack_tag': 'attack_tag',
        'asset_value': 'asset_value',
        'tag_list': 'tag_list',
        'att_ck': 'att_ck',
        'event_name': 'event_name'
    }

    def __init__(self, region=None, enterprise_project_id=None, begin_time=None, end_time=None, last_days=None, category=None, host_name=None, host_id=None, private_ip=None, public_ip=None, container_name=None, handle_status=None, severity=None, severity_list=None, attack_tag=None, asset_value=None, tag_list=None, att_ck=None, event_name=None):
        r"""ListEventTypeRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param begin_time: **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 
        :type begin_time: int
        :param end_time: **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 
        :type end_time: int
        :param last_days: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥
        :type last_days: int
        :param category: **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host : 主机安全事件 - container : 容器安全事件 - serverless : serverless场景安全事件 **默认取值**: 不涉及 
        :type category: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 服务器ID
        :type host_id: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param container_name: 容器实例名称
        :type container_name: str
        :param handle_status: 处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理
        :type handle_status: str
        :param severity: 威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急
        :type severity: str
        :param severity_list: 威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急
        :type severity_list: list[str]
        :param attack_tag: 攻击标识，包含如下：   - attack_success : 攻击成功   - attack_attempt : 攻击尝试   - attack_blocked : 攻击被阻断   - abnormal_behavior : 异常行为   - collapsible_host : 主机失陷   - system_vulnerability : 系统脆弱性
        :type attack_tag: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param tag_list: 事件标签列表，例如:[\&quot;热点事件\&quot;]
        :type tag_list: list[str]
        :param att_ck: ATT&amp;CK攻击阶，包含如下：   - Reconnaissance : 侦察   - Initial Access : 初始访问   - Execution : 执行   - Persistence : 持久化   - Privilege Escalation : 权限提升   - Defense Evasion : 防御绕过   - Credential Access : 凭据访问   - Command and Control : 命令与控制   - Impact : 影响破坏
        :type att_ck: str
        :param event_name: 告警名称
        :type event_name: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._begin_time = None
        self._end_time = None
        self._last_days = None
        self._category = None
        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._public_ip = None
        self._container_name = None
        self._handle_status = None
        self._severity = None
        self._severity_list = None
        self._attack_tag = None
        self._asset_value = None
        self._tag_list = None
        self._att_ck = None
        self._event_name = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if last_days is not None:
            self.last_days = last_days
        self.category = category
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if container_name is not None:
            self.container_name = container_name
        if handle_status is not None:
            self.handle_status = handle_status
        if severity is not None:
            self.severity = severity
        if severity_list is not None:
            self.severity_list = severity_list
        if attack_tag is not None:
            self.attack_tag = attack_tag
        if asset_value is not None:
            self.asset_value = asset_value
        if tag_list is not None:
            self.tag_list = tag_list
        if att_ck is not None:
            self.att_ck = att_ck
        if event_name is not None:
            self.event_name = event_name

    @property
    def region(self):
        r"""Gets the region of this ListEventTypeRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListEventTypeRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListEventTypeRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListEventTypeRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListEventTypeRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListEventTypeRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListEventTypeRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListEventTypeRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListEventTypeRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :return: The begin_time of this ListEventTypeRequest.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListEventTypeRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :param begin_time: The begin_time of this ListEventTypeRequest.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListEventTypeRequest.

        **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :return: The end_time of this ListEventTypeRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListEventTypeRequest.

        **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :param end_time: The end_time of this ListEventTypeRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def last_days(self):
        r"""Gets the last_days of this ListEventTypeRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :return: The last_days of this ListEventTypeRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListEventTypeRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :param last_days: The last_days of this ListEventTypeRequest.
        :type last_days: int
        """
        self._last_days = last_days

    @property
    def category(self):
        r"""Gets the category of this ListEventTypeRequest.

        **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host : 主机安全事件 - container : 容器安全事件 - serverless : serverless场景安全事件 **默认取值**: 不涉及 

        :return: The category of this ListEventTypeRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListEventTypeRequest.

        **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host : 主机安全事件 - container : 容器安全事件 - serverless : serverless场景安全事件 **默认取值**: 不涉及 

        :param category: The category of this ListEventTypeRequest.
        :type category: str
        """
        self._category = category

    @property
    def host_name(self):
        r"""Gets the host_name of this ListEventTypeRequest.

        服务器名称

        :return: The host_name of this ListEventTypeRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListEventTypeRequest.

        服务器名称

        :param host_name: The host_name of this ListEventTypeRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListEventTypeRequest.

        服务器ID

        :return: The host_id of this ListEventTypeRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListEventTypeRequest.

        服务器ID

        :param host_id: The host_id of this ListEventTypeRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListEventTypeRequest.

        服务器私有IP

        :return: The private_ip of this ListEventTypeRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListEventTypeRequest.

        服务器私有IP

        :param private_ip: The private_ip of this ListEventTypeRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListEventTypeRequest.

        服务器公网IP

        :return: The public_ip of this ListEventTypeRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListEventTypeRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListEventTypeRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def container_name(self):
        r"""Gets the container_name of this ListEventTypeRequest.

        容器实例名称

        :return: The container_name of this ListEventTypeRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListEventTypeRequest.

        容器实例名称

        :param container_name: The container_name of this ListEventTypeRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListEventTypeRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :return: The handle_status of this ListEventTypeRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListEventTypeRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :param handle_status: The handle_status of this ListEventTypeRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def severity(self):
        r"""Gets the severity of this ListEventTypeRequest.

        威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :return: The severity of this ListEventTypeRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListEventTypeRequest.

        威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :param severity: The severity of this ListEventTypeRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def severity_list(self):
        r"""Gets the severity_list of this ListEventTypeRequest.

        威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :return: The severity_list of this ListEventTypeRequest.
        :rtype: list[str]
        """
        return self._severity_list

    @severity_list.setter
    def severity_list(self, severity_list):
        r"""Sets the severity_list of this ListEventTypeRequest.

        威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :param severity_list: The severity_list of this ListEventTypeRequest.
        :type severity_list: list[str]
        """
        self._severity_list = severity_list

    @property
    def attack_tag(self):
        r"""Gets the attack_tag of this ListEventTypeRequest.

        攻击标识，包含如下：   - attack_success : 攻击成功   - attack_attempt : 攻击尝试   - attack_blocked : 攻击被阻断   - abnormal_behavior : 异常行为   - collapsible_host : 主机失陷   - system_vulnerability : 系统脆弱性

        :return: The attack_tag of this ListEventTypeRequest.
        :rtype: str
        """
        return self._attack_tag

    @attack_tag.setter
    def attack_tag(self, attack_tag):
        r"""Sets the attack_tag of this ListEventTypeRequest.

        攻击标识，包含如下：   - attack_success : 攻击成功   - attack_attempt : 攻击尝试   - attack_blocked : 攻击被阻断   - abnormal_behavior : 异常行为   - collapsible_host : 主机失陷   - system_vulnerability : 系统脆弱性

        :param attack_tag: The attack_tag of this ListEventTypeRequest.
        :type attack_tag: str
        """
        self._attack_tag = attack_tag

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListEventTypeRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ListEventTypeRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListEventTypeRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ListEventTypeRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def tag_list(self):
        r"""Gets the tag_list of this ListEventTypeRequest.

        事件标签列表，例如:[\"热点事件\"]

        :return: The tag_list of this ListEventTypeRequest.
        :rtype: list[str]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        r"""Sets the tag_list of this ListEventTypeRequest.

        事件标签列表，例如:[\"热点事件\"]

        :param tag_list: The tag_list of this ListEventTypeRequest.
        :type tag_list: list[str]
        """
        self._tag_list = tag_list

    @property
    def att_ck(self):
        r"""Gets the att_ck of this ListEventTypeRequest.

        ATT&CK攻击阶，包含如下：   - Reconnaissance : 侦察   - Initial Access : 初始访问   - Execution : 执行   - Persistence : 持久化   - Privilege Escalation : 权限提升   - Defense Evasion : 防御绕过   - Credential Access : 凭据访问   - Command and Control : 命令与控制   - Impact : 影响破坏

        :return: The att_ck of this ListEventTypeRequest.
        :rtype: str
        """
        return self._att_ck

    @att_ck.setter
    def att_ck(self, att_ck):
        r"""Sets the att_ck of this ListEventTypeRequest.

        ATT&CK攻击阶，包含如下：   - Reconnaissance : 侦察   - Initial Access : 初始访问   - Execution : 执行   - Persistence : 持久化   - Privilege Escalation : 权限提升   - Defense Evasion : 防御绕过   - Credential Access : 凭据访问   - Command and Control : 命令与控制   - Impact : 影响破坏

        :param att_ck: The att_ck of this ListEventTypeRequest.
        :type att_ck: str
        """
        self._att_ck = att_ck

    @property
    def event_name(self):
        r"""Gets the event_name of this ListEventTypeRequest.

        告警名称

        :return: The event_name of this ListEventTypeRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ListEventTypeRequest.

        告警名称

        :param event_name: The event_name of this ListEventTypeRequest.
        :type event_name: str
        """
        self._event_name = event_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListEventTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
