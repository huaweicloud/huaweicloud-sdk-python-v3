# coding: utf-8

import pprint
import re

import six





class AttachServerVolumeRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'volume_attachment': 'AttachServerVolumeOption'
    }

    attribute_map = {
        'volume_attachment': 'volumeAttachment'
    }

    def __init__(self, volume_attachment=None):
        """AttachServerVolumeRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._volume_attachment = None
        self.discriminator = None

        self.volume_attachment = volume_attachment

    @property
    def volume_attachment(self):
        """Gets the volume_attachment of this AttachServerVolumeRequestBody.


        :return: The volume_attachment of this AttachServerVolumeRequestBody.
        :rtype: AttachServerVolumeOption
        """
        return self._volume_attachment

    @volume_attachment.setter
    def volume_attachment(self, volume_attachment):
        """Sets the volume_attachment of this AttachServerVolumeRequestBody.


        :param volume_attachment: The volume_attachment of this AttachServerVolumeRequestBody.
        :type: AttachServerVolumeOption
        """
        self._volume_attachment = volume_attachment

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
        if not isinstance(other, AttachServerVolumeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
