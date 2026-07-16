# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Endpoints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dev_service': 'str',
        'extensions': 'dict(str, str)',
        'ssh_keys': 'list[str]'
    }

    attribute_map = {
        'dev_service': 'dev_service',
        'extensions': 'extensions',
        'ssh_keys': 'ssh_keys'
    }

    def __init__(self, dev_service=None, extensions=None, ssh_keys=None):
        r"""Endpoints

        The model defined in huaweicloud sdk

        :param dev_service: **参数解释**：支持的服务。 **取值范围**： - NOTEBOOK：可以通过https协议访问Notebook - SSH：可以通过SSH协议远程连接Notebook
        :type dev_service: str
        :param extensions: **参数解释**：通过应用专属URL直接打开应用进入远程开发模式。包含应用的各种扩展配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type extensions: dict(str, str)
        :param ssh_keys: **参数解释**：SSH密钥对名称列表。允许设置多个密钥对实现同时对SSH实例的访问。 **约束限制**：不涉及。 **取值范围**：0 - 1024个密钥对 **默认取值**：不涉及。
        :type ssh_keys: list[str]
        """
        
        

        self._dev_service = None
        self._extensions = None
        self._ssh_keys = None
        self.discriminator = None

        if dev_service is not None:
            self.dev_service = dev_service
        if extensions is not None:
            self.extensions = extensions
        if ssh_keys is not None:
            self.ssh_keys = ssh_keys

    @property
    def dev_service(self):
        r"""Gets the dev_service of this Endpoints.

        **参数解释**：支持的服务。 **取值范围**： - NOTEBOOK：可以通过https协议访问Notebook - SSH：可以通过SSH协议远程连接Notebook

        :return: The dev_service of this Endpoints.
        :rtype: str
        """
        return self._dev_service

    @dev_service.setter
    def dev_service(self, dev_service):
        r"""Sets the dev_service of this Endpoints.

        **参数解释**：支持的服务。 **取值范围**： - NOTEBOOK：可以通过https协议访问Notebook - SSH：可以通过SSH协议远程连接Notebook

        :param dev_service: The dev_service of this Endpoints.
        :type dev_service: str
        """
        self._dev_service = dev_service

    @property
    def extensions(self):
        r"""Gets the extensions of this Endpoints.

        **参数解释**：通过应用专属URL直接打开应用进入远程开发模式。包含应用的各种扩展配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The extensions of this Endpoints.
        :rtype: dict(str, str)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        r"""Sets the extensions of this Endpoints.

        **参数解释**：通过应用专属URL直接打开应用进入远程开发模式。包含应用的各种扩展配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param extensions: The extensions of this Endpoints.
        :type extensions: dict(str, str)
        """
        self._extensions = extensions

    @property
    def ssh_keys(self):
        r"""Gets the ssh_keys of this Endpoints.

        **参数解释**：SSH密钥对名称列表。允许设置多个密钥对实现同时对SSH实例的访问。 **约束限制**：不涉及。 **取值范围**：0 - 1024个密钥对 **默认取值**：不涉及。

        :return: The ssh_keys of this Endpoints.
        :rtype: list[str]
        """
        return self._ssh_keys

    @ssh_keys.setter
    def ssh_keys(self, ssh_keys):
        r"""Sets the ssh_keys of this Endpoints.

        **参数解释**：SSH密钥对名称列表。允许设置多个密钥对实现同时对SSH实例的访问。 **约束限制**：不涉及。 **取值范围**：0 - 1024个密钥对 **默认取值**：不涉及。

        :param ssh_keys: The ssh_keys of this Endpoints.
        :type ssh_keys: list[str]
        """
        self._ssh_keys = ssh_keys

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
        if not isinstance(other, Endpoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
