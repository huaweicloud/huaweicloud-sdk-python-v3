# coding: utf-8

import pprint
import re

import six





class DeleteApplicationRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'application_urn': 'str'
    }

    attribute_map = {
        'application_urn': 'application_urn'
    }

    def __init__(self, application_urn=None):
        """DeleteApplicationRequest - a model defined in huaweicloud sdk"""
        
        

        self._application_urn = None
        self.discriminator = None

        self.application_urn = application_urn

    @property
    def application_urn(self):
        """Gets the application_urn of this DeleteApplicationRequest.


        :return: The application_urn of this DeleteApplicationRequest.
        :rtype: str
        """
        return self._application_urn

    @application_urn.setter
    def application_urn(self, application_urn):
        """Sets the application_urn of this DeleteApplicationRequest.


        :param application_urn: The application_urn of this DeleteApplicationRequest.
        :type: str
        """
        self._application_urn = application_urn

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
        if not isinstance(other, DeleteApplicationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
