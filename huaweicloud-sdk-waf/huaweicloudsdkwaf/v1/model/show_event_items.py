# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'int',
        'policyid': 'str',
        'sip': 'str',
        'host': 'str',
        'url': 'str',
        'attack': 'str',
        'rule': 'str',
        'action': 'str',
        'cookie': 'str',
        'headers': 'object',
        'host_id': 'str',
        'id': 'str',
        'payload': 'str',
        'payload_location': 'str',
        'region': 'str',
        'process_time': 'int',
        'request_line': 'str',
        'response_size': 'int',
        'response_time': 'int',
        'status': 'str',
        'request_body': 'str'
    }

    attribute_map = {
        'time': 'time',
        'policyid': 'policyid',
        'sip': 'sip',
        'host': 'host',
        'url': 'url',
        'attack': 'attack',
        'rule': 'rule',
        'action': 'action',
        'cookie': 'cookie',
        'headers': 'headers',
        'host_id': 'host_id',
        'id': 'id',
        'payload': 'payload',
        'payload_location': 'payload_location',
        'region': 'region',
        'process_time': 'process_time',
        'request_line': 'request_line',
        'response_size': 'response_size',
        'response_time': 'response_time',
        'status': 'status',
        'request_body': 'request_body'
    }

    def __init__(self, time=None, policyid=None, sip=None, host=None, url=None, attack=None, rule=None, action=None, cookie=None, headers=None, host_id=None, id=None, payload=None, payload_location=None, region=None, process_time=None, request_line=None, response_size=None, response_time=None, status=None, request_body=None):
        """ShowEventItems

        The model defined in huaweicloud sdk

        :param time: 攻击发生时的时间戳（毫秒）
        :type time: int
        :param policyid: 策略id
        :type policyid: str
        :param sip: 源ip，Web访问者的IP地址（攻击者IP地址）
        :type sip: str
        :param host: 域名
        :type host: str
        :param url: 攻击的url链接
        :type url: str
        :param attack: 攻击类型
        :type attack: str
        :param rule: 命中的规则id
        :type rule: str
        :param action: 防护动作
        :type action: str
        :param cookie: 攻击请求的cookie
        :type cookie: str
        :param headers: 攻击请求的headers
        :type headers: object
        :param host_id: 被攻击的域名id
        :type host_id: str
        :param id: 防护事件id
        :type id: str
        :param payload: 恶意负载
        :type payload: str
        :param payload_location: 恶意负载位置
        :type payload_location: str
        :param region: 源ip地理位置
        :type region: str
        :param process_time: 处理时长
        :type process_time: int
        :param request_line: 攻击请求的请求行
        :type request_line: str
        :param response_size: 返回大小（字节）
        :type response_size: int
        :param response_time: 响应时间（毫秒）
        :type response_time: int
        :param status: 响应码
        :type status: str
        :param request_body: 请求体
        :type request_body: str
        """
        
        

        self._time = None
        self._policyid = None
        self._sip = None
        self._host = None
        self._url = None
        self._attack = None
        self._rule = None
        self._action = None
        self._cookie = None
        self._headers = None
        self._host_id = None
        self._id = None
        self._payload = None
        self._payload_location = None
        self._region = None
        self._process_time = None
        self._request_line = None
        self._response_size = None
        self._response_time = None
        self._status = None
        self._request_body = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if policyid is not None:
            self.policyid = policyid
        if sip is not None:
            self.sip = sip
        if host is not None:
            self.host = host
        if url is not None:
            self.url = url
        if attack is not None:
            self.attack = attack
        if rule is not None:
            self.rule = rule
        if action is not None:
            self.action = action
        if cookie is not None:
            self.cookie = cookie
        if headers is not None:
            self.headers = headers
        if host_id is not None:
            self.host_id = host_id
        if id is not None:
            self.id = id
        if payload is not None:
            self.payload = payload
        if payload_location is not None:
            self.payload_location = payload_location
        if region is not None:
            self.region = region
        if process_time is not None:
            self.process_time = process_time
        if request_line is not None:
            self.request_line = request_line
        if response_size is not None:
            self.response_size = response_size
        if response_time is not None:
            self.response_time = response_time
        if status is not None:
            self.status = status
        if request_body is not None:
            self.request_body = request_body

    @property
    def time(self):
        """Gets the time of this ShowEventItems.

        攻击发生时的时间戳（毫秒）

        :return: The time of this ShowEventItems.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ShowEventItems.

        攻击发生时的时间戳（毫秒）

        :param time: The time of this ShowEventItems.
        :type time: int
        """
        self._time = time

    @property
    def policyid(self):
        """Gets the policyid of this ShowEventItems.

        策略id

        :return: The policyid of this ShowEventItems.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this ShowEventItems.

        策略id

        :param policyid: The policyid of this ShowEventItems.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def sip(self):
        """Gets the sip of this ShowEventItems.

        源ip，Web访问者的IP地址（攻击者IP地址）

        :return: The sip of this ShowEventItems.
        :rtype: str
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        """Sets the sip of this ShowEventItems.

        源ip，Web访问者的IP地址（攻击者IP地址）

        :param sip: The sip of this ShowEventItems.
        :type sip: str
        """
        self._sip = sip

    @property
    def host(self):
        """Gets the host of this ShowEventItems.

        域名

        :return: The host of this ShowEventItems.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ShowEventItems.

        域名

        :param host: The host of this ShowEventItems.
        :type host: str
        """
        self._host = host

    @property
    def url(self):
        """Gets the url of this ShowEventItems.

        攻击的url链接

        :return: The url of this ShowEventItems.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ShowEventItems.

        攻击的url链接

        :param url: The url of this ShowEventItems.
        :type url: str
        """
        self._url = url

    @property
    def attack(self):
        """Gets the attack of this ShowEventItems.

        攻击类型

        :return: The attack of this ShowEventItems.
        :rtype: str
        """
        return self._attack

    @attack.setter
    def attack(self, attack):
        """Sets the attack of this ShowEventItems.

        攻击类型

        :param attack: The attack of this ShowEventItems.
        :type attack: str
        """
        self._attack = attack

    @property
    def rule(self):
        """Gets the rule of this ShowEventItems.

        命中的规则id

        :return: The rule of this ShowEventItems.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this ShowEventItems.

        命中的规则id

        :param rule: The rule of this ShowEventItems.
        :type rule: str
        """
        self._rule = rule

    @property
    def action(self):
        """Gets the action of this ShowEventItems.

        防护动作

        :return: The action of this ShowEventItems.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ShowEventItems.

        防护动作

        :param action: The action of this ShowEventItems.
        :type action: str
        """
        self._action = action

    @property
    def cookie(self):
        """Gets the cookie of this ShowEventItems.

        攻击请求的cookie

        :return: The cookie of this ShowEventItems.
        :rtype: str
        """
        return self._cookie

    @cookie.setter
    def cookie(self, cookie):
        """Sets the cookie of this ShowEventItems.

        攻击请求的cookie

        :param cookie: The cookie of this ShowEventItems.
        :type cookie: str
        """
        self._cookie = cookie

    @property
    def headers(self):
        """Gets the headers of this ShowEventItems.

        攻击请求的headers

        :return: The headers of this ShowEventItems.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ShowEventItems.

        攻击请求的headers

        :param headers: The headers of this ShowEventItems.
        :type headers: object
        """
        self._headers = headers

    @property
    def host_id(self):
        """Gets the host_id of this ShowEventItems.

        被攻击的域名id

        :return: The host_id of this ShowEventItems.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ShowEventItems.

        被攻击的域名id

        :param host_id: The host_id of this ShowEventItems.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def id(self):
        """Gets the id of this ShowEventItems.

        防护事件id

        :return: The id of this ShowEventItems.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowEventItems.

        防护事件id

        :param id: The id of this ShowEventItems.
        :type id: str
        """
        self._id = id

    @property
    def payload(self):
        """Gets the payload of this ShowEventItems.

        恶意负载

        :return: The payload of this ShowEventItems.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ShowEventItems.

        恶意负载

        :param payload: The payload of this ShowEventItems.
        :type payload: str
        """
        self._payload = payload

    @property
    def payload_location(self):
        """Gets the payload_location of this ShowEventItems.

        恶意负载位置

        :return: The payload_location of this ShowEventItems.
        :rtype: str
        """
        return self._payload_location

    @payload_location.setter
    def payload_location(self, payload_location):
        """Sets the payload_location of this ShowEventItems.

        恶意负载位置

        :param payload_location: The payload_location of this ShowEventItems.
        :type payload_location: str
        """
        self._payload_location = payload_location

    @property
    def region(self):
        """Gets the region of this ShowEventItems.

        源ip地理位置

        :return: The region of this ShowEventItems.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowEventItems.

        源ip地理位置

        :param region: The region of this ShowEventItems.
        :type region: str
        """
        self._region = region

    @property
    def process_time(self):
        """Gets the process_time of this ShowEventItems.

        处理时长

        :return: The process_time of this ShowEventItems.
        :rtype: int
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        """Sets the process_time of this ShowEventItems.

        处理时长

        :param process_time: The process_time of this ShowEventItems.
        :type process_time: int
        """
        self._process_time = process_time

    @property
    def request_line(self):
        """Gets the request_line of this ShowEventItems.

        攻击请求的请求行

        :return: The request_line of this ShowEventItems.
        :rtype: str
        """
        return self._request_line

    @request_line.setter
    def request_line(self, request_line):
        """Sets the request_line of this ShowEventItems.

        攻击请求的请求行

        :param request_line: The request_line of this ShowEventItems.
        :type request_line: str
        """
        self._request_line = request_line

    @property
    def response_size(self):
        """Gets the response_size of this ShowEventItems.

        返回大小（字节）

        :return: The response_size of this ShowEventItems.
        :rtype: int
        """
        return self._response_size

    @response_size.setter
    def response_size(self, response_size):
        """Sets the response_size of this ShowEventItems.

        返回大小（字节）

        :param response_size: The response_size of this ShowEventItems.
        :type response_size: int
        """
        self._response_size = response_size

    @property
    def response_time(self):
        """Gets the response_time of this ShowEventItems.

        响应时间（毫秒）

        :return: The response_time of this ShowEventItems.
        :rtype: int
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """Sets the response_time of this ShowEventItems.

        响应时间（毫秒）

        :param response_time: The response_time of this ShowEventItems.
        :type response_time: int
        """
        self._response_time = response_time

    @property
    def status(self):
        """Gets the status of this ShowEventItems.

        响应码

        :return: The status of this ShowEventItems.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowEventItems.

        响应码

        :param status: The status of this ShowEventItems.
        :type status: str
        """
        self._status = status

    @property
    def request_body(self):
        """Gets the request_body of this ShowEventItems.

        请求体

        :return: The request_body of this ShowEventItems.
        :rtype: str
        """
        return self._request_body

    @request_body.setter
    def request_body(self, request_body):
        """Sets the request_body of this ShowEventItems.

        请求体

        :param request_body: The request_body of this ShowEventItems.
        :type request_body: str
        """
        self._request_body = request_body

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
        if not isinstance(other, ShowEventItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
