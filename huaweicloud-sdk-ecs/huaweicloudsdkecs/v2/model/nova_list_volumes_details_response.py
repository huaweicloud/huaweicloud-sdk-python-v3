# coding: utf-8

import pprint
import re

import six


class NovaListVolumesDetailsResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'volumes': 'list[NovaVolumeDetail]'
    }

    attribute_map = {
        'volumes': 'volumes'
    }

    def __init__(self, volumes=None):  # noqa: E501
        """NovaListVolumesDetailsResponse - a model defined in huaweicloud sdk"""

        self._volumes = None
        self.discriminator = None

        if volumes is not None:
            self.volumes = volumes

    @property
    def volumes(self):
        """Gets the volumes of this NovaListVolumesDetailsResponse.

        磁盘详情列表。

        :return: The volumes of this NovaListVolumesDetailsResponse.
        :rtype: list[NovaVolumeDetail]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this NovaListVolumesDetailsResponse.

        磁盘详情列表。

        :param volumes: The volumes of this NovaListVolumesDetailsResponse.
        :type: list[NovaVolumeDetail]
        """
        self._volumes = volumes

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
        if not isinstance(other, NovaListVolumesDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
