# coding: utf-8

import six

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
        'field_name': 'str',
        'field_type': 'str',
        'field_length': 'str',
        'null_able': 'str',
        'is_partition': 'bool',
        'primary': 'str',
        'unique': 'str',
        'decimal_digits': 'str'
    }

    attribute_map = {
        'field_name': 'field_name',
        'field_type': 'field_type',
        'field_length': 'field_length',
        'null_able': 'null_able',
        'is_partition': 'is_partition',
        'primary': 'primary',
        'unique': 'unique',
        'decimal_digits': 'decimal_digits'
    }

    def __init__(self, field_name=None, field_type=None, field_length=None, null_able=None, is_partition=None, primary=None, unique=None, decimal_digits=None):
        """ColumnInfo

        The model defined in huaweicloud sdk

        :param field_name: 字段名称
        :type field_name: str
        :param field_type: 字段类型
        :type field_type: str
        :param field_length: 字段长度
        :type field_length: str
        :param null_able: 是否允许为空
        :type null_able: str
        :param is_partition: 是否是分区字段
        :type is_partition: bool
        :param primary: 是否是主键字段
        :type primary: str
        :param unique: 是否是唯一键字段
        :type unique: str
        :param decimal_digits: 小数部分位数，非数字类型返回null
        :type decimal_digits: str
        """
        
        

        self._field_name = None
        self._field_type = None
        self._field_length = None
        self._null_able = None
        self._is_partition = None
        self._primary = None
        self._unique = None
        self._decimal_digits = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if field_type is not None:
            self.field_type = field_type
        if field_length is not None:
            self.field_length = field_length
        if null_able is not None:
            self.null_able = null_able
        if is_partition is not None:
            self.is_partition = is_partition
        if primary is not None:
            self.primary = primary
        if unique is not None:
            self.unique = unique
        if decimal_digits is not None:
            self.decimal_digits = decimal_digits

    @property
    def field_name(self):
        """Gets the field_name of this ColumnInfo.

        字段名称

        :return: The field_name of this ColumnInfo.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this ColumnInfo.

        字段名称

        :param field_name: The field_name of this ColumnInfo.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def field_type(self):
        """Gets the field_type of this ColumnInfo.

        字段类型

        :return: The field_type of this ColumnInfo.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this ColumnInfo.

        字段类型

        :param field_type: The field_type of this ColumnInfo.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def field_length(self):
        """Gets the field_length of this ColumnInfo.

        字段长度

        :return: The field_length of this ColumnInfo.
        :rtype: str
        """
        return self._field_length

    @field_length.setter
    def field_length(self, field_length):
        """Sets the field_length of this ColumnInfo.

        字段长度

        :param field_length: The field_length of this ColumnInfo.
        :type field_length: str
        """
        self._field_length = field_length

    @property
    def null_able(self):
        """Gets the null_able of this ColumnInfo.

        是否允许为空

        :return: The null_able of this ColumnInfo.
        :rtype: str
        """
        return self._null_able

    @null_able.setter
    def null_able(self, null_able):
        """Sets the null_able of this ColumnInfo.

        是否允许为空

        :param null_able: The null_able of this ColumnInfo.
        :type null_able: str
        """
        self._null_able = null_able

    @property
    def is_partition(self):
        """Gets the is_partition of this ColumnInfo.

        是否是分区字段

        :return: The is_partition of this ColumnInfo.
        :rtype: bool
        """
        return self._is_partition

    @is_partition.setter
    def is_partition(self, is_partition):
        """Sets the is_partition of this ColumnInfo.

        是否是分区字段

        :param is_partition: The is_partition of this ColumnInfo.
        :type is_partition: bool
        """
        self._is_partition = is_partition

    @property
    def primary(self):
        """Gets the primary of this ColumnInfo.

        是否是主键字段

        :return: The primary of this ColumnInfo.
        :rtype: str
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this ColumnInfo.

        是否是主键字段

        :param primary: The primary of this ColumnInfo.
        :type primary: str
        """
        self._primary = primary

    @property
    def unique(self):
        """Gets the unique of this ColumnInfo.

        是否是唯一键字段

        :return: The unique of this ColumnInfo.
        :rtype: str
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this ColumnInfo.

        是否是唯一键字段

        :param unique: The unique of this ColumnInfo.
        :type unique: str
        """
        self._unique = unique

    @property
    def decimal_digits(self):
        """Gets the decimal_digits of this ColumnInfo.

        小数部分位数，非数字类型返回null

        :return: The decimal_digits of this ColumnInfo.
        :rtype: str
        """
        return self._decimal_digits

    @decimal_digits.setter
    def decimal_digits(self, decimal_digits):
        """Sets the decimal_digits of this ColumnInfo.

        小数部分位数，非数字类型返回null

        :param decimal_digits: The decimal_digits of this ColumnInfo.
        :type decimal_digits: str
        """
        self._decimal_digits = decimal_digits

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
        if not isinstance(other, ColumnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
