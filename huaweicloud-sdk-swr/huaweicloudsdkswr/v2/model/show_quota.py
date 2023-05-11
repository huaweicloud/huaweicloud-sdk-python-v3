# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuota:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_limit': 'int',
        'quota_key': 'str',
        'unit': 'str',
        'used': 'int'
    }

    attribute_map = {
        'quota_limit': 'quota_limit',
        'quota_key': 'quota_key',
        'unit': 'unit',
        'used': 'used'
    }

    def __init__(self, quota_limit=None, quota_key=None, unit=None, used=None):
        """ShowQuota

        The model defined in huaweicloud sdk

        :param quota_limit: 配额限制
        :type quota_limit: int
        :param quota_key: 配额类型
        :type quota_key: str
        :param unit: 单位 
        :type unit: str
        :param used: 已用配额
        :type used: int
        """
        
        

        self._quota_limit = None
        self._quota_key = None
        self._unit = None
        self._used = None
        self.discriminator = None

        self.quota_limit = quota_limit
        self.quota_key = quota_key
        self.unit = unit
        self.used = used

    @property
    def quota_limit(self):
        """Gets the quota_limit of this ShowQuota.

        配额限制

        :return: The quota_limit of this ShowQuota.
        :rtype: int
        """
        return self._quota_limit

    @quota_limit.setter
    def quota_limit(self, quota_limit):
        """Sets the quota_limit of this ShowQuota.

        配额限制

        :param quota_limit: The quota_limit of this ShowQuota.
        :type quota_limit: int
        """
        self._quota_limit = quota_limit

    @property
    def quota_key(self):
        """Gets the quota_key of this ShowQuota.

        配额类型

        :return: The quota_key of this ShowQuota.
        :rtype: str
        """
        return self._quota_key

    @quota_key.setter
    def quota_key(self, quota_key):
        """Sets the quota_key of this ShowQuota.

        配额类型

        :param quota_key: The quota_key of this ShowQuota.
        :type quota_key: str
        """
        self._quota_key = quota_key

    @property
    def unit(self):
        """Gets the unit of this ShowQuota.

        单位 

        :return: The unit of this ShowQuota.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ShowQuota.

        单位 

        :param unit: The unit of this ShowQuota.
        :type unit: str
        """
        self._unit = unit

    @property
    def used(self):
        """Gets the used of this ShowQuota.

        已用配额

        :return: The used of this ShowQuota.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ShowQuota.

        已用配额

        :param used: The used of this ShowQuota.
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
        if not isinstance(other, ShowQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
