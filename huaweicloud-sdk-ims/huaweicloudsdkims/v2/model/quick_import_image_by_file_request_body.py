# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuickImportImageByFileRequestBody:

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
        'description': 'str',
        'os_version': 'str',
        'image_url': 'str',
        'min_disk': 'int',
        'license_type': 'str',
        'tags': 'list[str]',
        'type': 'str',
        'enterprise_project_id': 'str',
        'architecture': 'str',
        'hw_firmware_type': 'str',
        'os_type': 'str',
        'image_tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'os_version': 'os_version',
        'image_url': 'image_url',
        'min_disk': 'min_disk',
        'license_type': 'license_type',
        'tags': 'tags',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'architecture': 'architecture',
        'hw_firmware_type': 'hw_firmware_type',
        'os_type': 'os_type',
        'image_tags': 'image_tags'
    }

    def __init__(self, name=None, description=None, os_version=None, image_url=None, min_disk=None, license_type=None, tags=None, type=None, enterprise_project_id=None, architecture=None, hw_firmware_type=None, os_type=None, image_tags=None):
        r"""QuickImportImageByFileRequestBody

        The model defined in huaweicloud sdk

        :param name: 镜像名称
        :type name: str
        :param description: 镜像描述信息。_description参数说明请参考镜像属性。支持字母、数字、中文等，不支持回车、&lt;、 &gt;，长度不能超过1024个字符。默认为空。
        :type description: str
        :param os_version: 操作系统版本。使用上传至OBS桶中的外部镜像文件制作镜像时生效
        :type os_version: str
        :param image_url: OBS桶中外部镜像文件地址。在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。格式为&lt;OBS桶名&gt;:&lt;OBS镜像文件名称&gt;。注意：此处的OBS桶和镜像文件的存储类别必须是OBS标准存储。
        :type image_url: str
        :param min_disk: 最小系统盘大小。在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。取值为1至1024GB。
        :type min_disk: int
        :param license_type: 操作系统使用的许可证类型。取值范围： platform：华为云官方许可证 byol：自带许可证（Bring Your Own License） 目前仅Windows操作系统支持设置该参数。
        :type license_type: str
        :param tags: 镜像标签列表。默认为空。 tags和image_tags只能使用一个。
        :type tags: list[str]
        :param type: 制作的镜像类型。系统盘镜像为ECS/BMS，数据盘镜像为DataImage. 制作数据盘镜像时该参数必选.
        :type type: str
        :param enterprise_project_id: 表示当前镜像所属的企业项目。 取值为0或无该值，表示属于default企业项目。 取值为UUID，表示属于该UUID对应的企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。
        :type enterprise_project_id: str
        :param architecture: 镜像的架构类型。取值包括： x86 arm 默认使用“x86”。
        :type architecture: str
        :param hw_firmware_type: 云主机云服务器的启动方式。目前支持： bios：表示bios引导启动。 uefi：表示uefi引导启动。
        :type hw_firmware_type: str
        :param os_type: 操作系统版本。 创建数据盘镜像时该参数取值为Linux或Windows，默认Linux。
        :type os_type: str
        :param image_tags: 新规范的镜像标签列表。默认为空。 tags和image_tags只能使用一个。
        :type image_tags: list[:class:`huaweicloudsdkims.v2.ResourceTag`]
        """
        
        

        self._name = None
        self._description = None
        self._os_version = None
        self._image_url = None
        self._min_disk = None
        self._license_type = None
        self._tags = None
        self._type = None
        self._enterprise_project_id = None
        self._architecture = None
        self._hw_firmware_type = None
        self._os_type = None
        self._image_tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.os_version = os_version
        self.image_url = image_url
        self.min_disk = min_disk
        if license_type is not None:
            self.license_type = license_type
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if architecture is not None:
            self.architecture = architecture
        if hw_firmware_type is not None:
            self.hw_firmware_type = hw_firmware_type
        if os_type is not None:
            self.os_type = os_type
        if image_tags is not None:
            self.image_tags = image_tags

    @property
    def name(self):
        r"""Gets the name of this QuickImportImageByFileRequestBody.

        镜像名称

        :return: The name of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QuickImportImageByFileRequestBody.

        镜像名称

        :param name: The name of this QuickImportImageByFileRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this QuickImportImageByFileRequestBody.

        镜像描述信息。_description参数说明请参考镜像属性。支持字母、数字、中文等，不支持回车、<、 >，长度不能超过1024个字符。默认为空。

        :return: The description of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this QuickImportImageByFileRequestBody.

        镜像描述信息。_description参数说明请参考镜像属性。支持字母、数字、中文等，不支持回车、<、 >，长度不能超过1024个字符。默认为空。

        :param description: The description of this QuickImportImageByFileRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def os_version(self):
        r"""Gets the os_version of this QuickImportImageByFileRequestBody.

        操作系统版本。使用上传至OBS桶中的外部镜像文件制作镜像时生效

        :return: The os_version of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this QuickImportImageByFileRequestBody.

        操作系统版本。使用上传至OBS桶中的外部镜像文件制作镜像时生效

        :param os_version: The os_version of this QuickImportImageByFileRequestBody.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def image_url(self):
        r"""Gets the image_url of this QuickImportImageByFileRequestBody.

        OBS桶中外部镜像文件地址。在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。格式为<OBS桶名>:<OBS镜像文件名称>。注意：此处的OBS桶和镜像文件的存储类别必须是OBS标准存储。

        :return: The image_url of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this QuickImportImageByFileRequestBody.

        OBS桶中外部镜像文件地址。在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。格式为<OBS桶名>:<OBS镜像文件名称>。注意：此处的OBS桶和镜像文件的存储类别必须是OBS标准存储。

        :param image_url: The image_url of this QuickImportImageByFileRequestBody.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def min_disk(self):
        r"""Gets the min_disk of this QuickImportImageByFileRequestBody.

        最小系统盘大小。在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。取值为1至1024GB。

        :return: The min_disk of this QuickImportImageByFileRequestBody.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        r"""Sets the min_disk of this QuickImportImageByFileRequestBody.

        最小系统盘大小。在使用OBS桶的外部镜像文件制作镜像时生效且为必选字段。取值为1至1024GB。

        :param min_disk: The min_disk of this QuickImportImageByFileRequestBody.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def license_type(self):
        r"""Gets the license_type of this QuickImportImageByFileRequestBody.

        操作系统使用的许可证类型。取值范围： platform：华为云官方许可证 byol：自带许可证（Bring Your Own License） 目前仅Windows操作系统支持设置该参数。

        :return: The license_type of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        r"""Sets the license_type of this QuickImportImageByFileRequestBody.

        操作系统使用的许可证类型。取值范围： platform：华为云官方许可证 byol：自带许可证（Bring Your Own License） 目前仅Windows操作系统支持设置该参数。

        :param license_type: The license_type of this QuickImportImageByFileRequestBody.
        :type license_type: str
        """
        self._license_type = license_type

    @property
    def tags(self):
        r"""Gets the tags of this QuickImportImageByFileRequestBody.

        镜像标签列表。默认为空。 tags和image_tags只能使用一个。

        :return: The tags of this QuickImportImageByFileRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this QuickImportImageByFileRequestBody.

        镜像标签列表。默认为空。 tags和image_tags只能使用一个。

        :param tags: The tags of this QuickImportImageByFileRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def type(self):
        r"""Gets the type of this QuickImportImageByFileRequestBody.

        制作的镜像类型。系统盘镜像为ECS/BMS，数据盘镜像为DataImage. 制作数据盘镜像时该参数必选.

        :return: The type of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this QuickImportImageByFileRequestBody.

        制作的镜像类型。系统盘镜像为ECS/BMS，数据盘镜像为DataImage. 制作数据盘镜像时该参数必选.

        :param type: The type of this QuickImportImageByFileRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this QuickImportImageByFileRequestBody.

        表示当前镜像所属的企业项目。 取值为0或无该值，表示属于default企业项目。 取值为UUID，表示属于该UUID对应的企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。

        :return: The enterprise_project_id of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this QuickImportImageByFileRequestBody.

        表示当前镜像所属的企业项目。 取值为0或无该值，表示属于default企业项目。 取值为UUID，表示属于该UUID对应的企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。

        :param enterprise_project_id: The enterprise_project_id of this QuickImportImageByFileRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def architecture(self):
        r"""Gets the architecture of this QuickImportImageByFileRequestBody.

        镜像的架构类型。取值包括： x86 arm 默认使用“x86”。

        :return: The architecture of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        r"""Sets the architecture of this QuickImportImageByFileRequestBody.

        镜像的架构类型。取值包括： x86 arm 默认使用“x86”。

        :param architecture: The architecture of this QuickImportImageByFileRequestBody.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def hw_firmware_type(self):
        r"""Gets the hw_firmware_type of this QuickImportImageByFileRequestBody.

        云主机云服务器的启动方式。目前支持： bios：表示bios引导启动。 uefi：表示uefi引导启动。

        :return: The hw_firmware_type of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._hw_firmware_type

    @hw_firmware_type.setter
    def hw_firmware_type(self, hw_firmware_type):
        r"""Sets the hw_firmware_type of this QuickImportImageByFileRequestBody.

        云主机云服务器的启动方式。目前支持： bios：表示bios引导启动。 uefi：表示uefi引导启动。

        :param hw_firmware_type: The hw_firmware_type of this QuickImportImageByFileRequestBody.
        :type hw_firmware_type: str
        """
        self._hw_firmware_type = hw_firmware_type

    @property
    def os_type(self):
        r"""Gets the os_type of this QuickImportImageByFileRequestBody.

        操作系统版本。 创建数据盘镜像时该参数取值为Linux或Windows，默认Linux。

        :return: The os_type of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this QuickImportImageByFileRequestBody.

        操作系统版本。 创建数据盘镜像时该参数取值为Linux或Windows，默认Linux。

        :param os_type: The os_type of this QuickImportImageByFileRequestBody.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def image_tags(self):
        r"""Gets the image_tags of this QuickImportImageByFileRequestBody.

        新规范的镜像标签列表。默认为空。 tags和image_tags只能使用一个。

        :return: The image_tags of this QuickImportImageByFileRequestBody.
        :rtype: list[:class:`huaweicloudsdkims.v2.ResourceTag`]
        """
        return self._image_tags

    @image_tags.setter
    def image_tags(self, image_tags):
        r"""Sets the image_tags of this QuickImportImageByFileRequestBody.

        新规范的镜像标签列表。默认为空。 tags和image_tags只能使用一个。

        :param image_tags: The image_tags of this QuickImportImageByFileRequestBody.
        :type image_tags: list[:class:`huaweicloudsdkims.v2.ResourceTag`]
        """
        self._image_tags = image_tags

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
        if not isinstance(other, QuickImportImageByFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
