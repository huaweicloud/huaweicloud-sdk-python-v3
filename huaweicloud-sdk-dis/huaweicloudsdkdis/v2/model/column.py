# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Column:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_family_name': 'str',
        'column_name': 'str',
        'value': 'str',
        'type': 'str'
    }

    attribute_map = {
        'column_family_name': 'column_family_name',
        'column_name': 'column_name',
        'value': 'value',
        'type': 'type'
    }

    def __init__(self, column_family_name=None, column_name=None, value=None, type=None):
        r"""Column

        The model defined in huaweicloud sdk

        :param column_family_name: 存储该通道数据的HBase表数据的列族名称。
        :type column_family_name: str
        :param column_name: 存储该通道数据的HBase表数据的列名称。  取值范围：1～32，只能包含英文字母、数字和下划线。
        :type column_name: str
        :param value: 通道内JSON数据的JSON属性名，用于生成HBase数据的列值。
        :type value: str
        :param type: 通道内JSON数据的JSON属性的类型名称。
        :type type: str
        """
        
        

        self._column_family_name = None
        self._column_name = None
        self._value = None
        self._type = None
        self.discriminator = None

        self.column_family_name = column_family_name
        self.column_name = column_name
        self.value = value
        self.type = type

    @property
    def column_family_name(self):
        r"""Gets the column_family_name of this Column.

        存储该通道数据的HBase表数据的列族名称。

        :return: The column_family_name of this Column.
        :rtype: str
        """
        return self._column_family_name

    @column_family_name.setter
    def column_family_name(self, column_family_name):
        r"""Sets the column_family_name of this Column.

        存储该通道数据的HBase表数据的列族名称。

        :param column_family_name: The column_family_name of this Column.
        :type column_family_name: str
        """
        self._column_family_name = column_family_name

    @property
    def column_name(self):
        r"""Gets the column_name of this Column.

        存储该通道数据的HBase表数据的列名称。  取值范围：1～32，只能包含英文字母、数字和下划线。

        :return: The column_name of this Column.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this Column.

        存储该通道数据的HBase表数据的列名称。  取值范围：1～32，只能包含英文字母、数字和下划线。

        :param column_name: The column_name of this Column.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def value(self):
        r"""Gets the value of this Column.

        通道内JSON数据的JSON属性名，用于生成HBase数据的列值。

        :return: The value of this Column.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Column.

        通道内JSON数据的JSON属性名，用于生成HBase数据的列值。

        :param value: The value of this Column.
        :type value: str
        """
        self._value = value

    @property
    def type(self):
        r"""Gets the type of this Column.

        通道内JSON数据的JSON属性的类型名称。

        :return: The type of this Column.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Column.

        通道内JSON数据的JSON属性的类型名称。

        :param type: The type of this Column.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, Column):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
