# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IgnoreAdvanced:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index': 'str',
        'contents': 'list[str]'
    }

    attribute_map = {
        'index': 'index',
        'contents': 'contents'
    }

    def __init__(self, index=None, contents=None):
        """IgnoreAdvanced

        The model defined in huaweicloud sdk

        :param index: 字段类型，支持的字段类型有：Params、Cookie、Header、Body、Multipart。   - 当选择“Params”、“Cookie”或者“Header”字段时，可以配置“全部”或根据需求配置子字段   - 当选择“Body”或“Multipart”字段时，可以配置“全部”
        :type index: str
        :param contents: 指定字段类型的子字段，默认值为“全部”
        :type contents: list[str]
        """
        
        

        self._index = None
        self._contents = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if contents is not None:
            self.contents = contents

    @property
    def index(self):
        """Gets the index of this IgnoreAdvanced.

        字段类型，支持的字段类型有：Params、Cookie、Header、Body、Multipart。   - 当选择“Params”、“Cookie”或者“Header”字段时，可以配置“全部”或根据需求配置子字段   - 当选择“Body”或“Multipart”字段时，可以配置“全部”

        :return: The index of this IgnoreAdvanced.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this IgnoreAdvanced.

        字段类型，支持的字段类型有：Params、Cookie、Header、Body、Multipart。   - 当选择“Params”、“Cookie”或者“Header”字段时，可以配置“全部”或根据需求配置子字段   - 当选择“Body”或“Multipart”字段时，可以配置“全部”

        :param index: The index of this IgnoreAdvanced.
        :type index: str
        """
        self._index = index

    @property
    def contents(self):
        """Gets the contents of this IgnoreAdvanced.

        指定字段类型的子字段，默认值为“全部”

        :return: The contents of this IgnoreAdvanced.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this IgnoreAdvanced.

        指定字段类型的子字段，默认值为“全部”

        :param contents: The contents of this IgnoreAdvanced.
        :type contents: list[str]
        """
        self._contents = contents

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
        if not isinstance(other, IgnoreAdvanced):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
