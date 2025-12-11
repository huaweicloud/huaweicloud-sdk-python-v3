# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventTopRiskRequest:

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
        'begin_time': 'int',
        'end_time': 'int',
        'last_days': 'int',
        'category': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'container_name': 'str',
        'event_type': 'int',
        'handle_status': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'last_days': 'last_days',
        'category': 'category',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'container_name': 'container_name',
        'event_type': 'event_type',
        'handle_status': 'handle_status',
        'severity': 'severity'
    }

    def __init__(self, region=None, enterprise_project_id=None, begin_time=None, end_time=None, last_days=None, category=None, host_name=None, host_id=None, private_ip=None, container_name=None, event_type=None, handle_status=None, severity=None):
        r"""ListEventTopRiskRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param begin_time: **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 
        :type begin_time: int
        :param end_time: **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 
        :type end_time: int
        :param last_days: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥
        :type last_days: int
        :param category: 事件类别，包含如下:   - host : 主机安全事件   - container : 容器安全事件
        :type category: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 服务器ID
        :type host_id: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param container_name: 容器实例名称
        :type container_name: str
        :param event_type: 事件类型，包含如下:   - 1001 : 通用恶意软件   - 1002 : 病毒   - 1003 : 蠕虫   - 1004 : 木马   - 1005 : 僵尸网络   - 1006 : 后门   - 1010 : Rootkit   - 1011 : 勒索软件   - 1012 ：黑客工具   - 1015 : Webshell   - 1016 : 挖矿   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2012 : 远程代码执行   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 3029 ：系统安全防护被禁用   - 3030 ：备份删除   - 3031 ：异常注册表操作   - 3036 : 容器镜像阻断   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号   - 4014 : 用户账号添加   - 4020 : 用户密码窃取   - 6002 : 端口扫描   - 6003 : 主机扫描   - 13001 : Kubernetes事件删除   - 13002 : Pod异常行为   - 13003 : 枚举用户信息   - 13004 : 绑定集群用户角色
        :type event_type: int
        :param handle_status: 处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理
        :type handle_status: str
        :param severity: 威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急
        :type severity: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._begin_time = None
        self._end_time = None
        self._last_days = None
        self._category = None
        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._container_name = None
        self._event_type = None
        self._handle_status = None
        self._severity = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if last_days is not None:
            self.last_days = last_days
        self.category = category
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if private_ip is not None:
            self.private_ip = private_ip
        if container_name is not None:
            self.container_name = container_name
        if event_type is not None:
            self.event_type = event_type
        if handle_status is not None:
            self.handle_status = handle_status
        if severity is not None:
            self.severity = severity

    @property
    def region(self):
        r"""Gets the region of this ListEventTopRiskRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListEventTopRiskRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListEventTopRiskRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListEventTopRiskRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListEventTopRiskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListEventTopRiskRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListEventTopRiskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListEventTopRiskRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListEventTopRiskRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :return: The begin_time of this ListEventTopRiskRequest.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListEventTopRiskRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 需小于等于end_time，未传end_time时默认查询至当前时间 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :param begin_time: The begin_time of this ListEventTopRiskRequest.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListEventTopRiskRequest.

        **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :return: The end_time of this ListEventTopRiskRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListEventTopRiskRequest.

        **参数解释**: 结束时间，13位时间戳 **约束限制**: 需大于等于begin_time，未传begin_time时默认从时间戳0开始查询 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） **默认取值**: 不涉及 

        :param end_time: The end_time of this ListEventTopRiskRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def last_days(self):
        r"""Gets the last_days of this ListEventTopRiskRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :return: The last_days of this ListEventTopRiskRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListEventTopRiskRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :param last_days: The last_days of this ListEventTopRiskRequest.
        :type last_days: int
        """
        self._last_days = last_days

    @property
    def category(self):
        r"""Gets the category of this ListEventTopRiskRequest.

        事件类别，包含如下:   - host : 主机安全事件   - container : 容器安全事件

        :return: The category of this ListEventTopRiskRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListEventTopRiskRequest.

        事件类别，包含如下:   - host : 主机安全事件   - container : 容器安全事件

        :param category: The category of this ListEventTopRiskRequest.
        :type category: str
        """
        self._category = category

    @property
    def host_name(self):
        r"""Gets the host_name of this ListEventTopRiskRequest.

        服务器名称

        :return: The host_name of this ListEventTopRiskRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListEventTopRiskRequest.

        服务器名称

        :param host_name: The host_name of this ListEventTopRiskRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListEventTopRiskRequest.

        服务器ID

        :return: The host_id of this ListEventTopRiskRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListEventTopRiskRequest.

        服务器ID

        :param host_id: The host_id of this ListEventTopRiskRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListEventTopRiskRequest.

        服务器私有IP

        :return: The private_ip of this ListEventTopRiskRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListEventTopRiskRequest.

        服务器私有IP

        :param private_ip: The private_ip of this ListEventTopRiskRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def container_name(self):
        r"""Gets the container_name of this ListEventTopRiskRequest.

        容器实例名称

        :return: The container_name of this ListEventTopRiskRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListEventTopRiskRequest.

        容器实例名称

        :param container_name: The container_name of this ListEventTopRiskRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def event_type(self):
        r"""Gets the event_type of this ListEventTopRiskRequest.

        事件类型，包含如下:   - 1001 : 通用恶意软件   - 1002 : 病毒   - 1003 : 蠕虫   - 1004 : 木马   - 1005 : 僵尸网络   - 1006 : 后门   - 1010 : Rootkit   - 1011 : 勒索软件   - 1012 ：黑客工具   - 1015 : Webshell   - 1016 : 挖矿   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2012 : 远程代码执行   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 3029 ：系统安全防护被禁用   - 3030 ：备份删除   - 3031 ：异常注册表操作   - 3036 : 容器镜像阻断   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号   - 4014 : 用户账号添加   - 4020 : 用户密码窃取   - 6002 : 端口扫描   - 6003 : 主机扫描   - 13001 : Kubernetes事件删除   - 13002 : Pod异常行为   - 13003 : 枚举用户信息   - 13004 : 绑定集群用户角色

        :return: The event_type of this ListEventTopRiskRequest.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListEventTopRiskRequest.

        事件类型，包含如下:   - 1001 : 通用恶意软件   - 1002 : 病毒   - 1003 : 蠕虫   - 1004 : 木马   - 1005 : 僵尸网络   - 1006 : 后门   - 1010 : Rootkit   - 1011 : 勒索软件   - 1012 ：黑客工具   - 1015 : Webshell   - 1016 : 挖矿   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2012 : 远程代码执行   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 3029 ：系统安全防护被禁用   - 3030 ：备份删除   - 3031 ：异常注册表操作   - 3036 : 容器镜像阻断   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号   - 4014 : 用户账号添加   - 4020 : 用户密码窃取   - 6002 : 端口扫描   - 6003 : 主机扫描   - 13001 : Kubernetes事件删除   - 13002 : Pod异常行为   - 13003 : 枚举用户信息   - 13004 : 绑定集群用户角色

        :param event_type: The event_type of this ListEventTopRiskRequest.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListEventTopRiskRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :return: The handle_status of this ListEventTopRiskRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListEventTopRiskRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :param handle_status: The handle_status of this ListEventTopRiskRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def severity(self):
        r"""Gets the severity of this ListEventTopRiskRequest.

        威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :return: The severity of this ListEventTopRiskRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListEventTopRiskRequest.

        威胁等级，包含如下:   - Security ：安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :param severity: The severity of this ListEventTopRiskRequest.
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
        if not isinstance(other, ListEventTopRiskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
