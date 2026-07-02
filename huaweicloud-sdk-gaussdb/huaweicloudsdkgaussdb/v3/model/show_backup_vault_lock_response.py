# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupVaultLockResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_vaultlock_info': 'BackupVaultLockInfo'
    }

    attribute_map = {
        'backup_vaultlock_info': 'backup_vaultlock_info'
    }

    def __init__(self, backup_vaultlock_info=None):
        r"""ShowBackupVaultLockResponse

        The model defined in huaweicloud sdk

        :param backup_vaultlock_info: 
        :type backup_vaultlock_info: :class:`huaweicloudsdkgaussdb.v3.BackupVaultLockInfo`
        """
        
        super().__init__()

        self._backup_vaultlock_info = None
        self.discriminator = None

        if backup_vaultlock_info is not None:
            self.backup_vaultlock_info = backup_vaultlock_info

    @property
    def backup_vaultlock_info(self):
        r"""Gets the backup_vaultlock_info of this ShowBackupVaultLockResponse.

        :return: The backup_vaultlock_info of this ShowBackupVaultLockResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.BackupVaultLockInfo`
        """
        return self._backup_vaultlock_info

    @backup_vaultlock_info.setter
    def backup_vaultlock_info(self, backup_vaultlock_info):
        r"""Sets the backup_vaultlock_info of this ShowBackupVaultLockResponse.

        :param backup_vaultlock_info: The backup_vaultlock_info of this ShowBackupVaultLockResponse.
        :type backup_vaultlock_info: :class:`huaweicloudsdkgaussdb.v3.BackupVaultLockInfo`
        """
        self._backup_vaultlock_info = backup_vaultlock_info

    def to_dict(self):
        import warnings
        warnings.warn("ShowBackupVaultLockResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowBackupVaultLockResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
