# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'maxitems': 'str',
        'package_name': 'str',
        'func_name': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'maxitems': 'maxitems',
        'package_name': 'package_name',
        'func_name': 'func_name'
    }

    def __init__(self, marker=None, maxitems=None, package_name=None, func_name=None):
        r"""ListFunctionsRequest

        The model defined in huaweicloud sdk

        :param marker: 上一次查询到的最后的记录位置。
        :type marker: str
        :param maxitems: 每次查询获取的最大函数记录数量 最大值：400 如果不提供该值或者提供的值大于400或等于0，则使用默认值：400 如果该值小于0，则返回参数错误。
        :type maxitems: str
        :param package_name: 自定义分组名称。
        :type package_name: str
        :param func_name: 函数名称。支持模糊查询
        :type func_name: str
        """
        
        

        self._marker = None
        self._maxitems = None
        self._package_name = None
        self._func_name = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if maxitems is not None:
            self.maxitems = maxitems
        if package_name is not None:
            self.package_name = package_name
        if func_name is not None:
            self.func_name = func_name

    @property
    def marker(self):
        r"""Gets the marker of this ListFunctionsRequest.

        上一次查询到的最后的记录位置。

        :return: The marker of this ListFunctionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListFunctionsRequest.

        上一次查询到的最后的记录位置。

        :param marker: The marker of this ListFunctionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def maxitems(self):
        r"""Gets the maxitems of this ListFunctionsRequest.

        每次查询获取的最大函数记录数量 最大值：400 如果不提供该值或者提供的值大于400或等于0，则使用默认值：400 如果该值小于0，则返回参数错误。

        :return: The maxitems of this ListFunctionsRequest.
        :rtype: str
        """
        return self._maxitems

    @maxitems.setter
    def maxitems(self, maxitems):
        r"""Sets the maxitems of this ListFunctionsRequest.

        每次查询获取的最大函数记录数量 最大值：400 如果不提供该值或者提供的值大于400或等于0，则使用默认值：400 如果该值小于0，则返回参数错误。

        :param maxitems: The maxitems of this ListFunctionsRequest.
        :type maxitems: str
        """
        self._maxitems = maxitems

    @property
    def package_name(self):
        r"""Gets the package_name of this ListFunctionsRequest.

        自定义分组名称。

        :return: The package_name of this ListFunctionsRequest.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        r"""Sets the package_name of this ListFunctionsRequest.

        自定义分组名称。

        :param package_name: The package_name of this ListFunctionsRequest.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def func_name(self):
        r"""Gets the func_name of this ListFunctionsRequest.

        函数名称。支持模糊查询

        :return: The func_name of this ListFunctionsRequest.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        r"""Sets the func_name of this ListFunctionsRequest.

        函数名称。支持模糊查询

        :param func_name: The func_name of this ListFunctionsRequest.
        :type func_name: str
        """
        self._func_name = func_name

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
        if not isinstance(other, ListFunctionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
