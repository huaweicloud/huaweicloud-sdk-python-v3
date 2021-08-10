# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventResponseBodyItems:


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
        'action': 'str',
        'request_line': 'str',
        'headers': 'ListEventResponseBodyHeaders',
        'cookie': 'str',
        'status': 'str',
        'region': 'str',
        'host_id': 'str',
        'response_time': 'int',
        'response_size': 'int',
        'response_body': 'str'
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
        'action': 'action',
        'request_line': 'request_line',
        'headers': 'headers',
        'cookie': 'cookie',
        'status': 'status',
        'region': 'region',
        'host_id': 'host_id',
        'response_time': 'response_time',
        'response_size': 'response_size',
        'response_body': 'response_body'
    }

    def __init__(self, id=None, time=None, policyid=None, sip=None, host=None, url=None, attack=None, rule=None, payload=None, action=None, request_line=None, headers=None, cookie=None, status=None, region=None, host_id=None, response_time=None, response_size=None, response_body=None):
        """ListEventResponseBodyItems - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._time = None
        self._policyid = None
        self._sip = None
        self._host = None
        self._url = None
        self._attack = None
        self._rule = None
        self._payload = None
        self._action = None
        self._request_line = None
        self._headers = None
        self._cookie = None
        self._status = None
        self._region = None
        self._host_id = None
        self._response_time = None
        self._response_size = None
        self._response_body = None
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

    @property
    def id(self):
        """Gets the id of this ListEventResponseBodyItems.

        事件id

        :return: The id of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListEventResponseBodyItems.

        事件id

        :param id: The id of this ListEventResponseBodyItems.
        :type: str
        """
        self._id = id

    @property
    def time(self):
        """Gets the time of this ListEventResponseBodyItems.

        次数

        :return: The time of this ListEventResponseBodyItems.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ListEventResponseBodyItems.

        次数

        :param time: The time of this ListEventResponseBodyItems.
        :type: int
        """
        self._time = time

    @property
    def policyid(self):
        """Gets the policyid of this ListEventResponseBodyItems.

        策略id

        :return: The policyid of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this ListEventResponseBodyItems.

        策略id

        :param policyid: The policyid of this ListEventResponseBodyItems.
        :type: str
        """
        self._policyid = policyid

    @property
    def sip(self):
        """Gets the sip of this ListEventResponseBodyItems.

        源ip

        :return: The sip of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        """Sets the sip of this ListEventResponseBodyItems.

        源ip

        :param sip: The sip of this ListEventResponseBodyItems.
        :type: str
        """
        self._sip = sip

    @property
    def host(self):
        """Gets the host of this ListEventResponseBodyItems.

        域名

        :return: The host of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ListEventResponseBodyItems.

        域名

        :param host: The host of this ListEventResponseBodyItems.
        :type: str
        """
        self._host = host

    @property
    def url(self):
        """Gets the url of this ListEventResponseBodyItems.

        攻击的url链接

        :return: The url of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ListEventResponseBodyItems.

        攻击的url链接

        :param url: The url of this ListEventResponseBodyItems.
        :type: str
        """
        self._url = url

    @property
    def attack(self):
        """Gets the attack of this ListEventResponseBodyItems.

        攻击类型

        :return: The attack of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._attack

    @attack.setter
    def attack(self, attack):
        """Sets the attack of this ListEventResponseBodyItems.

        攻击类型

        :param attack: The attack of this ListEventResponseBodyItems.
        :type: str
        """
        self._attack = attack

    @property
    def rule(self):
        """Gets the rule of this ListEventResponseBodyItems.

        命中的规则id

        :return: The rule of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this ListEventResponseBodyItems.

        命中的规则id

        :param rule: The rule of this ListEventResponseBodyItems.
        :type: str
        """
        self._rule = rule

    @property
    def payload(self):
        """Gets the payload of this ListEventResponseBodyItems.

        命中的载荷

        :return: The payload of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ListEventResponseBodyItems.

        命中的载荷

        :param payload: The payload of this ListEventResponseBodyItems.
        :type: str
        """
        self._payload = payload

    @property
    def action(self):
        """Gets the action of this ListEventResponseBodyItems.

        防护动作

        :return: The action of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListEventResponseBodyItems.

        防护动作

        :param action: The action of this ListEventResponseBodyItems.
        :type: str
        """
        self._action = action

    @property
    def request_line(self):
        """Gets the request_line of this ListEventResponseBodyItems.

        请求方法和路径

        :return: The request_line of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._request_line

    @request_line.setter
    def request_line(self, request_line):
        """Sets the request_line of this ListEventResponseBodyItems.

        请求方法和路径

        :param request_line: The request_line of this ListEventResponseBodyItems.
        :type: str
        """
        self._request_line = request_line

    @property
    def headers(self):
        """Gets the headers of this ListEventResponseBodyItems.


        :return: The headers of this ListEventResponseBodyItems.
        :rtype: ListEventResponseBodyHeaders
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ListEventResponseBodyItems.


        :param headers: The headers of this ListEventResponseBodyItems.
        :type: ListEventResponseBodyHeaders
        """
        self._headers = headers

    @property
    def cookie(self):
        """Gets the cookie of this ListEventResponseBodyItems.

        请求cookie

        :return: The cookie of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._cookie

    @cookie.setter
    def cookie(self, cookie):
        """Sets the cookie of this ListEventResponseBodyItems.

        请求cookie

        :param cookie: The cookie of this ListEventResponseBodyItems.
        :type: str
        """
        self._cookie = cookie

    @property
    def status(self):
        """Gets the status of this ListEventResponseBodyItems.

        响应码状态

        :return: The status of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListEventResponseBodyItems.

        响应码状态

        :param status: The status of this ListEventResponseBodyItems.
        :type: str
        """
        self._status = status

    @property
    def region(self):
        """Gets the region of this ListEventResponseBodyItems.

        区域

        :return: The region of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListEventResponseBodyItems.

        区域

        :param region: The region of this ListEventResponseBodyItems.
        :type: str
        """
        self._region = region

    @property
    def host_id(self):
        """Gets the host_id of this ListEventResponseBodyItems.

        域名id

        :return: The host_id of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListEventResponseBodyItems.

        域名id

        :param host_id: The host_id of this ListEventResponseBodyItems.
        :type: str
        """
        self._host_id = host_id

    @property
    def response_time(self):
        """Gets the response_time of this ListEventResponseBodyItems.

        响应时长

        :return: The response_time of this ListEventResponseBodyItems.
        :rtype: int
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """Sets the response_time of this ListEventResponseBodyItems.

        响应时长

        :param response_time: The response_time of this ListEventResponseBodyItems.
        :type: int
        """
        self._response_time = response_time

    @property
    def response_size(self):
        """Gets the response_size of this ListEventResponseBodyItems.

        响应体大小

        :return: The response_size of this ListEventResponseBodyItems.
        :rtype: int
        """
        return self._response_size

    @response_size.setter
    def response_size(self, response_size):
        """Sets the response_size of this ListEventResponseBodyItems.

        响应体大小

        :param response_size: The response_size of this ListEventResponseBodyItems.
        :type: int
        """
        self._response_size = response_size

    @property
    def response_body(self):
        """Gets the response_body of this ListEventResponseBodyItems.

        响应体

        :return: The response_body of this ListEventResponseBodyItems.
        :rtype: str
        """
        return self._response_body

    @response_body.setter
    def response_body(self, response_body):
        """Sets the response_body of this ListEventResponseBodyItems.

        响应体

        :param response_body: The response_body of this ListEventResponseBodyItems.
        :type: str
        """
        self._response_body = response_body

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
        if not isinstance(other, ListEventResponseBodyItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
