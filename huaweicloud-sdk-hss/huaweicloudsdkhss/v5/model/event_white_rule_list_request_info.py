# coding: utf-8

import six

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
        'judge_type': 'str'
    }

    attribute_map = {
        'event_type': 'event_type',
        'field_key': 'field_key',
        'field_value': 'field_value',
        'judge_type': 'judge_type'
    }

    def __init__(self, event_type=None, field_key=None, field_value=None, judge_type=None):
        r"""EventWhiteRuleListRequestInfo

        The model defined in huaweicloud sdk

        :param event_type: **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 
        :type event_type: int
        :param field_key: 加白字段，包含如下: - \&quot;file/process hash\&quot; # 进程/文件hash - \&quot;file_path\&quot; # 文件路径 - \&quot;process_path\&quot; # 进程路径 - \&quot;login_ip\&quot; # 登录ip - \&quot;reg_key\&quot; #注册表key - \&quot;process_cmdline\&quot; # 进程命令行 - \&quot;username\&quot; # 用户名
        :type field_key: str
        :param field_value: 加白字段值
        :type field_value: str
        :param judge_type: 通配符，包含如下: - \&quot;equal\&quot; # 相等 - \&quot;contain\&quot; # 包含
        :type judge_type: str
        """
        
        

        self._event_type = None
        self._field_key = None
        self._field_value = None
        self._judge_type = None
        self.discriminator = None

        self.event_type = event_type
        self.field_key = field_key
        self.field_value = field_value
        self.judge_type = judge_type

    @property
    def event_type(self):
        r"""Gets the event_type of this EventWhiteRuleListRequestInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 

        :return: The event_type of this EventWhiteRuleListRequestInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this EventWhiteRuleListRequestInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 

        :param event_type: The event_type of this EventWhiteRuleListRequestInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def field_key(self):
        r"""Gets the field_key of this EventWhiteRuleListRequestInfo.

        加白字段，包含如下: - \"file/process hash\" # 进程/文件hash - \"file_path\" # 文件路径 - \"process_path\" # 进程路径 - \"login_ip\" # 登录ip - \"reg_key\" #注册表key - \"process_cmdline\" # 进程命令行 - \"username\" # 用户名

        :return: The field_key of this EventWhiteRuleListRequestInfo.
        :rtype: str
        """
        return self._field_key

    @field_key.setter
    def field_key(self, field_key):
        r"""Sets the field_key of this EventWhiteRuleListRequestInfo.

        加白字段，包含如下: - \"file/process hash\" # 进程/文件hash - \"file_path\" # 文件路径 - \"process_path\" # 进程路径 - \"login_ip\" # 登录ip - \"reg_key\" #注册表key - \"process_cmdline\" # 进程命令行 - \"username\" # 用户名

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

        通配符，包含如下: - \"equal\" # 相等 - \"contain\" # 包含

        :return: The judge_type of this EventWhiteRuleListRequestInfo.
        :rtype: str
        """
        return self._judge_type

    @judge_type.setter
    def judge_type(self, judge_type):
        r"""Sets the judge_type of this EventWhiteRuleListRequestInfo.

        通配符，包含如下: - \"equal\" # 相等 - \"contain\" # 包含

        :param judge_type: The judge_type of this EventWhiteRuleListRequestInfo.
        :type judge_type: str
        """
        self._judge_type = judge_type

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
        if not isinstance(other, EventWhiteRuleListRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
