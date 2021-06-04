# coding: utf-8

import pprint
import re

import six





class RefererBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'referer': 'Referer'
    }

    attribute_map = {
        'referer': 'referer'
    }

    def __init__(self, referer=None):
        """RefererBody - a model defined in huaweicloud sdk"""
        
        

        self._referer = None
        self.discriminator = None

        self.referer = referer

    @property
    def referer(self):
        """Gets the referer of this RefererBody.


        :return: The referer of this RefererBody.
        :rtype: Referer
        """
        return self._referer

    @referer.setter
    def referer(self, referer):
        """Sets the referer of this RefererBody.


        :param referer: The referer of this RefererBody.
        :type: Referer
        """
        self._referer = referer

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
        if not isinstance(other, RefererBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
