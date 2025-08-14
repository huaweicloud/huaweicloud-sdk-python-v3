# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatakeyRequestBody:

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
        'datakey_length': 'str',
        'additional_authenticated_data': 'str',
        'sequence': 'str',
        'pin': 'str',
        'pin_type': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'key_spec': 'key_spec',
        'datakey_length': 'datakey_length',
        'additional_authenticated_data': 'additional_authenticated_data',
        'sequence': 'sequence',
        'pin': 'pin',
        'pin_type': 'pin_type'
    }

    def __init__(self, key_id=None, key_spec=None, datakey_length=None, additional_authenticated_data=None, sequence=None, pin=None, pin_type=None):
        r"""CreateDatakeyRequestBody

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。
        :type key_id: str
        :param key_spec: 指定生成的密钥bit位长度。有效值：AES_256、AES_128、SM4、HMAC_256、HMAC_384、HMAC_512、HMAC_SM3。  - AES_256：表示256比特的对称密钥。  - AES_128：表示128比特的对称密钥。  - SM4：表示SM4密钥。  - HMAC_256：表示HMAC_256密钥。  - HMAC_384：表示HMAC_384密钥。  - HMAC_512：表示HMAC_512密钥。  - HMAC_SM3：表示HMAC_SM3密钥。     说明：  datakey_length和key_spec二选一。   - 若datakey_length和key_spec都为空，默认生成256bit的密钥。   - 若datakey_length和key_spec都指定了值，仅datakey_length生效。
        :type key_spec: str
        :param datakey_length: 密钥bit位长度。取值为8的倍数，取值范围为8~8192。 说明：  datakey_length和key_spec二选一。   - 若datakey_length和key_spec都为空，默认生成256bit的密钥。   - 若datakey_length和key_spec都指定了值，仅datakey_length生效。
        :type datakey_length: str
        :param additional_authenticated_data: 身份验证的非敏感额外数据。任意字符串，长度不超过128字节。
        :type additional_authenticated_data: str
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        :param pin: pin码，用于数据密钥的认证，仅四级密评场景生效
        :type pin: str
        :param pin_type: pin码的类型，默认为“CipherText”： - PlainText：表示明文pin - CipherText：表示密文pin
        :type pin_type: str
        """
        
        

        self._key_id = None
        self._key_spec = None
        self._datakey_length = None
        self._additional_authenticated_data = None
        self._sequence = None
        self._pin = None
        self._pin_type = None
        self.discriminator = None

        self.key_id = key_id
        if key_spec is not None:
            self.key_spec = key_spec
        if datakey_length is not None:
            self.datakey_length = datakey_length
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
        r"""Gets the key_id of this CreateDatakeyRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this CreateDatakeyRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this CreateDatakeyRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this CreateDatakeyRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def key_spec(self):
        r"""Gets the key_spec of this CreateDatakeyRequestBody.

        指定生成的密钥bit位长度。有效值：AES_256、AES_128、SM4、HMAC_256、HMAC_384、HMAC_512、HMAC_SM3。  - AES_256：表示256比特的对称密钥。  - AES_128：表示128比特的对称密钥。  - SM4：表示SM4密钥。  - HMAC_256：表示HMAC_256密钥。  - HMAC_384：表示HMAC_384密钥。  - HMAC_512：表示HMAC_512密钥。  - HMAC_SM3：表示HMAC_SM3密钥。     说明：  datakey_length和key_spec二选一。   - 若datakey_length和key_spec都为空，默认生成256bit的密钥。   - 若datakey_length和key_spec都指定了值，仅datakey_length生效。

        :return: The key_spec of this CreateDatakeyRequestBody.
        :rtype: str
        """
        return self._key_spec

    @key_spec.setter
    def key_spec(self, key_spec):
        r"""Sets the key_spec of this CreateDatakeyRequestBody.

        指定生成的密钥bit位长度。有效值：AES_256、AES_128、SM4、HMAC_256、HMAC_384、HMAC_512、HMAC_SM3。  - AES_256：表示256比特的对称密钥。  - AES_128：表示128比特的对称密钥。  - SM4：表示SM4密钥。  - HMAC_256：表示HMAC_256密钥。  - HMAC_384：表示HMAC_384密钥。  - HMAC_512：表示HMAC_512密钥。  - HMAC_SM3：表示HMAC_SM3密钥。     说明：  datakey_length和key_spec二选一。   - 若datakey_length和key_spec都为空，默认生成256bit的密钥。   - 若datakey_length和key_spec都指定了值，仅datakey_length生效。

        :param key_spec: The key_spec of this CreateDatakeyRequestBody.
        :type key_spec: str
        """
        self._key_spec = key_spec

    @property
    def datakey_length(self):
        r"""Gets the datakey_length of this CreateDatakeyRequestBody.

        密钥bit位长度。取值为8的倍数，取值范围为8~8192。 说明：  datakey_length和key_spec二选一。   - 若datakey_length和key_spec都为空，默认生成256bit的密钥。   - 若datakey_length和key_spec都指定了值，仅datakey_length生效。

        :return: The datakey_length of this CreateDatakeyRequestBody.
        :rtype: str
        """
        return self._datakey_length

    @datakey_length.setter
    def datakey_length(self, datakey_length):
        r"""Sets the datakey_length of this CreateDatakeyRequestBody.

        密钥bit位长度。取值为8的倍数，取值范围为8~8192。 说明：  datakey_length和key_spec二选一。   - 若datakey_length和key_spec都为空，默认生成256bit的密钥。   - 若datakey_length和key_spec都指定了值，仅datakey_length生效。

        :param datakey_length: The datakey_length of this CreateDatakeyRequestBody.
        :type datakey_length: str
        """
        self._datakey_length = datakey_length

    @property
    def additional_authenticated_data(self):
        r"""Gets the additional_authenticated_data of this CreateDatakeyRequestBody.

        身份验证的非敏感额外数据。任意字符串，长度不超过128字节。

        :return: The additional_authenticated_data of this CreateDatakeyRequestBody.
        :rtype: str
        """
        return self._additional_authenticated_data

    @additional_authenticated_data.setter
    def additional_authenticated_data(self, additional_authenticated_data):
        r"""Sets the additional_authenticated_data of this CreateDatakeyRequestBody.

        身份验证的非敏感额外数据。任意字符串，长度不超过128字节。

        :param additional_authenticated_data: The additional_authenticated_data of this CreateDatakeyRequestBody.
        :type additional_authenticated_data: str
        """
        self._additional_authenticated_data = additional_authenticated_data

    @property
    def sequence(self):
        r"""Gets the sequence of this CreateDatakeyRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this CreateDatakeyRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this CreateDatakeyRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this CreateDatakeyRequestBody.
        :type sequence: str
        """
        self._sequence = sequence

    @property
    def pin(self):
        r"""Gets the pin of this CreateDatakeyRequestBody.

        pin码，用于数据密钥的认证，仅四级密评场景生效

        :return: The pin of this CreateDatakeyRequestBody.
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        r"""Sets the pin of this CreateDatakeyRequestBody.

        pin码，用于数据密钥的认证，仅四级密评场景生效

        :param pin: The pin of this CreateDatakeyRequestBody.
        :type pin: str
        """
        self._pin = pin

    @property
    def pin_type(self):
        r"""Gets the pin_type of this CreateDatakeyRequestBody.

        pin码的类型，默认为“CipherText”： - PlainText：表示明文pin - CipherText：表示密文pin

        :return: The pin_type of this CreateDatakeyRequestBody.
        :rtype: str
        """
        return self._pin_type

    @pin_type.setter
    def pin_type(self, pin_type):
        r"""Sets the pin_type of this CreateDatakeyRequestBody.

        pin码的类型，默认为“CipherText”： - PlainText：表示明文pin - CipherText：表示密文pin

        :param pin_type: The pin_type of this CreateDatakeyRequestBody.
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
        if not isinstance(other, CreateDatakeyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
