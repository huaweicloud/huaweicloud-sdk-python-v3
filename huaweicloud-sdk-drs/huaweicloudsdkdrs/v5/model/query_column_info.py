# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryColumnInfo:

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
        'primary_key_or_unique_index': 'str',
        'column_mapped_name': 'str',
        'is_filtered': 'bool',
        'is_partition_key': 'bool'
    }

    attribute_map = {
        'column_name': 'column_name',
        'column_type': 'column_type',
        'primary_key_or_unique_index': 'primary_key_or_unique_index',
        'column_mapped_name': 'column_mapped_name',
        'is_filtered': 'is_filtered',
        'is_partition_key': 'is_partition_key'
    }

    def __init__(self, column_name=None, column_type=None, primary_key_or_unique_index=None, column_mapped_name=None, is_filtered=None, is_partition_key=None):
        r"""QueryColumnInfo

        The model defined in huaweicloud sdk

        :param column_name: 列名
        :type column_name: str
        :param column_type: 列类型
        :type column_type: str
        :param primary_key_or_unique_index: 主键或者唯一索引
        :type primary_key_or_unique_index: str
        :param column_mapped_name: 列映射后的名称
        :type column_mapped_name: str
        :param is_filtered: 该列是否过滤
        :type is_filtered: bool
        :param is_partition_key: 该列是否partitionKey
        :type is_partition_key: bool
        """
        
        

        self._column_name = None
        self._column_type = None
        self._primary_key_or_unique_index = None
        self._column_mapped_name = None
        self._is_filtered = None
        self._is_partition_key = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if column_type is not None:
            self.column_type = column_type
        if primary_key_or_unique_index is not None:
            self.primary_key_or_unique_index = primary_key_or_unique_index
        if column_mapped_name is not None:
            self.column_mapped_name = column_mapped_name
        if is_filtered is not None:
            self.is_filtered = is_filtered
        if is_partition_key is not None:
            self.is_partition_key = is_partition_key

    @property
    def column_name(self):
        r"""Gets the column_name of this QueryColumnInfo.

        列名

        :return: The column_name of this QueryColumnInfo.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this QueryColumnInfo.

        列名

        :param column_name: The column_name of this QueryColumnInfo.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_type(self):
        r"""Gets the column_type of this QueryColumnInfo.

        列类型

        :return: The column_type of this QueryColumnInfo.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        r"""Sets the column_type of this QueryColumnInfo.

        列类型

        :param column_type: The column_type of this QueryColumnInfo.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def primary_key_or_unique_index(self):
        r"""Gets the primary_key_or_unique_index of this QueryColumnInfo.

        主键或者唯一索引

        :return: The primary_key_or_unique_index of this QueryColumnInfo.
        :rtype: str
        """
        return self._primary_key_or_unique_index

    @primary_key_or_unique_index.setter
    def primary_key_or_unique_index(self, primary_key_or_unique_index):
        r"""Sets the primary_key_or_unique_index of this QueryColumnInfo.

        主键或者唯一索引

        :param primary_key_or_unique_index: The primary_key_or_unique_index of this QueryColumnInfo.
        :type primary_key_or_unique_index: str
        """
        self._primary_key_or_unique_index = primary_key_or_unique_index

    @property
    def column_mapped_name(self):
        r"""Gets the column_mapped_name of this QueryColumnInfo.

        列映射后的名称

        :return: The column_mapped_name of this QueryColumnInfo.
        :rtype: str
        """
        return self._column_mapped_name

    @column_mapped_name.setter
    def column_mapped_name(self, column_mapped_name):
        r"""Sets the column_mapped_name of this QueryColumnInfo.

        列映射后的名称

        :param column_mapped_name: The column_mapped_name of this QueryColumnInfo.
        :type column_mapped_name: str
        """
        self._column_mapped_name = column_mapped_name

    @property
    def is_filtered(self):
        r"""Gets the is_filtered of this QueryColumnInfo.

        该列是否过滤

        :return: The is_filtered of this QueryColumnInfo.
        :rtype: bool
        """
        return self._is_filtered

    @is_filtered.setter
    def is_filtered(self, is_filtered):
        r"""Sets the is_filtered of this QueryColumnInfo.

        该列是否过滤

        :param is_filtered: The is_filtered of this QueryColumnInfo.
        :type is_filtered: bool
        """
        self._is_filtered = is_filtered

    @property
    def is_partition_key(self):
        r"""Gets the is_partition_key of this QueryColumnInfo.

        该列是否partitionKey

        :return: The is_partition_key of this QueryColumnInfo.
        :rtype: bool
        """
        return self._is_partition_key

    @is_partition_key.setter
    def is_partition_key(self, is_partition_key):
        r"""Sets the is_partition_key of this QueryColumnInfo.

        该列是否partitionKey

        :param is_partition_key: The is_partition_key of this QueryColumnInfo.
        :type is_partition_key: bool
        """
        self._is_partition_key = is_partition_key

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
        if not isinstance(other, QueryColumnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
