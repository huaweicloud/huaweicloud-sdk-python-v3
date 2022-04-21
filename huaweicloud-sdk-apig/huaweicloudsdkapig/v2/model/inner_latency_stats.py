# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InnerLatencyStats:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'max_inner_latency': 'int',
        'avg_inner_latency': 'float'
    }

    attribute_map = {
        'max_inner_latency': 'max_inner_latency',
        'avg_inner_latency': 'avg_inner_latency'
    }

    def __init__(self, max_inner_latency=None, avg_inner_latency=None):
        """InnerLatencyStats

        The model defined in huaweicloud sdk

        :param max_inner_latency: 最大网关内部延时  单位：ms
        :type max_inner_latency: int
        :param avg_inner_latency: 平均网关内部延时  单位：ms
        :type avg_inner_latency: float
        """
        
        

        self._max_inner_latency = None
        self._avg_inner_latency = None
        self.discriminator = None

        if max_inner_latency is not None:
            self.max_inner_latency = max_inner_latency
        if avg_inner_latency is not None:
            self.avg_inner_latency = avg_inner_latency

    @property
    def max_inner_latency(self):
        """Gets the max_inner_latency of this InnerLatencyStats.

        最大网关内部延时  单位：ms

        :return: The max_inner_latency of this InnerLatencyStats.
        :rtype: int
        """
        return self._max_inner_latency

    @max_inner_latency.setter
    def max_inner_latency(self, max_inner_latency):
        """Sets the max_inner_latency of this InnerLatencyStats.

        最大网关内部延时  单位：ms

        :param max_inner_latency: The max_inner_latency of this InnerLatencyStats.
        :type max_inner_latency: int
        """
        self._max_inner_latency = max_inner_latency

    @property
    def avg_inner_latency(self):
        """Gets the avg_inner_latency of this InnerLatencyStats.

        平均网关内部延时  单位：ms

        :return: The avg_inner_latency of this InnerLatencyStats.
        :rtype: float
        """
        return self._avg_inner_latency

    @avg_inner_latency.setter
    def avg_inner_latency(self, avg_inner_latency):
        """Sets the avg_inner_latency of this InnerLatencyStats.

        平均网关内部延时  单位：ms

        :param avg_inner_latency: The avg_inner_latency of this InnerLatencyStats.
        :type avg_inner_latency: float
        """
        self._avg_inner_latency = avg_inner_latency

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
        if not isinstance(other, InnerLatencyStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
