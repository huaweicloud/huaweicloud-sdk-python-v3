# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveAlarmWhiteListRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_list': 'list[AlarmWhiteListRequestInfo]',
        'restore_alarm': 'bool',
        'delete_all': 'bool',
        'event_type': 'int'
    }

    attribute_map = {
        'data_list': 'data_list',
        'restore_alarm': 'restore_alarm',
        'delete_all': 'delete_all',
        'event_type': 'event_type'
    }

    def __init__(self, data_list=None, restore_alarm=None, delete_all=None, event_type=None):
        r"""RemoveAlarmWhiteListRequestInfo

        The model defined in huaweicloud sdk

        :param data_list: **参数解释** : \&quot;删除告警白名单详情\&quot; 删除条件以data_list优先： 1、删除具体某些白名单时，data_list必需，delete_all可以不填。（data_list内hash、description、event_type必需，确定要删除白名单规则时delete_white_rule必须为ture） 2、删除所有白名单时（delete_all 必须为true），data_list一定不要传。 **约束限制** : 不涉及 **取值范围** : 最小值0，最大值100 **默认取值** : 不涉及 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.AlarmWhiteListRequestInfo`]
        :param restore_alarm: **参数解释**: 是否需要恢复相关告警 **约束限制**: 不涉及 **取值范围**: - true ：恢复告警 - false ：不恢复告警  **默认取值**: false
        :type restore_alarm: bool
        :param delete_all: **参数解释**: 是否删除所有白名单内容 1、删除所有白名单时，必须填。删除所有某种类型白名单时，请同时填写event_type参数 2、删除具体某些白名单时，请填写data_list。 **约束限制**: 不涉及 **取值范围**: - true ：删除所有白名单内容 - false ：不删除所有白名单内容  **默认取值**: false 
        :type delete_all: bool
        :param event_type: **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 
        :type event_type: int
        """
        
        

        self._data_list = None
        self._restore_alarm = None
        self._delete_all = None
        self._event_type = None
        self.discriminator = None

        if data_list is not None:
            self.data_list = data_list
        if restore_alarm is not None:
            self.restore_alarm = restore_alarm
        if delete_all is not None:
            self.delete_all = delete_all
        if event_type is not None:
            self.event_type = event_type

    @property
    def data_list(self):
        r"""Gets the data_list of this RemoveAlarmWhiteListRequestInfo.

        **参数解释** : \"删除告警白名单详情\" 删除条件以data_list优先： 1、删除具体某些白名单时，data_list必需，delete_all可以不填。（data_list内hash、description、event_type必需，确定要删除白名单规则时delete_white_rule必须为ture） 2、删除所有白名单时（delete_all 必须为true），data_list一定不要传。 **约束限制** : 不涉及 **取值范围** : 最小值0，最大值100 **默认取值** : 不涉及 

        :return: The data_list of this RemoveAlarmWhiteListRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AlarmWhiteListRequestInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this RemoveAlarmWhiteListRequestInfo.

        **参数解释** : \"删除告警白名单详情\" 删除条件以data_list优先： 1、删除具体某些白名单时，data_list必需，delete_all可以不填。（data_list内hash、description、event_type必需，确定要删除白名单规则时delete_white_rule必须为ture） 2、删除所有白名单时（delete_all 必须为true），data_list一定不要传。 **约束限制** : 不涉及 **取值范围** : 最小值0，最大值100 **默认取值** : 不涉及 

        :param data_list: The data_list of this RemoveAlarmWhiteListRequestInfo.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.AlarmWhiteListRequestInfo`]
        """
        self._data_list = data_list

    @property
    def restore_alarm(self):
        r"""Gets the restore_alarm of this RemoveAlarmWhiteListRequestInfo.

        **参数解释**: 是否需要恢复相关告警 **约束限制**: 不涉及 **取值范围**: - true ：恢复告警 - false ：不恢复告警  **默认取值**: false

        :return: The restore_alarm of this RemoveAlarmWhiteListRequestInfo.
        :rtype: bool
        """
        return self._restore_alarm

    @restore_alarm.setter
    def restore_alarm(self, restore_alarm):
        r"""Sets the restore_alarm of this RemoveAlarmWhiteListRequestInfo.

        **参数解释**: 是否需要恢复相关告警 **约束限制**: 不涉及 **取值范围**: - true ：恢复告警 - false ：不恢复告警  **默认取值**: false

        :param restore_alarm: The restore_alarm of this RemoveAlarmWhiteListRequestInfo.
        :type restore_alarm: bool
        """
        self._restore_alarm = restore_alarm

    @property
    def delete_all(self):
        r"""Gets the delete_all of this RemoveAlarmWhiteListRequestInfo.

        **参数解释**: 是否删除所有白名单内容 1、删除所有白名单时，必须填。删除所有某种类型白名单时，请同时填写event_type参数 2、删除具体某些白名单时，请填写data_list。 **约束限制**: 不涉及 **取值范围**: - true ：删除所有白名单内容 - false ：不删除所有白名单内容  **默认取值**: false 

        :return: The delete_all of this RemoveAlarmWhiteListRequestInfo.
        :rtype: bool
        """
        return self._delete_all

    @delete_all.setter
    def delete_all(self, delete_all):
        r"""Sets the delete_all of this RemoveAlarmWhiteListRequestInfo.

        **参数解释**: 是否删除所有白名单内容 1、删除所有白名单时，必须填。删除所有某种类型白名单时，请同时填写event_type参数 2、删除具体某些白名单时，请填写data_list。 **约束限制**: 不涉及 **取值范围**: - true ：删除所有白名单内容 - false ：不删除所有白名单内容  **默认取值**: false 

        :param delete_all: The delete_all of this RemoveAlarmWhiteListRequestInfo.
        :type delete_all: bool
        """
        self._delete_all = delete_all

    @property
    def event_type(self):
        r"""Gets the event_type of this RemoveAlarmWhiteListRequestInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 

        :return: The event_type of this RemoveAlarmWhiteListRequestInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this RemoveAlarmWhiteListRequestInfo.

        **参数解释**： 事件类型 **取值范围**：   - 1001：通用恶意软件   - 1002：病毒   - 1003：蠕虫   - 1004：木马   - 1005：僵尸网络   - 1006：后门   - 1010：Rootkit   - 1011：勒索软件   - 1012：黑客工具   - 1015：Webshell   - 1016：挖矿   - 1017：反弹Shell   - 2001：一般漏洞利用   - 2012：远程代码执行   - 2047：Redis漏洞利用   - 2048：Hadoop漏洞利用   - 2049：MySQL漏洞利用   - 3002：文件提权   - 3003：进程提权   - 3004：关键文件变更   - 3005：文件/目录变更   - 3007：进程异常行为   - 3015：高危命令执行   - 3018：异常Shell   - 3027：Crontab可疑任务   - 3029：系统安全防护被禁用   - 3030：备份删除   - 3031：异常注册表操作   - 3036：容器镜像阻断   - 4002：暴力破解   - 4004：异常登录   - 4006：非法系统账号   - 4014：用户账号添加   - 4020：用户密码窃取   - 6002：端口扫描   - 6003：主机扫描   - 13001：Kubernetes事件删除   - 13002：Pod异常行为   - 13003：枚举用户信息   - 13004：绑定集群用户角色 

        :param event_type: The event_type of this RemoveAlarmWhiteListRequestInfo.
        :type event_type: int
        """
        self._event_type = event_type

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
        if not isinstance(other, RemoveAlarmWhiteListRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
