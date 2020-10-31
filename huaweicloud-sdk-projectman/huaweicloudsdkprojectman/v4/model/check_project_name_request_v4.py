# coding: utf-8

import pprint
import re

import six





class CheckProjectNameRequestV4:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_name': 'str'
    }

    attribute_map = {
        'project_name': 'project_name'
    }

    def __init__(self, project_name=None):
        """CheckProjectNameRequestV4 - a model defined in huaweicloud sdk"""
        
        

        self._project_name = None
        self.discriminator = None

        self.project_name = project_name

    @property
    def project_name(self):
        """Gets the project_name of this CheckProjectNameRequestV4.

        项目名

        :return: The project_name of this CheckProjectNameRequestV4.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CheckProjectNameRequestV4.

        项目名

        :param project_name: The project_name of this CheckProjectNameRequestV4.
        :type: str
        """
        self._project_name = project_name

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
        if not isinstance(other, CheckProjectNameRequestV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
