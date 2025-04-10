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
        'functions': 'list[ListFunctionResult]',
        'next_marker': 'int',
        'count': 'int'
    }

    attribute_map = {
        'functions': 'functions',
        'next_marker': 'next_marker',
        'count': 'count'
    }

    def __init__(self, functions=None, next_marker=None, count=None):
        r"""ListFunctionsResponse

        The model defined in huaweicloud sdk

        :param functions: 函数列表。
        :type functions: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionResult`]
        :param next_marker: 函数下次记录读取位置。
        :type next_marker: int
        :param count: 满足查询条件的函数总数。
        :type count: int
        """
        
        super(ListFunctionsResponse, self).__init__()

        self._functions = None
        self._next_marker = None
        self._count = None
        self.discriminator = None

        if functions is not None:
            self.functions = functions
        if next_marker is not None:
            self.next_marker = next_marker
        if count is not None:
            self.count = count

    @property
    def functions(self):
        r"""Gets the functions of this ListFunctionsResponse.

        函数列表。

        :return: The functions of this ListFunctionsResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionResult`]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        r"""Sets the functions of this ListFunctionsResponse.

        函数列表。

        :param functions: The functions of this ListFunctionsResponse.
        :type functions: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionResult`]
        """
        self._functions = functions

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListFunctionsResponse.

        函数下次记录读取位置。

        :return: The next_marker of this ListFunctionsResponse.
        :rtype: int
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListFunctionsResponse.

        函数下次记录读取位置。

        :param next_marker: The next_marker of this ListFunctionsResponse.
        :type next_marker: int
        """
        self._next_marker = next_marker

    @property
    def count(self):
        r"""Gets the count of this ListFunctionsResponse.

        满足查询条件的函数总数。

        :return: The count of this ListFunctionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListFunctionsResponse.

        满足查询条件的函数总数。

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
