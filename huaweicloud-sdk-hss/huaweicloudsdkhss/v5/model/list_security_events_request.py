# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'last_days': 'int',
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'container_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'event_types': 'list[int]',
        'handle_status': 'str',
        'severity': 'str',
        'category': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'last_days': 'last_days',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'container_name': 'container_name',
        'offset': 'offset',
        'limit': 'limit',
        'event_types': 'event_types',
        'handle_status': 'handle_status',
        'severity': 'severity',
        'category': 'category',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, region=None, enterprise_project_id=None, last_days=None, host_name=None, host_id=None, private_ip=None, container_name=None, offset=None, limit=None, event_types=None, handle_status=None, severity=None, category=None, begin_time=None, end_time=None):
        """ListSecurityEventsRequest

        The model defined in huaweicloud sdk

        :param region: region id
        :type region: str
        :param enterprise_project_id: 租户企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param last_days: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥
        :type last_days: int
        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 服务器ID
        :type host_id: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param container_name: 容器名称
        :type container_name: str
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param event_types: 事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号
        :type event_types: list[int]
        :param handle_status: 处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理
        :type handle_status: str
        :param severity: 威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急
        :type severity: str
        :param category: 事件类别，包含如下:   - host : 主机安全事件   - container : 容器安全事件
        :type category: str
        :param begin_time: 自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥
        :type begin_time: str
        :param end_time: 自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥
        :type end_time: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._last_days = None
        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._container_name = None
        self._offset = None
        self._limit = None
        self._event_types = None
        self._handle_status = None
        self._severity = None
        self._category = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if last_days is not None:
            self.last_days = last_days
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if private_ip is not None:
            self.private_ip = private_ip
        if container_name is not None:
            self.container_name = container_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if event_types is not None:
            self.event_types = event_types
        if handle_status is not None:
            self.handle_status = handle_status
        if severity is not None:
            self.severity = severity
        self.category = category
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def region(self):
        """Gets the region of this ListSecurityEventsRequest.

        region id

        :return: The region of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListSecurityEventsRequest.

        region id

        :param region: The region of this ListSecurityEventsRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListSecurityEventsRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListSecurityEventsRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListSecurityEventsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def last_days(self):
        """Gets the last_days of this ListSecurityEventsRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :return: The last_days of this ListSecurityEventsRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        """Sets the last_days of this ListSecurityEventsRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :param last_days: The last_days of this ListSecurityEventsRequest.
        :type last_days: int
        """
        self._last_days = last_days

    @property
    def host_name(self):
        """Gets the host_name of this ListSecurityEventsRequest.

        服务器名称

        :return: The host_name of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListSecurityEventsRequest.

        服务器名称

        :param host_name: The host_name of this ListSecurityEventsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        """Gets the host_id of this ListSecurityEventsRequest.

        服务器ID

        :return: The host_id of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListSecurityEventsRequest.

        服务器ID

        :param host_id: The host_id of this ListSecurityEventsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        """Gets the private_ip of this ListSecurityEventsRequest.

        服务器私有IP

        :return: The private_ip of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ListSecurityEventsRequest.

        服务器私有IP

        :param private_ip: The private_ip of this ListSecurityEventsRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def container_name(self):
        """Gets the container_name of this ListSecurityEventsRequest.

        容器名称

        :return: The container_name of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this ListSecurityEventsRequest.

        容器名称

        :param container_name: The container_name of this ListSecurityEventsRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def offset(self):
        """Gets the offset of this ListSecurityEventsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListSecurityEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSecurityEventsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListSecurityEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSecurityEventsRequest.

        每页显示个数

        :return: The limit of this ListSecurityEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecurityEventsRequest.

        每页显示个数

        :param limit: The limit of this ListSecurityEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def event_types(self):
        """Gets the event_types of this ListSecurityEventsRequest.

        事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号

        :return: The event_types of this ListSecurityEventsRequest.
        :rtype: list[int]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this ListSecurityEventsRequest.

        事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号

        :param event_types: The event_types of this ListSecurityEventsRequest.
        :type event_types: list[int]
        """
        self._event_types = event_types

    @property
    def handle_status(self):
        """Gets the handle_status of this ListSecurityEventsRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :return: The handle_status of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        """Sets the handle_status of this ListSecurityEventsRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :param handle_status: The handle_status of this ListSecurityEventsRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def severity(self):
        """Gets the severity of this ListSecurityEventsRequest.

        威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :return: The severity of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ListSecurityEventsRequest.

        威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :param severity: The severity of this ListSecurityEventsRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def category(self):
        """Gets the category of this ListSecurityEventsRequest.

        事件类别，包含如下:   - host : 主机安全事件   - container : 容器安全事件

        :return: The category of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ListSecurityEventsRequest.

        事件类别，包含如下:   - host : 主机安全事件   - container : 容器安全事件

        :param category: The category of this ListSecurityEventsRequest.
        :type category: str
        """
        self._category = category

    @property
    def begin_time(self):
        """Gets the begin_time of this ListSecurityEventsRequest.

        自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :return: The begin_time of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListSecurityEventsRequest.

        自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :param begin_time: The begin_time of this ListSecurityEventsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListSecurityEventsRequest.

        自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :return: The end_time of this ListSecurityEventsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListSecurityEventsRequest.

        自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :param end_time: The end_time of this ListSecurityEventsRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListSecurityEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
