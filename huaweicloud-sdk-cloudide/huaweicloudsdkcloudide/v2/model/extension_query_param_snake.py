# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionQueryParamSnake:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filters': 'list[FilterSnake]',
        'flags': 'int'
    }

    attribute_map = {
        'filters': 'filters',
        'flags': 'flags'
    }

    def __init__(self, filters=None, flags=None):
        """ExtensionQueryParamSnake

        The model defined in huaweicloud sdk

        :param filters: 过滤字段
        :type filters: list[:class:`huaweicloudsdkcloudide.v2.FilterSnake`]
        :param flags: 插件flag;通过传递flag参数来进行过滤或其他操作。flag的基础数字是2\\4\\8\\16;传递的参数只能是这四个数字加法组合而成数字 利用它们之间二进制的运算获取的值进行其他操作.比如6&#x3D;0110&#x3D;0010+0100也就是2和4的集合flags
        :type flags: int
        """
        
        

        self._filters = None
        self._flags = None
        self.discriminator = None

        self.filters = filters
        self.flags = flags

    @property
    def filters(self):
        """Gets the filters of this ExtensionQueryParamSnake.

        过滤字段

        :return: The filters of this ExtensionQueryParamSnake.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.FilterSnake`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ExtensionQueryParamSnake.

        过滤字段

        :param filters: The filters of this ExtensionQueryParamSnake.
        :type filters: list[:class:`huaweicloudsdkcloudide.v2.FilterSnake`]
        """
        self._filters = filters

    @property
    def flags(self):
        """Gets the flags of this ExtensionQueryParamSnake.

        插件flag;通过传递flag参数来进行过滤或其他操作。flag的基础数字是2\\4\\8\\16;传递的参数只能是这四个数字加法组合而成数字 利用它们之间二进制的运算获取的值进行其他操作.比如6=0110=0010+0100也就是2和4的集合flags

        :return: The flags of this ExtensionQueryParamSnake.
        :rtype: int
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this ExtensionQueryParamSnake.

        插件flag;通过传递flag参数来进行过滤或其他操作。flag的基础数字是2\\4\\8\\16;传递的参数只能是这四个数字加法组合而成数字 利用它们之间二进制的运算获取的值进行其他操作.比如6=0110=0010+0100也就是2和4的集合flags

        :param flags: The flags of this ExtensionQueryParamSnake.
        :type flags: int
        """
        self._flags = flags

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
        if not isinstance(other, ExtensionQueryParamSnake):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
