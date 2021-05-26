# coding: utf-8

import pprint
import re

import six





class ShowSecretVersionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'secret_id': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'secret_id': 'secret_id',
        'version_id': 'version_id'
    }

    def __init__(self, secret_id=None, version_id=None):
        """ShowSecretVersionRequest - a model defined in huaweicloud sdk"""
        
        

        self._secret_id = None
        self._version_id = None
        self.discriminator = None

        self.secret_id = secret_id
        self.version_id = version_id

    @property
    def secret_id(self):
        """Gets the secret_id of this ShowSecretVersionRequest.

        凭据的资源标识符。

        :return: The secret_id of this ShowSecretVersionRequest.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """Sets the secret_id of this ShowSecretVersionRequest.

        凭据的资源标识符。

        :param secret_id: The secret_id of this ShowSecretVersionRequest.
        :type: str
        """
        self._secret_id = secret_id

    @property
    def version_id(self):
        """Gets the version_id of this ShowSecretVersionRequest.

        凭据的版本标识符。

        :return: The version_id of this ShowSecretVersionRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ShowSecretVersionRequest.

        凭据的版本标识符。

        :param version_id: The version_id of this ShowSecretVersionRequest.
        :type: str
        """
        self._version_id = version_id

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
        if not isinstance(other, ShowSecretVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
