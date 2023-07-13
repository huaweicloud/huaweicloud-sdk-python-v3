# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PointValidityingDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min': 'int',
        'max': 'int'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, min=None, max=None):
        """PointValidityingDTO

        The model defined in huaweicloud sdk

        :param min: 点位上报值的最小值，小于该值则上报告警
        :type min: int
        :param max: 点位上报值的最大值，大于该值则上报告警
        :type max: int
        """
        
        

        self._min = None
        self._max = None
        self.discriminator = None

        self.min = min
        self.max = max

    @property
    def min(self):
        """Gets the min of this PointValidityingDTO.

        点位上报值的最小值，小于该值则上报告警

        :return: The min of this PointValidityingDTO.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this PointValidityingDTO.

        点位上报值的最小值，小于该值则上报告警

        :param min: The min of this PointValidityingDTO.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this PointValidityingDTO.

        点位上报值的最大值，大于该值则上报告警

        :return: The max of this PointValidityingDTO.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this PointValidityingDTO.

        点位上报值的最大值，大于该值则上报告警

        :param max: The max of this PointValidityingDTO.
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
        if not isinstance(other, PointValidityingDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
