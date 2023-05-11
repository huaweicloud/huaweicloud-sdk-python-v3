# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Validity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'value': 'int',
        'start_from': 'int'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'start_from': 'start_from'
    }

    def __init__(self, type=None, value=None, start_from=None):
        """Validity

        The model defined in huaweicloud sdk

        :param type: 有效期类型，为必填值：   - **YEAR** : 年（12个月）   - **MONTH** : 月（统一按31天）   - **DAY** : 日   - **HOUR** : 小时
        :type type: str
        :param value: 证书有效期值，与type对应的类型值，换算成年需满足以下规则：   - 根CA，有效期小于等于30年；   - 从属CA与私有证书，有效期小于等于20年。
        :type value: int
        :param start_from: 起始时间，为可选值:   - 格式为时间戳（毫秒级），如1645146939688代表2022-02-18 09:15:39；   - 不早于当前时间5分钟，即start_from &gt; (current_time - 5min)。
        :type start_from: int
        """
        
        

        self._type = None
        self._value = None
        self._start_from = None
        self.discriminator = None

        self.type = type
        self.value = value
        if start_from is not None:
            self.start_from = start_from

    @property
    def type(self):
        """Gets the type of this Validity.

        有效期类型，为必填值：   - **YEAR** : 年（12个月）   - **MONTH** : 月（统一按31天）   - **DAY** : 日   - **HOUR** : 小时

        :return: The type of this Validity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Validity.

        有效期类型，为必填值：   - **YEAR** : 年（12个月）   - **MONTH** : 月（统一按31天）   - **DAY** : 日   - **HOUR** : 小时

        :param type: The type of this Validity.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this Validity.

        证书有效期值，与type对应的类型值，换算成年需满足以下规则：   - 根CA，有效期小于等于30年；   - 从属CA与私有证书，有效期小于等于20年。

        :return: The value of this Validity.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Validity.

        证书有效期值，与type对应的类型值，换算成年需满足以下规则：   - 根CA，有效期小于等于30年；   - 从属CA与私有证书，有效期小于等于20年。

        :param value: The value of this Validity.
        :type value: int
        """
        self._value = value

    @property
    def start_from(self):
        """Gets the start_from of this Validity.

        起始时间，为可选值:   - 格式为时间戳（毫秒级），如1645146939688代表2022-02-18 09:15:39；   - 不早于当前时间5分钟，即start_from > (current_time - 5min)。

        :return: The start_from of this Validity.
        :rtype: int
        """
        return self._start_from

    @start_from.setter
    def start_from(self, start_from):
        """Sets the start_from of this Validity.

        起始时间，为可选值:   - 格式为时间戳（毫秒级），如1645146939688代表2022-02-18 09:15:39；   - 不早于当前时间5分钟，即start_from > (current_time - 5min)。

        :param start_from: The start_from of this Validity.
        :type start_from: int
        """
        self._start_from = start_from

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
        if not isinstance(other, Validity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
