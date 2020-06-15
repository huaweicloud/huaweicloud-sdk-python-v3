# coding: utf-8

import pprint
import re

import six


class ImageMetadata(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'checksum': 'str',
        'container_format': 'str',
        'disk_format': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'image_source_type': 'str',
        'imagetype': 'str',
        'isregistered': 'str',
        'min_disk': 'str',
        'min_ram': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'os_version': 'str',
        'platform': 'str',
        'size': 'str',
        'virtual_env_type': 'str'
    }

    attribute_map = {
        'checksum': 'checksum',
        'container_format': 'container_format',
        'disk_format': 'disk_format',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'image_source_type': 'image_source_type',
        'imagetype': 'imagetype',
        'isregistered': 'isregistered',
        'min_disk': 'min_disk',
        'min_ram': 'min_ram',
        'os_bit': 'os_bit',
        'os_type': 'os_type',
        'os_version': 'os_version',
        'platform': 'platform',
        'size': 'size',
        'virtual_env_type': 'virtual_env_type'
    }

    def __init__(self, checksum=None, container_format=None, disk_format=None, image_id=None, image_name=None, image_source_type=None, imagetype=None, isregistered=None, min_disk=None, min_ram=None, os_bit=None, os_type=None, os_version=None, platform=None, size=None, virtual_env_type=None):  # noqa: E501
        """ImageMetadata - a model defined in huaweicloud sdk"""

        self._checksum = None
        self._container_format = None
        self._disk_format = None
        self._image_id = None
        self._image_name = None
        self._image_source_type = None
        self._imagetype = None
        self._isregistered = None
        self._min_disk = None
        self._min_ram = None
        self._os_bit = None
        self._os_type = None
        self._os_version = None
        self._platform = None
        self._size = None
        self._virtual_env_type = None
        self.discriminator = None

        self.checksum = checksum
        self.container_format = container_format
        self.disk_format = disk_format
        self.image_id = image_id
        self.image_name = image_name
        self.image_source_type = image_source_type
        self.imagetype = imagetype
        self.isregistered = isregistered
        self.min_disk = min_disk
        self.min_ram = min_ram
        self.os_bit = os_bit
        self.os_type = os_type
        self.os_version = os_version
        self.platform = platform
        self.size = size
        self.virtual_env_type = virtual_env_type

    @property
    def checksum(self):
        """Gets the checksum of this ImageMetadata.

        预留属性。

        :return: The checksum of this ImageMetadata.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this ImageMetadata.

        预留属性。

        :param checksum: The checksum of this ImageMetadata.
        :type: str
        """
        self._checksum = checksum

    @property
    def container_format(self):
        """Gets the container_format of this ImageMetadata.

        容器类型。

        :return: The container_format of this ImageMetadata.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        """Sets the container_format of this ImageMetadata.

        容器类型。

        :param container_format: The container_format of this ImageMetadata.
        :type: str
        """
        self._container_format = container_format

    @property
    def disk_format(self):
        """Gets the disk_format of this ImageMetadata.

        镜像的格式。

        :return: The disk_format of this ImageMetadata.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        """Sets the disk_format of this ImageMetadata.

        镜像的格式。

        :param disk_format: The disk_format of this ImageMetadata.
        :type: str
        """
        self._disk_format = disk_format

    @property
    def image_id(self):
        """Gets the image_id of this ImageMetadata.

        镜像ID。

        :return: The image_id of this ImageMetadata.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageMetadata.

        镜像ID。

        :param image_id: The image_id of this ImageMetadata.
        :type: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        """Gets the image_name of this ImageMetadata.

        镜像名称。

        :return: The image_name of this ImageMetadata.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ImageMetadata.

        镜像名称。

        :param image_name: The image_name of this ImageMetadata.
        :type: str
        """
        self._image_name = image_name

    @property
    def image_source_type(self):
        """Gets the image_source_type of this ImageMetadata.

        镜像后端存储类型。

        :return: The image_source_type of this ImageMetadata.
        :rtype: str
        """
        return self._image_source_type

    @image_source_type.setter
    def image_source_type(self, image_source_type):
        """Sets the image_source_type of this ImageMetadata.

        镜像后端存储类型。

        :param image_source_type: The image_source_type of this ImageMetadata.
        :type: str
        """
        self._image_source_type = image_source_type

    @property
    def imagetype(self):
        """Gets the imagetype of this ImageMetadata.

        镜像类型。

        :return: The imagetype of this ImageMetadata.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        """Sets the imagetype of this ImageMetadata.

        镜像类型。

        :param imagetype: The imagetype of this ImageMetadata.
        :type: str
        """
        self._imagetype = imagetype

    @property
    def isregistered(self):
        """Gets the isregistered of this ImageMetadata.

        是否是注册过的镜像，取值为 “true”或者“false”。

        :return: The isregistered of this ImageMetadata.
        :rtype: str
        """
        return self._isregistered

    @isregistered.setter
    def isregistered(self, isregistered):
        """Sets the isregistered of this ImageMetadata.

        是否是注册过的镜像，取值为 “true”或者“false”。

        :param isregistered: The isregistered of this ImageMetadata.
        :type: str
        """
        self._isregistered = isregistered

    @property
    def min_disk(self):
        """Gets the min_disk of this ImageMetadata.

        镜像运行最小磁盘空间，单位为 GB。

        :return: The min_disk of this ImageMetadata.
        :rtype: str
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this ImageMetadata.

        镜像运行最小磁盘空间，单位为 GB。

        :param min_disk: The min_disk of this ImageMetadata.
        :type: str
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        """Gets the min_ram of this ImageMetadata.

        镜像运行最小内存，单位为MB。

        :return: The min_ram of this ImageMetadata.
        :rtype: str
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this ImageMetadata.

        镜像运行最小内存，单位为MB。

        :param min_ram: The min_ram of this ImageMetadata.
        :type: str
        """
        self._min_ram = min_ram

    @property
    def os_bit(self):
        """Gets the os_bit of this ImageMetadata.

        操作系统位数，一般取值为“32” 或者“64”。

        :return: The os_bit of this ImageMetadata.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        """Sets the os_bit of this ImageMetadata.

        操作系统位数，一般取值为“32” 或者“64”。

        :param os_bit: The os_bit of this ImageMetadata.
        :type: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        """Gets the os_type of this ImageMetadata.

        操作系统类型，目前取值Linux， Windows，Other。

        :return: The os_type of this ImageMetadata.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ImageMetadata.

        操作系统类型，目前取值Linux， Windows，Other。

        :param os_type: The os_type of this ImageMetadata.
        :type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        """Gets the os_version of this ImageMetadata.

        操作系统具体版本。

        :return: The os_version of this ImageMetadata.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this ImageMetadata.

        操作系统具体版本。

        :param os_version: The os_version of this ImageMetadata.
        :type: str
        """
        self._os_version = os_version

    @property
    def platform(self):
        """Gets the platform of this ImageMetadata.

        镜像平台分类，取值为Windows， Ubuntu，RedHat，SUSE， CentOS，Other。

        :return: The platform of this ImageMetadata.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ImageMetadata.

        镜像平台分类，取值为Windows， Ubuntu，RedHat，SUSE， CentOS，Other。

        :param platform: The platform of this ImageMetadata.
        :type: str
        """
        self._platform = platform

    @property
    def size(self):
        """Gets the size of this ImageMetadata.

        预留属性。

        :return: The size of this ImageMetadata.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImageMetadata.

        预留属性。

        :param size: The size of this ImageMetadata.
        :type: str
        """
        self._size = size

    @property
    def virtual_env_type(self):
        """Gets the virtual_env_type of this ImageMetadata.

        镜像使用环境类型。

        :return: The virtual_env_type of this ImageMetadata.
        :rtype: str
        """
        return self._virtual_env_type

    @virtual_env_type.setter
    def virtual_env_type(self, virtual_env_type):
        """Sets the virtual_env_type of this ImageMetadata.

        镜像使用环境类型。

        :param virtual_env_type: The virtual_env_type of this ImageMetadata.
        :type: str
        """
        self._virtual_env_type = virtual_env_type

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
        if not isinstance(other, ImageMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
