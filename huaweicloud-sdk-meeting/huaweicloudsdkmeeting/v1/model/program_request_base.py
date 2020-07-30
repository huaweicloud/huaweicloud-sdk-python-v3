# coding: utf-8

import pprint
import re

import six





class ProgramRequestBase:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'program_name': 'str'
    }

    attribute_map = {
        'program_name': 'programName'
    }

    def __init__(self, program_name=None):
        """ProgramRequestBase - a model defined in huaweicloud sdk"""
        
        

        self._program_name = None
        self.discriminator = None

        if program_name is not None:
            self.program_name = program_name

    @property
    def program_name(self):
        """Gets the program_name of this ProgramRequestBase.

        节目名称

        :return: The program_name of this ProgramRequestBase.
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        """Sets the program_name of this ProgramRequestBase.

        节目名称

        :param program_name: The program_name of this ProgramRequestBase.
        :type: str
        """
        self._program_name = program_name

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
        if not isinstance(other, ProgramRequestBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
