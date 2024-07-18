# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductGroupDelFailInfo:

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
        'fail_reason': 'str',
        'products': 'list[ProductDelFailInfo]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'fail_reason': 'fail_reason',
        'products': 'products'
    }

    def __init__(self, group_id=None, fail_reason=None, products=None):
        """ProductGroupDelFailInfo

        The model defined in huaweicloud sdk

        :param group_id: 模板组ID
        :type group_id: str
        :param fail_reason: 模板组删除失败的原因
        :type fail_reason: str
        :param products: 删除失败的产物的信息
        :type products: list[:class:`huaweicloudsdkvod.v1.ProductDelFailInfo`]
        """
        
        

        self._group_id = None
        self._fail_reason = None
        self._products = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if products is not None:
            self.products = products

    @property
    def group_id(self):
        """Gets the group_id of this ProductGroupDelFailInfo.

        模板组ID

        :return: The group_id of this ProductGroupDelFailInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ProductGroupDelFailInfo.

        模板组ID

        :param group_id: The group_id of this ProductGroupDelFailInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ProductGroupDelFailInfo.

        模板组删除失败的原因

        :return: The fail_reason of this ProductGroupDelFailInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ProductGroupDelFailInfo.

        模板组删除失败的原因

        :param fail_reason: The fail_reason of this ProductGroupDelFailInfo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def products(self):
        """Gets the products of this ProductGroupDelFailInfo.

        删除失败的产物的信息

        :return: The products of this ProductGroupDelFailInfo.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ProductDelFailInfo`]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this ProductGroupDelFailInfo.

        删除失败的产物的信息

        :param products: The products of this ProductGroupDelFailInfo.
        :type products: list[:class:`huaweicloudsdkvod.v1.ProductDelFailInfo`]
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
        if not isinstance(other, ProductGroupDelFailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
