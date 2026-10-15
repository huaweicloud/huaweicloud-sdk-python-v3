# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrendPoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timestamp': 'int',
        'size': 'int',
        'qps': 'int',
        'traffic_in': 'int',
        'traffic_out': 'int'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'size': 'size',
        'qps': 'qps',
        'traffic_in': 'traffic_in',
        'traffic_out': 'traffic_out'
    }

    def __init__(self, timestamp=None, size=None, qps=None, traffic_in=None, traffic_out=None):
        r"""TrendPoint

        The model defined in huaweicloud sdk

        :param timestamp: 时间点（毫秒时间戳）
        :type timestamp: int
        :param size: key大小（size/storage维度返回）
        :type size: int
        :param qps: QPS值（qps维度返回）
        :type qps: int
        :param traffic_in: 入口流量（traffic维度返回，字节/秒）
        :type traffic_in: int
        :param traffic_out: 出口流量（traffic维度返回，字节/秒）
        :type traffic_out: int
        """
        
        

        self._timestamp = None
        self._size = None
        self._qps = None
        self._traffic_in = None
        self._traffic_out = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if size is not None:
            self.size = size
        if qps is not None:
            self.qps = qps
        if traffic_in is not None:
            self.traffic_in = traffic_in
        if traffic_out is not None:
            self.traffic_out = traffic_out

    @property
    def timestamp(self):
        r"""Gets the timestamp of this TrendPoint.

        时间点（毫秒时间戳）

        :return: The timestamp of this TrendPoint.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this TrendPoint.

        时间点（毫秒时间戳）

        :param timestamp: The timestamp of this TrendPoint.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def size(self):
        r"""Gets the size of this TrendPoint.

        key大小（size/storage维度返回）

        :return: The size of this TrendPoint.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this TrendPoint.

        key大小（size/storage维度返回）

        :param size: The size of this TrendPoint.
        :type size: int
        """
        self._size = size

    @property
    def qps(self):
        r"""Gets the qps of this TrendPoint.

        QPS值（qps维度返回）

        :return: The qps of this TrendPoint.
        :rtype: int
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        r"""Sets the qps of this TrendPoint.

        QPS值（qps维度返回）

        :param qps: The qps of this TrendPoint.
        :type qps: int
        """
        self._qps = qps

    @property
    def traffic_in(self):
        r"""Gets the traffic_in of this TrendPoint.

        入口流量（traffic维度返回，字节/秒）

        :return: The traffic_in of this TrendPoint.
        :rtype: int
        """
        return self._traffic_in

    @traffic_in.setter
    def traffic_in(self, traffic_in):
        r"""Sets the traffic_in of this TrendPoint.

        入口流量（traffic维度返回，字节/秒）

        :param traffic_in: The traffic_in of this TrendPoint.
        :type traffic_in: int
        """
        self._traffic_in = traffic_in

    @property
    def traffic_out(self):
        r"""Gets the traffic_out of this TrendPoint.

        出口流量（traffic维度返回，字节/秒）

        :return: The traffic_out of this TrendPoint.
        :rtype: int
        """
        return self._traffic_out

    @traffic_out.setter
    def traffic_out(self, traffic_out):
        r"""Sets the traffic_out of this TrendPoint.

        出口流量（traffic维度返回，字节/秒）

        :param traffic_out: The traffic_out of this TrendPoint.
        :type traffic_out: int
        """
        self._traffic_out = traffic_out

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TrendPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
