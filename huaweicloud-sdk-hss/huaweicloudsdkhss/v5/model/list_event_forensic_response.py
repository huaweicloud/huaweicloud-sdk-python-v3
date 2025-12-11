# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventForensicResponse(SdkResponse):

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
        'event_class_id': 'str',
        'support_download_file': 'bool',
        'malware_file_hash': 'str',
        'event_forensic_info': 'EventForensicInfo'
    }

    attribute_map = {
        'event_type': 'event_type',
        'event_class_id': 'event_class_id',
        'support_download_file': 'support_download_file',
        'malware_file_hash': 'malware_file_hash',
        'event_forensic_info': 'event_forensic_info'
    }

    def __init__(self, event_type=None, event_class_id=None, support_download_file=None, malware_file_hash=None, event_forensic_info=None):
        r"""ListEventForensicResponse

        The model defined in huaweicloud sdk

        :param event_type: **参数解释**： 事件类型 **取值范围**： - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012 ：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3027：Crontab可疑任务 - 3029 ：系统安全防护被禁用 - 3030 ：备份删除 - 3031 ：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色 - 11001：高级威胁事件
        :type event_type: int
        :param event_class_id: **参数解释**： 事件分类 **取值范围**： - container_1001：容器命名空间 - container_1002：容器开放端口 - container_1003：容器安全选项 - container_1004：容器挂载目录 - containerescape_0001：容器高危系统调用 - containerescape_0002：Shocker攻击 - containerescape_0003：DirtCow攻击 - containerescape_0004：容器文件逃逸攻击 - dockerfile_001：用户自定义容器保护文件被修改 - dockerfile_002：容器文件系统可执行文件被修改 - dockerproc_001：容器进程异常事件上报 - fileprotect_0001：文件提权 - fileprotect_0002：关键文件变更 - fileprotect_0003：关键文件路径变更 - fileprotect_0004：文件/目录变更 - av_1002：病毒 - av_1003：蠕虫 - av_1004：木马 - av_1005：僵尸网络 - av_1006：后门 - av_1007：间谍软件 - av_1008：恶意广告软件 - av_1009：钓鱼 - av_1010：Rootkit - av_1011：勒索软件 - av_1012：黑客工具 - av_1013：灰色软件 - av_1015：Webshell - av_1016：挖矿软件 - login_0001：尝试暴力破解 - login_0002：爆破成功 - login_1001：登录成功 - login_1002：异地登录 - login_1003：弱口令 - malware_0001：shell变更事件上报 - malware_0002：反弹shell事件上报 - malware_1001：恶意程序 - procdet_0001：进程异常行为检测 - procdet_0002：进程提权 - procreport_0001：危险命令 - user_1001：账号变更 - user_1002：风险账号 - vmescape_0001：虚拟机敏感命令执行 - vmescape_0002：虚拟化进程访问敏感文件 - vmescape_0003：虚拟机异常端口访问 - webshell_0001：网站后门 - network_1001：恶意挖矿 - network_1002：对外DDoS攻击 - network_1003：恶意扫描 - network_1004：敏感区域攻击 - ransomware_0001：勒索攻击 - ransomware_0002：勒索攻击 - ransomware_0003：勒索攻击 - fileless_0001：进程注入 - fileless_0002：动态库注入进程 - fileless_0003：关键配置变更 - fileless_0004：环境变量变更 - fileless_0005：内存文件进程 - fileless_0006：vdso劫持 - crontab_1001：Crontab可疑任务 - vul_exploit_0001：Redis漏洞利用攻击 - vul_exploit_0002：Hadoop漏洞利用攻击 - vul_exploit_0003：MySQL漏洞利用攻击 - rootkit_0001：可疑rootkit文件 - rootkit_0002：可疑内核模块 - RASP_0004：上传Webshell - RASP_0018：无文件Webshell - blockexec_001：已知勒索攻击 - hips_0001：Windows Defender防护被禁用 - hips_0002：可疑的黑客工具 - hips_0003：可疑的勒索加密行为 - hips_0004：隐藏账号创建 - hips_0005：读取用户密码凭据 - hips_0006：可疑的SAM文件导出 - hips_0007：可疑shadow copy删除操作 - hips_0008：备份文件删除 - hips_0009：可疑勒索病毒操作注册表 - hips_0010：可疑的异常进程行为 - hips_0011：可疑的扫描探测 - hips_0012：可疑的勒索病毒脚本运行 - hips_0013：可疑的挖矿命令执行 - hips_0014：可疑的禁用windows安全中心 - hips_0015：可疑的停止防火墙服务行为 - hips_0016：可疑的系统自动恢复禁用 - hips_0017：Office 创建可执行文件 - hips_0018：带宏Office文件异常创建 - hips_0019：可疑的注册表操作 - hips_0020：Confluence远程代码执行 - hips_0021：MSDT远程代码执行 - portscan_0001：通用端口扫描 - portscan_0002：秘密端口扫描 - k8s_1001：Kubernetes事件删除 - k8s_1002：创建特权Pod - k8s_1003：Pod中使用交互式shell - k8s_1004：创建敏感目录Pod - k8s_1005：创建主机网络的Pod - k8s_1006：创建主机Pid空间的Pod - k8s_1007：普通pod访问APIserver认证失败 - k8s_1008：普通Pod通过Curl访问APIServer - k8s_1009：系统管理空间执行exec - k8s_1010：系统管理空间创建Pod - k8s_1011：创建静态Pod - k8s_1012：创建DaemonSet - k8s_1013：创建集群计划任务 - k8s_1014：Secrets操作 - k8s_1015：枚举用户可执行的操作 - k8s_1016：高权限RoleBinding或ClusterRoleBinding - k8s_1017：ServiceAccount创建 - k8s_1018：创建Cronjob - k8s_1019：Pod中exec使用交互式shell - k8s_1020：无权限访问Apiserver - k8s_1021：使用curl访问APIServer - k8s_1022：Ingress漏洞 - k8s_1023：中间人攻击 - k8s_1024：蠕虫挖矿木马 - k8s_1025：K8s事件删除 - k8s_1026：SelfSubjectRulesReview场景 - imgblock_0001：镜像白名单阻断 - imgblock_0002：镜像黑名单阻断 - imgblock_0003：镜像标签白名单阻断 - imgblock_0004：镜像标签黑名单阻断 - imgblock_0005：创建容器白名单阻断 - imgblock_0006：创建容器黑名单阻断 - imgblock_0007：容器mount proc阻断 - imgblock_0008：容器seccomp unconfined阻断 - imgblock_0009：容器特权阻断 - imgblock_0010：容器capabilities阻断 - honeypot_0001：可疑的蜜罐异常访问
        :type event_class_id: str
        :param support_download_file: **参数解释**： 是否支持告警源文件下载 **取值范围**： - true：支持 - false：不支持
        :type support_download_file: bool
        :param malware_file_hash: **参数解释**： 恶意文件的hash,当前为sha256 **取值范围**： 不涉及
        :type malware_file_hash: str
        :param event_forensic_info: 
        :type event_forensic_info: :class:`huaweicloudsdkhss.v5.EventForensicInfo`
        """
        
        super().__init__()

        self._event_type = None
        self._event_class_id = None
        self._support_download_file = None
        self._malware_file_hash = None
        self._event_forensic_info = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if event_class_id is not None:
            self.event_class_id = event_class_id
        if support_download_file is not None:
            self.support_download_file = support_download_file
        if malware_file_hash is not None:
            self.malware_file_hash = malware_file_hash
        if event_forensic_info is not None:
            self.event_forensic_info = event_forensic_info

    @property
    def event_type(self):
        r"""Gets the event_type of this ListEventForensicResponse.

        **参数解释**： 事件类型 **取值范围**： - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012 ：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3027：Crontab可疑任务 - 3029 ：系统安全防护被禁用 - 3030 ：备份删除 - 3031 ：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色 - 11001：高级威胁事件

        :return: The event_type of this ListEventForensicResponse.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListEventForensicResponse.

        **参数解释**： 事件类型 **取值范围**： - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012 ：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3027：Crontab可疑任务 - 3029 ：系统安全防护被禁用 - 3030 ：备份删除 - 3031 ：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色 - 11001：高级威胁事件

        :param event_type: The event_type of this ListEventForensicResponse.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def event_class_id(self):
        r"""Gets the event_class_id of this ListEventForensicResponse.

        **参数解释**： 事件分类 **取值范围**： - container_1001：容器命名空间 - container_1002：容器开放端口 - container_1003：容器安全选项 - container_1004：容器挂载目录 - containerescape_0001：容器高危系统调用 - containerescape_0002：Shocker攻击 - containerescape_0003：DirtCow攻击 - containerescape_0004：容器文件逃逸攻击 - dockerfile_001：用户自定义容器保护文件被修改 - dockerfile_002：容器文件系统可执行文件被修改 - dockerproc_001：容器进程异常事件上报 - fileprotect_0001：文件提权 - fileprotect_0002：关键文件变更 - fileprotect_0003：关键文件路径变更 - fileprotect_0004：文件/目录变更 - av_1002：病毒 - av_1003：蠕虫 - av_1004：木马 - av_1005：僵尸网络 - av_1006：后门 - av_1007：间谍软件 - av_1008：恶意广告软件 - av_1009：钓鱼 - av_1010：Rootkit - av_1011：勒索软件 - av_1012：黑客工具 - av_1013：灰色软件 - av_1015：Webshell - av_1016：挖矿软件 - login_0001：尝试暴力破解 - login_0002：爆破成功 - login_1001：登录成功 - login_1002：异地登录 - login_1003：弱口令 - malware_0001：shell变更事件上报 - malware_0002：反弹shell事件上报 - malware_1001：恶意程序 - procdet_0001：进程异常行为检测 - procdet_0002：进程提权 - procreport_0001：危险命令 - user_1001：账号变更 - user_1002：风险账号 - vmescape_0001：虚拟机敏感命令执行 - vmescape_0002：虚拟化进程访问敏感文件 - vmescape_0003：虚拟机异常端口访问 - webshell_0001：网站后门 - network_1001：恶意挖矿 - network_1002：对外DDoS攻击 - network_1003：恶意扫描 - network_1004：敏感区域攻击 - ransomware_0001：勒索攻击 - ransomware_0002：勒索攻击 - ransomware_0003：勒索攻击 - fileless_0001：进程注入 - fileless_0002：动态库注入进程 - fileless_0003：关键配置变更 - fileless_0004：环境变量变更 - fileless_0005：内存文件进程 - fileless_0006：vdso劫持 - crontab_1001：Crontab可疑任务 - vul_exploit_0001：Redis漏洞利用攻击 - vul_exploit_0002：Hadoop漏洞利用攻击 - vul_exploit_0003：MySQL漏洞利用攻击 - rootkit_0001：可疑rootkit文件 - rootkit_0002：可疑内核模块 - RASP_0004：上传Webshell - RASP_0018：无文件Webshell - blockexec_001：已知勒索攻击 - hips_0001：Windows Defender防护被禁用 - hips_0002：可疑的黑客工具 - hips_0003：可疑的勒索加密行为 - hips_0004：隐藏账号创建 - hips_0005：读取用户密码凭据 - hips_0006：可疑的SAM文件导出 - hips_0007：可疑shadow copy删除操作 - hips_0008：备份文件删除 - hips_0009：可疑勒索病毒操作注册表 - hips_0010：可疑的异常进程行为 - hips_0011：可疑的扫描探测 - hips_0012：可疑的勒索病毒脚本运行 - hips_0013：可疑的挖矿命令执行 - hips_0014：可疑的禁用windows安全中心 - hips_0015：可疑的停止防火墙服务行为 - hips_0016：可疑的系统自动恢复禁用 - hips_0017：Office 创建可执行文件 - hips_0018：带宏Office文件异常创建 - hips_0019：可疑的注册表操作 - hips_0020：Confluence远程代码执行 - hips_0021：MSDT远程代码执行 - portscan_0001：通用端口扫描 - portscan_0002：秘密端口扫描 - k8s_1001：Kubernetes事件删除 - k8s_1002：创建特权Pod - k8s_1003：Pod中使用交互式shell - k8s_1004：创建敏感目录Pod - k8s_1005：创建主机网络的Pod - k8s_1006：创建主机Pid空间的Pod - k8s_1007：普通pod访问APIserver认证失败 - k8s_1008：普通Pod通过Curl访问APIServer - k8s_1009：系统管理空间执行exec - k8s_1010：系统管理空间创建Pod - k8s_1011：创建静态Pod - k8s_1012：创建DaemonSet - k8s_1013：创建集群计划任务 - k8s_1014：Secrets操作 - k8s_1015：枚举用户可执行的操作 - k8s_1016：高权限RoleBinding或ClusterRoleBinding - k8s_1017：ServiceAccount创建 - k8s_1018：创建Cronjob - k8s_1019：Pod中exec使用交互式shell - k8s_1020：无权限访问Apiserver - k8s_1021：使用curl访问APIServer - k8s_1022：Ingress漏洞 - k8s_1023：中间人攻击 - k8s_1024：蠕虫挖矿木马 - k8s_1025：K8s事件删除 - k8s_1026：SelfSubjectRulesReview场景 - imgblock_0001：镜像白名单阻断 - imgblock_0002：镜像黑名单阻断 - imgblock_0003：镜像标签白名单阻断 - imgblock_0004：镜像标签黑名单阻断 - imgblock_0005：创建容器白名单阻断 - imgblock_0006：创建容器黑名单阻断 - imgblock_0007：容器mount proc阻断 - imgblock_0008：容器seccomp unconfined阻断 - imgblock_0009：容器特权阻断 - imgblock_0010：容器capabilities阻断 - honeypot_0001：可疑的蜜罐异常访问

        :return: The event_class_id of this ListEventForensicResponse.
        :rtype: str
        """
        return self._event_class_id

    @event_class_id.setter
    def event_class_id(self, event_class_id):
        r"""Sets the event_class_id of this ListEventForensicResponse.

        **参数解释**： 事件分类 **取值范围**： - container_1001：容器命名空间 - container_1002：容器开放端口 - container_1003：容器安全选项 - container_1004：容器挂载目录 - containerescape_0001：容器高危系统调用 - containerescape_0002：Shocker攻击 - containerescape_0003：DirtCow攻击 - containerescape_0004：容器文件逃逸攻击 - dockerfile_001：用户自定义容器保护文件被修改 - dockerfile_002：容器文件系统可执行文件被修改 - dockerproc_001：容器进程异常事件上报 - fileprotect_0001：文件提权 - fileprotect_0002：关键文件变更 - fileprotect_0003：关键文件路径变更 - fileprotect_0004：文件/目录变更 - av_1002：病毒 - av_1003：蠕虫 - av_1004：木马 - av_1005：僵尸网络 - av_1006：后门 - av_1007：间谍软件 - av_1008：恶意广告软件 - av_1009：钓鱼 - av_1010：Rootkit - av_1011：勒索软件 - av_1012：黑客工具 - av_1013：灰色软件 - av_1015：Webshell - av_1016：挖矿软件 - login_0001：尝试暴力破解 - login_0002：爆破成功 - login_1001：登录成功 - login_1002：异地登录 - login_1003：弱口令 - malware_0001：shell变更事件上报 - malware_0002：反弹shell事件上报 - malware_1001：恶意程序 - procdet_0001：进程异常行为检测 - procdet_0002：进程提权 - procreport_0001：危险命令 - user_1001：账号变更 - user_1002：风险账号 - vmescape_0001：虚拟机敏感命令执行 - vmescape_0002：虚拟化进程访问敏感文件 - vmescape_0003：虚拟机异常端口访问 - webshell_0001：网站后门 - network_1001：恶意挖矿 - network_1002：对外DDoS攻击 - network_1003：恶意扫描 - network_1004：敏感区域攻击 - ransomware_0001：勒索攻击 - ransomware_0002：勒索攻击 - ransomware_0003：勒索攻击 - fileless_0001：进程注入 - fileless_0002：动态库注入进程 - fileless_0003：关键配置变更 - fileless_0004：环境变量变更 - fileless_0005：内存文件进程 - fileless_0006：vdso劫持 - crontab_1001：Crontab可疑任务 - vul_exploit_0001：Redis漏洞利用攻击 - vul_exploit_0002：Hadoop漏洞利用攻击 - vul_exploit_0003：MySQL漏洞利用攻击 - rootkit_0001：可疑rootkit文件 - rootkit_0002：可疑内核模块 - RASP_0004：上传Webshell - RASP_0018：无文件Webshell - blockexec_001：已知勒索攻击 - hips_0001：Windows Defender防护被禁用 - hips_0002：可疑的黑客工具 - hips_0003：可疑的勒索加密行为 - hips_0004：隐藏账号创建 - hips_0005：读取用户密码凭据 - hips_0006：可疑的SAM文件导出 - hips_0007：可疑shadow copy删除操作 - hips_0008：备份文件删除 - hips_0009：可疑勒索病毒操作注册表 - hips_0010：可疑的异常进程行为 - hips_0011：可疑的扫描探测 - hips_0012：可疑的勒索病毒脚本运行 - hips_0013：可疑的挖矿命令执行 - hips_0014：可疑的禁用windows安全中心 - hips_0015：可疑的停止防火墙服务行为 - hips_0016：可疑的系统自动恢复禁用 - hips_0017：Office 创建可执行文件 - hips_0018：带宏Office文件异常创建 - hips_0019：可疑的注册表操作 - hips_0020：Confluence远程代码执行 - hips_0021：MSDT远程代码执行 - portscan_0001：通用端口扫描 - portscan_0002：秘密端口扫描 - k8s_1001：Kubernetes事件删除 - k8s_1002：创建特权Pod - k8s_1003：Pod中使用交互式shell - k8s_1004：创建敏感目录Pod - k8s_1005：创建主机网络的Pod - k8s_1006：创建主机Pid空间的Pod - k8s_1007：普通pod访问APIserver认证失败 - k8s_1008：普通Pod通过Curl访问APIServer - k8s_1009：系统管理空间执行exec - k8s_1010：系统管理空间创建Pod - k8s_1011：创建静态Pod - k8s_1012：创建DaemonSet - k8s_1013：创建集群计划任务 - k8s_1014：Secrets操作 - k8s_1015：枚举用户可执行的操作 - k8s_1016：高权限RoleBinding或ClusterRoleBinding - k8s_1017：ServiceAccount创建 - k8s_1018：创建Cronjob - k8s_1019：Pod中exec使用交互式shell - k8s_1020：无权限访问Apiserver - k8s_1021：使用curl访问APIServer - k8s_1022：Ingress漏洞 - k8s_1023：中间人攻击 - k8s_1024：蠕虫挖矿木马 - k8s_1025：K8s事件删除 - k8s_1026：SelfSubjectRulesReview场景 - imgblock_0001：镜像白名单阻断 - imgblock_0002：镜像黑名单阻断 - imgblock_0003：镜像标签白名单阻断 - imgblock_0004：镜像标签黑名单阻断 - imgblock_0005：创建容器白名单阻断 - imgblock_0006：创建容器黑名单阻断 - imgblock_0007：容器mount proc阻断 - imgblock_0008：容器seccomp unconfined阻断 - imgblock_0009：容器特权阻断 - imgblock_0010：容器capabilities阻断 - honeypot_0001：可疑的蜜罐异常访问

        :param event_class_id: The event_class_id of this ListEventForensicResponse.
        :type event_class_id: str
        """
        self._event_class_id = event_class_id

    @property
    def support_download_file(self):
        r"""Gets the support_download_file of this ListEventForensicResponse.

        **参数解释**： 是否支持告警源文件下载 **取值范围**： - true：支持 - false：不支持

        :return: The support_download_file of this ListEventForensicResponse.
        :rtype: bool
        """
        return self._support_download_file

    @support_download_file.setter
    def support_download_file(self, support_download_file):
        r"""Sets the support_download_file of this ListEventForensicResponse.

        **参数解释**： 是否支持告警源文件下载 **取值范围**： - true：支持 - false：不支持

        :param support_download_file: The support_download_file of this ListEventForensicResponse.
        :type support_download_file: bool
        """
        self._support_download_file = support_download_file

    @property
    def malware_file_hash(self):
        r"""Gets the malware_file_hash of this ListEventForensicResponse.

        **参数解释**： 恶意文件的hash,当前为sha256 **取值范围**： 不涉及

        :return: The malware_file_hash of this ListEventForensicResponse.
        :rtype: str
        """
        return self._malware_file_hash

    @malware_file_hash.setter
    def malware_file_hash(self, malware_file_hash):
        r"""Sets the malware_file_hash of this ListEventForensicResponse.

        **参数解释**： 恶意文件的hash,当前为sha256 **取值范围**： 不涉及

        :param malware_file_hash: The malware_file_hash of this ListEventForensicResponse.
        :type malware_file_hash: str
        """
        self._malware_file_hash = malware_file_hash

    @property
    def event_forensic_info(self):
        r"""Gets the event_forensic_info of this ListEventForensicResponse.

        :return: The event_forensic_info of this ListEventForensicResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.EventForensicInfo`
        """
        return self._event_forensic_info

    @event_forensic_info.setter
    def event_forensic_info(self, event_forensic_info):
        r"""Sets the event_forensic_info of this ListEventForensicResponse.

        :param event_forensic_info: The event_forensic_info of this ListEventForensicResponse.
        :type event_forensic_info: :class:`huaweicloudsdkhss.v5.EventForensicInfo`
        """
        self._event_forensic_info = event_forensic_info

    def to_dict(self):
        import warnings
        warnings.warn("ListEventForensicResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListEventForensicResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
