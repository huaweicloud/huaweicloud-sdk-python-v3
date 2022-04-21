# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'begin_time': 'str',
        'end_time': 'str',
        'host_name': 'str',
        'event_types': 'list[str]',
        'handle_status': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'host_name': 'host_name',
        'event_types': 'event_types',
        'handle_status': 'handle_status',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, begin_time=None, end_time=None, host_name=None, event_types=None, handle_status=None, limit=None, offset=None):
        """ListEventsRequest

        The model defined in huaweicloud sdk

        :param begin_time: 查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天
        :type begin_time: str
        :param end_time: 查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天
        :type end_time: str
        :param host_name: 云主机名称
        :type host_name: str
        :param event_types: 事件类型，包含如下:   - Abnormal Login : 账户异常登录   - Invalid System Account : 风险账号   - Brute Force Cracking : 账号暴力破解   - System Start Script Change : 自启动检测   - Process Abnormal Activity : 进程异常行为   - Process Privilege Escalation : 进程提权操作   - File Privilege Escalation : 文件提权操作   - General Malware : 恶意程序（云查杀）   - Abnormal Shell : 异常shell   - Reverse Shell : 反弹Shell   - High-Risk Command Execution : 高危命令执行   - Key File Change : 关键文件变更   - Webshell : 网站后门
        :type event_types: list[str]
        :param handle_status: 是否已处理，包含如下类型：   - \&quot;unhandled\&quot; ： 未处理   - \&quot;handled\&quot; ： 已处理
        :type handle_status: str
        :param limit: 默认10
        :type limit: int
        :param offset: 默认0
        :type offset: int
        """
        
        

        self._begin_time = None
        self._end_time = None
        self._host_name = None
        self._event_types = None
        self._handle_status = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.begin_time = begin_time
        self.end_time = end_time
        if host_name is not None:
            self.host_name = host_name
        self.event_types = event_types
        if handle_status is not None:
            self.handle_status = handle_status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def begin_time(self):
        """Gets the begin_time of this ListEventsRequest.

        查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天

        :return: The begin_time of this ListEventsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListEventsRequest.

        查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天

        :param begin_time: The begin_time of this ListEventsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListEventsRequest.

        查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天

        :return: The end_time of this ListEventsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListEventsRequest.

        查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天

        :param end_time: The end_time of this ListEventsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def host_name(self):
        """Gets the host_name of this ListEventsRequest.

        云主机名称

        :return: The host_name of this ListEventsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListEventsRequest.

        云主机名称

        :param host_name: The host_name of this ListEventsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def event_types(self):
        """Gets the event_types of this ListEventsRequest.

        事件类型，包含如下:   - Abnormal Login : 账户异常登录   - Invalid System Account : 风险账号   - Brute Force Cracking : 账号暴力破解   - System Start Script Change : 自启动检测   - Process Abnormal Activity : 进程异常行为   - Process Privilege Escalation : 进程提权操作   - File Privilege Escalation : 文件提权操作   - General Malware : 恶意程序（云查杀）   - Abnormal Shell : 异常shell   - Reverse Shell : 反弹Shell   - High-Risk Command Execution : 高危命令执行   - Key File Change : 关键文件变更   - Webshell : 网站后门

        :return: The event_types of this ListEventsRequest.
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this ListEventsRequest.

        事件类型，包含如下:   - Abnormal Login : 账户异常登录   - Invalid System Account : 风险账号   - Brute Force Cracking : 账号暴力破解   - System Start Script Change : 自启动检测   - Process Abnormal Activity : 进程异常行为   - Process Privilege Escalation : 进程提权操作   - File Privilege Escalation : 文件提权操作   - General Malware : 恶意程序（云查杀）   - Abnormal Shell : 异常shell   - Reverse Shell : 反弹Shell   - High-Risk Command Execution : 高危命令执行   - Key File Change : 关键文件变更   - Webshell : 网站后门

        :param event_types: The event_types of this ListEventsRequest.
        :type event_types: list[str]
        """
        self._event_types = event_types

    @property
    def handle_status(self):
        """Gets the handle_status of this ListEventsRequest.

        是否已处理，包含如下类型：   - \"unhandled\" ： 未处理   - \"handled\" ： 已处理

        :return: The handle_status of this ListEventsRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        """Sets the handle_status of this ListEventsRequest.

        是否已处理，包含如下类型：   - \"unhandled\" ： 未处理   - \"handled\" ： 已处理

        :param handle_status: The handle_status of this ListEventsRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def limit(self):
        """Gets the limit of this ListEventsRequest.

        默认10

        :return: The limit of this ListEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEventsRequest.

        默认10

        :param limit: The limit of this ListEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListEventsRequest.

        默认0

        :return: The offset of this ListEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEventsRequest.

        默认0

        :param offset: The offset of this ListEventsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
