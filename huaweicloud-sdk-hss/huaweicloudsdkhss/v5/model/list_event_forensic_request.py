# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventForensicRequest:

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
        'event_type': 'int',
        'event_id': 'str',
        'occur_time': 'int',
        'category': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'event_type': 'event_type',
        'event_id': 'event_id',
        'occur_time': 'occur_time',
        'category': 'category'
    }

    def __init__(self, enterprise_project_id=None, event_type=None, event_id=None, occur_time=None, category=None):
        r"""ListEventForensicRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param event_type: **参数解释**： 事件类型 **约束限制**： 不涉及 **取值范围**： - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3027：Crontab可疑任务 - 3029：系统安全防护被禁用 - 3030：备份删除 - 3031：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色 - 11001：高级威胁事件  **默认取值**： 不涉及
        :type event_type: int
        :param event_id: **参数解释**： 事件编号 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及
        :type event_id: str
        :param occur_time: **参数解释**： 事件发生时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type occur_time: int
        :param category: **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件 - serverless：serverless场景安全事件 **默认取值**: 不涉及 
        :type category: str
        """
        
        

        self._enterprise_project_id = None
        self._event_type = None
        self._event_id = None
        self._occur_time = None
        self._category = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.event_type = event_type
        self.event_id = event_id
        self.occur_time = occur_time
        if category is not None:
            self.category = category

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListEventForensicRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListEventForensicRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListEventForensicRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListEventForensicRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def event_type(self):
        r"""Gets the event_type of this ListEventForensicRequest.

        **参数解释**： 事件类型 **约束限制**： 不涉及 **取值范围**： - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3027：Crontab可疑任务 - 3029：系统安全防护被禁用 - 3030：备份删除 - 3031：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色 - 11001：高级威胁事件  **默认取值**： 不涉及

        :return: The event_type of this ListEventForensicRequest.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListEventForensicRequest.

        **参数解释**： 事件类型 **约束限制**： 不涉及 **取值范围**： - 1001：通用恶意软件 - 1002：病毒 - 1003：蠕虫 - 1004：木马 - 1005：僵尸网络 - 1006：后门 - 1010：Rootkit - 1011：勒索软件 - 1012：黑客工具 - 1015：Webshell - 1016：挖矿 - 1017：反弹Shell - 2001：一般漏洞利用 - 2012：远程代码执行 - 2047：Redis漏洞利用 - 2048：Hadoop漏洞利用 - 2049：MySQL漏洞利用 - 3002：文件提权 - 3003：进程提权 - 3004：关键文件变更 - 3005：文件/目录变更 - 3007：进程异常行为 - 3015：高危命令执行 - 3018：异常Shell - 3027：Crontab可疑任务 - 3029：系统安全防护被禁用 - 3030：备份删除 - 3031：异常注册表操作 - 3036：容器镜像阻断 - 4002：暴力破解 - 4004：异常登录 - 4006：非法系统账号 - 4014：用户账号添加 - 4020：用户密码窃取 - 6002：端口扫描 - 6003：主机扫描 - 13001：Kubernetes事件删除 - 13002：Pod异常行为 - 13003：枚举用户信息 - 13004：绑定集群用户角色 - 11001：高级威胁事件  **默认取值**： 不涉及

        :param event_type: The event_type of this ListEventForensicRequest.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def event_id(self):
        r"""Gets the event_id of this ListEventForensicRequest.

        **参数解释**： 事件编号 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及

        :return: The event_id of this ListEventForensicRequest.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this ListEventForensicRequest.

        **参数解释**： 事件编号 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及

        :param event_id: The event_id of this ListEventForensicRequest.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def occur_time(self):
        r"""Gets the occur_time of this ListEventForensicRequest.

        **参数解释**： 事件发生时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The occur_time of this ListEventForensicRequest.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        r"""Sets the occur_time of this ListEventForensicRequest.

        **参数解释**： 事件发生时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param occur_time: The occur_time of this ListEventForensicRequest.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def category(self):
        r"""Gets the category of this ListEventForensicRequest.

        **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件 - serverless：serverless场景安全事件 **默认取值**: 不涉及 

        :return: The category of this ListEventForensicRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListEventForensicRequest.

        **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件 - serverless：serverless场景安全事件 **默认取值**: 不涉及 

        :param category: The category of this ListEventForensicRequest.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, ListEventForensicRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
