# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClearOnlineDDLTaskTempTableRequestV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_content': 'list[TaskContentItem]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_content': 'task_content'
    }

    def __init__(self, task_id=None, task_content=None):
        r"""ClearOnlineDDLTaskTempTableRequestV3

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**：   无锁变更任务唯一标识。  获取方法参见[查询无锁变更任务记录列表](https://support.huaweicloud.com/api-taurusdb/ListOnlineDdlTaskRecords.html)。   **约束限制**：   不涉及。   **取值范围**：   不涉及。  **默认取值**：   不涉及。
        :type task_id: str
        :param task_content: **参数解释**：  无锁变更任务详细内容，包含目标数据库和临时表名。  **约束限制**：  不涉及。
        :type task_content: list[:class:`huaweicloudsdkgaussdb.v3.TaskContentItem`]
        """
        
        

        self._task_id = None
        self._task_content = None
        self.discriminator = None

        self.task_id = task_id
        self.task_content = task_content

    @property
    def task_id(self):
        r"""Gets the task_id of this ClearOnlineDDLTaskTempTableRequestV3.

        **参数解释**：   无锁变更任务唯一标识。  获取方法参见[查询无锁变更任务记录列表](https://support.huaweicloud.com/api-taurusdb/ListOnlineDdlTaskRecords.html)。   **约束限制**：   不涉及。   **取值范围**：   不涉及。  **默认取值**：   不涉及。

        :return: The task_id of this ClearOnlineDDLTaskTempTableRequestV3.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ClearOnlineDDLTaskTempTableRequestV3.

        **参数解释**：   无锁变更任务唯一标识。  获取方法参见[查询无锁变更任务记录列表](https://support.huaweicloud.com/api-taurusdb/ListOnlineDdlTaskRecords.html)。   **约束限制**：   不涉及。   **取值范围**：   不涉及。  **默认取值**：   不涉及。

        :param task_id: The task_id of this ClearOnlineDDLTaskTempTableRequestV3.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_content(self):
        r"""Gets the task_content of this ClearOnlineDDLTaskTempTableRequestV3.

        **参数解释**：  无锁变更任务详细内容，包含目标数据库和临时表名。  **约束限制**：  不涉及。

        :return: The task_content of this ClearOnlineDDLTaskTempTableRequestV3.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.TaskContentItem`]
        """
        return self._task_content

    @task_content.setter
    def task_content(self, task_content):
        r"""Sets the task_content of this ClearOnlineDDLTaskTempTableRequestV3.

        **参数解释**：  无锁变更任务详细内容，包含目标数据库和临时表名。  **约束限制**：  不涉及。

        :param task_content: The task_content of this ClearOnlineDDLTaskTempTableRequestV3.
        :type task_content: list[:class:`huaweicloudsdkgaussdb.v3.TaskContentItem`]
        """
        self._task_content = task_content

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
        if not isinstance(other, ClearOnlineDDLTaskTempTableRequestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
