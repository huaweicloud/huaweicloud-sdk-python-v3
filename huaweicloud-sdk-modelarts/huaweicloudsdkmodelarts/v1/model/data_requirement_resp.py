# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataRequirementResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'conditions': 'list[ConstraintResp]',
        'value': 'dict(str, object)',
        'used_steps': 'list[str]',
        'delay': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'conditions': 'conditions',
        'value': 'value',
        'used_steps': 'used_steps',
        'delay': 'delay'
    }

    def __init__(self, name=None, type=None, conditions=None, value=None, used_steps=None, delay=None):
        r"""DataRequirementResp

        The model defined in huaweicloud sdk

        :param name: **参数解释**：训练数据的名称。 **取值范围**：不涉及。
        :type name: str
        :param type: **参数解释**：数据来源类型。 **取值范围**：枚举值如下： - dataset：数据集 - obs：OBS - swr：SWR - model_list：AI应用列表 - label_task：标注任务 - service：在线服务
        :type type: str
        :param conditions: **参数解释**：数据约束条件。
        :type conditions: list[:class:`huaweicloudsdkmodelarts.v1.ConstraintResp`]
        :param value: **参数解释**：数据的值。
        :type value: dict(str, object)
        :param used_steps: **参数解释**：使用了这条数据的工作流节点。
        :type used_steps: list[str]
        :param delay: **参数解释**：延时参数标记。 **取值范围**： - true：延时 - false：不延时
        :type delay: bool
        """
        
        

        self._name = None
        self._type = None
        self._conditions = None
        self._value = None
        self._used_steps = None
        self._delay = None
        self.discriminator = None

        self.name = name
        self.type = type
        if conditions is not None:
            self.conditions = conditions
        if value is not None:
            self.value = value
        if used_steps is not None:
            self.used_steps = used_steps
        if delay is not None:
            self.delay = delay

    @property
    def name(self):
        r"""Gets the name of this DataRequirementResp.

        **参数解释**：训练数据的名称。 **取值范围**：不涉及。

        :return: The name of this DataRequirementResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DataRequirementResp.

        **参数解释**：训练数据的名称。 **取值范围**：不涉及。

        :param name: The name of this DataRequirementResp.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this DataRequirementResp.

        **参数解释**：数据来源类型。 **取值范围**：枚举值如下： - dataset：数据集 - obs：OBS - swr：SWR - model_list：AI应用列表 - label_task：标注任务 - service：在线服务

        :return: The type of this DataRequirementResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DataRequirementResp.

        **参数解释**：数据来源类型。 **取值范围**：枚举值如下： - dataset：数据集 - obs：OBS - swr：SWR - model_list：AI应用列表 - label_task：标注任务 - service：在线服务

        :param type: The type of this DataRequirementResp.
        :type type: str
        """
        self._type = type

    @property
    def conditions(self):
        r"""Gets the conditions of this DataRequirementResp.

        **参数解释**：数据约束条件。

        :return: The conditions of this DataRequirementResp.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ConstraintResp`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this DataRequirementResp.

        **参数解释**：数据约束条件。

        :param conditions: The conditions of this DataRequirementResp.
        :type conditions: list[:class:`huaweicloudsdkmodelarts.v1.ConstraintResp`]
        """
        self._conditions = conditions

    @property
    def value(self):
        r"""Gets the value of this DataRequirementResp.

        **参数解释**：数据的值。

        :return: The value of this DataRequirementResp.
        :rtype: dict(str, object)
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this DataRequirementResp.

        **参数解释**：数据的值。

        :param value: The value of this DataRequirementResp.
        :type value: dict(str, object)
        """
        self._value = value

    @property
    def used_steps(self):
        r"""Gets the used_steps of this DataRequirementResp.

        **参数解释**：使用了这条数据的工作流节点。

        :return: The used_steps of this DataRequirementResp.
        :rtype: list[str]
        """
        return self._used_steps

    @used_steps.setter
    def used_steps(self, used_steps):
        r"""Sets the used_steps of this DataRequirementResp.

        **参数解释**：使用了这条数据的工作流节点。

        :param used_steps: The used_steps of this DataRequirementResp.
        :type used_steps: list[str]
        """
        self._used_steps = used_steps

    @property
    def delay(self):
        r"""Gets the delay of this DataRequirementResp.

        **参数解释**：延时参数标记。 **取值范围**： - true：延时 - false：不延时

        :return: The delay of this DataRequirementResp.
        :rtype: bool
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this DataRequirementResp.

        **参数解释**：延时参数标记。 **取值范围**： - true：延时 - false：不延时

        :param delay: The delay of this DataRequirementResp.
        :type delay: bool
        """
        self._delay = delay

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
        if not isinstance(other, DataRequirementResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
