# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Quota:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_key': 'str',
        'quota_limit': 'int',
        'used': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'quota_key': 'quota_key',
        'quota_limit': 'quota_limit',
        'used': 'used',
        'unit': 'unit'
    }

    def __init__(self, quota_key=None, quota_limit=None, used=None, unit=None):
        """Quota

        The model defined in huaweicloud sdk

        :param quota_key: 配额类型
        :type quota_key: str
        :param quota_limit: 可用的配额数，-1 代表不受限制
        :type quota_limit: int
        :param used: 已使用的配额数量
        :type used: int
        :param unit: 用量单位
        :type unit: str
        """
        
        

        self._quota_key = None
        self._quota_limit = None
        self._used = None
        self._unit = None
        self.discriminator = None

        if quota_key is not None:
            self.quota_key = quota_key
        if quota_limit is not None:
            self.quota_limit = quota_limit
        if used is not None:
            self.used = used
        if unit is not None:
            self.unit = unit

    @property
    def quota_key(self):
        """Gets the quota_key of this Quota.

        配额类型

        :return: The quota_key of this Quota.
        :rtype: str
        """
        return self._quota_key

    @quota_key.setter
    def quota_key(self, quota_key):
        """Sets the quota_key of this Quota.

        配额类型

        :param quota_key: The quota_key of this Quota.
        :type quota_key: str
        """
        self._quota_key = quota_key

    @property
    def quota_limit(self):
        """Gets the quota_limit of this Quota.

        可用的配额数，-1 代表不受限制

        :return: The quota_limit of this Quota.
        :rtype: int
        """
        return self._quota_limit

    @quota_limit.setter
    def quota_limit(self, quota_limit):
        """Sets the quota_limit of this Quota.

        可用的配额数，-1 代表不受限制

        :param quota_limit: The quota_limit of this Quota.
        :type quota_limit: int
        """
        self._quota_limit = quota_limit

    @property
    def used(self):
        """Gets the used of this Quota.

        已使用的配额数量

        :return: The used of this Quota.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this Quota.

        已使用的配额数量

        :param used: The used of this Quota.
        :type used: int
        """
        self._used = used

    @property
    def unit(self):
        """Gets the unit of this Quota.

        用量单位

        :return: The unit of this Quota.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Quota.

        用量单位

        :param unit: The unit of this Quota.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, Quota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
