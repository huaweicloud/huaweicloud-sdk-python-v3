# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerBpsDict:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'traffic_pos_id': 'int',
        'traffic_per_second': 'int',
        'packet_per_second': 'int'
    }

    attribute_map = {
        'traffic_pos_id': 'traffic_pos_id',
        'traffic_per_second': 'traffic_per_second',
        'packet_per_second': 'packet_per_second'
    }

    def __init__(self, traffic_pos_id=None, traffic_per_second=None, packet_per_second=None):
        """TriggerBpsDict

        The model defined in huaweicloud sdk

        :param traffic_pos_id: 流量分段ID
        :type traffic_pos_id: int
        :param traffic_per_second: 每秒流量（Mbit/s）阈值
        :type traffic_per_second: int
        :param packet_per_second: 每秒报文数（个/s）阈值
        :type packet_per_second: int
        """
        
        

        self._traffic_pos_id = None
        self._traffic_per_second = None
        self._packet_per_second = None
        self.discriminator = None

        self.traffic_pos_id = traffic_pos_id
        self.traffic_per_second = traffic_per_second
        self.packet_per_second = packet_per_second

    @property
    def traffic_pos_id(self):
        """Gets the traffic_pos_id of this TriggerBpsDict.

        流量分段ID

        :return: The traffic_pos_id of this TriggerBpsDict.
        :rtype: int
        """
        return self._traffic_pos_id

    @traffic_pos_id.setter
    def traffic_pos_id(self, traffic_pos_id):
        """Sets the traffic_pos_id of this TriggerBpsDict.

        流量分段ID

        :param traffic_pos_id: The traffic_pos_id of this TriggerBpsDict.
        :type traffic_pos_id: int
        """
        self._traffic_pos_id = traffic_pos_id

    @property
    def traffic_per_second(self):
        """Gets the traffic_per_second of this TriggerBpsDict.

        每秒流量（Mbit/s）阈值

        :return: The traffic_per_second of this TriggerBpsDict.
        :rtype: int
        """
        return self._traffic_per_second

    @traffic_per_second.setter
    def traffic_per_second(self, traffic_per_second):
        """Sets the traffic_per_second of this TriggerBpsDict.

        每秒流量（Mbit/s）阈值

        :param traffic_per_second: The traffic_per_second of this TriggerBpsDict.
        :type traffic_per_second: int
        """
        self._traffic_per_second = traffic_per_second

    @property
    def packet_per_second(self):
        """Gets the packet_per_second of this TriggerBpsDict.

        每秒报文数（个/s）阈值

        :return: The packet_per_second of this TriggerBpsDict.
        :rtype: int
        """
        return self._packet_per_second

    @packet_per_second.setter
    def packet_per_second(self, packet_per_second):
        """Sets the packet_per_second of this TriggerBpsDict.

        每秒报文数（个/s）阈值

        :param packet_per_second: The packet_per_second of this TriggerBpsDict.
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
        if not isinstance(other, TriggerBpsDict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
