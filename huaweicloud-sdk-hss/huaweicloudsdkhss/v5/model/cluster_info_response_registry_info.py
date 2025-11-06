# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterInfoResponseRegistryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'registry_type': 'str',
        'registry_addr': 'str',
        'registry_username': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'registry_type': 'registry_type',
        'registry_addr': 'registry_addr',
        'registry_username': 'registry_username',
        'namespace': 'namespace'
    }

    def __init__(self, registry_type=None, registry_addr=None, registry_username=None, namespace=None):
        r"""ClusterInfoResponseRegistryInfo

        The model defined in huaweicloud sdk

        :param registry_type: **参数解释** 镜像仓库类型 **取值范围** 字符长度1-256位
        :type registry_type: str
        :param registry_addr: **参数解释** 镜像仓地址 **取值范围** 字符长度1-256位
        :type registry_addr: str
        :param registry_username: **参数解释** 镜像仓用户名 **取值范围** 字符长度1-256位
        :type registry_username: str
        :param namespace: **参数解释** 组织 **取值范围** 字符长度1-256位
        :type namespace: str
        """
        
        

        self._registry_type = None
        self._registry_addr = None
        self._registry_username = None
        self._namespace = None
        self.discriminator = None

        if registry_type is not None:
            self.registry_type = registry_type
        if registry_addr is not None:
            self.registry_addr = registry_addr
        if registry_username is not None:
            self.registry_username = registry_username
        if namespace is not None:
            self.namespace = namespace

    @property
    def registry_type(self):
        r"""Gets the registry_type of this ClusterInfoResponseRegistryInfo.

        **参数解释** 镜像仓库类型 **取值范围** 字符长度1-256位

        :return: The registry_type of this ClusterInfoResponseRegistryInfo.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this ClusterInfoResponseRegistryInfo.

        **参数解释** 镜像仓库类型 **取值范围** 字符长度1-256位

        :param registry_type: The registry_type of this ClusterInfoResponseRegistryInfo.
        :type registry_type: str
        """
        self._registry_type = registry_type

    @property
    def registry_addr(self):
        r"""Gets the registry_addr of this ClusterInfoResponseRegistryInfo.

        **参数解释** 镜像仓地址 **取值范围** 字符长度1-256位

        :return: The registry_addr of this ClusterInfoResponseRegistryInfo.
        :rtype: str
        """
        return self._registry_addr

    @registry_addr.setter
    def registry_addr(self, registry_addr):
        r"""Sets the registry_addr of this ClusterInfoResponseRegistryInfo.

        **参数解释** 镜像仓地址 **取值范围** 字符长度1-256位

        :param registry_addr: The registry_addr of this ClusterInfoResponseRegistryInfo.
        :type registry_addr: str
        """
        self._registry_addr = registry_addr

    @property
    def registry_username(self):
        r"""Gets the registry_username of this ClusterInfoResponseRegistryInfo.

        **参数解释** 镜像仓用户名 **取值范围** 字符长度1-256位

        :return: The registry_username of this ClusterInfoResponseRegistryInfo.
        :rtype: str
        """
        return self._registry_username

    @registry_username.setter
    def registry_username(self, registry_username):
        r"""Sets the registry_username of this ClusterInfoResponseRegistryInfo.

        **参数解释** 镜像仓用户名 **取值范围** 字符长度1-256位

        :param registry_username: The registry_username of this ClusterInfoResponseRegistryInfo.
        :type registry_username: str
        """
        self._registry_username = registry_username

    @property
    def namespace(self):
        r"""Gets the namespace of this ClusterInfoResponseRegistryInfo.

        **参数解释** 组织 **取值范围** 字符长度1-256位

        :return: The namespace of this ClusterInfoResponseRegistryInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ClusterInfoResponseRegistryInfo.

        **参数解释** 组织 **取值范围** 字符长度1-256位

        :param namespace: The namespace of this ClusterInfoResponseRegistryInfo.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, ClusterInfoResponseRegistryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
