# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeConfigurationDataVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'resource_sub_type': 'str',
        'umask': 'str',
        'mount_info': 'list[VolumeConfigurationMountInfo]'
    }

    attribute_map = {
        'volume_id': 'volume_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'resource_sub_type': 'resource_sub_type',
        'umask': 'umask',
        'mount_info': 'mount_info'
    }

    def __init__(self, volume_id=None, resource_name=None, resource_type=None, resource_sub_type=None, umask=None, mount_info=None):
        """VolumeConfigurationDataVolume

        The model defined in huaweicloud sdk

        :param volume_id: 云存储ID。
        :type volume_id: str
        :param resource_name: 云存储名称。
        :type resource_name: str
        :param resource_type: 云存储类型。
        :type resource_type: str
        :param resource_sub_type: 云存储子类型。
        :type resource_sub_type: str
        :param umask: 设置目录或文件缺省权限，默认值0027，sfs3.0类型的云存储不支持配置此参数。
        :type umask: str
        :param mount_info: 
        :type mount_info: list[:class:`huaweicloudsdkcae.v1.VolumeConfigurationMountInfo`]
        """
        
        

        self._volume_id = None
        self._resource_name = None
        self._resource_type = None
        self._resource_sub_type = None
        self._umask = None
        self._mount_info = None
        self.discriminator = None

        if volume_id is not None:
            self.volume_id = volume_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_sub_type is not None:
            self.resource_sub_type = resource_sub_type
        if umask is not None:
            self.umask = umask
        if mount_info is not None:
            self.mount_info = mount_info

    @property
    def volume_id(self):
        """Gets the volume_id of this VolumeConfigurationDataVolume.

        云存储ID。

        :return: The volume_id of this VolumeConfigurationDataVolume.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this VolumeConfigurationDataVolume.

        云存储ID。

        :param volume_id: The volume_id of this VolumeConfigurationDataVolume.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def resource_name(self):
        """Gets the resource_name of this VolumeConfigurationDataVolume.

        云存储名称。

        :return: The resource_name of this VolumeConfigurationDataVolume.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this VolumeConfigurationDataVolume.

        云存储名称。

        :param resource_name: The resource_name of this VolumeConfigurationDataVolume.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this VolumeConfigurationDataVolume.

        云存储类型。

        :return: The resource_type of this VolumeConfigurationDataVolume.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this VolumeConfigurationDataVolume.

        云存储类型。

        :param resource_type: The resource_type of this VolumeConfigurationDataVolume.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_sub_type(self):
        """Gets the resource_sub_type of this VolumeConfigurationDataVolume.

        云存储子类型。

        :return: The resource_sub_type of this VolumeConfigurationDataVolume.
        :rtype: str
        """
        return self._resource_sub_type

    @resource_sub_type.setter
    def resource_sub_type(self, resource_sub_type):
        """Sets the resource_sub_type of this VolumeConfigurationDataVolume.

        云存储子类型。

        :param resource_sub_type: The resource_sub_type of this VolumeConfigurationDataVolume.
        :type resource_sub_type: str
        """
        self._resource_sub_type = resource_sub_type

    @property
    def umask(self):
        """Gets the umask of this VolumeConfigurationDataVolume.

        设置目录或文件缺省权限，默认值0027，sfs3.0类型的云存储不支持配置此参数。

        :return: The umask of this VolumeConfigurationDataVolume.
        :rtype: str
        """
        return self._umask

    @umask.setter
    def umask(self, umask):
        """Sets the umask of this VolumeConfigurationDataVolume.

        设置目录或文件缺省权限，默认值0027，sfs3.0类型的云存储不支持配置此参数。

        :param umask: The umask of this VolumeConfigurationDataVolume.
        :type umask: str
        """
        self._umask = umask

    @property
    def mount_info(self):
        """Gets the mount_info of this VolumeConfigurationDataVolume.

        :return: The mount_info of this VolumeConfigurationDataVolume.
        :rtype: list[:class:`huaweicloudsdkcae.v1.VolumeConfigurationMountInfo`]
        """
        return self._mount_info

    @mount_info.setter
    def mount_info(self, mount_info):
        """Sets the mount_info of this VolumeConfigurationDataVolume.

        :param mount_info: The mount_info of this VolumeConfigurationDataVolume.
        :type mount_info: list[:class:`huaweicloudsdkcae.v1.VolumeConfigurationMountInfo`]
        """
        self._mount_info = mount_info

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
        if not isinstance(other, VolumeConfigurationDataVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
