# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddColumnInfo:

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
        'column_value': 'str',
        'data_type': 'str'
    }

    attribute_map = {
        'column_type': 'column_type',
        'column_name': 'column_name',
        'column_value': 'column_value',
        'data_type': 'data_type'
    }

    def __init__(self, column_type=None, column_name=None, column_value=None, data_type=None):
        r"""AddColumnInfo

        The model defined in huaweicloud sdk

        :param column_type: 列类型
        :type column_type: str
        :param column_name: 列名称
        :type column_name: str
        :param column_value: 列填充值
        :type column_value: str
        :param data_type: 填充列的数据类型
        :type data_type: str
        """
        
        

        self._column_type = None
        self._column_name = None
        self._column_value = None
        self._data_type = None
        self.discriminator = None

        if column_type is not None:
            self.column_type = column_type
        if column_name is not None:
            self.column_name = column_name
        if column_value is not None:
            self.column_value = column_value
        if data_type is not None:
            self.data_type = data_type

    @property
    def column_type(self):
        r"""Gets the column_type of this AddColumnInfo.

        列类型

        :return: The column_type of this AddColumnInfo.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        r"""Sets the column_type of this AddColumnInfo.

        列类型

        :param column_type: The column_type of this AddColumnInfo.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def column_name(self):
        r"""Gets the column_name of this AddColumnInfo.

        列名称

        :return: The column_name of this AddColumnInfo.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this AddColumnInfo.

        列名称

        :param column_name: The column_name of this AddColumnInfo.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_value(self):
        r"""Gets the column_value of this AddColumnInfo.

        列填充值

        :return: The column_value of this AddColumnInfo.
        :rtype: str
        """
        return self._column_value

    @column_value.setter
    def column_value(self, column_value):
        r"""Sets the column_value of this AddColumnInfo.

        列填充值

        :param column_value: The column_value of this AddColumnInfo.
        :type column_value: str
        """
        self._column_value = column_value

    @property
    def data_type(self):
        r"""Gets the data_type of this AddColumnInfo.

        填充列的数据类型

        :return: The data_type of this AddColumnInfo.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this AddColumnInfo.

        填充列的数据类型

        :param data_type: The data_type of this AddColumnInfo.
        :type data_type: str
        """
        self._data_type = data_type

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
        if not isinstance(other, AddColumnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
