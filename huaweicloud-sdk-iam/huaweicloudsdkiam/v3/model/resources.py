# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max': 'int',
        'min': 'int',
        'quota': 'int',
        'type': 'str',
        'used': 'int'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min',
        'quota': 'quota',
        'type': 'type',
        'used': 'used'
    }

    def __init__(self, max=None, min=None, quota=None, type=None, used=None):
        """Resources

        The model defined in huaweicloud sdk

        :param max: 配额最大值。
        :type max: int
        :param min: 配额最小值。
        :type min: int
        :param quota: 当前配额。
        :type quota: int
        :param type: 配额类型。
        :type type: str
        :param used: 已使用的配额。
        :type used: int
        """
        
        

        self._max = None
        self._min = None
        self._quota = None
        self._type = None
        self._used = None
        self.discriminator = None

        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if quota is not None:
            self.quota = quota
        if type is not None:
            self.type = type
        if used is not None:
            self.used = used

    @property
    def max(self):
        """Gets the max of this Resources.

        配额最大值。

        :return: The max of this Resources.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this Resources.

        配额最大值。

        :param max: The max of this Resources.
        :type max: int
        """
        self._max = max

    @property
    def min(self):
        """Gets the min of this Resources.

        配额最小值。

        :return: The min of this Resources.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this Resources.

        配额最小值。

        :param min: The min of this Resources.
        :type min: int
        """
        self._min = min

    @property
    def quota(self):
        """Gets the quota of this Resources.

        当前配额。

        :return: The quota of this Resources.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this Resources.

        当前配额。

        :param quota: The quota of this Resources.
        :type quota: int
        """
        self._quota = quota

    @property
    def type(self):
        """Gets the type of this Resources.

        配额类型。

        :return: The type of this Resources.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Resources.

        配额类型。

        :param type: The type of this Resources.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this Resources.

        已使用的配额。

        :return: The used of this Resources.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this Resources.

        已使用的配额。

        :param used: The used of this Resources.
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
        if not isinstance(other, Resources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
