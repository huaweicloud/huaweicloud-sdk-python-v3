# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateBackupPolicyRequestBody:

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
        'backup_policy': 'MysqlBackupPolicyInfo'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'backup_policy': 'backup_policy'
    }

    def __init__(self, instance_ids=None, backup_policy=None):
        r"""BatchUpdateBackupPolicyRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: **参数解释**：  需要设置备份策略的实例ID列表。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  列表数量小于等于50。
        :type instance_ids: list[str]
        :param backup_policy: 
        :type backup_policy: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupPolicyInfo`
        """
        
        

        self._instance_ids = None
        self._backup_policy = None
        self.discriminator = None

        self.instance_ids = instance_ids
        self.backup_policy = backup_policy

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this BatchUpdateBackupPolicyRequestBody.

        **参数解释**：  需要设置备份策略的实例ID列表。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  列表数量小于等于50。

        :return: The instance_ids of this BatchUpdateBackupPolicyRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this BatchUpdateBackupPolicyRequestBody.

        **参数解释**：  需要设置备份策略的实例ID列表。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  列表数量小于等于50。

        :param instance_ids: The instance_ids of this BatchUpdateBackupPolicyRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def backup_policy(self):
        r"""Gets the backup_policy of this BatchUpdateBackupPolicyRequestBody.

        :return: The backup_policy of this BatchUpdateBackupPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupPolicyInfo`
        """
        return self._backup_policy

    @backup_policy.setter
    def backup_policy(self, backup_policy):
        r"""Sets the backup_policy of this BatchUpdateBackupPolicyRequestBody.

        :param backup_policy: The backup_policy of this BatchUpdateBackupPolicyRequestBody.
        :type backup_policy: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupPolicyInfo`
        """
        self._backup_policy = backup_policy

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
        if not isinstance(other, BatchUpdateBackupPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
