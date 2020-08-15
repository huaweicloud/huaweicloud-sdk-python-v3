# coding: utf-8

import pprint
import re

import six





class CreatePersonalAuthRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'repo_type': 'str',
        'body': 'AccessToken'
    }

    attribute_map = {
        'repo_type': 'repo_type',
        'body': 'body'
    }

    def __init__(self, repo_type=None, body=None):
        """CreatePersonalAuthRequest - a model defined in huaweicloud sdk"""
        
        

        self._repo_type = None
        self._body = None
        self.discriminator = None

        self.repo_type = repo_type
        if body is not None:
            self.body = body

    @property
    def repo_type(self):
        """Gets the repo_type of this CreatePersonalAuthRequest.


        :return: The repo_type of this CreatePersonalAuthRequest.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """Sets the repo_type of this CreatePersonalAuthRequest.


        :param repo_type: The repo_type of this CreatePersonalAuthRequest.
        :type: str
        """
        self._repo_type = repo_type

    @property
    def body(self):
        """Gets the body of this CreatePersonalAuthRequest.


        :return: The body of this CreatePersonalAuthRequest.
        :rtype: AccessToken
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreatePersonalAuthRequest.


        :param body: The body of this CreatePersonalAuthRequest.
        :type: AccessToken
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
        if not isinstance(other, CreatePersonalAuthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
