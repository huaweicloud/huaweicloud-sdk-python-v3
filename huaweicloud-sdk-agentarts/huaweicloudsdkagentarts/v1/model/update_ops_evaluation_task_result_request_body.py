# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOpsEvaluationTaskResultRequestBody:

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
        'evaluator_id': 'str',
        'evaluator_version': 'str',
        'item_id': 'str',
        'correction': 'UpdateOpsEvaluationTaskResultRequestBodyCorrection'
    }

    attribute_map = {
        'task_id': 'task_id',
        'evaluator_id': 'evaluator_id',
        'evaluator_version': 'evaluator_version',
        'item_id': 'item_id',
        'correction': 'correction'
    }

    def __init__(self, task_id=None, evaluator_id=None, evaluator_version=None, item_id=None, correction=None):
        r"""UpdateOpsEvaluationTaskResultRequestBody

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 评估任务的唯一标识符（ID）。 **约束限制：** 长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type task_id: str
        :param evaluator_id: **参数解释：** 执行评估的评估器唯一标识符。 **约束限制：** 长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type evaluator_id: str
        :param evaluator_version: **参数解释：** 评估器的版本号，用于精确锁定特定的评估算法版本。 **约束限制：** 长度为0到100个字符。 **取值范围：** 符合版本号格式的字符串，如\&quot;v1.0.0\&quot; **默认取值：** 不涉及。 
        :type evaluator_version: str
        :param item_id: **参数解释：** 具体需要校正的评估条目（Item）唯一标识符。 **约束限制：** 长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type item_id: str
        :param correction: 
        :type correction: :class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluationTaskResultRequestBodyCorrection`
        """
        
        

        self._task_id = None
        self._evaluator_id = None
        self._evaluator_version = None
        self._item_id = None
        self._correction = None
        self.discriminator = None

        self.task_id = task_id
        self.evaluator_id = evaluator_id
        self.evaluator_version = evaluator_version
        self.item_id = item_id
        self.correction = correction

    @property
    def task_id(self):
        r"""Gets the task_id of this UpdateOpsEvaluationTaskResultRequestBody.

        **参数解释：** 评估任务的唯一标识符（ID）。 **约束限制：** 长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The task_id of this UpdateOpsEvaluationTaskResultRequestBody.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this UpdateOpsEvaluationTaskResultRequestBody.

        **参数解释：** 评估任务的唯一标识符（ID）。 **约束限制：** 长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param task_id: The task_id of this UpdateOpsEvaluationTaskResultRequestBody.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this UpdateOpsEvaluationTaskResultRequestBody.

        **参数解释：** 执行评估的评估器唯一标识符。 **约束限制：** 长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The evaluator_id of this UpdateOpsEvaluationTaskResultRequestBody.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this UpdateOpsEvaluationTaskResultRequestBody.

        **参数解释：** 执行评估的评估器唯一标识符。 **约束限制：** 长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param evaluator_id: The evaluator_id of this UpdateOpsEvaluationTaskResultRequestBody.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def evaluator_version(self):
        r"""Gets the evaluator_version of this UpdateOpsEvaluationTaskResultRequestBody.

        **参数解释：** 评估器的版本号，用于精确锁定特定的评估算法版本。 **约束限制：** 长度为0到100个字符。 **取值范围：** 符合版本号格式的字符串，如\"v1.0.0\" **默认取值：** 不涉及。 

        :return: The evaluator_version of this UpdateOpsEvaluationTaskResultRequestBody.
        :rtype: str
        """
        return self._evaluator_version

    @evaluator_version.setter
    def evaluator_version(self, evaluator_version):
        r"""Sets the evaluator_version of this UpdateOpsEvaluationTaskResultRequestBody.

        **参数解释：** 评估器的版本号，用于精确锁定特定的评估算法版本。 **约束限制：** 长度为0到100个字符。 **取值范围：** 符合版本号格式的字符串，如\"v1.0.0\" **默认取值：** 不涉及。 

        :param evaluator_version: The evaluator_version of this UpdateOpsEvaluationTaskResultRequestBody.
        :type evaluator_version: str
        """
        self._evaluator_version = evaluator_version

    @property
    def item_id(self):
        r"""Gets the item_id of this UpdateOpsEvaluationTaskResultRequestBody.

        **参数解释：** 具体需要校正的评估条目（Item）唯一标识符。 **约束限制：** 长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The item_id of this UpdateOpsEvaluationTaskResultRequestBody.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this UpdateOpsEvaluationTaskResultRequestBody.

        **参数解释：** 具体需要校正的评估条目（Item）唯一标识符。 **约束限制：** 长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param item_id: The item_id of this UpdateOpsEvaluationTaskResultRequestBody.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def correction(self):
        r"""Gets the correction of this UpdateOpsEvaluationTaskResultRequestBody.

        :return: The correction of this UpdateOpsEvaluationTaskResultRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluationTaskResultRequestBodyCorrection`
        """
        return self._correction

    @correction.setter
    def correction(self, correction):
        r"""Sets the correction of this UpdateOpsEvaluationTaskResultRequestBody.

        :param correction: The correction of this UpdateOpsEvaluationTaskResultRequestBody.
        :type correction: :class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluationTaskResultRequestBodyCorrection`
        """
        self._correction = correction

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
        if not isinstance(other, UpdateOpsEvaluationTaskResultRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
