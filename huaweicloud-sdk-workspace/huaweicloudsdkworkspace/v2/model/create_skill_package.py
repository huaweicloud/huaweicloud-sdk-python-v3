# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSkillPackage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'package_name': 'str',
        'package_hash': 'str',
        'package_size': 'int',
        'regions': 'list[PackageRegionWithStatusInfo]'
    }

    attribute_map = {
        'version': 'version',
        'package_name': 'package_name',
        'package_hash': 'package_hash',
        'package_size': 'package_size',
        'regions': 'regions'
    }

    def __init__(self, version=None, package_name=None, package_hash=None, package_size=None, regions=None):
        r"""CreateSkillPackage

        The model defined in huaweicloud sdk

        :param version: 版本号。
        :type version: str
        :param package_name: 技能包文件名（与 getUploadUrls 中的 packageName 一致），服务端据此构造 OBS 路径。
        :type package_name: str
        :param package_hash: 技能包 SHA256 哈希值（前端上传前计算）。
        :type package_hash: str
        :param package_size: 技能包大小（字节），最大 104857600。
        :type package_size: int
        :param regions: OBS 存储区域信息（含上传状态）。
        :type regions: list[:class:`huaweicloudsdkworkspace.v2.PackageRegionWithStatusInfo`]
        """
        
        

        self._version = None
        self._package_name = None
        self._package_hash = None
        self._package_size = None
        self._regions = None
        self.discriminator = None

        self.version = version
        self.package_name = package_name
        self.package_hash = package_hash
        self.package_size = package_size
        self.regions = regions

    @property
    def version(self):
        r"""Gets the version of this CreateSkillPackage.

        版本号。

        :return: The version of this CreateSkillPackage.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateSkillPackage.

        版本号。

        :param version: The version of this CreateSkillPackage.
        :type version: str
        """
        self._version = version

    @property
    def package_name(self):
        r"""Gets the package_name of this CreateSkillPackage.

        技能包文件名（与 getUploadUrls 中的 packageName 一致），服务端据此构造 OBS 路径。

        :return: The package_name of this CreateSkillPackage.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        r"""Sets the package_name of this CreateSkillPackage.

        技能包文件名（与 getUploadUrls 中的 packageName 一致），服务端据此构造 OBS 路径。

        :param package_name: The package_name of this CreateSkillPackage.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def package_hash(self):
        r"""Gets the package_hash of this CreateSkillPackage.

        技能包 SHA256 哈希值（前端上传前计算）。

        :return: The package_hash of this CreateSkillPackage.
        :rtype: str
        """
        return self._package_hash

    @package_hash.setter
    def package_hash(self, package_hash):
        r"""Sets the package_hash of this CreateSkillPackage.

        技能包 SHA256 哈希值（前端上传前计算）。

        :param package_hash: The package_hash of this CreateSkillPackage.
        :type package_hash: str
        """
        self._package_hash = package_hash

    @property
    def package_size(self):
        r"""Gets the package_size of this CreateSkillPackage.

        技能包大小（字节），最大 104857600。

        :return: The package_size of this CreateSkillPackage.
        :rtype: int
        """
        return self._package_size

    @package_size.setter
    def package_size(self, package_size):
        r"""Sets the package_size of this CreateSkillPackage.

        技能包大小（字节），最大 104857600。

        :param package_size: The package_size of this CreateSkillPackage.
        :type package_size: int
        """
        self._package_size = package_size

    @property
    def regions(self):
        r"""Gets the regions of this CreateSkillPackage.

        OBS 存储区域信息（含上传状态）。

        :return: The regions of this CreateSkillPackage.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.PackageRegionWithStatusInfo`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this CreateSkillPackage.

        OBS 存储区域信息（含上传状态）。

        :param regions: The regions of this CreateSkillPackage.
        :type regions: list[:class:`huaweicloudsdkworkspace.v2.PackageRegionWithStatusInfo`]
        """
        self._regions = regions

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
        if not isinstance(other, CreateSkillPackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
