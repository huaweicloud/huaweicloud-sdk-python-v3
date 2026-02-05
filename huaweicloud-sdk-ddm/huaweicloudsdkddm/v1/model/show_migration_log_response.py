# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMigrationLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_logs': 'list[TaskLogsVO]',
        'cur_page': 'int',
        'per_page': 'int',
        'total': 'int'
    }

    attribute_map = {
        'task_logs': 'task_logs',
        'cur_page': 'cur_page',
        'per_page': 'per_page',
        'total': 'total'
    }

    def __init__(self, task_logs=None, cur_page=None, per_page=None, total=None):
        r"""ShowMigrationLogResponse

        The model defined in huaweicloud sdk

        :param task_logs: **参数解释**：  分片变更任务日志的集合。  **参数范围**：  不涉及。
        :type task_logs: list[:class:`huaweicloudsdkddm.v1.TaskLogsVO`]
        :param cur_page: **参数解释**：  当前页。  **参数范围**：  不涉及。
        :type cur_page: int
        :param per_page: **参数解释**：  每页条数。  **参数范围**：  不涉及。
        :type per_page: int
        :param total: **参数解释**：  总量。  **参数范围**：  不涉及。
        :type total: int
        """
        
        super().__init__()

        self._task_logs = None
        self._cur_page = None
        self._per_page = None
        self._total = None
        self.discriminator = None

        if task_logs is not None:
            self.task_logs = task_logs
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page
        if total is not None:
            self.total = total

    @property
    def task_logs(self):
        r"""Gets the task_logs of this ShowMigrationLogResponse.

        **参数解释**：  分片变更任务日志的集合。  **参数范围**：  不涉及。

        :return: The task_logs of this ShowMigrationLogResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.TaskLogsVO`]
        """
        return self._task_logs

    @task_logs.setter
    def task_logs(self, task_logs):
        r"""Sets the task_logs of this ShowMigrationLogResponse.

        **参数解释**：  分片变更任务日志的集合。  **参数范围**：  不涉及。

        :param task_logs: The task_logs of this ShowMigrationLogResponse.
        :type task_logs: list[:class:`huaweicloudsdkddm.v1.TaskLogsVO`]
        """
        self._task_logs = task_logs

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ShowMigrationLogResponse.

        **参数解释**：  当前页。  **参数范围**：  不涉及。

        :return: The cur_page of this ShowMigrationLogResponse.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ShowMigrationLogResponse.

        **参数解释**：  当前页。  **参数范围**：  不涉及。

        :param cur_page: The cur_page of this ShowMigrationLogResponse.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ShowMigrationLogResponse.

        **参数解释**：  每页条数。  **参数范围**：  不涉及。

        :return: The per_page of this ShowMigrationLogResponse.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ShowMigrationLogResponse.

        **参数解释**：  每页条数。  **参数范围**：  不涉及。

        :param per_page: The per_page of this ShowMigrationLogResponse.
        :type per_page: int
        """
        self._per_page = per_page

    @property
    def total(self):
        r"""Gets the total of this ShowMigrationLogResponse.

        **参数解释**：  总量。  **参数范围**：  不涉及。

        :return: The total of this ShowMigrationLogResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowMigrationLogResponse.

        **参数解释**：  总量。  **参数范围**：  不涉及。

        :param total: The total of this ShowMigrationLogResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ShowMigrationLogResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowMigrationLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
