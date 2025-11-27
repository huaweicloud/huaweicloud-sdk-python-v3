# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddonVersion:

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
        'version': 'str',
        'input': 'dict(str, object)',
        'stable': 'bool',
        'translate': 'dict(str, object)',
        'support_versions': 'list[SupportVersion]',
        'creation_timestamp': 'str',
        'update_timestamp': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'input': 'input',
        'stable': 'stable',
        'translate': 'translate',
        'support_versions': 'supportVersions',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp'
    }

    def __init__(self, id=None, version=None, input=None, stable=None, translate=None, support_versions=None, creation_timestamp=None, update_timestamp=None):
        r"""AddonVersion

        The model defined in huaweicloud sdk

        :param id: 插件包版本id
        :type id: str
        :param version: 插件版本信息
        :type version: str
        :param input: 输入
        :type input: dict(str, object)
        :param stable: 是否为稳定版本
        :type stable: bool
        :param translate: 供界面使用的翻译信息
        :type translate: dict(str, object)
        :param support_versions: 支持的集群类型和和支持的集群版本信息
        :type support_versions: list[:class:`huaweicloudsdkucs.v1.SupportVersion`]
        :param creation_timestamp: 记录创建时间
        :type creation_timestamp: str
        :param update_timestamp: 记录更新时间
        :type update_timestamp: str
        """
        
        

        self._id = None
        self._version = None
        self._input = None
        self._stable = None
        self._translate = None
        self._support_versions = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if input is not None:
            self.input = input
        if stable is not None:
            self.stable = stable
        if translate is not None:
            self.translate = translate
        if support_versions is not None:
            self.support_versions = support_versions
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp

    @property
    def id(self):
        r"""Gets the id of this AddonVersion.

        插件包版本id

        :return: The id of this AddonVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AddonVersion.

        插件包版本id

        :param id: The id of this AddonVersion.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this AddonVersion.

        插件版本信息

        :return: The version of this AddonVersion.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AddonVersion.

        插件版本信息

        :param version: The version of this AddonVersion.
        :type version: str
        """
        self._version = version

    @property
    def input(self):
        r"""Gets the input of this AddonVersion.

        输入

        :return: The input of this AddonVersion.
        :rtype: dict(str, object)
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this AddonVersion.

        输入

        :param input: The input of this AddonVersion.
        :type input: dict(str, object)
        """
        self._input = input

    @property
    def stable(self):
        r"""Gets the stable of this AddonVersion.

        是否为稳定版本

        :return: The stable of this AddonVersion.
        :rtype: bool
        """
        return self._stable

    @stable.setter
    def stable(self, stable):
        r"""Sets the stable of this AddonVersion.

        是否为稳定版本

        :param stable: The stable of this AddonVersion.
        :type stable: bool
        """
        self._stable = stable

    @property
    def translate(self):
        r"""Gets the translate of this AddonVersion.

        供界面使用的翻译信息

        :return: The translate of this AddonVersion.
        :rtype: dict(str, object)
        """
        return self._translate

    @translate.setter
    def translate(self, translate):
        r"""Sets the translate of this AddonVersion.

        供界面使用的翻译信息

        :param translate: The translate of this AddonVersion.
        :type translate: dict(str, object)
        """
        self._translate = translate

    @property
    def support_versions(self):
        r"""Gets the support_versions of this AddonVersion.

        支持的集群类型和和支持的集群版本信息

        :return: The support_versions of this AddonVersion.
        :rtype: list[:class:`huaweicloudsdkucs.v1.SupportVersion`]
        """
        return self._support_versions

    @support_versions.setter
    def support_versions(self, support_versions):
        r"""Sets the support_versions of this AddonVersion.

        支持的集群类型和和支持的集群版本信息

        :param support_versions: The support_versions of this AddonVersion.
        :type support_versions: list[:class:`huaweicloudsdkucs.v1.SupportVersion`]
        """
        self._support_versions = support_versions

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this AddonVersion.

        记录创建时间

        :return: The creation_timestamp of this AddonVersion.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this AddonVersion.

        记录创建时间

        :param creation_timestamp: The creation_timestamp of this AddonVersion.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        r"""Gets the update_timestamp of this AddonVersion.

        记录更新时间

        :return: The update_timestamp of this AddonVersion.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        r"""Sets the update_timestamp of this AddonVersion.

        记录更新时间

        :param update_timestamp: The update_timestamp of this AddonVersion.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

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
        if not isinstance(other, AddonVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
