# coding: utf-8

import pprint
import re

import six





class Image:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'container_format': 'str',
        'disk_format': 'str',
        'display_description': 'str',
        'id': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'size': 'int',
        'status': 'str',
        'updated_at': 'str',
        'volume_type': 'VolumeType'
    }

    attribute_map = {
        'container_format': 'container_format',
        'disk_format': 'disk_format',
        'display_description': 'display_description',
        'id': 'id',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'size': 'size',
        'status': 'status',
        'updated_at': 'updated_at',
        'volume_type': 'volume_type'
    }

    def __init__(self, container_format=None, disk_format=None, display_description=None, id=None, image_id=None, image_name=None, size=None, status=None, updated_at=None, volume_type=None):
        """Image - a model defined in huaweicloud sdk"""
        
        

        self._container_format = None
        self._disk_format = None
        self._display_description = None
        self._id = None
        self._image_id = None
        self._image_name = None
        self._size = None
        self._status = None
        self._updated_at = None
        self._volume_type = None
        self.discriminator = None

        if container_format is not None:
            self.container_format = container_format
        if disk_format is not None:
            self.disk_format = disk_format
        if display_description is not None:
            self.display_description = display_description
        self.id = id
        self.image_id = image_id
        self.image_name = image_name
        self.size = size
        self.status = status
        self.updated_at = updated_at
        if volume_type is not None:
            self.volume_type = volume_type

    @property
    def container_format(self):
        """Gets the container_format of this Image.

        云硬盘导出镜像的容器类型。  目前支持ami、ari、aki、ovf、bare。默认是bare。

        :return: The container_format of this Image.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        """Sets the container_format of this Image.

        云硬盘导出镜像的容器类型。  目前支持ami、ari、aki、ovf、bare。默认是bare。

        :param container_format: The container_format of this Image.
        :type: str
        """
        self._container_format = container_format

    @property
    def disk_format(self):
        """Gets the disk_format of this Image.

        云硬盘导出镜像的格式。  目前支持vhd、zvhd、zvhd2、raw、qcow2。默认是vhd。

        :return: The disk_format of this Image.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        """Sets the disk_format of this Image.

        云硬盘导出镜像的格式。  目前支持vhd、zvhd、zvhd2、raw、qcow2。默认是vhd。

        :param disk_format: The disk_format of this Image.
        :type: str
        """
        self._disk_format = disk_format

    @property
    def display_description(self):
        """Gets the display_description of this Image.

        云硬盘描述信息。

        :return: The display_description of this Image.
        :rtype: str
        """
        return self._display_description

    @display_description.setter
    def display_description(self, display_description):
        """Sets the display_description of this Image.

        云硬盘描述信息。

        :param display_description: The display_description of this Image.
        :type: str
        """
        self._display_description = display_description

    @property
    def id(self):
        """Gets the id of this Image.

        云硬盘ID。

        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Image.

        云硬盘ID。

        :param id: The id of this Image.
        :type: str
        """
        self._id = id

    @property
    def image_id(self):
        """Gets the image_id of this Image.

        云硬盘导出镜像的ID。

        :return: The image_id of this Image.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this Image.

        云硬盘导出镜像的ID。

        :param image_id: The image_id of this Image.
        :type: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        """Gets the image_name of this Image.

        云硬盘导出镜像的名称

        :return: The image_name of this Image.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this Image.

        云硬盘导出镜像的名称

        :param image_name: The image_name of this Image.
        :type: str
        """
        self._image_name = image_name

    @property
    def size(self):
        """Gets the size of this Image.

        云硬盘容量。

        :return: The size of this Image.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Image.

        云硬盘容量。

        :param size: The size of this Image.
        :type: int
        """
        self._size = size

    @property
    def status(self):
        """Gets the status of this Image.

        云硬盘导出镜像后的状态，正常值为 “uploading”。

        :return: The status of this Image.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Image.

        云硬盘导出镜像后的状态，正常值为 “uploading”。

        :param status: The status of this Image.
        :type: str
        """
        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this Image.

        云硬盘更新时间。  时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The updated_at of this Image.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Image.

        云硬盘更新时间。  时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param updated_at: The updated_at of this Image.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def volume_type(self):
        """Gets the volume_type of this Image.


        :return: The volume_type of this Image.
        :rtype: VolumeType
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this Image.


        :param volume_type: The volume_type of this Image.
        :type: VolumeType
        """
        self._volume_type = volume_type

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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
