# coding: utf-8

import pprint
import re

import six





class DeletePermanentAccessKeyRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access_key': 'str'
    }

    attribute_map = {
        'access_key': 'access_key'
    }

    def __init__(self, access_key=None):
        """DeletePermanentAccessKeyRequest - a model defined in huaweicloud sdk"""
        
        

        self._access_key = None
        self.discriminator = None

        self.access_key = access_key

    @property
    def access_key(self):
        """Gets the access_key of this DeletePermanentAccessKeyRequest.


        :return: The access_key of this DeletePermanentAccessKeyRequest.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this DeletePermanentAccessKeyRequest.


        :param access_key: The access_key of this DeletePermanentAccessKeyRequest.
        :type: str
        """
        self._access_key = access_key

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
        if not isinstance(other, DeletePermanentAccessKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
