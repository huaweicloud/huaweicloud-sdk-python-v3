# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppWhitelistEventResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'event_class_id': 'str',
        'event_type': 'int',
        'event_name': 'str',
        'severity': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'attack_phase': 'str',
        'attack_tag': 'str',
        'occur_time': 'int',
        'handle_time': 'int',
        'handle_status': 'str',
        'handle_method': 'str',
        'operate_accept_list': 'list[str]',
        'operate_detail_list': 'list[AppWhitelistEventDetailResInfo]',
        'resource_info': 'ProcessEventResourceResponseInfo',
        'recommendation': 'str',
        'process_info': 'list[EventProcessResInfo]',
        'policy_id': 'str',
        'policy_name': 'str',
        'os_type': 'str',
        'asset_value': 'str',
        'host_status': 'str',
        'agent_status': 'str',
        'protect_status': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'event_class_id': 'event_class_id',
        'event_type': 'event_type',
        'event_name': 'event_name',
        'severity': 'severity',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'attack_phase': 'attack_phase',
        'attack_tag': 'attack_tag',
        'occur_time': 'occur_time',
        'handle_time': 'handle_time',
        'handle_status': 'handle_status',
        'handle_method': 'handle_method',
        'operate_accept_list': 'operate_accept_list',
        'operate_detail_list': 'operate_detail_list',
        'resource_info': 'resource_info',
        'recommendation': 'recommendation',
        'process_info': 'process_info',
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'os_type': 'os_type',
        'asset_value': 'asset_value',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'protect_status': 'protect_status'
    }

    def __init__(self, event_id=None, event_class_id=None, event_type=None, event_name=None, severity=None, host_name=None, host_id=None, private_ip=None, public_ip=None, attack_phase=None, attack_tag=None, occur_time=None, handle_time=None, handle_status=None, handle_method=None, operate_accept_list=None, operate_detail_list=None, resource_info=None, recommendation=None, process_info=None, policy_id=None, policy_name=None, os_type=None, asset_value=None, host_status=None, agent_status=None, protect_status=None):
        r"""AppWhitelistEventResponseInfo

        The model defined in huaweicloud sdk

        :param event_id: **参数解释**： 事件ID **取值范围**： 字符长度1-64位 
        :type event_id: str
        :param event_class_id: **参数解释**： 事件分类 **取值范围**：   - container_1001：容器命名空间   - container_1002：容器开放端口   - container_1003：容器安全选项   - container_1004：容器挂载目录   - containerescape_0001：容器高危系统调用   - containerescape_0002：Shocker攻击   - containerescape_0003：DirtCow攻击   - containerescape_0004：容器文件逃逸攻击   - dockerfile_001：用户自定义容器保护文件被修改   - dockerfile_002：容器文件系统可执行文件被修改   - dockerproc_001：容器进程异常事件上报   - fileprotect_0001：文件提权   - fileprotect_0002：关键文件变更   - fileprotect_0003：关键文件路径变更   - fileprotect_0004：文件/目录变更   - av_1002：病毒   - av_1003：蠕虫   - av_1004：木马   - av_1005：僵尸网络   - av_1006：后门   - av_1007：间谍软件   - av_1008：恶意广告软件   - av_1009：钓鱼   - av_1010：Rootkit   - av_1011：勒索软件   - av_1012：黑客工具   - av_1013：灰色软件   - av_1015：Webshell   - av_1016：挖矿软件   - login_0001：尝试暴力破解   - login_0002：爆破成功   - login_1001：登录成功   - login_1002：异地登录   - login_1003：弱口令   - malware_0001：shell变更事件上报   - malware_0002：反弹shell事件上报   - malware_1001：恶意程序   - procdet_0001：进程异常行为检测   - procdet_0002：进程提权   - procreport_0001：危险命令   - user_1001：账号变更   - user_1002：风险账号   - vmescape_0001：虚拟机敏感命令执行   - vmescape_0002：虚拟化进程访问敏感文件   - vmescape_0003：虚拟机异常端口访问   - webshell_0001：网站后门   - network_1001：恶意挖矿   - network_1002：对外DDoS攻击   - network_1003：恶意扫描   - network_1004：敏感区域攻击   - ransomware_0001：勒索攻击   - ransomware_0002：勒索攻击   - ransomware_0003：勒索攻击   - fileless_0001：进程注入   - fileless_0002：动态库注入进程   - fileless_0003：关键配置变更   - fileless_0004：环境变量变更   - fileless_0005：内存文件进程   - fileless_0006：vdso劫持   - crontab_1001：Crontab可疑任务   - vul_exploit_0001：Redis漏洞利用攻击   - vul_exploit_0002：Hadoop漏洞利用攻击   - vul_exploit_0003：MySQL漏洞利用攻击   - rootkit_0001：可疑rootkit文件   - rootkit_0002：可疑内核模块   - RASP_0004：上传Webshell   - RASP_0018：无文件Webshell   - blockexec_001：已知勒索攻击   - hips_0001：Windows Defender防护被禁用   - hips_0002：可疑的黑客工具   - hips_0003：可疑的勒索加密行为   - hips_0004：隐藏账号创建   - hips_0005：读取用户密码凭据   - hips_0006：可疑的SAM文件导出   - hips_0007：可疑shadow copy删除操作   - hips_0008：备份文件删除   - hips_0009：可疑勒索病毒操作注册表   - hips_0010：可疑的异常进程行为   - hips_0011：可疑的扫描探测   - hips_0012：可疑的勒索病毒脚本运行   - hips_0013：可疑的挖矿命令执行   - hips_0014：可疑的禁用windows安全中心   - hips_0015：可疑的停止防火墙服务行为   - hips_0016：可疑的系统自动恢复禁用   - hips_0017：Offies创建可执行文件   - hips_0018：带宏Offies文件异常创建   - hips_0019：可疑的注册表操作   - hips_0020：Confluence远程代码执行   - hips_0021：MSDT远程代码执行   - portscan_0001：通用端口扫描   - portscan_0002：秘密端口扫描   - k8s_1001：Kubernetes事件删除   - k8s_1002：创建特权Pod   - k8s_1003：Pod中使用交互式shell   - k8s_1004：创建敏感目录Pod   - k8s_1005：创建主机网络的Pod   - k8s_1006：创建主机Pid空间的Pod   - k8s_1007：普通pod访问APIserver认证失败   - k8s_1008：普通Pod通过Curl访问APIServer   - k8s_1009：系统管理空间执行exec   - k8s_1010：系统管理空间创建Pod   - k8s_1011：创建静态Pod   - k8s_1012：创建DaemonSet   - k8s_1013：创建集群计划任务   - k8s_1014：Secrets操作   - k8s_1015：枚举用户可执行的操作   - k8s_1016：高权限RoleBinding或ClusterRoleBinding   - k8s_1017：ServiceAccount创建   - k8s_1018：创建Cronjob   - k8s_1019：Pod中exec使用交互式shell   - k8s_1020：无权限访问Apiserver   - k8s_1021：使用curl访问APIServer   - k8s_1022：Ingress漏洞   - k8s_1023：中间人攻击   - k8s_1024：蠕虫挖矿木马   - k8s_1025：K8s事件删除   - k8s_1026：SelfSubjectRulesReview场景   - imgblock_0001：镜像白名单阻断   - imgblock_0002：镜像黑名单阻断   - imgblock_0003：镜像标签白名单阻断   - imgblock_0004：镜像标签黑名单阻断   - imgblock_0005：创建容器白名单阻断   - imgblock_0006：创建容器黑名单阻断   - imgblock_0007：容器mount proc阻断   - imgblock_0008：容器seccomp unconfined阻断   - imgblock_0009：容器特权阻断   - imgblock_0010：容器capabilities阻断 
        :type event_class_id: str
        :param event_type: 事件类型，包含如下:   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色
        :type event_type: int
        :param event_name: 事件名称   - \&quot;white list alert malicious process\&quot;   - \&quot;white list alert suspicious process\&quot;
        :type event_name: str
        :param severity: **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 
        :type severity: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param attack_phase: **参数解释**： 攻击阶段 **取值范围**： - reconnaissance：侦查跟踪 - weaponization：武器构建 - delivery：载荷投递 - exploit：漏洞利用 - installation：安装植入 - command_and_control：命令与控制 - actions：目标达成 
        :type attack_phase: str
        :param attack_tag: **参数解释**： 攻击标识 **取值范围**： - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性 
        :type attack_tag: str
        :param occur_time: **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 
        :type occur_time: int
        :param handle_time: **参数解释**： 处置时间，毫秒，已处理的告警才有 **取值范围**： 最小值0，最大值9223372036854775807 
        :type handle_time: int
        :param handle_status: **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 
        :type handle_status: str
        :param handle_method: **参数解释**： 处理状态 **约束限制**: 不涉及 **取值范围**: - mark_as_trust：标记为可信 - mark_as_suspicious：标记为可疑 - isolate_and_kill：隔离查杀  **默认取值**: 不涉及 
        :type handle_method: str
        :param operate_accept_list: **参数解释**: 支持的处理操作 **约束限制**: 不涉及 
        :type operate_accept_list: list[str]
        :param operate_detail_list: 操作详情信息列表（页面不展示）
        :type operate_detail_list: list[:class:`huaweicloudsdkhss.v5.AppWhitelistEventDetailResInfo`]
        :param resource_info: 
        :type resource_info: :class:`huaweicloudsdkhss.v5.ProcessEventResourceResponseInfo`
        :param recommendation: **参数解释**: 处置建议 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 
        :type recommendation: str
        :param process_info: **参数解释**: 偏移量：进程信息列表 **约束限制**: 不涉及 
        :type process_info: list[:class:`huaweicloudsdkhss.v5.EventProcessResInfo`]
        :param policy_id: 策略ID
        :type policy_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 
        :type os_type: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param host_status: 服务器状态
        :type host_status: str
        :param agent_status: Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。
        :type agent_status: str
        :param protect_status: 防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。
        :type protect_status: str
        """
        
        

        self._event_id = None
        self._event_class_id = None
        self._event_type = None
        self._event_name = None
        self._severity = None
        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._public_ip = None
        self._attack_phase = None
        self._attack_tag = None
        self._occur_time = None
        self._handle_time = None
        self._handle_status = None
        self._handle_method = None
        self._operate_accept_list = None
        self._operate_detail_list = None
        self._resource_info = None
        self._recommendation = None
        self._process_info = None
        self._policy_id = None
        self._policy_name = None
        self._os_type = None
        self._asset_value = None
        self._host_status = None
        self._agent_status = None
        self._protect_status = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if event_class_id is not None:
            self.event_class_id = event_class_id
        if event_type is not None:
            self.event_type = event_type
        if event_name is not None:
            self.event_name = event_name
        if severity is not None:
            self.severity = severity
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if attack_phase is not None:
            self.attack_phase = attack_phase
        if attack_tag is not None:
            self.attack_tag = attack_tag
        if occur_time is not None:
            self.occur_time = occur_time
        if handle_time is not None:
            self.handle_time = handle_time
        if handle_status is not None:
            self.handle_status = handle_status
        if handle_method is not None:
            self.handle_method = handle_method
        if operate_accept_list is not None:
            self.operate_accept_list = operate_accept_list
        if operate_detail_list is not None:
            self.operate_detail_list = operate_detail_list
        if resource_info is not None:
            self.resource_info = resource_info
        if recommendation is not None:
            self.recommendation = recommendation
        if process_info is not None:
            self.process_info = process_info
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if os_type is not None:
            self.os_type = os_type
        if asset_value is not None:
            self.asset_value = asset_value
        if host_status is not None:
            self.host_status = host_status
        if agent_status is not None:
            self.agent_status = agent_status
        if protect_status is not None:
            self.protect_status = protect_status

    @property
    def event_id(self):
        r"""Gets the event_id of this AppWhitelistEventResponseInfo.

        **参数解释**： 事件ID **取值范围**： 字符长度1-64位 

        :return: The event_id of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this AppWhitelistEventResponseInfo.

        **参数解释**： 事件ID **取值范围**： 字符长度1-64位 

        :param event_id: The event_id of this AppWhitelistEventResponseInfo.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_class_id(self):
        r"""Gets the event_class_id of this AppWhitelistEventResponseInfo.

        **参数解释**： 事件分类 **取值范围**：   - container_1001：容器命名空间   - container_1002：容器开放端口   - container_1003：容器安全选项   - container_1004：容器挂载目录   - containerescape_0001：容器高危系统调用   - containerescape_0002：Shocker攻击   - containerescape_0003：DirtCow攻击   - containerescape_0004：容器文件逃逸攻击   - dockerfile_001：用户自定义容器保护文件被修改   - dockerfile_002：容器文件系统可执行文件被修改   - dockerproc_001：容器进程异常事件上报   - fileprotect_0001：文件提权   - fileprotect_0002：关键文件变更   - fileprotect_0003：关键文件路径变更   - fileprotect_0004：文件/目录变更   - av_1002：病毒   - av_1003：蠕虫   - av_1004：木马   - av_1005：僵尸网络   - av_1006：后门   - av_1007：间谍软件   - av_1008：恶意广告软件   - av_1009：钓鱼   - av_1010：Rootkit   - av_1011：勒索软件   - av_1012：黑客工具   - av_1013：灰色软件   - av_1015：Webshell   - av_1016：挖矿软件   - login_0001：尝试暴力破解   - login_0002：爆破成功   - login_1001：登录成功   - login_1002：异地登录   - login_1003：弱口令   - malware_0001：shell变更事件上报   - malware_0002：反弹shell事件上报   - malware_1001：恶意程序   - procdet_0001：进程异常行为检测   - procdet_0002：进程提权   - procreport_0001：危险命令   - user_1001：账号变更   - user_1002：风险账号   - vmescape_0001：虚拟机敏感命令执行   - vmescape_0002：虚拟化进程访问敏感文件   - vmescape_0003：虚拟机异常端口访问   - webshell_0001：网站后门   - network_1001：恶意挖矿   - network_1002：对外DDoS攻击   - network_1003：恶意扫描   - network_1004：敏感区域攻击   - ransomware_0001：勒索攻击   - ransomware_0002：勒索攻击   - ransomware_0003：勒索攻击   - fileless_0001：进程注入   - fileless_0002：动态库注入进程   - fileless_0003：关键配置变更   - fileless_0004：环境变量变更   - fileless_0005：内存文件进程   - fileless_0006：vdso劫持   - crontab_1001：Crontab可疑任务   - vul_exploit_0001：Redis漏洞利用攻击   - vul_exploit_0002：Hadoop漏洞利用攻击   - vul_exploit_0003：MySQL漏洞利用攻击   - rootkit_0001：可疑rootkit文件   - rootkit_0002：可疑内核模块   - RASP_0004：上传Webshell   - RASP_0018：无文件Webshell   - blockexec_001：已知勒索攻击   - hips_0001：Windows Defender防护被禁用   - hips_0002：可疑的黑客工具   - hips_0003：可疑的勒索加密行为   - hips_0004：隐藏账号创建   - hips_0005：读取用户密码凭据   - hips_0006：可疑的SAM文件导出   - hips_0007：可疑shadow copy删除操作   - hips_0008：备份文件删除   - hips_0009：可疑勒索病毒操作注册表   - hips_0010：可疑的异常进程行为   - hips_0011：可疑的扫描探测   - hips_0012：可疑的勒索病毒脚本运行   - hips_0013：可疑的挖矿命令执行   - hips_0014：可疑的禁用windows安全中心   - hips_0015：可疑的停止防火墙服务行为   - hips_0016：可疑的系统自动恢复禁用   - hips_0017：Offies创建可执行文件   - hips_0018：带宏Offies文件异常创建   - hips_0019：可疑的注册表操作   - hips_0020：Confluence远程代码执行   - hips_0021：MSDT远程代码执行   - portscan_0001：通用端口扫描   - portscan_0002：秘密端口扫描   - k8s_1001：Kubernetes事件删除   - k8s_1002：创建特权Pod   - k8s_1003：Pod中使用交互式shell   - k8s_1004：创建敏感目录Pod   - k8s_1005：创建主机网络的Pod   - k8s_1006：创建主机Pid空间的Pod   - k8s_1007：普通pod访问APIserver认证失败   - k8s_1008：普通Pod通过Curl访问APIServer   - k8s_1009：系统管理空间执行exec   - k8s_1010：系统管理空间创建Pod   - k8s_1011：创建静态Pod   - k8s_1012：创建DaemonSet   - k8s_1013：创建集群计划任务   - k8s_1014：Secrets操作   - k8s_1015：枚举用户可执行的操作   - k8s_1016：高权限RoleBinding或ClusterRoleBinding   - k8s_1017：ServiceAccount创建   - k8s_1018：创建Cronjob   - k8s_1019：Pod中exec使用交互式shell   - k8s_1020：无权限访问Apiserver   - k8s_1021：使用curl访问APIServer   - k8s_1022：Ingress漏洞   - k8s_1023：中间人攻击   - k8s_1024：蠕虫挖矿木马   - k8s_1025：K8s事件删除   - k8s_1026：SelfSubjectRulesReview场景   - imgblock_0001：镜像白名单阻断   - imgblock_0002：镜像黑名单阻断   - imgblock_0003：镜像标签白名单阻断   - imgblock_0004：镜像标签黑名单阻断   - imgblock_0005：创建容器白名单阻断   - imgblock_0006：创建容器黑名单阻断   - imgblock_0007：容器mount proc阻断   - imgblock_0008：容器seccomp unconfined阻断   - imgblock_0009：容器特权阻断   - imgblock_0010：容器capabilities阻断 

        :return: The event_class_id of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._event_class_id

    @event_class_id.setter
    def event_class_id(self, event_class_id):
        r"""Sets the event_class_id of this AppWhitelistEventResponseInfo.

        **参数解释**： 事件分类 **取值范围**：   - container_1001：容器命名空间   - container_1002：容器开放端口   - container_1003：容器安全选项   - container_1004：容器挂载目录   - containerescape_0001：容器高危系统调用   - containerescape_0002：Shocker攻击   - containerescape_0003：DirtCow攻击   - containerescape_0004：容器文件逃逸攻击   - dockerfile_001：用户自定义容器保护文件被修改   - dockerfile_002：容器文件系统可执行文件被修改   - dockerproc_001：容器进程异常事件上报   - fileprotect_0001：文件提权   - fileprotect_0002：关键文件变更   - fileprotect_0003：关键文件路径变更   - fileprotect_0004：文件/目录变更   - av_1002：病毒   - av_1003：蠕虫   - av_1004：木马   - av_1005：僵尸网络   - av_1006：后门   - av_1007：间谍软件   - av_1008：恶意广告软件   - av_1009：钓鱼   - av_1010：Rootkit   - av_1011：勒索软件   - av_1012：黑客工具   - av_1013：灰色软件   - av_1015：Webshell   - av_1016：挖矿软件   - login_0001：尝试暴力破解   - login_0002：爆破成功   - login_1001：登录成功   - login_1002：异地登录   - login_1003：弱口令   - malware_0001：shell变更事件上报   - malware_0002：反弹shell事件上报   - malware_1001：恶意程序   - procdet_0001：进程异常行为检测   - procdet_0002：进程提权   - procreport_0001：危险命令   - user_1001：账号变更   - user_1002：风险账号   - vmescape_0001：虚拟机敏感命令执行   - vmescape_0002：虚拟化进程访问敏感文件   - vmescape_0003：虚拟机异常端口访问   - webshell_0001：网站后门   - network_1001：恶意挖矿   - network_1002：对外DDoS攻击   - network_1003：恶意扫描   - network_1004：敏感区域攻击   - ransomware_0001：勒索攻击   - ransomware_0002：勒索攻击   - ransomware_0003：勒索攻击   - fileless_0001：进程注入   - fileless_0002：动态库注入进程   - fileless_0003：关键配置变更   - fileless_0004：环境变量变更   - fileless_0005：内存文件进程   - fileless_0006：vdso劫持   - crontab_1001：Crontab可疑任务   - vul_exploit_0001：Redis漏洞利用攻击   - vul_exploit_0002：Hadoop漏洞利用攻击   - vul_exploit_0003：MySQL漏洞利用攻击   - rootkit_0001：可疑rootkit文件   - rootkit_0002：可疑内核模块   - RASP_0004：上传Webshell   - RASP_0018：无文件Webshell   - blockexec_001：已知勒索攻击   - hips_0001：Windows Defender防护被禁用   - hips_0002：可疑的黑客工具   - hips_0003：可疑的勒索加密行为   - hips_0004：隐藏账号创建   - hips_0005：读取用户密码凭据   - hips_0006：可疑的SAM文件导出   - hips_0007：可疑shadow copy删除操作   - hips_0008：备份文件删除   - hips_0009：可疑勒索病毒操作注册表   - hips_0010：可疑的异常进程行为   - hips_0011：可疑的扫描探测   - hips_0012：可疑的勒索病毒脚本运行   - hips_0013：可疑的挖矿命令执行   - hips_0014：可疑的禁用windows安全中心   - hips_0015：可疑的停止防火墙服务行为   - hips_0016：可疑的系统自动恢复禁用   - hips_0017：Offies创建可执行文件   - hips_0018：带宏Offies文件异常创建   - hips_0019：可疑的注册表操作   - hips_0020：Confluence远程代码执行   - hips_0021：MSDT远程代码执行   - portscan_0001：通用端口扫描   - portscan_0002：秘密端口扫描   - k8s_1001：Kubernetes事件删除   - k8s_1002：创建特权Pod   - k8s_1003：Pod中使用交互式shell   - k8s_1004：创建敏感目录Pod   - k8s_1005：创建主机网络的Pod   - k8s_1006：创建主机Pid空间的Pod   - k8s_1007：普通pod访问APIserver认证失败   - k8s_1008：普通Pod通过Curl访问APIServer   - k8s_1009：系统管理空间执行exec   - k8s_1010：系统管理空间创建Pod   - k8s_1011：创建静态Pod   - k8s_1012：创建DaemonSet   - k8s_1013：创建集群计划任务   - k8s_1014：Secrets操作   - k8s_1015：枚举用户可执行的操作   - k8s_1016：高权限RoleBinding或ClusterRoleBinding   - k8s_1017：ServiceAccount创建   - k8s_1018：创建Cronjob   - k8s_1019：Pod中exec使用交互式shell   - k8s_1020：无权限访问Apiserver   - k8s_1021：使用curl访问APIServer   - k8s_1022：Ingress漏洞   - k8s_1023：中间人攻击   - k8s_1024：蠕虫挖矿木马   - k8s_1025：K8s事件删除   - k8s_1026：SelfSubjectRulesReview场景   - imgblock_0001：镜像白名单阻断   - imgblock_0002：镜像黑名单阻断   - imgblock_0003：镜像标签白名单阻断   - imgblock_0004：镜像标签黑名单阻断   - imgblock_0005：创建容器白名单阻断   - imgblock_0006：创建容器黑名单阻断   - imgblock_0007：容器mount proc阻断   - imgblock_0008：容器seccomp unconfined阻断   - imgblock_0009：容器特权阻断   - imgblock_0010：容器capabilities阻断 

        :param event_class_id: The event_class_id of this AppWhitelistEventResponseInfo.
        :type event_class_id: str
        """
        self._event_class_id = event_class_id

    @property
    def event_type(self):
        r"""Gets the event_type of this AppWhitelistEventResponseInfo.

        事件类型，包含如下:   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色

        :return: The event_type of this AppWhitelistEventResponseInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this AppWhitelistEventResponseInfo.

        事件类型，包含如下:   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色

        :param event_type: The event_type of this AppWhitelistEventResponseInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def event_name(self):
        r"""Gets the event_name of this AppWhitelistEventResponseInfo.

        事件名称   - \"white list alert malicious process\"   - \"white list alert suspicious process\"

        :return: The event_name of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this AppWhitelistEventResponseInfo.

        事件名称   - \"white list alert malicious process\"   - \"white list alert suspicious process\"

        :param event_name: The event_name of this AppWhitelistEventResponseInfo.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def severity(self):
        r"""Gets the severity of this AppWhitelistEventResponseInfo.

        **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 

        :return: The severity of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this AppWhitelistEventResponseInfo.

        **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 

        :param severity: The severity of this AppWhitelistEventResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def host_name(self):
        r"""Gets the host_name of this AppWhitelistEventResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this AppWhitelistEventResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this AppWhitelistEventResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this AppWhitelistEventResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this AppWhitelistEventResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this AppWhitelistEventResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this AppWhitelistEventResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this AppWhitelistEventResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this AppWhitelistEventResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this AppWhitelistEventResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this AppWhitelistEventResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this AppWhitelistEventResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def attack_phase(self):
        r"""Gets the attack_phase of this AppWhitelistEventResponseInfo.

        **参数解释**： 攻击阶段 **取值范围**： - reconnaissance：侦查跟踪 - weaponization：武器构建 - delivery：载荷投递 - exploit：漏洞利用 - installation：安装植入 - command_and_control：命令与控制 - actions：目标达成 

        :return: The attack_phase of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._attack_phase

    @attack_phase.setter
    def attack_phase(self, attack_phase):
        r"""Sets the attack_phase of this AppWhitelistEventResponseInfo.

        **参数解释**： 攻击阶段 **取值范围**： - reconnaissance：侦查跟踪 - weaponization：武器构建 - delivery：载荷投递 - exploit：漏洞利用 - installation：安装植入 - command_and_control：命令与控制 - actions：目标达成 

        :param attack_phase: The attack_phase of this AppWhitelistEventResponseInfo.
        :type attack_phase: str
        """
        self._attack_phase = attack_phase

    @property
    def attack_tag(self):
        r"""Gets the attack_tag of this AppWhitelistEventResponseInfo.

        **参数解释**： 攻击标识 **取值范围**： - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性 

        :return: The attack_tag of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._attack_tag

    @attack_tag.setter
    def attack_tag(self, attack_tag):
        r"""Sets the attack_tag of this AppWhitelistEventResponseInfo.

        **参数解释**： 攻击标识 **取值范围**： - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性 

        :param attack_tag: The attack_tag of this AppWhitelistEventResponseInfo.
        :type attack_tag: str
        """
        self._attack_tag = attack_tag

    @property
    def occur_time(self):
        r"""Gets the occur_time of this AppWhitelistEventResponseInfo.

        **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The occur_time of this AppWhitelistEventResponseInfo.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        r"""Sets the occur_time of this AppWhitelistEventResponseInfo.

        **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 

        :param occur_time: The occur_time of this AppWhitelistEventResponseInfo.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def handle_time(self):
        r"""Gets the handle_time of this AppWhitelistEventResponseInfo.

        **参数解释**： 处置时间，毫秒，已处理的告警才有 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The handle_time of this AppWhitelistEventResponseInfo.
        :rtype: int
        """
        return self._handle_time

    @handle_time.setter
    def handle_time(self, handle_time):
        r"""Sets the handle_time of this AppWhitelistEventResponseInfo.

        **参数解释**： 处置时间，毫秒，已处理的告警才有 **取值范围**： 最小值0，最大值9223372036854775807 

        :param handle_time: The handle_time of this AppWhitelistEventResponseInfo.
        :type handle_time: int
        """
        self._handle_time = handle_time

    @property
    def handle_status(self):
        r"""Gets the handle_status of this AppWhitelistEventResponseInfo.

        **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 

        :return: The handle_status of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this AppWhitelistEventResponseInfo.

        **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 

        :param handle_status: The handle_status of this AppWhitelistEventResponseInfo.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def handle_method(self):
        r"""Gets the handle_method of this AppWhitelistEventResponseInfo.

        **参数解释**： 处理状态 **约束限制**: 不涉及 **取值范围**: - mark_as_trust：标记为可信 - mark_as_suspicious：标记为可疑 - isolate_and_kill：隔离查杀  **默认取值**: 不涉及 

        :return: The handle_method of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._handle_method

    @handle_method.setter
    def handle_method(self, handle_method):
        r"""Sets the handle_method of this AppWhitelistEventResponseInfo.

        **参数解释**： 处理状态 **约束限制**: 不涉及 **取值范围**: - mark_as_trust：标记为可信 - mark_as_suspicious：标记为可疑 - isolate_and_kill：隔离查杀  **默认取值**: 不涉及 

        :param handle_method: The handle_method of this AppWhitelistEventResponseInfo.
        :type handle_method: str
        """
        self._handle_method = handle_method

    @property
    def operate_accept_list(self):
        r"""Gets the operate_accept_list of this AppWhitelistEventResponseInfo.

        **参数解释**: 支持的处理操作 **约束限制**: 不涉及 

        :return: The operate_accept_list of this AppWhitelistEventResponseInfo.
        :rtype: list[str]
        """
        return self._operate_accept_list

    @operate_accept_list.setter
    def operate_accept_list(self, operate_accept_list):
        r"""Sets the operate_accept_list of this AppWhitelistEventResponseInfo.

        **参数解释**: 支持的处理操作 **约束限制**: 不涉及 

        :param operate_accept_list: The operate_accept_list of this AppWhitelistEventResponseInfo.
        :type operate_accept_list: list[str]
        """
        self._operate_accept_list = operate_accept_list

    @property
    def operate_detail_list(self):
        r"""Gets the operate_detail_list of this AppWhitelistEventResponseInfo.

        操作详情信息列表（页面不展示）

        :return: The operate_detail_list of this AppWhitelistEventResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AppWhitelistEventDetailResInfo`]
        """
        return self._operate_detail_list

    @operate_detail_list.setter
    def operate_detail_list(self, operate_detail_list):
        r"""Sets the operate_detail_list of this AppWhitelistEventResponseInfo.

        操作详情信息列表（页面不展示）

        :param operate_detail_list: The operate_detail_list of this AppWhitelistEventResponseInfo.
        :type operate_detail_list: list[:class:`huaweicloudsdkhss.v5.AppWhitelistEventDetailResInfo`]
        """
        self._operate_detail_list = operate_detail_list

    @property
    def resource_info(self):
        r"""Gets the resource_info of this AppWhitelistEventResponseInfo.

        :return: The resource_info of this AppWhitelistEventResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ProcessEventResourceResponseInfo`
        """
        return self._resource_info

    @resource_info.setter
    def resource_info(self, resource_info):
        r"""Sets the resource_info of this AppWhitelistEventResponseInfo.

        :param resource_info: The resource_info of this AppWhitelistEventResponseInfo.
        :type resource_info: :class:`huaweicloudsdkhss.v5.ProcessEventResourceResponseInfo`
        """
        self._resource_info = resource_info

    @property
    def recommendation(self):
        r"""Gets the recommendation of this AppWhitelistEventResponseInfo.

        **参数解释**: 处置建议 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 

        :return: The recommendation of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        r"""Sets the recommendation of this AppWhitelistEventResponseInfo.

        **参数解释**: 处置建议 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 

        :param recommendation: The recommendation of this AppWhitelistEventResponseInfo.
        :type recommendation: str
        """
        self._recommendation = recommendation

    @property
    def process_info(self):
        r"""Gets the process_info of this AppWhitelistEventResponseInfo.

        **参数解释**: 偏移量：进程信息列表 **约束限制**: 不涉及 

        :return: The process_info of this AppWhitelistEventResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.EventProcessResInfo`]
        """
        return self._process_info

    @process_info.setter
    def process_info(self, process_info):
        r"""Sets the process_info of this AppWhitelistEventResponseInfo.

        **参数解释**: 偏移量：进程信息列表 **约束限制**: 不涉及 

        :param process_info: The process_info of this AppWhitelistEventResponseInfo.
        :type process_info: list[:class:`huaweicloudsdkhss.v5.EventProcessResInfo`]
        """
        self._process_info = process_info

    @property
    def policy_id(self):
        r"""Gets the policy_id of this AppWhitelistEventResponseInfo.

        策略ID

        :return: The policy_id of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this AppWhitelistEventResponseInfo.

        策略ID

        :param policy_id: The policy_id of this AppWhitelistEventResponseInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AppWhitelistEventResponseInfo.

        策略名称

        :return: The policy_name of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AppWhitelistEventResponseInfo.

        策略名称

        :param policy_name: The policy_name of this AppWhitelistEventResponseInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def os_type(self):
        r"""Gets the os_type of this AppWhitelistEventResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :return: The os_type of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this AppWhitelistEventResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :param os_type: The os_type of this AppWhitelistEventResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def asset_value(self):
        r"""Gets the asset_value of this AppWhitelistEventResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this AppWhitelistEventResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this AppWhitelistEventResponseInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def host_status(self):
        r"""Gets the host_status of this AppWhitelistEventResponseInfo.

        服务器状态

        :return: The host_status of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this AppWhitelistEventResponseInfo.

        服务器状态

        :param host_status: The host_status of this AppWhitelistEventResponseInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this AppWhitelistEventResponseInfo.

        Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。

        :return: The agent_status of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this AppWhitelistEventResponseInfo.

        Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。

        :param agent_status: The agent_status of this AppWhitelistEventResponseInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def protect_status(self):
        r"""Gets the protect_status of this AppWhitelistEventResponseInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :return: The protect_status of this AppWhitelistEventResponseInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this AppWhitelistEventResponseInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :param protect_status: The protect_status of this AppWhitelistEventResponseInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

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
        if not isinstance(other, AppWhitelistEventResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
