# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddonTemplateSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'require': 'bool',
        'labels': 'list[str]',
        'logo_url': 'str',
        'readme_url': 'str',
        'description': 'str',
        'versions': 'list[AddonVersion]'
    }

    attribute_map = {
        'type': 'type',
        'require': 'require',
        'labels': 'labels',
        'logo_url': 'logoURL',
        'readme_url': 'readmeURL',
        'description': 'description',
        'versions': 'versions'
    }

    def __init__(self, type=None, require=None, labels=None, logo_url=None, readme_url=None, description=None, versions=None):
        r"""AddonTemplateSpec

        The model defined in huaweicloud sdk

        :param type: 插件的安装类型，支持helm安装或static安装
        :type type: str
        :param require: 该插件是否为必装
        :type require: bool
        :param labels: 插件的标签列表
        :type labels: list[str]
        :param logo_url: Logo链接
        :type logo_url: str
        :param readme_url: README文档链接
        :type readme_url: str
        :param description: 描述信息
        :type description: str
        :param versions: 插件的版本列表
        :type versions: list[:class:`huaweicloudsdkucs.v1.AddonVersion`]
        """
        
        

        self._type = None
        self._require = None
        self._labels = None
        self._logo_url = None
        self._readme_url = None
        self._description = None
        self._versions = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if require is not None:
            self.require = require
        if labels is not None:
            self.labels = labels
        if logo_url is not None:
            self.logo_url = logo_url
        if readme_url is not None:
            self.readme_url = readme_url
        if description is not None:
            self.description = description
        if versions is not None:
            self.versions = versions

    @property
    def type(self):
        r"""Gets the type of this AddonTemplateSpec.

        插件的安装类型，支持helm安装或static安装

        :return: The type of this AddonTemplateSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AddonTemplateSpec.

        插件的安装类型，支持helm安装或static安装

        :param type: The type of this AddonTemplateSpec.
        :type type: str
        """
        self._type = type

    @property
    def require(self):
        r"""Gets the require of this AddonTemplateSpec.

        该插件是否为必装

        :return: The require of this AddonTemplateSpec.
        :rtype: bool
        """
        return self._require

    @require.setter
    def require(self, require):
        r"""Sets the require of this AddonTemplateSpec.

        该插件是否为必装

        :param require: The require of this AddonTemplateSpec.
        :type require: bool
        """
        self._require = require

    @property
    def labels(self):
        r"""Gets the labels of this AddonTemplateSpec.

        插件的标签列表

        :return: The labels of this AddonTemplateSpec.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this AddonTemplateSpec.

        插件的标签列表

        :param labels: The labels of this AddonTemplateSpec.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def logo_url(self):
        r"""Gets the logo_url of this AddonTemplateSpec.

        Logo链接

        :return: The logo_url of this AddonTemplateSpec.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        r"""Sets the logo_url of this AddonTemplateSpec.

        Logo链接

        :param logo_url: The logo_url of this AddonTemplateSpec.
        :type logo_url: str
        """
        self._logo_url = logo_url

    @property
    def readme_url(self):
        r"""Gets the readme_url of this AddonTemplateSpec.

        README文档链接

        :return: The readme_url of this AddonTemplateSpec.
        :rtype: str
        """
        return self._readme_url

    @readme_url.setter
    def readme_url(self, readme_url):
        r"""Sets the readme_url of this AddonTemplateSpec.

        README文档链接

        :param readme_url: The readme_url of this AddonTemplateSpec.
        :type readme_url: str
        """
        self._readme_url = readme_url

    @property
    def description(self):
        r"""Gets the description of this AddonTemplateSpec.

        描述信息

        :return: The description of this AddonTemplateSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddonTemplateSpec.

        描述信息

        :param description: The description of this AddonTemplateSpec.
        :type description: str
        """
        self._description = description

    @property
    def versions(self):
        r"""Gets the versions of this AddonTemplateSpec.

        插件的版本列表

        :return: The versions of this AddonTemplateSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.AddonVersion`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this AddonTemplateSpec.

        插件的版本列表

        :param versions: The versions of this AddonTemplateSpec.
        :type versions: list[:class:`huaweicloudsdkucs.v1.AddonVersion`]
        """
        self._versions = versions

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
        if not isinstance(other, AddonTemplateSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
