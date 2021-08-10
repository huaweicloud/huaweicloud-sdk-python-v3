# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventResponseBodyItems:


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
        'payload': 'str',
        'action': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'time': 'time',
        'policyid': 'policyid',
        'sip': 'sip',
        'host': 'host',
        'url': 'url',
        'attack': 'attack',
        'rule': 'rule',
        'payload': 'payload',
        'action': 'action',
        'timestamp': 'timestamp'
    }

    def __init__(self, time=None, policyid=None, sip=None, host=None, url=None, attack=None, rule=None, payload=None, action=None, timestamp=None):
        """ShowEventResponseBodyItems - a model defined in huaweicloud sdk"""
        
        

        self._time = None
        self._policyid = None
        self._sip = None
        self._host = None
        self._url = None
        self._attack = None
        self._rule = None
        self._payload = None
        self._action = None
        self._timestamp = None
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
        if payload is not None:
            self.payload = payload
        if action is not None:
            self.action = action
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def time(self):
        """Gets the time of this ShowEventResponseBodyItems.

        次数

        :return: The time of this ShowEventResponseBodyItems.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ShowEventResponseBodyItems.

        次数

        :param time: The time of this ShowEventResponseBodyItems.
        :type: int
        """
        self._time = time

    @property
    def policyid(self):
        """Gets the policyid of this ShowEventResponseBodyItems.

        策略id

        :return: The policyid of this ShowEventResponseBodyItems.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this ShowEventResponseBodyItems.

        策略id

        :param policyid: The policyid of this ShowEventResponseBodyItems.
        :type: str
        """
        self._policyid = policyid

    @property
    def sip(self):
        """Gets the sip of this ShowEventResponseBodyItems.

        源ip

        :return: The sip of this ShowEventResponseBodyItems.
        :rtype: str
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        """Sets the sip of this ShowEventResponseBodyItems.

        源ip

        :param sip: The sip of this ShowEventResponseBodyItems.
        :type: str
        """
        self._sip = sip

    @property
    def host(self):
        """Gets the host of this ShowEventResponseBodyItems.

        域名

        :return: The host of this ShowEventResponseBodyItems.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ShowEventResponseBodyItems.

        域名

        :param host: The host of this ShowEventResponseBodyItems.
        :type: str
        """
        self._host = host

    @property
    def url(self):
        """Gets the url of this ShowEventResponseBodyItems.

        攻击的url链接

        :return: The url of this ShowEventResponseBodyItems.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ShowEventResponseBodyItems.

        攻击的url链接

        :param url: The url of this ShowEventResponseBodyItems.
        :type: str
        """
        self._url = url

    @property
    def attack(self):
        """Gets the attack of this ShowEventResponseBodyItems.

        攻击类型

        :return: The attack of this ShowEventResponseBodyItems.
        :rtype: str
        """
        return self._attack

    @attack.setter
    def attack(self, attack):
        """Sets the attack of this ShowEventResponseBodyItems.

        攻击类型

        :param attack: The attack of this ShowEventResponseBodyItems.
        :type: str
        """
        self._attack = attack

    @property
    def rule(self):
        """Gets the rule of this ShowEventResponseBodyItems.

        命中的规则id

        :return: The rule of this ShowEventResponseBodyItems.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this ShowEventResponseBodyItems.

        命中的规则id

        :param rule: The rule of this ShowEventResponseBodyItems.
        :type: str
        """
        self._rule = rule

    @property
    def payload(self):
        """Gets the payload of this ShowEventResponseBodyItems.

        命中的载荷

        :return: The payload of this ShowEventResponseBodyItems.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ShowEventResponseBodyItems.

        命中的载荷

        :param payload: The payload of this ShowEventResponseBodyItems.
        :type: str
        """
        self._payload = payload

    @property
    def action(self):
        """Gets the action of this ShowEventResponseBodyItems.

        防护动作

        :return: The action of this ShowEventResponseBodyItems.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ShowEventResponseBodyItems.

        防护动作

        :param action: The action of this ShowEventResponseBodyItems.
        :type: str
        """
        self._action = action

    @property
    def timestamp(self):
        """Gets the timestamp of this ShowEventResponseBodyItems.

        时间戳

        :return: The timestamp of this ShowEventResponseBodyItems.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ShowEventResponseBodyItems.

        时间戳

        :param timestamp: The timestamp of this ShowEventResponseBodyItems.
        :type: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, ShowEventResponseBodyItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
