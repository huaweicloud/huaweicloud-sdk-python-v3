# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceBackupPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_policy_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'policy': 'BackupPolicy',
        'tenant_id': 'str'
    }

    attribute_map = {
        'backup_policy_id': 'backup_policy_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'policy': 'policy',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, backup_policy_id=None, created_at=None, updated_at=None, policy=None, tenant_id=None):
        """InstanceBackupPolicy

        The model defined in huaweicloud sdk

        :param backup_policy_id: 备份策略ID
        :type backup_policy_id: str
        :param created_at: 创建时间。格式为：2022-04-11T09:45:24.790Z
        :type created_at: str
        :param updated_at: 更新时间。格式为：2022-04-12T02:22:03.269Z
        :type updated_at: str
        :param policy: 
        :type policy: :class:`huaweicloudsdkdcs.v2.BackupPolicy`
        :param tenant_id: 租户ID
        :type tenant_id: str
        """
        
        

        self._backup_policy_id = None
        self._created_at = None
        self._updated_at = None
        self._policy = None
        self._tenant_id = None
        self.discriminator = None

        if backup_policy_id is not None:
            self.backup_policy_id = backup_policy_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if policy is not None:
            self.policy = policy
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def backup_policy_id(self):
        """Gets the backup_policy_id of this InstanceBackupPolicy.

        备份策略ID

        :return: The backup_policy_id of this InstanceBackupPolicy.
        :rtype: str
        """
        return self._backup_policy_id

    @backup_policy_id.setter
    def backup_policy_id(self, backup_policy_id):
        """Sets the backup_policy_id of this InstanceBackupPolicy.

        备份策略ID

        :param backup_policy_id: The backup_policy_id of this InstanceBackupPolicy.
        :type backup_policy_id: str
        """
        self._backup_policy_id = backup_policy_id

    @property
    def created_at(self):
        """Gets the created_at of this InstanceBackupPolicy.

        创建时间。格式为：2022-04-11T09:45:24.790Z

        :return: The created_at of this InstanceBackupPolicy.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InstanceBackupPolicy.

        创建时间。格式为：2022-04-11T09:45:24.790Z

        :param created_at: The created_at of this InstanceBackupPolicy.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this InstanceBackupPolicy.

        更新时间。格式为：2022-04-12T02:22:03.269Z

        :return: The updated_at of this InstanceBackupPolicy.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InstanceBackupPolicy.

        更新时间。格式为：2022-04-12T02:22:03.269Z

        :param updated_at: The updated_at of this InstanceBackupPolicy.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def policy(self):
        """Gets the policy of this InstanceBackupPolicy.

        :return: The policy of this InstanceBackupPolicy.
        :rtype: :class:`huaweicloudsdkdcs.v2.BackupPolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this InstanceBackupPolicy.

        :param policy: The policy of this InstanceBackupPolicy.
        :type policy: :class:`huaweicloudsdkdcs.v2.BackupPolicy`
        """
        self._policy = policy

    @property
    def tenant_id(self):
        """Gets the tenant_id of this InstanceBackupPolicy.

        租户ID

        :return: The tenant_id of this InstanceBackupPolicy.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this InstanceBackupPolicy.

        租户ID

        :param tenant_id: The tenant_id of this InstanceBackupPolicy.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, InstanceBackupPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
