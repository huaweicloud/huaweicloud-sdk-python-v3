# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsModelTuningTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'status_count': 'OpsModelTuningTaskStatusCount',
        'tasks': 'list[OpsModelTuningTask]'
    }

    attribute_map = {
        'total': 'total',
        'status_count': 'status_count',
        'tasks': 'tasks'
    }

    def __init__(self, total=None, status_count=None, tasks=None):
        r"""ListOpsModelTuningTasksResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释：** 满足过滤条件的记录总数，用于计算分页总页数。  **取值范围：** 0-100的整数。
        :type total: int
        :param status_count: 
        :type status_count: :class:`huaweicloudsdkagentarts.v1.OpsModelTuningTaskStatusCount`
        :param tasks: **参数解释：** 任务列表，表示当前分页下的任务详情列表。  **取值范围：** 符合OpsModelTuningTask 定义的对象数组。
        :type tasks: list[:class:`huaweicloudsdkagentarts.v1.OpsModelTuningTask`]
        """
        
        super().__init__()

        self._total = None
        self._status_count = None
        self._tasks = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if status_count is not None:
            self.status_count = status_count
        if tasks is not None:
            self.tasks = tasks

    @property
    def total(self):
        r"""Gets the total of this ListOpsModelTuningTasksResponse.

        **参数解释：** 满足过滤条件的记录总数，用于计算分页总页数。  **取值范围：** 0-100的整数。

        :return: The total of this ListOpsModelTuningTasksResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOpsModelTuningTasksResponse.

        **参数解释：** 满足过滤条件的记录总数，用于计算分页总页数。  **取值范围：** 0-100的整数。

        :param total: The total of this ListOpsModelTuningTasksResponse.
        :type total: int
        """
        self._total = total

    @property
    def status_count(self):
        r"""Gets the status_count of this ListOpsModelTuningTasksResponse.

        :return: The status_count of this ListOpsModelTuningTasksResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsModelTuningTaskStatusCount`
        """
        return self._status_count

    @status_count.setter
    def status_count(self, status_count):
        r"""Sets the status_count of this ListOpsModelTuningTasksResponse.

        :param status_count: The status_count of this ListOpsModelTuningTasksResponse.
        :type status_count: :class:`huaweicloudsdkagentarts.v1.OpsModelTuningTaskStatusCount`
        """
        self._status_count = status_count

    @property
    def tasks(self):
        r"""Gets the tasks of this ListOpsModelTuningTasksResponse.

        **参数解释：** 任务列表，表示当前分页下的任务详情列表。  **取值范围：** 符合OpsModelTuningTask 定义的对象数组。

        :return: The tasks of this ListOpsModelTuningTasksResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsModelTuningTask`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListOpsModelTuningTasksResponse.

        **参数解释：** 任务列表，表示当前分页下的任务详情列表。  **取值范围：** 符合OpsModelTuningTask 定义的对象数组。

        :param tasks: The tasks of this ListOpsModelTuningTasksResponse.
        :type tasks: list[:class:`huaweicloudsdkagentarts.v1.OpsModelTuningTask`]
        """
        self._tasks = tasks

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsModelTuningTasksResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOpsModelTuningTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
