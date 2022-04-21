# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlanceCreateImageMetadataRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'os_version': 'str',
        'container_format': 'str',
        'disk_format': 'str',
        'min_disk': 'int',
        'min_ram': 'int',
        'name': 'str',
        'protected': 'bool',
        'tags': 'list[str]',
        'visibility': 'str'
    }

    attribute_map = {
        'os_version': '__os_version',
        'container_format': 'container_format',
        'disk_format': 'disk_format',
        'min_disk': 'min_disk',
        'min_ram': 'min_ram',
        'name': 'name',
        'protected': 'protected',
        'tags': 'tags',
        'visibility': 'visibility'
    }

    def __init__(self, os_version=None, container_format=None, disk_format=None, min_disk=None, min_ram=None, name=None, protected=None, tags=None, visibility=None):
        """GlanceCreateImageMetadataRequestBody

        The model defined in huaweicloud sdk

        :param os_version: 镜像的操作系统具体版本,如果未指定__os_version，则默认设置为Other Linux(64 bit)，不保证该镜像能成功创建虚拟机以及通过该镜像创建的虚拟机能够正常使用。
        :type os_version: str
        :param container_format: 容器格式。默认取值为bare。
        :type container_format: str
        :param disk_format: 镜像文件格式。目前支持vhd，zvhd、zvhd2、raw，qcow2。默认取值为vhd
        :type disk_format: str
        :param min_disk: 镜像运行需要的最小磁盘，单位为GB 。必须大于镜像系统盘容量，否则创建云主机云服务器可能失败。
        :type min_disk: int
        :param min_ram: 镜像运行需要的最小内存，单位为MB。参数取值依据云主机云服务器的规格限制。默认取值为0。
        :type min_ram: int
        :param name: 镜像名称，如果未指定name的取值，则默认为空，但是使用该镜像创建虚拟机会失败。名称的长度为1-255位。
        :type name: str
        :param protected: 镜像是否被保护，保护后的镜像不可删除。默认取值为false。
        :type protected: bool
        :param tags: 镜像标签列表。长度为1-255位。默认为空。
        :type tags: list[str]
        :param visibility: 其他租户是否可见。默认取值为private。创建镜像元数据时，visibility取值只能为private。
        :type visibility: str
        """
        
        

        self._os_version = None
        self._container_format = None
        self._disk_format = None
        self._min_disk = None
        self._min_ram = None
        self._name = None
        self._protected = None
        self._tags = None
        self._visibility = None
        self.discriminator = None

        if os_version is not None:
            self.os_version = os_version
        if container_format is not None:
            self.container_format = container_format
        if disk_format is not None:
            self.disk_format = disk_format
        if min_disk is not None:
            self.min_disk = min_disk
        if min_ram is not None:
            self.min_ram = min_ram
        if name is not None:
            self.name = name
        if protected is not None:
            self.protected = protected
        if tags is not None:
            self.tags = tags
        if visibility is not None:
            self.visibility = visibility

    @property
    def os_version(self):
        """Gets the os_version of this GlanceCreateImageMetadataRequestBody.

        镜像的操作系统具体版本,如果未指定__os_version，则默认设置为Other Linux(64 bit)，不保证该镜像能成功创建虚拟机以及通过该镜像创建的虚拟机能够正常使用。

        :return: The os_version of this GlanceCreateImageMetadataRequestBody.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this GlanceCreateImageMetadataRequestBody.

        镜像的操作系统具体版本,如果未指定__os_version，则默认设置为Other Linux(64 bit)，不保证该镜像能成功创建虚拟机以及通过该镜像创建的虚拟机能够正常使用。

        :param os_version: The os_version of this GlanceCreateImageMetadataRequestBody.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def container_format(self):
        """Gets the container_format of this GlanceCreateImageMetadataRequestBody.

        容器格式。默认取值为bare。

        :return: The container_format of this GlanceCreateImageMetadataRequestBody.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        """Sets the container_format of this GlanceCreateImageMetadataRequestBody.

        容器格式。默认取值为bare。

        :param container_format: The container_format of this GlanceCreateImageMetadataRequestBody.
        :type container_format: str
        """
        self._container_format = container_format

    @property
    def disk_format(self):
        """Gets the disk_format of this GlanceCreateImageMetadataRequestBody.

        镜像文件格式。目前支持vhd，zvhd、zvhd2、raw，qcow2。默认取值为vhd

        :return: The disk_format of this GlanceCreateImageMetadataRequestBody.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        """Sets the disk_format of this GlanceCreateImageMetadataRequestBody.

        镜像文件格式。目前支持vhd，zvhd、zvhd2、raw，qcow2。默认取值为vhd

        :param disk_format: The disk_format of this GlanceCreateImageMetadataRequestBody.
        :type disk_format: str
        """
        self._disk_format = disk_format

    @property
    def min_disk(self):
        """Gets the min_disk of this GlanceCreateImageMetadataRequestBody.

        镜像运行需要的最小磁盘，单位为GB 。必须大于镜像系统盘容量，否则创建云主机云服务器可能失败。

        :return: The min_disk of this GlanceCreateImageMetadataRequestBody.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this GlanceCreateImageMetadataRequestBody.

        镜像运行需要的最小磁盘，单位为GB 。必须大于镜像系统盘容量，否则创建云主机云服务器可能失败。

        :param min_disk: The min_disk of this GlanceCreateImageMetadataRequestBody.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        """Gets the min_ram of this GlanceCreateImageMetadataRequestBody.

        镜像运行需要的最小内存，单位为MB。参数取值依据云主机云服务器的规格限制。默认取值为0。

        :return: The min_ram of this GlanceCreateImageMetadataRequestBody.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this GlanceCreateImageMetadataRequestBody.

        镜像运行需要的最小内存，单位为MB。参数取值依据云主机云服务器的规格限制。默认取值为0。

        :param min_ram: The min_ram of this GlanceCreateImageMetadataRequestBody.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def name(self):
        """Gets the name of this GlanceCreateImageMetadataRequestBody.

        镜像名称，如果未指定name的取值，则默认为空，但是使用该镜像创建虚拟机会失败。名称的长度为1-255位。

        :return: The name of this GlanceCreateImageMetadataRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlanceCreateImageMetadataRequestBody.

        镜像名称，如果未指定name的取值，则默认为空，但是使用该镜像创建虚拟机会失败。名称的长度为1-255位。

        :param name: The name of this GlanceCreateImageMetadataRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def protected(self):
        """Gets the protected of this GlanceCreateImageMetadataRequestBody.

        镜像是否被保护，保护后的镜像不可删除。默认取值为false。

        :return: The protected of this GlanceCreateImageMetadataRequestBody.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this GlanceCreateImageMetadataRequestBody.

        镜像是否被保护，保护后的镜像不可删除。默认取值为false。

        :param protected: The protected of this GlanceCreateImageMetadataRequestBody.
        :type protected: bool
        """
        self._protected = protected

    @property
    def tags(self):
        """Gets the tags of this GlanceCreateImageMetadataRequestBody.

        镜像标签列表。长度为1-255位。默认为空。

        :return: The tags of this GlanceCreateImageMetadataRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GlanceCreateImageMetadataRequestBody.

        镜像标签列表。长度为1-255位。默认为空。

        :param tags: The tags of this GlanceCreateImageMetadataRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def visibility(self):
        """Gets the visibility of this GlanceCreateImageMetadataRequestBody.

        其他租户是否可见。默认取值为private。创建镜像元数据时，visibility取值只能为private。

        :return: The visibility of this GlanceCreateImageMetadataRequestBody.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this GlanceCreateImageMetadataRequestBody.

        其他租户是否可见。默认取值为private。创建镜像元数据时，visibility取值只能为private。

        :param visibility: The visibility of this GlanceCreateImageMetadataRequestBody.
        :type visibility: str
        """
        self._visibility = visibility

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
        if not isinstance(other, GlanceCreateImageMetadataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
