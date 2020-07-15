# coding: utf-8

import pprint
import re

import six





class ListInstancesDatastoreResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, type=None, version=None):
        """ListInstancesDatastoreResult - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._version = None
        self.discriminator = None

        self.type = type
        self.version = version

    @property
    def type(self):
        """Gets the type of this ListInstancesDatastoreResult.

        数据库引擎。

        :return: The type of this ListInstancesDatastoreResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListInstancesDatastoreResult.

        数据库引擎。

        :param type: The type of this ListInstancesDatastoreResult.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ListInstancesDatastoreResult.

        数据库版本号。

        :return: The version of this ListInstancesDatastoreResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListInstancesDatastoreResult.

        数据库版本号。

        :param version: The version of this ListInstancesDatastoreResult.
        :type: str
        """
        self._version = version

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
        if not isinstance(other, ListInstancesDatastoreResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
