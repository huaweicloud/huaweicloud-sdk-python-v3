# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaResourceParams:

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
        'used': 'int',
        'quota': 'int',
        'min': 'int',
        'max': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'quota': 'quota',
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, type=None, used=None, quota=None, min=None, max=None):
        """QuotaResourceParams

        The model defined in huaweicloud sdk

        :param type: 资源类型server_groups：表示保护组资源类型。replications：表示复制对资源类型。
        :type type: str
        :param used: 已经使用的资源个数。
        :type used: int
        :param quota: 资源配额。-1：表示无穷大。
        :type quota: int
        :param min: 设置该资源配额允许的最小值。
        :type min: int
        :param max: 设置该资源配额允许的最大值。-1：表示无穷大。
        :type max: int
        """
        
        

        self._type = None
        self._used = None
        self._quota = None
        self._min = None
        self._max = None
        self.discriminator = None

        self.type = type
        self.used = used
        self.quota = quota
        self.min = min
        self.max = max

    @property
    def type(self):
        """Gets the type of this QuotaResourceParams.

        资源类型server_groups：表示保护组资源类型。replications：表示复制对资源类型。

        :return: The type of this QuotaResourceParams.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotaResourceParams.

        资源类型server_groups：表示保护组资源类型。replications：表示复制对资源类型。

        :param type: The type of this QuotaResourceParams.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this QuotaResourceParams.

        已经使用的资源个数。

        :return: The used of this QuotaResourceParams.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this QuotaResourceParams.

        已经使用的资源个数。

        :param used: The used of this QuotaResourceParams.
        :type used: int
        """
        self._used = used

    @property
    def quota(self):
        """Gets the quota of this QuotaResourceParams.

        资源配额。-1：表示无穷大。

        :return: The quota of this QuotaResourceParams.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this QuotaResourceParams.

        资源配额。-1：表示无穷大。

        :param quota: The quota of this QuotaResourceParams.
        :type quota: int
        """
        self._quota = quota

    @property
    def min(self):
        """Gets the min of this QuotaResourceParams.

        设置该资源配额允许的最小值。

        :return: The min of this QuotaResourceParams.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this QuotaResourceParams.

        设置该资源配额允许的最小值。

        :param min: The min of this QuotaResourceParams.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this QuotaResourceParams.

        设置该资源配额允许的最大值。-1：表示无穷大。

        :return: The max of this QuotaResourceParams.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this QuotaResourceParams.

        设置该资源配额允许的最大值。-1：表示无穷大。

        :param max: The max of this QuotaResourceParams.
        :type max: int
        """
        self._max = max

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
        if not isinstance(other, QuotaResourceParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
