# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlatformProductInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'product_title': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'product_title': 'product_title'
    }

    def __init__(self, product_id=None, product_title=None):
        """PlatformProductInfo

        The model defined in huaweicloud sdk

        :param product_id: 商品id
        :type product_id: str
        :param product_title: 商品标题
        :type product_title: str
        """
        
        

        self._product_id = None
        self._product_title = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if product_title is not None:
            self.product_title = product_title

    @property
    def product_id(self):
        """Gets the product_id of this PlatformProductInfo.

        商品id

        :return: The product_id of this PlatformProductInfo.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this PlatformProductInfo.

        商品id

        :param product_id: The product_id of this PlatformProductInfo.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_title(self):
        """Gets the product_title of this PlatformProductInfo.

        商品标题

        :return: The product_title of this PlatformProductInfo.
        :rtype: str
        """
        return self._product_title

    @product_title.setter
    def product_title(self, product_title):
        """Sets the product_title of this PlatformProductInfo.

        商品标题

        :param product_title: The product_title of this PlatformProductInfo.
        :type product_title: str
        """
        self._product_title = product_title

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
        if not isinstance(other, PlatformProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
