# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigureVaultItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vault_id': 'str',
        'policy_id': 'str',
        'encrypted': 'bool',
        'worm': 'bool',
        'policy_enable': 'bool'
    }

    attribute_map = {
        'vault_id': 'vault_id',
        'policy_id': 'policy_id',
        'encrypted': 'encrypted',
        'worm': 'worm',
        'policy_enable': 'policy_enable'
    }

    def __init__(self, vault_id=None, policy_id=None, encrypted=None, worm=None, policy_enable=None):
        r"""ConfigureVaultItem

        The model defined in huaweicloud sdk

        :param vault_id: CBR存储库ID
        :type vault_id: str
        :param policy_id: 策略ID
        :type policy_id: str
        :param encrypted: 是否加密
        :type encrypted: bool
        :param worm: 是否备份锁定
        :type worm: bool
        :param policy_enable: 策略是否启用
        :type policy_enable: bool
        """
        
        

        self._vault_id = None
        self._policy_id = None
        self._encrypted = None
        self._worm = None
        self._policy_enable = None
        self.discriminator = None

        self.vault_id = vault_id
        self.policy_id = policy_id
        if encrypted is not None:
            self.encrypted = encrypted
        if worm is not None:
            self.worm = worm
        self.policy_enable = policy_enable

    @property
    def vault_id(self):
        r"""Gets the vault_id of this ConfigureVaultItem.

        CBR存储库ID

        :return: The vault_id of this ConfigureVaultItem.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this ConfigureVaultItem.

        CBR存储库ID

        :param vault_id: The vault_id of this ConfigureVaultItem.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ConfigureVaultItem.

        策略ID

        :return: The policy_id of this ConfigureVaultItem.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ConfigureVaultItem.

        策略ID

        :param policy_id: The policy_id of this ConfigureVaultItem.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def encrypted(self):
        r"""Gets the encrypted of this ConfigureVaultItem.

        是否加密

        :return: The encrypted of this ConfigureVaultItem.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        r"""Sets the encrypted of this ConfigureVaultItem.

        是否加密

        :param encrypted: The encrypted of this ConfigureVaultItem.
        :type encrypted: bool
        """
        self._encrypted = encrypted

    @property
    def worm(self):
        r"""Gets the worm of this ConfigureVaultItem.

        是否备份锁定

        :return: The worm of this ConfigureVaultItem.
        :rtype: bool
        """
        return self._worm

    @worm.setter
    def worm(self, worm):
        r"""Sets the worm of this ConfigureVaultItem.

        是否备份锁定

        :param worm: The worm of this ConfigureVaultItem.
        :type worm: bool
        """
        self._worm = worm

    @property
    def policy_enable(self):
        r"""Gets the policy_enable of this ConfigureVaultItem.

        策略是否启用

        :return: The policy_enable of this ConfigureVaultItem.
        :rtype: bool
        """
        return self._policy_enable

    @policy_enable.setter
    def policy_enable(self, policy_enable):
        r"""Sets the policy_enable of this ConfigureVaultItem.

        策略是否启用

        :param policy_enable: The policy_enable of this ConfigureVaultItem.
        :type policy_enable: bool
        """
        self._policy_enable = policy_enable

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
        if not isinstance(other, ConfigureVaultItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
