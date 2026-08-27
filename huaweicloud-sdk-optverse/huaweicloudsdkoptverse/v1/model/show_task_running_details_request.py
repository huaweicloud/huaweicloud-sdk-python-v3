# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskRunningDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evolve_task_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'evolve_task_id': 'evolve_task_id',
        'type': 'type'
    }

    def __init__(self, evolve_task_id=None, type=None):
        r"""ShowTaskRunningDetailsRequest

        The model defined in huaweicloud sdk

        :param evolve_task_id: **参数解释**： 演化任务标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type evolve_task_id: str
        :param type: **参数解释**： 统计信息类型。 **约束限制**： 不涉及 **取值范围**： * PROGRESS： 进度信息。 * SUMMARY:   结果统计值。 * BEST_RESULT:  最优结果的commitId。 * GENERATION_STATS: 各迭代的统计值。 **默认取值**： 不涉及 
        :type type: str
        """
        
        

        self._evolve_task_id = None
        self._type = None
        self.discriminator = None

        self.evolve_task_id = evolve_task_id
        self.type = type

    @property
    def evolve_task_id(self):
        r"""Gets the evolve_task_id of this ShowTaskRunningDetailsRequest.

        **参数解释**： 演化任务标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The evolve_task_id of this ShowTaskRunningDetailsRequest.
        :rtype: str
        """
        return self._evolve_task_id

    @evolve_task_id.setter
    def evolve_task_id(self, evolve_task_id):
        r"""Sets the evolve_task_id of this ShowTaskRunningDetailsRequest.

        **参数解释**： 演化任务标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param evolve_task_id: The evolve_task_id of this ShowTaskRunningDetailsRequest.
        :type evolve_task_id: str
        """
        self._evolve_task_id = evolve_task_id

    @property
    def type(self):
        r"""Gets the type of this ShowTaskRunningDetailsRequest.

        **参数解释**： 统计信息类型。 **约束限制**： 不涉及 **取值范围**： * PROGRESS： 进度信息。 * SUMMARY:   结果统计值。 * BEST_RESULT:  最优结果的commitId。 * GENERATION_STATS: 各迭代的统计值。 **默认取值**： 不涉及 

        :return: The type of this ShowTaskRunningDetailsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowTaskRunningDetailsRequest.

        **参数解释**： 统计信息类型。 **约束限制**： 不涉及 **取值范围**： * PROGRESS： 进度信息。 * SUMMARY:   结果统计值。 * BEST_RESULT:  最优结果的commitId。 * GENERATION_STATS: 各迭代的统计值。 **默认取值**： 不涉及 

        :param type: The type of this ShowTaskRunningDetailsRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowTaskRunningDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
