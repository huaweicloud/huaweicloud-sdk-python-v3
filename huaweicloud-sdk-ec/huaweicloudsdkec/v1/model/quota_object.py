# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaObject:

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
        'unit': 'str',
        'min': 'int',
        'max': 'int',
        'quota': 'int',
        'used': 'int'
    }

    attribute_map = {
        'type': 'type',
        'unit': 'unit',
        'min': 'min',
        'max': 'max',
        'quota': 'quota',
        'used': 'used'
    }

    def __init__(self, type=None, unit=None, min=None, max=None, quota=None, used=None):
        """QuotaObject

        The model defined in huaweicloud sdk

        :param type: 配额类型
        :type type: str
        :param unit: 单位
        :type unit: str
        :param min: 最小值
        :type min: int
        :param max: 最大值
        :type max: int
        :param quota: 配额上限
        :type quota: int
        :param used: 已使用数
        :type used: int
        """
        
        

        self._type = None
        self._unit = None
        self._min = None
        self._max = None
        self._quota = None
        self._used = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if unit is not None:
            self.unit = unit
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used

    @property
    def type(self):
        """Gets the type of this QuotaObject.

        配额类型

        :return: The type of this QuotaObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotaObject.

        配额类型

        :param type: The type of this QuotaObject.
        :type type: str
        """
        self._type = type

    @property
    def unit(self):
        """Gets the unit of this QuotaObject.

        单位

        :return: The unit of this QuotaObject.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this QuotaObject.

        单位

        :param unit: The unit of this QuotaObject.
        :type unit: str
        """
        self._unit = unit

    @property
    def min(self):
        """Gets the min of this QuotaObject.

        最小值

        :return: The min of this QuotaObject.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this QuotaObject.

        最小值

        :param min: The min of this QuotaObject.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this QuotaObject.

        最大值

        :return: The max of this QuotaObject.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this QuotaObject.

        最大值

        :param max: The max of this QuotaObject.
        :type max: int
        """
        self._max = max

    @property
    def quota(self):
        """Gets the quota of this QuotaObject.

        配额上限

        :return: The quota of this QuotaObject.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this QuotaObject.

        配额上限

        :param quota: The quota of this QuotaObject.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        """Gets the used of this QuotaObject.

        已使用数

        :return: The used of this QuotaObject.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this QuotaObject.

        已使用数

        :param used: The used of this QuotaObject.
        :type used: int
        """
        self._used = used

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
        if not isinstance(other, QuotaObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
