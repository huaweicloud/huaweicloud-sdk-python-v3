# coding: utf-8

import pprint
import re

import six





class RestoreTableInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'old_name': 'str',
        'new_name': 'str'
    }

    attribute_map = {
        'old_name': 'oldName',
        'new_name': 'newName'
    }

    def __init__(self, old_name=None, new_name=None):
        """RestoreTableInfo - a model defined in huaweicloud sdk"""
        
        

        self._old_name = None
        self._new_name = None
        self.discriminator = None

        self.old_name = old_name
        self.new_name = new_name

    @property
    def old_name(self):
        """Gets the old_name of this RestoreTableInfo.

        旧表名

        :return: The old_name of this RestoreTableInfo.
        :rtype: str
        """
        return self._old_name

    @old_name.setter
    def old_name(self, old_name):
        """Sets the old_name of this RestoreTableInfo.

        旧表名

        :param old_name: The old_name of this RestoreTableInfo.
        :type: str
        """
        self._old_name = old_name

    @property
    def new_name(self):
        """Gets the new_name of this RestoreTableInfo.

        新表名

        :return: The new_name of this RestoreTableInfo.
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this RestoreTableInfo.

        新表名

        :param new_name: The new_name of this RestoreTableInfo.
        :type: str
        """
        self._new_name = new_name

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
        if not isinstance(other, RestoreTableInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
