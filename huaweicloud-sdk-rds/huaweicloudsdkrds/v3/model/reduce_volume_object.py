# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReduceVolumeObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'is_delay': 'bool',
        'iops': 'int',
        'throughput': 'int'
    }

    attribute_map = {
        'size': 'size',
        'is_delay': 'is_delay',
        'iops': 'iops',
        'throughput': 'throughput'
    }

    def __init__(self, size=None, is_delay=None, iops=None, throughput=None):
        r"""ReduceVolumeObject

        The model defined in huaweicloud sdk

        :param size: 缩容后实例磁盘的目标大小。每次缩容至少缩小10GB；目标大小必须为10的整数倍。 为确保实例的正常使用，根据当前磁盘的使用量情况存在磁盘容量下限，当此参数小于磁盘容量下限时，缩容会下发失败，此时请适当调大此参数。
        :type size: int
        :param is_delay: 是否定时变更。 - true，为定时在运维时间窗做变更。 - false，为立即变更，默认该方式。
        :type is_delay: bool
        :param iops: 该参数只有磁盘类型为Flexible SSD（GPSSD2）和极速型SSDV2（ESSD2）的磁盘必填。 对于Flexible SSD类型的磁盘，IOPS值配置的范围为3000~128000，具体可配置值受磁盘大小限制，需要小于等于500*磁盘容量。 对于极速型SSDV2类型的磁盘，IOPS值配置的范围为100~256000，具体可配置值受磁盘大小限制，需要小于等于1000*磁盘容量。
        :type iops: int
        :param throughput: 该参数只有磁盘类型为Flexible SSD（GPSSD2）的磁盘必填。 对于Flexible SSD类型的磁盘，throughput值配置的范围为125~1000 MiB/s，具体可配置值受IOPS大小限制，需要小于等于IOPS/4。
        :type throughput: int
        """
        
        

        self._size = None
        self._is_delay = None
        self._iops = None
        self._throughput = None
        self.discriminator = None

        self.size = size
        self.is_delay = is_delay
        if iops is not None:
            self.iops = iops
        if throughput is not None:
            self.throughput = throughput

    @property
    def size(self):
        r"""Gets the size of this ReduceVolumeObject.

        缩容后实例磁盘的目标大小。每次缩容至少缩小10GB；目标大小必须为10的整数倍。 为确保实例的正常使用，根据当前磁盘的使用量情况存在磁盘容量下限，当此参数小于磁盘容量下限时，缩容会下发失败，此时请适当调大此参数。

        :return: The size of this ReduceVolumeObject.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ReduceVolumeObject.

        缩容后实例磁盘的目标大小。每次缩容至少缩小10GB；目标大小必须为10的整数倍。 为确保实例的正常使用，根据当前磁盘的使用量情况存在磁盘容量下限，当此参数小于磁盘容量下限时，缩容会下发失败，此时请适当调大此参数。

        :param size: The size of this ReduceVolumeObject.
        :type size: int
        """
        self._size = size

    @property
    def is_delay(self):
        r"""Gets the is_delay of this ReduceVolumeObject.

        是否定时变更。 - true，为定时在运维时间窗做变更。 - false，为立即变更，默认该方式。

        :return: The is_delay of this ReduceVolumeObject.
        :rtype: bool
        """
        return self._is_delay

    @is_delay.setter
    def is_delay(self, is_delay):
        r"""Sets the is_delay of this ReduceVolumeObject.

        是否定时变更。 - true，为定时在运维时间窗做变更。 - false，为立即变更，默认该方式。

        :param is_delay: The is_delay of this ReduceVolumeObject.
        :type is_delay: bool
        """
        self._is_delay = is_delay

    @property
    def iops(self):
        r"""Gets the iops of this ReduceVolumeObject.

        该参数只有磁盘类型为Flexible SSD（GPSSD2）和极速型SSDV2（ESSD2）的磁盘必填。 对于Flexible SSD类型的磁盘，IOPS值配置的范围为3000~128000，具体可配置值受磁盘大小限制，需要小于等于500*磁盘容量。 对于极速型SSDV2类型的磁盘，IOPS值配置的范围为100~256000，具体可配置值受磁盘大小限制，需要小于等于1000*磁盘容量。

        :return: The iops of this ReduceVolumeObject.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        r"""Sets the iops of this ReduceVolumeObject.

        该参数只有磁盘类型为Flexible SSD（GPSSD2）和极速型SSDV2（ESSD2）的磁盘必填。 对于Flexible SSD类型的磁盘，IOPS值配置的范围为3000~128000，具体可配置值受磁盘大小限制，需要小于等于500*磁盘容量。 对于极速型SSDV2类型的磁盘，IOPS值配置的范围为100~256000，具体可配置值受磁盘大小限制，需要小于等于1000*磁盘容量。

        :param iops: The iops of this ReduceVolumeObject.
        :type iops: int
        """
        self._iops = iops

    @property
    def throughput(self):
        r"""Gets the throughput of this ReduceVolumeObject.

        该参数只有磁盘类型为Flexible SSD（GPSSD2）的磁盘必填。 对于Flexible SSD类型的磁盘，throughput值配置的范围为125~1000 MiB/s，具体可配置值受IOPS大小限制，需要小于等于IOPS/4。

        :return: The throughput of this ReduceVolumeObject.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        r"""Sets the throughput of this ReduceVolumeObject.

        该参数只有磁盘类型为Flexible SSD（GPSSD2）的磁盘必填。 对于Flexible SSD类型的磁盘，throughput值配置的范围为125~1000 MiB/s，具体可配置值受IOPS大小限制，需要小于等于IOPS/4。

        :param throughput: The throughput of this ReduceVolumeObject.
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
        if not isinstance(other, ReduceVolumeObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
