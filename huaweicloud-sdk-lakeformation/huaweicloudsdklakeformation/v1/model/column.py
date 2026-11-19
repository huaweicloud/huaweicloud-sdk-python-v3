# coding: utf-8

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
        'column_type': 'str',
        'column_name': 'str',
        'comment': 'str',
        'advance_column_type': 'str'
    }

    attribute_map = {
        'column_type': 'column_type',
        'column_name': 'column_name',
        'comment': 'comment',
        'advance_column_type': 'advance_column_type'
    }

    def __init__(self, column_type=None, column_name=None, comment=None, advance_column_type=None):
        r"""Column

        The model defined in huaweicloud sdk

        :param column_type: 列类型，包括array bigint binary boolean char date decimal double float int interval map set smallint string struct timestamp tinyint union varchar
        :type column_type: str
        :param column_name: 列名
        :type column_name: str
        :param comment: 列描述信息
        :type comment: str
        :param advance_column_type: 用户自定义类型名称，当且仅当column_type为struct，字段可填写。该字段存在值时，表示用户自定义的高阶类型
        :type advance_column_type: str
        """
        
        

        self._column_type = None
        self._column_name = None
        self._comment = None
        self._advance_column_type = None
        self.discriminator = None

        self.column_type = column_type
        self.column_name = column_name
        if comment is not None:
            self.comment = comment
        if advance_column_type is not None:
            self.advance_column_type = advance_column_type

    @property
    def column_type(self):
        r"""Gets the column_type of this Column.

        列类型，包括array bigint binary boolean char date decimal double float int interval map set smallint string struct timestamp tinyint union varchar

        :return: The column_type of this Column.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        r"""Sets the column_type of this Column.

        列类型，包括array bigint binary boolean char date decimal double float int interval map set smallint string struct timestamp tinyint union varchar

        :param column_type: The column_type of this Column.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def column_name(self):
        r"""Gets the column_name of this Column.

        列名

        :return: The column_name of this Column.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this Column.

        列名

        :param column_name: The column_name of this Column.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def comment(self):
        r"""Gets the comment of this Column.

        列描述信息

        :return: The comment of this Column.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this Column.

        列描述信息

        :param comment: The comment of this Column.
        :type comment: str
        """
        self._comment = comment

    @property
    def advance_column_type(self):
        r"""Gets the advance_column_type of this Column.

        用户自定义类型名称，当且仅当column_type为struct，字段可填写。该字段存在值时，表示用户自定义的高阶类型

        :return: The advance_column_type of this Column.
        :rtype: str
        """
        return self._advance_column_type

    @advance_column_type.setter
    def advance_column_type(self, advance_column_type):
        r"""Sets the advance_column_type of this Column.

        用户自定义类型名称，当且仅当column_type为struct，字段可填写。该字段存在值时，表示用户自定义的高阶类型

        :param advance_column_type: The advance_column_type of this Column.
        :type advance_column_type: str
        """
        self._advance_column_type = advance_column_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
