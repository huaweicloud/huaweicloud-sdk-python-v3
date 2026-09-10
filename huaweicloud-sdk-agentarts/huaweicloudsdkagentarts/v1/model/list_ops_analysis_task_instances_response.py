# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsAnalysisTaskInstancesResponse(SdkResponse):

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
        'task_instances': 'list[OpsAnalysisTaskInstanceListInfo]'
    }

    attribute_map = {
        'total': 'total',
        'task_instances': 'task_instances'
    }

    def __init__(self, total=None, task_instances=None):
        r"""ListOpsAnalysisTaskInstancesResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释：** 满足过滤条件的记录总数，用于计算分页总页数。 **取值范围：** 0-100的整数。
        :type total: int
        :param task_instances: **参数解释：** 具体分析任务执行的记录信息 **取值范围：** 不涉及
        :type task_instances: list[:class:`huaweicloudsdkagentarts.v1.OpsAnalysisTaskInstanceListInfo`]
        """
        
        super().__init__()

        self._total = None
        self._task_instances = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if task_instances is not None:
            self.task_instances = task_instances

    @property
    def total(self):
        r"""Gets the total of this ListOpsAnalysisTaskInstancesResponse.

        **参数解释：** 满足过滤条件的记录总数，用于计算分页总页数。 **取值范围：** 0-100的整数。

        :return: The total of this ListOpsAnalysisTaskInstancesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOpsAnalysisTaskInstancesResponse.

        **参数解释：** 满足过滤条件的记录总数，用于计算分页总页数。 **取值范围：** 0-100的整数。

        :param total: The total of this ListOpsAnalysisTaskInstancesResponse.
        :type total: int
        """
        self._total = total

    @property
    def task_instances(self):
        r"""Gets the task_instances of this ListOpsAnalysisTaskInstancesResponse.

        **参数解释：** 具体分析任务执行的记录信息 **取值范围：** 不涉及

        :return: The task_instances of this ListOpsAnalysisTaskInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsAnalysisTaskInstanceListInfo`]
        """
        return self._task_instances

    @task_instances.setter
    def task_instances(self, task_instances):
        r"""Sets the task_instances of this ListOpsAnalysisTaskInstancesResponse.

        **参数解释：** 具体分析任务执行的记录信息 **取值范围：** 不涉及

        :param task_instances: The task_instances of this ListOpsAnalysisTaskInstancesResponse.
        :type task_instances: list[:class:`huaweicloudsdkagentarts.v1.OpsAnalysisTaskInstanceListInfo`]
        """
        self._task_instances = task_instances

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsAnalysisTaskInstancesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOpsAnalysisTaskInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
