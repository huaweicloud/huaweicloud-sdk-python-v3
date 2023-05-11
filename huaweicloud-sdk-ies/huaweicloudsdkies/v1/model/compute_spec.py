# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputeSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_type': 'str',
        'count': 'int'
    }

    attribute_map = {
        'flavor_type': 'flavor_type',
        'count': 'count'
    }

    def __init__(self, flavor_type=None, count=None):
        """ComputeSpec

        The model defined in huaweicloud sdk

        :param flavor_type: 算力规格类型，如C6
        :type flavor_type: str
        :param count: 计算单元设备数
        :type count: int
        """
        
        

        self._flavor_type = None
        self._count = None
        self.discriminator = None

        self.flavor_type = flavor_type
        self.count = count

    @property
    def flavor_type(self):
        """Gets the flavor_type of this ComputeSpec.

        算力规格类型，如C6

        :return: The flavor_type of this ComputeSpec.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        """Sets the flavor_type of this ComputeSpec.

        算力规格类型，如C6

        :param flavor_type: The flavor_type of this ComputeSpec.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def count(self):
        """Gets the count of this ComputeSpec.

        计算单元设备数

        :return: The count of this ComputeSpec.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ComputeSpec.

        计算单元设备数

        :param count: The count of this ComputeSpec.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ComputeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
