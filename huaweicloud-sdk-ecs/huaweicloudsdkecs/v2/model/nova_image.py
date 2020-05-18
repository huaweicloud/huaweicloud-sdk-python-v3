# coding: utf-8

import pprint
import re

import six


class NovaImage(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'id': 'str',
        'links': 'list[NovaLink]',
        'name': 'str',
        'metadata': 'dict(str, str)',
        'os_ext_img_siz_esize': 'int',
        'min_disk': 'int',
        'min_ram': 'int',
        'progress': 'int',
        'status': 'str',
        'created': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'name': 'name',
        'metadata': 'metadata',
        'os_ext_img_siz_esize': 'OS-EXT-IMG-SIZE:size',
        'min_disk': 'minDisk',
        'min_ram': 'minRam',
        'progress': 'progress',
        'status': 'status',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, links=None, name=None, metadata=None, os_ext_img_siz_esize=None, min_disk=None, min_ram=None, progress=None, status=None, created=None, updated=None):  # noqa: E501
        """NovaImage - a model defined in huaweicloud sdk"""

        self._id = None
        self._links = None
        self._name = None
        self._metadata = None
        self._os_ext_img_siz_esize = None
        self._min_disk = None
        self._min_ram = None
        self._progress = None
        self._status = None
        self._created = None
        self._updated = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.name = name
        self.metadata = metadata
        self.os_ext_img_siz_esize = os_ext_img_siz_esize
        self.min_disk = min_disk
        self.min_ram = min_ram
        self.progress = progress
        self.status = status
        self.created = created
        self.updated = updated

    @property
    def id(self):
        """Gets the id of this NovaImage.

        镜像ID

        :return: The id of this NovaImage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaImage.

        镜像ID

        :param id: The id of this NovaImage.
        :type: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this NovaImage.

        镜像相关快捷链接地址

        :return: The links of this NovaImage.
        :rtype: list[NovaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NovaImage.

        镜像相关快捷链接地址

        :param links: The links of this NovaImage.
        :type: list[NovaLink]
        """
        self._links = links

    @property
    def name(self):
        """Gets the name of this NovaImage.

        镜像名称

        :return: The name of this NovaImage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaImage.

        镜像名称

        :param name: The name of this NovaImage.
        :type: str
        """
        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this NovaImage.

        metadata键值对

        :return: The metadata of this NovaImage.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NovaImage.

        metadata键值对

        :param metadata: The metadata of this NovaImage.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def os_ext_img_siz_esize(self):
        """Gets the os_ext_img_siz_esize of this NovaImage.

        镜像大小。 大于0。

        :return: The os_ext_img_siz_esize of this NovaImage.
        :rtype: int
        """
        return self._os_ext_img_siz_esize

    @os_ext_img_siz_esize.setter
    def os_ext_img_siz_esize(self, os_ext_img_siz_esize):
        """Sets the os_ext_img_siz_esize of this NovaImage.

        镜像大小。 大于0。

        :param os_ext_img_siz_esize: The os_ext_img_siz_esize of this NovaImage.
        :type: int
        """
        self._os_ext_img_siz_esize = os_ext_img_siz_esize

    @property
    def min_disk(self):
        """Gets the min_disk of this NovaImage.

        镜像要求的最小磁盘大小。 大于0。

        :return: The min_disk of this NovaImage.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this NovaImage.

        镜像要求的最小磁盘大小。 大于0。

        :param min_disk: The min_disk of this NovaImage.
        :type: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        """Gets the min_ram of this NovaImage.

        镜像要求的最小内存大小。 大于0。

        :return: The min_ram of this NovaImage.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this NovaImage.

        镜像要求的最小内存大小。 大于0。

        :param min_ram: The min_ram of this NovaImage.
        :type: int
        """
        self._min_ram = min_ram

    @property
    def progress(self):
        """Gets the progress of this NovaImage.

        镜像上传百分比。 大于0。

        :return: The progress of this NovaImage.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this NovaImage.

        镜像上传百分比。 大于0。

        :param progress: The progress of this NovaImage.
        :type: int
        """
        self._progress = progress

    @property
    def status(self):
        """Gets the status of this NovaImage.

        镜像状态

        :return: The status of this NovaImage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NovaImage.

        镜像状态

        :param status: The status of this NovaImage.
        :type: str
        """
        self._status = status

    @property
    def created(self):
        """Gets the created of this NovaImage.

        镜像创建时间。 ISO8601时间格式，例如：2013-06-09T06:42:18Z

        :return: The created of this NovaImage.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NovaImage.

        镜像创建时间。 ISO8601时间格式，例如：2013-06-09T06:42:18Z

        :param created: The created of this NovaImage.
        :type: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this NovaImage.

        镜像更新时间。 ISO8601时间格式，例如：2013-06-09T06:42:18Z

        :return: The updated of this NovaImage.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this NovaImage.

        镜像更新时间。 ISO8601时间格式，例如：2013-06-09T06:42:18Z

        :param updated: The updated of this NovaImage.
        :type: str
        """
        self._updated = updated

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
        if not isinstance(other, NovaImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
