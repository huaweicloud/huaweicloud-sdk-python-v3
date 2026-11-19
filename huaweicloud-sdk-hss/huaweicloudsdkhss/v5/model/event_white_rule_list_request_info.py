# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventWhiteRuleListRequestInfo:

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
        'field_key': 'str',
        'field_value': 'str',
        'judge_type': 'str',
        'scope': 'bool',
        'agent_ids': 'list[str]',
        'instance_ids': 'list[str]'
    }

    attribute_map = {
        'event_type': 'event_type',
        'field_key': 'field_key',
        'field_value': 'field_value',
        'judge_type': 'judge_type',
        'scope': 'scope',
        'agent_ids': 'agent_ids',
        'instance_ids': 'instance_ids'
    }

    def __init__(self, event_type=None, field_key=None, field_value=None, judge_type=None, scope=None, agent_ids=None, instance_ids=None):
        r"""EventWhiteRuleListRequestInfo

        The model defined in huaweicloud sdk

        :param event_type: **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3026：crontab提权   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色   - 2006：XSS攻击   - 2007：SQL注入   - 2008：XML注入   - 2009：代码注入   - 2010：命令注入   - 2011：命令执行   - 2042：漏洞逃逸攻击   - 2044：文件逃逸攻击   - 2046：JNDI注入   - 3008：容器进程异常   - 3009：容器异常启动   - 3016：高危系统调用   - 3021：敏感文件访问   - 3023：异常命令执行   - 3025：可疑异常   - 3038：系统日志删除   - 3039：可疑命令执行   - 3040：可疑进程运行   - 3041：可疑进程文件访问   - 3043：运行时异常行为   - 3044：内核模块加载   - 4016：用户账号变更   - 5001：未知网络访问   - 5003：异常外联行为   - 5014：端口转发   - 5015：可疑的下载请求   - 5016：可疑的HTTP请求   - 8005：目录遍历   - 11001：高级威胁事件   - 12001：进程注入   - 12002：动态库注入进程   - 12005：内存文件进程   - 12006：vdso劫持   - 12007：利用Windows工具攻击   - 12008：注册表恶意注入   - 60001：直接提示词注入   - 60002：恶意指令与越狱   - 61001：间接提示词注入   - 61002：数据投毒与误导   - 62001：工具反馈污染   - 62002：工具描述/接口注入   - 63001：越权操作攻击   - 63002：资源耗尽攻击   - 64001：未授权操作   - 64002：权限提升尝试   - 64003：角色访问违规   - 64004：策略约束违规   - 65001：未授权信息输出   - 65002：API密钥/凭证泄露   - 65003：内部业务数据泄露   - 65004：策略约束违规输出   - 65005：隐私信息泄露   - 66001：智能体高危命令执行   - 66002：智能体敏感文件访问   - 67001：其他类告警   - 68001：记忆投毒   - 68002：RAG异常调用   - 68003：工具参数注入   - 68004：工具循环调用   - 68005：上下文资源滥用 
        :type event_type: int
        :param field_key: **参数解释**： 加白字段 **取值范围**: - file/process hash：进程/文件hash。 - file_path：文件路径。 - process_path：进程路径。 - login_ip：登录ip。 - reg_key：注册表key。 - process_cmdline：进程命令行。 - username：用户名。 
        :type field_key: str
        :param field_value: 加白字段值
        :type field_value: str
        :param judge_type: **参数解释**： 通配符 **取值范围**: - equal：相等。 - contain：包含。 
        :type judge_type: str
        :param scope: **参数解释**: 是否选择所有主机 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: false 
        :type scope: bool
        :param agent_ids: **参数解释**: agent列表 **约束限制**: 不涉及 **取值范围**: 1-1000个agentID **默认取值**: 不涉及 
        :type agent_ids: list[str]
        :param instance_ids: **参数解释**: 实例ID列表 **约束限制**: 当需要为serverless配置规则时，传入此字段 **取值范围**: 1-1000个实例ID 
        :type instance_ids: list[str]
        """
        
        

        self._event_type = None
        self._field_key = None
        self._field_value = None
        self._judge_type = None
        self._scope = None
        self._agent_ids = None
        self._instance_ids = None
        self.discriminator = None

        self.event_type = event_type
        self.field_key = field_key
        self.field_value = field_value
        self.judge_type = judge_type
        if scope is not None:
            self.scope = scope
        if agent_ids is not None:
            self.agent_ids = agent_ids
        if instance_ids is not None:
            self.instance_ids = instance_ids

    @property
    def event_type(self):
        r"""Gets the event_type of this EventWhiteRuleListRequestInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3026：crontab提权   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色   - 2006：XSS攻击   - 2007：SQL注入   - 2008：XML注入   - 2009：代码注入   - 2010：命令注入   - 2011：命令执行   - 2042：漏洞逃逸攻击   - 2044：文件逃逸攻击   - 2046：JNDI注入   - 3008：容器进程异常   - 3009：容器异常启动   - 3016：高危系统调用   - 3021：敏感文件访问   - 3023：异常命令执行   - 3025：可疑异常   - 3038：系统日志删除   - 3039：可疑命令执行   - 3040：可疑进程运行   - 3041：可疑进程文件访问   - 3043：运行时异常行为   - 3044：内核模块加载   - 4016：用户账号变更   - 5001：未知网络访问   - 5003：异常外联行为   - 5014：端口转发   - 5015：可疑的下载请求   - 5016：可疑的HTTP请求   - 8005：目录遍历   - 11001：高级威胁事件   - 12001：进程注入   - 12002：动态库注入进程   - 12005：内存文件进程   - 12006：vdso劫持   - 12007：利用Windows工具攻击   - 12008：注册表恶意注入   - 60001：直接提示词注入   - 60002：恶意指令与越狱   - 61001：间接提示词注入   - 61002：数据投毒与误导   - 62001：工具反馈污染   - 62002：工具描述/接口注入   - 63001：越权操作攻击   - 63002：资源耗尽攻击   - 64001：未授权操作   - 64002：权限提升尝试   - 64003：角色访问违规   - 64004：策略约束违规   - 65001：未授权信息输出   - 65002：API密钥/凭证泄露   - 65003：内部业务数据泄露   - 65004：策略约束违规输出   - 65005：隐私信息泄露   - 66001：智能体高危命令执行   - 66002：智能体敏感文件访问   - 67001：其他类告警   - 68001：记忆投毒   - 68002：RAG异常调用   - 68003：工具参数注入   - 68004：工具循环调用   - 68005：上下文资源滥用 

        :return: The event_type of this EventWhiteRuleListRequestInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this EventWhiteRuleListRequestInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3026：crontab提权   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色   - 2006：XSS攻击   - 2007：SQL注入   - 2008：XML注入   - 2009：代码注入   - 2010：命令注入   - 2011：命令执行   - 2042：漏洞逃逸攻击   - 2044：文件逃逸攻击   - 2046：JNDI注入   - 3008：容器进程异常   - 3009：容器异常启动   - 3016：高危系统调用   - 3021：敏感文件访问   - 3023：异常命令执行   - 3025：可疑异常   - 3038：系统日志删除   - 3039：可疑命令执行   - 3040：可疑进程运行   - 3041：可疑进程文件访问   - 3043：运行时异常行为   - 3044：内核模块加载   - 4016：用户账号变更   - 5001：未知网络访问   - 5003：异常外联行为   - 5014：端口转发   - 5015：可疑的下载请求   - 5016：可疑的HTTP请求   - 8005：目录遍历   - 11001：高级威胁事件   - 12001：进程注入   - 12002：动态库注入进程   - 12005：内存文件进程   - 12006：vdso劫持   - 12007：利用Windows工具攻击   - 12008：注册表恶意注入   - 60001：直接提示词注入   - 60002：恶意指令与越狱   - 61001：间接提示词注入   - 61002：数据投毒与误导   - 62001：工具反馈污染   - 62002：工具描述/接口注入   - 63001：越权操作攻击   - 63002：资源耗尽攻击   - 64001：未授权操作   - 64002：权限提升尝试   - 64003：角色访问违规   - 64004：策略约束违规   - 65001：未授权信息输出   - 65002：API密钥/凭证泄露   - 65003：内部业务数据泄露   - 65004：策略约束违规输出   - 65005：隐私信息泄露   - 66001：智能体高危命令执行   - 66002：智能体敏感文件访问   - 67001：其他类告警   - 68001：记忆投毒   - 68002：RAG异常调用   - 68003：工具参数注入   - 68004：工具循环调用   - 68005：上下文资源滥用 

        :param event_type: The event_type of this EventWhiteRuleListRequestInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def field_key(self):
        r"""Gets the field_key of this EventWhiteRuleListRequestInfo.

        **参数解释**： 加白字段 **取值范围**: - file/process hash：进程/文件hash。 - file_path：文件路径。 - process_path：进程路径。 - login_ip：登录ip。 - reg_key：注册表key。 - process_cmdline：进程命令行。 - username：用户名。 

        :return: The field_key of this EventWhiteRuleListRequestInfo.
        :rtype: str
        """
        return self._field_key

    @field_key.setter
    def field_key(self, field_key):
        r"""Sets the field_key of this EventWhiteRuleListRequestInfo.

        **参数解释**： 加白字段 **取值范围**: - file/process hash：进程/文件hash。 - file_path：文件路径。 - process_path：进程路径。 - login_ip：登录ip。 - reg_key：注册表key。 - process_cmdline：进程命令行。 - username：用户名。 

        :param field_key: The field_key of this EventWhiteRuleListRequestInfo.
        :type field_key: str
        """
        self._field_key = field_key

    @property
    def field_value(self):
        r"""Gets the field_value of this EventWhiteRuleListRequestInfo.

        加白字段值

        :return: The field_value of this EventWhiteRuleListRequestInfo.
        :rtype: str
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        r"""Sets the field_value of this EventWhiteRuleListRequestInfo.

        加白字段值

        :param field_value: The field_value of this EventWhiteRuleListRequestInfo.
        :type field_value: str
        """
        self._field_value = field_value

    @property
    def judge_type(self):
        r"""Gets the judge_type of this EventWhiteRuleListRequestInfo.

        **参数解释**： 通配符 **取值范围**: - equal：相等。 - contain：包含。 

        :return: The judge_type of this EventWhiteRuleListRequestInfo.
        :rtype: str
        """
        return self._judge_type

    @judge_type.setter
    def judge_type(self, judge_type):
        r"""Sets the judge_type of this EventWhiteRuleListRequestInfo.

        **参数解释**： 通配符 **取值范围**: - equal：相等。 - contain：包含。 

        :param judge_type: The judge_type of this EventWhiteRuleListRequestInfo.
        :type judge_type: str
        """
        self._judge_type = judge_type

    @property
    def scope(self):
        r"""Gets the scope of this EventWhiteRuleListRequestInfo.

        **参数解释**: 是否选择所有主机 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: false 

        :return: The scope of this EventWhiteRuleListRequestInfo.
        :rtype: bool
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this EventWhiteRuleListRequestInfo.

        **参数解释**: 是否选择所有主机 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: false 

        :param scope: The scope of this EventWhiteRuleListRequestInfo.
        :type scope: bool
        """
        self._scope = scope

    @property
    def agent_ids(self):
        r"""Gets the agent_ids of this EventWhiteRuleListRequestInfo.

        **参数解释**: agent列表 **约束限制**: 不涉及 **取值范围**: 1-1000个agentID **默认取值**: 不涉及 

        :return: The agent_ids of this EventWhiteRuleListRequestInfo.
        :rtype: list[str]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        r"""Sets the agent_ids of this EventWhiteRuleListRequestInfo.

        **参数解释**: agent列表 **约束限制**: 不涉及 **取值范围**: 1-1000个agentID **默认取值**: 不涉及 

        :param agent_ids: The agent_ids of this EventWhiteRuleListRequestInfo.
        :type agent_ids: list[str]
        """
        self._agent_ids = agent_ids

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this EventWhiteRuleListRequestInfo.

        **参数解释**: 实例ID列表 **约束限制**: 当需要为serverless配置规则时，传入此字段 **取值范围**: 1-1000个实例ID 

        :return: The instance_ids of this EventWhiteRuleListRequestInfo.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this EventWhiteRuleListRequestInfo.

        **参数解释**: 实例ID列表 **约束限制**: 当需要为serverless配置规则时，传入此字段 **取值范围**: 1-1000个实例ID 

        :param instance_ids: The instance_ids of this EventWhiteRuleListRequestInfo.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

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
        if not isinstance(other, EventWhiteRuleListRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
