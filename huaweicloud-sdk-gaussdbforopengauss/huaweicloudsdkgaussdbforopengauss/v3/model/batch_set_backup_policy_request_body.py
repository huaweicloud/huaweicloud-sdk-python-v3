# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetBackupPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'backup_policy': 'BackupPolicyInfo'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'backup_policy': 'backup_policy'
    }

    def __init__(self, instance_ids=None, backup_policy=None):
        r"""BatchSetBackupPolicyRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: **参数解释**: 实例ID列表。 **约束限制**: 列表中的实例ID需严格匹配UUID规则，只能由英文字母、数字组成，且长度为36个字符。
        :type instance_ids: list[str]
        :param backup_policy: 
        :type backup_policy: :class:`huaweicloudsdkgaussdbforopengauss.v3.BackupPolicyInfo`
        """
        
        

        self._instance_ids = None
        self._backup_policy = None
        self.discriminator = None

        self.instance_ids = instance_ids
        self.backup_policy = backup_policy

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this BatchSetBackupPolicyRequestBody.

        **参数解释**: 实例ID列表。 **约束限制**: 列表中的实例ID需严格匹配UUID规则，只能由英文字母、数字组成，且长度为36个字符。

        :return: The instance_ids of this BatchSetBackupPolicyRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this BatchSetBackupPolicyRequestBody.

        **参数解释**: 实例ID列表。 **约束限制**: 列表中的实例ID需严格匹配UUID规则，只能由英文字母、数字组成，且长度为36个字符。

        :param instance_ids: The instance_ids of this BatchSetBackupPolicyRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def backup_policy(self):
        r"""Gets the backup_policy of this BatchSetBackupPolicyRequestBody.

        :return: The backup_policy of this BatchSetBackupPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.BackupPolicyInfo`
        """
        return self._backup_policy

    @backup_policy.setter
    def backup_policy(self, backup_policy):
        r"""Sets the backup_policy of this BatchSetBackupPolicyRequestBody.

        :param backup_policy: The backup_policy of this BatchSetBackupPolicyRequestBody.
        :type backup_policy: :class:`huaweicloudsdkgaussdbforopengauss.v3.BackupPolicyInfo`
        """
        self._backup_policy = backup_policy

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
        if not isinstance(other, BatchSetBackupPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
