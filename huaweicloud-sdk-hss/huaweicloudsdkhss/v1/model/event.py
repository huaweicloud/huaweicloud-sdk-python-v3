# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Event:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'event_type': 'str',
        'occur_time': 'int',
        'handle_time': 'int',
        'handle_status': 'str',
        'handle_method': 'str',
        'append_info': 'object'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'event_type': 'event_type',
        'occur_time': 'occur_time',
        'handle_time': 'handle_time',
        'handle_status': 'handle_status',
        'handle_method': 'handle_method',
        'append_info': 'append_info'
    }

    def __init__(self, host_id=None, host_name=None, event_type=None, occur_time=None, handle_time=None, handle_status=None, handle_method=None, append_info=None):
        """Event

        The model defined in huaweicloud sdk

        :param host_id: 云主机id
        :type host_id: str
        :param host_name: 云主机名称
        :type host_name: str
        :param event_type: 事件类型，包含如下:   - Abnormal Login : 账户异常登录   - Invalid System Account : 风险账号   - Brute Force Cracking : 账号暴力破解   - System Start Script Change : 自启动检测   - Process Abnormal Activity : 进程异常行为   - Process Privilege Escalation : 进程提权操作   - File Privilege Escalation : 文件提权操作   - General Malware : 恶意程序（云查杀）   - Abnormal Shell : 异常shell   - Reverse Shell : 反弹Shell   - High-Risk Command Execution : 高危命令执行   - Key File Change : 关键文件变更   - Webshell : 网站后门
        :type event_type: str
        :param occur_time: 发生时间，毫秒
        :type occur_time: int
        :param handle_time: 处理时间，毫秒
        :type handle_time: int
        :param handle_status: 处理状态，包含如下类型：   - \&quot;unhandled\&quot;：未处理   - \&quot;handled\&quot;：已处理
        :type handle_status: str
        :param handle_method: 处理方式，包含如下类型：   - \&quot;mark_as_handled\&quot; ： 手动处理   - \&quot;ignore\&quot; ： 忽略   - \&quot;add_to_alarm_whitelist\&quot; ：加入告警白名单   - \&quot;add_to_login_whitelist\&quot; ：加入登录白名单   - \&quot;isolate_and_kill\&quot; ：隔离查杀
        :type handle_method: str
        :param append_info: 事件详细信息，json格式
        :type append_info: object
        """
        
        

        self._host_id = None
        self._host_name = None
        self._event_type = None
        self._occur_time = None
        self._handle_time = None
        self._handle_status = None
        self._handle_method = None
        self._append_info = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if event_type is not None:
            self.event_type = event_type
        if occur_time is not None:
            self.occur_time = occur_time
        if handle_time is not None:
            self.handle_time = handle_time
        if handle_status is not None:
            self.handle_status = handle_status
        if handle_method is not None:
            self.handle_method = handle_method
        if append_info is not None:
            self.append_info = append_info

    @property
    def host_id(self):
        """Gets the host_id of this Event.

        云主机id

        :return: The host_id of this Event.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this Event.

        云主机id

        :param host_id: The host_id of this Event.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this Event.

        云主机名称

        :return: The host_name of this Event.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this Event.

        云主机名称

        :param host_name: The host_name of this Event.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def event_type(self):
        """Gets the event_type of this Event.

        事件类型，包含如下:   - Abnormal Login : 账户异常登录   - Invalid System Account : 风险账号   - Brute Force Cracking : 账号暴力破解   - System Start Script Change : 自启动检测   - Process Abnormal Activity : 进程异常行为   - Process Privilege Escalation : 进程提权操作   - File Privilege Escalation : 文件提权操作   - General Malware : 恶意程序（云查杀）   - Abnormal Shell : 异常shell   - Reverse Shell : 反弹Shell   - High-Risk Command Execution : 高危命令执行   - Key File Change : 关键文件变更   - Webshell : 网站后门

        :return: The event_type of this Event.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Event.

        事件类型，包含如下:   - Abnormal Login : 账户异常登录   - Invalid System Account : 风险账号   - Brute Force Cracking : 账号暴力破解   - System Start Script Change : 自启动检测   - Process Abnormal Activity : 进程异常行为   - Process Privilege Escalation : 进程提权操作   - File Privilege Escalation : 文件提权操作   - General Malware : 恶意程序（云查杀）   - Abnormal Shell : 异常shell   - Reverse Shell : 反弹Shell   - High-Risk Command Execution : 高危命令执行   - Key File Change : 关键文件变更   - Webshell : 网站后门

        :param event_type: The event_type of this Event.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def occur_time(self):
        """Gets the occur_time of this Event.

        发生时间，毫秒

        :return: The occur_time of this Event.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        """Sets the occur_time of this Event.

        发生时间，毫秒

        :param occur_time: The occur_time of this Event.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def handle_time(self):
        """Gets the handle_time of this Event.

        处理时间，毫秒

        :return: The handle_time of this Event.
        :rtype: int
        """
        return self._handle_time

    @handle_time.setter
    def handle_time(self, handle_time):
        """Sets the handle_time of this Event.

        处理时间，毫秒

        :param handle_time: The handle_time of this Event.
        :type handle_time: int
        """
        self._handle_time = handle_time

    @property
    def handle_status(self):
        """Gets the handle_status of this Event.

        处理状态，包含如下类型：   - \"unhandled\"：未处理   - \"handled\"：已处理

        :return: The handle_status of this Event.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        """Sets the handle_status of this Event.

        处理状态，包含如下类型：   - \"unhandled\"：未处理   - \"handled\"：已处理

        :param handle_status: The handle_status of this Event.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def handle_method(self):
        """Gets the handle_method of this Event.

        处理方式，包含如下类型：   - \"mark_as_handled\" ： 手动处理   - \"ignore\" ： 忽略   - \"add_to_alarm_whitelist\" ：加入告警白名单   - \"add_to_login_whitelist\" ：加入登录白名单   - \"isolate_and_kill\" ：隔离查杀

        :return: The handle_method of this Event.
        :rtype: str
        """
        return self._handle_method

    @handle_method.setter
    def handle_method(self, handle_method):
        """Sets the handle_method of this Event.

        处理方式，包含如下类型：   - \"mark_as_handled\" ： 手动处理   - \"ignore\" ： 忽略   - \"add_to_alarm_whitelist\" ：加入告警白名单   - \"add_to_login_whitelist\" ：加入登录白名单   - \"isolate_and_kill\" ：隔离查杀

        :param handle_method: The handle_method of this Event.
        :type handle_method: str
        """
        self._handle_method = handle_method

    @property
    def append_info(self):
        """Gets the append_info of this Event.

        事件详细信息，json格式

        :return: The append_info of this Event.
        :rtype: object
        """
        return self._append_info

    @append_info.setter
    def append_info(self, append_info):
        """Sets the append_info of this Event.

        事件详细信息，json格式

        :param append_info: The append_info of this Event.
        :type append_info: object
        """
        self._append_info = append_info

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
