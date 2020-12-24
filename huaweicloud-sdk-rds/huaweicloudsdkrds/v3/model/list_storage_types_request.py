# coding: utf-8

import pprint
import re

import six





class ListStorageTypesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'database_name': 'str',
        'version_name': 'str',
        'ha_mode': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'database_name': 'database_name',
        'version_name': 'version_name',
        'ha_mode': 'ha_mode'
    }

    def __init__(self, x_language=None, database_name=None, version_name=None, ha_mode=None):
        """ListStorageTypesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._database_name = None
        self._version_name = None
        self._ha_mode = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.database_name = database_name
        self.version_name = version_name
        if ha_mode is not None:
            self.ha_mode = ha_mode

    @property
    def x_language(self):
        """Gets the x_language of this ListStorageTypesRequest.


        :return: The x_language of this ListStorageTypesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListStorageTypesRequest.


        :param x_language: The x_language of this ListStorageTypesRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def database_name(self):
        """Gets the database_name of this ListStorageTypesRequest.


        :return: The database_name of this ListStorageTypesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListStorageTypesRequest.


        :param database_name: The database_name of this ListStorageTypesRequest.
        :type: str
        """
        self._database_name = database_name

    @property
    def version_name(self):
        """Gets the version_name of this ListStorageTypesRequest.


        :return: The version_name of this ListStorageTypesRequest.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this ListStorageTypesRequest.


        :param version_name: The version_name of this ListStorageTypesRequest.
        :type: str
        """
        self._version_name = version_name

    @property
    def ha_mode(self):
        """Gets the ha_mode of this ListStorageTypesRequest.


        :return: The ha_mode of this ListStorageTypesRequest.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        """Sets the ha_mode of this ListStorageTypesRequest.


        :param ha_mode: The ha_mode of this ListStorageTypesRequest.
        :type: str
        """
        self._ha_mode = ha_mode

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
        if not isinstance(other, ListStorageTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
