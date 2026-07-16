# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointsRes:

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
        'service': 'str',
        'uri': 'str',
        'key_pair_names': 'list[str]'
    }

    attribute_map = {
        'dev_service': 'dev_service',
        'service': 'service',
        'uri': 'uri',
        'key_pair_names': 'key_pair_names'
    }

    def __init__(self, dev_service=None, service=None, uri=None, key_pair_names=None):
        r"""EndpointsRes

        The model defined in huaweicloud sdk

        :param dev_service: **参数解释**：访问Notebook的途径。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：可以通过https协议访问Notebook。 - SSH：可以通过SSH协议远程连接Notebook。
        :type dev_service: str
        :param service: **参数解释**：访问Notebook的途径。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：可以通过https协议访问Notebook。 - SSH：可以通过SSH协议远程连接Notebook。
        :type service: str
        :param uri: **参数解释**：实例私有IP地址。 **取值范围**：不涉及。
        :type uri: str
        :param key_pair_names: **参数解释**：SSH密钥对名称列表，允许设置多个密钥对实现同时对SSH实例的访问。 **取值范围**：不涉及。
        :type key_pair_names: list[str]
        """
        
        

        self._dev_service = None
        self._service = None
        self._uri = None
        self._key_pair_names = None
        self.discriminator = None

        if dev_service is not None:
            self.dev_service = dev_service
        if service is not None:
            self.service = service
        if uri is not None:
            self.uri = uri
        if key_pair_names is not None:
            self.key_pair_names = key_pair_names

    @property
    def dev_service(self):
        r"""Gets the dev_service of this EndpointsRes.

        **参数解释**：访问Notebook的途径。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：可以通过https协议访问Notebook。 - SSH：可以通过SSH协议远程连接Notebook。

        :return: The dev_service of this EndpointsRes.
        :rtype: str
        """
        return self._dev_service

    @dev_service.setter
    def dev_service(self, dev_service):
        r"""Sets the dev_service of this EndpointsRes.

        **参数解释**：访问Notebook的途径。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：可以通过https协议访问Notebook。 - SSH：可以通过SSH协议远程连接Notebook。

        :param dev_service: The dev_service of this EndpointsRes.
        :type dev_service: str
        """
        self._dev_service = dev_service

    @property
    def service(self):
        r"""Gets the service of this EndpointsRes.

        **参数解释**：访问Notebook的途径。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：可以通过https协议访问Notebook。 - SSH：可以通过SSH协议远程连接Notebook。

        :return: The service of this EndpointsRes.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this EndpointsRes.

        **参数解释**：访问Notebook的途径。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：可以通过https协议访问Notebook。 - SSH：可以通过SSH协议远程连接Notebook。

        :param service: The service of this EndpointsRes.
        :type service: str
        """
        self._service = service

    @property
    def uri(self):
        r"""Gets the uri of this EndpointsRes.

        **参数解释**：实例私有IP地址。 **取值范围**：不涉及。

        :return: The uri of this EndpointsRes.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this EndpointsRes.

        **参数解释**：实例私有IP地址。 **取值范围**：不涉及。

        :param uri: The uri of this EndpointsRes.
        :type uri: str
        """
        self._uri = uri

    @property
    def key_pair_names(self):
        r"""Gets the key_pair_names of this EndpointsRes.

        **参数解释**：SSH密钥对名称列表，允许设置多个密钥对实现同时对SSH实例的访问。 **取值范围**：不涉及。

        :return: The key_pair_names of this EndpointsRes.
        :rtype: list[str]
        """
        return self._key_pair_names

    @key_pair_names.setter
    def key_pair_names(self, key_pair_names):
        r"""Sets the key_pair_names of this EndpointsRes.

        **参数解释**：SSH密钥对名称列表，允许设置多个密钥对实现同时对SSH实例的访问。 **取值范围**：不涉及。

        :param key_pair_names: The key_pair_names of this EndpointsRes.
        :type key_pair_names: list[str]
        """
        self._key_pair_names = key_pair_names

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
        if not isinstance(other, EndpointsRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
