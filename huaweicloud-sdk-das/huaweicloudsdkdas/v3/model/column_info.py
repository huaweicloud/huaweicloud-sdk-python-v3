# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnInfo:

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
        'data_type': 'str',
        'character_set_name': 'str',
        'primary_key': 'bool'
    }

    attribute_map = {
        'column_name': 'column_name',
        'data_type': 'data_type',
        'character_set_name': 'character_set_name',
        'primary_key': 'primary_key'
    }

    def __init__(self, column_name=None, data_type=None, character_set_name=None, primary_key=None):
        r"""ColumnInfo

        The model defined in huaweicloud sdk

        :param column_name: 列名称
        :type column_name: str
        :param data_type: 数据类型
        :type data_type: str
        :param character_set_name: 字符集名称
        :type character_set_name: str
        :param primary_key: 是否为主键
        :type primary_key: bool
        """
        
        

        self._column_name = None
        self._data_type = None
        self._character_set_name = None
        self._primary_key = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if data_type is not None:
            self.data_type = data_type
        if character_set_name is not None:
            self.character_set_name = character_set_name
        if primary_key is not None:
            self.primary_key = primary_key

    @property
    def column_name(self):
        r"""Gets the column_name of this ColumnInfo.

        列名称

        :return: The column_name of this ColumnInfo.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this ColumnInfo.

        列名称

        :param column_name: The column_name of this ColumnInfo.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def data_type(self):
        r"""Gets the data_type of this ColumnInfo.

        数据类型

        :return: The data_type of this ColumnInfo.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this ColumnInfo.

        数据类型

        :param data_type: The data_type of this ColumnInfo.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def character_set_name(self):
        r"""Gets the character_set_name of this ColumnInfo.

        字符集名称

        :return: The character_set_name of this ColumnInfo.
        :rtype: str
        """
        return self._character_set_name

    @character_set_name.setter
    def character_set_name(self, character_set_name):
        r"""Sets the character_set_name of this ColumnInfo.

        字符集名称

        :param character_set_name: The character_set_name of this ColumnInfo.
        :type character_set_name: str
        """
        self._character_set_name = character_set_name

    @property
    def primary_key(self):
        r"""Gets the primary_key of this ColumnInfo.

        是否为主键

        :return: The primary_key of this ColumnInfo.
        :rtype: bool
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        r"""Sets the primary_key of this ColumnInfo.

        是否为主键

        :param primary_key: The primary_key of this ColumnInfo.
        :type primary_key: bool
        """
        self._primary_key = primary_key

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
        if not isinstance(other, ColumnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
