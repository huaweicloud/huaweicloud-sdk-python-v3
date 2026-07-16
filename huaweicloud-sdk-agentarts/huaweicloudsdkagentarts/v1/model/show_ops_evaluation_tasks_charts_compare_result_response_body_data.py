# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluationTasksChartsCompareResultResponseBodyData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_metrics_stats': 'list[CompareTaskMetricsStat]'
    }

    attribute_map = {
        'task_metrics_stats': 'task_metrics_stats'
    }

    def __init__(self, task_metrics_stats=None):
        r"""ShowOpsEvaluationTasksChartsCompareResultResponseBodyData

        The model defined in huaweicloud sdk

        :param task_metrics_stats: 各任务的指标统计列表
        :type task_metrics_stats: list[:class:`huaweicloudsdkagentarts.v1.CompareTaskMetricsStat`]
        """
        
        

        self._task_metrics_stats = None
        self.discriminator = None

        if task_metrics_stats is not None:
            self.task_metrics_stats = task_metrics_stats

    @property
    def task_metrics_stats(self):
        r"""Gets the task_metrics_stats of this ShowOpsEvaluationTasksChartsCompareResultResponseBodyData.

        各任务的指标统计列表

        :return: The task_metrics_stats of this ShowOpsEvaluationTasksChartsCompareResultResponseBodyData.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CompareTaskMetricsStat`]
        """
        return self._task_metrics_stats

    @task_metrics_stats.setter
    def task_metrics_stats(self, task_metrics_stats):
        r"""Sets the task_metrics_stats of this ShowOpsEvaluationTasksChartsCompareResultResponseBodyData.

        各任务的指标统计列表

        :param task_metrics_stats: The task_metrics_stats of this ShowOpsEvaluationTasksChartsCompareResultResponseBodyData.
        :type task_metrics_stats: list[:class:`huaweicloudsdkagentarts.v1.CompareTaskMetricsStat`]
        """
        self._task_metrics_stats = task_metrics_stats

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
        if not isinstance(other, ShowOpsEvaluationTasksChartsCompareResultResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
