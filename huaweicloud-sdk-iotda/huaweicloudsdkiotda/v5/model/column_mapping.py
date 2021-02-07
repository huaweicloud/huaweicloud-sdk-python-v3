# coding: utf-8

import pprint
import re

import six





class ColumnMapping:


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
        'json_key': 'str'
    }

    attribute_map = {
        'column_name': 'column_name',
        'json_key': 'json_key'
    }

    def __init__(self, column_name=None, json_key=None):
        """ColumnMapping - a model defined in huaweicloud sdk"""
        
        

        self._column_name = None
        self._json_key = None
        self.discriminator = None

        self.column_name = column_name
        self.json_key = json_key

    @property
    def column_name(self):
        """Gets the column_name of this ColumnMapping.

        数据库的列名

        :return: The column_name of this ColumnMapping.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ColumnMapping.

        数据库的列名

        :param column_name: The column_name of this ColumnMapping.
        :type: str
        """
        self._column_name = column_name

    @property
    def json_key(self):
        """Gets the json_key of this ColumnMapping.

        流转数据的属性名

        :return: The json_key of this ColumnMapping.
        :rtype: str
        """
        return self._json_key

    @json_key.setter
    def json_key(self, json_key):
        """Sets the json_key of this ColumnMapping.

        流转数据的属性名

        :param json_key: The json_key of this ColumnMapping.
        :type: str
        """
        self._json_key = json_key

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ColumnMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
