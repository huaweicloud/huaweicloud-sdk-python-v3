# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRuleImageResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'image_digest': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'registry_name': 'str',
        'image_size': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'image_digest': 'image_digest',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'registry_name': 'registry_name',
        'image_size': 'image_size'
    }

    def __init__(self, namespace=None, image_digest=None, image_name=None, image_version=None, image_type=None, registry_name=None, image_size=None):
        r"""CheckRuleImageResponseInfo

        The model defined in huaweicloud sdk

        :param namespace: **参数解释**: 组织名称 **取值范围**: 字符长度0-64 
        :type namespace: str
        :param image_digest: **参数解释**: 镜像digest **取值范围**: 字符长度0-128 
        :type image_digest: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-128 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本 **取值范围**: 字符长度0-128 
        :type image_version: str
        :param image_type: **参数解释**: 镜像类型 **取值范围**: - private_image：私有镜像 - shared_image：共享镜像 - instance_image：企业镜像 - harbor：Harbor镜像 - jfrog：Jfrog镜像 - cicd：cicd镜像
        :type image_type: str
        :param registry_name: **参数解释**: 镜像仓库名称 **取值范围**: 字符长度0-128 
        :type registry_name: str
        :param image_size: **参数解释**: 版本大小 **取值范围**: 大小0-2147483547 
        :type image_size: int
        """
        
        

        self._namespace = None
        self._image_digest = None
        self._image_name = None
        self._image_version = None
        self._image_type = None
        self._registry_name = None
        self._image_size = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if image_digest is not None:
            self.image_digest = image_digest
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        if registry_name is not None:
            self.registry_name = registry_name
        if image_size is not None:
            self.image_size = image_size

    @property
    def namespace(self):
        r"""Gets the namespace of this CheckRuleImageResponseInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-64 

        :return: The namespace of this CheckRuleImageResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CheckRuleImageResponseInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-64 

        :param namespace: The namespace of this CheckRuleImageResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_digest(self):
        r"""Gets the image_digest of this CheckRuleImageResponseInfo.

        **参数解释**: 镜像digest **取值范围**: 字符长度0-128 

        :return: The image_digest of this CheckRuleImageResponseInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this CheckRuleImageResponseInfo.

        **参数解释**: 镜像digest **取值范围**: 字符长度0-128 

        :param image_digest: The image_digest of this CheckRuleImageResponseInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_name(self):
        r"""Gets the image_name of this CheckRuleImageResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-128 

        :return: The image_name of this CheckRuleImageResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this CheckRuleImageResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-128 

        :param image_name: The image_name of this CheckRuleImageResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this CheckRuleImageResponseInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-128 

        :return: The image_version of this CheckRuleImageResponseInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this CheckRuleImageResponseInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-128 

        :param image_version: The image_version of this CheckRuleImageResponseInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        r"""Gets the image_type of this CheckRuleImageResponseInfo.

        **参数解释**: 镜像类型 **取值范围**: - private_image：私有镜像 - shared_image：共享镜像 - instance_image：企业镜像 - harbor：Harbor镜像 - jfrog：Jfrog镜像 - cicd：cicd镜像

        :return: The image_type of this CheckRuleImageResponseInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this CheckRuleImageResponseInfo.

        **参数解释**: 镜像类型 **取值范围**: - private_image：私有镜像 - shared_image：共享镜像 - instance_image：企业镜像 - harbor：Harbor镜像 - jfrog：Jfrog镜像 - cicd：cicd镜像

        :param image_type: The image_type of this CheckRuleImageResponseInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def registry_name(self):
        r"""Gets the registry_name of this CheckRuleImageResponseInfo.

        **参数解释**: 镜像仓库名称 **取值范围**: 字符长度0-128 

        :return: The registry_name of this CheckRuleImageResponseInfo.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this CheckRuleImageResponseInfo.

        **参数解释**: 镜像仓库名称 **取值范围**: 字符长度0-128 

        :param registry_name: The registry_name of this CheckRuleImageResponseInfo.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def image_size(self):
        r"""Gets the image_size of this CheckRuleImageResponseInfo.

        **参数解释**: 版本大小 **取值范围**: 大小0-2147483547 

        :return: The image_size of this CheckRuleImageResponseInfo.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this CheckRuleImageResponseInfo.

        **参数解释**: 版本大小 **取值范围**: 大小0-2147483547 

        :param image_size: The image_size of this CheckRuleImageResponseInfo.
        :type image_size: int
        """
        self._image_size = image_size

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
        if not isinstance(other, CheckRuleImageResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
