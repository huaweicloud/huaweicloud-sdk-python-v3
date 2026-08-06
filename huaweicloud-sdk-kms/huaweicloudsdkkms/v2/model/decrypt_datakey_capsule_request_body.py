# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DecryptDatakeyCapsuleRequestBody:

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
        'public_key': 'str',
        'datakey_capsule': 'str',
        'attestation_document': 'DecryptDatakeyCapsuleRequestBodyAttestationDocument'
    }

    attribute_map = {
        'key_id': 'key_id',
        'public_key': 'public_key',
        'datakey_capsule': 'datakey_capsule',
        'attestation_document': 'attestation_document'
    }

    def __init__(self, key_id=None, public_key=None, datakey_capsule=None, attestation_document=None):
        r"""DecryptDatakeyCapsuleRequestBody

        The model defined in huaweicloud sdk

        :param key_id: **参数解释：** 密钥ID **约束限制：** UUID格式，满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及
        :type key_id: str
        :param public_key: **参数解释：** 公钥信息，使用RSAES_OAEP_SHA_256算法加密；如果传递了public_key，KMS会使用该公钥对明文数据密钥进行加密，并返回加密后的数据密钥 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type public_key: str
        :param datakey_capsule: **参数解释：** 密钥胶囊 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type datakey_capsule: str
        :param attestation_document: 
        :type attestation_document: :class:`huaweicloudsdkkms.v2.DecryptDatakeyCapsuleRequestBodyAttestationDocument`
        """
        
        

        self._key_id = None
        self._public_key = None
        self._datakey_capsule = None
        self._attestation_document = None
        self.discriminator = None

        self.key_id = key_id
        if public_key is not None:
            self.public_key = public_key
        self.datakey_capsule = datakey_capsule
        self.attestation_document = attestation_document

    @property
    def key_id(self):
        r"""Gets the key_id of this DecryptDatakeyCapsuleRequestBody.

        **参数解释：** 密钥ID **约束限制：** UUID格式，满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The key_id of this DecryptDatakeyCapsuleRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this DecryptDatakeyCapsuleRequestBody.

        **参数解释：** 密钥ID **约束限制：** UUID格式，满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :param key_id: The key_id of this DecryptDatakeyCapsuleRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def public_key(self):
        r"""Gets the public_key of this DecryptDatakeyCapsuleRequestBody.

        **参数解释：** 公钥信息，使用RSAES_OAEP_SHA_256算法加密；如果传递了public_key，KMS会使用该公钥对明文数据密钥进行加密，并返回加密后的数据密钥 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The public_key of this DecryptDatakeyCapsuleRequestBody.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        r"""Sets the public_key of this DecryptDatakeyCapsuleRequestBody.

        **参数解释：** 公钥信息，使用RSAES_OAEP_SHA_256算法加密；如果传递了public_key，KMS会使用该公钥对明文数据密钥进行加密，并返回加密后的数据密钥 **约束限制：** 仅支持RSA公钥 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param public_key: The public_key of this DecryptDatakeyCapsuleRequestBody.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def datakey_capsule(self):
        r"""Gets the datakey_capsule of this DecryptDatakeyCapsuleRequestBody.

        **参数解释：** 密钥胶囊 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The datakey_capsule of this DecryptDatakeyCapsuleRequestBody.
        :rtype: str
        """
        return self._datakey_capsule

    @datakey_capsule.setter
    def datakey_capsule(self, datakey_capsule):
        r"""Sets the datakey_capsule of this DecryptDatakeyCapsuleRequestBody.

        **参数解释：** 密钥胶囊 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param datakey_capsule: The datakey_capsule of this DecryptDatakeyCapsuleRequestBody.
        :type datakey_capsule: str
        """
        self._datakey_capsule = datakey_capsule

    @property
    def attestation_document(self):
        r"""Gets the attestation_document of this DecryptDatakeyCapsuleRequestBody.

        :return: The attestation_document of this DecryptDatakeyCapsuleRequestBody.
        :rtype: :class:`huaweicloudsdkkms.v2.DecryptDatakeyCapsuleRequestBodyAttestationDocument`
        """
        return self._attestation_document

    @attestation_document.setter
    def attestation_document(self, attestation_document):
        r"""Sets the attestation_document of this DecryptDatakeyCapsuleRequestBody.

        :param attestation_document: The attestation_document of this DecryptDatakeyCapsuleRequestBody.
        :type attestation_document: :class:`huaweicloudsdkkms.v2.DecryptDatakeyCapsuleRequestBodyAttestationDocument`
        """
        self._attestation_document = attestation_document

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
        if not isinstance(other, DecryptDatakeyCapsuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
