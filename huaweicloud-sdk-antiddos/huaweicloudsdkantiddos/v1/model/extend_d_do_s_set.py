# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtendDDoSSet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'int',
        'new_connection_limited': 'int',
        'total_connection_limited': 'int',
        'http_packet_per_second': 'int',
        'traffic_per_second': 'int',
        'packet_per_second': 'int'
    }

    attribute_map = {
        'set_id': 'SetID',
        'new_connection_limited': 'new_connection_limited',
        'total_connection_limited': 'total_connection_limited',
        'http_packet_per_second': 'http_packet_per_second',
        'traffic_per_second': 'traffic_per_second',
        'packet_per_second': 'packet_per_second'
    }

    def __init__(self, set_id=None, new_connection_limited=None, total_connection_limited=None, http_packet_per_second=None, traffic_per_second=None, packet_per_second=None):
        """ExtendDDoSSet

        The model defined in huaweicloud sdk

        :param set_id: 配置分段ID
        :type set_id: int
        :param new_connection_limited: 单一源IP新建连接个数
        :type new_connection_limited: int
        :param total_connection_limited: 单一源IP连接数总个数
        :type total_connection_limited: int
        :param http_packet_per_second: 每秒HTTP请求数（个/s）阈值
        :type http_packet_per_second: int
        :param traffic_per_second: 每秒流量（Mbit/s）阈值
        :type traffic_per_second: int
        :param packet_per_second: 每秒报文数（个/s）阈值
        :type packet_per_second: int
        """
        
        

        self._set_id = None
        self._new_connection_limited = None
        self._total_connection_limited = None
        self._http_packet_per_second = None
        self._traffic_per_second = None
        self._packet_per_second = None
        self.discriminator = None

        self.set_id = set_id
        self.new_connection_limited = new_connection_limited
        self.total_connection_limited = total_connection_limited
        self.http_packet_per_second = http_packet_per_second
        self.traffic_per_second = traffic_per_second
        self.packet_per_second = packet_per_second

    @property
    def set_id(self):
        """Gets the set_id of this ExtendDDoSSet.

        配置分段ID

        :return: The set_id of this ExtendDDoSSet.
        :rtype: int
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this ExtendDDoSSet.

        配置分段ID

        :param set_id: The set_id of this ExtendDDoSSet.
        :type set_id: int
        """
        self._set_id = set_id

    @property
    def new_connection_limited(self):
        """Gets the new_connection_limited of this ExtendDDoSSet.

        单一源IP新建连接个数

        :return: The new_connection_limited of this ExtendDDoSSet.
        :rtype: int
        """
        return self._new_connection_limited

    @new_connection_limited.setter
    def new_connection_limited(self, new_connection_limited):
        """Sets the new_connection_limited of this ExtendDDoSSet.

        单一源IP新建连接个数

        :param new_connection_limited: The new_connection_limited of this ExtendDDoSSet.
        :type new_connection_limited: int
        """
        self._new_connection_limited = new_connection_limited

    @property
    def total_connection_limited(self):
        """Gets the total_connection_limited of this ExtendDDoSSet.

        单一源IP连接数总个数

        :return: The total_connection_limited of this ExtendDDoSSet.
        :rtype: int
        """
        return self._total_connection_limited

    @total_connection_limited.setter
    def total_connection_limited(self, total_connection_limited):
        """Sets the total_connection_limited of this ExtendDDoSSet.

        单一源IP连接数总个数

        :param total_connection_limited: The total_connection_limited of this ExtendDDoSSet.
        :type total_connection_limited: int
        """
        self._total_connection_limited = total_connection_limited

    @property
    def http_packet_per_second(self):
        """Gets the http_packet_per_second of this ExtendDDoSSet.

        每秒HTTP请求数（个/s）阈值

        :return: The http_packet_per_second of this ExtendDDoSSet.
        :rtype: int
        """
        return self._http_packet_per_second

    @http_packet_per_second.setter
    def http_packet_per_second(self, http_packet_per_second):
        """Sets the http_packet_per_second of this ExtendDDoSSet.

        每秒HTTP请求数（个/s）阈值

        :param http_packet_per_second: The http_packet_per_second of this ExtendDDoSSet.
        :type http_packet_per_second: int
        """
        self._http_packet_per_second = http_packet_per_second

    @property
    def traffic_per_second(self):
        """Gets the traffic_per_second of this ExtendDDoSSet.

        每秒流量（Mbit/s）阈值

        :return: The traffic_per_second of this ExtendDDoSSet.
        :rtype: int
        """
        return self._traffic_per_second

    @traffic_per_second.setter
    def traffic_per_second(self, traffic_per_second):
        """Sets the traffic_per_second of this ExtendDDoSSet.

        每秒流量（Mbit/s）阈值

        :param traffic_per_second: The traffic_per_second of this ExtendDDoSSet.
        :type traffic_per_second: int
        """
        self._traffic_per_second = traffic_per_second

    @property
    def packet_per_second(self):
        """Gets the packet_per_second of this ExtendDDoSSet.

        每秒报文数（个/s）阈值

        :return: The packet_per_second of this ExtendDDoSSet.
        :rtype: int
        """
        return self._packet_per_second

    @packet_per_second.setter
    def packet_per_second(self, packet_per_second):
        """Sets the packet_per_second of this ExtendDDoSSet.

        每秒报文数（个/s）阈值

        :param packet_per_second: The packet_per_second of this ExtendDDoSSet.
        :type packet_per_second: int
        """
        self._packet_per_second = packet_per_second

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
        if not isinstance(other, ExtendDDoSSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
