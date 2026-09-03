# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTrainingJobLogsFromAomRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'training_job_id': 'str',
        'task_id': 'str',
        'base_line': 'str',
        'lines': 'int',
        'order': 'str'
    }

    attribute_map = {
        'training_job_id': 'training_job_id',
        'task_id': 'task_id',
        'base_line': 'base_line',
        'lines': 'lines',
        'order': 'order'
    }

    def __init__(self, training_job_id=None, task_id=None, base_line=None, lines=None, order=None):
        r"""ShowTrainingJobLogsFromAomRequest

        The model defined in huaweicloud sdk

        :param training_job_id: 训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。
        :type training_job_id: str
        :param task_id: 训练作业的任务名称。可从训练作业详情中的status.tasks字段中获取。
        :type task_id: str
        :param base_line: **参数解释**：日志查询的基线行号，用于分页查询。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及（从最新日志开始查询）。
        :type base_line: str
        :param lines: **参数解释**：返回的日志行数。 **约束限制**：不涉及。 **取值范围**：1 ~ 500。 **默认取值**：50。
        :type lines: int
        :param order: **参数解释**：日志排序方式。 **约束限制**：不涉及。 **取值范围**：枚举值如下： - asc：升序（从旧到新） - desc：降序（从新到旧） **默认取值**：desc。
        :type order: str
        """
        
        

        self._training_job_id = None
        self._task_id = None
        self._base_line = None
        self._lines = None
        self._order = None
        self.discriminator = None

        self.training_job_id = training_job_id
        self.task_id = task_id
        if base_line is not None:
            self.base_line = base_line
        if lines is not None:
            self.lines = lines
        if order is not None:
            self.order = order

    @property
    def training_job_id(self):
        r"""Gets the training_job_id of this ShowTrainingJobLogsFromAomRequest.

        训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。

        :return: The training_job_id of this ShowTrainingJobLogsFromAomRequest.
        :rtype: str
        """
        return self._training_job_id

    @training_job_id.setter
    def training_job_id(self, training_job_id):
        r"""Sets the training_job_id of this ShowTrainingJobLogsFromAomRequest.

        训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。

        :param training_job_id: The training_job_id of this ShowTrainingJobLogsFromAomRequest.
        :type training_job_id: str
        """
        self._training_job_id = training_job_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowTrainingJobLogsFromAomRequest.

        训练作业的任务名称。可从训练作业详情中的status.tasks字段中获取。

        :return: The task_id of this ShowTrainingJobLogsFromAomRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowTrainingJobLogsFromAomRequest.

        训练作业的任务名称。可从训练作业详情中的status.tasks字段中获取。

        :param task_id: The task_id of this ShowTrainingJobLogsFromAomRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def base_line(self):
        r"""Gets the base_line of this ShowTrainingJobLogsFromAomRequest.

        **参数解释**：日志查询的基线行号，用于分页查询。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及（从最新日志开始查询）。

        :return: The base_line of this ShowTrainingJobLogsFromAomRequest.
        :rtype: str
        """
        return self._base_line

    @base_line.setter
    def base_line(self, base_line):
        r"""Sets the base_line of this ShowTrainingJobLogsFromAomRequest.

        **参数解释**：日志查询的基线行号，用于分页查询。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及（从最新日志开始查询）。

        :param base_line: The base_line of this ShowTrainingJobLogsFromAomRequest.
        :type base_line: str
        """
        self._base_line = base_line

    @property
    def lines(self):
        r"""Gets the lines of this ShowTrainingJobLogsFromAomRequest.

        **参数解释**：返回的日志行数。 **约束限制**：不涉及。 **取值范围**：1 ~ 500。 **默认取值**：50。

        :return: The lines of this ShowTrainingJobLogsFromAomRequest.
        :rtype: int
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        r"""Sets the lines of this ShowTrainingJobLogsFromAomRequest.

        **参数解释**：返回的日志行数。 **约束限制**：不涉及。 **取值范围**：1 ~ 500。 **默认取值**：50。

        :param lines: The lines of this ShowTrainingJobLogsFromAomRequest.
        :type lines: int
        """
        self._lines = lines

    @property
    def order(self):
        r"""Gets the order of this ShowTrainingJobLogsFromAomRequest.

        **参数解释**：日志排序方式。 **约束限制**：不涉及。 **取值范围**：枚举值如下： - asc：升序（从旧到新） - desc：降序（从新到旧） **默认取值**：desc。

        :return: The order of this ShowTrainingJobLogsFromAomRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ShowTrainingJobLogsFromAomRequest.

        **参数解释**：日志排序方式。 **约束限制**：不涉及。 **取值范围**：枚举值如下： - asc：升序（从旧到新） - desc：降序（从新到旧） **默认取值**：desc。

        :param order: The order of this ShowTrainingJobLogsFromAomRequest.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ShowTrainingJobLogsFromAomRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
