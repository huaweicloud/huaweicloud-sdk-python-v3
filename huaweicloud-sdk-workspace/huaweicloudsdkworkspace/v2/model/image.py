# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'image_id': 'str',
        'min_disk': 'int',
        'created_at': 'str',
        'image_size': 'str',
        'updated_at': 'str',
        'product_code': 'str',
        'max_ram': 'str',
        'market_resource_type_code': 'str',
        'min_ram': 'int',
        'os_type': 'str',
        'image_type': 'str',
        'tags': 'list[str]',
        'platform': 'str',
        'os_bit': 'str',
        'os_version': 'str',
        'name': 'str',
        'market_service_type_code': 'str',
        'status': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'min_disk': 'min_disk',
        'created_at': 'created_at',
        'image_size': 'image_size',
        'updated_at': 'updated_at',
        'product_code': 'product_code',
        'max_ram': 'max_ram',
        'market_resource_type_code': 'market_resource_type_code',
        'min_ram': 'min_ram',
        'os_type': 'os_type',
        'image_type': 'image_type',
        'tags': 'tags',
        'platform': 'platform',
        'os_bit': 'os_bit',
        'os_version': 'os_version',
        'name': 'name',
        'market_service_type_code': 'market_service_type_code',
        'status': 'status'
    }

    def __init__(self, image_id=None, min_disk=None, created_at=None, image_size=None, updated_at=None, product_code=None, max_ram=None, market_resource_type_code=None, min_ram=None, os_type=None, image_type=None, tags=None, platform=None, os_bit=None, os_version=None, name=None, market_service_type_code=None, status=None):
        r"""Image

        The model defined in huaweicloud sdk

        :param image_id: 镜像id。
        :type image_id: str
        :param min_disk: 镜像运行需要的最小磁盘容量，单位为GB。取值为40～1024GB。
        :type min_disk: int
        :param created_at: 创建时间，格式为UTC时间，yyyy-MM-ddTHH:mm:ssZ。
        :type created_at: str
        :param image_size: 镜像文件的大小，单位为字节。
        :type image_size: str
        :param updated_at: 更新时间，格式为UTC时间，yyyy-MM-ddTHH:mm:ssZ。
        :type updated_at: str
        :param product_code: 市场镜像的产品ID。
        :type product_code: str
        :param max_ram: 镜像支持的最大内存，单位为MB。取值可以参考云服务器规格限制，一般不设置。
        :type max_ram: str
        :param market_resource_type_code: 云市场资源类型编码。
        :type market_resource_type_code: str
        :param min_ram: 镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，默认设置为0。
        :type min_ram: int
        :param os_type: 操作系统类型，目前取值Linux， Windows，Other。
        :type os_type: str
        :param image_type: 镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private 共享镜像：shared。
        :type image_type: str
        :param tags: 镜像标签列表。
        :type tags: list[str]
        :param platform: 镜像平台分类。
        :type platform: str
        :param os_bit: 操作系统位数，一般取值为“32”或者“64”。
        :type os_bit: str
        :param os_version: 操作系统具体版本。
        :type os_version: str
        :param name: 镜像名称。
        :type name: str
        :param market_service_type_code: 云市场服务类型编码。
        :type market_service_type_code: str
        :param status: 镜像状态。
        :type status: str
        """
        
        

        self._image_id = None
        self._min_disk = None
        self._created_at = None
        self._image_size = None
        self._updated_at = None
        self._product_code = None
        self._max_ram = None
        self._market_resource_type_code = None
        self._min_ram = None
        self._os_type = None
        self._image_type = None
        self._tags = None
        self._platform = None
        self._os_bit = None
        self._os_version = None
        self._name = None
        self._market_service_type_code = None
        self._status = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if min_disk is not None:
            self.min_disk = min_disk
        if created_at is not None:
            self.created_at = created_at
        if image_size is not None:
            self.image_size = image_size
        if updated_at is not None:
            self.updated_at = updated_at
        if product_code is not None:
            self.product_code = product_code
        if max_ram is not None:
            self.max_ram = max_ram
        if market_resource_type_code is not None:
            self.market_resource_type_code = market_resource_type_code
        if min_ram is not None:
            self.min_ram = min_ram
        if os_type is not None:
            self.os_type = os_type
        if image_type is not None:
            self.image_type = image_type
        if tags is not None:
            self.tags = tags
        if platform is not None:
            self.platform = platform
        if os_bit is not None:
            self.os_bit = os_bit
        if os_version is not None:
            self.os_version = os_version
        if name is not None:
            self.name = name
        if market_service_type_code is not None:
            self.market_service_type_code = market_service_type_code
        if status is not None:
            self.status = status

    @property
    def image_id(self):
        r"""Gets the image_id of this Image.

        镜像id。

        :return: The image_id of this Image.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this Image.

        镜像id。

        :param image_id: The image_id of this Image.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def min_disk(self):
        r"""Gets the min_disk of this Image.

        镜像运行需要的最小磁盘容量，单位为GB。取值为40～1024GB。

        :return: The min_disk of this Image.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        r"""Sets the min_disk of this Image.

        镜像运行需要的最小磁盘容量，单位为GB。取值为40～1024GB。

        :param min_disk: The min_disk of this Image.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def created_at(self):
        r"""Gets the created_at of this Image.

        创建时间，格式为UTC时间，yyyy-MM-ddTHH:mm:ssZ。

        :return: The created_at of this Image.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Image.

        创建时间，格式为UTC时间，yyyy-MM-ddTHH:mm:ssZ。

        :param created_at: The created_at of this Image.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def image_size(self):
        r"""Gets the image_size of this Image.

        镜像文件的大小，单位为字节。

        :return: The image_size of this Image.
        :rtype: str
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this Image.

        镜像文件的大小，单位为字节。

        :param image_size: The image_size of this Image.
        :type image_size: str
        """
        self._image_size = image_size

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Image.

        更新时间，格式为UTC时间，yyyy-MM-ddTHH:mm:ssZ。

        :return: The updated_at of this Image.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Image.

        更新时间，格式为UTC时间，yyyy-MM-ddTHH:mm:ssZ。

        :param updated_at: The updated_at of this Image.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def product_code(self):
        r"""Gets the product_code of this Image.

        市场镜像的产品ID。

        :return: The product_code of this Image.
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        r"""Sets the product_code of this Image.

        市场镜像的产品ID。

        :param product_code: The product_code of this Image.
        :type product_code: str
        """
        self._product_code = product_code

    @property
    def max_ram(self):
        r"""Gets the max_ram of this Image.

        镜像支持的最大内存，单位为MB。取值可以参考云服务器规格限制，一般不设置。

        :return: The max_ram of this Image.
        :rtype: str
        """
        return self._max_ram

    @max_ram.setter
    def max_ram(self, max_ram):
        r"""Sets the max_ram of this Image.

        镜像支持的最大内存，单位为MB。取值可以参考云服务器规格限制，一般不设置。

        :param max_ram: The max_ram of this Image.
        :type max_ram: str
        """
        self._max_ram = max_ram

    @property
    def market_resource_type_code(self):
        r"""Gets the market_resource_type_code of this Image.

        云市场资源类型编码。

        :return: The market_resource_type_code of this Image.
        :rtype: str
        """
        return self._market_resource_type_code

    @market_resource_type_code.setter
    def market_resource_type_code(self, market_resource_type_code):
        r"""Sets the market_resource_type_code of this Image.

        云市场资源类型编码。

        :param market_resource_type_code: The market_resource_type_code of this Image.
        :type market_resource_type_code: str
        """
        self._market_resource_type_code = market_resource_type_code

    @property
    def min_ram(self):
        r"""Gets the min_ram of this Image.

        镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，默认设置为0。

        :return: The min_ram of this Image.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        r"""Sets the min_ram of this Image.

        镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，默认设置为0。

        :param min_ram: The min_ram of this Image.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def os_type(self):
        r"""Gets the os_type of this Image.

        操作系统类型，目前取值Linux， Windows，Other。

        :return: The os_type of this Image.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this Image.

        操作系统类型，目前取值Linux， Windows，Other。

        :param os_type: The os_type of this Image.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def image_type(self):
        r"""Gets the image_type of this Image.

        镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private 共享镜像：shared。

        :return: The image_type of this Image.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this Image.

        镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private 共享镜像：shared。

        :param image_type: The image_type of this Image.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def tags(self):
        r"""Gets the tags of this Image.

        镜像标签列表。

        :return: The tags of this Image.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Image.

        镜像标签列表。

        :param tags: The tags of this Image.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def platform(self):
        r"""Gets the platform of this Image.

        镜像平台分类。

        :return: The platform of this Image.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this Image.

        镜像平台分类。

        :param platform: The platform of this Image.
        :type platform: str
        """
        self._platform = platform

    @property
    def os_bit(self):
        r"""Gets the os_bit of this Image.

        操作系统位数，一般取值为“32”或者“64”。

        :return: The os_bit of this Image.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this Image.

        操作系统位数，一般取值为“32”或者“64”。

        :param os_bit: The os_bit of this Image.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_version(self):
        r"""Gets the os_version of this Image.

        操作系统具体版本。

        :return: The os_version of this Image.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this Image.

        操作系统具体版本。

        :param os_version: The os_version of this Image.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def name(self):
        r"""Gets the name of this Image.

        镜像名称。

        :return: The name of this Image.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Image.

        镜像名称。

        :param name: The name of this Image.
        :type name: str
        """
        self._name = name

    @property
    def market_service_type_code(self):
        r"""Gets the market_service_type_code of this Image.

        云市场服务类型编码。

        :return: The market_service_type_code of this Image.
        :rtype: str
        """
        return self._market_service_type_code

    @market_service_type_code.setter
    def market_service_type_code(self, market_service_type_code):
        r"""Sets the market_service_type_code of this Image.

        云市场服务类型编码。

        :param market_service_type_code: The market_service_type_code of this Image.
        :type market_service_type_code: str
        """
        self._market_service_type_code = market_service_type_code

    @property
    def status(self):
        r"""Gets the status of this Image.

        镜像状态。

        :return: The status of this Image.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Image.

        镜像状态。

        :param status: The status of this Image.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
