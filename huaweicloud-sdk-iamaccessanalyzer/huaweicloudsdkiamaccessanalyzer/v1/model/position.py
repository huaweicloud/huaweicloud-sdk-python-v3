# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Position:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'line': 'int',
        'column': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'line': 'line',
        'column': 'column',
        'offset': 'offset'
    }

    def __init__(self, line=None, column=None, offset=None):
        r"""Position

        The model defined in huaweicloud sdk

        :param line: 位置的行号，从1开始。
        :type line: int
        :param column: 位置的列号，从0开始。
        :type column: int
        :param offset: 策略中与位置对应的偏移量，从0开始。
        :type offset: int
        """
        
        

        self._line = None
        self._column = None
        self._offset = None
        self.discriminator = None

        self.line = line
        self.column = column
        self.offset = offset

    @property
    def line(self):
        r"""Gets the line of this Position.

        位置的行号，从1开始。

        :return: The line of this Position.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this Position.

        位置的行号，从1开始。

        :param line: The line of this Position.
        :type line: int
        """
        self._line = line

    @property
    def column(self):
        r"""Gets the column of this Position.

        位置的列号，从0开始。

        :return: The column of this Position.
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        r"""Sets the column of this Position.

        位置的列号，从0开始。

        :param column: The column of this Position.
        :type column: int
        """
        self._column = column

    @property
    def offset(self):
        r"""Gets the offset of this Position.

        策略中与位置对应的偏移量，从0开始。

        :return: The offset of this Position.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this Position.

        策略中与位置对应的偏移量，从0开始。

        :param offset: The offset of this Position.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, Position):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
