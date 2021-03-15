# coding: utf-8

import pprint
import re

import six





class DatabaseForListSchema:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'schema_name': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'schema_name': 'schema_name',
        'owner': 'owner'
    }

    def __init__(self, schema_name=None, owner=None):
        """DatabaseForListSchema - a model defined in huaweicloud sdk"""
        
        

        self._schema_name = None
        self._owner = None
        self.discriminator = None

        self.schema_name = schema_name
        self.owner = owner

    @property
    def schema_name(self):
        """Gets the schema_name of this DatabaseForListSchema.

        schema名称。

        :return: The schema_name of this DatabaseForListSchema.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this DatabaseForListSchema.

        schema名称。

        :param schema_name: The schema_name of this DatabaseForListSchema.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def owner(self):
        """Gets the owner of this DatabaseForListSchema.

        schema所属用户。

        :return: The owner of this DatabaseForListSchema.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DatabaseForListSchema.

        schema所属用户。

        :param owner: The owner of this DatabaseForListSchema.
        :type: str
        """
        self._owner = owner

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
        if not isinstance(other, DatabaseForListSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
