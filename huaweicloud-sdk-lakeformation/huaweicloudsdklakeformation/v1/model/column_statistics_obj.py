# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnStatisticsObj:

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
        'data_type': 'str',
        'binary_statistics_data': 'BinaryColumnStatisticsData',
        'long_statistics_data': 'LongColumnStatisticsData',
        'decimal_statistics_data': 'DecimalColumnStatisticsData',
        'string_statistics_data': 'StringColumnStatisticsData',
        'double_statistics_data': 'DoubleColumnStatisticsData',
        'date_statistics_data': 'DateColumnStatisticsData',
        'boolean_statistics_data': 'BooleanColumnStatisticsData'
    }

    attribute_map = {
        'column_name': 'column_name',
        'column_type': 'column_type',
        'data_type': 'data_type',
        'binary_statistics_data': 'binary_statistics_data',
        'long_statistics_data': 'long_statistics_data',
        'decimal_statistics_data': 'decimal_statistics_data',
        'string_statistics_data': 'string_statistics_data',
        'double_statistics_data': 'double_statistics_data',
        'date_statistics_data': 'date_statistics_data',
        'boolean_statistics_data': 'boolean_statistics_data'
    }

    def __init__(self, column_name=None, column_type=None, data_type=None, binary_statistics_data=None, long_statistics_data=None, decimal_statistics_data=None, string_statistics_data=None, double_statistics_data=None, date_statistics_data=None, boolean_statistics_data=None):
        """ColumnStatisticsObj

        The model defined in huaweicloud sdk

        :param column_name: 数据列名
        :type column_name: str
        :param column_type: 数据类型，字段类型包括array bigint binary boolean char date decimal double float int interval map set smallint string struct timestamp tinyint union varchar
        :type column_type: str
        :param data_type: 统计信息类型
        :type data_type: str
        :param binary_statistics_data: 
        :type binary_statistics_data: :class:`huaweicloudsdklakeformation.v1.BinaryColumnStatisticsData`
        :param long_statistics_data: 
        :type long_statistics_data: :class:`huaweicloudsdklakeformation.v1.LongColumnStatisticsData`
        :param decimal_statistics_data: 
        :type decimal_statistics_data: :class:`huaweicloudsdklakeformation.v1.DecimalColumnStatisticsData`
        :param string_statistics_data: 
        :type string_statistics_data: :class:`huaweicloudsdklakeformation.v1.StringColumnStatisticsData`
        :param double_statistics_data: 
        :type double_statistics_data: :class:`huaweicloudsdklakeformation.v1.DoubleColumnStatisticsData`
        :param date_statistics_data: 
        :type date_statistics_data: :class:`huaweicloudsdklakeformation.v1.DateColumnStatisticsData`
        :param boolean_statistics_data: 
        :type boolean_statistics_data: :class:`huaweicloudsdklakeformation.v1.BooleanColumnStatisticsData`
        """
        
        

        self._column_name = None
        self._column_type = None
        self._data_type = None
        self._binary_statistics_data = None
        self._long_statistics_data = None
        self._decimal_statistics_data = None
        self._string_statistics_data = None
        self._double_statistics_data = None
        self._date_statistics_data = None
        self._boolean_statistics_data = None
        self.discriminator = None

        self.column_name = column_name
        self.column_type = column_type
        self.data_type = data_type
        if binary_statistics_data is not None:
            self.binary_statistics_data = binary_statistics_data
        if long_statistics_data is not None:
            self.long_statistics_data = long_statistics_data
        if decimal_statistics_data is not None:
            self.decimal_statistics_data = decimal_statistics_data
        if string_statistics_data is not None:
            self.string_statistics_data = string_statistics_data
        if double_statistics_data is not None:
            self.double_statistics_data = double_statistics_data
        if date_statistics_data is not None:
            self.date_statistics_data = date_statistics_data
        if boolean_statistics_data is not None:
            self.boolean_statistics_data = boolean_statistics_data

    @property
    def column_name(self):
        """Gets the column_name of this ColumnStatisticsObj.

        数据列名

        :return: The column_name of this ColumnStatisticsObj.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ColumnStatisticsObj.

        数据列名

        :param column_name: The column_name of this ColumnStatisticsObj.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_type(self):
        """Gets the column_type of this ColumnStatisticsObj.

        数据类型，字段类型包括array bigint binary boolean char date decimal double float int interval map set smallint string struct timestamp tinyint union varchar

        :return: The column_type of this ColumnStatisticsObj.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        """Sets the column_type of this ColumnStatisticsObj.

        数据类型，字段类型包括array bigint binary boolean char date decimal double float int interval map set smallint string struct timestamp tinyint union varchar

        :param column_type: The column_type of this ColumnStatisticsObj.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def data_type(self):
        """Gets the data_type of this ColumnStatisticsObj.

        统计信息类型

        :return: The data_type of this ColumnStatisticsObj.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ColumnStatisticsObj.

        统计信息类型

        :param data_type: The data_type of this ColumnStatisticsObj.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def binary_statistics_data(self):
        """Gets the binary_statistics_data of this ColumnStatisticsObj.

        :return: The binary_statistics_data of this ColumnStatisticsObj.
        :rtype: :class:`huaweicloudsdklakeformation.v1.BinaryColumnStatisticsData`
        """
        return self._binary_statistics_data

    @binary_statistics_data.setter
    def binary_statistics_data(self, binary_statistics_data):
        """Sets the binary_statistics_data of this ColumnStatisticsObj.

        :param binary_statistics_data: The binary_statistics_data of this ColumnStatisticsObj.
        :type binary_statistics_data: :class:`huaweicloudsdklakeformation.v1.BinaryColumnStatisticsData`
        """
        self._binary_statistics_data = binary_statistics_data

    @property
    def long_statistics_data(self):
        """Gets the long_statistics_data of this ColumnStatisticsObj.

        :return: The long_statistics_data of this ColumnStatisticsObj.
        :rtype: :class:`huaweicloudsdklakeformation.v1.LongColumnStatisticsData`
        """
        return self._long_statistics_data

    @long_statistics_data.setter
    def long_statistics_data(self, long_statistics_data):
        """Sets the long_statistics_data of this ColumnStatisticsObj.

        :param long_statistics_data: The long_statistics_data of this ColumnStatisticsObj.
        :type long_statistics_data: :class:`huaweicloudsdklakeformation.v1.LongColumnStatisticsData`
        """
        self._long_statistics_data = long_statistics_data

    @property
    def decimal_statistics_data(self):
        """Gets the decimal_statistics_data of this ColumnStatisticsObj.

        :return: The decimal_statistics_data of this ColumnStatisticsObj.
        :rtype: :class:`huaweicloudsdklakeformation.v1.DecimalColumnStatisticsData`
        """
        return self._decimal_statistics_data

    @decimal_statistics_data.setter
    def decimal_statistics_data(self, decimal_statistics_data):
        """Sets the decimal_statistics_data of this ColumnStatisticsObj.

        :param decimal_statistics_data: The decimal_statistics_data of this ColumnStatisticsObj.
        :type decimal_statistics_data: :class:`huaweicloudsdklakeformation.v1.DecimalColumnStatisticsData`
        """
        self._decimal_statistics_data = decimal_statistics_data

    @property
    def string_statistics_data(self):
        """Gets the string_statistics_data of this ColumnStatisticsObj.

        :return: The string_statistics_data of this ColumnStatisticsObj.
        :rtype: :class:`huaweicloudsdklakeformation.v1.StringColumnStatisticsData`
        """
        return self._string_statistics_data

    @string_statistics_data.setter
    def string_statistics_data(self, string_statistics_data):
        """Sets the string_statistics_data of this ColumnStatisticsObj.

        :param string_statistics_data: The string_statistics_data of this ColumnStatisticsObj.
        :type string_statistics_data: :class:`huaweicloudsdklakeformation.v1.StringColumnStatisticsData`
        """
        self._string_statistics_data = string_statistics_data

    @property
    def double_statistics_data(self):
        """Gets the double_statistics_data of this ColumnStatisticsObj.

        :return: The double_statistics_data of this ColumnStatisticsObj.
        :rtype: :class:`huaweicloudsdklakeformation.v1.DoubleColumnStatisticsData`
        """
        return self._double_statistics_data

    @double_statistics_data.setter
    def double_statistics_data(self, double_statistics_data):
        """Sets the double_statistics_data of this ColumnStatisticsObj.

        :param double_statistics_data: The double_statistics_data of this ColumnStatisticsObj.
        :type double_statistics_data: :class:`huaweicloudsdklakeformation.v1.DoubleColumnStatisticsData`
        """
        self._double_statistics_data = double_statistics_data

    @property
    def date_statistics_data(self):
        """Gets the date_statistics_data of this ColumnStatisticsObj.

        :return: The date_statistics_data of this ColumnStatisticsObj.
        :rtype: :class:`huaweicloudsdklakeformation.v1.DateColumnStatisticsData`
        """
        return self._date_statistics_data

    @date_statistics_data.setter
    def date_statistics_data(self, date_statistics_data):
        """Sets the date_statistics_data of this ColumnStatisticsObj.

        :param date_statistics_data: The date_statistics_data of this ColumnStatisticsObj.
        :type date_statistics_data: :class:`huaweicloudsdklakeformation.v1.DateColumnStatisticsData`
        """
        self._date_statistics_data = date_statistics_data

    @property
    def boolean_statistics_data(self):
        """Gets the boolean_statistics_data of this ColumnStatisticsObj.

        :return: The boolean_statistics_data of this ColumnStatisticsObj.
        :rtype: :class:`huaweicloudsdklakeformation.v1.BooleanColumnStatisticsData`
        """
        return self._boolean_statistics_data

    @boolean_statistics_data.setter
    def boolean_statistics_data(self, boolean_statistics_data):
        """Sets the boolean_statistics_data of this ColumnStatisticsObj.

        :param boolean_statistics_data: The boolean_statistics_data of this ColumnStatisticsObj.
        :type boolean_statistics_data: :class:`huaweicloudsdklakeformation.v1.BooleanColumnStatisticsData`
        """
        self._boolean_statistics_data = boolean_statistics_data

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
        if not isinstance(other, ColumnStatisticsObj):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
