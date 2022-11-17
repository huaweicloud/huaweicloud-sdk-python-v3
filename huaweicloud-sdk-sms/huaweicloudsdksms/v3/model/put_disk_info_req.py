# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutDiskInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disks': 'list[ServerDisk]',
        'volumegroups': 'list[VolumeGroups]',
        'btrfs_list': 'list[BtrfsFileSystem]'
    }

    attribute_map = {
        'disks': 'disks',
        'volumegroups': 'volumegroups',
        'btrfs_list': 'btrfs_list'
    }

    def __init__(self, disks=None, volumegroups=None, btrfs_list=None):
        """PutDiskInfoReq

        The model defined in huaweicloud sdk

        :param disks: 更新的磁盘信息
        :type disks: list[:class:`huaweicloudsdksms.v3.ServerDisk`]
        :param volumegroups: 更新的卷信息
        :type volumegroups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        :param btrfs_list: 更新的btrfs信息
        :type btrfs_list: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        """
        
        

        self._disks = None
        self._volumegroups = None
        self._btrfs_list = None
        self.discriminator = None

        if disks is not None:
            self.disks = disks
        if volumegroups is not None:
            self.volumegroups = volumegroups
        if btrfs_list is not None:
            self.btrfs_list = btrfs_list

    @property
    def disks(self):
        """Gets the disks of this PutDiskInfoReq.

        更新的磁盘信息

        :return: The disks of this PutDiskInfoReq.
        :rtype: list[:class:`huaweicloudsdksms.v3.ServerDisk`]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this PutDiskInfoReq.

        更新的磁盘信息

        :param disks: The disks of this PutDiskInfoReq.
        :type disks: list[:class:`huaweicloudsdksms.v3.ServerDisk`]
        """
        self._disks = disks

    @property
    def volumegroups(self):
        """Gets the volumegroups of this PutDiskInfoReq.

        更新的卷信息

        :return: The volumegroups of this PutDiskInfoReq.
        :rtype: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        return self._volumegroups

    @volumegroups.setter
    def volumegroups(self, volumegroups):
        """Sets the volumegroups of this PutDiskInfoReq.

        更新的卷信息

        :param volumegroups: The volumegroups of this PutDiskInfoReq.
        :type volumegroups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        self._volumegroups = volumegroups

    @property
    def btrfs_list(self):
        """Gets the btrfs_list of this PutDiskInfoReq.

        更新的btrfs信息

        :return: The btrfs_list of this PutDiskInfoReq.
        :rtype: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        """
        return self._btrfs_list

    @btrfs_list.setter
    def btrfs_list(self, btrfs_list):
        """Sets the btrfs_list of this PutDiskInfoReq.

        更新的btrfs信息

        :param btrfs_list: The btrfs_list of this PutDiskInfoReq.
        :type btrfs_list: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        """
        self._btrfs_list = btrfs_list

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PutDiskInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
