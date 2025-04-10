# coding: utf-8

import six

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

        :param type: 安全协议，安全认证时必填，对应Kafka字段：security.protocol。 - PLAINTEXT：无安全认证方式，仅需输入IP和端口进行连接。 - SASL_PLAINTEXT：使用SASL机制连接Kafka，需要设置SASL相关配置。 - SSL：使用SSL加密方式连接Kafka，需要设置SSL相关配置。 - SASL_SSL：使用SASL及SSL加密认证方式，需要设置SSL及SASL相关参数配置信息。
        :type type: str
        :param trust_store_key_name: 证书名称，安全协议为SSL、SASL_SSL时必填。
        :type trust_store_key_name: str
        :param trust_store_key: 安全证书base64转码后的值，安全协议为SSL、SASL_SSL时必填。
        :type trust_store_key: str
        :param trust_store_password: 证书密码，证书设置了密码时必填。
        :type trust_store_password: str
        :param endpoint_algorithm: 主机名端点识别算法，指定通过服务端证书验证服务端主机名的端点识别算法，不填表示禁用主机名验证。对应Kafka字段：ssl.endpoint.identification.algorithm。
        :type endpoint_algorithm: str
        :param sasl_mechanism: SASL机制，用于客户端连接的SASL机制，对应Kafka字段：sasl.mechanism，支持以下四项，取值： - GSSAPI - PLAIN - SCRAM-SHA-256 - SCRAM-SHA-512
        :type sasl_mechanism: str
        :param delegation_tokens: 是否为委托令牌鉴权，安全协议为SASL_SSL和SASL_PLAINTEXT时，SASL机制选择“SCRAM-SHA-256”或者“SCRAM-SHA-512”时生效。
        :type delegation_tokens: bool
        :param enable_key_store: 是否开启SSL双向认证。
        :type enable_key_store: bool
        :param key_store_key: Keystore证书，开启SSL双向认证时需要。
        :type key_store_key: str
        :param key_store_key_name: Keystore证书名称，开启SSL双向认证时需要。
        :type key_store_key_name: str
        :param key_store_password: Keystore证书密码，证书设置了密码时需要。对应Kafka字段：ssl.keystore.password。
        :type key_store_password: str
        :param set_private_key_password: 是否设置Keystore私钥密码，默认为false。
        :type set_private_key_password: bool
        :param key_password: Keystore私钥密码，开启SSL双向认证时，set_private_key_password为true时必填。对应Kafka字段：ssl.key.password。
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

        安全协议，安全认证时必填，对应Kafka字段：security.protocol。 - PLAINTEXT：无安全认证方式，仅需输入IP和端口进行连接。 - SASL_PLAINTEXT：使用SASL机制连接Kafka，需要设置SASL相关配置。 - SSL：使用SSL加密方式连接Kafka，需要设置SSL相关配置。 - SASL_SSL：使用SASL及SSL加密认证方式，需要设置SSL及SASL相关参数配置信息。

        :return: The type of this KafkaSecurity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this KafkaSecurity.

        安全协议，安全认证时必填，对应Kafka字段：security.protocol。 - PLAINTEXT：无安全认证方式，仅需输入IP和端口进行连接。 - SASL_PLAINTEXT：使用SASL机制连接Kafka，需要设置SASL相关配置。 - SSL：使用SSL加密方式连接Kafka，需要设置SSL相关配置。 - SASL_SSL：使用SASL及SSL加密认证方式，需要设置SSL及SASL相关参数配置信息。

        :param type: The type of this KafkaSecurity.
        :type type: str
        """
        self._type = type

    @property
    def trust_store_key_name(self):
        r"""Gets the trust_store_key_name of this KafkaSecurity.

        证书名称，安全协议为SSL、SASL_SSL时必填。

        :return: The trust_store_key_name of this KafkaSecurity.
        :rtype: str
        """
        return self._trust_store_key_name

    @trust_store_key_name.setter
    def trust_store_key_name(self, trust_store_key_name):
        r"""Sets the trust_store_key_name of this KafkaSecurity.

        证书名称，安全协议为SSL、SASL_SSL时必填。

        :param trust_store_key_name: The trust_store_key_name of this KafkaSecurity.
        :type trust_store_key_name: str
        """
        self._trust_store_key_name = trust_store_key_name

    @property
    def trust_store_key(self):
        r"""Gets the trust_store_key of this KafkaSecurity.

        安全证书base64转码后的值，安全协议为SSL、SASL_SSL时必填。

        :return: The trust_store_key of this KafkaSecurity.
        :rtype: str
        """
        return self._trust_store_key

    @trust_store_key.setter
    def trust_store_key(self, trust_store_key):
        r"""Sets the trust_store_key of this KafkaSecurity.

        安全证书base64转码后的值，安全协议为SSL、SASL_SSL时必填。

        :param trust_store_key: The trust_store_key of this KafkaSecurity.
        :type trust_store_key: str
        """
        self._trust_store_key = trust_store_key

    @property
    def trust_store_password(self):
        r"""Gets the trust_store_password of this KafkaSecurity.

        证书密码，证书设置了密码时必填。

        :return: The trust_store_password of this KafkaSecurity.
        :rtype: str
        """
        return self._trust_store_password

    @trust_store_password.setter
    def trust_store_password(self, trust_store_password):
        r"""Sets the trust_store_password of this KafkaSecurity.

        证书密码，证书设置了密码时必填。

        :param trust_store_password: The trust_store_password of this KafkaSecurity.
        :type trust_store_password: str
        """
        self._trust_store_password = trust_store_password

    @property
    def endpoint_algorithm(self):
        r"""Gets the endpoint_algorithm of this KafkaSecurity.

        主机名端点识别算法，指定通过服务端证书验证服务端主机名的端点识别算法，不填表示禁用主机名验证。对应Kafka字段：ssl.endpoint.identification.algorithm。

        :return: The endpoint_algorithm of this KafkaSecurity.
        :rtype: str
        """
        return self._endpoint_algorithm

    @endpoint_algorithm.setter
    def endpoint_algorithm(self, endpoint_algorithm):
        r"""Sets the endpoint_algorithm of this KafkaSecurity.

        主机名端点识别算法，指定通过服务端证书验证服务端主机名的端点识别算法，不填表示禁用主机名验证。对应Kafka字段：ssl.endpoint.identification.algorithm。

        :param endpoint_algorithm: The endpoint_algorithm of this KafkaSecurity.
        :type endpoint_algorithm: str
        """
        self._endpoint_algorithm = endpoint_algorithm

    @property
    def sasl_mechanism(self):
        r"""Gets the sasl_mechanism of this KafkaSecurity.

        SASL机制，用于客户端连接的SASL机制，对应Kafka字段：sasl.mechanism，支持以下四项，取值： - GSSAPI - PLAIN - SCRAM-SHA-256 - SCRAM-SHA-512

        :return: The sasl_mechanism of this KafkaSecurity.
        :rtype: str
        """
        return self._sasl_mechanism

    @sasl_mechanism.setter
    def sasl_mechanism(self, sasl_mechanism):
        r"""Sets the sasl_mechanism of this KafkaSecurity.

        SASL机制，用于客户端连接的SASL机制，对应Kafka字段：sasl.mechanism，支持以下四项，取值： - GSSAPI - PLAIN - SCRAM-SHA-256 - SCRAM-SHA-512

        :param sasl_mechanism: The sasl_mechanism of this KafkaSecurity.
        :type sasl_mechanism: str
        """
        self._sasl_mechanism = sasl_mechanism

    @property
    def delegation_tokens(self):
        r"""Gets the delegation_tokens of this KafkaSecurity.

        是否为委托令牌鉴权，安全协议为SASL_SSL和SASL_PLAINTEXT时，SASL机制选择“SCRAM-SHA-256”或者“SCRAM-SHA-512”时生效。

        :return: The delegation_tokens of this KafkaSecurity.
        :rtype: bool
        """
        return self._delegation_tokens

    @delegation_tokens.setter
    def delegation_tokens(self, delegation_tokens):
        r"""Sets the delegation_tokens of this KafkaSecurity.

        是否为委托令牌鉴权，安全协议为SASL_SSL和SASL_PLAINTEXT时，SASL机制选择“SCRAM-SHA-256”或者“SCRAM-SHA-512”时生效。

        :param delegation_tokens: The delegation_tokens of this KafkaSecurity.
        :type delegation_tokens: bool
        """
        self._delegation_tokens = delegation_tokens

    @property
    def enable_key_store(self):
        r"""Gets the enable_key_store of this KafkaSecurity.

        是否开启SSL双向认证。

        :return: The enable_key_store of this KafkaSecurity.
        :rtype: bool
        """
        return self._enable_key_store

    @enable_key_store.setter
    def enable_key_store(self, enable_key_store):
        r"""Sets the enable_key_store of this KafkaSecurity.

        是否开启SSL双向认证。

        :param enable_key_store: The enable_key_store of this KafkaSecurity.
        :type enable_key_store: bool
        """
        self._enable_key_store = enable_key_store

    @property
    def key_store_key(self):
        r"""Gets the key_store_key of this KafkaSecurity.

        Keystore证书，开启SSL双向认证时需要。

        :return: The key_store_key of this KafkaSecurity.
        :rtype: str
        """
        return self._key_store_key

    @key_store_key.setter
    def key_store_key(self, key_store_key):
        r"""Sets the key_store_key of this KafkaSecurity.

        Keystore证书，开启SSL双向认证时需要。

        :param key_store_key: The key_store_key of this KafkaSecurity.
        :type key_store_key: str
        """
        self._key_store_key = key_store_key

    @property
    def key_store_key_name(self):
        r"""Gets the key_store_key_name of this KafkaSecurity.

        Keystore证书名称，开启SSL双向认证时需要。

        :return: The key_store_key_name of this KafkaSecurity.
        :rtype: str
        """
        return self._key_store_key_name

    @key_store_key_name.setter
    def key_store_key_name(self, key_store_key_name):
        r"""Sets the key_store_key_name of this KafkaSecurity.

        Keystore证书名称，开启SSL双向认证时需要。

        :param key_store_key_name: The key_store_key_name of this KafkaSecurity.
        :type key_store_key_name: str
        """
        self._key_store_key_name = key_store_key_name

    @property
    def key_store_password(self):
        r"""Gets the key_store_password of this KafkaSecurity.

        Keystore证书密码，证书设置了密码时需要。对应Kafka字段：ssl.keystore.password。

        :return: The key_store_password of this KafkaSecurity.
        :rtype: str
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        r"""Sets the key_store_password of this KafkaSecurity.

        Keystore证书密码，证书设置了密码时需要。对应Kafka字段：ssl.keystore.password。

        :param key_store_password: The key_store_password of this KafkaSecurity.
        :type key_store_password: str
        """
        self._key_store_password = key_store_password

    @property
    def set_private_key_password(self):
        r"""Gets the set_private_key_password of this KafkaSecurity.

        是否设置Keystore私钥密码，默认为false。

        :return: The set_private_key_password of this KafkaSecurity.
        :rtype: bool
        """
        return self._set_private_key_password

    @set_private_key_password.setter
    def set_private_key_password(self, set_private_key_password):
        r"""Sets the set_private_key_password of this KafkaSecurity.

        是否设置Keystore私钥密码，默认为false。

        :param set_private_key_password: The set_private_key_password of this KafkaSecurity.
        :type set_private_key_password: bool
        """
        self._set_private_key_password = set_private_key_password

    @property
    def key_password(self):
        r"""Gets the key_password of this KafkaSecurity.

        Keystore私钥密码，开启SSL双向认证时，set_private_key_password为true时必填。对应Kafka字段：ssl.key.password。

        :return: The key_password of this KafkaSecurity.
        :rtype: str
        """
        return self._key_password

    @key_password.setter
    def key_password(self, key_password):
        r"""Sets the key_password of this KafkaSecurity.

        Keystore私钥密码，开启SSL双向认证时，set_private_key_password为true时必填。对应Kafka字段：ssl.key.password。

        :param key_password: The key_password of this KafkaSecurity.
        :type key_password: str
        """
        self._key_password = key_password

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
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
