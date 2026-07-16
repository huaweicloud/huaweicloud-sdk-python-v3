# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_scenario': 'list[str]',
        'category': 'list[str]',
        'name': 'list[str]',
        'objective': 'list[str]',
        'target_type': 'list[str]'
    }

    attribute_map = {
        'business_scenario': 'BusinessScenario',
        'category': 'Category',
        'name': 'Name',
        'objective': 'Objective',
        'target_type': 'TargetType'
    }

    def __init__(self, business_scenario=None, category=None, name=None, objective=None, target_type=None):
        r"""ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN

        The model defined in huaweicloud sdk

        :param business_scenario: **参数解释：** 业务场景标签。 **取值范围：** 不涉及。 
        :type business_scenario: list[str]
        :param category: **参数解释：** 类型标签标识技术领域。 **取值范围：** 不涉及。 
        :type category: list[str]
        :param name: **参数解释：** 名字标签标识功能特点。 **取值范围：** 不涉及。 
        :type name: list[str]
        :param objective: **参数解释：** 目标标签反映核心价值。 **取值范围：** 不涉及。 
        :type objective: list[str]
        :param target_type: **参数解释：** 目标类型标签标识处理对象。 **取值范围：** 不涉及。 
        :type target_type: list[str]
        """
        
        

        self._business_scenario = None
        self._category = None
        self._name = None
        self._objective = None
        self._target_type = None
        self.discriminator = None

        if business_scenario is not None:
            self.business_scenario = business_scenario
        if category is not None:
            self.category = category
        if name is not None:
            self.name = name
        if objective is not None:
            self.objective = objective
        if target_type is not None:
            self.target_type = target_type

    @property
    def business_scenario(self):
        r"""Gets the business_scenario of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.

        **参数解释：** 业务场景标签。 **取值范围：** 不涉及。 

        :return: The business_scenario of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.
        :rtype: list[str]
        """
        return self._business_scenario

    @business_scenario.setter
    def business_scenario(self, business_scenario):
        r"""Sets the business_scenario of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.

        **参数解释：** 业务场景标签。 **取值范围：** 不涉及。 

        :param business_scenario: The business_scenario of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.
        :type business_scenario: list[str]
        """
        self._business_scenario = business_scenario

    @property
    def category(self):
        r"""Gets the category of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.

        **参数解释：** 类型标签标识技术领域。 **取值范围：** 不涉及。 

        :return: The category of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.
        :rtype: list[str]
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.

        **参数解释：** 类型标签标识技术领域。 **取值范围：** 不涉及。 

        :param category: The category of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.
        :type category: list[str]
        """
        self._category = category

    @property
    def name(self):
        r"""Gets the name of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.

        **参数解释：** 名字标签标识功能特点。 **取值范围：** 不涉及。 

        :return: The name of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.

        **参数解释：** 名字标签标识功能特点。 **取值范围：** 不涉及。 

        :param name: The name of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.
        :type name: list[str]
        """
        self._name = name

    @property
    def objective(self):
        r"""Gets the objective of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.

        **参数解释：** 目标标签反映核心价值。 **取值范围：** 不涉及。 

        :return: The objective of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.
        :rtype: list[str]
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        r"""Sets the objective of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.

        **参数解释：** 目标标签反映核心价值。 **取值范围：** 不涉及。 

        :param objective: The objective of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.
        :type objective: list[str]
        """
        self._objective = objective

    @property
    def target_type(self):
        r"""Gets the target_type of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.

        **参数解释：** 目标类型标签标识处理对象。 **取值范围：** 不涉及。 

        :return: The target_type of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.
        :rtype: list[str]
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.

        **参数解释：** 目标类型标签标识处理对象。 **取值范围：** 不涉及。 

        :param target_type: The target_type of this ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN.
        :type target_type: list[str]
        """
        self._target_type = target_type

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
        if not isinstance(other, ShowOpsEvaluatorTemplateResponseBodyTemplateTagsZhCN):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
