# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluationTasksResponseBodyData:

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
        'items': 'list[OpsEvaluationTaskSummary]',
        'avg_score': 'dict(str, str)',
        'total_task_status': 'ListOpsEvaluationTasksResponseBodyDataTotalTaskStatus'
    }

    attribute_map = {
        'total': 'total',
        'items': 'items',
        'avg_score': 'avg_score',
        'total_task_status': 'total_task_status'
    }

    def __init__(self, total=None, items=None, avg_score=None, total_task_status=None):
        r"""ListOpsEvaluationTasksResponseBodyData

        The model defined in huaweicloud sdk

        :param total: 符合条件的任务总数。
        :type total: int
        :param items: 评估任务列表。
        :type items: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluationTaskSummary`]
        :param avg_score: 各评估器的平均得分（键为评估器ID，值为平均得分字符串）。
        :type avg_score: dict(str, str)
        :param total_task_status: 
        :type total_task_status: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationTasksResponseBodyDataTotalTaskStatus`
        """
        
        

        self._total = None
        self._items = None
        self._avg_score = None
        self._total_task_status = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if items is not None:
            self.items = items
        if avg_score is not None:
            self.avg_score = avg_score
        if total_task_status is not None:
            self.total_task_status = total_task_status

    @property
    def total(self):
        r"""Gets the total of this ListOpsEvaluationTasksResponseBodyData.

        符合条件的任务总数。

        :return: The total of this ListOpsEvaluationTasksResponseBodyData.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOpsEvaluationTasksResponseBodyData.

        符合条件的任务总数。

        :param total: The total of this ListOpsEvaluationTasksResponseBodyData.
        :type total: int
        """
        self._total = total

    @property
    def items(self):
        r"""Gets the items of this ListOpsEvaluationTasksResponseBodyData.

        评估任务列表。

        :return: The items of this ListOpsEvaluationTasksResponseBodyData.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluationTaskSummary`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListOpsEvaluationTasksResponseBodyData.

        评估任务列表。

        :param items: The items of this ListOpsEvaluationTasksResponseBodyData.
        :type items: list[:class:`huaweicloudsdkagentarts.v1.OpsEvaluationTaskSummary`]
        """
        self._items = items

    @property
    def avg_score(self):
        r"""Gets the avg_score of this ListOpsEvaluationTasksResponseBodyData.

        各评估器的平均得分（键为评估器ID，值为平均得分字符串）。

        :return: The avg_score of this ListOpsEvaluationTasksResponseBodyData.
        :rtype: dict(str, str)
        """
        return self._avg_score

    @avg_score.setter
    def avg_score(self, avg_score):
        r"""Sets the avg_score of this ListOpsEvaluationTasksResponseBodyData.

        各评估器的平均得分（键为评估器ID，值为平均得分字符串）。

        :param avg_score: The avg_score of this ListOpsEvaluationTasksResponseBodyData.
        :type avg_score: dict(str, str)
        """
        self._avg_score = avg_score

    @property
    def total_task_status(self):
        r"""Gets the total_task_status of this ListOpsEvaluationTasksResponseBodyData.

        :return: The total_task_status of this ListOpsEvaluationTasksResponseBodyData.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationTasksResponseBodyDataTotalTaskStatus`
        """
        return self._total_task_status

    @total_task_status.setter
    def total_task_status(self, total_task_status):
        r"""Sets the total_task_status of this ListOpsEvaluationTasksResponseBodyData.

        :param total_task_status: The total_task_status of this ListOpsEvaluationTasksResponseBodyData.
        :type total_task_status: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationTasksResponseBodyDataTotalTaskStatus`
        """
        self._total_task_status = total_task_status

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
        if not isinstance(other, ListOpsEvaluationTasksResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
