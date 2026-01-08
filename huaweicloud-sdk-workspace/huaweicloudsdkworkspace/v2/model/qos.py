# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Qos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iops': 'int',
        'throughput': 'int'
    }

    attribute_map = {
        'iops': 'iops',
        'throughput': 'throughput'
    }

    def __init__(self, iops=None, throughput=None):
        r"""Qos

        The model defined in huaweicloud sdk

        :param iops: iops，磁盘每秒进行读写的操作次数。
        :type iops: int
        :param throughput: 吞吐量，磁盘每秒成功传送的数据量，即读取和写入的数据量，单位是MiB/s。
        :type throughput: int
        """
        
        

        self._iops = None
        self._throughput = None
        self.discriminator = None

        self.iops = iops
        self.throughput = throughput

    @property
    def iops(self):
        r"""Gets the iops of this Qos.

        iops，磁盘每秒进行读写的操作次数。

        :return: The iops of this Qos.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        r"""Sets the iops of this Qos.

        iops，磁盘每秒进行读写的操作次数。

        :param iops: The iops of this Qos.
        :type iops: int
        """
        self._iops = iops

    @property
    def throughput(self):
        r"""Gets the throughput of this Qos.

        吞吐量，磁盘每秒成功传送的数据量，即读取和写入的数据量，单位是MiB/s。

        :return: The throughput of this Qos.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        r"""Sets the throughput of this Qos.

        吞吐量，磁盘每秒成功传送的数据量，即读取和写入的数据量，单位是MiB/s。

        :param throughput: The throughput of this Qos.
        :type throughput: int
        """
        self._throughput = throughput

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
        if not isinstance(other, Qos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
