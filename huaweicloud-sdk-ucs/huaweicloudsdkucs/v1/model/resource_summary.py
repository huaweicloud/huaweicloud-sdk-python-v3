# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allocatable': 'dict(str, object)',
        'allocating': 'dict(str, object)',
        'allocated': 'dict(str, object)',
        'capacity': 'dict(str, object)'
    }

    attribute_map = {
        'allocatable': 'allocatable',
        'allocating': 'allocating',
        'allocated': 'allocated',
        'capacity': 'capacity'
    }

    def __init__(self, allocatable=None, allocating=None, allocated=None, capacity=None):
        r"""ResourceSummary

        The model defined in huaweicloud sdk

        :param allocatable: 可分配的资源
        :type allocatable: dict(str, object)
        :param allocating: 分配中的资源
        :type allocating: dict(str, object)
        :param allocated: 已分配的资源
        :type allocated: dict(str, object)
        :param capacity: 资源总量
        :type capacity: dict(str, object)
        """
        
        

        self._allocatable = None
        self._allocating = None
        self._allocated = None
        self._capacity = None
        self.discriminator = None

        if allocatable is not None:
            self.allocatable = allocatable
        if allocating is not None:
            self.allocating = allocating
        if allocated is not None:
            self.allocated = allocated
        if capacity is not None:
            self.capacity = capacity

    @property
    def allocatable(self):
        r"""Gets the allocatable of this ResourceSummary.

        可分配的资源

        :return: The allocatable of this ResourceSummary.
        :rtype: dict(str, object)
        """
        return self._allocatable

    @allocatable.setter
    def allocatable(self, allocatable):
        r"""Sets the allocatable of this ResourceSummary.

        可分配的资源

        :param allocatable: The allocatable of this ResourceSummary.
        :type allocatable: dict(str, object)
        """
        self._allocatable = allocatable

    @property
    def allocating(self):
        r"""Gets the allocating of this ResourceSummary.

        分配中的资源

        :return: The allocating of this ResourceSummary.
        :rtype: dict(str, object)
        """
        return self._allocating

    @allocating.setter
    def allocating(self, allocating):
        r"""Sets the allocating of this ResourceSummary.

        分配中的资源

        :param allocating: The allocating of this ResourceSummary.
        :type allocating: dict(str, object)
        """
        self._allocating = allocating

    @property
    def allocated(self):
        r"""Gets the allocated of this ResourceSummary.

        已分配的资源

        :return: The allocated of this ResourceSummary.
        :rtype: dict(str, object)
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        r"""Sets the allocated of this ResourceSummary.

        已分配的资源

        :param allocated: The allocated of this ResourceSummary.
        :type allocated: dict(str, object)
        """
        self._allocated = allocated

    @property
    def capacity(self):
        r"""Gets the capacity of this ResourceSummary.

        资源总量

        :return: The capacity of this ResourceSummary.
        :rtype: dict(str, object)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this ResourceSummary.

        资源总量

        :param capacity: The capacity of this ResourceSummary.
        :type capacity: dict(str, object)
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
        if not isinstance(other, ResourceSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
