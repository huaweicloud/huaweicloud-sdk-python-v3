# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteGaussMySqlInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_retention_strategy': 'str'
    }

    attribute_map = {
        'backup_retention_strategy': 'backup_retention_strategy'
    }

    def __init__(self, backup_retention_strategy=None):
        r"""DeleteGaussMySqlInstanceRequestBody

        The model defined in huaweicloud sdk

        :param backup_retention_strategy: **参数解释**：  释放实例时的备份保留策略。  **约束限制**：  不涉及。  **取值范围**：  - retain_all：永久保留全部备份，包含回收站备份、自动全量备份、自动差量备份、手动备份，不包含增量备份。实例删除后，永久保留的备份会产生费用。 - retain_last：保留回收站备份和手动备份。超过回收站策略的保留天数后，系统将删除回收站备份，仅保留手动备份。手动备份会产生费用，其余保留的备份不收费。 - delete_all：删除全部备份。  **默认取值**：  retain_last。
        :type backup_retention_strategy: str
        """
        
        

        self._backup_retention_strategy = None
        self.discriminator = None

        if backup_retention_strategy is not None:
            self.backup_retention_strategy = backup_retention_strategy

    @property
    def backup_retention_strategy(self):
        r"""Gets the backup_retention_strategy of this DeleteGaussMySqlInstanceRequestBody.

        **参数解释**：  释放实例时的备份保留策略。  **约束限制**：  不涉及。  **取值范围**：  - retain_all：永久保留全部备份，包含回收站备份、自动全量备份、自动差量备份、手动备份，不包含增量备份。实例删除后，永久保留的备份会产生费用。 - retain_last：保留回收站备份和手动备份。超过回收站策略的保留天数后，系统将删除回收站备份，仅保留手动备份。手动备份会产生费用，其余保留的备份不收费。 - delete_all：删除全部备份。  **默认取值**：  retain_last。

        :return: The backup_retention_strategy of this DeleteGaussMySqlInstanceRequestBody.
        :rtype: str
        """
        return self._backup_retention_strategy

    @backup_retention_strategy.setter
    def backup_retention_strategy(self, backup_retention_strategy):
        r"""Sets the backup_retention_strategy of this DeleteGaussMySqlInstanceRequestBody.

        **参数解释**：  释放实例时的备份保留策略。  **约束限制**：  不涉及。  **取值范围**：  - retain_all：永久保留全部备份，包含回收站备份、自动全量备份、自动差量备份、手动备份，不包含增量备份。实例删除后，永久保留的备份会产生费用。 - retain_last：保留回收站备份和手动备份。超过回收站策略的保留天数后，系统将删除回收站备份，仅保留手动备份。手动备份会产生费用，其余保留的备份不收费。 - delete_all：删除全部备份。  **默认取值**：  retain_last。

        :param backup_retention_strategy: The backup_retention_strategy of this DeleteGaussMySqlInstanceRequestBody.
        :type backup_retention_strategy: str
        """
        self._backup_retention_strategy = backup_retention_strategy

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
        if not isinstance(other, DeleteGaussMySqlInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
