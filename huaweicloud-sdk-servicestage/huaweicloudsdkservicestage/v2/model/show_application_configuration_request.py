# coding: utf-8

import pprint
import re

import six





class ShowApplicationConfigurationRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'environment_id': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'environment_id': 'environment_id'
    }

    def __init__(self, application_id=None, environment_id=None):
        """ShowApplicationConfigurationRequest - a model defined in huaweicloud sdk"""
        
        

        self._application_id = None
        self._environment_id = None
        self.discriminator = None

        self.application_id = application_id
        if environment_id is not None:
            self.environment_id = environment_id

    @property
    def application_id(self):
        """Gets the application_id of this ShowApplicationConfigurationRequest.


        :return: The application_id of this ShowApplicationConfigurationRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ShowApplicationConfigurationRequest.


        :param application_id: The application_id of this ShowApplicationConfigurationRequest.
        :type: str
        """
        self._application_id = application_id

    @property
    def environment_id(self):
        """Gets the environment_id of this ShowApplicationConfigurationRequest.


        :return: The environment_id of this ShowApplicationConfigurationRequest.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this ShowApplicationConfigurationRequest.


        :param environment_id: The environment_id of this ShowApplicationConfigurationRequest.
        :type: str
        """
        self._environment_id = environment_id

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
        if not isinstance(other, ShowApplicationConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
