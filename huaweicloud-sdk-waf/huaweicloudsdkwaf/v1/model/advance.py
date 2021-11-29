# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Advance:


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
        """Advance - a model defined in huaweicloud sdk"""
        
        

        self._index = None
        self._contents = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if contents is not None:
            self.contents = contents

    @property
    def index(self):
        """Gets the index of this Advance.

        索引（参数：params，会话cookie：cookie，header字段：header，body字段：body，多种组合：multipart）

        :return: The index of this Advance.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Advance.

        索引（参数：params，会话cookie：cookie，header字段：header，body字段：body，多种组合：multipart）

        :param index: The index of this Advance.
        :type: str
        """
        self._index = index

    @property
    def contents(self):
        """Gets the contents of this Advance.

        指定字段（仅在param，cookie，header模式下可以使用）

        :return: The contents of this Advance.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this Advance.

        指定字段（仅在param，cookie，header模式下可以使用）

        :param contents: The contents of this Advance.
        :type: list[str]
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
        if not isinstance(other, Advance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
