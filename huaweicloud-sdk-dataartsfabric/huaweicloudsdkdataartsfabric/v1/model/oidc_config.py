# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OidcConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_oidc': 'bool',
        'client_id': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'enable_oidc': 'enable_oidc',
        'client_id': 'client_id',
        'namespace': 'namespace'
    }

    def __init__(self, enable_oidc=None, client_id=None, namespace=None):
        r"""OidcConfig

        The model defined in huaweicloud sdk

        :param enable_oidc: - **参数解释**：是否开启oidc功能。 - **约束限制**：不涉及。 - **取值范围**：开启true，关闭false。 - **默认取值**：false。 
        :type enable_oidc: bool
        :param client_id: - **参数解释**：客户端ID。 - **约束限制**：不涉及。 - **取值范围**：长度为[1,64]的字母、数字、下划线(_)、中划线(-)、点(.)的组合。 - **默认取值**：null。 
        :type client_id: str
        :param namespace: - **参数解释**：RayService命名空间。 - **约束限制**：不涉及。 - **取值范围**：长度为16位，均为ray-svc-xxx格式。 - **默认取值**：null。 
        :type namespace: str
        """
        
        

        self._enable_oidc = None
        self._client_id = None
        self._namespace = None
        self.discriminator = None

        if enable_oidc is not None:
            self.enable_oidc = enable_oidc
        if client_id is not None:
            self.client_id = client_id
        if namespace is not None:
            self.namespace = namespace

    @property
    def enable_oidc(self):
        r"""Gets the enable_oidc of this OidcConfig.

        - **参数解释**：是否开启oidc功能。 - **约束限制**：不涉及。 - **取值范围**：开启true，关闭false。 - **默认取值**：false。 

        :return: The enable_oidc of this OidcConfig.
        :rtype: bool
        """
        return self._enable_oidc

    @enable_oidc.setter
    def enable_oidc(self, enable_oidc):
        r"""Sets the enable_oidc of this OidcConfig.

        - **参数解释**：是否开启oidc功能。 - **约束限制**：不涉及。 - **取值范围**：开启true，关闭false。 - **默认取值**：false。 

        :param enable_oidc: The enable_oidc of this OidcConfig.
        :type enable_oidc: bool
        """
        self._enable_oidc = enable_oidc

    @property
    def client_id(self):
        r"""Gets the client_id of this OidcConfig.

        - **参数解释**：客户端ID。 - **约束限制**：不涉及。 - **取值范围**：长度为[1,64]的字母、数字、下划线(_)、中划线(-)、点(.)的组合。 - **默认取值**：null。 

        :return: The client_id of this OidcConfig.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this OidcConfig.

        - **参数解释**：客户端ID。 - **约束限制**：不涉及。 - **取值范围**：长度为[1,64]的字母、数字、下划线(_)、中划线(-)、点(.)的组合。 - **默认取值**：null。 

        :param client_id: The client_id of this OidcConfig.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def namespace(self):
        r"""Gets the namespace of this OidcConfig.

        - **参数解释**：RayService命名空间。 - **约束限制**：不涉及。 - **取值范围**：长度为16位，均为ray-svc-xxx格式。 - **默认取值**：null。 

        :return: The namespace of this OidcConfig.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this OidcConfig.

        - **参数解释**：RayService命名空间。 - **约束限制**：不涉及。 - **取值范围**：长度为16位，均为ray-svc-xxx格式。 - **默认取值**：null。 

        :param namespace: The namespace of this OidcConfig.
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
        if not isinstance(other, OidcConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
