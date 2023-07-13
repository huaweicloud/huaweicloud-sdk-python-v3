# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnsList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'comment': 'str',
        'column_name': 'str',
        'column_type': 'str',
        'seq_number': 'int',
        'primary': 'bool',
        'partition_col': 'bool'
    }

    attribute_map = {
        'comment': 'comment',
        'column_name': 'column_name',
        'column_type': 'column_type',
        'seq_number': 'seq_number',
        'primary': 'primary',
        'partition_col': 'partition_col'
    }

    def __init__(self, comment=None, column_name=None, column_type=None, seq_number=None, primary=None, partition_col=None):
        """ColumnsList

        The model defined in huaweicloud sdk

        :param comment: 字段注解
        :type comment: str
        :param column_name: 字段名称
        :type column_name: str
        :param column_type: 字段类型
        :type column_type: str
        :param seq_number: 字段的顺序
        :type seq_number: int
        :param primary: 字段是否为主键
        :type primary: bool
        :param partition_col: 是否对字段进行分割
        :type partition_col: bool
        """
        
        

        self._comment = None
        self._column_name = None
        self._column_type = None
        self._seq_number = None
        self._primary = None
        self._partition_col = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if column_name is not None:
            self.column_name = column_name
        if column_type is not None:
            self.column_type = column_type
        if seq_number is not None:
            self.seq_number = seq_number
        if primary is not None:
            self.primary = primary
        if partition_col is not None:
            self.partition_col = partition_col

    @property
    def comment(self):
        """Gets the comment of this ColumnsList.

        字段注解

        :return: The comment of this ColumnsList.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ColumnsList.

        字段注解

        :param comment: The comment of this ColumnsList.
        :type comment: str
        """
        self._comment = comment

    @property
    def column_name(self):
        """Gets the column_name of this ColumnsList.

        字段名称

        :return: The column_name of this ColumnsList.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ColumnsList.

        字段名称

        :param column_name: The column_name of this ColumnsList.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_type(self):
        """Gets the column_type of this ColumnsList.

        字段类型

        :return: The column_type of this ColumnsList.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        """Sets the column_type of this ColumnsList.

        字段类型

        :param column_type: The column_type of this ColumnsList.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def seq_number(self):
        """Gets the seq_number of this ColumnsList.

        字段的顺序

        :return: The seq_number of this ColumnsList.
        :rtype: int
        """
        return self._seq_number

    @seq_number.setter
    def seq_number(self, seq_number):
        """Sets the seq_number of this ColumnsList.

        字段的顺序

        :param seq_number: The seq_number of this ColumnsList.
        :type seq_number: int
        """
        self._seq_number = seq_number

    @property
    def primary(self):
        """Gets the primary of this ColumnsList.

        字段是否为主键

        :return: The primary of this ColumnsList.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this ColumnsList.

        字段是否为主键

        :param primary: The primary of this ColumnsList.
        :type primary: bool
        """
        self._primary = primary

    @property
    def partition_col(self):
        """Gets the partition_col of this ColumnsList.

        是否对字段进行分割

        :return: The partition_col of this ColumnsList.
        :rtype: bool
        """
        return self._partition_col

    @partition_col.setter
    def partition_col(self, partition_col):
        """Sets the partition_col of this ColumnsList.

        是否对字段进行分割

        :param partition_col: The partition_col of this ColumnsList.
        :type partition_col: bool
        """
        self._partition_col = partition_col

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
        if not isinstance(other, ColumnsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
