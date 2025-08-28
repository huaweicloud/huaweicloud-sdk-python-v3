# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostVaultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'asset_value': 'str',
        'default_backup_name_suffix': 'str',
        'default_vault': 'HostVaultInfoDefaultVault',
        'vaults': 'list[HostVaultInfoVaults]'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'asset_value': 'asset_value',
        'default_backup_name_suffix': 'default_backup_name_suffix',
        'default_vault': 'default_vault',
        'vaults': 'vaults'
    }

    def __init__(self, host_id=None, host_name=None, public_ip=None, private_ip=None, asset_value=None, default_backup_name_suffix=None, default_vault=None, vaults=None):
        r"""HostVaultInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 主机id **取值范围**: 字符长度1-128位 
        :type host_id: str
        :param host_name: **参数解释**: 主机名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param public_ip: **参数解释**: 主机公网ip **取值范围**: 字符长度1-128位 
        :type public_ip: str
        :param private_ip: **参数解释**: 主机私网ip **取值范围**: 字符长度1-128位 
        :type private_ip: str
        :param asset_value: **参数解释**: 主机的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 
        :type asset_value: str
        :param default_backup_name_suffix: **参数解释**: 默认备份名称的后缀 **取值范围**: 字符长度0-32位 
        :type default_backup_name_suffix: str
        :param default_vault: 
        :type default_vault: :class:`huaweicloudsdkhss.v5.HostVaultInfoDefaultVault`
        :param vaults: **参数解释**: 主机的存储库列表 **取值范围**: 不涉及 
        :type vaults: list[:class:`huaweicloudsdkhss.v5.HostVaultInfoVaults`]
        """
        
        

        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._asset_value = None
        self._default_backup_name_suffix = None
        self._default_vault = None
        self._vaults = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if asset_value is not None:
            self.asset_value = asset_value
        if default_backup_name_suffix is not None:
            self.default_backup_name_suffix = default_backup_name_suffix
        if default_vault is not None:
            self.default_vault = default_vault
        if vaults is not None:
            self.vaults = vaults

    @property
    def host_id(self):
        r"""Gets the host_id of this HostVaultInfo.

        **参数解释**: 主机id **取值范围**: 字符长度1-128位 

        :return: The host_id of this HostVaultInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this HostVaultInfo.

        **参数解释**: 主机id **取值范围**: 字符长度1-128位 

        :param host_id: The host_id of this HostVaultInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this HostVaultInfo.

        **参数解释**: 主机名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this HostVaultInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this HostVaultInfo.

        **参数解释**: 主机名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this HostVaultInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this HostVaultInfo.

        **参数解释**: 主机公网ip **取值范围**: 字符长度1-128位 

        :return: The public_ip of this HostVaultInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this HostVaultInfo.

        **参数解释**: 主机公网ip **取值范围**: 字符长度1-128位 

        :param public_ip: The public_ip of this HostVaultInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this HostVaultInfo.

        **参数解释**: 主机私网ip **取值范围**: 字符长度1-128位 

        :return: The private_ip of this HostVaultInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this HostVaultInfo.

        **参数解释**: 主机私网ip **取值范围**: 字符长度1-128位 

        :param private_ip: The private_ip of this HostVaultInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def asset_value(self):
        r"""Gets the asset_value of this HostVaultInfo.

        **参数解释**: 主机的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 

        :return: The asset_value of this HostVaultInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this HostVaultInfo.

        **参数解释**: 主机的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 

        :param asset_value: The asset_value of this HostVaultInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def default_backup_name_suffix(self):
        r"""Gets the default_backup_name_suffix of this HostVaultInfo.

        **参数解释**: 默认备份名称的后缀 **取值范围**: 字符长度0-32位 

        :return: The default_backup_name_suffix of this HostVaultInfo.
        :rtype: str
        """
        return self._default_backup_name_suffix

    @default_backup_name_suffix.setter
    def default_backup_name_suffix(self, default_backup_name_suffix):
        r"""Sets the default_backup_name_suffix of this HostVaultInfo.

        **参数解释**: 默认备份名称的后缀 **取值范围**: 字符长度0-32位 

        :param default_backup_name_suffix: The default_backup_name_suffix of this HostVaultInfo.
        :type default_backup_name_suffix: str
        """
        self._default_backup_name_suffix = default_backup_name_suffix

    @property
    def default_vault(self):
        r"""Gets the default_vault of this HostVaultInfo.

        :return: The default_vault of this HostVaultInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.HostVaultInfoDefaultVault`
        """
        return self._default_vault

    @default_vault.setter
    def default_vault(self, default_vault):
        r"""Sets the default_vault of this HostVaultInfo.

        :param default_vault: The default_vault of this HostVaultInfo.
        :type default_vault: :class:`huaweicloudsdkhss.v5.HostVaultInfoDefaultVault`
        """
        self._default_vault = default_vault

    @property
    def vaults(self):
        r"""Gets the vaults of this HostVaultInfo.

        **参数解释**: 主机的存储库列表 **取值范围**: 不涉及 

        :return: The vaults of this HostVaultInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostVaultInfoVaults`]
        """
        return self._vaults

    @vaults.setter
    def vaults(self, vaults):
        r"""Sets the vaults of this HostVaultInfo.

        **参数解释**: 主机的存储库列表 **取值范围**: 不涉及 

        :param vaults: The vaults of this HostVaultInfo.
        :type vaults: list[:class:`huaweicloudsdkhss.v5.HostVaultInfoVaults`]
        """
        self._vaults = vaults

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
        if not isinstance(other, HostVaultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
