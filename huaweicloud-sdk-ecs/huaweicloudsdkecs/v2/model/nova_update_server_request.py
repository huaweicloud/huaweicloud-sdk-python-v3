# coding: utf-8

import pprint
import re

import six


class NovaUpdateServerRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'open_stack_api_version': 'str',
        'server_id': 'str',
        'body': 'NovaUpdateServerRequestBody'
    }

    attribute_map = {
        'open_stack_api_version': 'OpenStack-API-Version',
        'server_id': 'server_id',
        'body': 'body'
    }

    def __init__(self, open_stack_api_version='compute 2.60', server_id=None, body=None):  # noqa: E501
        """NovaUpdateServerRequest - a model defined in huaweicloud sdk"""

        self._open_stack_api_version = None
        self._server_id = None
        self._body = None
        self.discriminator = None

        if open_stack_api_version is not None:
            self.open_stack_api_version = open_stack_api_version
        self.server_id = server_id
        if body is not None:
            self.body = body

    @property
    def open_stack_api_version(self):
        """Gets the open_stack_api_version of this NovaUpdateServerRequest.


        :return: The open_stack_api_version of this NovaUpdateServerRequest.
        :rtype: str
        """
        return self._open_stack_api_version

    @open_stack_api_version.setter
    def open_stack_api_version(self, open_stack_api_version):
        """Sets the open_stack_api_version of this NovaUpdateServerRequest.


        :param open_stack_api_version: The open_stack_api_version of this NovaUpdateServerRequest.
        :type: str
        """
        self._open_stack_api_version = open_stack_api_version

    @property
    def server_id(self):
        """Gets the server_id of this NovaUpdateServerRequest.


        :return: The server_id of this NovaUpdateServerRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this NovaUpdateServerRequest.


        :param server_id: The server_id of this NovaUpdateServerRequest.
        :type: str
        """
        self._server_id = server_id

    @property
    def body(self):
        """Gets the body of this NovaUpdateServerRequest.


        :return: The body of this NovaUpdateServerRequest.
        :rtype: NovaUpdateServerRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this NovaUpdateServerRequest.


        :param body: The body of this NovaUpdateServerRequest.
        :type: NovaUpdateServerRequestBody
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
        if not isinstance(other, NovaUpdateServerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
