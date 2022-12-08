# coding: utf-8

import re
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
        'size': 'str',
        'share_type': 'str',
        'charge_mode': 'str',
        'product_id': 'str'
    }

    attribute_map = {
        'size': 'size',
        'share_type': 'share_type',
        'charge_mode': 'charge_mode',
        'product_id': 'product_id'
    }

    def __init__(self, size=None, share_type=None, charge_mode=None, product_id=None):
        """BandWidth

        The model defined in huaweicloud sdk

        :param size: 带宽，按需1-100，包年包月1-300
        :type size: str
        :param share_type: 共享类型 目前只支持PER
        :type share_type: str
        :param charge_mode: 带宽计费类型 未traffic或为空
        :type charge_mode: str
        :param product_id: 带宽对应产品ID
        :type product_id: str
        """
        
        

        self._size = None
        self._share_type = None
        self._charge_mode = None
        self._product_id = None
        self.discriminator = None

        self.size = size
        self.share_type = share_type
        self.charge_mode = charge_mode
        self.product_id = product_id

    @property
    def size(self):
        """Gets the size of this BandWidth.

        带宽，按需1-100，包年包月1-300

        :return: The size of this BandWidth.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BandWidth.

        带宽，按需1-100，包年包月1-300

        :param size: The size of this BandWidth.
        :type size: str
        """
        self._size = size

    @property
    def share_type(self):
        """Gets the share_type of this BandWidth.

        共享类型 目前只支持PER

        :return: The share_type of this BandWidth.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this BandWidth.

        共享类型 目前只支持PER

        :param share_type: The share_type of this BandWidth.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this BandWidth.

        带宽计费类型 未traffic或为空

        :return: The charge_mode of this BandWidth.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this BandWidth.

        带宽计费类型 未traffic或为空

        :param charge_mode: The charge_mode of this BandWidth.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def product_id(self):
        """Gets the product_id of this BandWidth.

        带宽对应产品ID

        :return: The product_id of this BandWidth.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this BandWidth.

        带宽对应产品ID

        :param product_id: The product_id of this BandWidth.
        :type product_id: str
        """
        self._product_id = product_id

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
