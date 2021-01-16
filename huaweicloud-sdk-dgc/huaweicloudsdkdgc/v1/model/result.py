# coding: utf-8

import pprint
import re

import six





class Result:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'row_count': 'int',
        'rows': 'str',
        'schema': 'str'
    }

    attribute_map = {
        'message': 'message',
        'row_count': 'rowCount',
        'rows': 'rows',
        'schema': 'schema'
    }

    def __init__(self, message=None, row_count=None, rows=None, schema=None):
        """Result - a model defined in huaweicloud sdk"""
        
        

        self._message = None
        self._row_count = None
        self._rows = None
        self._schema = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if row_count is not None:
            self.row_count = row_count
        if rows is not None:
            self.rows = rows
        if schema is not None:
            self.schema = schema

    @property
    def message(self):
        """Gets the message of this Result.


        :return: The message of this Result.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Result.


        :param message: The message of this Result.
        :type: str
        """
        self._message = message

    @property
    def row_count(self):
        """Gets the row_count of this Result.


        :return: The row_count of this Result.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this Result.


        :param row_count: The row_count of this Result.
        :type: int
        """
        self._row_count = row_count

    @property
    def rows(self):
        """Gets the rows of this Result.


        :return: The rows of this Result.
        :rtype: str
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this Result.


        :param rows: The rows of this Result.
        :type: str
        """
        self._rows = rows

    @property
    def schema(self):
        """Gets the schema of this Result.


        :return: The schema of this Result.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this Result.


        :param schema: The schema of this Result.
        :type: str
        """
        self._schema = schema

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
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
