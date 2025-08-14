# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmWhiteListResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_name': 'str',
        'hash': 'str',
        'description': 'str',
        'event_type': 'int',
        'white_field': 'str',
        'field_value': 'str',
        'judge_type': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'enterprise_project_name': 'enterprise_project_name',
        'hash': 'hash',
        'description': 'description',
        'event_type': 'event_type',
        'white_field': 'white_field',
        'field_value': 'field_value',
        'judge_type': 'judge_type',
        'update_time': 'update_time'
    }

    def __init__(self, enterprise_project_name=None, hash=None, description=None, event_type=None, white_field=None, field_value=None, judge_type=None, update_time=None):
        r"""AlarmWhiteListResponseInfo

        The model defined in huaweicloud sdk

        :param enterprise_project_name: 企业项目名称
        :type enterprise_project_name: str
        :param hash: **参数解释**: 事件白名单SHA256 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及
        :type hash: str
        :param description: **参数解释**: 描述信息。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及
        :type description: str
        :param event_type: **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 
        :type event_type: int
        :param white_field: 加白字段，包含如下: - \&quot;file/process hash\&quot; # 进程/文件hash - \&quot;file_path\&quot; # 文件路径 - \&quot;process_path\&quot; # 进程路径 - \&quot;login_ip\&quot; # 登录ip - \&quot;reg_key\&quot; #注册表key - \&quot;process_cmdline\&quot; # 进程命令行 - \&quot;username\&quot; # 用户名
        :type white_field: str
        :param field_value: 加白字段值
        :type field_value: str
        :param judge_type: 通配符，包含如下: - \&quot;equal\&quot; # 相等 - \&quot;contain\&quot; # 包含
        :type judge_type: str
        :param update_time: 事件白名单更新时间，毫秒
        :type update_time: int
        """
        
        

        self._enterprise_project_name = None
        self._hash = None
        self._description = None
        self._event_type = None
        self._white_field = None
        self._field_value = None
        self._judge_type = None
        self._update_time = None
        self.discriminator = None

        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if hash is not None:
            self.hash = hash
        if description is not None:
            self.description = description
        if event_type is not None:
            self.event_type = event_type
        if white_field is not None:
            self.white_field = white_field
        if field_value is not None:
            self.field_value = field_value
        if judge_type is not None:
            self.judge_type = judge_type
        if update_time is not None:
            self.update_time = update_time

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this AlarmWhiteListResponseInfo.

        企业项目名称

        :return: The enterprise_project_name of this AlarmWhiteListResponseInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this AlarmWhiteListResponseInfo.

        企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this AlarmWhiteListResponseInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def hash(self):
        r"""Gets the hash of this AlarmWhiteListResponseInfo.

        **参数解释**: 事件白名单SHA256 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及

        :return: The hash of this AlarmWhiteListResponseInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this AlarmWhiteListResponseInfo.

        **参数解释**: 事件白名单SHA256 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及

        :param hash: The hash of this AlarmWhiteListResponseInfo.
        :type hash: str
        """
        self._hash = hash

    @property
    def description(self):
        r"""Gets the description of this AlarmWhiteListResponseInfo.

        **参数解释**: 描述信息。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及

        :return: The description of this AlarmWhiteListResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlarmWhiteListResponseInfo.

        **参数解释**: 描述信息。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及

        :param description: The description of this AlarmWhiteListResponseInfo.
        :type description: str
        """
        self._description = description

    @property
    def event_type(self):
        r"""Gets the event_type of this AlarmWhiteListResponseInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 

        :return: The event_type of this AlarmWhiteListResponseInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this AlarmWhiteListResponseInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 

        :param event_type: The event_type of this AlarmWhiteListResponseInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def white_field(self):
        r"""Gets the white_field of this AlarmWhiteListResponseInfo.

        加白字段，包含如下: - \"file/process hash\" # 进程/文件hash - \"file_path\" # 文件路径 - \"process_path\" # 进程路径 - \"login_ip\" # 登录ip - \"reg_key\" #注册表key - \"process_cmdline\" # 进程命令行 - \"username\" # 用户名

        :return: The white_field of this AlarmWhiteListResponseInfo.
        :rtype: str
        """
        return self._white_field

    @white_field.setter
    def white_field(self, white_field):
        r"""Sets the white_field of this AlarmWhiteListResponseInfo.

        加白字段，包含如下: - \"file/process hash\" # 进程/文件hash - \"file_path\" # 文件路径 - \"process_path\" # 进程路径 - \"login_ip\" # 登录ip - \"reg_key\" #注册表key - \"process_cmdline\" # 进程命令行 - \"username\" # 用户名

        :param white_field: The white_field of this AlarmWhiteListResponseInfo.
        :type white_field: str
        """
        self._white_field = white_field

    @property
    def field_value(self):
        r"""Gets the field_value of this AlarmWhiteListResponseInfo.

        加白字段值

        :return: The field_value of this AlarmWhiteListResponseInfo.
        :rtype: str
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        r"""Sets the field_value of this AlarmWhiteListResponseInfo.

        加白字段值

        :param field_value: The field_value of this AlarmWhiteListResponseInfo.
        :type field_value: str
        """
        self._field_value = field_value

    @property
    def judge_type(self):
        r"""Gets the judge_type of this AlarmWhiteListResponseInfo.

        通配符，包含如下: - \"equal\" # 相等 - \"contain\" # 包含

        :return: The judge_type of this AlarmWhiteListResponseInfo.
        :rtype: str
        """
        return self._judge_type

    @judge_type.setter
    def judge_type(self, judge_type):
        r"""Sets the judge_type of this AlarmWhiteListResponseInfo.

        通配符，包含如下: - \"equal\" # 相等 - \"contain\" # 包含

        :param judge_type: The judge_type of this AlarmWhiteListResponseInfo.
        :type judge_type: str
        """
        self._judge_type = judge_type

    @property
    def update_time(self):
        r"""Gets the update_time of this AlarmWhiteListResponseInfo.

        事件白名单更新时间，毫秒

        :return: The update_time of this AlarmWhiteListResponseInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AlarmWhiteListResponseInfo.

        事件白名单更新时间，毫秒

        :param update_time: The update_time of this AlarmWhiteListResponseInfo.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, AlarmWhiteListResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
