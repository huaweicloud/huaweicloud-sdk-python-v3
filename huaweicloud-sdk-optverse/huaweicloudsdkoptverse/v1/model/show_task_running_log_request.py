# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskRunningLogRequest:

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
        'start_byte': 'int',
        'end_byte': 'int'
    }

    attribute_map = {
        'evolve_task_id': 'evolve_task_id',
        'start_byte': 'start_byte',
        'end_byte': 'end_byte'
    }

    def __init__(self, evolve_task_id=None, start_byte=None, end_byte=None):
        r"""ShowTaskRunningLogRequest

        The model defined in huaweicloud sdk

        :param evolve_task_id: **参数解释**： 演化任务标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type evolve_task_id: str
        :param start_byte: **参数解释**： 算法的启动时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type start_byte: int
        :param end_byte: **参数解释**： 算法的最后更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type end_byte: int
        """
        
        

        self._evolve_task_id = None
        self._start_byte = None
        self._end_byte = None
        self.discriminator = None

        self.evolve_task_id = evolve_task_id
        if start_byte is not None:
            self.start_byte = start_byte
        if end_byte is not None:
            self.end_byte = end_byte

    @property
    def evolve_task_id(self):
        r"""Gets the evolve_task_id of this ShowTaskRunningLogRequest.

        **参数解释**： 演化任务标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The evolve_task_id of this ShowTaskRunningLogRequest.
        :rtype: str
        """
        return self._evolve_task_id

    @evolve_task_id.setter
    def evolve_task_id(self, evolve_task_id):
        r"""Sets the evolve_task_id of this ShowTaskRunningLogRequest.

        **参数解释**： 演化任务标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param evolve_task_id: The evolve_task_id of this ShowTaskRunningLogRequest.
        :type evolve_task_id: str
        """
        self._evolve_task_id = evolve_task_id

    @property
    def start_byte(self):
        r"""Gets the start_byte of this ShowTaskRunningLogRequest.

        **参数解释**： 算法的启动时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The start_byte of this ShowTaskRunningLogRequest.
        :rtype: int
        """
        return self._start_byte

    @start_byte.setter
    def start_byte(self, start_byte):
        r"""Sets the start_byte of this ShowTaskRunningLogRequest.

        **参数解释**： 算法的启动时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param start_byte: The start_byte of this ShowTaskRunningLogRequest.
        :type start_byte: int
        """
        self._start_byte = start_byte

    @property
    def end_byte(self):
        r"""Gets the end_byte of this ShowTaskRunningLogRequest.

        **参数解释**： 算法的最后更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The end_byte of this ShowTaskRunningLogRequest.
        :rtype: int
        """
        return self._end_byte

    @end_byte.setter
    def end_byte(self, end_byte):
        r"""Sets the end_byte of this ShowTaskRunningLogRequest.

        **参数解释**： 算法的最后更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param end_byte: The end_byte of this ShowTaskRunningLogRequest.
        :type end_byte: int
        """
        self._end_byte = end_byte

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
        if not isinstance(other, ShowTaskRunningLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
