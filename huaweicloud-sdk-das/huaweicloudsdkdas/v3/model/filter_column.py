# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FilterColumn:

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
        'column_value': 'str'
    }

    attribute_map = {
        'column_name': 'column_name',
        'column_value': 'column_value'
    }

    def __init__(self, column_name=None, column_value=None):
        r"""FilterColumn

        The model defined in huaweicloud sdk

        :param column_name: 筛选条件字段名
        :type column_name: str
        :param column_value: 筛选条件值
        :type column_value: str
        """
        
        

        self._column_name = None
        self._column_value = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if column_value is not None:
            self.column_value = column_value

    @property
    def column_name(self):
        r"""Gets the column_name of this FilterColumn.

        筛选条件字段名

        :return: The column_name of this FilterColumn.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this FilterColumn.

        筛选条件字段名

        :param column_name: The column_name of this FilterColumn.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_value(self):
        r"""Gets the column_value of this FilterColumn.

        筛选条件值

        :return: The column_value of this FilterColumn.
        :rtype: str
        """
        return self._column_value

    @column_value.setter
    def column_value(self, column_value):
        r"""Sets the column_value of this FilterColumn.

        筛选条件值

        :param column_value: The column_value of this FilterColumn.
        :type column_value: str
        """
        self._column_value = column_value

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
        if not isinstance(other, FilterColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
