# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'time': 'int',
        'policyid': 'str',
        'sip': 'str',
        'host': 'str',
        'url': 'str',
        'attack': 'str',
        'rule': 'str',
        'payload': 'str',
        'payload_location': 'str',
        'action': 'str',
        'request_line': 'str',
        'headers': 'object',
        'cookie': 'str',
        'status': 'str',
        'process_time': 'int',
        'region': 'str',
        'host_id': 'str',
        'response_time': 'int',
        'response_size': 'int',
        'response_body': 'str',
        'request_body': 'str'
    }

    attribute_map = {
        'id': 'id',
        'time': 'time',
        'policyid': 'policyid',
        'sip': 'sip',
        'host': 'host',
        'url': 'url',
        'attack': 'attack',
        'rule': 'rule',
        'payload': 'payload',
        'payload_location': 'payload_location',
        'action': 'action',
        'request_line': 'request_line',
        'headers': 'headers',
        'cookie': 'cookie',
        'status': 'status',
        'process_time': 'process_time',
        'region': 'region',
        'host_id': 'host_id',
        'response_time': 'response_time',
        'response_size': 'response_size',
        'response_body': 'response_body',
        'request_body': 'request_body'
    }

    def __init__(self, id=None, time=None, policyid=None, sip=None, host=None, url=None, attack=None, rule=None, payload=None, payload_location=None, action=None, request_line=None, headers=None, cookie=None, status=None, process_time=None, region=None, host_id=None, response_time=None, response_size=None, response_body=None, request_body=None):
        """ListEventItems

        The model defined in huaweicloud sdk

        :param id: 事件id
        :type id: str
        :param time: 攻击发生时的时间戳(毫秒)
        :type time: int
        :param policyid: 策略id
        :type policyid: str
        :param sip: 源ip，Web访问者的IP地址（攻击者IP地址）
        :type sip: str
        :param host: 域名
        :type host: str
        :param url: 攻击的url链接
        :type url: str
        :param attack: 攻击类型:   - vuln：其它攻击类型   - sqli： sql注入攻击   - lfi： 本地文件包含  - cmdi：命令注入攻击   - xss：XSS攻击   - robot：恶意爬虫   - rfi：远程文件包含   - custom_custom：精准防护   - webshell：网站木马   - custom_whiteblackip：黑白名单拦截   - custom_geoip：地理访问控制拦截   - antitamper：防篡改   - anticrawler：反爬虫    - leakage：网站信息防泄漏   - illegal：非法请求 
        :type attack: str
        :param rule: 命中的规则id
        :type rule: str
        :param payload: 命中的载荷
        :type payload: str
        :param payload_location: 命中的载荷位置
        :type payload_location: str
        :param action: 防护动作
        :type action: str
        :param request_line: 请求方法和路径
        :type request_line: str
        :param headers: http请求header
        :type headers: object
        :param cookie: 请求cookie
        :type cookie: str
        :param status: 响应码状态
        :type status: str
        :param process_time: 处理时长
        :type process_time: int
        :param region: 地理位置
        :type region: str
        :param host_id: 域名id
        :type host_id: str
        :param response_time: 响应时长
        :type response_time: int
        :param response_size: 响应体大小
        :type response_size: int
        :param response_body: 响应体
        :type response_body: str
        :param request_body: 请求体
        :type request_body: str
        """
        
        

        self._id = None
        self._time = None
        self._policyid = None
        self._sip = None
        self._host = None
        self._url = None
        self._attack = None
        self._rule = None
        self._payload = None
        self._payload_location = None
        self._action = None
        self._request_line = None
        self._headers = None
        self._cookie = None
        self._status = None
        self._process_time = None
        self._region = None
        self._host_id = None
        self._response_time = None
        self._response_size = None
        self._response_body = None
        self._request_body = None
        self.discriminator = None

        if id is not None:
            self.id = id
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
        if payload is not None:
            self.payload = payload
        if payload_location is not None:
            self.payload_location = payload_location
        if action is not None:
            self.action = action
        if request_line is not None:
            self.request_line = request_line
        if headers is not None:
            self.headers = headers
        if cookie is not None:
            self.cookie = cookie
        if status is not None:
            self.status = status
        if process_time is not None:
            self.process_time = process_time
        if region is not None:
            self.region = region
        if host_id is not None:
            self.host_id = host_id
        if response_time is not None:
            self.response_time = response_time
        if response_size is not None:
            self.response_size = response_size
        if response_body is not None:
            self.response_body = response_body
        if request_body is not None:
            self.request_body = request_body

    @property
    def id(self):
        """Gets the id of this ListEventItems.

        事件id

        :return: The id of this ListEventItems.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListEventItems.

        事件id

        :param id: The id of this ListEventItems.
        :type id: str
        """
        self._id = id

    @property
    def time(self):
        """Gets the time of this ListEventItems.

        攻击发生时的时间戳(毫秒)

        :return: The time of this ListEventItems.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ListEventItems.

        攻击发生时的时间戳(毫秒)

        :param time: The time of this ListEventItems.
        :type time: int
        """
        self._time = time

    @property
    def policyid(self):
        """Gets the policyid of this ListEventItems.

        策略id

        :return: The policyid of this ListEventItems.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this ListEventItems.

        策略id

        :param policyid: The policyid of this ListEventItems.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def sip(self):
        """Gets the sip of this ListEventItems.

        源ip，Web访问者的IP地址（攻击者IP地址）

        :return: The sip of this ListEventItems.
        :rtype: str
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        """Sets the sip of this ListEventItems.

        源ip，Web访问者的IP地址（攻击者IP地址）

        :param sip: The sip of this ListEventItems.
        :type sip: str
        """
        self._sip = sip

    @property
    def host(self):
        """Gets the host of this ListEventItems.

        域名

        :return: The host of this ListEventItems.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ListEventItems.

        域名

        :param host: The host of this ListEventItems.
        :type host: str
        """
        self._host = host

    @property
    def url(self):
        """Gets the url of this ListEventItems.

        攻击的url链接

        :return: The url of this ListEventItems.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ListEventItems.

        攻击的url链接

        :param url: The url of this ListEventItems.
        :type url: str
        """
        self._url = url

    @property
    def attack(self):
        """Gets the attack of this ListEventItems.

        攻击类型:   - vuln：其它攻击类型   - sqli： sql注入攻击   - lfi： 本地文件包含  - cmdi：命令注入攻击   - xss：XSS攻击   - robot：恶意爬虫   - rfi：远程文件包含   - custom_custom：精准防护   - webshell：网站木马   - custom_whiteblackip：黑白名单拦截   - custom_geoip：地理访问控制拦截   - antitamper：防篡改   - anticrawler：反爬虫    - leakage：网站信息防泄漏   - illegal：非法请求 

        :return: The attack of this ListEventItems.
        :rtype: str
        """
        return self._attack

    @attack.setter
    def attack(self, attack):
        """Sets the attack of this ListEventItems.

        攻击类型:   - vuln：其它攻击类型   - sqli： sql注入攻击   - lfi： 本地文件包含  - cmdi：命令注入攻击   - xss：XSS攻击   - robot：恶意爬虫   - rfi：远程文件包含   - custom_custom：精准防护   - webshell：网站木马   - custom_whiteblackip：黑白名单拦截   - custom_geoip：地理访问控制拦截   - antitamper：防篡改   - anticrawler：反爬虫    - leakage：网站信息防泄漏   - illegal：非法请求 

        :param attack: The attack of this ListEventItems.
        :type attack: str
        """
        self._attack = attack

    @property
    def rule(self):
        """Gets the rule of this ListEventItems.

        命中的规则id

        :return: The rule of this ListEventItems.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this ListEventItems.

        命中的规则id

        :param rule: The rule of this ListEventItems.
        :type rule: str
        """
        self._rule = rule

    @property
    def payload(self):
        """Gets the payload of this ListEventItems.

        命中的载荷

        :return: The payload of this ListEventItems.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ListEventItems.

        命中的载荷

        :param payload: The payload of this ListEventItems.
        :type payload: str
        """
        self._payload = payload

    @property
    def payload_location(self):
        """Gets the payload_location of this ListEventItems.

        命中的载荷位置

        :return: The payload_location of this ListEventItems.
        :rtype: str
        """
        return self._payload_location

    @payload_location.setter
    def payload_location(self, payload_location):
        """Sets the payload_location of this ListEventItems.

        命中的载荷位置

        :param payload_location: The payload_location of this ListEventItems.
        :type payload_location: str
        """
        self._payload_location = payload_location

    @property
    def action(self):
        """Gets the action of this ListEventItems.

        防护动作

        :return: The action of this ListEventItems.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListEventItems.

        防护动作

        :param action: The action of this ListEventItems.
        :type action: str
        """
        self._action = action

    @property
    def request_line(self):
        """Gets the request_line of this ListEventItems.

        请求方法和路径

        :return: The request_line of this ListEventItems.
        :rtype: str
        """
        return self._request_line

    @request_line.setter
    def request_line(self, request_line):
        """Sets the request_line of this ListEventItems.

        请求方法和路径

        :param request_line: The request_line of this ListEventItems.
        :type request_line: str
        """
        self._request_line = request_line

    @property
    def headers(self):
        """Gets the headers of this ListEventItems.

        http请求header

        :return: The headers of this ListEventItems.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ListEventItems.

        http请求header

        :param headers: The headers of this ListEventItems.
        :type headers: object
        """
        self._headers = headers

    @property
    def cookie(self):
        """Gets the cookie of this ListEventItems.

        请求cookie

        :return: The cookie of this ListEventItems.
        :rtype: str
        """
        return self._cookie

    @cookie.setter
    def cookie(self, cookie):
        """Sets the cookie of this ListEventItems.

        请求cookie

        :param cookie: The cookie of this ListEventItems.
        :type cookie: str
        """
        self._cookie = cookie

    @property
    def status(self):
        """Gets the status of this ListEventItems.

        响应码状态

        :return: The status of this ListEventItems.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListEventItems.

        响应码状态

        :param status: The status of this ListEventItems.
        :type status: str
        """
        self._status = status

    @property
    def process_time(self):
        """Gets the process_time of this ListEventItems.

        处理时长

        :return: The process_time of this ListEventItems.
        :rtype: int
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        """Sets the process_time of this ListEventItems.

        处理时长

        :param process_time: The process_time of this ListEventItems.
        :type process_time: int
        """
        self._process_time = process_time

    @property
    def region(self):
        """Gets the region of this ListEventItems.

        地理位置

        :return: The region of this ListEventItems.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListEventItems.

        地理位置

        :param region: The region of this ListEventItems.
        :type region: str
        """
        self._region = region

    @property
    def host_id(self):
        """Gets the host_id of this ListEventItems.

        域名id

        :return: The host_id of this ListEventItems.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListEventItems.

        域名id

        :param host_id: The host_id of this ListEventItems.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def response_time(self):
        """Gets the response_time of this ListEventItems.

        响应时长

        :return: The response_time of this ListEventItems.
        :rtype: int
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """Sets the response_time of this ListEventItems.

        响应时长

        :param response_time: The response_time of this ListEventItems.
        :type response_time: int
        """
        self._response_time = response_time

    @property
    def response_size(self):
        """Gets the response_size of this ListEventItems.

        响应体大小

        :return: The response_size of this ListEventItems.
        :rtype: int
        """
        return self._response_size

    @response_size.setter
    def response_size(self, response_size):
        """Sets the response_size of this ListEventItems.

        响应体大小

        :param response_size: The response_size of this ListEventItems.
        :type response_size: int
        """
        self._response_size = response_size

    @property
    def response_body(self):
        """Gets the response_body of this ListEventItems.

        响应体

        :return: The response_body of this ListEventItems.
        :rtype: str
        """
        return self._response_body

    @response_body.setter
    def response_body(self, response_body):
        """Sets the response_body of this ListEventItems.

        响应体

        :param response_body: The response_body of this ListEventItems.
        :type response_body: str
        """
        self._response_body = response_body

    @property
    def request_body(self):
        """Gets the request_body of this ListEventItems.

        请求体

        :return: The request_body of this ListEventItems.
        :rtype: str
        """
        return self._request_body

    @request_body.setter
    def request_body(self, request_body):
        """Sets the request_body of this ListEventItems.

        请求体

        :param request_body: The request_body of this ListEventItems.
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
        if not isinstance(other, ListEventItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
