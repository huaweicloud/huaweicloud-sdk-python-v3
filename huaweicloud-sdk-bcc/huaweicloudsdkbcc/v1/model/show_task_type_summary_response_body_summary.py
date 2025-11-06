# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskTypeSummaryResponseBodySummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_task_count': 'int',
        'backup_task_count': 'int',
        'replication_task_count': 'int',
        'restore_task_count': 'int',
        'delete_task_count': 'int',
        'vault_delete_task_count': 'int',
        'remove_resource_task_count': 'int'
    }

    attribute_map = {
        'total_task_count': 'total_task_count',
        'backup_task_count': 'backup_task_count',
        'replication_task_count': 'replication_task_count',
        'restore_task_count': 'restore_task_count',
        'delete_task_count': 'delete_task_count',
        'vault_delete_task_count': 'vault_delete_task_count',
        'remove_resource_task_count': 'remove_resource_task_count'
    }

    def __init__(self, total_task_count=None, backup_task_count=None, replication_task_count=None, restore_task_count=None, delete_task_count=None, vault_delete_task_count=None, remove_resource_task_count=None):
        r"""ShowTaskTypeSummaryResponseBodySummary

        The model defined in huaweicloud sdk

        :param total_task_count: 总任务数据
        :type total_task_count: int
        :param backup_task_count: 备份任务总数
        :type backup_task_count: int
        :param replication_task_count: 复制任务总数
        :type replication_task_count: int
        :param restore_task_count: 恢复任务总数
        :type restore_task_count: int
        :param delete_task_count: 删除备份任务总数
        :type delete_task_count: int
        :param vault_delete_task_count: 删除存储库任务总数
        :type vault_delete_task_count: int
        :param remove_resource_task_count: 移除存储库资源总数
        :type remove_resource_task_count: int
        """
        
        

        self._total_task_count = None
        self._backup_task_count = None
        self._replication_task_count = None
        self._restore_task_count = None
        self._delete_task_count = None
        self._vault_delete_task_count = None
        self._remove_resource_task_count = None
        self.discriminator = None

        self.total_task_count = total_task_count
        self.backup_task_count = backup_task_count
        self.replication_task_count = replication_task_count
        self.restore_task_count = restore_task_count
        self.delete_task_count = delete_task_count
        self.vault_delete_task_count = vault_delete_task_count
        self.remove_resource_task_count = remove_resource_task_count

    @property
    def total_task_count(self):
        r"""Gets the total_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        总任务数据

        :return: The total_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :rtype: int
        """
        return self._total_task_count

    @total_task_count.setter
    def total_task_count(self, total_task_count):
        r"""Sets the total_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        总任务数据

        :param total_task_count: The total_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :type total_task_count: int
        """
        self._total_task_count = total_task_count

    @property
    def backup_task_count(self):
        r"""Gets the backup_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        备份任务总数

        :return: The backup_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :rtype: int
        """
        return self._backup_task_count

    @backup_task_count.setter
    def backup_task_count(self, backup_task_count):
        r"""Sets the backup_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        备份任务总数

        :param backup_task_count: The backup_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :type backup_task_count: int
        """
        self._backup_task_count = backup_task_count

    @property
    def replication_task_count(self):
        r"""Gets the replication_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        复制任务总数

        :return: The replication_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :rtype: int
        """
        return self._replication_task_count

    @replication_task_count.setter
    def replication_task_count(self, replication_task_count):
        r"""Sets the replication_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        复制任务总数

        :param replication_task_count: The replication_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :type replication_task_count: int
        """
        self._replication_task_count = replication_task_count

    @property
    def restore_task_count(self):
        r"""Gets the restore_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        恢复任务总数

        :return: The restore_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :rtype: int
        """
        return self._restore_task_count

    @restore_task_count.setter
    def restore_task_count(self, restore_task_count):
        r"""Sets the restore_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        恢复任务总数

        :param restore_task_count: The restore_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :type restore_task_count: int
        """
        self._restore_task_count = restore_task_count

    @property
    def delete_task_count(self):
        r"""Gets the delete_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        删除备份任务总数

        :return: The delete_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :rtype: int
        """
        return self._delete_task_count

    @delete_task_count.setter
    def delete_task_count(self, delete_task_count):
        r"""Sets the delete_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        删除备份任务总数

        :param delete_task_count: The delete_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :type delete_task_count: int
        """
        self._delete_task_count = delete_task_count

    @property
    def vault_delete_task_count(self):
        r"""Gets the vault_delete_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        删除存储库任务总数

        :return: The vault_delete_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :rtype: int
        """
        return self._vault_delete_task_count

    @vault_delete_task_count.setter
    def vault_delete_task_count(self, vault_delete_task_count):
        r"""Sets the vault_delete_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        删除存储库任务总数

        :param vault_delete_task_count: The vault_delete_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :type vault_delete_task_count: int
        """
        self._vault_delete_task_count = vault_delete_task_count

    @property
    def remove_resource_task_count(self):
        r"""Gets the remove_resource_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        移除存储库资源总数

        :return: The remove_resource_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :rtype: int
        """
        return self._remove_resource_task_count

    @remove_resource_task_count.setter
    def remove_resource_task_count(self, remove_resource_task_count):
        r"""Sets the remove_resource_task_count of this ShowTaskTypeSummaryResponseBodySummary.

        移除存储库资源总数

        :param remove_resource_task_count: The remove_resource_task_count of this ShowTaskTypeSummaryResponseBodySummary.
        :type remove_resource_task_count: int
        """
        self._remove_resource_task_count = remove_resource_task_count

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
        if not isinstance(other, ShowTaskTypeSummaryResponseBodySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
