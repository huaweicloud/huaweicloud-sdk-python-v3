# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KmsConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_type': 'KmsKeyType',
        'kms_key_id': 'str'
    }

    attribute_map = {
        'key_type': 'key_type',
        'kms_key_id': 'kms_key_id'
    }

    def __init__(self, key_type=None, kms_key_id=None):
        r"""KmsConfiguration

        The model defined in huaweicloud sdk

        :param key_type: 
        :type key_type: :class:`huaweicloudsdkagentidentity.v1.KmsKeyType`
        :param kms_key_id: The identifier of the KMS key used for the token vault.
        :type kms_key_id: str
        """
        
        

        self._key_type = None
        self._kms_key_id = None
        self.discriminator = None

        self.key_type = key_type
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id

    @property
    def key_type(self):
        r"""Gets the key_type of this KmsConfiguration.

        :return: The key_type of this KmsConfiguration.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.KmsKeyType`
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        r"""Sets the key_type of this KmsConfiguration.

        :param key_type: The key_type of this KmsConfiguration.
        :type key_type: :class:`huaweicloudsdkagentidentity.v1.KmsKeyType`
        """
        self._key_type = key_type

    @property
    def kms_key_id(self):
        r"""Gets the kms_key_id of this KmsConfiguration.

        The identifier of the KMS key used for the token vault.

        :return: The kms_key_id of this KmsConfiguration.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        r"""Sets the kms_key_id of this KmsConfiguration.

        The identifier of the KMS key used for the token vault.

        :param kms_key_id: The kms_key_id of this KmsConfiguration.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

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
        if not isinstance(other, KmsConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
