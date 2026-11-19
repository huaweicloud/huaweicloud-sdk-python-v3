# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHoneypotEventsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'begin_time': 'int',
        'end_time': 'int',
        'last_days': 'int',
        'host_name': 'str',
        'host_id': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'last_days': 'last_days',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'severity': 'severity'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, begin_time=None, end_time=None, last_days=None, host_name=None, host_id=None, public_ip=None, private_ip=None, severity=None):
        r"""ListHoneypotEventsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param begin_time: **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 
        :type begin_time: int
        :param end_time: **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 
        :type end_time: int
        :param last_days: **参数解释**: 查询时间范围天数 **约束限制**: 与begin_time、end_time互斥，不可同时传参，优先按last_days筛选 **取值范围**: 最小值1，最大值90（支持查询近90天内任务） **默认取值**: 不涉及 
        :type last_days: int
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param public_ip: **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 
        :type public_ip: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param severity: 威胁等级，包含如下:   - Security：安全   - Low：低危   - Medium：中危   - High：高危   - Critical：危急
        :type severity: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._begin_time = None
        self._end_time = None
        self._last_days = None
        self._host_name = None
        self._host_id = None
        self._public_ip = None
        self._private_ip = None
        self._severity = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if last_days is not None:
            self.last_days = last_days
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if severity is not None:
            self.severity = severity

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListHoneypotEventsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListHoneypotEventsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListHoneypotEventsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListHoneypotEventsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListHoneypotEventsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListHoneypotEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHoneypotEventsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListHoneypotEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListHoneypotEventsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListHoneypotEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHoneypotEventsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListHoneypotEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListHoneypotEventsRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :return: The begin_time of this ListHoneypotEventsRequest.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListHoneypotEventsRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :param begin_time: The begin_time of this ListHoneypotEventsRequest.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListHoneypotEventsRequest.

        **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :return: The end_time of this ListHoneypotEventsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListHoneypotEventsRequest.

        **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :param end_time: The end_time of this ListHoneypotEventsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def last_days(self):
        r"""Gets the last_days of this ListHoneypotEventsRequest.

        **参数解释**: 查询时间范围天数 **约束限制**: 与begin_time、end_time互斥，不可同时传参，优先按last_days筛选 **取值范围**: 最小值1，最大值90（支持查询近90天内任务） **默认取值**: 不涉及 

        :return: The last_days of this ListHoneypotEventsRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListHoneypotEventsRequest.

        **参数解释**: 查询时间范围天数 **约束限制**: 与begin_time、end_time互斥，不可同时传参，优先按last_days筛选 **取值范围**: 最小值1，最大值90（支持查询近90天内任务） **默认取值**: 不涉及 

        :param last_days: The last_days of this ListHoneypotEventsRequest.
        :type last_days: int
        """
        self._last_days = last_days

    @property
    def host_name(self):
        r"""Gets the host_name of this ListHoneypotEventsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListHoneypotEventsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListHoneypotEventsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListHoneypotEventsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListHoneypotEventsRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListHoneypotEventsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListHoneypotEventsRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListHoneypotEventsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListHoneypotEventsRequest.

        **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 

        :return: The public_ip of this ListHoneypotEventsRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListHoneypotEventsRequest.

        **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 

        :param public_ip: The public_ip of this ListHoneypotEventsRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListHoneypotEventsRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ListHoneypotEventsRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListHoneypotEventsRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListHoneypotEventsRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def severity(self):
        r"""Gets the severity of this ListHoneypotEventsRequest.

        威胁等级，包含如下:   - Security：安全   - Low：低危   - Medium：中危   - High：高危   - Critical：危急

        :return: The severity of this ListHoneypotEventsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListHoneypotEventsRequest.

        威胁等级，包含如下:   - Security：安全   - Low：低危   - Medium：中危   - High：高危   - Critical：危急

        :param severity: The severity of this ListHoneypotEventsRequest.
        :type severity: str
        """
        self._severity = severity

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
        if not isinstance(other, ListHoneypotEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
