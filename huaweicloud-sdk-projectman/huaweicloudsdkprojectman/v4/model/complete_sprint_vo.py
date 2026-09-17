# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompleteSprintVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate': 'str',
        'move_to_sprint_id': 'str'
    }

    attribute_map = {
        'operate': 'operate',
        'move_to_sprint_id': 'move_to_sprint_id'
    }

    def __init__(self, operate=None, move_to_sprint_id=None):
        r"""CompleteSprintVO

        The model defined in huaweicloud sdk

        :param operate: **参数解释**： 操作类型。 **约束限制**： 不涉及。 **取值范围**： - start：开始发布/迭代计划 - complete：完成发布/迭代计划 - reset：将计划状态设置为\&quot;未开始\&quot; - restart：重新开始发布/迭代计划 - move：将工作项移动到其他迭代 **默认取值**： 不涉及。
        :type operate: str
        :param move_to_sprint_id: **参数解释**： 将工作项移动到指定迭代ID。operate参数值为complete时，需要将未完成的工作项移动到其他迭代。 **约束限制**： operate参数值为complete时需填写。空字符串表示将工作项移动到\&quot;待规划\&quot;。 **取值范围**： 长度为18~19个字符的数字字符串。 **默认取值**： 不涉及。
        :type move_to_sprint_id: str
        """
        
        

        self._operate = None
        self._move_to_sprint_id = None
        self.discriminator = None

        self.operate = operate
        if move_to_sprint_id is not None:
            self.move_to_sprint_id = move_to_sprint_id

    @property
    def operate(self):
        r"""Gets the operate of this CompleteSprintVO.

        **参数解释**： 操作类型。 **约束限制**： 不涉及。 **取值范围**： - start：开始发布/迭代计划 - complete：完成发布/迭代计划 - reset：将计划状态设置为\"未开始\" - restart：重新开始发布/迭代计划 - move：将工作项移动到其他迭代 **默认取值**： 不涉及。

        :return: The operate of this CompleteSprintVO.
        :rtype: str
        """
        return self._operate

    @operate.setter
    def operate(self, operate):
        r"""Sets the operate of this CompleteSprintVO.

        **参数解释**： 操作类型。 **约束限制**： 不涉及。 **取值范围**： - start：开始发布/迭代计划 - complete：完成发布/迭代计划 - reset：将计划状态设置为\"未开始\" - restart：重新开始发布/迭代计划 - move：将工作项移动到其他迭代 **默认取值**： 不涉及。

        :param operate: The operate of this CompleteSprintVO.
        :type operate: str
        """
        self._operate = operate

    @property
    def move_to_sprint_id(self):
        r"""Gets the move_to_sprint_id of this CompleteSprintVO.

        **参数解释**： 将工作项移动到指定迭代ID。operate参数值为complete时，需要将未完成的工作项移动到其他迭代。 **约束限制**： operate参数值为complete时需填写。空字符串表示将工作项移动到\"待规划\"。 **取值范围**： 长度为18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :return: The move_to_sprint_id of this CompleteSprintVO.
        :rtype: str
        """
        return self._move_to_sprint_id

    @move_to_sprint_id.setter
    def move_to_sprint_id(self, move_to_sprint_id):
        r"""Sets the move_to_sprint_id of this CompleteSprintVO.

        **参数解释**： 将工作项移动到指定迭代ID。operate参数值为complete时，需要将未完成的工作项移动到其他迭代。 **约束限制**： operate参数值为complete时需填写。空字符串表示将工作项移动到\"待规划\"。 **取值范围**： 长度为18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :param move_to_sprint_id: The move_to_sprint_id of this CompleteSprintVO.
        :type move_to_sprint_id: str
        """
        self._move_to_sprint_id = move_to_sprint_id

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
        if not isinstance(other, CompleteSprintVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
