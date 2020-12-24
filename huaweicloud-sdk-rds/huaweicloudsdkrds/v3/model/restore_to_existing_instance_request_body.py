# coding: utf-8

import pprint
import re

import six





class RestoreToExistingInstanceRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'source': 'RestoreToExistingInstanceRequestBodySource',
        'target': 'RestoreToExistingInstanceRequestBodyTarget'
    }

    attribute_map = {
        'source': 'source',
        'target': 'target'
    }

    def __init__(self, source=None, target=None):
        """RestoreToExistingInstanceRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._source = None
        self._target = None
        self.discriminator = None

        self.source = source
        self.target = target

    @property
    def source(self):
        """Gets the source of this RestoreToExistingInstanceRequestBody.


        :return: The source of this RestoreToExistingInstanceRequestBody.
        :rtype: RestoreToExistingInstanceRequestBodySource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this RestoreToExistingInstanceRequestBody.


        :param source: The source of this RestoreToExistingInstanceRequestBody.
        :type: RestoreToExistingInstanceRequestBodySource
        """
        self._source = source

    @property
    def target(self):
        """Gets the target of this RestoreToExistingInstanceRequestBody.


        :return: The target of this RestoreToExistingInstanceRequestBody.
        :rtype: RestoreToExistingInstanceRequestBodyTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this RestoreToExistingInstanceRequestBody.


        :param target: The target of this RestoreToExistingInstanceRequestBody.
        :type: RestoreToExistingInstanceRequestBodyTarget
        """
        self._target = target

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
        if not isinstance(other, RestoreToExistingInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
