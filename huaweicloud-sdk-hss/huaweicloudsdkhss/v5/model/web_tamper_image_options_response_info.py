# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperImageOptionsResponseInfo:

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
        'image_full_name': 'str',
        'image_id': 'str',
        'image_version_list': 'list[str]',
        'image_namespace': 'str',
        'registry_name': 'str',
        'registry_type': 'str'
    }

    attribute_map = {
        'image_name': 'image_name',
        'image_full_name': 'image_full_name',
        'image_id': 'image_id',
        'image_version_list': 'image_version_list',
        'image_namespace': 'image_namespace',
        'registry_name': 'registry_name',
        'registry_type': 'registry_type'
    }

    def __init__(self, image_name=None, image_full_name=None, image_id=None, image_version_list=None, image_namespace=None, registry_name=None, registry_type=None):
        r"""WebTamperImageOptionsResponseInfo

        The model defined in huaweicloud sdk

        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-512位 
        :type image_name: str
        :param image_full_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-512位 
        :type image_full_name: str
        :param image_id: **参数解释**: 镜像id **取值范围**: 字符长度0-64位 
        :type image_id: str
        :param image_version_list: **参数解释**: 镜像版本列表 **约束限制**: 不涉及 **取值范围**: 最少0条，最多100条 **默认取值**: 不涉及 
        :type image_version_list: list[str]
        :param image_namespace: **参数解释**: 仓库镜像的组织名称 **取值范围**: 字符长度0-512位 
        :type image_namespace: str
        :param registry_name: **参数解释**: 镜像仓库名称 **取值范围**: 字符长度1-128位 
        :type registry_name: str
        :param registry_type: **参数解释**： 镜像仓库类型 **取值范围**： - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。 
        :type registry_type: str
        """
        
        

        self._image_name = None
        self._image_full_name = None
        self._image_id = None
        self._image_version_list = None
        self._image_namespace = None
        self._registry_name = None
        self._registry_type = None
        self.discriminator = None

        if image_name is not None:
            self.image_name = image_name
        if image_full_name is not None:
            self.image_full_name = image_full_name
        if image_id is not None:
            self.image_id = image_id
        if image_version_list is not None:
            self.image_version_list = image_version_list
        if image_namespace is not None:
            self.image_namespace = image_namespace
        if registry_name is not None:
            self.registry_name = registry_name
        if registry_type is not None:
            self.registry_type = registry_type

    @property
    def image_name(self):
        r"""Gets the image_name of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-512位 

        :return: The image_name of this WebTamperImageOptionsResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-512位 

        :param image_name: The image_name of this WebTamperImageOptionsResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_full_name(self):
        r"""Gets the image_full_name of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-512位 

        :return: The image_full_name of this WebTamperImageOptionsResponseInfo.
        :rtype: str
        """
        return self._image_full_name

    @image_full_name.setter
    def image_full_name(self, image_full_name):
        r"""Sets the image_full_name of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-512位 

        :param image_full_name: The image_full_name of this WebTamperImageOptionsResponseInfo.
        :type image_full_name: str
        """
        self._image_full_name = image_full_name

    @property
    def image_id(self):
        r"""Gets the image_id of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-64位 

        :return: The image_id of this WebTamperImageOptionsResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-64位 

        :param image_id: The image_id of this WebTamperImageOptionsResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_version_list(self):
        r"""Gets the image_version_list of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 镜像版本列表 **约束限制**: 不涉及 **取值范围**: 最少0条，最多100条 **默认取值**: 不涉及 

        :return: The image_version_list of this WebTamperImageOptionsResponseInfo.
        :rtype: list[str]
        """
        return self._image_version_list

    @image_version_list.setter
    def image_version_list(self, image_version_list):
        r"""Sets the image_version_list of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 镜像版本列表 **约束限制**: 不涉及 **取值范围**: 最少0条，最多100条 **默认取值**: 不涉及 

        :param image_version_list: The image_version_list of this WebTamperImageOptionsResponseInfo.
        :type image_version_list: list[str]
        """
        self._image_version_list = image_version_list

    @property
    def image_namespace(self):
        r"""Gets the image_namespace of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 仓库镜像的组织名称 **取值范围**: 字符长度0-512位 

        :return: The image_namespace of this WebTamperImageOptionsResponseInfo.
        :rtype: str
        """
        return self._image_namespace

    @image_namespace.setter
    def image_namespace(self, image_namespace):
        r"""Sets the image_namespace of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 仓库镜像的组织名称 **取值范围**: 字符长度0-512位 

        :param image_namespace: The image_namespace of this WebTamperImageOptionsResponseInfo.
        :type image_namespace: str
        """
        self._image_namespace = image_namespace

    @property
    def registry_name(self):
        r"""Gets the registry_name of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 镜像仓库名称 **取值范围**: 字符长度1-128位 

        :return: The registry_name of this WebTamperImageOptionsResponseInfo.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this WebTamperImageOptionsResponseInfo.

        **参数解释**: 镜像仓库名称 **取值范围**: 字符长度1-128位 

        :param registry_name: The registry_name of this WebTamperImageOptionsResponseInfo.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def registry_type(self):
        r"""Gets the registry_type of this WebTamperImageOptionsResponseInfo.

        **参数解释**： 镜像仓库类型 **取值范围**： - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。 

        :return: The registry_type of this WebTamperImageOptionsResponseInfo.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this WebTamperImageOptionsResponseInfo.

        **参数解释**： 镜像仓库类型 **取值范围**： - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。 

        :param registry_type: The registry_type of this WebTamperImageOptionsResponseInfo.
        :type registry_type: str
        """
        self._registry_type = registry_type

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
        if not isinstance(other, WebTamperImageOptionsResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
