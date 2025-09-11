# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandWidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chargemode': 'str',
        'productid': 'str',
        'sharetype': 'str',
        'size': 'int'
    }

    attribute_map = {
        'chargemode': 'chargemode',
        'productid': 'productid',
        'sharetype': 'sharetype',
        'size': 'size'
    }

    def __init__(self, chargemode=None, productid=None, sharetype=None, size=None):
        r"""BandWidth

        The model defined in huaweicloud sdk

        :param chargemode: 计费类型
        :type chargemode: str
        :param productid: 带宽对应产品ID
        :type productid: str
        :param sharetype: 共享类型，目前仅支持PER
        :type sharetype: str
        :param size: 带宽，按需1-100M，包年包月1-300M
        :type size: int
        """
        
        

        self._chargemode = None
        self._productid = None
        self._sharetype = None
        self._size = None
        self.discriminator = None

        if chargemode is not None:
            self.chargemode = chargemode
        if productid is not None:
            self.productid = productid
        if sharetype is not None:
            self.sharetype = sharetype
        if size is not None:
            self.size = size

    @property
    def chargemode(self):
        r"""Gets the chargemode of this BandWidth.

        计费类型

        :return: The chargemode of this BandWidth.
        :rtype: str
        """
        return self._chargemode

    @chargemode.setter
    def chargemode(self, chargemode):
        r"""Sets the chargemode of this BandWidth.

        计费类型

        :param chargemode: The chargemode of this BandWidth.
        :type chargemode: str
        """
        self._chargemode = chargemode

    @property
    def productid(self):
        r"""Gets the productid of this BandWidth.

        带宽对应产品ID

        :return: The productid of this BandWidth.
        :rtype: str
        """
        return self._productid

    @productid.setter
    def productid(self, productid):
        r"""Sets the productid of this BandWidth.

        带宽对应产品ID

        :param productid: The productid of this BandWidth.
        :type productid: str
        """
        self._productid = productid

    @property
    def sharetype(self):
        r"""Gets the sharetype of this BandWidth.

        共享类型，目前仅支持PER

        :return: The sharetype of this BandWidth.
        :rtype: str
        """
        return self._sharetype

    @sharetype.setter
    def sharetype(self, sharetype):
        r"""Sets the sharetype of this BandWidth.

        共享类型，目前仅支持PER

        :param sharetype: The sharetype of this BandWidth.
        :type sharetype: str
        """
        self._sharetype = sharetype

    @property
    def size(self):
        r"""Gets the size of this BandWidth.

        带宽，按需1-100M，包年包月1-300M

        :return: The size of this BandWidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BandWidth.

        带宽，按需1-100M，包年包月1-300M

        :param size: The size of this BandWidth.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, BandWidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
