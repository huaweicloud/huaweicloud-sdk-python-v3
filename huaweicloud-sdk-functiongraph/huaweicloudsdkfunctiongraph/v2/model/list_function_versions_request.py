# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionVersionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'marker': 'str',
        'maxitems': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'marker': 'marker',
        'maxitems': 'maxitems'
    }

    def __init__(self, function_urn=None, marker=None, maxitems=None):
        """ListFunctionVersionsRequest

        The model defined in huaweicloud sdk

        :param function_urn: 函数的URN，详细解释见FunctionGraph函数模型的描述。
        :type function_urn: str
        :param marker: 上一次查询到的最后的记录位置。
        :type marker: str
        :param maxitems: 每次查询获取的最大函数记录数量。
        :type maxitems: str
        """
        
        

        self._function_urn = None
        self._marker = None
        self._maxitems = None
        self.discriminator = None

        self.function_urn = function_urn
        if marker is not None:
            self.marker = marker
        if maxitems is not None:
            self.maxitems = maxitems

    @property
    def function_urn(self):
        """Gets the function_urn of this ListFunctionVersionsRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :return: The function_urn of this ListFunctionVersionsRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this ListFunctionVersionsRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :param function_urn: The function_urn of this ListFunctionVersionsRequest.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def marker(self):
        """Gets the marker of this ListFunctionVersionsRequest.

        上一次查询到的最后的记录位置。

        :return: The marker of this ListFunctionVersionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListFunctionVersionsRequest.

        上一次查询到的最后的记录位置。

        :param marker: The marker of this ListFunctionVersionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def maxitems(self):
        """Gets the maxitems of this ListFunctionVersionsRequest.

        每次查询获取的最大函数记录数量。

        :return: The maxitems of this ListFunctionVersionsRequest.
        :rtype: str
        """
        return self._maxitems

    @maxitems.setter
    def maxitems(self, maxitems):
        """Sets the maxitems of this ListFunctionVersionsRequest.

        每次查询获取的最大函数记录数量。

        :param maxitems: The maxitems of this ListFunctionVersionsRequest.
        :type maxitems: str
        """
        self._maxitems = maxitems

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
        if not isinstance(other, ListFunctionVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
