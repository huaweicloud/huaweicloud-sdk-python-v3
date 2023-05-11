# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtremumDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'float',
        'row_number': 'int',
        'column_name': 'str',
        'row_name': 'str'
    }

    attribute_map = {
        'value': 'value',
        'row_number': 'row_number',
        'column_name': 'column_name',
        'row_name': 'row_name'
    }

    def __init__(self, value=None, row_number=None, column_name=None, row_name=None):
        """ExtremumDto

        The model defined in huaweicloud sdk

        :param value: 最值
        :type value: float
        :param row_number: 最值所在的行数
        :type row_number: int
        :param column_name: 最值所在的列名
        :type column_name: str
        :param row_name: 最值所在的行名
        :type row_name: str
        """
        
        

        self._value = None
        self._row_number = None
        self._column_name = None
        self._row_name = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if row_number is not None:
            self.row_number = row_number
        if column_name is not None:
            self.column_name = column_name
        if row_name is not None:
            self.row_name = row_name

    @property
    def value(self):
        """Gets the value of this ExtremumDto.

        最值

        :return: The value of this ExtremumDto.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ExtremumDto.

        最值

        :param value: The value of this ExtremumDto.
        :type value: float
        """
        self._value = value

    @property
    def row_number(self):
        """Gets the row_number of this ExtremumDto.

        最值所在的行数

        :return: The row_number of this ExtremumDto.
        :rtype: int
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number):
        """Sets the row_number of this ExtremumDto.

        最值所在的行数

        :param row_number: The row_number of this ExtremumDto.
        :type row_number: int
        """
        self._row_number = row_number

    @property
    def column_name(self):
        """Gets the column_name of this ExtremumDto.

        最值所在的列名

        :return: The column_name of this ExtremumDto.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ExtremumDto.

        最值所在的列名

        :param column_name: The column_name of this ExtremumDto.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def row_name(self):
        """Gets the row_name of this ExtremumDto.

        最值所在的行名

        :return: The row_name of this ExtremumDto.
        :rtype: str
        """
        return self._row_name

    @row_name.setter
    def row_name(self, row_name):
        """Sets the row_name of this ExtremumDto.

        最值所在的行名

        :param row_name: The row_name of this ExtremumDto.
        :type row_name: str
        """
        self._row_name = row_name

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
        if not isinstance(other, ExtremumDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
