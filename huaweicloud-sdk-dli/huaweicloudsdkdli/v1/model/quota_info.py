# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaInfo:

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
        'quota': 'int',
        'used': 'int'
    }

    attribute_map = {
        'type': 'type',
        'min': 'min',
        'max': 'max',
        'quota': 'quota',
        'used': 'used'
    }

    def __init__(self, type=None, min=None, max=None, quota=None, used=None):
        r"""QuotaInfo

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param min: 配额的最小值
        :type min: int
        :param max: 配额的最大值
        :type max: int
        :param quota: 目前的配额
        :type quota: int
        :param used: 已用的配额
        :type used: int
        """
        
        

        self._type = None
        self._min = None
        self._max = None
        self._quota = None
        self._used = None
        self.discriminator = None

        if type is not None:
            self.type = type
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
        r"""Gets the type of this QuotaInfo.

        :return: The type of this QuotaInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this QuotaInfo.

        :param type: The type of this QuotaInfo.
        :type type: str
        """
        self._type = type

    @property
    def min(self):
        r"""Gets the min of this QuotaInfo.

        配额的最小值

        :return: The min of this QuotaInfo.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this QuotaInfo.

        配额的最小值

        :param min: The min of this QuotaInfo.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this QuotaInfo.

        配额的最大值

        :return: The max of this QuotaInfo.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this QuotaInfo.

        配额的最大值

        :param max: The max of this QuotaInfo.
        :type max: int
        """
        self._max = max

    @property
    def quota(self):
        r"""Gets the quota of this QuotaInfo.

        目前的配额

        :return: The quota of this QuotaInfo.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this QuotaInfo.

        目前的配额

        :param quota: The quota of this QuotaInfo.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this QuotaInfo.

        已用的配额

        :return: The used of this QuotaInfo.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this QuotaInfo.

        已用的配额

        :param used: The used of this QuotaInfo.
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
        if not isinstance(other, QuotaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
