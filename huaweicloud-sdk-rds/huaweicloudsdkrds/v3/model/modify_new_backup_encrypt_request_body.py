# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyNewBackupEncryptRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kms_key': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'kms_key': 'kms_key',
        'enabled': 'enabled'
    }

    def __init__(self, kms_key=None, enabled=None):
        r"""ModifyNewBackupEncryptRequestBody

        The model defined in huaweicloud sdk

        :param kms_key: **参数解释**：  KMS密钥ID，用于备份加密。  **约束限制**：  当enabled为true时必填，当enabled为false时不需填写。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type kms_key: str
        :param enabled: **参数解释**：  是否开启备份加密。  **约束限制**：  不涉及。  **取值范围**：  - true：开启备份加密 - false：关闭备份加密  **默认取值**：  不涉及。
        :type enabled: bool
        """
        
        

        self._kms_key = None
        self._enabled = None
        self.discriminator = None

        if kms_key is not None:
            self.kms_key = kms_key
        self.enabled = enabled

    @property
    def kms_key(self):
        r"""Gets the kms_key of this ModifyNewBackupEncryptRequestBody.

        **参数解释**：  KMS密钥ID，用于备份加密。  **约束限制**：  当enabled为true时必填，当enabled为false时不需填写。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The kms_key of this ModifyNewBackupEncryptRequestBody.
        :rtype: str
        """
        return self._kms_key

    @kms_key.setter
    def kms_key(self, kms_key):
        r"""Sets the kms_key of this ModifyNewBackupEncryptRequestBody.

        **参数解释**：  KMS密钥ID，用于备份加密。  **约束限制**：  当enabled为true时必填，当enabled为false时不需填写。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param kms_key: The kms_key of this ModifyNewBackupEncryptRequestBody.
        :type kms_key: str
        """
        self._kms_key = kms_key

    @property
    def enabled(self):
        r"""Gets the enabled of this ModifyNewBackupEncryptRequestBody.

        **参数解释**：  是否开启备份加密。  **约束限制**：  不涉及。  **取值范围**：  - true：开启备份加密 - false：关闭备份加密  **默认取值**：  不涉及。

        :return: The enabled of this ModifyNewBackupEncryptRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ModifyNewBackupEncryptRequestBody.

        **参数解释**：  是否开启备份加密。  **约束限制**：  不涉及。  **取值范围**：  - true：开启备份加密 - false：关闭备份加密  **默认取值**：  不涉及。

        :param enabled: The enabled of this ModifyNewBackupEncryptRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, ModifyNewBackupEncryptRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
