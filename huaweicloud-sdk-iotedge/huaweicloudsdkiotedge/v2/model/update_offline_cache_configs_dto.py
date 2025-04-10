# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOfflineCacheConfigsDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'capacity': 'int'
    }

    attribute_map = {
        'capacity': 'capacity'
    }

    def __init__(self, capacity=None):
        r"""UpdateOfflineCacheConfigsDTO

        The model defined in huaweicloud sdk

        :param capacity: 节点离线缓存容量，单位MB，默认2048，取值范围500-65536
        :type capacity: int
        """
        
        

        self._capacity = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity

    @property
    def capacity(self):
        r"""Gets the capacity of this UpdateOfflineCacheConfigsDTO.

        节点离线缓存容量，单位MB，默认2048，取值范围500-65536

        :return: The capacity of this UpdateOfflineCacheConfigsDTO.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this UpdateOfflineCacheConfigsDTO.

        节点离线缓存容量，单位MB，默认2048，取值范围500-65536

        :param capacity: The capacity of this UpdateOfflineCacheConfigsDTO.
        :type capacity: int
        """
        self._capacity = capacity

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
        if not isinstance(other, UpdateOfflineCacheConfigsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
