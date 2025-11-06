# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbPolicyDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_policy': 'DbPolicyDetailBackupPolicy',
        'offsite_backup_policy': 'list[DbPolicyDetailOffsiteBackupPolicy]'
    }

    attribute_map = {
        'backup_policy': 'backup_policy',
        'offsite_backup_policy': 'offsite_backup_policy'
    }

    def __init__(self, backup_policy=None, offsite_backup_policy=None):
        r"""DbPolicyDetail

        The model defined in huaweicloud sdk

        :param backup_policy: 
        :type backup_policy: :class:`huaweicloudsdkbcc.v1.DbPolicyDetailBackupPolicy`
        :param offsite_backup_policy: 数据库复制策略
        :type offsite_backup_policy: list[:class:`huaweicloudsdkbcc.v1.DbPolicyDetailOffsiteBackupPolicy`]
        """
        
        

        self._backup_policy = None
        self._offsite_backup_policy = None
        self.discriminator = None

        if backup_policy is not None:
            self.backup_policy = backup_policy
        if offsite_backup_policy is not None:
            self.offsite_backup_policy = offsite_backup_policy

    @property
    def backup_policy(self):
        r"""Gets the backup_policy of this DbPolicyDetail.

        :return: The backup_policy of this DbPolicyDetail.
        :rtype: :class:`huaweicloudsdkbcc.v1.DbPolicyDetailBackupPolicy`
        """
        return self._backup_policy

    @backup_policy.setter
    def backup_policy(self, backup_policy):
        r"""Sets the backup_policy of this DbPolicyDetail.

        :param backup_policy: The backup_policy of this DbPolicyDetail.
        :type backup_policy: :class:`huaweicloudsdkbcc.v1.DbPolicyDetailBackupPolicy`
        """
        self._backup_policy = backup_policy

    @property
    def offsite_backup_policy(self):
        r"""Gets the offsite_backup_policy of this DbPolicyDetail.

        数据库复制策略

        :return: The offsite_backup_policy of this DbPolicyDetail.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.DbPolicyDetailOffsiteBackupPolicy`]
        """
        return self._offsite_backup_policy

    @offsite_backup_policy.setter
    def offsite_backup_policy(self, offsite_backup_policy):
        r"""Sets the offsite_backup_policy of this DbPolicyDetail.

        数据库复制策略

        :param offsite_backup_policy: The offsite_backup_policy of this DbPolicyDetail.
        :type offsite_backup_policy: list[:class:`huaweicloudsdkbcc.v1.DbPolicyDetailOffsiteBackupPolicy`]
        """
        self._offsite_backup_policy = offsite_backup_policy

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
        if not isinstance(other, DbPolicyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
