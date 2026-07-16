# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluationTasksCompareResultRequest:

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
        'task_ids': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_ids': 'task_ids',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, task_id=None, task_ids=None, offset=None, limit=None):
        r"""ShowOpsEvaluationTasksCompareResultRequest

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 基线评估任务的唯一标识符（ID）。 **约束限制：** 字符长度在0到100之间。 **取值范围：** 长度为0到100个字符的字符串。 **默认取值：** 不涉及。
        :type task_id: str
        :param task_ids: **参数解释：** 基线评估任务的唯一标识符列表，多个任务间用逗号相隔。 **约束限制：** 字符串类型，最大长度1000字符。 **取值范围：** 字符串长度不超过1000。 **默认取值：** 不涉及。
        :type task_ids: str
        :param offset: **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 
        :type offset: int
        :param limit: **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 
        :type limit: int
        """
        
        

        self._task_id = None
        self._task_ids = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.task_id = task_id
        self.task_ids = task_ids
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowOpsEvaluationTasksCompareResultRequest.

        **参数解释：** 基线评估任务的唯一标识符（ID）。 **约束限制：** 字符长度在0到100之间。 **取值范围：** 长度为0到100个字符的字符串。 **默认取值：** 不涉及。

        :return: The task_id of this ShowOpsEvaluationTasksCompareResultRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowOpsEvaluationTasksCompareResultRequest.

        **参数解释：** 基线评估任务的唯一标识符（ID）。 **约束限制：** 字符长度在0到100之间。 **取值范围：** 长度为0到100个字符的字符串。 **默认取值：** 不涉及。

        :param task_id: The task_id of this ShowOpsEvaluationTasksCompareResultRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_ids(self):
        r"""Gets the task_ids of this ShowOpsEvaluationTasksCompareResultRequest.

        **参数解释：** 基线评估任务的唯一标识符列表，多个任务间用逗号相隔。 **约束限制：** 字符串类型，最大长度1000字符。 **取值范围：** 字符串长度不超过1000。 **默认取值：** 不涉及。

        :return: The task_ids of this ShowOpsEvaluationTasksCompareResultRequest.
        :rtype: str
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        r"""Sets the task_ids of this ShowOpsEvaluationTasksCompareResultRequest.

        **参数解释：** 基线评估任务的唯一标识符列表，多个任务间用逗号相隔。 **约束限制：** 字符串类型，最大长度1000字符。 **取值范围：** 字符串长度不超过1000。 **默认取值：** 不涉及。

        :param task_ids: The task_ids of this ShowOpsEvaluationTasksCompareResultRequest.
        :type task_ids: str
        """
        self._task_ids = task_ids

    @property
    def offset(self):
        r"""Gets the offset of this ShowOpsEvaluationTasksCompareResultRequest.

        **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 

        :return: The offset of this ShowOpsEvaluationTasksCompareResultRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowOpsEvaluationTasksCompareResultRequest.

        **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 

        :param offset: The offset of this ShowOpsEvaluationTasksCompareResultRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowOpsEvaluationTasksCompareResultRequest.

        **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 

        :return: The limit of this ShowOpsEvaluationTasksCompareResultRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowOpsEvaluationTasksCompareResultRequest.

        **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 

        :param limit: The limit of this ShowOpsEvaluationTasksCompareResultRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowOpsEvaluationTasksCompareResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
