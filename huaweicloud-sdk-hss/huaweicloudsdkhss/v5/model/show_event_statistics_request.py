# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventStatisticsRequest:

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
        'last_days': 'int',
        'begin_time': 'int',
        'end_time': 'int',
        'category': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'container_name': 'str',
        'event_type': 'int',
        'event_types': 'list[str]',
        'handle_status': 'str',
        'severity': 'str',
        'event_class_ids': 'list[str]',
        'severity_list': 'list[str]',
        'attack_tag': 'str',
        'att_ck': 'str',
        'asset_value': 'str',
        'tag_list': 'list[str]',
        'event_name': 'str',
        'source': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'last_days': 'last_days',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'category': 'category',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'container_name': 'container_name',
        'event_type': 'event_type',
        'event_types': 'event_types',
        'handle_status': 'handle_status',
        'severity': 'severity',
        'event_class_ids': 'event_class_ids',
        'severity_list': 'severity_list',
        'attack_tag': 'attack_tag',
        'att_ck': 'att_ck',
        'asset_value': 'asset_value',
        'tag_list': 'tag_list',
        'event_name': 'event_name',
        'source': 'source'
    }

    def __init__(self, enterprise_project_id=None, last_days=None, begin_time=None, end_time=None, category=None, host_name=None, host_id=None, private_ip=None, public_ip=None, container_name=None, event_type=None, event_types=None, handle_status=None, severity=None, event_class_ids=None, severity_list=None, attack_tag=None, att_ck=None, asset_value=None, tag_list=None, event_name=None, source=None):
        r"""ShowEventStatisticsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param last_days: **参数解释**: 查询时间范围天数 **约束限制**: 与begin_time、end_time互斥，不可同时传参，优先按last_days筛选 **取值范围**: 最小值1，最大值90（支持查询近90天内任务） **默认取值**: 不涉及 
        :type last_days: int
        :param begin_time: **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 
        :type begin_time: int
        :param end_time: **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 
        :type end_time: int
        :param category: **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件 - serverless：serverless - ai：AI Defender  **默认取值**: host 
        :type category: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_id: **参数解释**: 服务器的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param public_ip: **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 
        :type public_ip: str
        :param container_name: **参数解释**: 容器实例名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type container_name: str
        :param event_type: **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3026：crontab提权   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色   - 2006：XSS攻击   - 2007：SQL注入   - 2008：XML注入   - 2009：代码注入   - 2010：命令注入   - 2011：命令执行   - 2042：漏洞逃逸攻击   - 2044：文件逃逸攻击   - 2046：JNDI注入   - 3008：容器进程异常   - 3009：容器异常启动   - 3016：高危系统调用   - 3021：敏感文件访问   - 3023：异常命令执行   - 3025：可疑异常   - 3038：系统日志删除   - 3039：可疑命令执行   - 3040：可疑进程运行   - 3041：可疑进程文件访问   - 3043：运行时异常行为   - 3044：内核模块加载   - 4016：用户账号变更   - 5001：未知网络访问   - 5003：异常外联行为   - 5014：端口转发   - 5015：可疑的下载请求   - 5016：可疑的HTTP请求   - 8005：目录遍历   - 11001：高级威胁事件   - 12001：进程注入   - 12002：动态库注入进程   - 12005：内存文件进程   - 12006：vdso劫持   - 12007：利用Windows工具攻击   - 12008：注册表恶意注入   - 60001：直接提示词注入   - 60002：恶意指令与越狱   - 61001：间接提示词注入   - 61002：数据投毒与误导   - 62001：工具反馈污染   - 62002：工具描述/接口注入   - 63001：越权操作攻击   - 63002：资源耗尽攻击   - 64001：未授权操作   - 64002：权限提升尝试   - 64003：角色访问违规   - 64004：策略约束违规   - 65001：未授权信息输出   - 65002：API密钥/凭证泄露   - 65003：内部业务数据泄露   - 65004：策略约束违规输出   - 65005：隐私信息泄露   - 66001：智能体高危命令执行   - 66002：智能体敏感文件访问   - 67001：其他类告警   - 68001：记忆投毒   - 68002：RAG异常调用   - 68003：工具参数注入   - 68004：工具循环调用   - 68005：上下文资源滥用 
        :type event_type: int
        :param event_types: **参数解释**: 事件大类列表 **约束限制**: 不涉及 **取值范围**: 1-50个事件类型 **默认取值**: 不涉及 
        :type event_types: list[str]
        :param handle_status: **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: 包含如下:   - unhandled：未处理   - handled：已处理  **默认取值**: 不涉及 
        :type handle_status: str
        :param severity: 威胁等级，包含如下:   - Security：安全   - Low：低危   - Medium：中危   - High：高危   - Critical：危急
        :type severity: str
        :param event_class_ids: 事件标识，包含如下: - container_1001：容器命名空间 - container_1002：容器开放端口 - container_1003：容器安全选项 - container_1004：容器挂载目录 - containerescape_0001：容器高危系统调用 - containerescape_0002：Shocker攻击 - containerescape_0003：DirtCow攻击 - containerescape_0004：容器文件逃逸攻击 - dockerfile_001：用户自定义容器保护文件被修改 - dockerfile_002：容器文件系统可执行文件被修改 - dockerproc_001：容器进程异常事件上报 - fileprotect_0001：文件提权 - fileprotect_0002：关键文件变更 - fileprotect_0003：关键文件路径变更 - fileprotect_0004：文件/目录变更 - av_1002：病毒 - av_1003：蠕虫 - av_1004：木马 - av_1005：僵尸网络 - av_1006：后门 - av_1007：间谍软件 - av_1008：恶意广告软件 - av_1009：钓鱼 - av_1010：Rootkit - av_1011：勒索软件 - av_1012：黑客工具 - av_1013：灰色软件 - av_1015：Webshell - av_1016：挖矿软件 - login_0001：尝试暴力破解 - login_0002：爆破成功 - login_1001：登录成功 - login_1002：异地登录 - login_1003：弱口令 - malware_0001：shell变更事件上报 - malware_0002：反弹shell事件上报 - malware_1001：恶意程序 - procdet_0001：进程异常行为检测 - procdet_0002：进程提权 - crontab_0001：crontab脚本提权 - crontab_0002：恶意路径提权 - procreport_0001：危险命令 - user_1001：账号变更 - user_1002：风险账号 - vmescape_0001：虚拟机敏感命令执行 - vmescape_0002：虚拟化进程访问敏感文件 - vmescape_0003：虚拟机异常端口访问 - webshell_0001：网站后门 - network_1001：恶意挖矿 - network_1002：对外DDoS攻击 - network_1003：恶意扫描 - network_1004：敏感区域攻击 - ransomware_0001：勒索攻击 - ransomware_0002：勒索攻击 - ransomware_0003：勒索攻击 - fileless_0001：进程注入 - fileless_0002：动态库注入进程 - fileless_0003：关键配置变更 - fileless_0004：环境变量变更 - fileless_0005：内存文件进程 - fileless_0006：vdso劫持 - crontab_1001：Crontab可疑任务 - vul_exploit_0001：Redis漏洞利用攻击 - vul_exploit_0002：Hadoop漏洞利用攻击 - vul_exploit_0003：MySQL漏洞利用攻击 - rootkit_0001：可疑rootkit文件 - rootkit_0002：可疑内核模块 - RASP_0004：上传Webshell - RASP_0018：无文件Webshell - blockexec_001：已知勒索攻击 - hips_0001：Windows Defender防护被禁用 - hips_0002：可疑的黑客工具 - hips_0003：可疑的勒索加密行为 - hips_0004：隐藏账号创建 - hips_0005：读取用户密码凭据 - hips_0006：可疑的SAM文件导出 - hips_0007：可疑shadow copy删除操作 - hips_0008：备份文件删除 - hips_0009：可疑勒索病毒操作注册表 - hips_0010：可疑的异常进程行为 - hips_0011：可疑的扫描探测 - hips_0012：可疑的勒索病毒脚本运行 - hips_0013：可疑的挖矿命令执行 - hips_0014：可疑的禁用windows安全中心 - hips_0015：可疑的停止防火墙服务行为 - hips_0016：可疑的系统自动恢复禁用 - hips_0017：Office创建可执行文件 - hips_0018：带宏Office文件异常创建 - hips_0019：可疑的注册表操作 - hips_0020：Confluence远程代码执行 - hips_0021：MSDT远程代码执行 - portscan_0001：通用端口扫描 - portscan_0002：秘密端口扫描 - k8s_1001：Kubernetes事件删除 - k8s_1002：创建特权Pod - k8s_1003：Pod中使用交互式shell - k8s_1004：创建敏感目录Pod - k8s_1005：创建主机网络的Pod - k8s_1006：创建主机Pid空间的Pod - k8s_1007：普通pod访问APIserver认证失败 - k8s_1008：普通Pod通过Curl访问APIServer - k8s_1009：系统管理空间执行exec - k8s_1010：系统管理空间创建Pod - k8s_1011：创建静态Pod - k8s_1012：创建DaemonSet - k8s_1013：创建集群计划任务 - k8s_1014：Secrets操作 - k8s_1015：枚举用户可执行的操作 - k8s_1016：高权限RoleBinding或ClusterRoleBinding - k8s_1017：ServiceAccount创建 - k8s_1018：创建Cronjob - k8s_1019：Pod中exec使用交互式shell - k8s_1020：无权限访问Apiserver - k8s_1021：使用curl访问APIServer - k8s_1022：Ingress漏洞 - k8s_1023：中间人攻击 - k8s_1024：蠕虫挖矿木马 - k8s_1025：K8s事件删除 - k8s_1026：SelfSubjectRulesReview场景 - imgblock_0001：镜像白名单阻断 - imgblock_0002：镜像黑名单阻断 - imgblock_0003：镜像标签白名单阻断 - imgblock_0004：镜像标签黑名单阻断 - imgblock_0005：创建容器白名单阻断 - imgblock_0006：创建容器黑名单阻断 - imgblock_0007：容器mount proc阻断 - imgblock_0008：容器seccomp unconfined阻断 - imgblock_0009：容器特权阻断 - imgblock_0010：容器capabilities阻断
        :type event_class_ids: list[str]
        :param severity_list: **参数解释**: 威胁等级，已废弃 **约束限制**: 不涉及 **取值范围**: 威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命  **默认取值**: 不涉及 
        :type severity_list: list[str]
        :param attack_tag: 攻击标识，包含如下：   - attack_success : 攻击成功   - attack_attempt : 攻击尝试   - attack_blocked : 攻击被阻断   - abnormal_behavior : 异常行为   - collapsible_host : 主机失陷   - system_vulnerability : 系统脆弱性
        :type attack_tag: str
        :param att_ck: **参数解释**： ATT&amp;CK攻击阶段 **约束限制**: 不涉及 **取值范围**: - Reconnaissance：侦察 - Initial Access：初始访问 - Execution：执行 - Persistence：持久化 - Privilege Escalation：权限提升 - Defense Evasion：防御绕过 - Credential Access：凭据访问 - Command and Control：命令与控制 - Impact：影响破坏  **默认取值**: 不涉及 
        :type att_ck: str
        :param asset_value: **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 
        :type asset_value: str
        :param tag_list: **参数解释**: 事件标签 **约束限制**: 不涉及 **取值范围**: 1-20个标签 **默认取值**: 不涉及 
        :type tag_list: list[str]
        :param event_name: 告警名称
        :type event_name: str
        :param source: **参数解释**: 来源 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type source: str
        """
        
        

        self._enterprise_project_id = None
        self._last_days = None
        self._begin_time = None
        self._end_time = None
        self._category = None
        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._public_ip = None
        self._container_name = None
        self._event_type = None
        self._event_types = None
        self._handle_status = None
        self._severity = None
        self._event_class_ids = None
        self._severity_list = None
        self._attack_tag = None
        self._att_ck = None
        self._asset_value = None
        self._tag_list = None
        self._event_name = None
        self._source = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if last_days is not None:
            self.last_days = last_days
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if category is not None:
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
        if event_types is not None:
            self.event_types = event_types
        if handle_status is not None:
            self.handle_status = handle_status
        if severity is not None:
            self.severity = severity
        if event_class_ids is not None:
            self.event_class_ids = event_class_ids
        if severity_list is not None:
            self.severity_list = severity_list
        if attack_tag is not None:
            self.attack_tag = attack_tag
        if att_ck is not None:
            self.att_ck = att_ck
        if asset_value is not None:
            self.asset_value = asset_value
        if tag_list is not None:
            self.tag_list = tag_list
        if event_name is not None:
            self.event_name = event_name
        if source is not None:
            self.source = source

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowEventStatisticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowEventStatisticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowEventStatisticsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def last_days(self):
        r"""Gets the last_days of this ShowEventStatisticsRequest.

        **参数解释**: 查询时间范围天数 **约束限制**: 与begin_time、end_time互斥，不可同时传参，优先按last_days筛选 **取值范围**: 最小值1，最大值90（支持查询近90天内任务） **默认取值**: 不涉及 

        :return: The last_days of this ShowEventStatisticsRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ShowEventStatisticsRequest.

        **参数解释**: 查询时间范围天数 **约束限制**: 与begin_time、end_time互斥，不可同时传参，优先按last_days筛选 **取值范围**: 最小值1，最大值90（支持查询近90天内任务） **默认取值**: 不涉及 

        :param last_days: The last_days of this ShowEventStatisticsRequest.
        :type last_days: int
        """
        self._last_days = last_days

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowEventStatisticsRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :return: The begin_time of this ShowEventStatisticsRequest.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowEventStatisticsRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :param begin_time: The begin_time of this ShowEventStatisticsRequest.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowEventStatisticsRequest.

        **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :return: The end_time of this ShowEventStatisticsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowEventStatisticsRequest.

        **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :param end_time: The end_time of this ShowEventStatisticsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def category(self):
        r"""Gets the category of this ShowEventStatisticsRequest.

        **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件 - serverless：serverless - ai：AI Defender  **默认取值**: host 

        :return: The category of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowEventStatisticsRequest.

        **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件 - serverless：serverless - ai：AI Defender  **默认取值**: host 

        :param category: The category of this ShowEventStatisticsRequest.
        :type category: str
        """
        self._category = category

    @property
    def host_name(self):
        r"""Gets the host_name of this ShowEventStatisticsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ShowEventStatisticsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ShowEventStatisticsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ShowEventStatisticsRequest.

        **参数解释**: 服务器的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ShowEventStatisticsRequest.

        **参数解释**: 服务器的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ShowEventStatisticsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ShowEventStatisticsRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ShowEventStatisticsRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ShowEventStatisticsRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ShowEventStatisticsRequest.

        **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 

        :return: The public_ip of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ShowEventStatisticsRequest.

        **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 

        :param public_ip: The public_ip of this ShowEventStatisticsRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def container_name(self):
        r"""Gets the container_name of this ShowEventStatisticsRequest.

        **参数解释**: 容器实例名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The container_name of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ShowEventStatisticsRequest.

        **参数解释**: 容器实例名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param container_name: The container_name of this ShowEventStatisticsRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def event_type(self):
        r"""Gets the event_type of this ShowEventStatisticsRequest.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3026：crontab提权   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色   - 2006：XSS攻击   - 2007：SQL注入   - 2008：XML注入   - 2009：代码注入   - 2010：命令注入   - 2011：命令执行   - 2042：漏洞逃逸攻击   - 2044：文件逃逸攻击   - 2046：JNDI注入   - 3008：容器进程异常   - 3009：容器异常启动   - 3016：高危系统调用   - 3021：敏感文件访问   - 3023：异常命令执行   - 3025：可疑异常   - 3038：系统日志删除   - 3039：可疑命令执行   - 3040：可疑进程运行   - 3041：可疑进程文件访问   - 3043：运行时异常行为   - 3044：内核模块加载   - 4016：用户账号变更   - 5001：未知网络访问   - 5003：异常外联行为   - 5014：端口转发   - 5015：可疑的下载请求   - 5016：可疑的HTTP请求   - 8005：目录遍历   - 11001：高级威胁事件   - 12001：进程注入   - 12002：动态库注入进程   - 12005：内存文件进程   - 12006：vdso劫持   - 12007：利用Windows工具攻击   - 12008：注册表恶意注入   - 60001：直接提示词注入   - 60002：恶意指令与越狱   - 61001：间接提示词注入   - 61002：数据投毒与误导   - 62001：工具反馈污染   - 62002：工具描述/接口注入   - 63001：越权操作攻击   - 63002：资源耗尽攻击   - 64001：未授权操作   - 64002：权限提升尝试   - 64003：角色访问违规   - 64004：策略约束违规   - 65001：未授权信息输出   - 65002：API密钥/凭证泄露   - 65003：内部业务数据泄露   - 65004：策略约束违规输出   - 65005：隐私信息泄露   - 66001：智能体高危命令执行   - 66002：智能体敏感文件访问   - 67001：其他类告警   - 68001：记忆投毒   - 68002：RAG异常调用   - 68003：工具参数注入   - 68004：工具循环调用   - 68005：上下文资源滥用 

        :return: The event_type of this ShowEventStatisticsRequest.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ShowEventStatisticsRequest.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3026：crontab提权   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色   - 2006：XSS攻击   - 2007：SQL注入   - 2008：XML注入   - 2009：代码注入   - 2010：命令注入   - 2011：命令执行   - 2042：漏洞逃逸攻击   - 2044：文件逃逸攻击   - 2046：JNDI注入   - 3008：容器进程异常   - 3009：容器异常启动   - 3016：高危系统调用   - 3021：敏感文件访问   - 3023：异常命令执行   - 3025：可疑异常   - 3038：系统日志删除   - 3039：可疑命令执行   - 3040：可疑进程运行   - 3041：可疑进程文件访问   - 3043：运行时异常行为   - 3044：内核模块加载   - 4016：用户账号变更   - 5001：未知网络访问   - 5003：异常外联行为   - 5014：端口转发   - 5015：可疑的下载请求   - 5016：可疑的HTTP请求   - 8005：目录遍历   - 11001：高级威胁事件   - 12001：进程注入   - 12002：动态库注入进程   - 12005：内存文件进程   - 12006：vdso劫持   - 12007：利用Windows工具攻击   - 12008：注册表恶意注入   - 60001：直接提示词注入   - 60002：恶意指令与越狱   - 61001：间接提示词注入   - 61002：数据投毒与误导   - 62001：工具反馈污染   - 62002：工具描述/接口注入   - 63001：越权操作攻击   - 63002：资源耗尽攻击   - 64001：未授权操作   - 64002：权限提升尝试   - 64003：角色访问违规   - 64004：策略约束违规   - 65001：未授权信息输出   - 65002：API密钥/凭证泄露   - 65003：内部业务数据泄露   - 65004：策略约束违规输出   - 65005：隐私信息泄露   - 66001：智能体高危命令执行   - 66002：智能体敏感文件访问   - 67001：其他类告警   - 68001：记忆投毒   - 68002：RAG异常调用   - 68003：工具参数注入   - 68004：工具循环调用   - 68005：上下文资源滥用 

        :param event_type: The event_type of this ShowEventStatisticsRequest.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def event_types(self):
        r"""Gets the event_types of this ShowEventStatisticsRequest.

        **参数解释**: 事件大类列表 **约束限制**: 不涉及 **取值范围**: 1-50个事件类型 **默认取值**: 不涉及 

        :return: The event_types of this ShowEventStatisticsRequest.
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        r"""Sets the event_types of this ShowEventStatisticsRequest.

        **参数解释**: 事件大类列表 **约束限制**: 不涉及 **取值范围**: 1-50个事件类型 **默认取值**: 不涉及 

        :param event_types: The event_types of this ShowEventStatisticsRequest.
        :type event_types: list[str]
        """
        self._event_types = event_types

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ShowEventStatisticsRequest.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: 包含如下:   - unhandled：未处理   - handled：已处理  **默认取值**: 不涉及 

        :return: The handle_status of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ShowEventStatisticsRequest.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: 包含如下:   - unhandled：未处理   - handled：已处理  **默认取值**: 不涉及 

        :param handle_status: The handle_status of this ShowEventStatisticsRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def severity(self):
        r"""Gets the severity of this ShowEventStatisticsRequest.

        威胁等级，包含如下:   - Security：安全   - Low：低危   - Medium：中危   - High：高危   - Critical：危急

        :return: The severity of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ShowEventStatisticsRequest.

        威胁等级，包含如下:   - Security：安全   - Low：低危   - Medium：中危   - High：高危   - Critical：危急

        :param severity: The severity of this ShowEventStatisticsRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def event_class_ids(self):
        r"""Gets the event_class_ids of this ShowEventStatisticsRequest.

        事件标识，包含如下: - container_1001：容器命名空间 - container_1002：容器开放端口 - container_1003：容器安全选项 - container_1004：容器挂载目录 - containerescape_0001：容器高危系统调用 - containerescape_0002：Shocker攻击 - containerescape_0003：DirtCow攻击 - containerescape_0004：容器文件逃逸攻击 - dockerfile_001：用户自定义容器保护文件被修改 - dockerfile_002：容器文件系统可执行文件被修改 - dockerproc_001：容器进程异常事件上报 - fileprotect_0001：文件提权 - fileprotect_0002：关键文件变更 - fileprotect_0003：关键文件路径变更 - fileprotect_0004：文件/目录变更 - av_1002：病毒 - av_1003：蠕虫 - av_1004：木马 - av_1005：僵尸网络 - av_1006：后门 - av_1007：间谍软件 - av_1008：恶意广告软件 - av_1009：钓鱼 - av_1010：Rootkit - av_1011：勒索软件 - av_1012：黑客工具 - av_1013：灰色软件 - av_1015：Webshell - av_1016：挖矿软件 - login_0001：尝试暴力破解 - login_0002：爆破成功 - login_1001：登录成功 - login_1002：异地登录 - login_1003：弱口令 - malware_0001：shell变更事件上报 - malware_0002：反弹shell事件上报 - malware_1001：恶意程序 - procdet_0001：进程异常行为检测 - procdet_0002：进程提权 - crontab_0001：crontab脚本提权 - crontab_0002：恶意路径提权 - procreport_0001：危险命令 - user_1001：账号变更 - user_1002：风险账号 - vmescape_0001：虚拟机敏感命令执行 - vmescape_0002：虚拟化进程访问敏感文件 - vmescape_0003：虚拟机异常端口访问 - webshell_0001：网站后门 - network_1001：恶意挖矿 - network_1002：对外DDoS攻击 - network_1003：恶意扫描 - network_1004：敏感区域攻击 - ransomware_0001：勒索攻击 - ransomware_0002：勒索攻击 - ransomware_0003：勒索攻击 - fileless_0001：进程注入 - fileless_0002：动态库注入进程 - fileless_0003：关键配置变更 - fileless_0004：环境变量变更 - fileless_0005：内存文件进程 - fileless_0006：vdso劫持 - crontab_1001：Crontab可疑任务 - vul_exploit_0001：Redis漏洞利用攻击 - vul_exploit_0002：Hadoop漏洞利用攻击 - vul_exploit_0003：MySQL漏洞利用攻击 - rootkit_0001：可疑rootkit文件 - rootkit_0002：可疑内核模块 - RASP_0004：上传Webshell - RASP_0018：无文件Webshell - blockexec_001：已知勒索攻击 - hips_0001：Windows Defender防护被禁用 - hips_0002：可疑的黑客工具 - hips_0003：可疑的勒索加密行为 - hips_0004：隐藏账号创建 - hips_0005：读取用户密码凭据 - hips_0006：可疑的SAM文件导出 - hips_0007：可疑shadow copy删除操作 - hips_0008：备份文件删除 - hips_0009：可疑勒索病毒操作注册表 - hips_0010：可疑的异常进程行为 - hips_0011：可疑的扫描探测 - hips_0012：可疑的勒索病毒脚本运行 - hips_0013：可疑的挖矿命令执行 - hips_0014：可疑的禁用windows安全中心 - hips_0015：可疑的停止防火墙服务行为 - hips_0016：可疑的系统自动恢复禁用 - hips_0017：Office创建可执行文件 - hips_0018：带宏Office文件异常创建 - hips_0019：可疑的注册表操作 - hips_0020：Confluence远程代码执行 - hips_0021：MSDT远程代码执行 - portscan_0001：通用端口扫描 - portscan_0002：秘密端口扫描 - k8s_1001：Kubernetes事件删除 - k8s_1002：创建特权Pod - k8s_1003：Pod中使用交互式shell - k8s_1004：创建敏感目录Pod - k8s_1005：创建主机网络的Pod - k8s_1006：创建主机Pid空间的Pod - k8s_1007：普通pod访问APIserver认证失败 - k8s_1008：普通Pod通过Curl访问APIServer - k8s_1009：系统管理空间执行exec - k8s_1010：系统管理空间创建Pod - k8s_1011：创建静态Pod - k8s_1012：创建DaemonSet - k8s_1013：创建集群计划任务 - k8s_1014：Secrets操作 - k8s_1015：枚举用户可执行的操作 - k8s_1016：高权限RoleBinding或ClusterRoleBinding - k8s_1017：ServiceAccount创建 - k8s_1018：创建Cronjob - k8s_1019：Pod中exec使用交互式shell - k8s_1020：无权限访问Apiserver - k8s_1021：使用curl访问APIServer - k8s_1022：Ingress漏洞 - k8s_1023：中间人攻击 - k8s_1024：蠕虫挖矿木马 - k8s_1025：K8s事件删除 - k8s_1026：SelfSubjectRulesReview场景 - imgblock_0001：镜像白名单阻断 - imgblock_0002：镜像黑名单阻断 - imgblock_0003：镜像标签白名单阻断 - imgblock_0004：镜像标签黑名单阻断 - imgblock_0005：创建容器白名单阻断 - imgblock_0006：创建容器黑名单阻断 - imgblock_0007：容器mount proc阻断 - imgblock_0008：容器seccomp unconfined阻断 - imgblock_0009：容器特权阻断 - imgblock_0010：容器capabilities阻断

        :return: The event_class_ids of this ShowEventStatisticsRequest.
        :rtype: list[str]
        """
        return self._event_class_ids

    @event_class_ids.setter
    def event_class_ids(self, event_class_ids):
        r"""Sets the event_class_ids of this ShowEventStatisticsRequest.

        事件标识，包含如下: - container_1001：容器命名空间 - container_1002：容器开放端口 - container_1003：容器安全选项 - container_1004：容器挂载目录 - containerescape_0001：容器高危系统调用 - containerescape_0002：Shocker攻击 - containerescape_0003：DirtCow攻击 - containerescape_0004：容器文件逃逸攻击 - dockerfile_001：用户自定义容器保护文件被修改 - dockerfile_002：容器文件系统可执行文件被修改 - dockerproc_001：容器进程异常事件上报 - fileprotect_0001：文件提权 - fileprotect_0002：关键文件变更 - fileprotect_0003：关键文件路径变更 - fileprotect_0004：文件/目录变更 - av_1002：病毒 - av_1003：蠕虫 - av_1004：木马 - av_1005：僵尸网络 - av_1006：后门 - av_1007：间谍软件 - av_1008：恶意广告软件 - av_1009：钓鱼 - av_1010：Rootkit - av_1011：勒索软件 - av_1012：黑客工具 - av_1013：灰色软件 - av_1015：Webshell - av_1016：挖矿软件 - login_0001：尝试暴力破解 - login_0002：爆破成功 - login_1001：登录成功 - login_1002：异地登录 - login_1003：弱口令 - malware_0001：shell变更事件上报 - malware_0002：反弹shell事件上报 - malware_1001：恶意程序 - procdet_0001：进程异常行为检测 - procdet_0002：进程提权 - crontab_0001：crontab脚本提权 - crontab_0002：恶意路径提权 - procreport_0001：危险命令 - user_1001：账号变更 - user_1002：风险账号 - vmescape_0001：虚拟机敏感命令执行 - vmescape_0002：虚拟化进程访问敏感文件 - vmescape_0003：虚拟机异常端口访问 - webshell_0001：网站后门 - network_1001：恶意挖矿 - network_1002：对外DDoS攻击 - network_1003：恶意扫描 - network_1004：敏感区域攻击 - ransomware_0001：勒索攻击 - ransomware_0002：勒索攻击 - ransomware_0003：勒索攻击 - fileless_0001：进程注入 - fileless_0002：动态库注入进程 - fileless_0003：关键配置变更 - fileless_0004：环境变量变更 - fileless_0005：内存文件进程 - fileless_0006：vdso劫持 - crontab_1001：Crontab可疑任务 - vul_exploit_0001：Redis漏洞利用攻击 - vul_exploit_0002：Hadoop漏洞利用攻击 - vul_exploit_0003：MySQL漏洞利用攻击 - rootkit_0001：可疑rootkit文件 - rootkit_0002：可疑内核模块 - RASP_0004：上传Webshell - RASP_0018：无文件Webshell - blockexec_001：已知勒索攻击 - hips_0001：Windows Defender防护被禁用 - hips_0002：可疑的黑客工具 - hips_0003：可疑的勒索加密行为 - hips_0004：隐藏账号创建 - hips_0005：读取用户密码凭据 - hips_0006：可疑的SAM文件导出 - hips_0007：可疑shadow copy删除操作 - hips_0008：备份文件删除 - hips_0009：可疑勒索病毒操作注册表 - hips_0010：可疑的异常进程行为 - hips_0011：可疑的扫描探测 - hips_0012：可疑的勒索病毒脚本运行 - hips_0013：可疑的挖矿命令执行 - hips_0014：可疑的禁用windows安全中心 - hips_0015：可疑的停止防火墙服务行为 - hips_0016：可疑的系统自动恢复禁用 - hips_0017：Office创建可执行文件 - hips_0018：带宏Office文件异常创建 - hips_0019：可疑的注册表操作 - hips_0020：Confluence远程代码执行 - hips_0021：MSDT远程代码执行 - portscan_0001：通用端口扫描 - portscan_0002：秘密端口扫描 - k8s_1001：Kubernetes事件删除 - k8s_1002：创建特权Pod - k8s_1003：Pod中使用交互式shell - k8s_1004：创建敏感目录Pod - k8s_1005：创建主机网络的Pod - k8s_1006：创建主机Pid空间的Pod - k8s_1007：普通pod访问APIserver认证失败 - k8s_1008：普通Pod通过Curl访问APIServer - k8s_1009：系统管理空间执行exec - k8s_1010：系统管理空间创建Pod - k8s_1011：创建静态Pod - k8s_1012：创建DaemonSet - k8s_1013：创建集群计划任务 - k8s_1014：Secrets操作 - k8s_1015：枚举用户可执行的操作 - k8s_1016：高权限RoleBinding或ClusterRoleBinding - k8s_1017：ServiceAccount创建 - k8s_1018：创建Cronjob - k8s_1019：Pod中exec使用交互式shell - k8s_1020：无权限访问Apiserver - k8s_1021：使用curl访问APIServer - k8s_1022：Ingress漏洞 - k8s_1023：中间人攻击 - k8s_1024：蠕虫挖矿木马 - k8s_1025：K8s事件删除 - k8s_1026：SelfSubjectRulesReview场景 - imgblock_0001：镜像白名单阻断 - imgblock_0002：镜像黑名单阻断 - imgblock_0003：镜像标签白名单阻断 - imgblock_0004：镜像标签黑名单阻断 - imgblock_0005：创建容器白名单阻断 - imgblock_0006：创建容器黑名单阻断 - imgblock_0007：容器mount proc阻断 - imgblock_0008：容器seccomp unconfined阻断 - imgblock_0009：容器特权阻断 - imgblock_0010：容器capabilities阻断

        :param event_class_ids: The event_class_ids of this ShowEventStatisticsRequest.
        :type event_class_ids: list[str]
        """
        self._event_class_ids = event_class_ids

    @property
    def severity_list(self):
        r"""Gets the severity_list of this ShowEventStatisticsRequest.

        **参数解释**: 威胁等级，已废弃 **约束限制**: 不涉及 **取值范围**: 威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命  **默认取值**: 不涉及 

        :return: The severity_list of this ShowEventStatisticsRequest.
        :rtype: list[str]
        """
        return self._severity_list

    @severity_list.setter
    def severity_list(self, severity_list):
        r"""Sets the severity_list of this ShowEventStatisticsRequest.

        **参数解释**: 威胁等级，已废弃 **约束限制**: 不涉及 **取值范围**: 威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命  **默认取值**: 不涉及 

        :param severity_list: The severity_list of this ShowEventStatisticsRequest.
        :type severity_list: list[str]
        """
        self._severity_list = severity_list

    @property
    def attack_tag(self):
        r"""Gets the attack_tag of this ShowEventStatisticsRequest.

        攻击标识，包含如下：   - attack_success : 攻击成功   - attack_attempt : 攻击尝试   - attack_blocked : 攻击被阻断   - abnormal_behavior : 异常行为   - collapsible_host : 主机失陷   - system_vulnerability : 系统脆弱性

        :return: The attack_tag of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._attack_tag

    @attack_tag.setter
    def attack_tag(self, attack_tag):
        r"""Sets the attack_tag of this ShowEventStatisticsRequest.

        攻击标识，包含如下：   - attack_success : 攻击成功   - attack_attempt : 攻击尝试   - attack_blocked : 攻击被阻断   - abnormal_behavior : 异常行为   - collapsible_host : 主机失陷   - system_vulnerability : 系统脆弱性

        :param attack_tag: The attack_tag of this ShowEventStatisticsRequest.
        :type attack_tag: str
        """
        self._attack_tag = attack_tag

    @property
    def att_ck(self):
        r"""Gets the att_ck of this ShowEventStatisticsRequest.

        **参数解释**： ATT&CK攻击阶段 **约束限制**: 不涉及 **取值范围**: - Reconnaissance：侦察 - Initial Access：初始访问 - Execution：执行 - Persistence：持久化 - Privilege Escalation：权限提升 - Defense Evasion：防御绕过 - Credential Access：凭据访问 - Command and Control：命令与控制 - Impact：影响破坏  **默认取值**: 不涉及 

        :return: The att_ck of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._att_ck

    @att_ck.setter
    def att_ck(self, att_ck):
        r"""Sets the att_ck of this ShowEventStatisticsRequest.

        **参数解释**： ATT&CK攻击阶段 **约束限制**: 不涉及 **取值范围**: - Reconnaissance：侦察 - Initial Access：初始访问 - Execution：执行 - Persistence：持久化 - Privilege Escalation：权限提升 - Defense Evasion：防御绕过 - Credential Access：凭据访问 - Command and Control：命令与控制 - Impact：影响破坏  **默认取值**: 不涉及 

        :param att_ck: The att_ck of this ShowEventStatisticsRequest.
        :type att_ck: str
        """
        self._att_ck = att_ck

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ShowEventStatisticsRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :return: The asset_value of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ShowEventStatisticsRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :param asset_value: The asset_value of this ShowEventStatisticsRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def tag_list(self):
        r"""Gets the tag_list of this ShowEventStatisticsRequest.

        **参数解释**: 事件标签 **约束限制**: 不涉及 **取值范围**: 1-20个标签 **默认取值**: 不涉及 

        :return: The tag_list of this ShowEventStatisticsRequest.
        :rtype: list[str]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        r"""Sets the tag_list of this ShowEventStatisticsRequest.

        **参数解释**: 事件标签 **约束限制**: 不涉及 **取值范围**: 1-20个标签 **默认取值**: 不涉及 

        :param tag_list: The tag_list of this ShowEventStatisticsRequest.
        :type tag_list: list[str]
        """
        self._tag_list = tag_list

    @property
    def event_name(self):
        r"""Gets the event_name of this ShowEventStatisticsRequest.

        告警名称

        :return: The event_name of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ShowEventStatisticsRequest.

        告警名称

        :param event_name: The event_name of this ShowEventStatisticsRequest.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def source(self):
        r"""Gets the source of this ShowEventStatisticsRequest.

        **参数解释**: 来源 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The source of this ShowEventStatisticsRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ShowEventStatisticsRequest.

        **参数解释**: 来源 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param source: The source of this ShowEventStatisticsRequest.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, ShowEventStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
