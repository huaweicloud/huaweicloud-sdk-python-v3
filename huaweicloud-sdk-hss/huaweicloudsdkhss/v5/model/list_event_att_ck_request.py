# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventAttCkRequest:

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
        'last_days': 'int',
        'category': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'container_name': 'str',
        'event_type': 'int',
        'handle_status': 'str',
        'severity': 'str',
        'severity_list': 'list[str]',
        'attack_tag': 'str',
        'asset_value': 'str',
        'tag_list': 'list[str]',
        'event_name': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'last_days': 'last_days',
        'category': 'category',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'container_name': 'container_name',
        'event_type': 'event_type',
        'handle_status': 'handle_status',
        'severity': 'severity',
        'severity_list': 'severity_list',
        'attack_tag': 'attack_tag',
        'asset_value': 'asset_value',
        'tag_list': 'tag_list',
        'event_name': 'event_name'
    }

    def __init__(self, region=None, enterprise_project_id=None, last_days=None, category=None, host_name=None, host_id=None, private_ip=None, public_ip=None, container_name=None, event_type=None, handle_status=None, severity=None, severity_list=None, attack_tag=None, asset_value=None, tag_list=None, event_name=None):
        r"""ListEventAttCkRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param last_days: **参数解释**: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥。 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值30 **默认取值**: 不涉及 
        :type last_days: int
        :param category: **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host : 主机安全事件 - container : 容器安全事件 - serverless : serverless场景安全事件  **默认取值**: 不涉及 
        :type category: str
        :param host_name: **参数解释**： 服务器名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 
        :type host_name: str
        :param host_id: **参数解释**： 服务器ID **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 
        :type host_id: str
        :param private_ip: **参数解释**： 服务器私有IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 
        :type private_ip: str
        :param public_ip: **参数解释**： 服务器公网IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 
        :type public_ip: str
        :param container_name: **参数解释**： 容器实例名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-512位 **默认取值**： 不涉及 
        :type container_name: str
        :param event_type: **参数解释**: 事件类型 **约束限制**: 不涉及 **取值范围**: - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3026：crontab提权 - 3027：Crontab可疑任务 - 3029：系统安全防护被禁用 - 3030：备份删除 - 3031：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色  **默认取值**: 不涉及 
        :type event_type: int
        :param handle_status: **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 
        :type handle_status: str
        :param severity: **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 
        :type severity: str
        :param severity_list: **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 
        :type severity_list: list[str]
        :param attack_tag: **参数解释**: 攻击标识 **约束限制**: 不涉及 **取值范围**: - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性  **默认取值**: 不涉及 
        :type attack_tag: str
        :param asset_value: **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：般资产 - test：测试资产  **默认取值**: 不涉及 
        :type asset_value: str
        :param tag_list: 事件标签列表，例如:[\&quot;热点事件\&quot;]
        :type tag_list: list[str]
        :param event_name: **参数解释**： 告警名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type event_name: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._last_days = None
        self._category = None
        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._public_ip = None
        self._container_name = None
        self._event_type = None
        self._handle_status = None
        self._severity = None
        self._severity_list = None
        self._attack_tag = None
        self._asset_value = None
        self._tag_list = None
        self._event_name = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
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
        if event_type is not None:
            self.event_type = event_type
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
        if event_name is not None:
            self.event_name = event_name

    @property
    def region(self):
        r"""Gets the region of this ListEventAttCkRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The region of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListEventAttCkRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param region: The region of this ListEventAttCkRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListEventAttCkRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListEventAttCkRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListEventAttCkRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def last_days(self):
        r"""Gets the last_days of this ListEventAttCkRequest.

        **参数解释**: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥。 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值30 **默认取值**: 不涉及 

        :return: The last_days of this ListEventAttCkRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListEventAttCkRequest.

        **参数解释**: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥。 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值30 **默认取值**: 不涉及 

        :param last_days: The last_days of this ListEventAttCkRequest.
        :type last_days: int
        """
        self._last_days = last_days

    @property
    def category(self):
        r"""Gets the category of this ListEventAttCkRequest.

        **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host : 主机安全事件 - container : 容器安全事件 - serverless : serverless场景安全事件  **默认取值**: 不涉及 

        :return: The category of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListEventAttCkRequest.

        **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host : 主机安全事件 - container : 容器安全事件 - serverless : serverless场景安全事件  **默认取值**: 不涉及 

        :param category: The category of this ListEventAttCkRequest.
        :type category: str
        """
        self._category = category

    @property
    def host_name(self):
        r"""Gets the host_name of this ListEventAttCkRequest.

        **参数解释**： 服务器名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :return: The host_name of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListEventAttCkRequest.

        **参数解释**： 服务器名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :param host_name: The host_name of this ListEventAttCkRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListEventAttCkRequest.

        **参数解释**： 服务器ID **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :return: The host_id of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListEventAttCkRequest.

        **参数解释**： 服务器ID **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :param host_id: The host_id of this ListEventAttCkRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListEventAttCkRequest.

        **参数解释**： 服务器私有IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :return: The private_ip of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListEventAttCkRequest.

        **参数解释**： 服务器私有IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :param private_ip: The private_ip of this ListEventAttCkRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListEventAttCkRequest.

        **参数解释**： 服务器公网IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :return: The public_ip of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListEventAttCkRequest.

        **参数解释**： 服务器公网IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :param public_ip: The public_ip of this ListEventAttCkRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def container_name(self):
        r"""Gets the container_name of this ListEventAttCkRequest.

        **参数解释**： 容器实例名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-512位 **默认取值**： 不涉及 

        :return: The container_name of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListEventAttCkRequest.

        **参数解释**： 容器实例名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-512位 **默认取值**： 不涉及 

        :param container_name: The container_name of this ListEventAttCkRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def event_type(self):
        r"""Gets the event_type of this ListEventAttCkRequest.

        **参数解释**: 事件类型 **约束限制**: 不涉及 **取值范围**: - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3026：crontab提权 - 3027：Crontab可疑任务 - 3029：系统安全防护被禁用 - 3030：备份删除 - 3031：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色  **默认取值**: 不涉及 

        :return: The event_type of this ListEventAttCkRequest.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListEventAttCkRequest.

        **参数解释**: 事件类型 **约束限制**: 不涉及 **取值范围**: - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3026：crontab提权 - 3027：Crontab可疑任务 - 3029：系统安全防护被禁用 - 3030：备份删除 - 3031：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色  **默认取值**: 不涉及 

        :param event_type: The event_type of this ListEventAttCkRequest.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListEventAttCkRequest.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 

        :return: The handle_status of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListEventAttCkRequest.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 

        :param handle_status: The handle_status of this ListEventAttCkRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def severity(self):
        r"""Gets the severity of this ListEventAttCkRequest.

        **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 

        :return: The severity of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListEventAttCkRequest.

        **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 

        :param severity: The severity of this ListEventAttCkRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def severity_list(self):
        r"""Gets the severity_list of this ListEventAttCkRequest.

        **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 

        :return: The severity_list of this ListEventAttCkRequest.
        :rtype: list[str]
        """
        return self._severity_list

    @severity_list.setter
    def severity_list(self, severity_list):
        r"""Sets the severity_list of this ListEventAttCkRequest.

        **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 

        :param severity_list: The severity_list of this ListEventAttCkRequest.
        :type severity_list: list[str]
        """
        self._severity_list = severity_list

    @property
    def attack_tag(self):
        r"""Gets the attack_tag of this ListEventAttCkRequest.

        **参数解释**: 攻击标识 **约束限制**: 不涉及 **取值范围**: - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性  **默认取值**: 不涉及 

        :return: The attack_tag of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._attack_tag

    @attack_tag.setter
    def attack_tag(self, attack_tag):
        r"""Sets the attack_tag of this ListEventAttCkRequest.

        **参数解释**: 攻击标识 **约束限制**: 不涉及 **取值范围**: - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性  **默认取值**: 不涉及 

        :param attack_tag: The attack_tag of this ListEventAttCkRequest.
        :type attack_tag: str
        """
        self._attack_tag = attack_tag

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListEventAttCkRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：般资产 - test：测试资产  **默认取值**: 不涉及 

        :return: The asset_value of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListEventAttCkRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：般资产 - test：测试资产  **默认取值**: 不涉及 

        :param asset_value: The asset_value of this ListEventAttCkRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def tag_list(self):
        r"""Gets the tag_list of this ListEventAttCkRequest.

        事件标签列表，例如:[\"热点事件\"]

        :return: The tag_list of this ListEventAttCkRequest.
        :rtype: list[str]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        r"""Sets the tag_list of this ListEventAttCkRequest.

        事件标签列表，例如:[\"热点事件\"]

        :param tag_list: The tag_list of this ListEventAttCkRequest.
        :type tag_list: list[str]
        """
        self._tag_list = tag_list

    @property
    def event_name(self):
        r"""Gets the event_name of this ListEventAttCkRequest.

        **参数解释**： 告警名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The event_name of this ListEventAttCkRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ListEventAttCkRequest.

        **参数解释**： 告警名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param event_name: The event_name of this ListEventAttCkRequest.
        :type event_name: str
        """
        self._event_name = event_name

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
        if not isinstance(other, ListEventAttCkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
