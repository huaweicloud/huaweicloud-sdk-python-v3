# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateEventRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_class_id': 'str',
        'event_id': 'str',
        'event_type': 'int',
        'occur_time': 'int',
        'operate_detail_list': 'list[EventDetailRequestInfo]'
    }

    attribute_map = {
        'event_class_id': 'event_class_id',
        'event_id': 'event_id',
        'event_type': 'event_type',
        'occur_time': 'occur_time',
        'operate_detail_list': 'operate_detail_list'
    }

    def __init__(self, event_class_id=None, event_id=None, event_type=None, occur_time=None, operate_detail_list=None):
        """OperateEventRequestInfo

        The model defined in huaweicloud sdk

        :param event_class_id: 事件分类，包含如下:   - container_1001 : 容器命名空间   - container_1002 : 容器开放端口   - container_1003 : 容器安全选项   - container_1004 : 容器挂载目录   - containerescape_0001 : 容器高危系统调用   - containerescape_0002 : Shocker攻击   - containerescape_0003 : DirtCow攻击   - containerescape_0004 : 容器文件逃逸攻击   - dockerfile_001 : 用户自定义容器保护文件被修改   - dockerfile_002 : 容器文件系统可执行文件被修改   - dockerproc_001 : 容器进程异常事件上报   - fileprotect_0001 : 文件提权   - fileprotect_0002 : 关键文件变更   - fileprotect_0003 : 关键文件路径变更   - fileprotect_0004 : 文件目录变更   - login_0001 : 尝试暴力破解   - login_0002 : 爆破成功   - login_1001 : 登录成功   - login_1002 : 异地登录   - login_1003 : 弱口令   - malware_0001 : shell变更事件上报   - malware_0002 : 反弹shell事件上报   - malware_1001 : 恶意程序   - procdet_0001 : 进程异常行为检测   - procdet_0002 : 进程提权   - procreport_0001 : 危险命令   - user_1001 : 账号变更   - user_1002 : 风险账号   - vmescape_0001 : 虚拟机敏感命令执行   - vmescape_0002 : 虚拟化进程访问敏感文件   - vmescape_0003 : 虚拟机异常端口访问   - webshell_0001 : 网站后门   - network_1001 : 恶意挖矿   - network_1002 : 对外DDoS攻击   - network_1003 : 恶意扫描   - network_1004 : 敏感区域攻击   - crontab_1001 : Crontab可疑任务   - vul_exploit_0001 : Redis漏洞利用攻击   - vul_exploit_0002 : Hadoop漏洞利用攻击   - vul_exploit_0003 : MySQL漏洞利用攻击
        :type event_class_id: str
        :param event_id: 事件编号
        :type event_id: str
        :param event_type: 事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号
        :type event_type: int
        :param occur_time: 发生时间，毫秒
        :type occur_time: int
        :param operate_detail_list: 操作详情信息列表
        :type operate_detail_list: list[:class:`huaweicloudsdkhss.v5.EventDetailRequestInfo`]
        """
        
        

        self._event_class_id = None
        self._event_id = None
        self._event_type = None
        self._occur_time = None
        self._operate_detail_list = None
        self.discriminator = None

        if event_class_id is not None:
            self.event_class_id = event_class_id
        if event_id is not None:
            self.event_id = event_id
        if event_type is not None:
            self.event_type = event_type
        if occur_time is not None:
            self.occur_time = occur_time
        if operate_detail_list is not None:
            self.operate_detail_list = operate_detail_list

    @property
    def event_class_id(self):
        """Gets the event_class_id of this OperateEventRequestInfo.

        事件分类，包含如下:   - container_1001 : 容器命名空间   - container_1002 : 容器开放端口   - container_1003 : 容器安全选项   - container_1004 : 容器挂载目录   - containerescape_0001 : 容器高危系统调用   - containerescape_0002 : Shocker攻击   - containerescape_0003 : DirtCow攻击   - containerescape_0004 : 容器文件逃逸攻击   - dockerfile_001 : 用户自定义容器保护文件被修改   - dockerfile_002 : 容器文件系统可执行文件被修改   - dockerproc_001 : 容器进程异常事件上报   - fileprotect_0001 : 文件提权   - fileprotect_0002 : 关键文件变更   - fileprotect_0003 : 关键文件路径变更   - fileprotect_0004 : 文件目录变更   - login_0001 : 尝试暴力破解   - login_0002 : 爆破成功   - login_1001 : 登录成功   - login_1002 : 异地登录   - login_1003 : 弱口令   - malware_0001 : shell变更事件上报   - malware_0002 : 反弹shell事件上报   - malware_1001 : 恶意程序   - procdet_0001 : 进程异常行为检测   - procdet_0002 : 进程提权   - procreport_0001 : 危险命令   - user_1001 : 账号变更   - user_1002 : 风险账号   - vmescape_0001 : 虚拟机敏感命令执行   - vmescape_0002 : 虚拟化进程访问敏感文件   - vmescape_0003 : 虚拟机异常端口访问   - webshell_0001 : 网站后门   - network_1001 : 恶意挖矿   - network_1002 : 对外DDoS攻击   - network_1003 : 恶意扫描   - network_1004 : 敏感区域攻击   - crontab_1001 : Crontab可疑任务   - vul_exploit_0001 : Redis漏洞利用攻击   - vul_exploit_0002 : Hadoop漏洞利用攻击   - vul_exploit_0003 : MySQL漏洞利用攻击

        :return: The event_class_id of this OperateEventRequestInfo.
        :rtype: str
        """
        return self._event_class_id

    @event_class_id.setter
    def event_class_id(self, event_class_id):
        """Sets the event_class_id of this OperateEventRequestInfo.

        事件分类，包含如下:   - container_1001 : 容器命名空间   - container_1002 : 容器开放端口   - container_1003 : 容器安全选项   - container_1004 : 容器挂载目录   - containerescape_0001 : 容器高危系统调用   - containerescape_0002 : Shocker攻击   - containerescape_0003 : DirtCow攻击   - containerescape_0004 : 容器文件逃逸攻击   - dockerfile_001 : 用户自定义容器保护文件被修改   - dockerfile_002 : 容器文件系统可执行文件被修改   - dockerproc_001 : 容器进程异常事件上报   - fileprotect_0001 : 文件提权   - fileprotect_0002 : 关键文件变更   - fileprotect_0003 : 关键文件路径变更   - fileprotect_0004 : 文件目录变更   - login_0001 : 尝试暴力破解   - login_0002 : 爆破成功   - login_1001 : 登录成功   - login_1002 : 异地登录   - login_1003 : 弱口令   - malware_0001 : shell变更事件上报   - malware_0002 : 反弹shell事件上报   - malware_1001 : 恶意程序   - procdet_0001 : 进程异常行为检测   - procdet_0002 : 进程提权   - procreport_0001 : 危险命令   - user_1001 : 账号变更   - user_1002 : 风险账号   - vmescape_0001 : 虚拟机敏感命令执行   - vmescape_0002 : 虚拟化进程访问敏感文件   - vmescape_0003 : 虚拟机异常端口访问   - webshell_0001 : 网站后门   - network_1001 : 恶意挖矿   - network_1002 : 对外DDoS攻击   - network_1003 : 恶意扫描   - network_1004 : 敏感区域攻击   - crontab_1001 : Crontab可疑任务   - vul_exploit_0001 : Redis漏洞利用攻击   - vul_exploit_0002 : Hadoop漏洞利用攻击   - vul_exploit_0003 : MySQL漏洞利用攻击

        :param event_class_id: The event_class_id of this OperateEventRequestInfo.
        :type event_class_id: str
        """
        self._event_class_id = event_class_id

    @property
    def event_id(self):
        """Gets the event_id of this OperateEventRequestInfo.

        事件编号

        :return: The event_id of this OperateEventRequestInfo.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this OperateEventRequestInfo.

        事件编号

        :param event_id: The event_id of this OperateEventRequestInfo.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_type(self):
        """Gets the event_type of this OperateEventRequestInfo.

        事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号

        :return: The event_type of this OperateEventRequestInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this OperateEventRequestInfo.

        事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号

        :param event_type: The event_type of this OperateEventRequestInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def occur_time(self):
        """Gets the occur_time of this OperateEventRequestInfo.

        发生时间，毫秒

        :return: The occur_time of this OperateEventRequestInfo.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        """Sets the occur_time of this OperateEventRequestInfo.

        发生时间，毫秒

        :param occur_time: The occur_time of this OperateEventRequestInfo.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def operate_detail_list(self):
        """Gets the operate_detail_list of this OperateEventRequestInfo.

        操作详情信息列表

        :return: The operate_detail_list of this OperateEventRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.EventDetailRequestInfo`]
        """
        return self._operate_detail_list

    @operate_detail_list.setter
    def operate_detail_list(self, operate_detail_list):
        """Sets the operate_detail_list of this OperateEventRequestInfo.

        操作详情信息列表

        :param operate_detail_list: The operate_detail_list of this OperateEventRequestInfo.
        :type operate_detail_list: list[:class:`huaweicloudsdkhss.v5.EventDetailRequestInfo`]
        """
        self._operate_detail_list = operate_detail_list

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
        if not isinstance(other, OperateEventRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
