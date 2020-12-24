# coding: utf-8

import pprint
import re

import six





class RestoreDatabasesInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'database': 'str',
        'tables': 'list[RestoreTableInfo]'
    }

    attribute_map = {
        'database': 'database',
        'tables': 'tables'
    }

    def __init__(self, database=None, tables=None):
        """RestoreDatabasesInfo - a model defined in huaweicloud sdk"""
        
        

        self._database = None
        self._tables = None
        self.discriminator = None

        self.database = database
        self.tables = tables

    @property
    def database(self):
        """Gets the database of this RestoreDatabasesInfo.

        库名

        :return: The database of this RestoreDatabasesInfo.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this RestoreDatabasesInfo.

        库名

        :param database: The database of this RestoreDatabasesInfo.
        :type: str
        """
        self._database = database

    @property
    def tables(self):
        """Gets the tables of this RestoreDatabasesInfo.

        表信息

        :return: The tables of this RestoreDatabasesInfo.
        :rtype: list[RestoreTableInfo]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this RestoreDatabasesInfo.

        表信息

        :param tables: The tables of this RestoreDatabasesInfo.
        :type: list[RestoreTableInfo]
        """
        self._tables = tables

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
        if not isinstance(other, RestoreDatabasesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
