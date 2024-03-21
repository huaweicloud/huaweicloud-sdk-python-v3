# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableColumnDTO:

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
        'description': 'str',
        'type': 'str',
        'is_partition_column': 'bool'
    }

    attribute_map = {
        'column_name': 'column_name',
        'description': 'description',
        'type': 'type',
        'is_partition_column': 'is_partition_column'
    }

    def __init__(self, column_name=None, description=None, type=None, is_partition_column=None):
        """TableColumnDTO

        The model defined in huaweicloud sdk

        :param column_name: 字段名称
        :type column_name: str
        :param description: 字段描述
        :type description: str
        :param type: 字段类型
        :type type: str
        :param is_partition_column: 是否是分区字段
        :type is_partition_column: bool
        """
        
        

        self._column_name = None
        self._description = None
        self._type = None
        self._is_partition_column = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if is_partition_column is not None:
            self.is_partition_column = is_partition_column

    @property
    def column_name(self):
        """Gets the column_name of this TableColumnDTO.

        字段名称

        :return: The column_name of this TableColumnDTO.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this TableColumnDTO.

        字段名称

        :param column_name: The column_name of this TableColumnDTO.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def description(self):
        """Gets the description of this TableColumnDTO.

        字段描述

        :return: The description of this TableColumnDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TableColumnDTO.

        字段描述

        :param description: The description of this TableColumnDTO.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this TableColumnDTO.

        字段类型

        :return: The type of this TableColumnDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TableColumnDTO.

        字段类型

        :param type: The type of this TableColumnDTO.
        :type type: str
        """
        self._type = type

    @property
    def is_partition_column(self):
        """Gets the is_partition_column of this TableColumnDTO.

        是否是分区字段

        :return: The is_partition_column of this TableColumnDTO.
        :rtype: bool
        """
        return self._is_partition_column

    @is_partition_column.setter
    def is_partition_column(self, is_partition_column):
        """Sets the is_partition_column of this TableColumnDTO.

        是否是分区字段

        :param is_partition_column: The is_partition_column of this TableColumnDTO.
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
        if not isinstance(other, TableColumnDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
