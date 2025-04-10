# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LatencyStats:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_latency': 'int',
        'avg_latency': 'float'
    }

    attribute_map = {
        'max_latency': 'max_latency',
        'avg_latency': 'avg_latency'
    }

    def __init__(self, max_latency=None, avg_latency=None):
        r"""LatencyStats

        The model defined in huaweicloud sdk

        :param max_latency: 最大延时  单位：ms
        :type max_latency: int
        :param avg_latency: 平均延时  单位：ms
        :type avg_latency: float
        """
        
        

        self._max_latency = None
        self._avg_latency = None
        self.discriminator = None

        if max_latency is not None:
            self.max_latency = max_latency
        if avg_latency is not None:
            self.avg_latency = avg_latency

    @property
    def max_latency(self):
        r"""Gets the max_latency of this LatencyStats.

        最大延时  单位：ms

        :return: The max_latency of this LatencyStats.
        :rtype: int
        """
        return self._max_latency

    @max_latency.setter
    def max_latency(self, max_latency):
        r"""Sets the max_latency of this LatencyStats.

        最大延时  单位：ms

        :param max_latency: The max_latency of this LatencyStats.
        :type max_latency: int
        """
        self._max_latency = max_latency

    @property
    def avg_latency(self):
        r"""Gets the avg_latency of this LatencyStats.

        平均延时  单位：ms

        :return: The avg_latency of this LatencyStats.
        :rtype: float
        """
        return self._avg_latency

    @avg_latency.setter
    def avg_latency(self, avg_latency):
        r"""Sets the avg_latency of this LatencyStats.

        平均延时  单位：ms

        :param avg_latency: The avg_latency of this LatencyStats.
        :type avg_latency: float
        """
        self._avg_latency = avg_latency

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
        if not isinstance(other, LatencyStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
