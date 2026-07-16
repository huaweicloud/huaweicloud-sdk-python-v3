# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Gpu:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unit_num': 'int',
        'product_name': 'str',
        'memory': 'str'
    }

    attribute_map = {
        'unit_num': 'unit_num',
        'product_name': 'product_name',
        'memory': 'memory'
    }

    def __init__(self, unit_num=None, product_name=None, memory=None):
        r"""Gpu

        The model defined in huaweicloud sdk

        :param unit_num: gpu卡数。
        :type unit_num: int
        :param product_name: 产品名。
        :type product_name: str
        :param memory: 内存。
        :type memory: str
        """
        
        

        self._unit_num = None
        self._product_name = None
        self._memory = None
        self.discriminator = None

        if unit_num is not None:
            self.unit_num = unit_num
        if product_name is not None:
            self.product_name = product_name
        if memory is not None:
            self.memory = memory

    @property
    def unit_num(self):
        r"""Gets the unit_num of this Gpu.

        gpu卡数。

        :return: The unit_num of this Gpu.
        :rtype: int
        """
        return self._unit_num

    @unit_num.setter
    def unit_num(self, unit_num):
        r"""Sets the unit_num of this Gpu.

        gpu卡数。

        :param unit_num: The unit_num of this Gpu.
        :type unit_num: int
        """
        self._unit_num = unit_num

    @property
    def product_name(self):
        r"""Gets the product_name of this Gpu.

        产品名。

        :return: The product_name of this Gpu.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this Gpu.

        产品名。

        :param product_name: The product_name of this Gpu.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def memory(self):
        r"""Gets the memory of this Gpu.

        内存。

        :return: The memory of this Gpu.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this Gpu.

        内存。

        :param memory: The memory of this Gpu.
        :type memory: str
        """
        self._memory = memory

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
        if not isinstance(other, Gpu):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
