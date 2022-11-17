# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetServerByTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'btrfs_list': 'list[BtrfsFileSystem]',
        'disks': 'list[TargetDisks]',
        'name': 'str',
        'vm_id': 'str',
        'volume_groups': 'list[VolumeGroups]'
    }

    attribute_map = {
        'btrfs_list': 'btrfs_list',
        'disks': 'disks',
        'name': 'name',
        'vm_id': 'vm_id',
        'volume_groups': 'volume_groups'
    }

    def __init__(self, btrfs_list=None, disks=None, name=None, vm_id=None, volume_groups=None):
        """TargetServerByTask

        The model defined in huaweicloud sdk

        :param btrfs_list: btrfs信息，数据从源端获取
        :type btrfs_list: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        :param disks: 磁盘信息
        :type disks: list[:class:`huaweicloudsdksms.v3.TargetDisks`]
        :param name: 名称
        :type name: str
        :param vm_id: 虚拟机ID
        :type vm_id: str
        :param volume_groups: 卷组，数据从源端获取
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        
        

        self._btrfs_list = None
        self._disks = None
        self._name = None
        self._vm_id = None
        self._volume_groups = None
        self.discriminator = None

        if btrfs_list is not None:
            self.btrfs_list = btrfs_list
        self.disks = disks
        self.name = name
        self.vm_id = vm_id
        if volume_groups is not None:
            self.volume_groups = volume_groups

    @property
    def btrfs_list(self):
        """Gets the btrfs_list of this TargetServerByTask.

        btrfs信息，数据从源端获取

        :return: The btrfs_list of this TargetServerByTask.
        :rtype: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        """
        return self._btrfs_list

    @btrfs_list.setter
    def btrfs_list(self, btrfs_list):
        """Sets the btrfs_list of this TargetServerByTask.

        btrfs信息，数据从源端获取

        :param btrfs_list: The btrfs_list of this TargetServerByTask.
        :type btrfs_list: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        """
        self._btrfs_list = btrfs_list

    @property
    def disks(self):
        """Gets the disks of this TargetServerByTask.

        磁盘信息

        :return: The disks of this TargetServerByTask.
        :rtype: list[:class:`huaweicloudsdksms.v3.TargetDisks`]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this TargetServerByTask.

        磁盘信息

        :param disks: The disks of this TargetServerByTask.
        :type disks: list[:class:`huaweicloudsdksms.v3.TargetDisks`]
        """
        self._disks = disks

    @property
    def name(self):
        """Gets the name of this TargetServerByTask.

        名称

        :return: The name of this TargetServerByTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetServerByTask.

        名称

        :param name: The name of this TargetServerByTask.
        :type name: str
        """
        self._name = name

    @property
    def vm_id(self):
        """Gets the vm_id of this TargetServerByTask.

        虚拟机ID

        :return: The vm_id of this TargetServerByTask.
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this TargetServerByTask.

        虚拟机ID

        :param vm_id: The vm_id of this TargetServerByTask.
        :type vm_id: str
        """
        self._vm_id = vm_id

    @property
    def volume_groups(self):
        """Gets the volume_groups of this TargetServerByTask.

        卷组，数据从源端获取

        :return: The volume_groups of this TargetServerByTask.
        :rtype: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        return self._volume_groups

    @volume_groups.setter
    def volume_groups(self, volume_groups):
        """Sets the volume_groups of this TargetServerByTask.

        卷组，数据从源端获取

        :param volume_groups: The volume_groups of this TargetServerByTask.
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        self._volume_groups = volume_groups

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
        if not isinstance(other, TargetServerByTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
