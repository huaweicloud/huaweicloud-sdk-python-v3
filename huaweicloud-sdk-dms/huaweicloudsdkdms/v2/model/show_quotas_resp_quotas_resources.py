# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotasRespQuotasResources:

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
        'used': 'int',
        'min': 'int',
        'max': 'int'
    }

    attribute_map = {
        'type': 'type',
        'quota': 'quota',
        'used': 'used',
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, type=None, quota=None, used=None, min=None, max=None):
        """ShowQuotasRespQuotasResources

        The model defined in huaweicloud sdk

        :param type: 配额名称。
        :type type: str
        :param quota: 配额数量。
        :type quota: int
        :param used: 已使用的数量。
        :type used: int
        :param min: 配额调整的最小值。
        :type min: int
        :param max: 配额调整的最大值。
        :type max: int
        """
        
        

        self._type = None
        self._quota = None
        self._used = None
        self._min = None
        self._max = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def type(self):
        """Gets the type of this ShowQuotasRespQuotasResources.

        配额名称。

        :return: The type of this ShowQuotasRespQuotasResources.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowQuotasRespQuotasResources.

        配额名称。

        :param type: The type of this ShowQuotasRespQuotasResources.
        :type type: str
        """
        self._type = type

    @property
    def quota(self):
        """Gets the quota of this ShowQuotasRespQuotasResources.

        配额数量。

        :return: The quota of this ShowQuotasRespQuotasResources.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ShowQuotasRespQuotasResources.

        配额数量。

        :param quota: The quota of this ShowQuotasRespQuotasResources.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        """Gets the used of this ShowQuotasRespQuotasResources.

        已使用的数量。

        :return: The used of this ShowQuotasRespQuotasResources.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ShowQuotasRespQuotasResources.

        已使用的数量。

        :param used: The used of this ShowQuotasRespQuotasResources.
        :type used: int
        """
        self._used = used

    @property
    def min(self):
        """Gets the min of this ShowQuotasRespQuotasResources.

        配额调整的最小值。

        :return: The min of this ShowQuotasRespQuotasResources.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ShowQuotasRespQuotasResources.

        配额调整的最小值。

        :param min: The min of this ShowQuotasRespQuotasResources.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this ShowQuotasRespQuotasResources.

        配额调整的最大值。

        :return: The max of this ShowQuotasRespQuotasResources.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ShowQuotasRespQuotasResources.

        配额调整的最大值。

        :param max: The max of this ShowQuotasRespQuotasResources.
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
        if not isinstance(other, ShowQuotasRespQuotasResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
