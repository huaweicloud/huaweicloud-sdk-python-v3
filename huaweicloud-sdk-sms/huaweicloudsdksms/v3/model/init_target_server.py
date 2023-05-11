# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InitTargetServer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disks': 'list[DiskIntargetServer]',
        'volume_groups': 'list[VolumeGroups]'
    }

    attribute_map = {
        'disks': 'disks',
        'volume_groups': 'volume_groups'
    }

    def __init__(self, disks=None, volume_groups=None):
        """InitTargetServer

        The model defined in huaweicloud sdk

        :param disks: 推荐的目的端服务器的磁盘信息
        :type disks: list[:class:`huaweicloudsdksms.v3.DiskIntargetServer`]
        :param volume_groups: Linux必选，如果没有卷组，输入[]
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        
        

        self._disks = None
        self._volume_groups = None
        self.discriminator = None

        self.disks = disks
        if volume_groups is not None:
            self.volume_groups = volume_groups

    @property
    def disks(self):
        """Gets the disks of this InitTargetServer.

        推荐的目的端服务器的磁盘信息

        :return: The disks of this InitTargetServer.
        :rtype: list[:class:`huaweicloudsdksms.v3.DiskIntargetServer`]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this InitTargetServer.

        推荐的目的端服务器的磁盘信息

        :param disks: The disks of this InitTargetServer.
        :type disks: list[:class:`huaweicloudsdksms.v3.DiskIntargetServer`]
        """
        self._disks = disks

    @property
    def volume_groups(self):
        """Gets the volume_groups of this InitTargetServer.

        Linux必选，如果没有卷组，输入[]

        :return: The volume_groups of this InitTargetServer.
        :rtype: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        return self._volume_groups

    @volume_groups.setter
    def volume_groups(self, volume_groups):
        """Sets the volume_groups of this InitTargetServer.

        Linux必选，如果没有卷组，输入[]

        :param volume_groups: The volume_groups of this InitTargetServer.
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
        if not isinstance(other, InitTargetServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
