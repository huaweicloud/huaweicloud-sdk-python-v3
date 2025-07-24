# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareTypesAttribution:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'capacity': 'ShareTypesAttributionCapacity',
        'bandwidth': 'ShareTypesAttributionBandwidth',
        'iops': 'ShareTypesAttributionIops',
        'single_channel_4k_latency': 'ShareTypesAttributionSingleChannel4KLatency'
    }

    attribute_map = {
        'capacity': 'capacity',
        'bandwidth': 'bandwidth',
        'iops': 'iops',
        'single_channel_4k_latency': 'single_channel_4k_latency'
    }

    def __init__(self, capacity=None, bandwidth=None, iops=None, single_channel_4k_latency=None):
        r"""ShareTypesAttribution

        The model defined in huaweicloud sdk

        :param capacity: 
        :type capacity: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionCapacity`
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionBandwidth`
        :param iops: 
        :type iops: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionIops`
        :param single_channel_4k_latency: 
        :type single_channel_4k_latency: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionSingleChannel4KLatency`
        """
        
        

        self._capacity = None
        self._bandwidth = None
        self._iops = None
        self._single_channel_4k_latency = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if iops is not None:
            self.iops = iops
        if single_channel_4k_latency is not None:
            self.single_channel_4k_latency = single_channel_4k_latency

    @property
    def capacity(self):
        r"""Gets the capacity of this ShareTypesAttribution.

        :return: The capacity of this ShareTypesAttribution.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionCapacity`
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this ShareTypesAttribution.

        :param capacity: The capacity of this ShareTypesAttribution.
        :type capacity: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionCapacity`
        """
        self._capacity = capacity

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this ShareTypesAttribution.

        :return: The bandwidth of this ShareTypesAttribution.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionBandwidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this ShareTypesAttribution.

        :param bandwidth: The bandwidth of this ShareTypesAttribution.
        :type bandwidth: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionBandwidth`
        """
        self._bandwidth = bandwidth

    @property
    def iops(self):
        r"""Gets the iops of this ShareTypesAttribution.

        :return: The iops of this ShareTypesAttribution.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionIops`
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        r"""Sets the iops of this ShareTypesAttribution.

        :param iops: The iops of this ShareTypesAttribution.
        :type iops: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionIops`
        """
        self._iops = iops

    @property
    def single_channel_4k_latency(self):
        r"""Gets the single_channel_4k_latency of this ShareTypesAttribution.

        :return: The single_channel_4k_latency of this ShareTypesAttribution.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionSingleChannel4KLatency`
        """
        return self._single_channel_4k_latency

    @single_channel_4k_latency.setter
    def single_channel_4k_latency(self, single_channel_4k_latency):
        r"""Sets the single_channel_4k_latency of this ShareTypesAttribution.

        :param single_channel_4k_latency: The single_channel_4k_latency of this ShareTypesAttribution.
        :type single_channel_4k_latency: :class:`huaweicloudsdksfsturbo.v1.ShareTypesAttributionSingleChannel4KLatency`
        """
        self._single_channel_4k_latency = single_channel_4k_latency

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
        if not isinstance(other, ShareTypesAttribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
