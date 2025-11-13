# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBatchOperationTaskRequest:

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
        'error_item_limit': 'int',
        'error_item_offset': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'error_item_limit': 'error_item_limit',
        'error_item_offset': 'error_item_offset'
    }

    def __init__(self, task_id=None, error_item_limit=None, error_item_offset=None):
        r"""ShowBatchOperationTaskRequest

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 批量操作任务的ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type task_id: str
        :param error_item_limit: **参数解释：** 分页查询时配置每页返回的失败条目个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500
        :type error_item_limit: int
        :param error_item_offset: **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个失败条目开始查询。 **约束限制：** 不涉及。 **取值范围：** 0~2147483647。 **默认取值：** 0
        :type error_item_offset: int
        """
        
        

        self._task_id = None
        self._error_item_limit = None
        self._error_item_offset = None
        self.discriminator = None

        self.task_id = task_id
        if error_item_limit is not None:
            self.error_item_limit = error_item_limit
        if error_item_offset is not None:
            self.error_item_offset = error_item_offset

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowBatchOperationTaskRequest.

        **参数解释：** 批量操作任务的ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The task_id of this ShowBatchOperationTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowBatchOperationTaskRequest.

        **参数解释：** 批量操作任务的ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param task_id: The task_id of this ShowBatchOperationTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def error_item_limit(self):
        r"""Gets the error_item_limit of this ShowBatchOperationTaskRequest.

        **参数解释：** 分页查询时配置每页返回的失败条目个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500

        :return: The error_item_limit of this ShowBatchOperationTaskRequest.
        :rtype: int
        """
        return self._error_item_limit

    @error_item_limit.setter
    def error_item_limit(self, error_item_limit):
        r"""Sets the error_item_limit of this ShowBatchOperationTaskRequest.

        **参数解释：** 分页查询时配置每页返回的失败条目个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500

        :param error_item_limit: The error_item_limit of this ShowBatchOperationTaskRequest.
        :type error_item_limit: int
        """
        self._error_item_limit = error_item_limit

    @property
    def error_item_offset(self):
        r"""Gets the error_item_offset of this ShowBatchOperationTaskRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个失败条目开始查询。 **约束限制：** 不涉及。 **取值范围：** 0~2147483647。 **默认取值：** 0

        :return: The error_item_offset of this ShowBatchOperationTaskRequest.
        :rtype: int
        """
        return self._error_item_offset

    @error_item_offset.setter
    def error_item_offset(self, error_item_offset):
        r"""Sets the error_item_offset of this ShowBatchOperationTaskRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个失败条目开始查询。 **约束限制：** 不涉及。 **取值范围：** 0~2147483647。 **默认取值：** 0

        :param error_item_offset: The error_item_offset of this ShowBatchOperationTaskRequest.
        :type error_item_offset: int
        """
        self._error_item_offset = error_item_offset

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
        if not isinstance(other, ShowBatchOperationTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
