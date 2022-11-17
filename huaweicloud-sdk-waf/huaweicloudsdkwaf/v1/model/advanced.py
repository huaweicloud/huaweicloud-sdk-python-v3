# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Advanced:

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
        'contensts': 'list[str]'
    }

    attribute_map = {
        'index': 'index',
        'contensts': 'contensts'
    }

    def __init__(self, index=None, contensts=None):
        """Advanced

        The model defined in huaweicloud sdk

        :param index: 字段类型，支持的字段类型有：Params、Cookie、Header、Body、Multipart。   - 当选择“Params”、“Cookie”或者“Header”字段时，可以配置“全部”或根据需求配置子字段   - 当选择“Body”或“Multipart”字段时，可以配置“全部”
        :type index: str
        :param contensts: 指定字段类型的子字段，默认值为“全部”
        :type contensts: list[str]
        """
        
        

        self._index = None
        self._contensts = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if contensts is not None:
            self.contensts = contensts

    @property
    def index(self):
        """Gets the index of this Advanced.

        字段类型，支持的字段类型有：Params、Cookie、Header、Body、Multipart。   - 当选择“Params”、“Cookie”或者“Header”字段时，可以配置“全部”或根据需求配置子字段   - 当选择“Body”或“Multipart”字段时，可以配置“全部”

        :return: The index of this Advanced.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Advanced.

        字段类型，支持的字段类型有：Params、Cookie、Header、Body、Multipart。   - 当选择“Params”、“Cookie”或者“Header”字段时，可以配置“全部”或根据需求配置子字段   - 当选择“Body”或“Multipart”字段时，可以配置“全部”

        :param index: The index of this Advanced.
        :type index: str
        """
        self._index = index

    @property
    def contensts(self):
        """Gets the contensts of this Advanced.

        指定字段类型的子字段，默认值为“全部”

        :return: The contensts of this Advanced.
        :rtype: list[str]
        """
        return self._contensts

    @contensts.setter
    def contensts(self, contensts):
        """Sets the contensts of this Advanced.

        指定字段类型的子字段，默认值为“全部”

        :param contensts: The contensts of this Advanced.
        :type contensts: list[str]
        """
        self._contensts = contensts

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
        if not isinstance(other, Advanced):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
