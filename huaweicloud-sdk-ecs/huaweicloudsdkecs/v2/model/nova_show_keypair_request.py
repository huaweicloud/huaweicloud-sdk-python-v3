# coding: utf-8

import pprint
import re

import six





class NovaShowKeypairRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'keypair_name': 'str',
        'open_stack_api_version': 'str'
    }

    attribute_map = {
        'keypair_name': 'keypair_name',
        'open_stack_api_version': 'OpenStack-API-Version'
    }

    def __init__(self, keypair_name=None, open_stack_api_version=None):
        """NovaShowKeypairRequest - a model defined in huaweicloud sdk"""
        
        

        self._keypair_name = None
        self._open_stack_api_version = None
        self.discriminator = None

        self.keypair_name = keypair_name
        if open_stack_api_version is not None:
            self.open_stack_api_version = open_stack_api_version

    @property
    def keypair_name(self):
        """Gets the keypair_name of this NovaShowKeypairRequest.


        :return: The keypair_name of this NovaShowKeypairRequest.
        :rtype: str
        """
        return self._keypair_name

    @keypair_name.setter
    def keypair_name(self, keypair_name):
        """Sets the keypair_name of this NovaShowKeypairRequest.


        :param keypair_name: The keypair_name of this NovaShowKeypairRequest.
        :type: str
        """
        self._keypair_name = keypair_name

    @property
    def open_stack_api_version(self):
        """Gets the open_stack_api_version of this NovaShowKeypairRequest.


        :return: The open_stack_api_version of this NovaShowKeypairRequest.
        :rtype: str
        """
        return self._open_stack_api_version

    @open_stack_api_version.setter
    def open_stack_api_version(self, open_stack_api_version):
        """Sets the open_stack_api_version of this NovaShowKeypairRequest.


        :param open_stack_api_version: The open_stack_api_version of this NovaShowKeypairRequest.
        :type: str
        """
        self._open_stack_api_version = open_stack_api_version

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
        if not isinstance(other, NovaShowKeypairRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
