# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Iops:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'min': 'int',
        'max': 'int',
        'range_by_size': 'float'
    }

    attribute_map = {
        'resource_spec_code': 'resource_spec_code',
        'min': 'min',
        'max': 'max',
        'range_by_size': 'range_by_size'
    }

    def __init__(self, resource_spec_code=None, min=None, max=None, range_by_size=None):
        r"""Iops

        The model defined in huaweicloud sdk

        :param resource_spec_code: 产品ID。
        :type resource_spec_code: str
        :param min: 最小值。
        :type min: int
        :param max: 最大值。
        :type max: int
        :param range_by_size: 可取值范围，&lt;&#x3D;rangeBySize乘size。
        :type range_by_size: float
        """
        
        

        self._resource_spec_code = None
        self._min = None
        self._max = None
        self._range_by_size = None
        self.discriminator = None

        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if range_by_size is not None:
            self.range_by_size = range_by_size

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this Iops.

        产品ID。

        :return: The resource_spec_code of this Iops.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this Iops.

        产品ID。

        :param resource_spec_code: The resource_spec_code of this Iops.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def min(self):
        r"""Gets the min of this Iops.

        最小值。

        :return: The min of this Iops.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this Iops.

        最小值。

        :param min: The min of this Iops.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this Iops.

        最大值。

        :return: The max of this Iops.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this Iops.

        最大值。

        :param max: The max of this Iops.
        :type max: int
        """
        self._max = max

    @property
    def range_by_size(self):
        r"""Gets the range_by_size of this Iops.

        可取值范围，<=rangeBySize乘size。

        :return: The range_by_size of this Iops.
        :rtype: float
        """
        return self._range_by_size

    @range_by_size.setter
    def range_by_size(self, range_by_size):
        r"""Sets the range_by_size of this Iops.

        可取值范围，<=rangeBySize乘size。

        :param range_by_size: The range_by_size of this Iops.
        :type range_by_size: float
        """
        self._range_by_size = range_by_size

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
        if not isinstance(other, Iops):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
