# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RaspProtectHistoryResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'private_ip': 'str',
        'alarm_time': 'int',
        'event_name': 'str',
        'severity': 'str',
        'req_src_ip': 'str',
        'app_stack': 'str',
        'attack_input_name': 'str',
        'attack_input_value': 'str',
        'query_string': 'str',
        'req_headers': 'str',
        'req_method': 'str',
        'req_params': 'str',
        'req_path': 'str',
        'req_protocol': 'str',
        'req_url': 'str',
        'attack_tag': 'str',
        'chk_probe': 'str',
        'chk_rule': 'str',
        'chk_rule_desc': 'str',
        'exist_bug': 'str'
    }

    attribute_map = {
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'alarm_time': 'alarm_time',
        'event_name': 'event_name',
        'severity': 'severity',
        'req_src_ip': 'req_src_ip',
        'app_stack': 'app_stack',
        'attack_input_name': 'attack_input_name',
        'attack_input_value': 'attack_input_value',
        'query_string': 'query_string',
        'req_headers': 'req_headers',
        'req_method': 'req_method',
        'req_params': 'req_params',
        'req_path': 'req_path',
        'req_protocol': 'req_protocol',
        'req_url': 'req_url',
        'attack_tag': 'attack_tag',
        'chk_probe': 'chk_probe',
        'chk_rule': 'chk_rule',
        'chk_rule_desc': 'chk_rule_desc',
        'exist_bug': 'exist_bug'
    }

    def __init__(self, host_name=None, private_ip=None, alarm_time=None, event_name=None, severity=None, req_src_ip=None, app_stack=None, attack_input_name=None, attack_input_value=None, query_string=None, req_headers=None, req_method=None, req_params=None, req_path=None, req_protocol=None, req_url=None, attack_tag=None, chk_probe=None, chk_rule=None, chk_rule_desc=None, exist_bug=None):
        r"""RaspProtectHistoryResponseInfo

        The model defined in huaweicloud sdk

        :param host_name: **参数解释** 应用防护事件所属云服务器的名称，用于标识事件来源主机 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线，符合华为云ECS命名规范 
        :type host_name: str
        :param private_ip: **参数解释** 应用防护事件所属云服务器的私有IP地址，用于定位事件来源主机的网络位置 **取值范围** 符合IPv4格式的字符串（如192.168.0.97），支持多个私有IP用逗号分隔 
        :type private_ip: str
        :param alarm_time: **参数解释** 应用防护事件的发生时间，以Unix时间戳（毫秒级）表示 **时间格式** 可转换为YYYY-MM-DD HH:MM:SS格式（如1736414463000对应2024-12-10 10:41:03） **取值范围** Unix时间戳（毫秒级），取值0-为当前系统时间戳 
        :type alarm_time: int
        :param event_name: **参数解释** 应用防护事件的具体名称，标识事件对应的攻击类型（如ExpressionInject表示表达式注入攻击） **取值范围** 字符长度1-128位，支持英文、数字、下划线，为系统预定义的攻击类型标识 
        :type event_name: str
        :param severity: **参数解释** 应用防护事件的告警级别，用于筛选指定严重程度的事件 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：信息级 - Low：低危 - Medium：中危 - High：高危 - Critical：紧急 **默认取值** 无 
        :type severity: str
        :param req_src_ip: **参数解释** 发起攻击的源IP地址，可能是公网IP或内网IP，用于定位攻击来源 **取值范围** 符合IPv4或IPv6格式的字符串，支持单个IP或IP段（如127.0.0.1、2001:db8::1） 
        :type req_src_ip: str
        :param app_stack: **参数解释** 应用防护事件发生时的应用程序调用堆栈信息，用于定位漏洞触发点 **取值范围** 字符长度0-4096位，支持英文、数字、符号等堆栈信息常见字符，为空表示无堆栈数据 
        :type app_stack: str
        :param attack_input_name: **参数解释** 攻击请求中的附属字段名称（如请求头字段、表单字段等），用于标识攻击载荷的传入字段 **取值范围** 字符长度0-256位，支持英文、数字、符号等HTTP请求字段常见字符，为空表示无相关字段 
        :type attack_input_name: str
        :param attack_input_value: **参数解释** 攻击请求中包含的恶意载荷数据（如注入脚本、恶意命令等），用于分析攻击手段 **取值范围** 字符长度0-2048位，支持各类字符（含特殊字符），为空表示无恶意载荷 
        :type attack_input_value: str
        :param query_string: **参数解释** 攻击请求的URL查询字符串部分（即?后的参数），用于分析攻击请求的参数传递方式 **取值范围** 字符长度0-1024位，支持URL编码后的字符，为空表示无查询字符串 
        :type query_string: str
        :param req_headers: **参数解释** 攻击请求的HTTP请求头信息，以JSON格式存储，包含User-Agent、Host等字段 **取值范围** 字符长度0-4096位，为JSON格式字符串，字段名和值支持常见HTTP头字符，为空表示无请求头信息 
        :type req_headers: str
        :param req_method: **参数解释** 攻击请求使用的HTTP方法（如GET、POST），用于分析攻击的请求类型 **取值范围** 字符长度3-10位，支持标准HTTP方法（GET、POST、PUT、DELETE等），区分大小写 
        :type req_method: str
        :param req_params: **参数解释** 攻击请求的请求体参数（如POST请求的表单数据），用于分析攻击的参数传递内容 **取值范围** 字符长度0-2048位，支持表单编码或JSON格式字符，为空表示无请求体参数 
        :type req_params: str
        :param req_path: **参数解释** 攻击请求的URL路径部分（不含查询字符串），用于定位攻击的目标接口 **取值范围** 字符长度0-512位，支持URL路径字符（如/、字母、数字、短横线、下划线），为空表示根路径 
        :type req_path: str
        :param req_protocol: **参数解释** 攻击请求使用的HTTP协议版本（如HTTP/1.1），用于分析攻击的协议环境 **取值范围** 字符长度5-10位，支持HTTP/1.0、HTTP/1.1、HTTP/2等标准协议版本 
        :type req_protocol: str
        :param req_url: **参数解释** 攻击请求的完整URL地址（含协议、主机、路径、查询字符串），用于完整还原攻击请求 **取值范围** 字符长度0-1024位，符合URL格式规范，为空表示无完整URL信息 
        :type req_url: str
        :param attack_tag: **参数解释** 应用防护事件的攻击类型标识，与请求参数的攻击标识对应（格式为小写下划线） **取值范围** - Attack Success：攻击成功 - Attack Attempt：攻击尝试 - Attack Blocked：攻击被阻断 - Abnormal Behavior：异常行为 - Collapsible Host：主机失陷 - System Vulnerability：系统脆弱性 
        :type attack_tag: str
        :param chk_probe: **参数解释**: 检测到该攻击事件的RASP探针标识，用于定位探针类型和检测模块 **取值范围**: 字符长度1-128位，支持英文、数字、点号、短横线、下划线，为系统预定义的探针标识 
        :type chk_probe: str
        :param chk_rule: **参数解释** 触发该防护事件的检测规则唯一标识，用于关联具体的防护规则配置 **取值范围** 字符长度1-64位，支持英文、数字、下划线，为系统预定义的规则标识（如ExpressionInject） 
        :type chk_rule: str
        :param chk_rule_desc: **参数解释** 触发该防护事件的检测规则详细描述，说明规则的检测逻辑和目的 **取值范围** 字符长度0-512位，支持中文、英文、数字、常用标点符号，为空表示无规则描述 
        :type chk_rule_desc: str
        :param exist_bug: **参数解释** 标识该防护事件是否因应用存在漏洞导致（yes表示存在漏洞，no表示不存在） **取值范围** - yes：存在漏洞 - no：不存在漏洞 - unknown：未知 
        :type exist_bug: str
        """
        
        

        self._host_name = None
        self._private_ip = None
        self._alarm_time = None
        self._event_name = None
        self._severity = None
        self._req_src_ip = None
        self._app_stack = None
        self._attack_input_name = None
        self._attack_input_value = None
        self._query_string = None
        self._req_headers = None
        self._req_method = None
        self._req_params = None
        self._req_path = None
        self._req_protocol = None
        self._req_url = None
        self._attack_tag = None
        self._chk_probe = None
        self._chk_rule = None
        self._chk_rule_desc = None
        self._exist_bug = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if alarm_time is not None:
            self.alarm_time = alarm_time
        if event_name is not None:
            self.event_name = event_name
        if severity is not None:
            self.severity = severity
        if req_src_ip is not None:
            self.req_src_ip = req_src_ip
        if app_stack is not None:
            self.app_stack = app_stack
        if attack_input_name is not None:
            self.attack_input_name = attack_input_name
        if attack_input_value is not None:
            self.attack_input_value = attack_input_value
        if query_string is not None:
            self.query_string = query_string
        if req_headers is not None:
            self.req_headers = req_headers
        if req_method is not None:
            self.req_method = req_method
        if req_params is not None:
            self.req_params = req_params
        if req_path is not None:
            self.req_path = req_path
        if req_protocol is not None:
            self.req_protocol = req_protocol
        if req_url is not None:
            self.req_url = req_url
        if attack_tag is not None:
            self.attack_tag = attack_tag
        if chk_probe is not None:
            self.chk_probe = chk_probe
        if chk_rule is not None:
            self.chk_rule = chk_rule
        if chk_rule_desc is not None:
            self.chk_rule_desc = chk_rule_desc
        if exist_bug is not None:
            self.exist_bug = exist_bug

    @property
    def host_name(self):
        r"""Gets the host_name of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件所属云服务器的名称，用于标识事件来源主机 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线，符合华为云ECS命名规范 

        :return: The host_name of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件所属云服务器的名称，用于标识事件来源主机 **取值范围** 字符长度1-64位，支持中文、英文、数字、短横线、下划线，符合华为云ECS命名规范 

        :param host_name: The host_name of this RaspProtectHistoryResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件所属云服务器的私有IP地址，用于定位事件来源主机的网络位置 **取值范围** 符合IPv4格式的字符串（如192.168.0.97），支持多个私有IP用逗号分隔 

        :return: The private_ip of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件所属云服务器的私有IP地址，用于定位事件来源主机的网络位置 **取值范围** 符合IPv4格式的字符串（如192.168.0.97），支持多个私有IP用逗号分隔 

        :param private_ip: The private_ip of this RaspProtectHistoryResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def alarm_time(self):
        r"""Gets the alarm_time of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件的发生时间，以Unix时间戳（毫秒级）表示 **时间格式** 可转换为YYYY-MM-DD HH:MM:SS格式（如1736414463000对应2024-12-10 10:41:03） **取值范围** Unix时间戳（毫秒级），取值0-为当前系统时间戳 

        :return: The alarm_time of this RaspProtectHistoryResponseInfo.
        :rtype: int
        """
        return self._alarm_time

    @alarm_time.setter
    def alarm_time(self, alarm_time):
        r"""Sets the alarm_time of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件的发生时间，以Unix时间戳（毫秒级）表示 **时间格式** 可转换为YYYY-MM-DD HH:MM:SS格式（如1736414463000对应2024-12-10 10:41:03） **取值范围** Unix时间戳（毫秒级），取值0-为当前系统时间戳 

        :param alarm_time: The alarm_time of this RaspProtectHistoryResponseInfo.
        :type alarm_time: int
        """
        self._alarm_time = alarm_time

    @property
    def event_name(self):
        r"""Gets the event_name of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件的具体名称，标识事件对应的攻击类型（如ExpressionInject表示表达式注入攻击） **取值范围** 字符长度1-128位，支持英文、数字、下划线，为系统预定义的攻击类型标识 

        :return: The event_name of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件的具体名称，标识事件对应的攻击类型（如ExpressionInject表示表达式注入攻击） **取值范围** 字符长度1-128位，支持英文、数字、下划线，为系统预定义的攻击类型标识 

        :param event_name: The event_name of this RaspProtectHistoryResponseInfo.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def severity(self):
        r"""Gets the severity of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件的告警级别，用于筛选指定严重程度的事件 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：信息级 - Low：低危 - Medium：中危 - High：高危 - Critical：紧急 **默认取值** 无 

        :return: The severity of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件的告警级别，用于筛选指定严重程度的事件 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：信息级 - Low：低危 - Medium：中危 - High：高危 - Critical：紧急 **默认取值** 无 

        :param severity: The severity of this RaspProtectHistoryResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def req_src_ip(self):
        r"""Gets the req_src_ip of this RaspProtectHistoryResponseInfo.

        **参数解释** 发起攻击的源IP地址，可能是公网IP或内网IP，用于定位攻击来源 **取值范围** 符合IPv4或IPv6格式的字符串，支持单个IP或IP段（如127.0.0.1、2001:db8::1） 

        :return: The req_src_ip of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_src_ip

    @req_src_ip.setter
    def req_src_ip(self, req_src_ip):
        r"""Sets the req_src_ip of this RaspProtectHistoryResponseInfo.

        **参数解释** 发起攻击的源IP地址，可能是公网IP或内网IP，用于定位攻击来源 **取值范围** 符合IPv4或IPv6格式的字符串，支持单个IP或IP段（如127.0.0.1、2001:db8::1） 

        :param req_src_ip: The req_src_ip of this RaspProtectHistoryResponseInfo.
        :type req_src_ip: str
        """
        self._req_src_ip = req_src_ip

    @property
    def app_stack(self):
        r"""Gets the app_stack of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件发生时的应用程序调用堆栈信息，用于定位漏洞触发点 **取值范围** 字符长度0-4096位，支持英文、数字、符号等堆栈信息常见字符，为空表示无堆栈数据 

        :return: The app_stack of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._app_stack

    @app_stack.setter
    def app_stack(self, app_stack):
        r"""Sets the app_stack of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件发生时的应用程序调用堆栈信息，用于定位漏洞触发点 **取值范围** 字符长度0-4096位，支持英文、数字、符号等堆栈信息常见字符，为空表示无堆栈数据 

        :param app_stack: The app_stack of this RaspProtectHistoryResponseInfo.
        :type app_stack: str
        """
        self._app_stack = app_stack

    @property
    def attack_input_name(self):
        r"""Gets the attack_input_name of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求中的附属字段名称（如请求头字段、表单字段等），用于标识攻击载荷的传入字段 **取值范围** 字符长度0-256位，支持英文、数字、符号等HTTP请求字段常见字符，为空表示无相关字段 

        :return: The attack_input_name of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._attack_input_name

    @attack_input_name.setter
    def attack_input_name(self, attack_input_name):
        r"""Sets the attack_input_name of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求中的附属字段名称（如请求头字段、表单字段等），用于标识攻击载荷的传入字段 **取值范围** 字符长度0-256位，支持英文、数字、符号等HTTP请求字段常见字符，为空表示无相关字段 

        :param attack_input_name: The attack_input_name of this RaspProtectHistoryResponseInfo.
        :type attack_input_name: str
        """
        self._attack_input_name = attack_input_name

    @property
    def attack_input_value(self):
        r"""Gets the attack_input_value of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求中包含的恶意载荷数据（如注入脚本、恶意命令等），用于分析攻击手段 **取值范围** 字符长度0-2048位，支持各类字符（含特殊字符），为空表示无恶意载荷 

        :return: The attack_input_value of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._attack_input_value

    @attack_input_value.setter
    def attack_input_value(self, attack_input_value):
        r"""Sets the attack_input_value of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求中包含的恶意载荷数据（如注入脚本、恶意命令等），用于分析攻击手段 **取值范围** 字符长度0-2048位，支持各类字符（含特殊字符），为空表示无恶意载荷 

        :param attack_input_value: The attack_input_value of this RaspProtectHistoryResponseInfo.
        :type attack_input_value: str
        """
        self._attack_input_value = attack_input_value

    @property
    def query_string(self):
        r"""Gets the query_string of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求的URL查询字符串部分（即?后的参数），用于分析攻击请求的参数传递方式 **取值范围** 字符长度0-1024位，支持URL编码后的字符，为空表示无查询字符串 

        :return: The query_string of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        r"""Sets the query_string of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求的URL查询字符串部分（即?后的参数），用于分析攻击请求的参数传递方式 **取值范围** 字符长度0-1024位，支持URL编码后的字符，为空表示无查询字符串 

        :param query_string: The query_string of this RaspProtectHistoryResponseInfo.
        :type query_string: str
        """
        self._query_string = query_string

    @property
    def req_headers(self):
        r"""Gets the req_headers of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求的HTTP请求头信息，以JSON格式存储，包含User-Agent、Host等字段 **取值范围** 字符长度0-4096位，为JSON格式字符串，字段名和值支持常见HTTP头字符，为空表示无请求头信息 

        :return: The req_headers of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_headers

    @req_headers.setter
    def req_headers(self, req_headers):
        r"""Sets the req_headers of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求的HTTP请求头信息，以JSON格式存储，包含User-Agent、Host等字段 **取值范围** 字符长度0-4096位，为JSON格式字符串，字段名和值支持常见HTTP头字符，为空表示无请求头信息 

        :param req_headers: The req_headers of this RaspProtectHistoryResponseInfo.
        :type req_headers: str
        """
        self._req_headers = req_headers

    @property
    def req_method(self):
        r"""Gets the req_method of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求使用的HTTP方法（如GET、POST），用于分析攻击的请求类型 **取值范围** 字符长度3-10位，支持标准HTTP方法（GET、POST、PUT、DELETE等），区分大小写 

        :return: The req_method of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        r"""Sets the req_method of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求使用的HTTP方法（如GET、POST），用于分析攻击的请求类型 **取值范围** 字符长度3-10位，支持标准HTTP方法（GET、POST、PUT、DELETE等），区分大小写 

        :param req_method: The req_method of this RaspProtectHistoryResponseInfo.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_params(self):
        r"""Gets the req_params of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求的请求体参数（如POST请求的表单数据），用于分析攻击的参数传递内容 **取值范围** 字符长度0-2048位，支持表单编码或JSON格式字符，为空表示无请求体参数 

        :return: The req_params of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_params

    @req_params.setter
    def req_params(self, req_params):
        r"""Sets the req_params of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求的请求体参数（如POST请求的表单数据），用于分析攻击的参数传递内容 **取值范围** 字符长度0-2048位，支持表单编码或JSON格式字符，为空表示无请求体参数 

        :param req_params: The req_params of this RaspProtectHistoryResponseInfo.
        :type req_params: str
        """
        self._req_params = req_params

    @property
    def req_path(self):
        r"""Gets the req_path of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求的URL路径部分（不含查询字符串），用于定位攻击的目标接口 **取值范围** 字符长度0-512位，支持URL路径字符（如/、字母、数字、短横线、下划线），为空表示根路径 

        :return: The req_path of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_path

    @req_path.setter
    def req_path(self, req_path):
        r"""Sets the req_path of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求的URL路径部分（不含查询字符串），用于定位攻击的目标接口 **取值范围** 字符长度0-512位，支持URL路径字符（如/、字母、数字、短横线、下划线），为空表示根路径 

        :param req_path: The req_path of this RaspProtectHistoryResponseInfo.
        :type req_path: str
        """
        self._req_path = req_path

    @property
    def req_protocol(self):
        r"""Gets the req_protocol of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求使用的HTTP协议版本（如HTTP/1.1），用于分析攻击的协议环境 **取值范围** 字符长度5-10位，支持HTTP/1.0、HTTP/1.1、HTTP/2等标准协议版本 

        :return: The req_protocol of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        r"""Sets the req_protocol of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求使用的HTTP协议版本（如HTTP/1.1），用于分析攻击的协议环境 **取值范围** 字符长度5-10位，支持HTTP/1.0、HTTP/1.1、HTTP/2等标准协议版本 

        :param req_protocol: The req_protocol of this RaspProtectHistoryResponseInfo.
        :type req_protocol: str
        """
        self._req_protocol = req_protocol

    @property
    def req_url(self):
        r"""Gets the req_url of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求的完整URL地址（含协议、主机、路径、查询字符串），用于完整还原攻击请求 **取值范围** 字符长度0-1024位，符合URL格式规范，为空表示无完整URL信息 

        :return: The req_url of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_url

    @req_url.setter
    def req_url(self, req_url):
        r"""Sets the req_url of this RaspProtectHistoryResponseInfo.

        **参数解释** 攻击请求的完整URL地址（含协议、主机、路径、查询字符串），用于完整还原攻击请求 **取值范围** 字符长度0-1024位，符合URL格式规范，为空表示无完整URL信息 

        :param req_url: The req_url of this RaspProtectHistoryResponseInfo.
        :type req_url: str
        """
        self._req_url = req_url

    @property
    def attack_tag(self):
        r"""Gets the attack_tag of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件的攻击类型标识，与请求参数的攻击标识对应（格式为小写下划线） **取值范围** - Attack Success：攻击成功 - Attack Attempt：攻击尝试 - Attack Blocked：攻击被阻断 - Abnormal Behavior：异常行为 - Collapsible Host：主机失陷 - System Vulnerability：系统脆弱性 

        :return: The attack_tag of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._attack_tag

    @attack_tag.setter
    def attack_tag(self, attack_tag):
        r"""Sets the attack_tag of this RaspProtectHistoryResponseInfo.

        **参数解释** 应用防护事件的攻击类型标识，与请求参数的攻击标识对应（格式为小写下划线） **取值范围** - Attack Success：攻击成功 - Attack Attempt：攻击尝试 - Attack Blocked：攻击被阻断 - Abnormal Behavior：异常行为 - Collapsible Host：主机失陷 - System Vulnerability：系统脆弱性 

        :param attack_tag: The attack_tag of this RaspProtectHistoryResponseInfo.
        :type attack_tag: str
        """
        self._attack_tag = attack_tag

    @property
    def chk_probe(self):
        r"""Gets the chk_probe of this RaspProtectHistoryResponseInfo.

        **参数解释**: 检测到该攻击事件的RASP探针标识，用于定位探针类型和检测模块 **取值范围**: 字符长度1-128位，支持英文、数字、点号、短横线、下划线，为系统预定义的探针标识 

        :return: The chk_probe of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._chk_probe

    @chk_probe.setter
    def chk_probe(self, chk_probe):
        r"""Sets the chk_probe of this RaspProtectHistoryResponseInfo.

        **参数解释**: 检测到该攻击事件的RASP探针标识，用于定位探针类型和检测模块 **取值范围**: 字符长度1-128位，支持英文、数字、点号、短横线、下划线，为系统预定义的探针标识 

        :param chk_probe: The chk_probe of this RaspProtectHistoryResponseInfo.
        :type chk_probe: str
        """
        self._chk_probe = chk_probe

    @property
    def chk_rule(self):
        r"""Gets the chk_rule of this RaspProtectHistoryResponseInfo.

        **参数解释** 触发该防护事件的检测规则唯一标识，用于关联具体的防护规则配置 **取值范围** 字符长度1-64位，支持英文、数字、下划线，为系统预定义的规则标识（如ExpressionInject） 

        :return: The chk_rule of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._chk_rule

    @chk_rule.setter
    def chk_rule(self, chk_rule):
        r"""Sets the chk_rule of this RaspProtectHistoryResponseInfo.

        **参数解释** 触发该防护事件的检测规则唯一标识，用于关联具体的防护规则配置 **取值范围** 字符长度1-64位，支持英文、数字、下划线，为系统预定义的规则标识（如ExpressionInject） 

        :param chk_rule: The chk_rule of this RaspProtectHistoryResponseInfo.
        :type chk_rule: str
        """
        self._chk_rule = chk_rule

    @property
    def chk_rule_desc(self):
        r"""Gets the chk_rule_desc of this RaspProtectHistoryResponseInfo.

        **参数解释** 触发该防护事件的检测规则详细描述，说明规则的检测逻辑和目的 **取值范围** 字符长度0-512位，支持中文、英文、数字、常用标点符号，为空表示无规则描述 

        :return: The chk_rule_desc of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._chk_rule_desc

    @chk_rule_desc.setter
    def chk_rule_desc(self, chk_rule_desc):
        r"""Sets the chk_rule_desc of this RaspProtectHistoryResponseInfo.

        **参数解释** 触发该防护事件的检测规则详细描述，说明规则的检测逻辑和目的 **取值范围** 字符长度0-512位，支持中文、英文、数字、常用标点符号，为空表示无规则描述 

        :param chk_rule_desc: The chk_rule_desc of this RaspProtectHistoryResponseInfo.
        :type chk_rule_desc: str
        """
        self._chk_rule_desc = chk_rule_desc

    @property
    def exist_bug(self):
        r"""Gets the exist_bug of this RaspProtectHistoryResponseInfo.

        **参数解释** 标识该防护事件是否因应用存在漏洞导致（yes表示存在漏洞，no表示不存在） **取值范围** - yes：存在漏洞 - no：不存在漏洞 - unknown：未知 

        :return: The exist_bug of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._exist_bug

    @exist_bug.setter
    def exist_bug(self, exist_bug):
        r"""Sets the exist_bug of this RaspProtectHistoryResponseInfo.

        **参数解释** 标识该防护事件是否因应用存在漏洞导致（yes表示存在漏洞，no表示不存在） **取值范围** - yes：存在漏洞 - no：不存在漏洞 - unknown：未知 

        :param exist_bug: The exist_bug of this RaspProtectHistoryResponseInfo.
        :type exist_bug: str
        """
        self._exist_bug = exist_bug

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
        if not isinstance(other, RaspProtectHistoryResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
