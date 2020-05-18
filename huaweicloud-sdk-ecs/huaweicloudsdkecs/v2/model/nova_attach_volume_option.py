# coding: utf-8

import pprint
import re

import six


class NovaAttachVolumeOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'device': 'str',
        'volume_id': 'str'
    }

    attribute_map = {
        'device': 'device',
        'volume_id': 'volumeId'
    }

    def __init__(self, device=None, volume_id=None):  # noqa: E501
        """NovaAttachVolumeOption - a model defined in huaweicloud sdk"""

        self._device = None
        self._volume_id = None
        self.discriminator = None

        if device is not None:
            self.device = device
        self.volume_id = volume_id

    @property
    def device(self):
        """Gets the device of this NovaAttachVolumeOption.

        磁盘挂载点，如/dev/sda，/dev/sdb。  新增加的磁盘挂载点不能和已有的磁盘挂载点相同。  需要根据已有设备名称顺序指定，否则由系统自动生成。  说明： VBD磁盘挂载点只支持从/dev/vdb到/dev/vdx，建议按英文字母顺序进行挂载，否则可能出现云服务器中磁盘盘符错乱的情况。

        :return: The device of this NovaAttachVolumeOption.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this NovaAttachVolumeOption.

        磁盘挂载点，如/dev/sda，/dev/sdb。  新增加的磁盘挂载点不能和已有的磁盘挂载点相同。  需要根据已有设备名称顺序指定，否则由系统自动生成。  说明： VBD磁盘挂载点只支持从/dev/vdb到/dev/vdx，建议按英文字母顺序进行挂载，否则可能出现云服务器中磁盘盘符错乱的情况。

        :param device: The device of this NovaAttachVolumeOption.
        :type: str
        """
        self._device = device

    @property
    def volume_id(self):
        """Gets the volume_id of this NovaAttachVolumeOption.

        待挂载磁盘的磁盘ID，UUID格式。

        :return: The volume_id of this NovaAttachVolumeOption.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this NovaAttachVolumeOption.

        待挂载磁盘的磁盘ID，UUID格式。

        :param volume_id: The volume_id of this NovaAttachVolumeOption.
        :type: str
        """
        self._volume_id = volume_id

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
        if not isinstance(other, NovaAttachVolumeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
