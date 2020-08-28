# coding: utf-8

import pprint
import re

import six





class CreateFunctionVersionRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'digest': 'str',
        'version': 'str',
        'description': 'str'
    }

    attribute_map = {
        'digest': 'digest',
        'version': 'version',
        'description': 'description'
    }

    def __init__(self, digest=None, version=None, description=None):
        """CreateFunctionVersionRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._digest = None
        self._version = None
        self._description = None
        self.discriminator = None

        if digest is not None:
            self.digest = digest
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description

    @property
    def digest(self):
        """Gets the digest of this CreateFunctionVersionRequestBody.

        md5键值

        :return: The digest of this CreateFunctionVersionRequestBody.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this CreateFunctionVersionRequestBody.

        md5键值

        :param digest: The digest of this CreateFunctionVersionRequestBody.
        :type: str
        """
        self._digest = digest

    @property
    def version(self):
        """Gets the version of this CreateFunctionVersionRequestBody.

        发布版本名称

        :return: The version of this CreateFunctionVersionRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateFunctionVersionRequestBody.

        发布版本名称

        :param version: The version of this CreateFunctionVersionRequestBody.
        :type: str
        """
        self._version = version

    @property
    def description(self):
        """Gets the description of this CreateFunctionVersionRequestBody.

        发布版本描述

        :return: The description of this CreateFunctionVersionRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateFunctionVersionRequestBody.

        发布版本描述

        :param description: The description of this CreateFunctionVersionRequestBody.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, CreateFunctionVersionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
