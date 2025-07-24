# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareTypesAttributionIops:

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
        'min': 'int'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min'
    }

    def __init__(self, max=None, min=None):
        r"""ShareTypesAttributionIops

        The model defined in huaweicloud sdk

        :param max: 最大iops
        :type max: int
        :param min: 最小iops
        :type min: int
        """
        
        

        self._max = None
        self._min = None
        self.discriminator = None

        if max is not None:
            self.max = max
        if min is not None:
            self.min = min

    @property
    def max(self):
        r"""Gets the max of this ShareTypesAttributionIops.

        最大iops

        :return: The max of this ShareTypesAttributionIops.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this ShareTypesAttributionIops.

        最大iops

        :param max: The max of this ShareTypesAttributionIops.
        :type max: int
        """
        self._max = max

    @property
    def min(self):
        r"""Gets the min of this ShareTypesAttributionIops.

        最小iops

        :return: The min of this ShareTypesAttributionIops.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this ShareTypesAttributionIops.

        最小iops

        :param min: The min of this ShareTypesAttributionIops.
        :type min: int
        """
        self._min = min

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
        if not isinstance(other, ShareTypesAttributionIops):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
