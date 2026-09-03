# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUploadUrlsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slug': 'str',
        'version': 'str',
        'package_name': 'str',
        'regions': 'list[str]'
    }

    attribute_map = {
        'slug': 'slug',
        'version': 'version',
        'package_name': 'package_name',
        'regions': 'regions'
    }

    def __init__(self, slug=None, version=None, package_name=None, regions=None):
        r"""CreateUploadUrlsReq

        The model defined in huaweicloud sdk

        :param slug: 技能slug（用于构建 OBS 路径）。
        :type slug: str
        :param version: 版本号（用于构建 OBS 路径）。
        :type version: str
        :param package_name: 包文件名。
        :type package_name: str
        :param regions: 目标 region 列表。
        :type regions: list[str]
        """
        
        

        self._slug = None
        self._version = None
        self._package_name = None
        self._regions = None
        self.discriminator = None

        self.slug = slug
        self.version = version
        self.package_name = package_name
        self.regions = regions

    @property
    def slug(self):
        r"""Gets the slug of this CreateUploadUrlsReq.

        技能slug（用于构建 OBS 路径）。

        :return: The slug of this CreateUploadUrlsReq.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        r"""Sets the slug of this CreateUploadUrlsReq.

        技能slug（用于构建 OBS 路径）。

        :param slug: The slug of this CreateUploadUrlsReq.
        :type slug: str
        """
        self._slug = slug

    @property
    def version(self):
        r"""Gets the version of this CreateUploadUrlsReq.

        版本号（用于构建 OBS 路径）。

        :return: The version of this CreateUploadUrlsReq.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateUploadUrlsReq.

        版本号（用于构建 OBS 路径）。

        :param version: The version of this CreateUploadUrlsReq.
        :type version: str
        """
        self._version = version

    @property
    def package_name(self):
        r"""Gets the package_name of this CreateUploadUrlsReq.

        包文件名。

        :return: The package_name of this CreateUploadUrlsReq.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        r"""Sets the package_name of this CreateUploadUrlsReq.

        包文件名。

        :param package_name: The package_name of this CreateUploadUrlsReq.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def regions(self):
        r"""Gets the regions of this CreateUploadUrlsReq.

        目标 region 列表。

        :return: The regions of this CreateUploadUrlsReq.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this CreateUploadUrlsReq.

        目标 region 列表。

        :param regions: The regions of this CreateUploadUrlsReq.
        :type regions: list[str]
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
        if not isinstance(other, CreateUploadUrlsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
