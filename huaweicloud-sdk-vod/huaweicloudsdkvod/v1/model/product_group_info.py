# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductGroupInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'products': 'list[ProductUrlInfo]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'products': 'products'
    }

    def __init__(self, group_id=None, products=None):
        r"""ProductGroupInfo

        The model defined in huaweicloud sdk

        :param group_id: 模板组ID
        :type group_id: str
        :param products: 产物信息
        :type products: list[:class:`huaweicloudsdkvod.v1.ProductUrlInfo`]
        """
        
        

        self._group_id = None
        self._products = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if products is not None:
            self.products = products

    @property
    def group_id(self):
        r"""Gets the group_id of this ProductGroupInfo.

        模板组ID

        :return: The group_id of this ProductGroupInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ProductGroupInfo.

        模板组ID

        :param group_id: The group_id of this ProductGroupInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def products(self):
        r"""Gets the products of this ProductGroupInfo.

        产物信息

        :return: The products of this ProductGroupInfo.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ProductUrlInfo`]
        """
        return self._products

    @products.setter
    def products(self, products):
        r"""Sets the products of this ProductGroupInfo.

        产物信息

        :param products: The products of this ProductGroupInfo.
        :type products: list[:class:`huaweicloudsdkvod.v1.ProductUrlInfo`]
        """
        self._products = products

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
        if not isinstance(other, ProductGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
