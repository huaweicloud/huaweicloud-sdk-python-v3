# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricTableItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allocated': 'Allocated',
        'capacity': 'Capacity'
    }

    attribute_map = {
        'allocated': 'allocated',
        'capacity': 'capacity'
    }

    def __init__(self, allocated=None, capacity=None):
        r"""MetricTableItem

        The model defined in huaweicloud sdk

        :param allocated: 
        :type allocated: :class:`huaweicloudsdkmodelarts.v1.Allocated`
        :param capacity: 
        :type capacity: :class:`huaweicloudsdkmodelarts.v1.Capacity`
        """
        
        

        self._allocated = None
        self._capacity = None
        self.discriminator = None

        if allocated is not None:
            self.allocated = allocated
        if capacity is not None:
            self.capacity = capacity

    @property
    def allocated(self):
        r"""Gets the allocated of this MetricTableItem.

        :return: The allocated of this MetricTableItem.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Allocated`
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        r"""Sets the allocated of this MetricTableItem.

        :param allocated: The allocated of this MetricTableItem.
        :type allocated: :class:`huaweicloudsdkmodelarts.v1.Allocated`
        """
        self._allocated = allocated

    @property
    def capacity(self):
        r"""Gets the capacity of this MetricTableItem.

        :return: The capacity of this MetricTableItem.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Capacity`
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this MetricTableItem.

        :param capacity: The capacity of this MetricTableItem.
        :type capacity: :class:`huaweicloudsdkmodelarts.v1.Capacity`
        """
        self._capacity = capacity

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
        if not isinstance(other, MetricTableItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
