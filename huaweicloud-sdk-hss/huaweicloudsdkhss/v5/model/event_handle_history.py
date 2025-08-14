# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventHandleHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_type': 'int',
        'host_name': 'str',
        'event_abstract': 'str',
        'attack_tag': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'asset_value': 'str',
        'occur_time': 'int',
        'handle_status': 'str',
        'notes': 'str',
        'event_class_id': 'str',
        'event_name': 'str',
        'handle_time': 'int',
        'operate_type': 'str',
        'severity': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'event_type': 'event_type',
        'host_name': 'host_name',
        'event_abstract': 'event_abstract',
        'attack_tag': 'attack_tag',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'asset_value': 'asset_value',
        'occur_time': 'occur_time',
        'handle_status': 'handle_status',
        'notes': 'notes',
        'event_class_id': 'event_class_id',
        'event_name': 'event_name',
        'handle_time': 'handle_time',
        'operate_type': 'operate_type',
        'severity': 'severity',
        'user_name': 'user_name'
    }

    def __init__(self, event_type=None, host_name=None, event_abstract=None, attack_tag=None, private_ip=None, public_ip=None, asset_value=None, occur_time=None, handle_status=None, notes=None, event_class_id=None, event_name=None, handle_time=None, operate_type=None, severity=None, user_name=None):
        r"""EventHandleHistory

        The model defined in huaweicloud sdk

        :param event_type: 事件类型
        :type event_type: int
        :param host_name: 主机名称
        :type host_name: str
        :param event_abstract: 事件摘要
        :type event_abstract: str
        :param attack_tag: 攻击标识，包含如下： - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性
        :type attack_tag: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param asset_value: 资产重要性，包含如下:   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param occur_time: **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 
        :type occur_time: int
        :param handle_status: **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 
        :type handle_status: str
        :param notes: 备注
        :type notes: str
        :param event_class_id: **参数解释**： 事件分类 **取值范围**：   - container_1001：容器命名空间   - container_1002：容器开放端口   - container_1003：容器安全选项   - container_1004：容器挂载目录   - containerescape_0001：容器高危系统调用   - containerescape_0002：Shocker攻击   - containerescape_0003：DirtCow攻击   - containerescape_0004：容器文件逃逸攻击   - dockerfile_001：用户自定义容器保护文件被修改   - dockerfile_002：容器文件系统可执行文件被修改   - dockerproc_001：容器进程异常事件上报   - fileprotect_0001：文件提权   - fileprotect_0002：关键文件变更   - fileprotect_0003：关键文件路径变更   - fileprotect_0004：文件/目录变更   - av_1002：病毒   - av_1003：蠕虫   - av_1004：木马   - av_1005：僵尸网络   - av_1006：后门   - av_1007：间谍软件   - av_1008：恶意广告软件   - av_1009：钓鱼   - av_1010：Rootkit   - av_1011：勒索软件   - av_1012：黑客工具   - av_1013：灰色软件   - av_1015：Webshell   - av_1016：挖矿软件   - login_0001：尝试暴力破解   - login_0002：爆破成功   - login_1001：登录成功   - login_1002：异地登录   - login_1003：弱口令   - malware_0001：shell变更事件上报   - malware_0002：反弹shell事件上报   - malware_1001：恶意程序   - procdet_0001：进程异常行为检测   - procdet_0002：进程提权   - procreport_0001：危险命令   - user_1001：账号变更   - user_1002：风险账号   - vmescape_0001：虚拟机敏感命令执行   - vmescape_0002：虚拟化进程访问敏感文件   - vmescape_0003：虚拟机异常端口访问   - webshell_0001：网站后门   - network_1001：恶意挖矿   - network_1002：对外DDoS攻击   - network_1003：恶意扫描   - network_1004：敏感区域攻击   - ransomware_0001：勒索攻击   - ransomware_0002：勒索攻击   - ransomware_0003：勒索攻击   - fileless_0001：进程注入   - fileless_0002：动态库注入进程   - fileless_0003：关键配置变更   - fileless_0004：环境变量变更   - fileless_0005：内存文件进程   - fileless_0006：vdso劫持   - crontab_1001：Crontab可疑任务   - vul_exploit_0001：Redis漏洞利用攻击   - vul_exploit_0002：Hadoop漏洞利用攻击   - vul_exploit_0003：MySQL漏洞利用攻击   - rootkit_0001：可疑rootkit文件   - rootkit_0002：可疑内核模块   - RASP_0004：上传Webshell   - RASP_0018：无文件Webshell   - blockexec_001：已知勒索攻击   - hips_0001：Windows Defender防护被禁用   - hips_0002：可疑的黑客工具   - hips_0003：可疑的勒索加密行为   - hips_0004：隐藏账号创建   - hips_0005：读取用户密码凭据   - hips_0006：可疑的SAM文件导出   - hips_0007：可疑shadow copy删除操作   - hips_0008：备份文件删除   - hips_0009：可疑勒索病毒操作注册表   - hips_0010：可疑的异常进程行为   - hips_0011：可疑的扫描探测   - hips_0012：可疑的勒索病毒脚本运行   - hips_0013：可疑的挖矿命令执行   - hips_0014：可疑的禁用windows安全中心   - hips_0015：可疑的停止防火墙服务行为   - hips_0016：可疑的系统自动恢复禁用   - hips_0017：Offies创建可执行文件   - hips_0018：带宏Offies文件异常创建   - hips_0019：可疑的注册表操作   - hips_0020：Confluence远程代码执行   - hips_0021：MSDT远程代码执行   - portscan_0001：通用端口扫描   - portscan_0002：秘密端口扫描   - k8s_1001：Kubernetes事件删除   - k8s_1002：创建特权Pod   - k8s_1003：Pod中使用交互式shell   - k8s_1004：创建敏感目录Pod   - k8s_1005：创建主机网络的Pod   - k8s_1006：创建主机Pid空间的Pod   - k8s_1007：普通pod访问APIserver认证失败   - k8s_1008：普通Pod通过Curl访问APIServer   - k8s_1009：系统管理空间执行exec   - k8s_1010：系统管理空间创建Pod   - k8s_1011：创建静态Pod   - k8s_1012：创建DaemonSet   - k8s_1013：创建集群计划任务   - k8s_1014：Secrets操作   - k8s_1015：枚举用户可执行的操作   - k8s_1016：高权限RoleBinding或ClusterRoleBinding   - k8s_1017：ServiceAccount创建   - k8s_1018：创建Cronjob   - k8s_1019：Pod中exec使用交互式shell   - k8s_1020：无权限访问Apiserver   - k8s_1021：使用curl访问APIServer   - k8s_1022：Ingress漏洞   - k8s_1023：中间人攻击   - k8s_1024：蠕虫挖矿木马   - k8s_1025：K8s事件删除   - k8s_1026：SelfSubjectRulesReview场景   - imgblock_0001：镜像白名单阻断   - imgblock_0002：镜像黑名单阻断   - imgblock_0003：镜像标签白名单阻断   - imgblock_0004：镜像标签黑名单阻断   - imgblock_0005：创建容器白名单阻断   - imgblock_0006：创建容器黑名单阻断   - imgblock_0007：容器mount proc阻断   - imgblock_0008：容器seccomp unconfined阻断   - imgblock_0009：容器特权阻断   - imgblock_0010：容器capabilities阻断 
        :type event_class_id: str
        :param event_name: 事件名称
        :type event_name: str
        :param handle_time: **参数解释**： 处置时间，毫秒，已处理的告警才有 **取值范围**： 最小值0，最大值9223372036854775807 
        :type handle_time: int
        :param operate_type: **参数解释**： 处理方式 **取值范围**： - mark_as_handled：手动处理 - ignore：忽略 - add_to_alarm_whitelist：加入告警白名单 - add_to_login_whitelist：加入登录白名单 - isolate_and_kill：隔离查杀 - unhandle：取消手动处理 - do_not_ignore：取消忽略 - remove_from_alarm_whitelist：删除告警白名单 - remove_from_login_whitelist：删除登录白名单 - do_not_isolate_or_kill：取消隔离查杀 
        :type operate_type: str
        :param severity: **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 
        :type severity: str
        :param user_name: 用户名
        :type user_name: str
        """
        
        

        self._event_type = None
        self._host_name = None
        self._event_abstract = None
        self._attack_tag = None
        self._private_ip = None
        self._public_ip = None
        self._asset_value = None
        self._occur_time = None
        self._handle_status = None
        self._notes = None
        self._event_class_id = None
        self._event_name = None
        self._handle_time = None
        self._operate_type = None
        self._severity = None
        self._user_name = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if host_name is not None:
            self.host_name = host_name
        if event_abstract is not None:
            self.event_abstract = event_abstract
        if attack_tag is not None:
            self.attack_tag = attack_tag
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if asset_value is not None:
            self.asset_value = asset_value
        if occur_time is not None:
            self.occur_time = occur_time
        if handle_status is not None:
            self.handle_status = handle_status
        if notes is not None:
            self.notes = notes
        if event_class_id is not None:
            self.event_class_id = event_class_id
        if event_name is not None:
            self.event_name = event_name
        if handle_time is not None:
            self.handle_time = handle_time
        if operate_type is not None:
            self.operate_type = operate_type
        if severity is not None:
            self.severity = severity
        if user_name is not None:
            self.user_name = user_name

    @property
    def event_type(self):
        r"""Gets the event_type of this EventHandleHistory.

        事件类型

        :return: The event_type of this EventHandleHistory.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this EventHandleHistory.

        事件类型

        :param event_type: The event_type of this EventHandleHistory.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def host_name(self):
        r"""Gets the host_name of this EventHandleHistory.

        主机名称

        :return: The host_name of this EventHandleHistory.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this EventHandleHistory.

        主机名称

        :param host_name: The host_name of this EventHandleHistory.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def event_abstract(self):
        r"""Gets the event_abstract of this EventHandleHistory.

        事件摘要

        :return: The event_abstract of this EventHandleHistory.
        :rtype: str
        """
        return self._event_abstract

    @event_abstract.setter
    def event_abstract(self, event_abstract):
        r"""Sets the event_abstract of this EventHandleHistory.

        事件摘要

        :param event_abstract: The event_abstract of this EventHandleHistory.
        :type event_abstract: str
        """
        self._event_abstract = event_abstract

    @property
    def attack_tag(self):
        r"""Gets the attack_tag of this EventHandleHistory.

        攻击标识，包含如下： - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性

        :return: The attack_tag of this EventHandleHistory.
        :rtype: str
        """
        return self._attack_tag

    @attack_tag.setter
    def attack_tag(self, attack_tag):
        r"""Sets the attack_tag of this EventHandleHistory.

        攻击标识，包含如下： - attack_success：攻击成功 - attack_attempt：攻击尝试 - attack_blocked：攻击被阻断 - abnormal_behavior：异常行为 - collapsible_host：主机失陷 - system_vulnerability：系统脆弱性

        :param attack_tag: The attack_tag of this EventHandleHistory.
        :type attack_tag: str
        """
        self._attack_tag = attack_tag

    @property
    def private_ip(self):
        r"""Gets the private_ip of this EventHandleHistory.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this EventHandleHistory.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this EventHandleHistory.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this EventHandleHistory.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this EventHandleHistory.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this EventHandleHistory.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this EventHandleHistory.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this EventHandleHistory.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def asset_value(self):
        r"""Gets the asset_value of this EventHandleHistory.

        资产重要性，包含如下:   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this EventHandleHistory.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this EventHandleHistory.

        资产重要性，包含如下:   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this EventHandleHistory.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def occur_time(self):
        r"""Gets the occur_time of this EventHandleHistory.

        **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The occur_time of this EventHandleHistory.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        r"""Sets the occur_time of this EventHandleHistory.

        **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 

        :param occur_time: The occur_time of this EventHandleHistory.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def handle_status(self):
        r"""Gets the handle_status of this EventHandleHistory.

        **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 

        :return: The handle_status of this EventHandleHistory.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this EventHandleHistory.

        **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 

        :param handle_status: The handle_status of this EventHandleHistory.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def notes(self):
        r"""Gets the notes of this EventHandleHistory.

        备注

        :return: The notes of this EventHandleHistory.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        r"""Sets the notes of this EventHandleHistory.

        备注

        :param notes: The notes of this EventHandleHistory.
        :type notes: str
        """
        self._notes = notes

    @property
    def event_class_id(self):
        r"""Gets the event_class_id of this EventHandleHistory.

        **参数解释**： 事件分类 **取值范围**：   - container_1001：容器命名空间   - container_1002：容器开放端口   - container_1003：容器安全选项   - container_1004：容器挂载目录   - containerescape_0001：容器高危系统调用   - containerescape_0002：Shocker攻击   - containerescape_0003：DirtCow攻击   - containerescape_0004：容器文件逃逸攻击   - dockerfile_001：用户自定义容器保护文件被修改   - dockerfile_002：容器文件系统可执行文件被修改   - dockerproc_001：容器进程异常事件上报   - fileprotect_0001：文件提权   - fileprotect_0002：关键文件变更   - fileprotect_0003：关键文件路径变更   - fileprotect_0004：文件/目录变更   - av_1002：病毒   - av_1003：蠕虫   - av_1004：木马   - av_1005：僵尸网络   - av_1006：后门   - av_1007：间谍软件   - av_1008：恶意广告软件   - av_1009：钓鱼   - av_1010：Rootkit   - av_1011：勒索软件   - av_1012：黑客工具   - av_1013：灰色软件   - av_1015：Webshell   - av_1016：挖矿软件   - login_0001：尝试暴力破解   - login_0002：爆破成功   - login_1001：登录成功   - login_1002：异地登录   - login_1003：弱口令   - malware_0001：shell变更事件上报   - malware_0002：反弹shell事件上报   - malware_1001：恶意程序   - procdet_0001：进程异常行为检测   - procdet_0002：进程提权   - procreport_0001：危险命令   - user_1001：账号变更   - user_1002：风险账号   - vmescape_0001：虚拟机敏感命令执行   - vmescape_0002：虚拟化进程访问敏感文件   - vmescape_0003：虚拟机异常端口访问   - webshell_0001：网站后门   - network_1001：恶意挖矿   - network_1002：对外DDoS攻击   - network_1003：恶意扫描   - network_1004：敏感区域攻击   - ransomware_0001：勒索攻击   - ransomware_0002：勒索攻击   - ransomware_0003：勒索攻击   - fileless_0001：进程注入   - fileless_0002：动态库注入进程   - fileless_0003：关键配置变更   - fileless_0004：环境变量变更   - fileless_0005：内存文件进程   - fileless_0006：vdso劫持   - crontab_1001：Crontab可疑任务   - vul_exploit_0001：Redis漏洞利用攻击   - vul_exploit_0002：Hadoop漏洞利用攻击   - vul_exploit_0003：MySQL漏洞利用攻击   - rootkit_0001：可疑rootkit文件   - rootkit_0002：可疑内核模块   - RASP_0004：上传Webshell   - RASP_0018：无文件Webshell   - blockexec_001：已知勒索攻击   - hips_0001：Windows Defender防护被禁用   - hips_0002：可疑的黑客工具   - hips_0003：可疑的勒索加密行为   - hips_0004：隐藏账号创建   - hips_0005：读取用户密码凭据   - hips_0006：可疑的SAM文件导出   - hips_0007：可疑shadow copy删除操作   - hips_0008：备份文件删除   - hips_0009：可疑勒索病毒操作注册表   - hips_0010：可疑的异常进程行为   - hips_0011：可疑的扫描探测   - hips_0012：可疑的勒索病毒脚本运行   - hips_0013：可疑的挖矿命令执行   - hips_0014：可疑的禁用windows安全中心   - hips_0015：可疑的停止防火墙服务行为   - hips_0016：可疑的系统自动恢复禁用   - hips_0017：Offies创建可执行文件   - hips_0018：带宏Offies文件异常创建   - hips_0019：可疑的注册表操作   - hips_0020：Confluence远程代码执行   - hips_0021：MSDT远程代码执行   - portscan_0001：通用端口扫描   - portscan_0002：秘密端口扫描   - k8s_1001：Kubernetes事件删除   - k8s_1002：创建特权Pod   - k8s_1003：Pod中使用交互式shell   - k8s_1004：创建敏感目录Pod   - k8s_1005：创建主机网络的Pod   - k8s_1006：创建主机Pid空间的Pod   - k8s_1007：普通pod访问APIserver认证失败   - k8s_1008：普通Pod通过Curl访问APIServer   - k8s_1009：系统管理空间执行exec   - k8s_1010：系统管理空间创建Pod   - k8s_1011：创建静态Pod   - k8s_1012：创建DaemonSet   - k8s_1013：创建集群计划任务   - k8s_1014：Secrets操作   - k8s_1015：枚举用户可执行的操作   - k8s_1016：高权限RoleBinding或ClusterRoleBinding   - k8s_1017：ServiceAccount创建   - k8s_1018：创建Cronjob   - k8s_1019：Pod中exec使用交互式shell   - k8s_1020：无权限访问Apiserver   - k8s_1021：使用curl访问APIServer   - k8s_1022：Ingress漏洞   - k8s_1023：中间人攻击   - k8s_1024：蠕虫挖矿木马   - k8s_1025：K8s事件删除   - k8s_1026：SelfSubjectRulesReview场景   - imgblock_0001：镜像白名单阻断   - imgblock_0002：镜像黑名单阻断   - imgblock_0003：镜像标签白名单阻断   - imgblock_0004：镜像标签黑名单阻断   - imgblock_0005：创建容器白名单阻断   - imgblock_0006：创建容器黑名单阻断   - imgblock_0007：容器mount proc阻断   - imgblock_0008：容器seccomp unconfined阻断   - imgblock_0009：容器特权阻断   - imgblock_0010：容器capabilities阻断 

        :return: The event_class_id of this EventHandleHistory.
        :rtype: str
        """
        return self._event_class_id

    @event_class_id.setter
    def event_class_id(self, event_class_id):
        r"""Sets the event_class_id of this EventHandleHistory.

        **参数解释**： 事件分类 **取值范围**：   - container_1001：容器命名空间   - container_1002：容器开放端口   - container_1003：容器安全选项   - container_1004：容器挂载目录   - containerescape_0001：容器高危系统调用   - containerescape_0002：Shocker攻击   - containerescape_0003：DirtCow攻击   - containerescape_0004：容器文件逃逸攻击   - dockerfile_001：用户自定义容器保护文件被修改   - dockerfile_002：容器文件系统可执行文件被修改   - dockerproc_001：容器进程异常事件上报   - fileprotect_0001：文件提权   - fileprotect_0002：关键文件变更   - fileprotect_0003：关键文件路径变更   - fileprotect_0004：文件/目录变更   - av_1002：病毒   - av_1003：蠕虫   - av_1004：木马   - av_1005：僵尸网络   - av_1006：后门   - av_1007：间谍软件   - av_1008：恶意广告软件   - av_1009：钓鱼   - av_1010：Rootkit   - av_1011：勒索软件   - av_1012：黑客工具   - av_1013：灰色软件   - av_1015：Webshell   - av_1016：挖矿软件   - login_0001：尝试暴力破解   - login_0002：爆破成功   - login_1001：登录成功   - login_1002：异地登录   - login_1003：弱口令   - malware_0001：shell变更事件上报   - malware_0002：反弹shell事件上报   - malware_1001：恶意程序   - procdet_0001：进程异常行为检测   - procdet_0002：进程提权   - procreport_0001：危险命令   - user_1001：账号变更   - user_1002：风险账号   - vmescape_0001：虚拟机敏感命令执行   - vmescape_0002：虚拟化进程访问敏感文件   - vmescape_0003：虚拟机异常端口访问   - webshell_0001：网站后门   - network_1001：恶意挖矿   - network_1002：对外DDoS攻击   - network_1003：恶意扫描   - network_1004：敏感区域攻击   - ransomware_0001：勒索攻击   - ransomware_0002：勒索攻击   - ransomware_0003：勒索攻击   - fileless_0001：进程注入   - fileless_0002：动态库注入进程   - fileless_0003：关键配置变更   - fileless_0004：环境变量变更   - fileless_0005：内存文件进程   - fileless_0006：vdso劫持   - crontab_1001：Crontab可疑任务   - vul_exploit_0001：Redis漏洞利用攻击   - vul_exploit_0002：Hadoop漏洞利用攻击   - vul_exploit_0003：MySQL漏洞利用攻击   - rootkit_0001：可疑rootkit文件   - rootkit_0002：可疑内核模块   - RASP_0004：上传Webshell   - RASP_0018：无文件Webshell   - blockexec_001：已知勒索攻击   - hips_0001：Windows Defender防护被禁用   - hips_0002：可疑的黑客工具   - hips_0003：可疑的勒索加密行为   - hips_0004：隐藏账号创建   - hips_0005：读取用户密码凭据   - hips_0006：可疑的SAM文件导出   - hips_0007：可疑shadow copy删除操作   - hips_0008：备份文件删除   - hips_0009：可疑勒索病毒操作注册表   - hips_0010：可疑的异常进程行为   - hips_0011：可疑的扫描探测   - hips_0012：可疑的勒索病毒脚本运行   - hips_0013：可疑的挖矿命令执行   - hips_0014：可疑的禁用windows安全中心   - hips_0015：可疑的停止防火墙服务行为   - hips_0016：可疑的系统自动恢复禁用   - hips_0017：Offies创建可执行文件   - hips_0018：带宏Offies文件异常创建   - hips_0019：可疑的注册表操作   - hips_0020：Confluence远程代码执行   - hips_0021：MSDT远程代码执行   - portscan_0001：通用端口扫描   - portscan_0002：秘密端口扫描   - k8s_1001：Kubernetes事件删除   - k8s_1002：创建特权Pod   - k8s_1003：Pod中使用交互式shell   - k8s_1004：创建敏感目录Pod   - k8s_1005：创建主机网络的Pod   - k8s_1006：创建主机Pid空间的Pod   - k8s_1007：普通pod访问APIserver认证失败   - k8s_1008：普通Pod通过Curl访问APIServer   - k8s_1009：系统管理空间执行exec   - k8s_1010：系统管理空间创建Pod   - k8s_1011：创建静态Pod   - k8s_1012：创建DaemonSet   - k8s_1013：创建集群计划任务   - k8s_1014：Secrets操作   - k8s_1015：枚举用户可执行的操作   - k8s_1016：高权限RoleBinding或ClusterRoleBinding   - k8s_1017：ServiceAccount创建   - k8s_1018：创建Cronjob   - k8s_1019：Pod中exec使用交互式shell   - k8s_1020：无权限访问Apiserver   - k8s_1021：使用curl访问APIServer   - k8s_1022：Ingress漏洞   - k8s_1023：中间人攻击   - k8s_1024：蠕虫挖矿木马   - k8s_1025：K8s事件删除   - k8s_1026：SelfSubjectRulesReview场景   - imgblock_0001：镜像白名单阻断   - imgblock_0002：镜像黑名单阻断   - imgblock_0003：镜像标签白名单阻断   - imgblock_0004：镜像标签黑名单阻断   - imgblock_0005：创建容器白名单阻断   - imgblock_0006：创建容器黑名单阻断   - imgblock_0007：容器mount proc阻断   - imgblock_0008：容器seccomp unconfined阻断   - imgblock_0009：容器特权阻断   - imgblock_0010：容器capabilities阻断 

        :param event_class_id: The event_class_id of this EventHandleHistory.
        :type event_class_id: str
        """
        self._event_class_id = event_class_id

    @property
    def event_name(self):
        r"""Gets the event_name of this EventHandleHistory.

        事件名称

        :return: The event_name of this EventHandleHistory.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this EventHandleHistory.

        事件名称

        :param event_name: The event_name of this EventHandleHistory.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def handle_time(self):
        r"""Gets the handle_time of this EventHandleHistory.

        **参数解释**： 处置时间，毫秒，已处理的告警才有 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The handle_time of this EventHandleHistory.
        :rtype: int
        """
        return self._handle_time

    @handle_time.setter
    def handle_time(self, handle_time):
        r"""Sets the handle_time of this EventHandleHistory.

        **参数解释**： 处置时间，毫秒，已处理的告警才有 **取值范围**： 最小值0，最大值9223372036854775807 

        :param handle_time: The handle_time of this EventHandleHistory.
        :type handle_time: int
        """
        self._handle_time = handle_time

    @property
    def operate_type(self):
        r"""Gets the operate_type of this EventHandleHistory.

        **参数解释**： 处理方式 **取值范围**： - mark_as_handled：手动处理 - ignore：忽略 - add_to_alarm_whitelist：加入告警白名单 - add_to_login_whitelist：加入登录白名单 - isolate_and_kill：隔离查杀 - unhandle：取消手动处理 - do_not_ignore：取消忽略 - remove_from_alarm_whitelist：删除告警白名单 - remove_from_login_whitelist：删除登录白名单 - do_not_isolate_or_kill：取消隔离查杀 

        :return: The operate_type of this EventHandleHistory.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this EventHandleHistory.

        **参数解释**： 处理方式 **取值范围**： - mark_as_handled：手动处理 - ignore：忽略 - add_to_alarm_whitelist：加入告警白名单 - add_to_login_whitelist：加入登录白名单 - isolate_and_kill：隔离查杀 - unhandle：取消手动处理 - do_not_ignore：取消忽略 - remove_from_alarm_whitelist：删除告警白名单 - remove_from_login_whitelist：删除登录白名单 - do_not_isolate_or_kill：取消隔离查杀 

        :param operate_type: The operate_type of this EventHandleHistory.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def severity(self):
        r"""Gets the severity of this EventHandleHistory.

        **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 

        :return: The severity of this EventHandleHistory.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this EventHandleHistory.

        **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 

        :param severity: The severity of this EventHandleHistory.
        :type severity: str
        """
        self._severity = severity

    @property
    def user_name(self):
        r"""Gets the user_name of this EventHandleHistory.

        用户名

        :return: The user_name of this EventHandleHistory.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this EventHandleHistory.

        用户名

        :param user_name: The user_name of this EventHandleHistory.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, EventHandleHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
