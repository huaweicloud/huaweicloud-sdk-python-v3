# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcePrice:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'price': 'float',
        'size': 'str',
        'type': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'price': 'price',
        'size': 'size',
        'type': 'type'
    }

    def __init__(self, arch=None, price=None, size=None, type=None):
        r"""ResourcePrice

        The model defined in huaweicloud sdk

        :param arch: cpu架构 x86|arm
        :type arch: str
        :param price: 价格
        :type price: float
        :param size: 规格。 类型为&#39;storage&#39;时，size值可以为5GB，10GB，20GB。 类型为&#39;cpuMemory&#39;时，arch为&#39;x86&#39;，size值可以为1U1G，2U4G，4U8G；arch为&#39;arm&#39;，size值可以为4U8G。
        :type size: str
        :param type: 类型。目前可以取值storage，cpuMemory
        :type type: str
        """
        
        

        self._arch = None
        self._price = None
        self._size = None
        self._type = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        if price is not None:
            self.price = price
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type

    @property
    def arch(self):
        r"""Gets the arch of this ResourcePrice.

        cpu架构 x86|arm

        :return: The arch of this ResourcePrice.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ResourcePrice.

        cpu架构 x86|arm

        :param arch: The arch of this ResourcePrice.
        :type arch: str
        """
        self._arch = arch

    @property
    def price(self):
        r"""Gets the price of this ResourcePrice.

        价格

        :return: The price of this ResourcePrice.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        r"""Sets the price of this ResourcePrice.

        价格

        :param price: The price of this ResourcePrice.
        :type price: float
        """
        self._price = price

    @property
    def size(self):
        r"""Gets the size of this ResourcePrice.

        规格。 类型为'storage'时，size值可以为5GB，10GB，20GB。 类型为'cpuMemory'时，arch为'x86'，size值可以为1U1G，2U4G，4U8G；arch为'arm'，size值可以为4U8G。

        :return: The size of this ResourcePrice.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ResourcePrice.

        规格。 类型为'storage'时，size值可以为5GB，10GB，20GB。 类型为'cpuMemory'时，arch为'x86'，size值可以为1U1G，2U4G，4U8G；arch为'arm'，size值可以为4U8G。

        :param size: The size of this ResourcePrice.
        :type size: str
        """
        self._size = size

    @property
    def type(self):
        r"""Gets the type of this ResourcePrice.

        类型。目前可以取值storage，cpuMemory

        :return: The type of this ResourcePrice.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourcePrice.

        类型。目前可以取值storage，cpuMemory

        :param type: The type of this ResourcePrice.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ResourcePrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
