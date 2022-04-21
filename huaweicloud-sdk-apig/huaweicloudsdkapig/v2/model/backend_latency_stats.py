# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackendLatencyStats:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'max_backend_latency': 'int',
        'avg_backend_latency': 'float'
    }

    attribute_map = {
        'max_backend_latency': 'max_backend_latency',
        'avg_backend_latency': 'avg_backend_latency'
    }

    def __init__(self, max_backend_latency=None, avg_backend_latency=None):
        """BackendLatencyStats

        The model defined in huaweicloud sdk

        :param max_backend_latency: 最大后端延时
        :type max_backend_latency: int
        :param avg_backend_latency: 平均后端延时
        :type avg_backend_latency: float
        """
        
        

        self._max_backend_latency = None
        self._avg_backend_latency = None
        self.discriminator = None

        if max_backend_latency is not None:
            self.max_backend_latency = max_backend_latency
        if avg_backend_latency is not None:
            self.avg_backend_latency = avg_backend_latency

    @property
    def max_backend_latency(self):
        """Gets the max_backend_latency of this BackendLatencyStats.

        最大后端延时

        :return: The max_backend_latency of this BackendLatencyStats.
        :rtype: int
        """
        return self._max_backend_latency

    @max_backend_latency.setter
    def max_backend_latency(self, max_backend_latency):
        """Sets the max_backend_latency of this BackendLatencyStats.

        最大后端延时

        :param max_backend_latency: The max_backend_latency of this BackendLatencyStats.
        :type max_backend_latency: int
        """
        self._max_backend_latency = max_backend_latency

    @property
    def avg_backend_latency(self):
        """Gets the avg_backend_latency of this BackendLatencyStats.

        平均后端延时

        :return: The avg_backend_latency of this BackendLatencyStats.
        :rtype: float
        """
        return self._avg_backend_latency

    @avg_backend_latency.setter
    def avg_backend_latency(self, avg_backend_latency):
        """Sets the avg_backend_latency of this BackendLatencyStats.

        平均后端延时

        :param avg_backend_latency: The avg_backend_latency of this BackendLatencyStats.
        :type avg_backend_latency: float
        """
        self._avg_backend_latency = avg_backend_latency

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
        if not isinstance(other, BackendLatencyStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
