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
        'column_type': 'str',
        'key_type': 'str',
        'column_mapped_name': 'str',
        'status': 'bool',
        'partition': 'bool'
    }

    attribute_map = {
        'column_name': 'column_name',
        'column_type': 'column_type',
        'key_type': 'key_type',
        'column_mapped_name': 'column_mapped_name',
        'status': 'status',
        'partition': 'partition'
    }

    def __init__(self, column_name=None, column_type=None, key_type=None, column_mapped_name=None, status=None, partition=None):
        r"""ColumnInfo

        The model defined in huaweicloud sdk

        :param column_name: 列名
        :type column_name: str
        :param column_type: 列类型
        :type column_type: str
        :param key_type: 列的键类型。
        :type key_type: str
        :param column_mapped_name: 列映射后的名称
        :type column_mapped_name: str
        :param status: 该列是否过滤
        :type status: bool
        :param partition: 该列是否partitionKey
        :type partition: bool
        """
        
        

        self._column_name = None
        self._column_type = None
        self._key_type = None
        self._column_mapped_name = None
        self._status = None
        self._partition = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if column_type is not None:
            self.column_type = column_type
        if key_type is not None:
            self.key_type = key_type
        if column_mapped_name is not None:
            self.column_mapped_name = column_mapped_name
        if status is not None:
            self.status = status
        if partition is not None:
            self.partition = partition

    @property
    def column_name(self):
        r"""Gets the column_name of this ColumnInfo.

        列名

        :return: The column_name of this ColumnInfo.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this ColumnInfo.

        列名

        :param column_name: The column_name of this ColumnInfo.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_type(self):
        r"""Gets the column_type of this ColumnInfo.

        列类型

        :return: The column_type of this ColumnInfo.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        r"""Sets the column_type of this ColumnInfo.

        列类型

        :param column_type: The column_type of this ColumnInfo.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def key_type(self):
        r"""Gets the key_type of this ColumnInfo.

        列的键类型。

        :return: The key_type of this ColumnInfo.
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        r"""Sets the key_type of this ColumnInfo.

        列的键类型。

        :param key_type: The key_type of this ColumnInfo.
        :type key_type: str
        """
        self._key_type = key_type

    @property
    def column_mapped_name(self):
        r"""Gets the column_mapped_name of this ColumnInfo.

        列映射后的名称

        :return: The column_mapped_name of this ColumnInfo.
        :rtype: str
        """
        return self._column_mapped_name

    @column_mapped_name.setter
    def column_mapped_name(self, column_mapped_name):
        r"""Sets the column_mapped_name of this ColumnInfo.

        列映射后的名称

        :param column_mapped_name: The column_mapped_name of this ColumnInfo.
        :type column_mapped_name: str
        """
        self._column_mapped_name = column_mapped_name

    @property
    def status(self):
        r"""Gets the status of this ColumnInfo.

        该列是否过滤

        :return: The status of this ColumnInfo.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ColumnInfo.

        该列是否过滤

        :param status: The status of this ColumnInfo.
        :type status: bool
        """
        self._status = status

    @property
    def partition(self):
        r"""Gets the partition of this ColumnInfo.

        该列是否partitionKey

        :return: The partition of this ColumnInfo.
        :rtype: bool
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this ColumnInfo.

        该列是否partitionKey

        :param partition: The partition of this ColumnInfo.
        :type partition: bool
        """
        self._partition = partition

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
