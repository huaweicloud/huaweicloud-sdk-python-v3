# coding: utf-8

import pprint
import re

import six





class KeyAliasInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'key_alias': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'key_alias': 'key_alias'
    }

    def __init__(self, key_id=None, key_alias=None):
        """KeyAliasInfo - a model defined in huaweicloud sdk"""
        
        

        self._key_id = None
        self._key_alias = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if key_alias is not None:
            self.key_alias = key_alias

    @property
    def key_id(self):
        """Gets the key_id of this KeyAliasInfo.

        密钥ID。

        :return: The key_id of this KeyAliasInfo.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this KeyAliasInfo.

        密钥ID。

        :param key_id: The key_id of this KeyAliasInfo.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_alias(self):
        """Gets the key_alias of this KeyAliasInfo.

        密钥别名。

        :return: The key_alias of this KeyAliasInfo.
        :rtype: str
        """
        return self._key_alias

    @key_alias.setter
    def key_alias(self, key_alias):
        """Sets the key_alias of this KeyAliasInfo.

        密钥别名。

        :param key_alias: The key_alias of this KeyAliasInfo.
        :type: str
        """
        self._key_alias = key_alias

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
        if not isinstance(other, KeyAliasInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
