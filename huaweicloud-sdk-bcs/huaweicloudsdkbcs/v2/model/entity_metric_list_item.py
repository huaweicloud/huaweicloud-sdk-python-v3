# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EntityMetricListItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cpu_usage': 'str',
        'disk_read_rate': 'str',
        'disk_write_rate': 'str',
        'mem_usage': 'str',
        'recv_bytes_rate': 'str',
        'send_bytes_rate': 'str'
    }

    attribute_map = {
        'cpu_usage': 'cpuUsage',
        'disk_read_rate': 'diskReadRate',
        'disk_write_rate': 'diskWriteRate',
        'mem_usage': 'memUsage',
        'recv_bytes_rate': 'recvBytesRate',
        'send_bytes_rate': 'sendBytesRate'
    }

    def __init__(self, cpu_usage=None, disk_read_rate=None, disk_write_rate=None, mem_usage=None, recv_bytes_rate=None, send_bytes_rate=None):
        """EntityMetricListItem

        The model defined in huaweicloud sdk

        :param cpu_usage: cpu使用率
        :type cpu_usage: str
        :param disk_read_rate: 磁盘使用率
        :type disk_read_rate: str
        :param disk_write_rate: 磁盘写入速率
        :type disk_write_rate: str
        :param mem_usage: 物理内存使用率
        :type mem_usage: str
        :param recv_bytes_rate: 下行BPs
        :type recv_bytes_rate: str
        :param send_bytes_rate: 上行BPs
        :type send_bytes_rate: str
        """
        
        

        self._cpu_usage = None
        self._disk_read_rate = None
        self._disk_write_rate = None
        self._mem_usage = None
        self._recv_bytes_rate = None
        self._send_bytes_rate = None
        self.discriminator = None

        if cpu_usage is not None:
            self.cpu_usage = cpu_usage
        if disk_read_rate is not None:
            self.disk_read_rate = disk_read_rate
        if disk_write_rate is not None:
            self.disk_write_rate = disk_write_rate
        if mem_usage is not None:
            self.mem_usage = mem_usage
        if recv_bytes_rate is not None:
            self.recv_bytes_rate = recv_bytes_rate
        if send_bytes_rate is not None:
            self.send_bytes_rate = send_bytes_rate

    @property
    def cpu_usage(self):
        """Gets the cpu_usage of this EntityMetricListItem.

        cpu使用率

        :return: The cpu_usage of this EntityMetricListItem.
        :rtype: str
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        """Sets the cpu_usage of this EntityMetricListItem.

        cpu使用率

        :param cpu_usage: The cpu_usage of this EntityMetricListItem.
        :type cpu_usage: str
        """
        self._cpu_usage = cpu_usage

    @property
    def disk_read_rate(self):
        """Gets the disk_read_rate of this EntityMetricListItem.

        磁盘使用率

        :return: The disk_read_rate of this EntityMetricListItem.
        :rtype: str
        """
        return self._disk_read_rate

    @disk_read_rate.setter
    def disk_read_rate(self, disk_read_rate):
        """Sets the disk_read_rate of this EntityMetricListItem.

        磁盘使用率

        :param disk_read_rate: The disk_read_rate of this EntityMetricListItem.
        :type disk_read_rate: str
        """
        self._disk_read_rate = disk_read_rate

    @property
    def disk_write_rate(self):
        """Gets the disk_write_rate of this EntityMetricListItem.

        磁盘写入速率

        :return: The disk_write_rate of this EntityMetricListItem.
        :rtype: str
        """
        return self._disk_write_rate

    @disk_write_rate.setter
    def disk_write_rate(self, disk_write_rate):
        """Sets the disk_write_rate of this EntityMetricListItem.

        磁盘写入速率

        :param disk_write_rate: The disk_write_rate of this EntityMetricListItem.
        :type disk_write_rate: str
        """
        self._disk_write_rate = disk_write_rate

    @property
    def mem_usage(self):
        """Gets the mem_usage of this EntityMetricListItem.

        物理内存使用率

        :return: The mem_usage of this EntityMetricListItem.
        :rtype: str
        """
        return self._mem_usage

    @mem_usage.setter
    def mem_usage(self, mem_usage):
        """Sets the mem_usage of this EntityMetricListItem.

        物理内存使用率

        :param mem_usage: The mem_usage of this EntityMetricListItem.
        :type mem_usage: str
        """
        self._mem_usage = mem_usage

    @property
    def recv_bytes_rate(self):
        """Gets the recv_bytes_rate of this EntityMetricListItem.

        下行BPs

        :return: The recv_bytes_rate of this EntityMetricListItem.
        :rtype: str
        """
        return self._recv_bytes_rate

    @recv_bytes_rate.setter
    def recv_bytes_rate(self, recv_bytes_rate):
        """Sets the recv_bytes_rate of this EntityMetricListItem.

        下行BPs

        :param recv_bytes_rate: The recv_bytes_rate of this EntityMetricListItem.
        :type recv_bytes_rate: str
        """
        self._recv_bytes_rate = recv_bytes_rate

    @property
    def send_bytes_rate(self):
        """Gets the send_bytes_rate of this EntityMetricListItem.

        上行BPs

        :return: The send_bytes_rate of this EntityMetricListItem.
        :rtype: str
        """
        return self._send_bytes_rate

    @send_bytes_rate.setter
    def send_bytes_rate(self, send_bytes_rate):
        """Sets the send_bytes_rate of this EntityMetricListItem.

        上行BPs

        :param send_bytes_rate: The send_bytes_rate of this EntityMetricListItem.
        :type send_bytes_rate: str
        """
        self._send_bytes_rate = send_bytes_rate

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
        if not isinstance(other, EntityMetricListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
