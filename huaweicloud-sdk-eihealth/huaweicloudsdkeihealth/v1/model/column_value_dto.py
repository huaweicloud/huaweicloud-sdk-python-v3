# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnValueDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'column': 'str',
        'value': 'str'
    }

    attribute_map = {
        'column': 'column',
        'value': 'value'
    }

    def __init__(self, column=None, value=None):
        """ColumnValueDto

        The model defined in huaweicloud sdk

        :param column: 列名
        :type column: str
        :param value: 该列对应的值
        :type value: str
        """
        
        

        self._column = None
        self._value = None
        self.discriminator = None

        if column is not None:
            self.column = column
        if value is not None:
            self.value = value

    @property
    def column(self):
        """Gets the column of this ColumnValueDto.

        列名

        :return: The column of this ColumnValueDto.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this ColumnValueDto.

        列名

        :param column: The column of this ColumnValueDto.
        :type column: str
        """
        self._column = column

    @property
    def value(self):
        """Gets the value of this ColumnValueDto.

        该列对应的值

        :return: The value of this ColumnValueDto.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ColumnValueDto.

        该列对应的值

        :param value: The value of this ColumnValueDto.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, ColumnValueDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
