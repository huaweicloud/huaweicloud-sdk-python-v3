# coding: utf-8

import pprint
import re

import six





class CreateApplicationEndpointRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'application_urn': 'str',
        'body': 'CreateApplicationEndpointRequestBody'
    }

    attribute_map = {
        'application_urn': 'application_urn',
        'body': 'body'
    }

    def __init__(self, application_urn=None, body=None):
        """CreateApplicationEndpointRequest - a model defined in huaweicloud sdk"""
        
        

        self._application_urn = None
        self._body = None
        self.discriminator = None

        self.application_urn = application_urn
        if body is not None:
            self.body = body

    @property
    def application_urn(self):
        """Gets the application_urn of this CreateApplicationEndpointRequest.


        :return: The application_urn of this CreateApplicationEndpointRequest.
        :rtype: str
        """
        return self._application_urn

    @application_urn.setter
    def application_urn(self, application_urn):
        """Sets the application_urn of this CreateApplicationEndpointRequest.


        :param application_urn: The application_urn of this CreateApplicationEndpointRequest.
        :type: str
        """
        self._application_urn = application_urn

    @property
    def body(self):
        """Gets the body of this CreateApplicationEndpointRequest.


        :return: The body of this CreateApplicationEndpointRequest.
        :rtype: CreateApplicationEndpointRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateApplicationEndpointRequest.


        :param body: The body of this CreateApplicationEndpointRequest.
        :type: CreateApplicationEndpointRequestBody
        """
        self._body = body

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
        if not isinstance(other, CreateApplicationEndpointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
