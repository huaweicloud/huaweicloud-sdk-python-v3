# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordItem:

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
        'task_content': 'list[OnlineDDLTaskContentItem]',
        'created_at': 'int',
        'ended_at': 'int',
        'task_status': 'str',
        'alter_stage': 'int',
        'percentage': 'float',
        'error_reason': 'str',
        'temp_table_name': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_content': 'task_content',
        'created_at': 'created_at',
        'ended_at': 'ended_at',
        'task_status': 'task_status',
        'alter_stage': 'alter_stage',
        'percentage': 'percentage',
        'error_reason': 'error_reason',
        'temp_table_name': 'temp_table_name'
    }

    def __init__(self, task_id=None, task_content=None, created_at=None, ended_at=None, task_status=None, alter_stage=None, percentage=None, error_reason=None, temp_table_name=None):
        r"""RecordItem

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**：  无锁变更任务记录标识。  **取值范围**：  不涉及。
        :type task_id: str
        :param task_content: **参数解释**：  无锁变更任务详细内容。
        :type task_content: list[:class:`huaweicloudsdkgaussdb.v3.OnlineDDLTaskContentItem`]
        :param created_at: **参数解释**：  无锁变更任务创建时间，13位毫秒时间戳。  **取值范围**： 不涉及。
        :type created_at: int
        :param ended_at: **参数解释**：  无锁变更任务结束时间，13位毫秒时间戳。  **取值范围**： 不涉及。
        :type ended_at: int
        :param task_status: **参数解释**：  无锁变更任务执行状态。  **取值范围**：   - checking：表示正在执行预检查步骤。   - check successful： 表示预检查步骤执行成功。   - check failed： 表示预检查步骤执行失败。   - altering： 表示正在任务正在执行变更步骤。   - alter successful： 表示变更步骤执行成功。   - alter failed： 表示变更步骤执行失败。   - stopping：表示正在执行停止任务步骤。   - stop successful： 表示执行停止步骤成功。   - stop failed： 表示执行停止步骤失败。   - cleaning： 表示正在执行清理临时表步骤。   - clean successful： 表示清理临时表步骤执行成功。   - clean failed： 表示清理临时表步骤执行失败。
        :type task_status: str
        :param alter_stage: **参数解释**：  表示数据库内核层面无锁变更任务运行阶段。  **取值范围**：   - 0：表示无锁变更任务未开始。  - 1：表示无锁变更任务已完成资源初始化。  - 2：表示无锁变更任务正在运行。  - 3：表示无锁变更任务已完成。
        :type alter_stage: int
        :param percentage: **参数解释**：  无锁变更任务百分比进度，1位小数精度。  **取值范围**：  0.0-100.0。
        :type percentage: float
        :param error_reason: **参数解释**：  无锁变更任务失败原因，任务执行失败时有返回值。  **取值范围**： 不涉及。
        :type error_reason: str
        :param temp_table_name: **参数解释**：  无锁变更任务临时表名称，关闭临时表自动清理时有返回值。  **取值范围**： 不涉及。
        :type temp_table_name: str
        """
        
        

        self._task_id = None
        self._task_content = None
        self._created_at = None
        self._ended_at = None
        self._task_status = None
        self._alter_stage = None
        self._percentage = None
        self._error_reason = None
        self._temp_table_name = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_content is not None:
            self.task_content = task_content
        if created_at is not None:
            self.created_at = created_at
        if ended_at is not None:
            self.ended_at = ended_at
        if task_status is not None:
            self.task_status = task_status
        if alter_stage is not None:
            self.alter_stage = alter_stage
        if percentage is not None:
            self.percentage = percentage
        if error_reason is not None:
            self.error_reason = error_reason
        if temp_table_name is not None:
            self.temp_table_name = temp_table_name

    @property
    def task_id(self):
        r"""Gets the task_id of this RecordItem.

        **参数解释**：  无锁变更任务记录标识。  **取值范围**：  不涉及。

        :return: The task_id of this RecordItem.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this RecordItem.

        **参数解释**：  无锁变更任务记录标识。  **取值范围**：  不涉及。

        :param task_id: The task_id of this RecordItem.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_content(self):
        r"""Gets the task_content of this RecordItem.

        **参数解释**：  无锁变更任务详细内容。

        :return: The task_content of this RecordItem.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.OnlineDDLTaskContentItem`]
        """
        return self._task_content

    @task_content.setter
    def task_content(self, task_content):
        r"""Sets the task_content of this RecordItem.

        **参数解释**：  无锁变更任务详细内容。

        :param task_content: The task_content of this RecordItem.
        :type task_content: list[:class:`huaweicloudsdkgaussdb.v3.OnlineDDLTaskContentItem`]
        """
        self._task_content = task_content

    @property
    def created_at(self):
        r"""Gets the created_at of this RecordItem.

        **参数解释**：  无锁变更任务创建时间，13位毫秒时间戳。  **取值范围**： 不涉及。

        :return: The created_at of this RecordItem.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RecordItem.

        **参数解释**：  无锁变更任务创建时间，13位毫秒时间戳。  **取值范围**： 不涉及。

        :param created_at: The created_at of this RecordItem.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def ended_at(self):
        r"""Gets the ended_at of this RecordItem.

        **参数解释**：  无锁变更任务结束时间，13位毫秒时间戳。  **取值范围**： 不涉及。

        :return: The ended_at of this RecordItem.
        :rtype: int
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        r"""Sets the ended_at of this RecordItem.

        **参数解释**：  无锁变更任务结束时间，13位毫秒时间戳。  **取值范围**： 不涉及。

        :param ended_at: The ended_at of this RecordItem.
        :type ended_at: int
        """
        self._ended_at = ended_at

    @property
    def task_status(self):
        r"""Gets the task_status of this RecordItem.

        **参数解释**：  无锁变更任务执行状态。  **取值范围**：   - checking：表示正在执行预检查步骤。   - check successful： 表示预检查步骤执行成功。   - check failed： 表示预检查步骤执行失败。   - altering： 表示正在任务正在执行变更步骤。   - alter successful： 表示变更步骤执行成功。   - alter failed： 表示变更步骤执行失败。   - stopping：表示正在执行停止任务步骤。   - stop successful： 表示执行停止步骤成功。   - stop failed： 表示执行停止步骤失败。   - cleaning： 表示正在执行清理临时表步骤。   - clean successful： 表示清理临时表步骤执行成功。   - clean failed： 表示清理临时表步骤执行失败。

        :return: The task_status of this RecordItem.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this RecordItem.

        **参数解释**：  无锁变更任务执行状态。  **取值范围**：   - checking：表示正在执行预检查步骤。   - check successful： 表示预检查步骤执行成功。   - check failed： 表示预检查步骤执行失败。   - altering： 表示正在任务正在执行变更步骤。   - alter successful： 表示变更步骤执行成功。   - alter failed： 表示变更步骤执行失败。   - stopping：表示正在执行停止任务步骤。   - stop successful： 表示执行停止步骤成功。   - stop failed： 表示执行停止步骤失败。   - cleaning： 表示正在执行清理临时表步骤。   - clean successful： 表示清理临时表步骤执行成功。   - clean failed： 表示清理临时表步骤执行失败。

        :param task_status: The task_status of this RecordItem.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def alter_stage(self):
        r"""Gets the alter_stage of this RecordItem.

        **参数解释**：  表示数据库内核层面无锁变更任务运行阶段。  **取值范围**：   - 0：表示无锁变更任务未开始。  - 1：表示无锁变更任务已完成资源初始化。  - 2：表示无锁变更任务正在运行。  - 3：表示无锁变更任务已完成。

        :return: The alter_stage of this RecordItem.
        :rtype: int
        """
        return self._alter_stage

    @alter_stage.setter
    def alter_stage(self, alter_stage):
        r"""Sets the alter_stage of this RecordItem.

        **参数解释**：  表示数据库内核层面无锁变更任务运行阶段。  **取值范围**：   - 0：表示无锁变更任务未开始。  - 1：表示无锁变更任务已完成资源初始化。  - 2：表示无锁变更任务正在运行。  - 3：表示无锁变更任务已完成。

        :param alter_stage: The alter_stage of this RecordItem.
        :type alter_stage: int
        """
        self._alter_stage = alter_stage

    @property
    def percentage(self):
        r"""Gets the percentage of this RecordItem.

        **参数解释**：  无锁变更任务百分比进度，1位小数精度。  **取值范围**：  0.0-100.0。

        :return: The percentage of this RecordItem.
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        r"""Sets the percentage of this RecordItem.

        **参数解释**：  无锁变更任务百分比进度，1位小数精度。  **取值范围**：  0.0-100.0。

        :param percentage: The percentage of this RecordItem.
        :type percentage: float
        """
        self._percentage = percentage

    @property
    def error_reason(self):
        r"""Gets the error_reason of this RecordItem.

        **参数解释**：  无锁变更任务失败原因，任务执行失败时有返回值。  **取值范围**： 不涉及。

        :return: The error_reason of this RecordItem.
        :rtype: str
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        r"""Sets the error_reason of this RecordItem.

        **参数解释**：  无锁变更任务失败原因，任务执行失败时有返回值。  **取值范围**： 不涉及。

        :param error_reason: The error_reason of this RecordItem.
        :type error_reason: str
        """
        self._error_reason = error_reason

    @property
    def temp_table_name(self):
        r"""Gets the temp_table_name of this RecordItem.

        **参数解释**：  无锁变更任务临时表名称，关闭临时表自动清理时有返回值。  **取值范围**： 不涉及。

        :return: The temp_table_name of this RecordItem.
        :rtype: str
        """
        return self._temp_table_name

    @temp_table_name.setter
    def temp_table_name(self, temp_table_name):
        r"""Sets the temp_table_name of this RecordItem.

        **参数解释**：  无锁变更任务临时表名称，关闭临时表自动清理时有返回值。  **取值范围**： 不涉及。

        :param temp_table_name: The temp_table_name of this RecordItem.
        :type temp_table_name: str
        """
        self._temp_table_name = temp_table_name

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
        if not isinstance(other, RecordItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
