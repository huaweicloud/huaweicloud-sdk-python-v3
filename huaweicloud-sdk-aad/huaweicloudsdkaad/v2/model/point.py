# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Point:

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
        'total': 'int',
        'attack': 'int',
        'basic': 'int',
        'cc': 'int',
        'custom_custom': 'int'
    }

    attribute_map = {
        'time': 'time',
        'total': 'total',
        'attack': 'attack',
        'basic': 'basic',
        'cc': 'cc',
        'custom_custom': 'custom_custom'
    }

    def __init__(self, time=None, total=None, attack=None, basic=None, cc=None, custom_custom=None):
        r"""Point

        The model defined in huaweicloud sdk

        :param time: 时间戳
        :type time: int
        :param total: 请求总量
        :type total: int
        :param attack: 攻击总量
        :type attack: int
        :param basic: web基础防护
        :type basic: int
        :param cc: 频率控制
        :type cc: int
        :param custom_custom: 精准防护
        :type custom_custom: int
        """
        
        

        self._time = None
        self._total = None
        self._attack = None
        self._basic = None
        self._cc = None
        self._custom_custom = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if total is not None:
            self.total = total
        if attack is not None:
            self.attack = attack
        if basic is not None:
            self.basic = basic
        if cc is not None:
            self.cc = cc
        if custom_custom is not None:
            self.custom_custom = custom_custom

    @property
    def time(self):
        r"""Gets the time of this Point.

        时间戳

        :return: The time of this Point.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this Point.

        时间戳

        :param time: The time of this Point.
        :type time: int
        """
        self._time = time

    @property
    def total(self):
        r"""Gets the total of this Point.

        请求总量

        :return: The total of this Point.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this Point.

        请求总量

        :param total: The total of this Point.
        :type total: int
        """
        self._total = total

    @property
    def attack(self):
        r"""Gets the attack of this Point.

        攻击总量

        :return: The attack of this Point.
        :rtype: int
        """
        return self._attack

    @attack.setter
    def attack(self, attack):
        r"""Sets the attack of this Point.

        攻击总量

        :param attack: The attack of this Point.
        :type attack: int
        """
        self._attack = attack

    @property
    def basic(self):
        r"""Gets the basic of this Point.

        web基础防护

        :return: The basic of this Point.
        :rtype: int
        """
        return self._basic

    @basic.setter
    def basic(self, basic):
        r"""Sets the basic of this Point.

        web基础防护

        :param basic: The basic of this Point.
        :type basic: int
        """
        self._basic = basic

    @property
    def cc(self):
        r"""Gets the cc of this Point.

        频率控制

        :return: The cc of this Point.
        :rtype: int
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        r"""Sets the cc of this Point.

        频率控制

        :param cc: The cc of this Point.
        :type cc: int
        """
        self._cc = cc

    @property
    def custom_custom(self):
        r"""Gets the custom_custom of this Point.

        精准防护

        :return: The custom_custom of this Point.
        :rtype: int
        """
        return self._custom_custom

    @custom_custom.setter
    def custom_custom(self, custom_custom):
        r"""Sets the custom_custom of this Point.

        精准防护

        :param custom_custom: The custom_custom of this Point.
        :type custom_custom: int
        """
        self._custom_custom = custom_custom

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
        if not isinstance(other, Point):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
