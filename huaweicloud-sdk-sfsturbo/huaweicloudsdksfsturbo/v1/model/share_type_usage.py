# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareTypeUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'capacity': 'ShareTypeUsageCapacity',
        'bandwidth': 'ShareTypeUsageBandwidth',
        'quantity': 'ShareTypeUsageQuantity'
    }

    attribute_map = {
        'capacity': 'capacity',
        'bandwidth': 'bandwidth',
        'quantity': 'quantity'
    }

    def __init__(self, capacity=None, bandwidth=None, quantity=None):
        r"""ShareTypeUsage

        The model defined in huaweicloud sdk

        :param capacity: 
        :type capacity: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsageCapacity`
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsageBandwidth`
        :param quantity: 
        :type quantity: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsageQuantity`
        """
        
        

        self._capacity = None
        self._bandwidth = None
        self._quantity = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if quantity is not None:
            self.quantity = quantity

    @property
    def capacity(self):
        r"""Gets the capacity of this ShareTypeUsage.

        :return: The capacity of this ShareTypeUsage.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsageCapacity`
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this ShareTypeUsage.

        :param capacity: The capacity of this ShareTypeUsage.
        :type capacity: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsageCapacity`
        """
        self._capacity = capacity

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this ShareTypeUsage.

        :return: The bandwidth of this ShareTypeUsage.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsageBandwidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this ShareTypeUsage.

        :param bandwidth: The bandwidth of this ShareTypeUsage.
        :type bandwidth: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsageBandwidth`
        """
        self._bandwidth = bandwidth

    @property
    def quantity(self):
        r"""Gets the quantity of this ShareTypeUsage.

        :return: The quantity of this ShareTypeUsage.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsageQuantity`
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        r"""Sets the quantity of this ShareTypeUsage.

        :param quantity: The quantity of this ShareTypeUsage.
        :type quantity: :class:`huaweicloudsdksfsturbo.v1.ShareTypeUsageQuantity`
        """
        self._quantity = quantity

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
        if not isinstance(other, ShareTypeUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
