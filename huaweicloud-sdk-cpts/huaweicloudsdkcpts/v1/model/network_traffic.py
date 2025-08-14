# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkTraffic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'avg_network_traffic': 'float',
        'max_down_stream': 'int',
        'max_network_traffic': 'int',
        'max_upstream': 'int',
        'min_network_traffic': 'float'
    }

    attribute_map = {
        'avg_network_traffic': 'avg_network_traffic',
        'max_down_stream': 'max_down_stream',
        'max_network_traffic': 'max_network_traffic',
        'max_upstream': 'max_upstream',
        'min_network_traffic': 'min_network_traffic'
    }

    def __init__(self, avg_network_traffic=None, max_down_stream=None, max_network_traffic=None, max_upstream=None, min_network_traffic=None):
        r"""NetworkTraffic

        The model defined in huaweicloud sdk

        :param avg_network_traffic: 平均网络流量
        :type avg_network_traffic: float
        :param max_down_stream: 最大下行带宽
        :type max_down_stream: int
        :param max_network_traffic: 最大网络流量（流量峰值）
        :type max_network_traffic: int
        :param max_upstream: 最大上行带宽
        :type max_upstream: int
        :param min_network_traffic: 最小网络流量
        :type min_network_traffic: float
        """
        
        

        self._avg_network_traffic = None
        self._max_down_stream = None
        self._max_network_traffic = None
        self._max_upstream = None
        self._min_network_traffic = None
        self.discriminator = None

        if avg_network_traffic is not None:
            self.avg_network_traffic = avg_network_traffic
        if max_down_stream is not None:
            self.max_down_stream = max_down_stream
        if max_network_traffic is not None:
            self.max_network_traffic = max_network_traffic
        if max_upstream is not None:
            self.max_upstream = max_upstream
        if min_network_traffic is not None:
            self.min_network_traffic = min_network_traffic

    @property
    def avg_network_traffic(self):
        r"""Gets the avg_network_traffic of this NetworkTraffic.

        平均网络流量

        :return: The avg_network_traffic of this NetworkTraffic.
        :rtype: float
        """
        return self._avg_network_traffic

    @avg_network_traffic.setter
    def avg_network_traffic(self, avg_network_traffic):
        r"""Sets the avg_network_traffic of this NetworkTraffic.

        平均网络流量

        :param avg_network_traffic: The avg_network_traffic of this NetworkTraffic.
        :type avg_network_traffic: float
        """
        self._avg_network_traffic = avg_network_traffic

    @property
    def max_down_stream(self):
        r"""Gets the max_down_stream of this NetworkTraffic.

        最大下行带宽

        :return: The max_down_stream of this NetworkTraffic.
        :rtype: int
        """
        return self._max_down_stream

    @max_down_stream.setter
    def max_down_stream(self, max_down_stream):
        r"""Sets the max_down_stream of this NetworkTraffic.

        最大下行带宽

        :param max_down_stream: The max_down_stream of this NetworkTraffic.
        :type max_down_stream: int
        """
        self._max_down_stream = max_down_stream

    @property
    def max_network_traffic(self):
        r"""Gets the max_network_traffic of this NetworkTraffic.

        最大网络流量（流量峰值）

        :return: The max_network_traffic of this NetworkTraffic.
        :rtype: int
        """
        return self._max_network_traffic

    @max_network_traffic.setter
    def max_network_traffic(self, max_network_traffic):
        r"""Sets the max_network_traffic of this NetworkTraffic.

        最大网络流量（流量峰值）

        :param max_network_traffic: The max_network_traffic of this NetworkTraffic.
        :type max_network_traffic: int
        """
        self._max_network_traffic = max_network_traffic

    @property
    def max_upstream(self):
        r"""Gets the max_upstream of this NetworkTraffic.

        最大上行带宽

        :return: The max_upstream of this NetworkTraffic.
        :rtype: int
        """
        return self._max_upstream

    @max_upstream.setter
    def max_upstream(self, max_upstream):
        r"""Sets the max_upstream of this NetworkTraffic.

        最大上行带宽

        :param max_upstream: The max_upstream of this NetworkTraffic.
        :type max_upstream: int
        """
        self._max_upstream = max_upstream

    @property
    def min_network_traffic(self):
        r"""Gets the min_network_traffic of this NetworkTraffic.

        最小网络流量

        :return: The min_network_traffic of this NetworkTraffic.
        :rtype: float
        """
        return self._min_network_traffic

    @min_network_traffic.setter
    def min_network_traffic(self, min_network_traffic):
        r"""Sets the min_network_traffic of this NetworkTraffic.

        最小网络流量

        :param min_network_traffic: The min_network_traffic of this NetworkTraffic.
        :type min_network_traffic: float
        """
        self._min_network_traffic = min_network_traffic

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
        if not isinstance(other, NetworkTraffic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
