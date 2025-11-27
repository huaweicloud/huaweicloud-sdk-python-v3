# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_name': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'protect_directory_info_list': 'list[ProtectDirectoryInfo]',
        'exclude_file_types': 'list[str]'
    }

    attribute_map = {
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'protect_directory_info_list': 'protect_directory_info_list',
        'exclude_file_types': 'exclude_file_types'
    }

    def __init__(self, image_name=None, image_version=None, image_type=None, protect_directory_info_list=None, exclude_file_types=None):
        r"""ProtectImageInfo

        The model defined in huaweicloud sdk

        :param image_name: **参数解释**： 镜像名称 **约束限制**: 不涉及 **取值范围**： 字符长度1-256位 **默认取值**: 不涉及 
        :type image_name: str
        :param image_version: **参数解释**： 镜像版本 **约束限制**: 不涉及 **取值范围**： 字符长度0-64位 **默认取值**: 不涉及 
        :type image_version: str
        :param image_type: **参数解释**： 镜像类型 **约束限制**: 不涉及 **取值范围**： - registry 仓库镜像 - local 本地镜像 - custom 自定义镜像  **默认取值**: custom 
        :type image_type: str
        :param protect_directory_info_list: **参数解释**： 防护目录信息 **约束限制**: 不涉及 **取值范围**： 最少1条，最多50条 **默认取值**: 不涉及 
        :type protect_directory_info_list: list[:class:`huaweicloudsdkhss.v5.ProtectDirectoryInfo`]
        :param exclude_file_types: **参数解释**： 防护排除的文件类型列表 **约束限制**: 不涉及 **取值范围**： 最少0条，最多10条 **默认取值**: 不涉及 
        :type exclude_file_types: list[str]
        """
        
        

        self._image_name = None
        self._image_version = None
        self._image_type = None
        self._protect_directory_info_list = None
        self._exclude_file_types = None
        self.discriminator = None

        self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        self.protect_directory_info_list = protect_directory_info_list
        if exclude_file_types is not None:
            self.exclude_file_types = exclude_file_types

    @property
    def image_name(self):
        r"""Gets the image_name of this ProtectImageInfo.

        **参数解释**： 镜像名称 **约束限制**: 不涉及 **取值范围**： 字符长度1-256位 **默认取值**: 不涉及 

        :return: The image_name of this ProtectImageInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ProtectImageInfo.

        **参数解释**： 镜像名称 **约束限制**: 不涉及 **取值范围**： 字符长度1-256位 **默认取值**: 不涉及 

        :param image_name: The image_name of this ProtectImageInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ProtectImageInfo.

        **参数解释**： 镜像版本 **约束限制**: 不涉及 **取值范围**： 字符长度0-64位 **默认取值**: 不涉及 

        :return: The image_version of this ProtectImageInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ProtectImageInfo.

        **参数解释**： 镜像版本 **约束限制**: 不涉及 **取值范围**： 字符长度0-64位 **默认取值**: 不涉及 

        :param image_version: The image_version of this ProtectImageInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        r"""Gets the image_type of this ProtectImageInfo.

        **参数解释**： 镜像类型 **约束限制**: 不涉及 **取值范围**： - registry 仓库镜像 - local 本地镜像 - custom 自定义镜像  **默认取值**: custom 

        :return: The image_type of this ProtectImageInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ProtectImageInfo.

        **参数解释**： 镜像类型 **约束限制**: 不涉及 **取值范围**： - registry 仓库镜像 - local 本地镜像 - custom 自定义镜像  **默认取值**: custom 

        :param image_type: The image_type of this ProtectImageInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def protect_directory_info_list(self):
        r"""Gets the protect_directory_info_list of this ProtectImageInfo.

        **参数解释**： 防护目录信息 **约束限制**: 不涉及 **取值范围**： 最少1条，最多50条 **默认取值**: 不涉及 

        :return: The protect_directory_info_list of this ProtectImageInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ProtectDirectoryInfo`]
        """
        return self._protect_directory_info_list

    @protect_directory_info_list.setter
    def protect_directory_info_list(self, protect_directory_info_list):
        r"""Sets the protect_directory_info_list of this ProtectImageInfo.

        **参数解释**： 防护目录信息 **约束限制**: 不涉及 **取值范围**： 最少1条，最多50条 **默认取值**: 不涉及 

        :param protect_directory_info_list: The protect_directory_info_list of this ProtectImageInfo.
        :type protect_directory_info_list: list[:class:`huaweicloudsdkhss.v5.ProtectDirectoryInfo`]
        """
        self._protect_directory_info_list = protect_directory_info_list

    @property
    def exclude_file_types(self):
        r"""Gets the exclude_file_types of this ProtectImageInfo.

        **参数解释**： 防护排除的文件类型列表 **约束限制**: 不涉及 **取值范围**： 最少0条，最多10条 **默认取值**: 不涉及 

        :return: The exclude_file_types of this ProtectImageInfo.
        :rtype: list[str]
        """
        return self._exclude_file_types

    @exclude_file_types.setter
    def exclude_file_types(self, exclude_file_types):
        r"""Sets the exclude_file_types of this ProtectImageInfo.

        **参数解释**： 防护排除的文件类型列表 **约束限制**: 不涉及 **取值范围**： 最少0条，最多10条 **默认取值**: 不涉及 

        :param exclude_file_types: The exclude_file_types of this ProtectImageInfo.
        :type exclude_file_types: list[str]
        """
        self._exclude_file_types = exclude_file_types

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProtectImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
