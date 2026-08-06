# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatakeyCapsuleRequestBody:

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
        'datakey_length': 'str',
        'public_key': 'str',
        'policy_id': 'str',
        'key_policy': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'datakey_length': 'datakey_length',
        'public_key': 'public_key',
        'policy_id': 'policy_id',
        'key_policy': 'key_policy'
    }

    def __init__(self, key_id=None, datakey_length=None, public_key=None, policy_id=None, key_policy=None):
        r"""CreateDatakeyCapsuleRequestBody

        The model defined in huaweicloud sdk

        :param key_id: **参数解释：** 密钥ID **约束限制：** UUID格式，满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及
        :type key_id: str
        :param datakey_length: **参数解释：** 待创建的数据密钥长度 **约束限制：** 256或者128二选一 **取值范围：** - 128 - 256 **默认取值：** 不涉及
        :type datakey_length: str
        :param public_key: **参数解释：** 公钥信息，使用RSAES_OAEP_SHA_256算法加密；如果传递了public_key，KMS会使用该公钥对明文数据密钥进行加密，并返回加密后的数据密钥 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type public_key: str
        :param policy_id: **参数解释：** 密钥策略ID和内联的密钥策略二选一 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_id: str
        :param key_policy: **参数解释：** 密钥策略ID和内联的密钥策略二选一 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type key_policy: str
        """
        
        

        self._key_id = None
        self._datakey_length = None
        self._public_key = None
        self._policy_id = None
        self._key_policy = None
        self.discriminator = None

        self.key_id = key_id
        self.datakey_length = datakey_length
        if public_key is not None:
            self.public_key = public_key
        if policy_id is not None:
            self.policy_id = policy_id
        if key_policy is not None:
            self.key_policy = key_policy

    @property
    def key_id(self):
        r"""Gets the key_id of this CreateDatakeyCapsuleRequestBody.

        **参数解释：** 密钥ID **约束限制：** UUID格式，满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The key_id of this CreateDatakeyCapsuleRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this CreateDatakeyCapsuleRequestBody.

        **参数解释：** 密钥ID **约束限制：** UUID格式，满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :param key_id: The key_id of this CreateDatakeyCapsuleRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def datakey_length(self):
        r"""Gets the datakey_length of this CreateDatakeyCapsuleRequestBody.

        **参数解释：** 待创建的数据密钥长度 **约束限制：** 256或者128二选一 **取值范围：** - 128 - 256 **默认取值：** 不涉及

        :return: The datakey_length of this CreateDatakeyCapsuleRequestBody.
        :rtype: str
        """
        return self._datakey_length

    @datakey_length.setter
    def datakey_length(self, datakey_length):
        r"""Sets the datakey_length of this CreateDatakeyCapsuleRequestBody.

        **参数解释：** 待创建的数据密钥长度 **约束限制：** 256或者128二选一 **取值范围：** - 128 - 256 **默认取值：** 不涉及

        :param datakey_length: The datakey_length of this CreateDatakeyCapsuleRequestBody.
        :type datakey_length: str
        """
        self._datakey_length = datakey_length

    @property
    def public_key(self):
        r"""Gets the public_key of this CreateDatakeyCapsuleRequestBody.

        **参数解释：** 公钥信息，使用RSAES_OAEP_SHA_256算法加密；如果传递了public_key，KMS会使用该公钥对明文数据密钥进行加密，并返回加密后的数据密钥 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The public_key of this CreateDatakeyCapsuleRequestBody.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        r"""Sets the public_key of this CreateDatakeyCapsuleRequestBody.

        **参数解释：** 公钥信息，使用RSAES_OAEP_SHA_256算法加密；如果传递了public_key，KMS会使用该公钥对明文数据密钥进行加密，并返回加密后的数据密钥 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param public_key: The public_key of this CreateDatakeyCapsuleRequestBody.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def policy_id(self):
        r"""Gets the policy_id of this CreateDatakeyCapsuleRequestBody.

        **参数解释：** 密钥策略ID和内联的密钥策略二选一 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_id of this CreateDatakeyCapsuleRequestBody.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this CreateDatakeyCapsuleRequestBody.

        **参数解释：** 密钥策略ID和内联的密钥策略二选一 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_id: The policy_id of this CreateDatakeyCapsuleRequestBody.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def key_policy(self):
        r"""Gets the key_policy of this CreateDatakeyCapsuleRequestBody.

        **参数解释：** 密钥策略ID和内联的密钥策略二选一 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The key_policy of this CreateDatakeyCapsuleRequestBody.
        :rtype: str
        """
        return self._key_policy

    @key_policy.setter
    def key_policy(self, key_policy):
        r"""Sets the key_policy of this CreateDatakeyCapsuleRequestBody.

        **参数解释：** 密钥策略ID和内联的密钥策略二选一 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param key_policy: The key_policy of this CreateDatakeyCapsuleRequestBody.
        :type key_policy: str
        """
        self._key_policy = key_policy

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
        if not isinstance(other, CreateDatakeyCapsuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
