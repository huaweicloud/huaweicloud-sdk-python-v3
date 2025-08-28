# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'region': 'str',
        'enterprise_project_id': 'str',
        'last_days': 'int',
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'container_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'event_types': 'list[int]',
        'handle_status': 'str',
        'severity': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'event_class_ids': 'list[str]',
        'severity_list': 'list[str]',
        'attack_tag': 'str',
        'asset_value': 'str',
        'tag_list': 'list[str]',
        'att_ck': 'str',
        'event_name': 'str',
        'auto_block': 'bool'
    }

    attribute_map = {
        'category': 'category',
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'last_days': 'last_days',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'container_name': 'container_name',
        'offset': 'offset',
        'limit': 'limit',
        'event_types': 'event_types',
        'handle_status': 'handle_status',
        'severity': 'severity',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'event_class_ids': 'event_class_ids',
        'severity_list': 'severity_list',
        'attack_tag': 'attack_tag',
        'asset_value': 'asset_value',
        'tag_list': 'tag_list',
        'att_ck': 'att_ck',
        'event_name': 'event_name',
        'auto_block': 'auto_block'
    }

    def __init__(self, category=None, region=None, enterprise_project_id=None, last_days=None, host_name=None, host_id=None, private_ip=None, public_ip=None, container_name=None, offset=None, limit=None, event_types=None, handle_status=None, severity=None, begin_time=None, end_time=None, event_class_ids=None, severity_list=None, attack_tag=None, asset_value=None, tag_list=None, att_ck=None, event_name=None, auto_block=None):
        r"""ListSecurityEventsRequest

        The model defined in huaweicloud sdk

        :param category: **参数解释**： 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件  **默认取值**: 不涉及 
        :type category: str
        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param last_days: **参数解释**: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥。 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值30 **默认取值**: 不涉及 
        :type last_days: int
        :param host_name: **参数解释**： 服务器名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 
        :type host_name: str
        :param host_id: **参数解释**： 服务器ID **约束限制**： 不涉及 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及 
        :type host_id: str
        :param private_ip: **参数解释**： 服务器私有IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 
        :type private_ip: str
        :param public_ip: **参数解释**： 服务器公网IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 
        :type public_ip: str
        :param container_name: **参数解释**： 容器实例名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-512位 **默认取值**： 不涉及 
        :type container_name: str
        :param offset: **参数解释**: 偏移量，指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 最小值10，最大值1000 **默认取值**: 10 
        :type limit: int
        :param event_types: **参数解释**: 事件类型 **约束限制**: 不涉及 **取值范围**: - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3026：crontab提权 - 3027：Crontab可疑任务 - 3029：系统安全防护被禁用 - 3030：备份删除 - 3031：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色  **默认取值**: 不涉及 
        :type event_types: list[int]
        :param handle_status: **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 
        :type handle_status: str
        :param severity: **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 
        :type severity: str
        :param begin_time: **参数解释**： 自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥 **约束限制**： 不涉及 **取值范围**： 字符长度13位 **默认取值**： 不涉及 
        :type begin_time: str
        :param end_time: **参数解释**： 自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥 **约束限制**： 不涉及 **取值范围**： 字符长度13位 **默认取值**： 不涉及 
        :type end_time: str
        :param event_class_ids: **参数解释**: 事件标识 **约束限制**: 不涉及 **取值范围**: - container_1001：容器命名空间 - container_1002：容器开放端口 - container_1003：容器安全选项 - container_1004：容器挂载目录 - containerescape_0001：容器高危系统调用 - containerescape_0002：Shocker攻击 - containerescape_0003：DirtCow攻击 - containerescape_0004：容器文件逃逸攻击 - dockerfile_001：用户自定义容器保护文件被修改 - dockerfile_002：容器文件系统可执行文件被修改 - dockerproc_001：容器进程异常事件上报 - fileprotect_0001：文件提权 - fileprotect_0002：关键文件变更 - fileprotect_0003：关键文件路径变更 - fileprotect_0004：文件/目录变更 - av_1002：病毒 - av_1003：蠕虫 - av_1004：木马 - av_1005：僵尸网络 - av_1006：后门 - av_1007：间谍软件 - av_1008：恶意广告软件 - av_1009：钓鱼 - av_1010：Rootkit - av_1011：勒索软件 - av_1012：黑客工具 - av_1013：灰色软件 - av_1015：Webshell - av_1016：挖矿软件 - login_0001：尝试暴力破解 - login_0002：爆破成功 - login_1001：登录成功 - login_1002：异地登录 - login_1003：弱口令 - malware_0001：shell变更事件上报 - malware_0002：反弹shell事件上报 - malware_1001：恶意程序 - procdet_0001：进程异常行为检测 - procdet_0002：进程提权 - crontab_0001：crontab脚本提权 - crontab_0002：恶意路径提权 - procreport_0001：危险命令 - user_1001：账号变更 - user_1002：风险账号 - vmescape_0001：虚拟机敏感命令执行 - vmescape_0002：虚拟化进程访问敏感文件 - vmescape_0003：虚拟机异常端口访问 - webshell_0001：网站后门 - network_1001：恶意挖矿 - network_1002：对外DDoS攻击 - network_1003：恶意扫描 - network_1004：敏感区域攻击 - ransomware_0001：勒索攻击 - ransomware_0002：勒索攻击 - ransomware_0003：勒索攻击 - fileless_0001：进程注入 - fileless_0002：动态库注入进程 - fileless_0003：关键配置变更 - fileless_0004：环境变量变更 - fileless_0005：内存文件进程 - fileless_0006：vdso劫持 - crontab_1001：Crontab可疑任务 - vul_exploit_0001：Redis漏洞利用攻击 - vul_exploit_0002：Hadoop漏洞利用攻击 - vul_exploit_0003：MySQL漏洞利用攻击 - rootkit_0001：可疑rootkit文件 - rootkit_0002：可疑内核模块 - RASP_0004：上传Webshell - RASP_0018：无文件Webshell - blockexec_001：已知勒索攻击 - hips_0001：Windows Defender防护被禁用 - hips_0002：可疑的黑客工具 - hips_0003：可疑的勒索加密行为 - hips_0004：隐藏账号创建 - hips_0005：读取用户密码凭据 - hips_0006：可疑的SAM文件导出 - hips_0007：可疑shadow copy删除操作 - hips_0008：备份文件删除 - hips_0009：可疑勒索病毒操作注册表 - hips_0010：可疑的异常进程行为 - hips_0011：可疑的扫描探测 - hips_0012：可疑的勒索病毒脚本运行 - hips_0013：可疑的挖矿命令执行 - hips_0014：可疑的禁用windows安全中心 - hips_0015：可疑的停止防火墙服务行为 - hips_0016：可疑的系统自动恢复禁用 - hips_0017：Offies创建可执行文件 - hips_0018：带宏Offies文件异常创建 - hips_0019：可疑的注册表操作 - hips_0020：Confluence远程代码执行 - hips_0021：MSDT远程代码执行 - portscan_0001：通用端口扫描 - portscan_0002：秘密端口扫描 - k8s_1001：Kubernetes事件删除 - k8s_1002：创建特权Pod - k8s_1003：Pod中使用交互式shell - k8s_1004：创建敏感目录Pod - k8s_1005：创建主机网络的Pod - k8s_1006：创建主机Pid空间的Pod - k8s_1007：普通pod访问APIserver认证失败 - k8s_1008：普通Pod通过Curl访问APIServer - k8s_1009：系统管理空间执行exec - k8s_1010：系统管理空间创建Pod - k8s_1011：创建静态Pod - k8s_1012：创建DaemonSet - k8s_1013：创建集群计划任务 - k8s_1014：Secrets操作 - k8s_1015：枚举用户可执行的操作 - k8s_1016：高权限RoleBinding或ClusterRoleBinding - k8s_1017：ServiceAccount创建 - k8s_1018：创建Cronjob - k8s_1019：Pod中exec使用交互式shell - k8s_1020：无权限访问Apiserver - k8s_1021：使用curl访问APIServer - k8s_1022：Ingress漏洞 - k8s_1023：中间人攻击 - k8s_1024：蠕虫挖矿木马 - k8s_1025：K8s事件删除 - k8s_1026：SelfSubjectRulesReview场景 - imgblock_0001：镜像白名单阻断 - imgblock_0002：镜像黑名单阻断 - imgblock_0003：镜像标签白名单阻断 - imgblock_0004：镜像标签黑名单阻断 - imgblock_0005：创建容器白名单阻断 - imgblock_0006：创建容器黑名单阻断 - imgblock_0007：容器mount proc阻断 - imgblock_0008：容器seccomp unconfined阻断 - imgblock_0009：容器特权阻断 - imgblock_0010：容器capabilities阻断  **默认取值**: 不涉及 
        :type event_class_ids: list[str]
        :param severity_list: **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 
        :type severity_list: list[str]
        :param attack_tag: **参数解释**: 攻击标识 **约束限制**: 不涉及 **取值范围**: - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性  **默认取值**: 不涉及 
        :type attack_tag: str
        :param asset_value: **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：般资产 - test：测试资产  **默认取值**: 不涉及 
        :type asset_value: str
        :param tag_list: 事件标签列表，例如:[\&quot;热点事件\&quot;]
        :type tag_list: list[str]
        :param att_ck: **参数解释**: ATT&amp;CK攻击阶段 **约束限制**: 不涉及 **取值范围**: - Reconnaissance：侦察 - Initial Access：初始访问 - Execution：执行 - Persistence：持久化 - Privilege Escalation：权限提升 - Defense Evasion：防御绕过 - Credential Access：凭据访问 - Command and Control：命令与控制 - Impact：影响破坏  **默认取值**: 不涉及 
        :type att_ck: str
        :param event_name: **参数解释**： 告警名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type event_name: str
        :param auto_block: **参数解释**： 是否自动阻断告警 **约束限制**： 不涉及 **取值范围**： - true：自动阻断告警 - false：不自动阻断告警 **默认取值**： 不涉及 
        :type auto_block: bool
        """
        
        

        self._category = None
        self._region = None
        self._enterprise_project_id = None
        self._last_days = None
        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._public_ip = None
        self._container_name = None
        self._offset = None
        self._limit = None
        self._event_types = None
        self._handle_status = None
        self._severity = None
        self._begin_time = None
        self._end_time = None
        self._event_class_ids = None
        self._severity_list = None
        self._attack_tag = None
        self._asset_value = None
        self._tag_list = None
        self._att_ck = None
        self._event_name = None
        self._auto_block = None
        self.discriminator = None

        self.category = category
        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if last_days is not None:
            self.last_days = last_days
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
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if event_types is not None:
            self.event_types = event_types
        if handle_status is not None:
            self.handle_status = handle_status
        if severity is not None:
            self.severity = severity
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if event_class_ids is not None:
            self.event_class_ids = event_class_ids
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
        if auto_block is not None:
            self.auto_block = auto_block

    @property
    def category(self):
        r"""Gets the category of this ListSecurityEventsRequest.

        **参数解释**： 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件  **默认取值**: 不涉及 

        :return: The category of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListSecurityEventsRequest.

        **参数解释**： 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件  **默认取值**: 不涉及 

        :param category: The category of this ListSecurityEventsRequest.
        :type category: str
        """
        self._category = category

    @property
    def region(self):
        r"""Gets the region of this ListSecurityEventsRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The region of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListSecurityEventsRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param region: The region of this ListSecurityEventsRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListSecurityEventsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListSecurityEventsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListSecurityEventsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def last_days(self):
        r"""Gets the last_days of this ListSecurityEventsRequest.

        **参数解释**: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥。 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值30 **默认取值**: 不涉及 

        :return: The last_days of this ListSecurityEventsRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListSecurityEventsRequest.

        **参数解释**: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥。 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值30 **默认取值**: 不涉及 

        :param last_days: The last_days of this ListSecurityEventsRequest.
        :type last_days: int
        """
        self._last_days = last_days

    @property
    def host_name(self):
        r"""Gets the host_name of this ListSecurityEventsRequest.

        **参数解释**： 服务器名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :return: The host_name of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListSecurityEventsRequest.

        **参数解释**： 服务器名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :param host_name: The host_name of this ListSecurityEventsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListSecurityEventsRequest.

        **参数解释**： 服务器ID **约束限制**： 不涉及 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及 

        :return: The host_id of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListSecurityEventsRequest.

        **参数解释**： 服务器ID **约束限制**： 不涉及 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及 

        :param host_id: The host_id of this ListSecurityEventsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListSecurityEventsRequest.

        **参数解释**： 服务器私有IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :return: The private_ip of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListSecurityEventsRequest.

        **参数解释**： 服务器私有IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :param private_ip: The private_ip of this ListSecurityEventsRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListSecurityEventsRequest.

        **参数解释**： 服务器公网IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :return: The public_ip of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListSecurityEventsRequest.

        **参数解释**： 服务器公网IP **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :param public_ip: The public_ip of this ListSecurityEventsRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def container_name(self):
        r"""Gets the container_name of this ListSecurityEventsRequest.

        **参数解释**： 容器实例名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-512位 **默认取值**： 不涉及 

        :return: The container_name of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListSecurityEventsRequest.

        **参数解释**： 容器实例名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-512位 **默认取值**： 不涉及 

        :param container_name: The container_name of this ListSecurityEventsRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityEventsRequest.

        **参数解释**: 偏移量，指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListSecurityEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityEventsRequest.

        **参数解释**: 偏移量，指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListSecurityEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityEventsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 最小值10，最大值1000 **默认取值**: 10 

        :return: The limit of this ListSecurityEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityEventsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 最小值10，最大值1000 **默认取值**: 10 

        :param limit: The limit of this ListSecurityEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def event_types(self):
        r"""Gets the event_types of this ListSecurityEventsRequest.

        **参数解释**: 事件类型 **约束限制**: 不涉及 **取值范围**: - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3026：crontab提权 - 3027：Crontab可疑任务 - 3029：系统安全防护被禁用 - 3030：备份删除 - 3031：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色  **默认取值**: 不涉及 

        :return: The event_types of this ListSecurityEventsRequest.
        :rtype: list[int]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        r"""Sets the event_types of this ListSecurityEventsRequest.

        **参数解释**: 事件类型 **约束限制**: 不涉及 **取值范围**: - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3026：crontab提权 - 3027：Crontab可疑任务 - 3029：系统安全防护被禁用 - 3030：备份删除 - 3031：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色  **默认取值**: 不涉及 

        :param event_types: The event_types of this ListSecurityEventsRequest.
        :type event_types: list[int]
        """
        self._event_types = event_types

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListSecurityEventsRequest.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 

        :return: The handle_status of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListSecurityEventsRequest.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 

        :param handle_status: The handle_status of this ListSecurityEventsRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def severity(self):
        r"""Gets the severity of this ListSecurityEventsRequest.

        **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 

        :return: The severity of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListSecurityEventsRequest.

        **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 

        :param severity: The severity of this ListSecurityEventsRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListSecurityEventsRequest.

        **参数解释**： 自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥 **约束限制**： 不涉及 **取值范围**： 字符长度13位 **默认取值**： 不涉及 

        :return: The begin_time of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListSecurityEventsRequest.

        **参数解释**： 自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥 **约束限制**： 不涉及 **取值范围**： 字符长度13位 **默认取值**： 不涉及 

        :param begin_time: The begin_time of this ListSecurityEventsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSecurityEventsRequest.

        **参数解释**： 自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥 **约束限制**： 不涉及 **取值范围**： 字符长度13位 **默认取值**： 不涉及 

        :return: The end_time of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSecurityEventsRequest.

        **参数解释**： 自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥 **约束限制**： 不涉及 **取值范围**： 字符长度13位 **默认取值**： 不涉及 

        :param end_time: The end_time of this ListSecurityEventsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def event_class_ids(self):
        r"""Gets the event_class_ids of this ListSecurityEventsRequest.

        **参数解释**: 事件标识 **约束限制**: 不涉及 **取值范围**: - container_1001：容器命名空间 - container_1002：容器开放端口 - container_1003：容器安全选项 - container_1004：容器挂载目录 - containerescape_0001：容器高危系统调用 - containerescape_0002：Shocker攻击 - containerescape_0003：DirtCow攻击 - containerescape_0004：容器文件逃逸攻击 - dockerfile_001：用户自定义容器保护文件被修改 - dockerfile_002：容器文件系统可执行文件被修改 - dockerproc_001：容器进程异常事件上报 - fileprotect_0001：文件提权 - fileprotect_0002：关键文件变更 - fileprotect_0003：关键文件路径变更 - fileprotect_0004：文件/目录变更 - av_1002：病毒 - av_1003：蠕虫 - av_1004：木马 - av_1005：僵尸网络 - av_1006：后门 - av_1007：间谍软件 - av_1008：恶意广告软件 - av_1009：钓鱼 - av_1010：Rootkit - av_1011：勒索软件 - av_1012：黑客工具 - av_1013：灰色软件 - av_1015：Webshell - av_1016：挖矿软件 - login_0001：尝试暴力破解 - login_0002：爆破成功 - login_1001：登录成功 - login_1002：异地登录 - login_1003：弱口令 - malware_0001：shell变更事件上报 - malware_0002：反弹shell事件上报 - malware_1001：恶意程序 - procdet_0001：进程异常行为检测 - procdet_0002：进程提权 - crontab_0001：crontab脚本提权 - crontab_0002：恶意路径提权 - procreport_0001：危险命令 - user_1001：账号变更 - user_1002：风险账号 - vmescape_0001：虚拟机敏感命令执行 - vmescape_0002：虚拟化进程访问敏感文件 - vmescape_0003：虚拟机异常端口访问 - webshell_0001：网站后门 - network_1001：恶意挖矿 - network_1002：对外DDoS攻击 - network_1003：恶意扫描 - network_1004：敏感区域攻击 - ransomware_0001：勒索攻击 - ransomware_0002：勒索攻击 - ransomware_0003：勒索攻击 - fileless_0001：进程注入 - fileless_0002：动态库注入进程 - fileless_0003：关键配置变更 - fileless_0004：环境变量变更 - fileless_0005：内存文件进程 - fileless_0006：vdso劫持 - crontab_1001：Crontab可疑任务 - vul_exploit_0001：Redis漏洞利用攻击 - vul_exploit_0002：Hadoop漏洞利用攻击 - vul_exploit_0003：MySQL漏洞利用攻击 - rootkit_0001：可疑rootkit文件 - rootkit_0002：可疑内核模块 - RASP_0004：上传Webshell - RASP_0018：无文件Webshell - blockexec_001：已知勒索攻击 - hips_0001：Windows Defender防护被禁用 - hips_0002：可疑的黑客工具 - hips_0003：可疑的勒索加密行为 - hips_0004：隐藏账号创建 - hips_0005：读取用户密码凭据 - hips_0006：可疑的SAM文件导出 - hips_0007：可疑shadow copy删除操作 - hips_0008：备份文件删除 - hips_0009：可疑勒索病毒操作注册表 - hips_0010：可疑的异常进程行为 - hips_0011：可疑的扫描探测 - hips_0012：可疑的勒索病毒脚本运行 - hips_0013：可疑的挖矿命令执行 - hips_0014：可疑的禁用windows安全中心 - hips_0015：可疑的停止防火墙服务行为 - hips_0016：可疑的系统自动恢复禁用 - hips_0017：Offies创建可执行文件 - hips_0018：带宏Offies文件异常创建 - hips_0019：可疑的注册表操作 - hips_0020：Confluence远程代码执行 - hips_0021：MSDT远程代码执行 - portscan_0001：通用端口扫描 - portscan_0002：秘密端口扫描 - k8s_1001：Kubernetes事件删除 - k8s_1002：创建特权Pod - k8s_1003：Pod中使用交互式shell - k8s_1004：创建敏感目录Pod - k8s_1005：创建主机网络的Pod - k8s_1006：创建主机Pid空间的Pod - k8s_1007：普通pod访问APIserver认证失败 - k8s_1008：普通Pod通过Curl访问APIServer - k8s_1009：系统管理空间执行exec - k8s_1010：系统管理空间创建Pod - k8s_1011：创建静态Pod - k8s_1012：创建DaemonSet - k8s_1013：创建集群计划任务 - k8s_1014：Secrets操作 - k8s_1015：枚举用户可执行的操作 - k8s_1016：高权限RoleBinding或ClusterRoleBinding - k8s_1017：ServiceAccount创建 - k8s_1018：创建Cronjob - k8s_1019：Pod中exec使用交互式shell - k8s_1020：无权限访问Apiserver - k8s_1021：使用curl访问APIServer - k8s_1022：Ingress漏洞 - k8s_1023：中间人攻击 - k8s_1024：蠕虫挖矿木马 - k8s_1025：K8s事件删除 - k8s_1026：SelfSubjectRulesReview场景 - imgblock_0001：镜像白名单阻断 - imgblock_0002：镜像黑名单阻断 - imgblock_0003：镜像标签白名单阻断 - imgblock_0004：镜像标签黑名单阻断 - imgblock_0005：创建容器白名单阻断 - imgblock_0006：创建容器黑名单阻断 - imgblock_0007：容器mount proc阻断 - imgblock_0008：容器seccomp unconfined阻断 - imgblock_0009：容器特权阻断 - imgblock_0010：容器capabilities阻断  **默认取值**: 不涉及 

        :return: The event_class_ids of this ListSecurityEventsRequest.
        :rtype: list[str]
        """
        return self._event_class_ids

    @event_class_ids.setter
    def event_class_ids(self, event_class_ids):
        r"""Sets the event_class_ids of this ListSecurityEventsRequest.

        **参数解释**: 事件标识 **约束限制**: 不涉及 **取值范围**: - container_1001：容器命名空间 - container_1002：容器开放端口 - container_1003：容器安全选项 - container_1004：容器挂载目录 - containerescape_0001：容器高危系统调用 - containerescape_0002：Shocker攻击 - containerescape_0003：DirtCow攻击 - containerescape_0004：容器文件逃逸攻击 - dockerfile_001：用户自定义容器保护文件被修改 - dockerfile_002：容器文件系统可执行文件被修改 - dockerproc_001：容器进程异常事件上报 - fileprotect_0001：文件提权 - fileprotect_0002：关键文件变更 - fileprotect_0003：关键文件路径变更 - fileprotect_0004：文件/目录变更 - av_1002：病毒 - av_1003：蠕虫 - av_1004：木马 - av_1005：僵尸网络 - av_1006：后门 - av_1007：间谍软件 - av_1008：恶意广告软件 - av_1009：钓鱼 - av_1010：Rootkit - av_1011：勒索软件 - av_1012：黑客工具 - av_1013：灰色软件 - av_1015：Webshell - av_1016：挖矿软件 - login_0001：尝试暴力破解 - login_0002：爆破成功 - login_1001：登录成功 - login_1002：异地登录 - login_1003：弱口令 - malware_0001：shell变更事件上报 - malware_0002：反弹shell事件上报 - malware_1001：恶意程序 - procdet_0001：进程异常行为检测 - procdet_0002：进程提权 - crontab_0001：crontab脚本提权 - crontab_0002：恶意路径提权 - procreport_0001：危险命令 - user_1001：账号变更 - user_1002：风险账号 - vmescape_0001：虚拟机敏感命令执行 - vmescape_0002：虚拟化进程访问敏感文件 - vmescape_0003：虚拟机异常端口访问 - webshell_0001：网站后门 - network_1001：恶意挖矿 - network_1002：对外DDoS攻击 - network_1003：恶意扫描 - network_1004：敏感区域攻击 - ransomware_0001：勒索攻击 - ransomware_0002：勒索攻击 - ransomware_0003：勒索攻击 - fileless_0001：进程注入 - fileless_0002：动态库注入进程 - fileless_0003：关键配置变更 - fileless_0004：环境变量变更 - fileless_0005：内存文件进程 - fileless_0006：vdso劫持 - crontab_1001：Crontab可疑任务 - vul_exploit_0001：Redis漏洞利用攻击 - vul_exploit_0002：Hadoop漏洞利用攻击 - vul_exploit_0003：MySQL漏洞利用攻击 - rootkit_0001：可疑rootkit文件 - rootkit_0002：可疑内核模块 - RASP_0004：上传Webshell - RASP_0018：无文件Webshell - blockexec_001：已知勒索攻击 - hips_0001：Windows Defender防护被禁用 - hips_0002：可疑的黑客工具 - hips_0003：可疑的勒索加密行为 - hips_0004：隐藏账号创建 - hips_0005：读取用户密码凭据 - hips_0006：可疑的SAM文件导出 - hips_0007：可疑shadow copy删除操作 - hips_0008：备份文件删除 - hips_0009：可疑勒索病毒操作注册表 - hips_0010：可疑的异常进程行为 - hips_0011：可疑的扫描探测 - hips_0012：可疑的勒索病毒脚本运行 - hips_0013：可疑的挖矿命令执行 - hips_0014：可疑的禁用windows安全中心 - hips_0015：可疑的停止防火墙服务行为 - hips_0016：可疑的系统自动恢复禁用 - hips_0017：Offies创建可执行文件 - hips_0018：带宏Offies文件异常创建 - hips_0019：可疑的注册表操作 - hips_0020：Confluence远程代码执行 - hips_0021：MSDT远程代码执行 - portscan_0001：通用端口扫描 - portscan_0002：秘密端口扫描 - k8s_1001：Kubernetes事件删除 - k8s_1002：创建特权Pod - k8s_1003：Pod中使用交互式shell - k8s_1004：创建敏感目录Pod - k8s_1005：创建主机网络的Pod - k8s_1006：创建主机Pid空间的Pod - k8s_1007：普通pod访问APIserver认证失败 - k8s_1008：普通Pod通过Curl访问APIServer - k8s_1009：系统管理空间执行exec - k8s_1010：系统管理空间创建Pod - k8s_1011：创建静态Pod - k8s_1012：创建DaemonSet - k8s_1013：创建集群计划任务 - k8s_1014：Secrets操作 - k8s_1015：枚举用户可执行的操作 - k8s_1016：高权限RoleBinding或ClusterRoleBinding - k8s_1017：ServiceAccount创建 - k8s_1018：创建Cronjob - k8s_1019：Pod中exec使用交互式shell - k8s_1020：无权限访问Apiserver - k8s_1021：使用curl访问APIServer - k8s_1022：Ingress漏洞 - k8s_1023：中间人攻击 - k8s_1024：蠕虫挖矿木马 - k8s_1025：K8s事件删除 - k8s_1026：SelfSubjectRulesReview场景 - imgblock_0001：镜像白名单阻断 - imgblock_0002：镜像黑名单阻断 - imgblock_0003：镜像标签白名单阻断 - imgblock_0004：镜像标签黑名单阻断 - imgblock_0005：创建容器白名单阻断 - imgblock_0006：创建容器黑名单阻断 - imgblock_0007：容器mount proc阻断 - imgblock_0008：容器seccomp unconfined阻断 - imgblock_0009：容器特权阻断 - imgblock_0010：容器capabilities阻断  **默认取值**: 不涉及 

        :param event_class_ids: The event_class_ids of this ListSecurityEventsRequest.
        :type event_class_ids: list[str]
        """
        self._event_class_ids = event_class_ids

    @property
    def severity_list(self):
        r"""Gets the severity_list of this ListSecurityEventsRequest.

        **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 

        :return: The severity_list of this ListSecurityEventsRequest.
        :rtype: list[str]
        """
        return self._severity_list

    @severity_list.setter
    def severity_list(self, severity_list):
        r"""Sets the severity_list of this ListSecurityEventsRequest.

        **参数解释**: 威胁等级 **约束限制**: 不涉及 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值**: 不涉及 

        :param severity_list: The severity_list of this ListSecurityEventsRequest.
        :type severity_list: list[str]
        """
        self._severity_list = severity_list

    @property
    def attack_tag(self):
        r"""Gets the attack_tag of this ListSecurityEventsRequest.

        **参数解释**: 攻击标识 **约束限制**: 不涉及 **取值范围**: - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性  **默认取值**: 不涉及 

        :return: The attack_tag of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._attack_tag

    @attack_tag.setter
    def attack_tag(self, attack_tag):
        r"""Sets the attack_tag of this ListSecurityEventsRequest.

        **参数解释**: 攻击标识 **约束限制**: 不涉及 **取值范围**: - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性  **默认取值**: 不涉及 

        :param attack_tag: The attack_tag of this ListSecurityEventsRequest.
        :type attack_tag: str
        """
        self._attack_tag = attack_tag

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListSecurityEventsRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：般资产 - test：测试资产  **默认取值**: 不涉及 

        :return: The asset_value of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListSecurityEventsRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：般资产 - test：测试资产  **默认取值**: 不涉及 

        :param asset_value: The asset_value of this ListSecurityEventsRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def tag_list(self):
        r"""Gets the tag_list of this ListSecurityEventsRequest.

        事件标签列表，例如:[\"热点事件\"]

        :return: The tag_list of this ListSecurityEventsRequest.
        :rtype: list[str]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        r"""Sets the tag_list of this ListSecurityEventsRequest.

        事件标签列表，例如:[\"热点事件\"]

        :param tag_list: The tag_list of this ListSecurityEventsRequest.
        :type tag_list: list[str]
        """
        self._tag_list = tag_list

    @property
    def att_ck(self):
        r"""Gets the att_ck of this ListSecurityEventsRequest.

        **参数解释**: ATT&CK攻击阶段 **约束限制**: 不涉及 **取值范围**: - Reconnaissance：侦察 - Initial Access：初始访问 - Execution：执行 - Persistence：持久化 - Privilege Escalation：权限提升 - Defense Evasion：防御绕过 - Credential Access：凭据访问 - Command and Control：命令与控制 - Impact：影响破坏  **默认取值**: 不涉及 

        :return: The att_ck of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._att_ck

    @att_ck.setter
    def att_ck(self, att_ck):
        r"""Sets the att_ck of this ListSecurityEventsRequest.

        **参数解释**: ATT&CK攻击阶段 **约束限制**: 不涉及 **取值范围**: - Reconnaissance：侦察 - Initial Access：初始访问 - Execution：执行 - Persistence：持久化 - Privilege Escalation：权限提升 - Defense Evasion：防御绕过 - Credential Access：凭据访问 - Command and Control：命令与控制 - Impact：影响破坏  **默认取值**: 不涉及 

        :param att_ck: The att_ck of this ListSecurityEventsRequest.
        :type att_ck: str
        """
        self._att_ck = att_ck

    @property
    def event_name(self):
        r"""Gets the event_name of this ListSecurityEventsRequest.

        **参数解释**： 告警名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The event_name of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ListSecurityEventsRequest.

        **参数解释**： 告警名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param event_name: The event_name of this ListSecurityEventsRequest.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def auto_block(self):
        r"""Gets the auto_block of this ListSecurityEventsRequest.

        **参数解释**： 是否自动阻断告警 **约束限制**： 不涉及 **取值范围**： - true：自动阻断告警 - false：不自动阻断告警 **默认取值**： 不涉及 

        :return: The auto_block of this ListSecurityEventsRequest.
        :rtype: bool
        """
        return self._auto_block

    @auto_block.setter
    def auto_block(self, auto_block):
        r"""Sets the auto_block of this ListSecurityEventsRequest.

        **参数解释**： 是否自动阻断告警 **约束限制**： 不涉及 **取值范围**： - true：自动阻断告警 - false：不自动阻断告警 **默认取值**： 不涉及 

        :param auto_block: The auto_block of this ListSecurityEventsRequest.
        :type auto_block: bool
        """
        self._auto_block = auto_block

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
        if not isinstance(other, ListSecurityEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
