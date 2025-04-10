# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDDoSAttackEventRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int',
        'ip': 'str',
        'attack_flow_low': 'str',
        'attack_flow_up': 'str',
        'attack_status': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit',
        'ip': 'ip',
        'attack_flow_low': 'attack_flow_low',
        'attack_flow_up': 'attack_flow_up',
        'attack_status': 'attack_status'
    }

    def __init__(self, start_time=None, end_time=None, offset=None, limit=None, ip=None, attack_flow_low=None, attack_flow_up=None, attack_status=None):
        r"""ListDDoSAttackEventRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 开始时间（毫秒时间戳）
        :type start_time: str
        :param end_time: 结束时间（毫秒时间戳）
        :type end_time: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 限制条数，范围1-100
        :type limit: int
        :param ip: 高防ip
        :type ip: str
        :param attack_flow_low: 攻击流量最小值
        :type attack_flow_low: str
        :param attack_flow_up: 攻击流量最大值
        :type attack_flow_up: str
        :param attack_status: 攻击状态：attack-攻击; normal-结束攻击
        :type attack_status: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self._ip = None
        self._attack_flow_low = None
        self._attack_flow_up = None
        self._attack_status = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.offset = offset
        self.limit = limit
        self.ip = ip
        if attack_flow_low is not None:
            self.attack_flow_low = attack_flow_low
        if attack_flow_up is not None:
            self.attack_flow_up = attack_flow_up
        if attack_status is not None:
            self.attack_status = attack_status

    @property
    def start_time(self):
        r"""Gets the start_time of this ListDDoSAttackEventRequestBody.

        开始时间（毫秒时间戳）

        :return: The start_time of this ListDDoSAttackEventRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListDDoSAttackEventRequestBody.

        开始时间（毫秒时间戳）

        :param start_time: The start_time of this ListDDoSAttackEventRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListDDoSAttackEventRequestBody.

        结束时间（毫秒时间戳）

        :return: The end_time of this ListDDoSAttackEventRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListDDoSAttackEventRequestBody.

        结束时间（毫秒时间戳）

        :param end_time: The end_time of this ListDDoSAttackEventRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListDDoSAttackEventRequestBody.

        偏移量

        :return: The offset of this ListDDoSAttackEventRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDDoSAttackEventRequestBody.

        偏移量

        :param offset: The offset of this ListDDoSAttackEventRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDDoSAttackEventRequestBody.

        限制条数，范围1-100

        :return: The limit of this ListDDoSAttackEventRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDDoSAttackEventRequestBody.

        限制条数，范围1-100

        :param limit: The limit of this ListDDoSAttackEventRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def ip(self):
        r"""Gets the ip of this ListDDoSAttackEventRequestBody.

        高防ip

        :return: The ip of this ListDDoSAttackEventRequestBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ListDDoSAttackEventRequestBody.

        高防ip

        :param ip: The ip of this ListDDoSAttackEventRequestBody.
        :type ip: str
        """
        self._ip = ip

    @property
    def attack_flow_low(self):
        r"""Gets the attack_flow_low of this ListDDoSAttackEventRequestBody.

        攻击流量最小值

        :return: The attack_flow_low of this ListDDoSAttackEventRequestBody.
        :rtype: str
        """
        return self._attack_flow_low

    @attack_flow_low.setter
    def attack_flow_low(self, attack_flow_low):
        r"""Sets the attack_flow_low of this ListDDoSAttackEventRequestBody.

        攻击流量最小值

        :param attack_flow_low: The attack_flow_low of this ListDDoSAttackEventRequestBody.
        :type attack_flow_low: str
        """
        self._attack_flow_low = attack_flow_low

    @property
    def attack_flow_up(self):
        r"""Gets the attack_flow_up of this ListDDoSAttackEventRequestBody.

        攻击流量最大值

        :return: The attack_flow_up of this ListDDoSAttackEventRequestBody.
        :rtype: str
        """
        return self._attack_flow_up

    @attack_flow_up.setter
    def attack_flow_up(self, attack_flow_up):
        r"""Sets the attack_flow_up of this ListDDoSAttackEventRequestBody.

        攻击流量最大值

        :param attack_flow_up: The attack_flow_up of this ListDDoSAttackEventRequestBody.
        :type attack_flow_up: str
        """
        self._attack_flow_up = attack_flow_up

    @property
    def attack_status(self):
        r"""Gets the attack_status of this ListDDoSAttackEventRequestBody.

        攻击状态：attack-攻击; normal-结束攻击

        :return: The attack_status of this ListDDoSAttackEventRequestBody.
        :rtype: str
        """
        return self._attack_status

    @attack_status.setter
    def attack_status(self, attack_status):
        r"""Sets the attack_status of this ListDDoSAttackEventRequestBody.

        攻击状态：attack-攻击; normal-结束攻击

        :param attack_status: The attack_status of this ListDDoSAttackEventRequestBody.
        :type attack_status: str
        """
        self._attack_status = attack_status

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
        if not isinstance(other, ListDDoSAttackEventRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
