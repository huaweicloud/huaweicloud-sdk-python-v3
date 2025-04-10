# coding: utf-8

import six

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
        'alarm_time': 'object',
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

        :param host_name: 主机名称
        :type host_name: str
        :param private_ip: 主机私有IP
        :type private_ip: str
        :param alarm_time: 告警时间(ms)
        :type alarm_time: object
        :param event_name: 告警名称
        :type event_name: str
        :param severity: 告警级别
        :type severity: str
        :param req_src_ip: 源IP
        :type req_src_ip: str
        :param app_stack: 应用程序调用堆栈信息
        :type app_stack: str
        :param attack_input_name: 攻击附属字段
        :type attack_input_name: str
        :param attack_input_value: 攻击负载内容
        :type attack_input_value: str
        :param query_string: 查询字符串
        :type query_string: str
        :param req_headers: web请求头信息
        :type req_headers: str
        :param req_method: WEB请求方法
        :type req_method: str
        :param req_params: WEB请求参数
        :type req_params: str
        :param req_path: WEB请求路径
        :type req_path: str
        :param req_protocol: WEB请求协议
        :type req_protocol: str
        :param req_url: WEB请求URL地址
        :type req_url: str
        :param attack_tag: 攻击标识
        :type attack_tag: str
        :param chk_probe: 探针标识
        :type chk_probe: str
        :param chk_rule: 检测规则标识
        :type chk_rule: str
        :param chk_rule_desc: 规则描述
        :type chk_rule_desc: str
        :param exist_bug: 应用是否存在bug
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

        主机名称

        :return: The host_name of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this RaspProtectHistoryResponseInfo.

        主机名称

        :param host_name: The host_name of this RaspProtectHistoryResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this RaspProtectHistoryResponseInfo.

        主机私有IP

        :return: The private_ip of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this RaspProtectHistoryResponseInfo.

        主机私有IP

        :param private_ip: The private_ip of this RaspProtectHistoryResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def alarm_time(self):
        r"""Gets the alarm_time of this RaspProtectHistoryResponseInfo.

        告警时间(ms)

        :return: The alarm_time of this RaspProtectHistoryResponseInfo.
        :rtype: object
        """
        return self._alarm_time

    @alarm_time.setter
    def alarm_time(self, alarm_time):
        r"""Sets the alarm_time of this RaspProtectHistoryResponseInfo.

        告警时间(ms)

        :param alarm_time: The alarm_time of this RaspProtectHistoryResponseInfo.
        :type alarm_time: object
        """
        self._alarm_time = alarm_time

    @property
    def event_name(self):
        r"""Gets the event_name of this RaspProtectHistoryResponseInfo.

        告警名称

        :return: The event_name of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this RaspProtectHistoryResponseInfo.

        告警名称

        :param event_name: The event_name of this RaspProtectHistoryResponseInfo.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def severity(self):
        r"""Gets the severity of this RaspProtectHistoryResponseInfo.

        告警级别

        :return: The severity of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this RaspProtectHistoryResponseInfo.

        告警级别

        :param severity: The severity of this RaspProtectHistoryResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def req_src_ip(self):
        r"""Gets the req_src_ip of this RaspProtectHistoryResponseInfo.

        源IP

        :return: The req_src_ip of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_src_ip

    @req_src_ip.setter
    def req_src_ip(self, req_src_ip):
        r"""Sets the req_src_ip of this RaspProtectHistoryResponseInfo.

        源IP

        :param req_src_ip: The req_src_ip of this RaspProtectHistoryResponseInfo.
        :type req_src_ip: str
        """
        self._req_src_ip = req_src_ip

    @property
    def app_stack(self):
        r"""Gets the app_stack of this RaspProtectHistoryResponseInfo.

        应用程序调用堆栈信息

        :return: The app_stack of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._app_stack

    @app_stack.setter
    def app_stack(self, app_stack):
        r"""Sets the app_stack of this RaspProtectHistoryResponseInfo.

        应用程序调用堆栈信息

        :param app_stack: The app_stack of this RaspProtectHistoryResponseInfo.
        :type app_stack: str
        """
        self._app_stack = app_stack

    @property
    def attack_input_name(self):
        r"""Gets the attack_input_name of this RaspProtectHistoryResponseInfo.

        攻击附属字段

        :return: The attack_input_name of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._attack_input_name

    @attack_input_name.setter
    def attack_input_name(self, attack_input_name):
        r"""Sets the attack_input_name of this RaspProtectHistoryResponseInfo.

        攻击附属字段

        :param attack_input_name: The attack_input_name of this RaspProtectHistoryResponseInfo.
        :type attack_input_name: str
        """
        self._attack_input_name = attack_input_name

    @property
    def attack_input_value(self):
        r"""Gets the attack_input_value of this RaspProtectHistoryResponseInfo.

        攻击负载内容

        :return: The attack_input_value of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._attack_input_value

    @attack_input_value.setter
    def attack_input_value(self, attack_input_value):
        r"""Sets the attack_input_value of this RaspProtectHistoryResponseInfo.

        攻击负载内容

        :param attack_input_value: The attack_input_value of this RaspProtectHistoryResponseInfo.
        :type attack_input_value: str
        """
        self._attack_input_value = attack_input_value

    @property
    def query_string(self):
        r"""Gets the query_string of this RaspProtectHistoryResponseInfo.

        查询字符串

        :return: The query_string of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        r"""Sets the query_string of this RaspProtectHistoryResponseInfo.

        查询字符串

        :param query_string: The query_string of this RaspProtectHistoryResponseInfo.
        :type query_string: str
        """
        self._query_string = query_string

    @property
    def req_headers(self):
        r"""Gets the req_headers of this RaspProtectHistoryResponseInfo.

        web请求头信息

        :return: The req_headers of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_headers

    @req_headers.setter
    def req_headers(self, req_headers):
        r"""Sets the req_headers of this RaspProtectHistoryResponseInfo.

        web请求头信息

        :param req_headers: The req_headers of this RaspProtectHistoryResponseInfo.
        :type req_headers: str
        """
        self._req_headers = req_headers

    @property
    def req_method(self):
        r"""Gets the req_method of this RaspProtectHistoryResponseInfo.

        WEB请求方法

        :return: The req_method of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        r"""Sets the req_method of this RaspProtectHistoryResponseInfo.

        WEB请求方法

        :param req_method: The req_method of this RaspProtectHistoryResponseInfo.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_params(self):
        r"""Gets the req_params of this RaspProtectHistoryResponseInfo.

        WEB请求参数

        :return: The req_params of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_params

    @req_params.setter
    def req_params(self, req_params):
        r"""Sets the req_params of this RaspProtectHistoryResponseInfo.

        WEB请求参数

        :param req_params: The req_params of this RaspProtectHistoryResponseInfo.
        :type req_params: str
        """
        self._req_params = req_params

    @property
    def req_path(self):
        r"""Gets the req_path of this RaspProtectHistoryResponseInfo.

        WEB请求路径

        :return: The req_path of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_path

    @req_path.setter
    def req_path(self, req_path):
        r"""Sets the req_path of this RaspProtectHistoryResponseInfo.

        WEB请求路径

        :param req_path: The req_path of this RaspProtectHistoryResponseInfo.
        :type req_path: str
        """
        self._req_path = req_path

    @property
    def req_protocol(self):
        r"""Gets the req_protocol of this RaspProtectHistoryResponseInfo.

        WEB请求协议

        :return: The req_protocol of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        r"""Sets the req_protocol of this RaspProtectHistoryResponseInfo.

        WEB请求协议

        :param req_protocol: The req_protocol of this RaspProtectHistoryResponseInfo.
        :type req_protocol: str
        """
        self._req_protocol = req_protocol

    @property
    def req_url(self):
        r"""Gets the req_url of this RaspProtectHistoryResponseInfo.

        WEB请求URL地址

        :return: The req_url of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._req_url

    @req_url.setter
    def req_url(self, req_url):
        r"""Sets the req_url of this RaspProtectHistoryResponseInfo.

        WEB请求URL地址

        :param req_url: The req_url of this RaspProtectHistoryResponseInfo.
        :type req_url: str
        """
        self._req_url = req_url

    @property
    def attack_tag(self):
        r"""Gets the attack_tag of this RaspProtectHistoryResponseInfo.

        攻击标识

        :return: The attack_tag of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._attack_tag

    @attack_tag.setter
    def attack_tag(self, attack_tag):
        r"""Sets the attack_tag of this RaspProtectHistoryResponseInfo.

        攻击标识

        :param attack_tag: The attack_tag of this RaspProtectHistoryResponseInfo.
        :type attack_tag: str
        """
        self._attack_tag = attack_tag

    @property
    def chk_probe(self):
        r"""Gets the chk_probe of this RaspProtectHistoryResponseInfo.

        探针标识

        :return: The chk_probe of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._chk_probe

    @chk_probe.setter
    def chk_probe(self, chk_probe):
        r"""Sets the chk_probe of this RaspProtectHistoryResponseInfo.

        探针标识

        :param chk_probe: The chk_probe of this RaspProtectHistoryResponseInfo.
        :type chk_probe: str
        """
        self._chk_probe = chk_probe

    @property
    def chk_rule(self):
        r"""Gets the chk_rule of this RaspProtectHistoryResponseInfo.

        检测规则标识

        :return: The chk_rule of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._chk_rule

    @chk_rule.setter
    def chk_rule(self, chk_rule):
        r"""Sets the chk_rule of this RaspProtectHistoryResponseInfo.

        检测规则标识

        :param chk_rule: The chk_rule of this RaspProtectHistoryResponseInfo.
        :type chk_rule: str
        """
        self._chk_rule = chk_rule

    @property
    def chk_rule_desc(self):
        r"""Gets the chk_rule_desc of this RaspProtectHistoryResponseInfo.

        规则描述

        :return: The chk_rule_desc of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._chk_rule_desc

    @chk_rule_desc.setter
    def chk_rule_desc(self, chk_rule_desc):
        r"""Sets the chk_rule_desc of this RaspProtectHistoryResponseInfo.

        规则描述

        :param chk_rule_desc: The chk_rule_desc of this RaspProtectHistoryResponseInfo.
        :type chk_rule_desc: str
        """
        self._chk_rule_desc = chk_rule_desc

    @property
    def exist_bug(self):
        r"""Gets the exist_bug of this RaspProtectHistoryResponseInfo.

        应用是否存在bug

        :return: The exist_bug of this RaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._exist_bug

    @exist_bug.setter
    def exist_bug(self, exist_bug):
        r"""Sets the exist_bug of this RaspProtectHistoryResponseInfo.

        应用是否存在bug

        :param exist_bug: The exist_bug of this RaspProtectHistoryResponseInfo.
        :type exist_bug: str
        """
        self._exist_bug = exist_bug

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
        if not isinstance(other, RaspProtectHistoryResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
