# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaOuterResource:

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
        'min': 'int',
        'max': 'int',
        'quota': 'int'
    }

    attribute_map = {
        'type': 'type',
        'min': 'min',
        'max': 'max',
        'quota': 'quota'
    }

    def __init__(self, type=None, min=None, max=None, quota=None):
        r"""QuotaOuterResource

        The model defined in huaweicloud sdk

        :param type: 配额标识。
        :type type: str
        :param min: 配额的最小阈值。
        :type min: int
        :param max: 配额的最大阈值。
        :type max: int
        :param quota: 配额大小。
        :type quota: int
        """
        
        

        self._type = None
        self._min = None
        self._max = None
        self._quota = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if quota is not None:
            self.quota = quota

    @property
    def type(self):
        r"""Gets the type of this QuotaOuterResource.

        配额标识。

        :return: The type of this QuotaOuterResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this QuotaOuterResource.

        配额标识。

        :param type: The type of this QuotaOuterResource.
        :type type: str
        """
        self._type = type

    @property
    def min(self):
        r"""Gets the min of this QuotaOuterResource.

        配额的最小阈值。

        :return: The min of this QuotaOuterResource.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this QuotaOuterResource.

        配额的最小阈值。

        :param min: The min of this QuotaOuterResource.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this QuotaOuterResource.

        配额的最大阈值。

        :return: The max of this QuotaOuterResource.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this QuotaOuterResource.

        配额的最大阈值。

        :param max: The max of this QuotaOuterResource.
        :type max: int
        """
        self._max = max

    @property
    def quota(self):
        r"""Gets the quota of this QuotaOuterResource.

        配额大小。

        :return: The quota of this QuotaOuterResource.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this QuotaOuterResource.

        配额大小。

        :param quota: The quota of this QuotaOuterResource.
        :type quota: int
        """
        self._quota = quota

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
        if not isinstance(other, QuotaOuterResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
