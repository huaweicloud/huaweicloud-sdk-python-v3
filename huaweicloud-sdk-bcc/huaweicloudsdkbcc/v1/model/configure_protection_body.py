# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigureProtectionBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'protect_engine': 'str',
        'local_vaults': 'list[ConfigureVaultItem]',
        'remote_vaults': 'list[ConfigureVaultItem]',
        'db_backup_policy': 'DbBackupPolicyBody',
        'db_offsite_backup_policy': 'DbOffsiteBackupPolicyBody'
    }

    attribute_map = {
        'ids': 'ids',
        'protect_engine': 'protect_engine',
        'local_vaults': 'local_vaults',
        'remote_vaults': 'remote_vaults',
        'db_backup_policy': 'db_backup_policy',
        'db_offsite_backup_policy': 'db_offsite_backup_policy'
    }

    def __init__(self, ids=None, protect_engine=None, local_vaults=None, remote_vaults=None, db_backup_policy=None, db_offsite_backup_policy=None):
        r"""ConfigureProtectionBody

        The model defined in huaweicloud sdk

        :param ids: 资源ID列表
        :type ids: list[str]
        :param protect_engine: 资源保护采用的方式。分为云备份cbr和数据库db
        :type protect_engine: str
        :param local_vaults: 
        :type local_vaults: list[:class:`huaweicloudsdkbcc.v1.ConfigureVaultItem`]
        :param remote_vaults: 
        :type remote_vaults: list[:class:`huaweicloudsdkbcc.v1.ConfigureVaultItem`]
        :param db_backup_policy: 
        :type db_backup_policy: :class:`huaweicloudsdkbcc.v1.DbBackupPolicyBody`
        :param db_offsite_backup_policy: 
        :type db_offsite_backup_policy: :class:`huaweicloudsdkbcc.v1.DbOffsiteBackupPolicyBody`
        """
        
        

        self._ids = None
        self._protect_engine = None
        self._local_vaults = None
        self._remote_vaults = None
        self._db_backup_policy = None
        self._db_offsite_backup_policy = None
        self.discriminator = None

        self.ids = ids
        self.protect_engine = protect_engine
        if local_vaults is not None:
            self.local_vaults = local_vaults
        if remote_vaults is not None:
            self.remote_vaults = remote_vaults
        if db_backup_policy is not None:
            self.db_backup_policy = db_backup_policy
        if db_offsite_backup_policy is not None:
            self.db_offsite_backup_policy = db_offsite_backup_policy

    @property
    def ids(self):
        r"""Gets the ids of this ConfigureProtectionBody.

        资源ID列表

        :return: The ids of this ConfigureProtectionBody.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this ConfigureProtectionBody.

        资源ID列表

        :param ids: The ids of this ConfigureProtectionBody.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def protect_engine(self):
        r"""Gets the protect_engine of this ConfigureProtectionBody.

        资源保护采用的方式。分为云备份cbr和数据库db

        :return: The protect_engine of this ConfigureProtectionBody.
        :rtype: str
        """
        return self._protect_engine

    @protect_engine.setter
    def protect_engine(self, protect_engine):
        r"""Sets the protect_engine of this ConfigureProtectionBody.

        资源保护采用的方式。分为云备份cbr和数据库db

        :param protect_engine: The protect_engine of this ConfigureProtectionBody.
        :type protect_engine: str
        """
        self._protect_engine = protect_engine

    @property
    def local_vaults(self):
        r"""Gets the local_vaults of this ConfigureProtectionBody.

        :return: The local_vaults of this ConfigureProtectionBody.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.ConfigureVaultItem`]
        """
        return self._local_vaults

    @local_vaults.setter
    def local_vaults(self, local_vaults):
        r"""Sets the local_vaults of this ConfigureProtectionBody.

        :param local_vaults: The local_vaults of this ConfigureProtectionBody.
        :type local_vaults: list[:class:`huaweicloudsdkbcc.v1.ConfigureVaultItem`]
        """
        self._local_vaults = local_vaults

    @property
    def remote_vaults(self):
        r"""Gets the remote_vaults of this ConfigureProtectionBody.

        :return: The remote_vaults of this ConfigureProtectionBody.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.ConfigureVaultItem`]
        """
        return self._remote_vaults

    @remote_vaults.setter
    def remote_vaults(self, remote_vaults):
        r"""Sets the remote_vaults of this ConfigureProtectionBody.

        :param remote_vaults: The remote_vaults of this ConfigureProtectionBody.
        :type remote_vaults: list[:class:`huaweicloudsdkbcc.v1.ConfigureVaultItem`]
        """
        self._remote_vaults = remote_vaults

    @property
    def db_backup_policy(self):
        r"""Gets the db_backup_policy of this ConfigureProtectionBody.

        :return: The db_backup_policy of this ConfigureProtectionBody.
        :rtype: :class:`huaweicloudsdkbcc.v1.DbBackupPolicyBody`
        """
        return self._db_backup_policy

    @db_backup_policy.setter
    def db_backup_policy(self, db_backup_policy):
        r"""Sets the db_backup_policy of this ConfigureProtectionBody.

        :param db_backup_policy: The db_backup_policy of this ConfigureProtectionBody.
        :type db_backup_policy: :class:`huaweicloudsdkbcc.v1.DbBackupPolicyBody`
        """
        self._db_backup_policy = db_backup_policy

    @property
    def db_offsite_backup_policy(self):
        r"""Gets the db_offsite_backup_policy of this ConfigureProtectionBody.

        :return: The db_offsite_backup_policy of this ConfigureProtectionBody.
        :rtype: :class:`huaweicloudsdkbcc.v1.DbOffsiteBackupPolicyBody`
        """
        return self._db_offsite_backup_policy

    @db_offsite_backup_policy.setter
    def db_offsite_backup_policy(self, db_offsite_backup_policy):
        r"""Sets the db_offsite_backup_policy of this ConfigureProtectionBody.

        :param db_offsite_backup_policy: The db_offsite_backup_policy of this ConfigureProtectionBody.
        :type db_offsite_backup_policy: :class:`huaweicloudsdkbcc.v1.DbOffsiteBackupPolicyBody`
        """
        self._db_offsite_backup_policy = db_offsite_backup_policy

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
        if not isinstance(other, ConfigureProtectionBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
