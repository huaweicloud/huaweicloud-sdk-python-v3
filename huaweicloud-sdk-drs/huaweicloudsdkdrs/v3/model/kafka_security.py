# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaSecurity:

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
        'trust_store_key_name': 'str',
        'trust_store_key': 'str',
        'trust_store_password': 'str',
        'endpoint_algorithm': 'str',
        'sasl_mechanism': 'str',
        'delegation_tokens': 'bool',
        'enable_key_store': 'bool',
        'key_store_key': 'str',
        'key_store_key_name': 'str',
        'key_store_password': 'str',
        'set_private_key_password': 'bool',
        'key_password': 'str'
    }

    attribute_map = {
        'type': 'type',
        'trust_store_key_name': 'trust_store_key_name',
        'trust_store_key': 'trust_store_key',
        'trust_store_password': 'trust_store_password',
        'endpoint_algorithm': 'endpoint_algorithm',
        'sasl_mechanism': 'sasl_mechanism',
        'delegation_tokens': 'delegation_tokens',
        'enable_key_store': 'enable_key_store',
        'key_store_key': 'key_store_key',
        'key_store_key_name': 'key_store_key_name',
        'key_store_password': 'key_store_password',
        'set_private_key_password': 'set_private_key_password',
        'key_password': 'key_password'
    }

    def __init__(self, type=None, trust_store_key_name=None, trust_store_key=None, trust_store_password=None, endpoint_algorithm=None, sasl_mechanism=None, delegation_tokens=None, enable_key_store=None, key_store_key=None, key_store_key_name=None, key_store_password=None, set_private_key_password=None, key_password=None):
        r"""KafkaSecurity

        The model defined in huaweicloud sdk

        :param type: **参数解释**：  安全协议类型，安全认证时必填，对应Kafka字段：security.protocol。  **约束限制**：  - 安全认证时必填。  **取值范围**：  - PLAINTEXT：无安全认证方式，仅需输入IP和端口进行连接 - SASL_PLAINTEXT：使用SASL机制连接Kafka，需要设置SASL相关配置 - SSL：使用SSL加密方式连接Kafka，需要设置SSL相关配置 - SASL_SSL：使用SASL及SSL加密认证方式，需要设置SSL及SASL相关参数配置信息  **默认取值**：  不涉及
        :type type: str
        :param trust_store_key_name: **参数解释**：  证书名称。  **约束限制**：  - 安全协议为SSL、SASL_SSL时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type trust_store_key_name: str
        :param trust_store_key: **参数解释**：  安全证书base64转码后的值。  **约束限制**：  - 安全协议为SSL、SASL_SSL时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type trust_store_key: str
        :param trust_store_password: **参数解释**：  证书密码。  **约束限制**：  - 证书设置了密码时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type trust_store_password: str
        :param endpoint_algorithm: **参数解释**：  主机名端点识别算法，指定通过服务端证书验证服务端主机名的端点识别算法，对应Kafka字段：ssl.endpoint.identification.algorithm。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不填表示禁用主机名验证
        :type endpoint_algorithm: str
        :param sasl_mechanism: **参数解释**：  SASL机制，用于客户端连接的SASL机制，对应Kafka字段：sasl.mechanism。  **约束限制**：  - 认证类型为SASL_PLAINTEXT、SASL_SSL时必填。  **取值范围**：  - GSSAPI：GSSAPI机制 - PLAIN：PLAIN机制 - SCRAM-SHA-256：SCRAM-SHA-256机制 - SCRAM-SHA-512：SCRAM-SHA-512机制  **默认取值**：  不涉及
        :type sasl_mechanism: str
        :param delegation_tokens: **参数解释**：  是否为委托令牌鉴权。  **约束限制**：  - 安全协议为SASL_SSL和SASL_PLAINTEXT时，SASL机制选择SCRAM-SHA-256或者SCRAM-SHA-512时生效。  **取值范围**：  - true：使用委托令牌鉴权 - false：不使用委托令牌鉴权  **默认取值**：  不涉及
        :type delegation_tokens: bool
        :param enable_key_store: **参数解释**：  是否开启SSL双向认证。  **约束限制**：  不涉及。  **取值范围**：  - true：开启SSL双向认证 - false：不开启SSL双向认证  **默认取值**：  不涉及
        :type enable_key_store: bool
        :param key_store_key: **参数解释**：  Keystore证书。  **约束限制**：  - 开启SSL双向认证时需要。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type key_store_key: str
        :param key_store_key_name: **参数解释**：  Keystore证书名称。  **约束限制**：  - 开启SSL双向认证时需要。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type key_store_key_name: str
        :param key_store_password: **参数解释**：  Keystore证书密码，对应Kafka字段：ssl.keystore.password。  **约束限制**：  - 证书设置了密码时需要。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type key_store_password: str
        :param set_private_key_password: **参数解释**：  是否设置Keystore私钥密码。  **约束限制**：  不涉及。  **取值范围**：  - true：设置Keystore私钥密码 - false：不设置Keystore私钥密码  **默认取值**：  false
        :type set_private_key_password: bool
        :param key_password: **参数解释**：  Keystore私钥密码，对应Kafka字段：ssl.key.password。  **约束限制**：  - 开启SSL双向认证时，set_private_key_password为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type key_password: str
        """
        
        

        self._type = None
        self._trust_store_key_name = None
        self._trust_store_key = None
        self._trust_store_password = None
        self._endpoint_algorithm = None
        self._sasl_mechanism = None
        self._delegation_tokens = None
        self._enable_key_store = None
        self._key_store_key = None
        self._key_store_key_name = None
        self._key_store_password = None
        self._set_private_key_password = None
        self._key_password = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if trust_store_key_name is not None:
            self.trust_store_key_name = trust_store_key_name
        if trust_store_key is not None:
            self.trust_store_key = trust_store_key
        if trust_store_password is not None:
            self.trust_store_password = trust_store_password
        if endpoint_algorithm is not None:
            self.endpoint_algorithm = endpoint_algorithm
        if sasl_mechanism is not None:
            self.sasl_mechanism = sasl_mechanism
        if delegation_tokens is not None:
            self.delegation_tokens = delegation_tokens
        if enable_key_store is not None:
            self.enable_key_store = enable_key_store
        if key_store_key is not None:
            self.key_store_key = key_store_key
        if key_store_key_name is not None:
            self.key_store_key_name = key_store_key_name
        if key_store_password is not None:
            self.key_store_password = key_store_password
        if set_private_key_password is not None:
            self.set_private_key_password = set_private_key_password
        if key_password is not None:
            self.key_password = key_password

    @property
    def type(self):
        r"""Gets the type of this KafkaSecurity.

        **参数解释**：  安全协议类型，安全认证时必填，对应Kafka字段：security.protocol。  **约束限制**：  - 安全认证时必填。  **取值范围**：  - PLAINTEXT：无安全认证方式，仅需输入IP和端口进行连接 - SASL_PLAINTEXT：使用SASL机制连接Kafka，需要设置SASL相关配置 - SSL：使用SSL加密方式连接Kafka，需要设置SSL相关配置 - SASL_SSL：使用SASL及SSL加密认证方式，需要设置SSL及SASL相关参数配置信息  **默认取值**：  不涉及

        :return: The type of this KafkaSecurity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this KafkaSecurity.

        **参数解释**：  安全协议类型，安全认证时必填，对应Kafka字段：security.protocol。  **约束限制**：  - 安全认证时必填。  **取值范围**：  - PLAINTEXT：无安全认证方式，仅需输入IP和端口进行连接 - SASL_PLAINTEXT：使用SASL机制连接Kafka，需要设置SASL相关配置 - SSL：使用SSL加密方式连接Kafka，需要设置SSL相关配置 - SASL_SSL：使用SASL及SSL加密认证方式，需要设置SSL及SASL相关参数配置信息  **默认取值**：  不涉及

        :param type: The type of this KafkaSecurity.
        :type type: str
        """
        self._type = type

    @property
    def trust_store_key_name(self):
        r"""Gets the trust_store_key_name of this KafkaSecurity.

        **参数解释**：  证书名称。  **约束限制**：  - 安全协议为SSL、SASL_SSL时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The trust_store_key_name of this KafkaSecurity.
        :rtype: str
        """
        return self._trust_store_key_name

    @trust_store_key_name.setter
    def trust_store_key_name(self, trust_store_key_name):
        r"""Sets the trust_store_key_name of this KafkaSecurity.

        **参数解释**：  证书名称。  **约束限制**：  - 安全协议为SSL、SASL_SSL时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param trust_store_key_name: The trust_store_key_name of this KafkaSecurity.
        :type trust_store_key_name: str
        """
        self._trust_store_key_name = trust_store_key_name

    @property
    def trust_store_key(self):
        r"""Gets the trust_store_key of this KafkaSecurity.

        **参数解释**：  安全证书base64转码后的值。  **约束限制**：  - 安全协议为SSL、SASL_SSL时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The trust_store_key of this KafkaSecurity.
        :rtype: str
        """
        return self._trust_store_key

    @trust_store_key.setter
    def trust_store_key(self, trust_store_key):
        r"""Sets the trust_store_key of this KafkaSecurity.

        **参数解释**：  安全证书base64转码后的值。  **约束限制**：  - 安全协议为SSL、SASL_SSL时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param trust_store_key: The trust_store_key of this KafkaSecurity.
        :type trust_store_key: str
        """
        self._trust_store_key = trust_store_key

    @property
    def trust_store_password(self):
        r"""Gets the trust_store_password of this KafkaSecurity.

        **参数解释**：  证书密码。  **约束限制**：  - 证书设置了密码时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The trust_store_password of this KafkaSecurity.
        :rtype: str
        """
        return self._trust_store_password

    @trust_store_password.setter
    def trust_store_password(self, trust_store_password):
        r"""Sets the trust_store_password of this KafkaSecurity.

        **参数解释**：  证书密码。  **约束限制**：  - 证书设置了密码时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param trust_store_password: The trust_store_password of this KafkaSecurity.
        :type trust_store_password: str
        """
        self._trust_store_password = trust_store_password

    @property
    def endpoint_algorithm(self):
        r"""Gets the endpoint_algorithm of this KafkaSecurity.

        **参数解释**：  主机名端点识别算法，指定通过服务端证书验证服务端主机名的端点识别算法，对应Kafka字段：ssl.endpoint.identification.algorithm。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不填表示禁用主机名验证

        :return: The endpoint_algorithm of this KafkaSecurity.
        :rtype: str
        """
        return self._endpoint_algorithm

    @endpoint_algorithm.setter
    def endpoint_algorithm(self, endpoint_algorithm):
        r"""Sets the endpoint_algorithm of this KafkaSecurity.

        **参数解释**：  主机名端点识别算法，指定通过服务端证书验证服务端主机名的端点识别算法，对应Kafka字段：ssl.endpoint.identification.algorithm。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不填表示禁用主机名验证

        :param endpoint_algorithm: The endpoint_algorithm of this KafkaSecurity.
        :type endpoint_algorithm: str
        """
        self._endpoint_algorithm = endpoint_algorithm

    @property
    def sasl_mechanism(self):
        r"""Gets the sasl_mechanism of this KafkaSecurity.

        **参数解释**：  SASL机制，用于客户端连接的SASL机制，对应Kafka字段：sasl.mechanism。  **约束限制**：  - 认证类型为SASL_PLAINTEXT、SASL_SSL时必填。  **取值范围**：  - GSSAPI：GSSAPI机制 - PLAIN：PLAIN机制 - SCRAM-SHA-256：SCRAM-SHA-256机制 - SCRAM-SHA-512：SCRAM-SHA-512机制  **默认取值**：  不涉及

        :return: The sasl_mechanism of this KafkaSecurity.
        :rtype: str
        """
        return self._sasl_mechanism

    @sasl_mechanism.setter
    def sasl_mechanism(self, sasl_mechanism):
        r"""Sets the sasl_mechanism of this KafkaSecurity.

        **参数解释**：  SASL机制，用于客户端连接的SASL机制，对应Kafka字段：sasl.mechanism。  **约束限制**：  - 认证类型为SASL_PLAINTEXT、SASL_SSL时必填。  **取值范围**：  - GSSAPI：GSSAPI机制 - PLAIN：PLAIN机制 - SCRAM-SHA-256：SCRAM-SHA-256机制 - SCRAM-SHA-512：SCRAM-SHA-512机制  **默认取值**：  不涉及

        :param sasl_mechanism: The sasl_mechanism of this KafkaSecurity.
        :type sasl_mechanism: str
        """
        self._sasl_mechanism = sasl_mechanism

    @property
    def delegation_tokens(self):
        r"""Gets the delegation_tokens of this KafkaSecurity.

        **参数解释**：  是否为委托令牌鉴权。  **约束限制**：  - 安全协议为SASL_SSL和SASL_PLAINTEXT时，SASL机制选择SCRAM-SHA-256或者SCRAM-SHA-512时生效。  **取值范围**：  - true：使用委托令牌鉴权 - false：不使用委托令牌鉴权  **默认取值**：  不涉及

        :return: The delegation_tokens of this KafkaSecurity.
        :rtype: bool
        """
        return self._delegation_tokens

    @delegation_tokens.setter
    def delegation_tokens(self, delegation_tokens):
        r"""Sets the delegation_tokens of this KafkaSecurity.

        **参数解释**：  是否为委托令牌鉴权。  **约束限制**：  - 安全协议为SASL_SSL和SASL_PLAINTEXT时，SASL机制选择SCRAM-SHA-256或者SCRAM-SHA-512时生效。  **取值范围**：  - true：使用委托令牌鉴权 - false：不使用委托令牌鉴权  **默认取值**：  不涉及

        :param delegation_tokens: The delegation_tokens of this KafkaSecurity.
        :type delegation_tokens: bool
        """
        self._delegation_tokens = delegation_tokens

    @property
    def enable_key_store(self):
        r"""Gets the enable_key_store of this KafkaSecurity.

        **参数解释**：  是否开启SSL双向认证。  **约束限制**：  不涉及。  **取值范围**：  - true：开启SSL双向认证 - false：不开启SSL双向认证  **默认取值**：  不涉及

        :return: The enable_key_store of this KafkaSecurity.
        :rtype: bool
        """
        return self._enable_key_store

    @enable_key_store.setter
    def enable_key_store(self, enable_key_store):
        r"""Sets the enable_key_store of this KafkaSecurity.

        **参数解释**：  是否开启SSL双向认证。  **约束限制**：  不涉及。  **取值范围**：  - true：开启SSL双向认证 - false：不开启SSL双向认证  **默认取值**：  不涉及

        :param enable_key_store: The enable_key_store of this KafkaSecurity.
        :type enable_key_store: bool
        """
        self._enable_key_store = enable_key_store

    @property
    def key_store_key(self):
        r"""Gets the key_store_key of this KafkaSecurity.

        **参数解释**：  Keystore证书。  **约束限制**：  - 开启SSL双向认证时需要。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The key_store_key of this KafkaSecurity.
        :rtype: str
        """
        return self._key_store_key

    @key_store_key.setter
    def key_store_key(self, key_store_key):
        r"""Sets the key_store_key of this KafkaSecurity.

        **参数解释**：  Keystore证书。  **约束限制**：  - 开启SSL双向认证时需要。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param key_store_key: The key_store_key of this KafkaSecurity.
        :type key_store_key: str
        """
        self._key_store_key = key_store_key

    @property
    def key_store_key_name(self):
        r"""Gets the key_store_key_name of this KafkaSecurity.

        **参数解释**：  Keystore证书名称。  **约束限制**：  - 开启SSL双向认证时需要。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The key_store_key_name of this KafkaSecurity.
        :rtype: str
        """
        return self._key_store_key_name

    @key_store_key_name.setter
    def key_store_key_name(self, key_store_key_name):
        r"""Sets the key_store_key_name of this KafkaSecurity.

        **参数解释**：  Keystore证书名称。  **约束限制**：  - 开启SSL双向认证时需要。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param key_store_key_name: The key_store_key_name of this KafkaSecurity.
        :type key_store_key_name: str
        """
        self._key_store_key_name = key_store_key_name

    @property
    def key_store_password(self):
        r"""Gets the key_store_password of this KafkaSecurity.

        **参数解释**：  Keystore证书密码，对应Kafka字段：ssl.keystore.password。  **约束限制**：  - 证书设置了密码时需要。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The key_store_password of this KafkaSecurity.
        :rtype: str
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        r"""Sets the key_store_password of this KafkaSecurity.

        **参数解释**：  Keystore证书密码，对应Kafka字段：ssl.keystore.password。  **约束限制**：  - 证书设置了密码时需要。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param key_store_password: The key_store_password of this KafkaSecurity.
        :type key_store_password: str
        """
        self._key_store_password = key_store_password

    @property
    def set_private_key_password(self):
        r"""Gets the set_private_key_password of this KafkaSecurity.

        **参数解释**：  是否设置Keystore私钥密码。  **约束限制**：  不涉及。  **取值范围**：  - true：设置Keystore私钥密码 - false：不设置Keystore私钥密码  **默认取值**：  false

        :return: The set_private_key_password of this KafkaSecurity.
        :rtype: bool
        """
        return self._set_private_key_password

    @set_private_key_password.setter
    def set_private_key_password(self, set_private_key_password):
        r"""Sets the set_private_key_password of this KafkaSecurity.

        **参数解释**：  是否设置Keystore私钥密码。  **约束限制**：  不涉及。  **取值范围**：  - true：设置Keystore私钥密码 - false：不设置Keystore私钥密码  **默认取值**：  false

        :param set_private_key_password: The set_private_key_password of this KafkaSecurity.
        :type set_private_key_password: bool
        """
        self._set_private_key_password = set_private_key_password

    @property
    def key_password(self):
        r"""Gets the key_password of this KafkaSecurity.

        **参数解释**：  Keystore私钥密码，对应Kafka字段：ssl.key.password。  **约束限制**：  - 开启SSL双向认证时，set_private_key_password为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The key_password of this KafkaSecurity.
        :rtype: str
        """
        return self._key_password

    @key_password.setter
    def key_password(self, key_password):
        r"""Sets the key_password of this KafkaSecurity.

        **参数解释**：  Keystore私钥密码，对应Kafka字段：ssl.key.password。  **约束限制**：  - 开启SSL双向认证时，set_private_key_password为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param key_password: The key_password of this KafkaSecurity.
        :type key_password: str
        """
        self._key_password = key_password

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
        if not isinstance(other, KafkaSecurity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
