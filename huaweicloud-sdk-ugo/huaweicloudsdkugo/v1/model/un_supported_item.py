# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnSupportedItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reason': 'str',
        'suggestion': 'str',
        'line_number': 'int',
        'position': 'int'
    }

    attribute_map = {
        'reason': 'reason',
        'suggestion': 'suggestion',
        'line_number': 'line_number',
        'position': 'position'
    }

    def __init__(self, reason=None, suggestion=None, line_number=None, position=None):
        """UnSupportedItem

        The model defined in huaweicloud sdk

        :param reason: SQL语句不支持转换的原因。
        :type reason: str
        :param suggestion: SQL语句不支持转换的建议。
        :type suggestion: str
        :param line_number: 行号。
        :type line_number: int
        :param position: 位置。
        :type position: int
        """
        
        

        self._reason = None
        self._suggestion = None
        self._line_number = None
        self._position = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason
        if suggestion is not None:
            self.suggestion = suggestion
        if line_number is not None:
            self.line_number = line_number
        if position is not None:
            self.position = position

    @property
    def reason(self):
        """Gets the reason of this UnSupportedItem.

        SQL语句不支持转换的原因。

        :return: The reason of this UnSupportedItem.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this UnSupportedItem.

        SQL语句不支持转换的原因。

        :param reason: The reason of this UnSupportedItem.
        :type reason: str
        """
        self._reason = reason

    @property
    def suggestion(self):
        """Gets the suggestion of this UnSupportedItem.

        SQL语句不支持转换的建议。

        :return: The suggestion of this UnSupportedItem.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this UnSupportedItem.

        SQL语句不支持转换的建议。

        :param suggestion: The suggestion of this UnSupportedItem.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def line_number(self):
        """Gets the line_number of this UnSupportedItem.

        行号。

        :return: The line_number of this UnSupportedItem.
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this UnSupportedItem.

        行号。

        :param line_number: The line_number of this UnSupportedItem.
        :type line_number: int
        """
        self._line_number = line_number

    @property
    def position(self):
        """Gets the position of this UnSupportedItem.

        位置。

        :return: The position of this UnSupportedItem.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this UnSupportedItem.

        位置。

        :param position: The position of this UnSupportedItem.
        :type position: int
        """
        self._position = position

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
        if not isinstance(other, UnSupportedItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
