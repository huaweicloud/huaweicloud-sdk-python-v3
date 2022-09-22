# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutSourceServerBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'migprojectid': 'str',
        'disks': 'list[PutDisk]',
        'volume_groups': 'list[PutVolumeGroups]'
    }

    attribute_map = {
        'name': 'name',
        'migprojectid': 'migprojectid',
        'disks': 'disks',
        'volume_groups': 'volume_groups'
    }

    def __init__(self, name=None, migprojectid=None, disks=None, volume_groups=None):
        """PutSourceServerBody

        The model defined in huaweicloud sdk

        :param name: 源端服务器修改后的名字
        :type name: str
        :param migprojectid: 源端服务器修改后所属的迁移项目ID
        :type migprojectid: str
        :param disks: 磁盘
        :type disks: list[:class:`huaweicloudsdksms.v3.PutDisk`]
        :param volume_groups: 卷组
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.PutVolumeGroups`]
        """
        
        

        self._name = None
        self._migprojectid = None
        self._disks = None
        self._volume_groups = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if migprojectid is not None:
            self.migprojectid = migprojectid
        if disks is not None:
            self.disks = disks
        if volume_groups is not None:
            self.volume_groups = volume_groups

    @property
    def name(self):
        """Gets the name of this PutSourceServerBody.

        源端服务器修改后的名字

        :return: The name of this PutSourceServerBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutSourceServerBody.

        源端服务器修改后的名字

        :param name: The name of this PutSourceServerBody.
        :type name: str
        """
        self._name = name

    @property
    def migprojectid(self):
        """Gets the migprojectid of this PutSourceServerBody.

        源端服务器修改后所属的迁移项目ID

        :return: The migprojectid of this PutSourceServerBody.
        :rtype: str
        """
        return self._migprojectid

    @migprojectid.setter
    def migprojectid(self, migprojectid):
        """Sets the migprojectid of this PutSourceServerBody.

        源端服务器修改后所属的迁移项目ID

        :param migprojectid: The migprojectid of this PutSourceServerBody.
        :type migprojectid: str
        """
        self._migprojectid = migprojectid

    @property
    def disks(self):
        """Gets the disks of this PutSourceServerBody.

        磁盘

        :return: The disks of this PutSourceServerBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.PutDisk`]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this PutSourceServerBody.

        磁盘

        :param disks: The disks of this PutSourceServerBody.
        :type disks: list[:class:`huaweicloudsdksms.v3.PutDisk`]
        """
        self._disks = disks

    @property
    def volume_groups(self):
        """Gets the volume_groups of this PutSourceServerBody.

        卷组

        :return: The volume_groups of this PutSourceServerBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.PutVolumeGroups`]
        """
        return self._volume_groups

    @volume_groups.setter
    def volume_groups(self, volume_groups):
        """Sets the volume_groups of this PutSourceServerBody.

        卷组

        :param volume_groups: The volume_groups of this PutSourceServerBody.
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.PutVolumeGroups`]
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
        if not isinstance(other, PutSourceServerBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
