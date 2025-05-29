# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateImageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_images': 'list[CreateDataImage]',
        'description': 'str',
        'enterprise_project_id': 'str',
        'image_tags': 'list[TagKeyValue]',
        'instance_id': 'str',
        'name': 'str',
        'tags': 'list[str]',
        'max_ram': 'int',
        'min_ram': 'int',
        'os_version': 'str',
        'image_url': 'str',
        'min_disk': 'int',
        'is_config': 'bool',
        'cmk_id': 'str',
        'type': 'str',
        'is_quick_import': 'bool',
        'architecture': 'str',
        'volume_id': 'str',
        'hw_firmware_type': 'str'
    }

    attribute_map = {
        'data_images': 'data_images',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'image_tags': 'image_tags',
        'instance_id': 'instance_id',
        'name': 'name',
        'tags': 'tags',
        'max_ram': 'max_ram',
        'min_ram': 'min_ram',
        'os_version': 'os_version',
        'image_url': 'image_url',
        'min_disk': 'min_disk',
        'is_config': 'is_config',
        'cmk_id': 'cmk_id',
        'type': 'type',
        'is_quick_import': 'is_quick_import',
        'architecture': 'architecture',
        'volume_id': 'volume_id',
        'hw_firmware_type': 'hw_firmware_type'
    }

    def __init__(self, data_images=None, description=None, enterprise_project_id=None, image_tags=None, instance_id=None, name=None, tags=None, max_ram=None, min_ram=None, os_version=None, image_url=None, min_disk=None, is_config=None, cmk_id=None, type=None, is_quick_import=None, architecture=None, volume_id=None, hw_firmware_type=None):
        r"""CreateImageRequestBody

        The model defined in huaweicloud sdk

        :param data_images: 需要转换的数据盘信息，其中，当使用云服务器上的数据盘进行私有数据盘镜像创建时，该字段必选。 如果不是用于制作数据盘镜像，该字段默认为空。
        :type data_images: list[:class:`huaweicloudsdkims.v2.CreateDataImage`]
        :param description: 镜像描述信息。支持字母、数字、中文等，不支持回车、&lt;、 &gt;，长度不能超过1024个字符。默认为空。
        :type description: str
        :param enterprise_project_id: 表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目。取值为UUID，表示属于该UUID对应的企业项目。
        :type enterprise_project_id: str
        :param image_tags: 新规范的镜像标签列表。默认为空。tags和image_tags只能使用一个。
        :type image_tags: list[:class:`huaweicloudsdkims.v2.TagKeyValue`]
        :param instance_id: 需要转换的云服务器ID。使用instance_id字段，从云服务器制作私有镜像时，该字段填写云服务器ID。
        :type instance_id: str
        :param name: 镜像名称
        :type name: str
        :param tags: 镜像标签列表。默认为空。tags和image_tags只能使用一个。
        :type tags: list[str]
        :param max_ram: 表示镜像支持的最大内存，单位为MB。
        :type max_ram: int
        :param min_ram: 表示镜像支持的最小内存，单位为MB，默认为0，表示不受限制。
        :type min_ram: int
        :param os_version: 操作系统版本。 使用上传至OBS桶中的外部镜像文件制作镜像时生效。 当“is_quick_import”的值为“true”时，即使用镜像文件快速导入方式导入系统盘镜像，则该参数为必填参数。
        :type os_version: str
        :param image_url: OBS桶中外部镜像文件地址。 在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。格式为&lt;OBS桶名&gt;:&lt;OBS镜像文件名称&gt;。
        :type image_url: str
        :param min_disk: 最小系统盘大小。 在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。取值为40～1024GB。
        :type min_disk: int
        :param is_config: 是否自动配置。 取值为true或false。 如果需要后台自动配置，取值为true，否则为false。默认取值为false。
        :type is_config: bool
        :param cmk_id: 创建加密镜像的用户主密钥，具体取值请参考《密钥管理服务用户指南》获取。
        :type cmk_id: str
        :param type: 镜像的类型。 取值为ECS、BMS、FusionCompute、Ironic。默认使用“ECS”。 ECS/FusionCompute：表示是ECS服务器的镜像。 BMS/Ironic：表示是BMS服务器的镜像。
        :type type: str
        :param is_quick_import: 是否使用镜像文件快速导入方式，导入系统盘镜像。 是，配置为true。 否，配置为false。 关于镜像文件快速导入的约束与限制请参见镜像文件快速导入。
        :type is_quick_import: bool
        :param architecture: 镜像的架构类型。取值包括： x86 arm 默认使用“x86”。 当架构类型为arm时，镜像引导方式将自动转为UEFI的引导方式。
        :type architecture: str
        :param volume_id: 数据盘的卷ID。当数据盘创建系统盘镜像时，该参数必选
        :type volume_id: str
        :param hw_firmware_type: 云主机云服务器的启动方式。目前支持： bios：表示bios引导启动。 uefi：表示uefi引导启动。
        :type hw_firmware_type: str
        """
        
        

        self._data_images = None
        self._description = None
        self._enterprise_project_id = None
        self._image_tags = None
        self._instance_id = None
        self._name = None
        self._tags = None
        self._max_ram = None
        self._min_ram = None
        self._os_version = None
        self._image_url = None
        self._min_disk = None
        self._is_config = None
        self._cmk_id = None
        self._type = None
        self._is_quick_import = None
        self._architecture = None
        self._volume_id = None
        self._hw_firmware_type = None
        self.discriminator = None

        if data_images is not None:
            self.data_images = data_images
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if image_tags is not None:
            self.image_tags = image_tags
        if instance_id is not None:
            self.instance_id = instance_id
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if max_ram is not None:
            self.max_ram = max_ram
        if min_ram is not None:
            self.min_ram = min_ram
        if os_version is not None:
            self.os_version = os_version
        if image_url is not None:
            self.image_url = image_url
        if min_disk is not None:
            self.min_disk = min_disk
        if is_config is not None:
            self.is_config = is_config
        if cmk_id is not None:
            self.cmk_id = cmk_id
        if type is not None:
            self.type = type
        if is_quick_import is not None:
            self.is_quick_import = is_quick_import
        if architecture is not None:
            self.architecture = architecture
        if volume_id is not None:
            self.volume_id = volume_id
        if hw_firmware_type is not None:
            self.hw_firmware_type = hw_firmware_type

    @property
    def data_images(self):
        r"""Gets the data_images of this CreateImageRequestBody.

        需要转换的数据盘信息，其中，当使用云服务器上的数据盘进行私有数据盘镜像创建时，该字段必选。 如果不是用于制作数据盘镜像，该字段默认为空。

        :return: The data_images of this CreateImageRequestBody.
        :rtype: list[:class:`huaweicloudsdkims.v2.CreateDataImage`]
        """
        return self._data_images

    @data_images.setter
    def data_images(self, data_images):
        r"""Sets the data_images of this CreateImageRequestBody.

        需要转换的数据盘信息，其中，当使用云服务器上的数据盘进行私有数据盘镜像创建时，该字段必选。 如果不是用于制作数据盘镜像，该字段默认为空。

        :param data_images: The data_images of this CreateImageRequestBody.
        :type data_images: list[:class:`huaweicloudsdkims.v2.CreateDataImage`]
        """
        self._data_images = data_images

    @property
    def description(self):
        r"""Gets the description of this CreateImageRequestBody.

        镜像描述信息。支持字母、数字、中文等，不支持回车、<、 >，长度不能超过1024个字符。默认为空。

        :return: The description of this CreateImageRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateImageRequestBody.

        镜像描述信息。支持字母、数字、中文等，不支持回车、<、 >，长度不能超过1024个字符。默认为空。

        :param description: The description of this CreateImageRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateImageRequestBody.

        表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目。取值为UUID，表示属于该UUID对应的企业项目。

        :return: The enterprise_project_id of this CreateImageRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateImageRequestBody.

        表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目。取值为UUID，表示属于该UUID对应的企业项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateImageRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_tags(self):
        r"""Gets the image_tags of this CreateImageRequestBody.

        新规范的镜像标签列表。默认为空。tags和image_tags只能使用一个。

        :return: The image_tags of this CreateImageRequestBody.
        :rtype: list[:class:`huaweicloudsdkims.v2.TagKeyValue`]
        """
        return self._image_tags

    @image_tags.setter
    def image_tags(self, image_tags):
        r"""Sets the image_tags of this CreateImageRequestBody.

        新规范的镜像标签列表。默认为空。tags和image_tags只能使用一个。

        :param image_tags: The image_tags of this CreateImageRequestBody.
        :type image_tags: list[:class:`huaweicloudsdkims.v2.TagKeyValue`]
        """
        self._image_tags = image_tags

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateImageRequestBody.

        需要转换的云服务器ID。使用instance_id字段，从云服务器制作私有镜像时，该字段填写云服务器ID。

        :return: The instance_id of this CreateImageRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateImageRequestBody.

        需要转换的云服务器ID。使用instance_id字段，从云服务器制作私有镜像时，该字段填写云服务器ID。

        :param instance_id: The instance_id of this CreateImageRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this CreateImageRequestBody.

        镜像名称

        :return: The name of this CreateImageRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateImageRequestBody.

        镜像名称

        :param name: The name of this CreateImageRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        r"""Gets the tags of this CreateImageRequestBody.

        镜像标签列表。默认为空。tags和image_tags只能使用一个。

        :return: The tags of this CreateImageRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateImageRequestBody.

        镜像标签列表。默认为空。tags和image_tags只能使用一个。

        :param tags: The tags of this CreateImageRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def max_ram(self):
        r"""Gets the max_ram of this CreateImageRequestBody.

        表示镜像支持的最大内存，单位为MB。

        :return: The max_ram of this CreateImageRequestBody.
        :rtype: int
        """
        return self._max_ram

    @max_ram.setter
    def max_ram(self, max_ram):
        r"""Sets the max_ram of this CreateImageRequestBody.

        表示镜像支持的最大内存，单位为MB。

        :param max_ram: The max_ram of this CreateImageRequestBody.
        :type max_ram: int
        """
        self._max_ram = max_ram

    @property
    def min_ram(self):
        r"""Gets the min_ram of this CreateImageRequestBody.

        表示镜像支持的最小内存，单位为MB，默认为0，表示不受限制。

        :return: The min_ram of this CreateImageRequestBody.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        r"""Sets the min_ram of this CreateImageRequestBody.

        表示镜像支持的最小内存，单位为MB，默认为0，表示不受限制。

        :param min_ram: The min_ram of this CreateImageRequestBody.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def os_version(self):
        r"""Gets the os_version of this CreateImageRequestBody.

        操作系统版本。 使用上传至OBS桶中的外部镜像文件制作镜像时生效。 当“is_quick_import”的值为“true”时，即使用镜像文件快速导入方式导入系统盘镜像，则该参数为必填参数。

        :return: The os_version of this CreateImageRequestBody.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this CreateImageRequestBody.

        操作系统版本。 使用上传至OBS桶中的外部镜像文件制作镜像时生效。 当“is_quick_import”的值为“true”时，即使用镜像文件快速导入方式导入系统盘镜像，则该参数为必填参数。

        :param os_version: The os_version of this CreateImageRequestBody.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def image_url(self):
        r"""Gets the image_url of this CreateImageRequestBody.

        OBS桶中外部镜像文件地址。 在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。格式为<OBS桶名>:<OBS镜像文件名称>。

        :return: The image_url of this CreateImageRequestBody.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this CreateImageRequestBody.

        OBS桶中外部镜像文件地址。 在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。格式为<OBS桶名>:<OBS镜像文件名称>。

        :param image_url: The image_url of this CreateImageRequestBody.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def min_disk(self):
        r"""Gets the min_disk of this CreateImageRequestBody.

        最小系统盘大小。 在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。取值为40～1024GB。

        :return: The min_disk of this CreateImageRequestBody.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        r"""Sets the min_disk of this CreateImageRequestBody.

        最小系统盘大小。 在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。取值为40～1024GB。

        :param min_disk: The min_disk of this CreateImageRequestBody.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def is_config(self):
        r"""Gets the is_config of this CreateImageRequestBody.

        是否自动配置。 取值为true或false。 如果需要后台自动配置，取值为true，否则为false。默认取值为false。

        :return: The is_config of this CreateImageRequestBody.
        :rtype: bool
        """
        return self._is_config

    @is_config.setter
    def is_config(self, is_config):
        r"""Sets the is_config of this CreateImageRequestBody.

        是否自动配置。 取值为true或false。 如果需要后台自动配置，取值为true，否则为false。默认取值为false。

        :param is_config: The is_config of this CreateImageRequestBody.
        :type is_config: bool
        """
        self._is_config = is_config

    @property
    def cmk_id(self):
        r"""Gets the cmk_id of this CreateImageRequestBody.

        创建加密镜像的用户主密钥，具体取值请参考《密钥管理服务用户指南》获取。

        :return: The cmk_id of this CreateImageRequestBody.
        :rtype: str
        """
        return self._cmk_id

    @cmk_id.setter
    def cmk_id(self, cmk_id):
        r"""Sets the cmk_id of this CreateImageRequestBody.

        创建加密镜像的用户主密钥，具体取值请参考《密钥管理服务用户指南》获取。

        :param cmk_id: The cmk_id of this CreateImageRequestBody.
        :type cmk_id: str
        """
        self._cmk_id = cmk_id

    @property
    def type(self):
        r"""Gets the type of this CreateImageRequestBody.

        镜像的类型。 取值为ECS、BMS、FusionCompute、Ironic。默认使用“ECS”。 ECS/FusionCompute：表示是ECS服务器的镜像。 BMS/Ironic：表示是BMS服务器的镜像。

        :return: The type of this CreateImageRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateImageRequestBody.

        镜像的类型。 取值为ECS、BMS、FusionCompute、Ironic。默认使用“ECS”。 ECS/FusionCompute：表示是ECS服务器的镜像。 BMS/Ironic：表示是BMS服务器的镜像。

        :param type: The type of this CreateImageRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def is_quick_import(self):
        r"""Gets the is_quick_import of this CreateImageRequestBody.

        是否使用镜像文件快速导入方式，导入系统盘镜像。 是，配置为true。 否，配置为false。 关于镜像文件快速导入的约束与限制请参见镜像文件快速导入。

        :return: The is_quick_import of this CreateImageRequestBody.
        :rtype: bool
        """
        return self._is_quick_import

    @is_quick_import.setter
    def is_quick_import(self, is_quick_import):
        r"""Sets the is_quick_import of this CreateImageRequestBody.

        是否使用镜像文件快速导入方式，导入系统盘镜像。 是，配置为true。 否，配置为false。 关于镜像文件快速导入的约束与限制请参见镜像文件快速导入。

        :param is_quick_import: The is_quick_import of this CreateImageRequestBody.
        :type is_quick_import: bool
        """
        self._is_quick_import = is_quick_import

    @property
    def architecture(self):
        r"""Gets the architecture of this CreateImageRequestBody.

        镜像的架构类型。取值包括： x86 arm 默认使用“x86”。 当架构类型为arm时，镜像引导方式将自动转为UEFI的引导方式。

        :return: The architecture of this CreateImageRequestBody.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        r"""Sets the architecture of this CreateImageRequestBody.

        镜像的架构类型。取值包括： x86 arm 默认使用“x86”。 当架构类型为arm时，镜像引导方式将自动转为UEFI的引导方式。

        :param architecture: The architecture of this CreateImageRequestBody.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def volume_id(self):
        r"""Gets the volume_id of this CreateImageRequestBody.

        数据盘的卷ID。当数据盘创建系统盘镜像时，该参数必选

        :return: The volume_id of this CreateImageRequestBody.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this CreateImageRequestBody.

        数据盘的卷ID。当数据盘创建系统盘镜像时，该参数必选

        :param volume_id: The volume_id of this CreateImageRequestBody.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def hw_firmware_type(self):
        r"""Gets the hw_firmware_type of this CreateImageRequestBody.

        云主机云服务器的启动方式。目前支持： bios：表示bios引导启动。 uefi：表示uefi引导启动。

        :return: The hw_firmware_type of this CreateImageRequestBody.
        :rtype: str
        """
        return self._hw_firmware_type

    @hw_firmware_type.setter
    def hw_firmware_type(self, hw_firmware_type):
        r"""Sets the hw_firmware_type of this CreateImageRequestBody.

        云主机云服务器的启动方式。目前支持： bios：表示bios引导启动。 uefi：表示uefi引导启动。

        :param hw_firmware_type: The hw_firmware_type of this CreateImageRequestBody.
        :type hw_firmware_type: str
        """
        self._hw_firmware_type = hw_firmware_type

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
        if not isinstance(other, CreateImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
