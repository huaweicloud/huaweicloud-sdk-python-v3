# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostVaultInfoVaults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vault_name': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'vault_name': 'vault_name',
        'vault_id': 'vault_id'
    }

    def __init__(self, vault_name=None, vault_id=None):
        r"""HostVaultInfoVaults

        The model defined in huaweicloud sdk

        :param vault_name: **参数解释**: 存储库名称 **取值范围**: 字符长度1-128位 
        :type vault_name: str
        :param vault_id: **参数解释**: 存储库id **取值范围**: 字符长度1-128位 
        :type vault_id: str
        """
        
        

        self._vault_name = None
        self._vault_id = None
        self.discriminator = None

        if vault_name is not None:
            self.vault_name = vault_name
        if vault_id is not None:
            self.vault_id = vault_id

    @property
    def vault_name(self):
        r"""Gets the vault_name of this HostVaultInfoVaults.

        **参数解释**: 存储库名称 **取值范围**: 字符长度1-128位 

        :return: The vault_name of this HostVaultInfoVaults.
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        r"""Sets the vault_name of this HostVaultInfoVaults.

        **参数解释**: 存储库名称 **取值范围**: 字符长度1-128位 

        :param vault_name: The vault_name of this HostVaultInfoVaults.
        :type vault_name: str
        """
        self._vault_name = vault_name

    @property
    def vault_id(self):
        r"""Gets the vault_id of this HostVaultInfoVaults.

        **参数解释**: 存储库id **取值范围**: 字符长度1-128位 

        :return: The vault_id of this HostVaultInfoVaults.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this HostVaultInfoVaults.

        **参数解释**: 存储库id **取值范围**: 字符长度1-128位 

        :param vault_id: The vault_id of this HostVaultInfoVaults.
        :type vault_id: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, HostVaultInfoVaults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
