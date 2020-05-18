# coding: utf-8

import pprint
import re

import six


class ListServerVolumeAttachmentsResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'volume_attachments': 'list[ServerVolumeAttachment]'
    }

    attribute_map = {
        'volume_attachments': 'volumeAttachments'
    }

    def __init__(self, volume_attachments=None):  # noqa: E501
        """ListServerVolumeAttachmentsResponse - a model defined in huaweicloud sdk"""

        self._volume_attachments = None
        self.discriminator = None

        if volume_attachments is not None:
            self.volume_attachments = volume_attachments

    @property
    def volume_attachments(self):
        """Gets the volume_attachments of this ListServerVolumeAttachmentsResponse.

        云服务器挂载信息列表

        :return: The volume_attachments of this ListServerVolumeAttachmentsResponse.
        :rtype: list[ServerVolumeAttachment]
        """
        return self._volume_attachments

    @volume_attachments.setter
    def volume_attachments(self, volume_attachments):
        """Sets the volume_attachments of this ListServerVolumeAttachmentsResponse.

        云服务器挂载信息列表

        :param volume_attachments: The volume_attachments of this ListServerVolumeAttachmentsResponse.
        :type: list[ServerVolumeAttachment]
        """
        self._volume_attachments = volume_attachments

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
        if not isinstance(other, ListServerVolumeAttachmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
