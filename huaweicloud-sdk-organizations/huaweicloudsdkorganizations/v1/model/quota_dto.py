# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaDto:

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
        'quota': 'int',
        'min': 'int',
        'max': 'int',
        'used': 'int'
    }

    attribute_map = {
        'type': 'type',
        'quota': 'quota',
        'min': 'min',
        'max': 'max',
        'used': 'used'
    }

    def __init__(self, type=None, quota=None, min=None, max=None, used=None):
        """QuotaDto

        The model defined in huaweicloud sdk

        :param type: 配额类型，account账户，organizational_unit组织单元，policy策略。
        :type type: str
        :param quota: 配额数量。
        :type quota: int
        :param min: 最小配额。
        :type min: int
        :param max: 最大配额。
        :type max: int
        :param used: 已使用数量。
        :type used: int
        """
        
        

        self._type = None
        self._quota = None
        self._min = None
        self._max = None
        self._used = None
        self.discriminator = None

        self.type = type
        self.quota = quota
        self.min = min
        self.max = max
        self.used = used

    @property
    def type(self):
        """Gets the type of this QuotaDto.

        配额类型，account账户，organizational_unit组织单元，policy策略。

        :return: The type of this QuotaDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotaDto.

        配额类型，account账户，organizational_unit组织单元，policy策略。

        :param type: The type of this QuotaDto.
        :type type: str
        """
        self._type = type

    @property
    def quota(self):
        """Gets the quota of this QuotaDto.

        配额数量。

        :return: The quota of this QuotaDto.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this QuotaDto.

        配额数量。

        :param quota: The quota of this QuotaDto.
        :type quota: int
        """
        self._quota = quota

    @property
    def min(self):
        """Gets the min of this QuotaDto.

        最小配额。

        :return: The min of this QuotaDto.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this QuotaDto.

        最小配额。

        :param min: The min of this QuotaDto.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this QuotaDto.

        最大配额。

        :return: The max of this QuotaDto.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this QuotaDto.

        最大配额。

        :param max: The max of this QuotaDto.
        :type max: int
        """
        self._max = max

    @property
    def used(self):
        """Gets the used of this QuotaDto.

        已使用数量。

        :return: The used of this QuotaDto.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this QuotaDto.

        已使用数量。

        :param used: The used of this QuotaDto.
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
        if not isinstance(other, QuotaDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
