# coding: utf-8

import pprint
import re

import six





class BlockDeviceAttachableQuantity:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'free_scsi': 'int',
        'free_blk': 'int',
        'free_disk': 'int'
    }

    attribute_map = {
        'free_scsi': 'free_scsi',
        'free_blk': 'free_blk',
        'free_disk': 'free_disk'
    }

    def __init__(self, free_scsi=None, free_blk=None, free_disk=None):
        """BlockDeviceAttachableQuantity - a model defined in huaweicloud sdk"""
        
        

        self._free_scsi = None
        self._free_blk = None
        self._free_disk = None
        self.discriminator = None

        if free_scsi is not None:
            self.free_scsi = free_scsi
        if free_blk is not None:
            self.free_blk = free_blk
        if free_disk is not None:
            self.free_disk = free_disk

    @property
    def free_scsi(self):
        """Gets the free_scsi of this BlockDeviceAttachableQuantity.

        云服务器可挂载scsi类型磁盘数量。

        :return: The free_scsi of this BlockDeviceAttachableQuantity.
        :rtype: int
        """
        return self._free_scsi

    @free_scsi.setter
    def free_scsi(self, free_scsi):
        """Sets the free_scsi of this BlockDeviceAttachableQuantity.

        云服务器可挂载scsi类型磁盘数量。

        :param free_scsi: The free_scsi of this BlockDeviceAttachableQuantity.
        :type: int
        """
        self._free_scsi = free_scsi

    @property
    def free_blk(self):
        """Gets the free_blk of this BlockDeviceAttachableQuantity.

        云服务器可挂载virtio_blk类型磁盘数量。

        :return: The free_blk of this BlockDeviceAttachableQuantity.
        :rtype: int
        """
        return self._free_blk

    @free_blk.setter
    def free_blk(self, free_blk):
        """Sets the free_blk of this BlockDeviceAttachableQuantity.

        云服务器可挂载virtio_blk类型磁盘数量。

        :param free_blk: The free_blk of this BlockDeviceAttachableQuantity.
        :type: int
        """
        self._free_blk = free_blk

    @property
    def free_disk(self):
        """Gets the free_disk of this BlockDeviceAttachableQuantity.

        云服务器可挂载磁盘总数。

        :return: The free_disk of this BlockDeviceAttachableQuantity.
        :rtype: int
        """
        return self._free_disk

    @free_disk.setter
    def free_disk(self, free_disk):
        """Sets the free_disk of this BlockDeviceAttachableQuantity.

        云服务器可挂载磁盘总数。

        :param free_disk: The free_disk of this BlockDeviceAttachableQuantity.
        :type: int
        """
        self._free_disk = free_disk

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
        if not isinstance(other, BlockDeviceAttachableQuantity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
