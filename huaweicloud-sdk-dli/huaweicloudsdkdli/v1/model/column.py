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
        'column_name': 'str',
        'type': 'str',
        'description': 'str',
        'is_partition_column': 'bool'
    }

    attribute_map = {
        'column_name': 'column_name',
        'type': 'type',
        'description': 'description',
        'is_partition_column': 'is_partition_column'
    }

    def __init__(self, column_name=None, type=None, description=None, is_partition_column=None):
        r"""Column

        The model defined in huaweicloud sdk

        :param column_name: 列的名称。
        :type column_name: str
        :param type: 列的数据类型。
        :type type: str
        :param description: 列的描述信息。
        :type description: str
        :param is_partition_column: 表示该列是否为分区列。“true”表示为分区列，“false”为非分区列，默认为“false”。
        :type is_partition_column: bool
        """
        
        

        self._column_name = None
        self._type = None
        self._description = None
        self._is_partition_column = None
        self.discriminator = None

        self.column_name = column_name
        self.type = type
        if description is not None:
            self.description = description
        if is_partition_column is not None:
            self.is_partition_column = is_partition_column

    @property
    def column_name(self):
        r"""Gets the column_name of this Column.

        列的名称。

        :return: The column_name of this Column.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this Column.

        列的名称。

        :param column_name: The column_name of this Column.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def type(self):
        r"""Gets the type of this Column.

        列的数据类型。

        :return: The type of this Column.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Column.

        列的数据类型。

        :param type: The type of this Column.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this Column.

        列的描述信息。

        :return: The description of this Column.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Column.

        列的描述信息。

        :param description: The description of this Column.
        :type description: str
        """
        self._description = description

    @property
    def is_partition_column(self):
        r"""Gets the is_partition_column of this Column.

        表示该列是否为分区列。“true”表示为分区列，“false”为非分区列，默认为“false”。

        :return: The is_partition_column of this Column.
        :rtype: bool
        """
        return self._is_partition_column

    @is_partition_column.setter
    def is_partition_column(self, is_partition_column):
        r"""Sets the is_partition_column of this Column.

        表示该列是否为分区列。“true”表示为分区列，“false”为非分区列，默认为“false”。

        :param is_partition_column: The is_partition_column of this Column.
        :type is_partition_column: bool
        """
        self._is_partition_column = is_partition_column

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
