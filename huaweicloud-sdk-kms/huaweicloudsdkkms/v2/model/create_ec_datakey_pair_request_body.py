# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEcDatakeyPairRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'key_spec': 'str',
        'with_plain_text': 'bool',
        'additional_authenticated_data': 'str',
        'sequence': 'str',
        'pin': 'str',
        'pin_type': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'key_spec': 'key_spec',
        'with_plain_text': 'with_plain_text',
        'additional_authenticated_data': 'additional_authenticated_data',
        'sequence': 'sequence',
        'pin': 'pin',
        'pin_type': 'pin_type'
    }

    def __init__(self, key_id=None, key_spec=None, with_plain_text=None, additional_authenticated_data=None, sequence=None, pin=None, pin_type=None):
        r"""CreateEcDatakeyPairRequestBody

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。
        :type key_id: str
        :param key_spec: 需要包含算法、长度、曲线信息。可选值有ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SM2
        :type key_spec: str
        :param with_plain_text: 是否返回明文私钥，默认为true
        :type with_plain_text: bool
        :param additional_authenticated_data: 认证加密的额外信息，请不要填写敏感信息
        :type additional_authenticated_data: str
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        :param pin: 指定PIN码保护。仅四级密评场景支持该参数。
        :type pin: str
        :param pin_type: pin码的类型，默认为“CipherText”，可选“PlainText”。仅四级密评场景支持该参数。
        :type pin_type: str
        """
        
        

        self._key_id = None
        self._key_spec = None
        self._with_plain_text = None
        self._additional_authenticated_data = None
        self._sequence = None
        self._pin = None
        self._pin_type = None
        self.discriminator = None

        self.key_id = key_id
        self.key_spec = key_spec
        if with_plain_text is not None:
            self.with_plain_text = with_plain_text
        if additional_authenticated_data is not None:
            self.additional_authenticated_data = additional_authenticated_data
        if sequence is not None:
            self.sequence = sequence
        if pin is not None:
            self.pin = pin
        if pin_type is not None:
            self.pin_type = pin_type

    @property
    def key_id(self):
        r"""Gets the key_id of this CreateEcDatakeyPairRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this CreateEcDatakeyPairRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this CreateEcDatakeyPairRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this CreateEcDatakeyPairRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def key_spec(self):
        r"""Gets the key_spec of this CreateEcDatakeyPairRequestBody.

        需要包含算法、长度、曲线信息。可选值有ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SM2

        :return: The key_spec of this CreateEcDatakeyPairRequestBody.
        :rtype: str
        """
        return self._key_spec

    @key_spec.setter
    def key_spec(self, key_spec):
        r"""Sets the key_spec of this CreateEcDatakeyPairRequestBody.

        需要包含算法、长度、曲线信息。可选值有ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SM2

        :param key_spec: The key_spec of this CreateEcDatakeyPairRequestBody.
        :type key_spec: str
        """
        self._key_spec = key_spec

    @property
    def with_plain_text(self):
        r"""Gets the with_plain_text of this CreateEcDatakeyPairRequestBody.

        是否返回明文私钥，默认为true

        :return: The with_plain_text of this CreateEcDatakeyPairRequestBody.
        :rtype: bool
        """
        return self._with_plain_text

    @with_plain_text.setter
    def with_plain_text(self, with_plain_text):
        r"""Sets the with_plain_text of this CreateEcDatakeyPairRequestBody.

        是否返回明文私钥，默认为true

        :param with_plain_text: The with_plain_text of this CreateEcDatakeyPairRequestBody.
        :type with_plain_text: bool
        """
        self._with_plain_text = with_plain_text

    @property
    def additional_authenticated_data(self):
        r"""Gets the additional_authenticated_data of this CreateEcDatakeyPairRequestBody.

        认证加密的额外信息，请不要填写敏感信息

        :return: The additional_authenticated_data of this CreateEcDatakeyPairRequestBody.
        :rtype: str
        """
        return self._additional_authenticated_data

    @additional_authenticated_data.setter
    def additional_authenticated_data(self, additional_authenticated_data):
        r"""Sets the additional_authenticated_data of this CreateEcDatakeyPairRequestBody.

        认证加密的额外信息，请不要填写敏感信息

        :param additional_authenticated_data: The additional_authenticated_data of this CreateEcDatakeyPairRequestBody.
        :type additional_authenticated_data: str
        """
        self._additional_authenticated_data = additional_authenticated_data

    @property
    def sequence(self):
        r"""Gets the sequence of this CreateEcDatakeyPairRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this CreateEcDatakeyPairRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this CreateEcDatakeyPairRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this CreateEcDatakeyPairRequestBody.
        :type sequence: str
        """
        self._sequence = sequence

    @property
    def pin(self):
        r"""Gets the pin of this CreateEcDatakeyPairRequestBody.

        指定PIN码保护。仅四级密评场景支持该参数。

        :return: The pin of this CreateEcDatakeyPairRequestBody.
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        r"""Sets the pin of this CreateEcDatakeyPairRequestBody.

        指定PIN码保护。仅四级密评场景支持该参数。

        :param pin: The pin of this CreateEcDatakeyPairRequestBody.
        :type pin: str
        """
        self._pin = pin

    @property
    def pin_type(self):
        r"""Gets the pin_type of this CreateEcDatakeyPairRequestBody.

        pin码的类型，默认为“CipherText”，可选“PlainText”。仅四级密评场景支持该参数。

        :return: The pin_type of this CreateEcDatakeyPairRequestBody.
        :rtype: str
        """
        return self._pin_type

    @pin_type.setter
    def pin_type(self, pin_type):
        r"""Sets the pin_type of this CreateEcDatakeyPairRequestBody.

        pin码的类型，默认为“CipherText”，可选“PlainText”。仅四级密评场景支持该参数。

        :param pin_type: The pin_type of this CreateEcDatakeyPairRequestBody.
        :type pin_type: str
        """
        self._pin_type = pin_type

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
        if not isinstance(other, CreateEcDatakeyPairRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
