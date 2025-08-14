# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmWhiteListRequestInfo:

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
        'hash': 'str',
        'description': 'str',
        'delete_white_rule': 'bool',
        'white_field': 'str',
        'judge_type': 'str',
        'field_value': 'str',
        'file_hash': 'str',
        'file_path': 'str'
    }

    attribute_map = {
        'event_type': 'event_type',
        'hash': 'hash',
        'description': 'description',
        'delete_white_rule': 'delete_white_rule',
        'white_field': 'white_field',
        'judge_type': 'judge_type',
        'field_value': 'field_value',
        'file_hash': 'file_hash',
        'file_path': 'file_path'
    }

    def __init__(self, event_type=None, hash=None, description=None, delete_white_rule=None, white_field=None, judge_type=None, field_value=None, file_hash=None, file_path=None):
        r"""AlarmWhiteListRequestInfo

        The model defined in huaweicloud sdk

        :param event_type: **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 
        :type event_type: int
        :param hash: **参数解释**: 事件白名单SHA256 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及
        :type hash: str
        :param description: **参数解释**: 描述信息。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及
        :type description: str
        :param delete_white_rule: **参数解释**: 是否删除告警白名单规则(仅删除的白名单是规则类型时使用) **约束限制**: 不涉及 **取值范围**: - true：删除告警白名单规则 - false: 不删除告警白名单规则  **默认取值**: 不涉及
        :type delete_white_rule: bool
        :param white_field: **参数解释**: 加白字段 **约束限制**: 不涉及 **取值范围**: - \&quot;file_path\&quot;：文件路径 - \&quot;process_path\&quot;：进程路径 - \&quot;login_ip\&quot;：登录ip - \&quot;reg_key\&quot;：注册表key - \&quot;process_cmdline\&quot;： 进程命令行 - \&quot;username\&quot;： 用户名  **默认取值**: 不涉及
        :type white_field: str
        :param judge_type: **参数解释**: 通配符 **约束限制**: 不涉及 **取值范围**:   - \&quot;equal\&quot;： 相等   - \&quot;not_equal\&quot;：不相等   - \&quot;contain\&quot;： 包含   - \&quot;not_contain\&quot;： 不包含  **默认取值**: 不涉及
        :type judge_type: str
        :param field_value: **参数解释**: 加白字段值 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及
        :type field_value: str
        :param file_hash: **参数解释**: 文件哈希 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及
        :type file_hash: str
        :param file_path: **参数解释**: 文件路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及
        :type file_path: str
        """
        
        

        self._event_type = None
        self._hash = None
        self._description = None
        self._delete_white_rule = None
        self._white_field = None
        self._judge_type = None
        self._field_value = None
        self._file_hash = None
        self._file_path = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if hash is not None:
            self.hash = hash
        if description is not None:
            self.description = description
        if delete_white_rule is not None:
            self.delete_white_rule = delete_white_rule
        if white_field is not None:
            self.white_field = white_field
        if judge_type is not None:
            self.judge_type = judge_type
        if field_value is not None:
            self.field_value = field_value
        if file_hash is not None:
            self.file_hash = file_hash
        if file_path is not None:
            self.file_path = file_path

    @property
    def event_type(self):
        r"""Gets the event_type of this AlarmWhiteListRequestInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 

        :return: The event_type of this AlarmWhiteListRequestInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this AlarmWhiteListRequestInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 

        :param event_type: The event_type of this AlarmWhiteListRequestInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def hash(self):
        r"""Gets the hash of this AlarmWhiteListRequestInfo.

        **参数解释**: 事件白名单SHA256 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及

        :return: The hash of this AlarmWhiteListRequestInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this AlarmWhiteListRequestInfo.

        **参数解释**: 事件白名单SHA256 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及

        :param hash: The hash of this AlarmWhiteListRequestInfo.
        :type hash: str
        """
        self._hash = hash

    @property
    def description(self):
        r"""Gets the description of this AlarmWhiteListRequestInfo.

        **参数解释**: 描述信息。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及

        :return: The description of this AlarmWhiteListRequestInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlarmWhiteListRequestInfo.

        **参数解释**: 描述信息。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64 **默认取值**: 不涉及

        :param description: The description of this AlarmWhiteListRequestInfo.
        :type description: str
        """
        self._description = description

    @property
    def delete_white_rule(self):
        r"""Gets the delete_white_rule of this AlarmWhiteListRequestInfo.

        **参数解释**: 是否删除告警白名单规则(仅删除的白名单是规则类型时使用) **约束限制**: 不涉及 **取值范围**: - true：删除告警白名单规则 - false: 不删除告警白名单规则  **默认取值**: 不涉及

        :return: The delete_white_rule of this AlarmWhiteListRequestInfo.
        :rtype: bool
        """
        return self._delete_white_rule

    @delete_white_rule.setter
    def delete_white_rule(self, delete_white_rule):
        r"""Sets the delete_white_rule of this AlarmWhiteListRequestInfo.

        **参数解释**: 是否删除告警白名单规则(仅删除的白名单是规则类型时使用) **约束限制**: 不涉及 **取值范围**: - true：删除告警白名单规则 - false: 不删除告警白名单规则  **默认取值**: 不涉及

        :param delete_white_rule: The delete_white_rule of this AlarmWhiteListRequestInfo.
        :type delete_white_rule: bool
        """
        self._delete_white_rule = delete_white_rule

    @property
    def white_field(self):
        r"""Gets the white_field of this AlarmWhiteListRequestInfo.

        **参数解释**: 加白字段 **约束限制**: 不涉及 **取值范围**: - \"file_path\"：文件路径 - \"process_path\"：进程路径 - \"login_ip\"：登录ip - \"reg_key\"：注册表key - \"process_cmdline\"： 进程命令行 - \"username\"： 用户名  **默认取值**: 不涉及

        :return: The white_field of this AlarmWhiteListRequestInfo.
        :rtype: str
        """
        return self._white_field

    @white_field.setter
    def white_field(self, white_field):
        r"""Sets the white_field of this AlarmWhiteListRequestInfo.

        **参数解释**: 加白字段 **约束限制**: 不涉及 **取值范围**: - \"file_path\"：文件路径 - \"process_path\"：进程路径 - \"login_ip\"：登录ip - \"reg_key\"：注册表key - \"process_cmdline\"： 进程命令行 - \"username\"： 用户名  **默认取值**: 不涉及

        :param white_field: The white_field of this AlarmWhiteListRequestInfo.
        :type white_field: str
        """
        self._white_field = white_field

    @property
    def judge_type(self):
        r"""Gets the judge_type of this AlarmWhiteListRequestInfo.

        **参数解释**: 通配符 **约束限制**: 不涉及 **取值范围**:   - \"equal\"： 相等   - \"not_equal\"：不相等   - \"contain\"： 包含   - \"not_contain\"： 不包含  **默认取值**: 不涉及

        :return: The judge_type of this AlarmWhiteListRequestInfo.
        :rtype: str
        """
        return self._judge_type

    @judge_type.setter
    def judge_type(self, judge_type):
        r"""Sets the judge_type of this AlarmWhiteListRequestInfo.

        **参数解释**: 通配符 **约束限制**: 不涉及 **取值范围**:   - \"equal\"： 相等   - \"not_equal\"：不相等   - \"contain\"： 包含   - \"not_contain\"： 不包含  **默认取值**: 不涉及

        :param judge_type: The judge_type of this AlarmWhiteListRequestInfo.
        :type judge_type: str
        """
        self._judge_type = judge_type

    @property
    def field_value(self):
        r"""Gets the field_value of this AlarmWhiteListRequestInfo.

        **参数解释**: 加白字段值 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及

        :return: The field_value of this AlarmWhiteListRequestInfo.
        :rtype: str
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        r"""Sets the field_value of this AlarmWhiteListRequestInfo.

        **参数解释**: 加白字段值 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及

        :param field_value: The field_value of this AlarmWhiteListRequestInfo.
        :type field_value: str
        """
        self._field_value = field_value

    @property
    def file_hash(self):
        r"""Gets the file_hash of this AlarmWhiteListRequestInfo.

        **参数解释**: 文件哈希 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及

        :return: The file_hash of this AlarmWhiteListRequestInfo.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        r"""Sets the file_hash of this AlarmWhiteListRequestInfo.

        **参数解释**: 文件哈希 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及

        :param file_hash: The file_hash of this AlarmWhiteListRequestInfo.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def file_path(self):
        r"""Gets the file_path of this AlarmWhiteListRequestInfo.

        **参数解释**: 文件路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及

        :return: The file_path of this AlarmWhiteListRequestInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this AlarmWhiteListRequestInfo.

        **参数解释**: 文件路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及

        :param file_path: The file_path of this AlarmWhiteListRequestInfo.
        :type file_path: str
        """
        self._file_path = file_path

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
        if not isinstance(other, AlarmWhiteListRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
