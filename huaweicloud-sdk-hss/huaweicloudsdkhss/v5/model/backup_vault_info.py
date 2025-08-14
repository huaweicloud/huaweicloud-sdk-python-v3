# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupVaultInfo:

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
        'vault_name': 'str',
        'vault_size': 'int',
        'vault_used': 'int',
        'vault_allocated': 'int',
        'vault_charging_mode': 'str',
        'vault_status': 'str',
        'backup_policy_id': 'str',
        'backup_policy_name': 'str',
        'backup_policy_enabled': 'bool',
        'resources_num': 'int'
    }

    attribute_map = {
        'vault_id': 'vault_id',
        'vault_name': 'vault_name',
        'vault_size': 'vault_size',
        'vault_used': 'vault_used',
        'vault_allocated': 'vault_allocated',
        'vault_charging_mode': 'vault_charging_mode',
        'vault_status': 'vault_status',
        'backup_policy_id': 'backup_policy_id',
        'backup_policy_name': 'backup_policy_name',
        'backup_policy_enabled': 'backup_policy_enabled',
        'resources_num': 'resources_num'
    }

    def __init__(self, vault_id=None, vault_name=None, vault_size=None, vault_used=None, vault_allocated=None, vault_charging_mode=None, vault_status=None, backup_policy_id=None, backup_policy_name=None, backup_policy_enabled=None, resources_num=None):
        r"""BackupVaultInfo

        The model defined in huaweicloud sdk

        :param vault_id: 存储库ID
        :type vault_id: str
        :param vault_name: 存储库名称
        :type vault_name: str
        :param vault_size: 存储库总容量，单位GB
        :type vault_size: int
        :param vault_used: 已使用容量，单位MB，指的是已有备份占用的容量，例如绑定了1台主机，已经有两个备份数，两个备份60G，则已使用容量为60G。
        :type vault_used: int
        :param vault_allocated: 已分配容量，单位GB，指绑定的服务器大小，例如绑定了1台主机，主机大小40G，则已分配容量为40G。
        :type vault_allocated: int
        :param vault_charging_mode: 存储库创建模式：   - 按需：post_paid   - 包周期：pre_paid
        :type vault_charging_mode: str
        :param vault_status: 存储库状态。   - available：可用。   - lock：被锁定。   - frozen：冻结。   - deleting：删除中。   - error：错误。
        :type vault_status: str
        :param backup_policy_id: 备份策略ID，若为空，则为未绑定状态，若不为空，通过backup_policy_enabled字段判断策略是否启用
        :type backup_policy_id: str
        :param backup_policy_name: 备份策略名称
        :type backup_policy_name: str
        :param backup_policy_enabled: 备份策略是否启用
        :type backup_policy_enabled: bool
        :param resources_num: 已绑定服务器（个）
        :type resources_num: int
        """
        
        

        self._vault_id = None
        self._vault_name = None
        self._vault_size = None
        self._vault_used = None
        self._vault_allocated = None
        self._vault_charging_mode = None
        self._vault_status = None
        self._backup_policy_id = None
        self._backup_policy_name = None
        self._backup_policy_enabled = None
        self._resources_num = None
        self.discriminator = None

        if vault_id is not None:
            self.vault_id = vault_id
        if vault_name is not None:
            self.vault_name = vault_name
        if vault_size is not None:
            self.vault_size = vault_size
        if vault_used is not None:
            self.vault_used = vault_used
        if vault_allocated is not None:
            self.vault_allocated = vault_allocated
        if vault_charging_mode is not None:
            self.vault_charging_mode = vault_charging_mode
        if vault_status is not None:
            self.vault_status = vault_status
        if backup_policy_id is not None:
            self.backup_policy_id = backup_policy_id
        if backup_policy_name is not None:
            self.backup_policy_name = backup_policy_name
        if backup_policy_enabled is not None:
            self.backup_policy_enabled = backup_policy_enabled
        if resources_num is not None:
            self.resources_num = resources_num

    @property
    def vault_id(self):
        r"""Gets the vault_id of this BackupVaultInfo.

        存储库ID

        :return: The vault_id of this BackupVaultInfo.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this BackupVaultInfo.

        存储库ID

        :param vault_id: The vault_id of this BackupVaultInfo.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def vault_name(self):
        r"""Gets the vault_name of this BackupVaultInfo.

        存储库名称

        :return: The vault_name of this BackupVaultInfo.
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        r"""Sets the vault_name of this BackupVaultInfo.

        存储库名称

        :param vault_name: The vault_name of this BackupVaultInfo.
        :type vault_name: str
        """
        self._vault_name = vault_name

    @property
    def vault_size(self):
        r"""Gets the vault_size of this BackupVaultInfo.

        存储库总容量，单位GB

        :return: The vault_size of this BackupVaultInfo.
        :rtype: int
        """
        return self._vault_size

    @vault_size.setter
    def vault_size(self, vault_size):
        r"""Sets the vault_size of this BackupVaultInfo.

        存储库总容量，单位GB

        :param vault_size: The vault_size of this BackupVaultInfo.
        :type vault_size: int
        """
        self._vault_size = vault_size

    @property
    def vault_used(self):
        r"""Gets the vault_used of this BackupVaultInfo.

        已使用容量，单位MB，指的是已有备份占用的容量，例如绑定了1台主机，已经有两个备份数，两个备份60G，则已使用容量为60G。

        :return: The vault_used of this BackupVaultInfo.
        :rtype: int
        """
        return self._vault_used

    @vault_used.setter
    def vault_used(self, vault_used):
        r"""Sets the vault_used of this BackupVaultInfo.

        已使用容量，单位MB，指的是已有备份占用的容量，例如绑定了1台主机，已经有两个备份数，两个备份60G，则已使用容量为60G。

        :param vault_used: The vault_used of this BackupVaultInfo.
        :type vault_used: int
        """
        self._vault_used = vault_used

    @property
    def vault_allocated(self):
        r"""Gets the vault_allocated of this BackupVaultInfo.

        已分配容量，单位GB，指绑定的服务器大小，例如绑定了1台主机，主机大小40G，则已分配容量为40G。

        :return: The vault_allocated of this BackupVaultInfo.
        :rtype: int
        """
        return self._vault_allocated

    @vault_allocated.setter
    def vault_allocated(self, vault_allocated):
        r"""Sets the vault_allocated of this BackupVaultInfo.

        已分配容量，单位GB，指绑定的服务器大小，例如绑定了1台主机，主机大小40G，则已分配容量为40G。

        :param vault_allocated: The vault_allocated of this BackupVaultInfo.
        :type vault_allocated: int
        """
        self._vault_allocated = vault_allocated

    @property
    def vault_charging_mode(self):
        r"""Gets the vault_charging_mode of this BackupVaultInfo.

        存储库创建模式：   - 按需：post_paid   - 包周期：pre_paid

        :return: The vault_charging_mode of this BackupVaultInfo.
        :rtype: str
        """
        return self._vault_charging_mode

    @vault_charging_mode.setter
    def vault_charging_mode(self, vault_charging_mode):
        r"""Sets the vault_charging_mode of this BackupVaultInfo.

        存储库创建模式：   - 按需：post_paid   - 包周期：pre_paid

        :param vault_charging_mode: The vault_charging_mode of this BackupVaultInfo.
        :type vault_charging_mode: str
        """
        self._vault_charging_mode = vault_charging_mode

    @property
    def vault_status(self):
        r"""Gets the vault_status of this BackupVaultInfo.

        存储库状态。   - available：可用。   - lock：被锁定。   - frozen：冻结。   - deleting：删除中。   - error：错误。

        :return: The vault_status of this BackupVaultInfo.
        :rtype: str
        """
        return self._vault_status

    @vault_status.setter
    def vault_status(self, vault_status):
        r"""Sets the vault_status of this BackupVaultInfo.

        存储库状态。   - available：可用。   - lock：被锁定。   - frozen：冻结。   - deleting：删除中。   - error：错误。

        :param vault_status: The vault_status of this BackupVaultInfo.
        :type vault_status: str
        """
        self._vault_status = vault_status

    @property
    def backup_policy_id(self):
        r"""Gets the backup_policy_id of this BackupVaultInfo.

        备份策略ID，若为空，则为未绑定状态，若不为空，通过backup_policy_enabled字段判断策略是否启用

        :return: The backup_policy_id of this BackupVaultInfo.
        :rtype: str
        """
        return self._backup_policy_id

    @backup_policy_id.setter
    def backup_policy_id(self, backup_policy_id):
        r"""Sets the backup_policy_id of this BackupVaultInfo.

        备份策略ID，若为空，则为未绑定状态，若不为空，通过backup_policy_enabled字段判断策略是否启用

        :param backup_policy_id: The backup_policy_id of this BackupVaultInfo.
        :type backup_policy_id: str
        """
        self._backup_policy_id = backup_policy_id

    @property
    def backup_policy_name(self):
        r"""Gets the backup_policy_name of this BackupVaultInfo.

        备份策略名称

        :return: The backup_policy_name of this BackupVaultInfo.
        :rtype: str
        """
        return self._backup_policy_name

    @backup_policy_name.setter
    def backup_policy_name(self, backup_policy_name):
        r"""Sets the backup_policy_name of this BackupVaultInfo.

        备份策略名称

        :param backup_policy_name: The backup_policy_name of this BackupVaultInfo.
        :type backup_policy_name: str
        """
        self._backup_policy_name = backup_policy_name

    @property
    def backup_policy_enabled(self):
        r"""Gets the backup_policy_enabled of this BackupVaultInfo.

        备份策略是否启用

        :return: The backup_policy_enabled of this BackupVaultInfo.
        :rtype: bool
        """
        return self._backup_policy_enabled

    @backup_policy_enabled.setter
    def backup_policy_enabled(self, backup_policy_enabled):
        r"""Sets the backup_policy_enabled of this BackupVaultInfo.

        备份策略是否启用

        :param backup_policy_enabled: The backup_policy_enabled of this BackupVaultInfo.
        :type backup_policy_enabled: bool
        """
        self._backup_policy_enabled = backup_policy_enabled

    @property
    def resources_num(self):
        r"""Gets the resources_num of this BackupVaultInfo.

        已绑定服务器（个）

        :return: The resources_num of this BackupVaultInfo.
        :rtype: int
        """
        return self._resources_num

    @resources_num.setter
    def resources_num(self, resources_num):
        r"""Sets the resources_num of this BackupVaultInfo.

        已绑定服务器（个）

        :param resources_num: The resources_num of this BackupVaultInfo.
        :type resources_num: int
        """
        self._resources_num = resources_num

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
        if not isinstance(other, BackupVaultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
