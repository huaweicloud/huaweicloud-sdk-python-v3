# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateOpsModelTuningTaskTagsRequest:

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
        'body': 'BatchCreateOpsModelTuningTaskTagsRequestBody'
    }

    attribute_map = {
        'task_id': 'task_id',
        'body': 'body'
    }

    def __init__(self, task_id=None, body=None):
        r"""BatchCreateOpsModelTuningTaskTagsRequest

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 模型优化任务ID，标识任务的唯一标识符。获取方法请参考查询模型优化任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无
        :type task_id: str
        :param body: Body of the BatchCreateOpsModelTuningTaskTagsRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.BatchCreateOpsModelTuningTaskTagsRequestBody`
        """
        
        

        self._task_id = None
        self._body = None
        self.discriminator = None

        self.task_id = task_id
        if body is not None:
            self.body = body

    @property
    def task_id(self):
        r"""Gets the task_id of this BatchCreateOpsModelTuningTaskTagsRequest.

        **参数解释：** 模型优化任务ID，标识任务的唯一标识符。获取方法请参考查询模型优化任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :return: The task_id of this BatchCreateOpsModelTuningTaskTagsRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this BatchCreateOpsModelTuningTaskTagsRequest.

        **参数解释：** 模型优化任务ID，标识任务的唯一标识符。获取方法请参考查询模型优化任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :param task_id: The task_id of this BatchCreateOpsModelTuningTaskTagsRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def body(self):
        r"""Gets the body of this BatchCreateOpsModelTuningTaskTagsRequest.

        :return: The body of this BatchCreateOpsModelTuningTaskTagsRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchCreateOpsModelTuningTaskTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCreateOpsModelTuningTaskTagsRequest.

        :param body: The body of this BatchCreateOpsModelTuningTaskTagsRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.BatchCreateOpsModelTuningTaskTagsRequestBody`
        """
        self._body = body

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
        if not isinstance(other, BatchCreateOpsModelTuningTaskTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
