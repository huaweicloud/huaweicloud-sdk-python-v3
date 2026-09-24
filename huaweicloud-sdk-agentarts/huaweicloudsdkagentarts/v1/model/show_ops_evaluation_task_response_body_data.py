# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluationTaskResponseBodyData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task': 'OpsEvaluationTaskSummary',
        'avg_score': 'dict(str, str)',
        'fuzz_name': 'list[str]',
        'usage': 'ShowOpsEvaluationTaskResponseBodyDataUsage'
    }

    attribute_map = {
        'task': 'task',
        'avg_score': 'avg_score',
        'fuzz_name': 'fuzz_name',
        'usage': 'usage'
    }

    def __init__(self, task=None, avg_score=None, fuzz_name=None, usage=None):
        r"""ShowOpsEvaluationTaskResponseBodyData

        The model defined in huaweicloud sdk

        :param task: 
        :type task: :class:`huaweicloudsdkagentarts.v1.OpsEvaluationTaskSummary`
        :param avg_score: 各评估器的平均得分（键为评估器ID，值为平均得分字符串）。
        :type avg_score: dict(str, str)
        :param fuzz_name: 同名任务列表（通过 name 参数模糊查询时的同名任务名称）。
        :type fuzz_name: list[str]
        :param usage: 
        :type usage: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskResponseBodyDataUsage`
        """
        
        

        self._task = None
        self._avg_score = None
        self._fuzz_name = None
        self._usage = None
        self.discriminator = None

        if task is not None:
            self.task = task
        if avg_score is not None:
            self.avg_score = avg_score
        if fuzz_name is not None:
            self.fuzz_name = fuzz_name
        if usage is not None:
            self.usage = usage

    @property
    def task(self):
        r"""Gets the task of this ShowOpsEvaluationTaskResponseBodyData.

        :return: The task of this ShowOpsEvaluationTaskResponseBodyData.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsEvaluationTaskSummary`
        """
        return self._task

    @task.setter
    def task(self, task):
        r"""Sets the task of this ShowOpsEvaluationTaskResponseBodyData.

        :param task: The task of this ShowOpsEvaluationTaskResponseBodyData.
        :type task: :class:`huaweicloudsdkagentarts.v1.OpsEvaluationTaskSummary`
        """
        self._task = task

    @property
    def avg_score(self):
        r"""Gets the avg_score of this ShowOpsEvaluationTaskResponseBodyData.

        各评估器的平均得分（键为评估器ID，值为平均得分字符串）。

        :return: The avg_score of this ShowOpsEvaluationTaskResponseBodyData.
        :rtype: dict(str, str)
        """
        return self._avg_score

    @avg_score.setter
    def avg_score(self, avg_score):
        r"""Sets the avg_score of this ShowOpsEvaluationTaskResponseBodyData.

        各评估器的平均得分（键为评估器ID，值为平均得分字符串）。

        :param avg_score: The avg_score of this ShowOpsEvaluationTaskResponseBodyData.
        :type avg_score: dict(str, str)
        """
        self._avg_score = avg_score

    @property
    def fuzz_name(self):
        r"""Gets the fuzz_name of this ShowOpsEvaluationTaskResponseBodyData.

        同名任务列表（通过 name 参数模糊查询时的同名任务名称）。

        :return: The fuzz_name of this ShowOpsEvaluationTaskResponseBodyData.
        :rtype: list[str]
        """
        return self._fuzz_name

    @fuzz_name.setter
    def fuzz_name(self, fuzz_name):
        r"""Sets the fuzz_name of this ShowOpsEvaluationTaskResponseBodyData.

        同名任务列表（通过 name 参数模糊查询时的同名任务名称）。

        :param fuzz_name: The fuzz_name of this ShowOpsEvaluationTaskResponseBodyData.
        :type fuzz_name: list[str]
        """
        self._fuzz_name = fuzz_name

    @property
    def usage(self):
        r"""Gets the usage of this ShowOpsEvaluationTaskResponseBodyData.

        :return: The usage of this ShowOpsEvaluationTaskResponseBodyData.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskResponseBodyDataUsage`
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this ShowOpsEvaluationTaskResponseBodyData.

        :param usage: The usage of this ShowOpsEvaluationTaskResponseBodyData.
        :type usage: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskResponseBodyDataUsage`
        """
        self._usage = usage

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
        if not isinstance(other, ShowOpsEvaluationTaskResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
