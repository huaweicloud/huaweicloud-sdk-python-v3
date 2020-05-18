# coding: utf-8

import pprint
import re

import six


class NovaAttachInterfaceResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'interface_attachment': 'NovaServerInterfaceDetail'
    }

    attribute_map = {
        'interface_attachment': 'interfaceAttachment'
    }

    def __init__(self, interface_attachment=None):  # noqa: E501
        """NovaAttachInterfaceResponse - a model defined in huaweicloud sdk"""

        self._interface_attachment = None
        self.discriminator = None

        if interface_attachment is not None:
            self.interface_attachment = interface_attachment

    @property
    def interface_attachment(self):
        """Gets the interface_attachment of this NovaAttachInterfaceResponse.


        :return: The interface_attachment of this NovaAttachInterfaceResponse.
        :rtype: NovaServerInterfaceDetail
        """
        return self._interface_attachment

    @interface_attachment.setter
    def interface_attachment(self, interface_attachment):
        """Sets the interface_attachment of this NovaAttachInterfaceResponse.


        :param interface_attachment: The interface_attachment of this NovaAttachInterfaceResponse.
        :type: NovaServerInterfaceDetail
        """
        self._interface_attachment = interface_attachment

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
        if not isinstance(other, NovaAttachInterfaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
