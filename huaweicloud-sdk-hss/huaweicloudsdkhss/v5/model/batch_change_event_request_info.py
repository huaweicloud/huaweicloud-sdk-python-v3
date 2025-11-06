# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchChangeEventRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_type': 'str',
        'handler': 'str',
        'event_type': 'int',
        'category': 'str'
    }

    attribute_map = {
        'operate_type': 'operate_type',
        'handler': 'handler',
        'event_type': 'event_type',
        'category': 'category'
    }

    def __init__(self, operate_type=None, handler=None, event_type=None, category=None):
        r"""BatchChangeEventRequestInfo

        The model defined in huaweicloud sdk

        :param operate_type: **参数解释**： 处理方式 **取值范围**： - mark_as_handled：手动处理 - ignore：忽略 - add_to_alarm_whitelist：加入告警白名单 - add_to_login_whitelist：加入登录白名单 - isolate_and_kill：隔离查杀 - unhandle：取消手动处理 - do_not_ignore：取消忽略 - remove_from_alarm_whitelist：删除告警白名单 - remove_from_login_whitelist：删除登录白名单 - do_not_isolate_or_kill：取消隔离查杀 
        :type operate_type: str
        :param handler: **参数解释**： 备注信息，已处理的告警才有 **取值范围**： 字符长度1-256位 
        :type handler: str
        :param event_type: **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 
        :type event_type: int
        :param category: 告警分类，包含如下：   - container：容器   - host：主机
        :type category: str
        """
        
        

        self._operate_type = None
        self._handler = None
        self._event_type = None
        self._category = None
        self.discriminator = None

        self.operate_type = operate_type
        self.handler = handler
        self.event_type = event_type
        if category is not None:
            self.category = category

    @property
    def operate_type(self):
        r"""Gets the operate_type of this BatchChangeEventRequestInfo.

        **参数解释**： 处理方式 **取值范围**： - mark_as_handled：手动处理 - ignore：忽略 - add_to_alarm_whitelist：加入告警白名单 - add_to_login_whitelist：加入登录白名单 - isolate_and_kill：隔离查杀 - unhandle：取消手动处理 - do_not_ignore：取消忽略 - remove_from_alarm_whitelist：删除告警白名单 - remove_from_login_whitelist：删除登录白名单 - do_not_isolate_or_kill：取消隔离查杀 

        :return: The operate_type of this BatchChangeEventRequestInfo.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this BatchChangeEventRequestInfo.

        **参数解释**： 处理方式 **取值范围**： - mark_as_handled：手动处理 - ignore：忽略 - add_to_alarm_whitelist：加入告警白名单 - add_to_login_whitelist：加入登录白名单 - isolate_and_kill：隔离查杀 - unhandle：取消手动处理 - do_not_ignore：取消忽略 - remove_from_alarm_whitelist：删除告警白名单 - remove_from_login_whitelist：删除登录白名单 - do_not_isolate_or_kill：取消隔离查杀 

        :param operate_type: The operate_type of this BatchChangeEventRequestInfo.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def handler(self):
        r"""Gets the handler of this BatchChangeEventRequestInfo.

        **参数解释**： 备注信息，已处理的告警才有 **取值范围**： 字符长度1-256位 

        :return: The handler of this BatchChangeEventRequestInfo.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        r"""Sets the handler of this BatchChangeEventRequestInfo.

        **参数解释**： 备注信息，已处理的告警才有 **取值范围**： 字符长度1-256位 

        :param handler: The handler of this BatchChangeEventRequestInfo.
        :type handler: str
        """
        self._handler = handler

    @property
    def event_type(self):
        r"""Gets the event_type of this BatchChangeEventRequestInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 

        :return: The event_type of this BatchChangeEventRequestInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this BatchChangeEventRequestInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 

        :param event_type: The event_type of this BatchChangeEventRequestInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def category(self):
        r"""Gets the category of this BatchChangeEventRequestInfo.

        告警分类，包含如下：   - container：容器   - host：主机

        :return: The category of this BatchChangeEventRequestInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this BatchChangeEventRequestInfo.

        告警分类，包含如下：   - container：容器   - host：主机

        :param category: The category of this BatchChangeEventRequestInfo.
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
        if not isinstance(other, BatchChangeEventRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
