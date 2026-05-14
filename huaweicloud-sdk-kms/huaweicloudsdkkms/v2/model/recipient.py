# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Recipient:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attestation_document': 'str',
        'key_encryption_algorithm': 'str'
    }

    attribute_map = {
        'attestation_document': 'attestation_document',
        'key_encryption_algorithm': 'key_encryption_algorithm'
    }

    def __init__(self, attestation_document=None, key_encryption_algorithm=None):
        r"""Recipient

        The model defined in huaweicloud sdk

        :param attestation_document: 擎天机密计算证明文档
        :type attestation_document: str
        :param key_encryption_algorithm: 指定加密算法，仅支持RSAES_OAEP_SHA_256
        :type key_encryption_algorithm: str
        """
        
        

        self._attestation_document = None
        self._key_encryption_algorithm = None
        self.discriminator = None

        if attestation_document is not None:
            self.attestation_document = attestation_document
        if key_encryption_algorithm is not None:
            self.key_encryption_algorithm = key_encryption_algorithm

    @property
    def attestation_document(self):
        r"""Gets the attestation_document of this Recipient.

        擎天机密计算证明文档

        :return: The attestation_document of this Recipient.
        :rtype: str
        """
        return self._attestation_document

    @attestation_document.setter
    def attestation_document(self, attestation_document):
        r"""Sets the attestation_document of this Recipient.

        擎天机密计算证明文档

        :param attestation_document: The attestation_document of this Recipient.
        :type attestation_document: str
        """
        self._attestation_document = attestation_document

    @property
    def key_encryption_algorithm(self):
        r"""Gets the key_encryption_algorithm of this Recipient.

        指定加密算法，仅支持RSAES_OAEP_SHA_256

        :return: The key_encryption_algorithm of this Recipient.
        :rtype: str
        """
        return self._key_encryption_algorithm

    @key_encryption_algorithm.setter
    def key_encryption_algorithm(self, key_encryption_algorithm):
        r"""Sets the key_encryption_algorithm of this Recipient.

        指定加密算法，仅支持RSAES_OAEP_SHA_256

        :param key_encryption_algorithm: The key_encryption_algorithm of this Recipient.
        :type key_encryption_algorithm: str
        """
        self._key_encryption_algorithm = key_encryption_algorithm

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
        if not isinstance(other, Recipient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
