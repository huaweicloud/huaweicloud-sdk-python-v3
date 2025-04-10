# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_functions': 'list[FunctionDTO]',
        'count': 'int'
    }

    attribute_map = {
        'product_functions': 'product_functions',
        'count': 'count'
    }

    def __init__(self, product_functions=None, count=None):
        r"""ListFunctionsResponse

        The model defined in huaweicloud sdk

        :param product_functions: **参数说明**：编解码函数列表。
        :type product_functions: list[:class:`huaweicloudsdkiotda.v5.FunctionDTO`]
        :param count: **参数说明**：满足查询条件的记录总数。
        :type count: int
        """
        
        super(ListFunctionsResponse, self).__init__()

        self._product_functions = None
        self._count = None
        self.discriminator = None

        if product_functions is not None:
            self.product_functions = product_functions
        if count is not None:
            self.count = count

    @property
    def product_functions(self):
        r"""Gets the product_functions of this ListFunctionsResponse.

        **参数说明**：编解码函数列表。

        :return: The product_functions of this ListFunctionsResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.FunctionDTO`]
        """
        return self._product_functions

    @product_functions.setter
    def product_functions(self, product_functions):
        r"""Sets the product_functions of this ListFunctionsResponse.

        **参数说明**：编解码函数列表。

        :param product_functions: The product_functions of this ListFunctionsResponse.
        :type product_functions: list[:class:`huaweicloudsdkiotda.v5.FunctionDTO`]
        """
        self._product_functions = product_functions

    @property
    def count(self):
        r"""Gets the count of this ListFunctionsResponse.

        **参数说明**：满足查询条件的记录总数。

        :return: The count of this ListFunctionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListFunctionsResponse.

        **参数说明**：满足查询条件的记录总数。

        :param count: The count of this ListFunctionsResponse.
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
        if not isinstance(other, ListFunctionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
