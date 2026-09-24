# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluationTaskResponseBodyDataUsage:

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
        'prompt_tokens': 'int',
        'completion_tokens': 'int',
        'total_tokens': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'prompt_tokens': 'prompt_tokens',
        'completion_tokens': 'completion_tokens',
        'total_tokens': 'total_tokens'
    }

    def __init__(self, task_id=None, prompt_tokens=None, completion_tokens=None, total_tokens=None):
        r"""ShowOpsEvaluationTaskResponseBodyDataUsage

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param prompt_tokens: 输入 Token 数
        :type prompt_tokens: int
        :param completion_tokens: 输出 Token 数
        :type completion_tokens: int
        :param total_tokens: 总 Token 数
        :type total_tokens: int
        """
        
        

        self._task_id = None
        self._prompt_tokens = None
        self._completion_tokens = None
        self._total_tokens = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if prompt_tokens is not None:
            self.prompt_tokens = prompt_tokens
        if completion_tokens is not None:
            self.completion_tokens = completion_tokens
        if total_tokens is not None:
            self.total_tokens = total_tokens

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowOpsEvaluationTaskResponseBodyDataUsage.

        任务ID

        :return: The task_id of this ShowOpsEvaluationTaskResponseBodyDataUsage.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowOpsEvaluationTaskResponseBodyDataUsage.

        任务ID

        :param task_id: The task_id of this ShowOpsEvaluationTaskResponseBodyDataUsage.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def prompt_tokens(self):
        r"""Gets the prompt_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.

        输入 Token 数

        :return: The prompt_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.
        :rtype: int
        """
        return self._prompt_tokens

    @prompt_tokens.setter
    def prompt_tokens(self, prompt_tokens):
        r"""Sets the prompt_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.

        输入 Token 数

        :param prompt_tokens: The prompt_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.
        :type prompt_tokens: int
        """
        self._prompt_tokens = prompt_tokens

    @property
    def completion_tokens(self):
        r"""Gets the completion_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.

        输出 Token 数

        :return: The completion_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.
        :rtype: int
        """
        return self._completion_tokens

    @completion_tokens.setter
    def completion_tokens(self, completion_tokens):
        r"""Sets the completion_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.

        输出 Token 数

        :param completion_tokens: The completion_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.
        :type completion_tokens: int
        """
        self._completion_tokens = completion_tokens

    @property
    def total_tokens(self):
        r"""Gets the total_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.

        总 Token 数

        :return: The total_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.
        :rtype: int
        """
        return self._total_tokens

    @total_tokens.setter
    def total_tokens(self, total_tokens):
        r"""Sets the total_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.

        总 Token 数

        :param total_tokens: The total_tokens of this ShowOpsEvaluationTaskResponseBodyDataUsage.
        :type total_tokens: int
        """
        self._total_tokens = total_tokens

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
        if not isinstance(other, ShowOpsEvaluationTaskResponseBodyDataUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
