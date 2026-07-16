# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service': 'str',
        'key_pair_names': 'list[str]'
    }

    attribute_map = {
        'service': 'service',
        'key_pair_names': 'key_pair_names'
    }

    def __init__(self, service=None, key_pair_names=None):
        r"""EndpointsReq

        The model defined in huaweicloud sdk

        :param service: **参数解释**：支持的服务。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下：  - NOTEBOOK：可以通过https协议访问Notebook。  - SSH：可以通过SSH协议远程连接Notebook。  **默认取值**：不涉及。
        :type service: str
        :param key_pair_names: **参数解释**：SSH密钥对名称，可以在云服务器控制台（ECS）“密钥对”页面创建和查看。 **约束限制**：不涉及。
        :type key_pair_names: list[str]
        """
        
        

        self._service = None
        self._key_pair_names = None
        self.discriminator = None

        if service is not None:
            self.service = service
        if key_pair_names is not None:
            self.key_pair_names = key_pair_names

    @property
    def service(self):
        r"""Gets the service of this EndpointsReq.

        **参数解释**：支持的服务。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下：  - NOTEBOOK：可以通过https协议访问Notebook。  - SSH：可以通过SSH协议远程连接Notebook。  **默认取值**：不涉及。

        :return: The service of this EndpointsReq.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this EndpointsReq.

        **参数解释**：支持的服务。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下：  - NOTEBOOK：可以通过https协议访问Notebook。  - SSH：可以通过SSH协议远程连接Notebook。  **默认取值**：不涉及。

        :param service: The service of this EndpointsReq.
        :type service: str
        """
        self._service = service

    @property
    def key_pair_names(self):
        r"""Gets the key_pair_names of this EndpointsReq.

        **参数解释**：SSH密钥对名称，可以在云服务器控制台（ECS）“密钥对”页面创建和查看。 **约束限制**：不涉及。

        :return: The key_pair_names of this EndpointsReq.
        :rtype: list[str]
        """
        return self._key_pair_names

    @key_pair_names.setter
    def key_pair_names(self, key_pair_names):
        r"""Sets the key_pair_names of this EndpointsReq.

        **参数解释**：SSH密钥对名称，可以在云服务器控制台（ECS）“密钥对”页面创建和查看。 **约束限制**：不涉及。

        :param key_pair_names: The key_pair_names of this EndpointsReq.
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
        if not isinstance(other, EndpointsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
