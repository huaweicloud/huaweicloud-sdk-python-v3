# coding: utf-8

import pprint
import re

import six





class DeleteServerMetadataRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'server_id': 'str'
    }

    attribute_map = {
        'key': 'key',
        'server_id': 'server_id'
    }

    def __init__(self, key=None, server_id=None):
        """DeleteServerMetadataRequest - a model defined in huaweicloud sdk"""
        
        

        self._key = None
        self._server_id = None
        self.discriminator = None

        self.key = key
        self.server_id = server_id

    @property
    def key(self):
        """Gets the key of this DeleteServerMetadataRequest.


        :return: The key of this DeleteServerMetadataRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeleteServerMetadataRequest.


        :param key: The key of this DeleteServerMetadataRequest.
        :type: str
        """
        self._key = key

    @property
    def server_id(self):
        """Gets the server_id of this DeleteServerMetadataRequest.


        :return: The server_id of this DeleteServerMetadataRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this DeleteServerMetadataRequest.


        :param server_id: The server_id of this DeleteServerMetadataRequest.
        :type: str
        """
        self._server_id = server_id

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
        if not isinstance(other, DeleteServerMetadataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
