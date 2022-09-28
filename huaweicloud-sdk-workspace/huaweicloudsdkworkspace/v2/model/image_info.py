# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'image_type': 'str',
        'os_type': 'str',
        'os_version': 'str',
        'disk_format': 'str',
        'name': 'str',
        'min_ram': 'int',
        'min_disk': 'int',
        'product_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'image_type': 'image_type',
        'os_type': 'os_type',
        'os_version': 'os_version',
        'disk_format': 'disk_format',
        'name': 'name',
        'min_ram': 'min_ram',
        'min_disk': 'min_disk',
        'product_code': 'product_code'
    }

    def __init__(self, id=None, image_type=None, os_type=None, os_version=None, disk_format=None, name=None, min_ram=None, min_disk=None, product_code=None):
        """ImageInfo

        The model defined in huaweicloud sdk

        :param id: 镜像ID。
        :type id: str
        :param image_type: 镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private。
        :type image_type: str
        :param os_type: 操作系统类型，目前取值Linux， Windows，Other。
        :type os_type: str
        :param os_version: 操作系统具体版本。
        :type os_version: str
        :param disk_format: 镜像格式，目前支持vhd，raw，qcow2，zvhd2格式。
        :type disk_format: str
        :param name: 镜像名称。
        :type name: str
        :param min_ram: 镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，一般设置为0。
        :type min_ram: int
        :param min_disk: 镜像运行需要的最小磁盘，单位为GB 。取值为40～1024GB。
        :type min_disk: int
        :param product_code: 镜像的产品编码。
        :type product_code: str
        """
        
        

        self._id = None
        self._image_type = None
        self._os_type = None
        self._os_version = None
        self._disk_format = None
        self._name = None
        self._min_ram = None
        self._min_disk = None
        self._product_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if image_type is not None:
            self.image_type = image_type
        if os_type is not None:
            self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version
        if disk_format is not None:
            self.disk_format = disk_format
        if name is not None:
            self.name = name
        if min_ram is not None:
            self.min_ram = min_ram
        if min_disk is not None:
            self.min_disk = min_disk
        if product_code is not None:
            self.product_code = product_code

    @property
    def id(self):
        """Gets the id of this ImageInfo.

        镜像ID。

        :return: The id of this ImageInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageInfo.

        镜像ID。

        :param id: The id of this ImageInfo.
        :type id: str
        """
        self._id = id

    @property
    def image_type(self):
        """Gets the image_type of this ImageInfo.

        镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private。

        :return: The image_type of this ImageInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this ImageInfo.

        镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private。

        :param image_type: The image_type of this ImageInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def os_type(self):
        """Gets the os_type of this ImageInfo.

        操作系统类型，目前取值Linux， Windows，Other。

        :return: The os_type of this ImageInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ImageInfo.

        操作系统类型，目前取值Linux， Windows，Other。

        :param os_type: The os_type of this ImageInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        """Gets the os_version of this ImageInfo.

        操作系统具体版本。

        :return: The os_version of this ImageInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this ImageInfo.

        操作系统具体版本。

        :param os_version: The os_version of this ImageInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def disk_format(self):
        """Gets the disk_format of this ImageInfo.

        镜像格式，目前支持vhd，raw，qcow2，zvhd2格式。

        :return: The disk_format of this ImageInfo.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        """Sets the disk_format of this ImageInfo.

        镜像格式，目前支持vhd，raw，qcow2，zvhd2格式。

        :param disk_format: The disk_format of this ImageInfo.
        :type disk_format: str
        """
        self._disk_format = disk_format

    @property
    def name(self):
        """Gets the name of this ImageInfo.

        镜像名称。

        :return: The name of this ImageInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageInfo.

        镜像名称。

        :param name: The name of this ImageInfo.
        :type name: str
        """
        self._name = name

    @property
    def min_ram(self):
        """Gets the min_ram of this ImageInfo.

        镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，一般设置为0。

        :return: The min_ram of this ImageInfo.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this ImageInfo.

        镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，一般设置为0。

        :param min_ram: The min_ram of this ImageInfo.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def min_disk(self):
        """Gets the min_disk of this ImageInfo.

        镜像运行需要的最小磁盘，单位为GB 。取值为40～1024GB。

        :return: The min_disk of this ImageInfo.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this ImageInfo.

        镜像运行需要的最小磁盘，单位为GB 。取值为40～1024GB。

        :param min_disk: The min_disk of this ImageInfo.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def product_code(self):
        """Gets the product_code of this ImageInfo.

        镜像的产品编码。

        :return: The product_code of this ImageInfo.
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this ImageInfo.

        镜像的产品编码。

        :param product_code: The product_code of this ImageInfo.
        :type product_code: str
        """
        self._product_code = product_code

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
        if not isinstance(other, ImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
