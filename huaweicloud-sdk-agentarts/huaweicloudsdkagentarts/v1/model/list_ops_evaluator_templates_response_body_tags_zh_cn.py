# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorTemplatesResponseBodyTagsZhCN:

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
        'category': 'list[str]'
    }

    attribute_map = {
        'business_scenario': 'BusinessScenario',
        'category': 'Category'
    }

    def __init__(self, business_scenario=None, category=None):
        r"""ListOpsEvaluatorTemplatesResponseBodyTagsZhCN

        The model defined in huaweicloud sdk

        :param business_scenario: **参数解释：** 业务场景标签。 **取值范围：** 如 AIGC。 
        :type business_scenario: list[str]
        :param category: **参数解释：** 功能类别标签。 **取值范围：** 如 LLM。 
        :type category: list[str]
        """
        
        

        self._business_scenario = None
        self._category = None
        self.discriminator = None

        if business_scenario is not None:
            self.business_scenario = business_scenario
        if category is not None:
            self.category = category

    @property
    def business_scenario(self):
        r"""Gets the business_scenario of this ListOpsEvaluatorTemplatesResponseBodyTagsZhCN.

        **参数解释：** 业务场景标签。 **取值范围：** 如 AIGC。 

        :return: The business_scenario of this ListOpsEvaluatorTemplatesResponseBodyTagsZhCN.
        :rtype: list[str]
        """
        return self._business_scenario

    @business_scenario.setter
    def business_scenario(self, business_scenario):
        r"""Sets the business_scenario of this ListOpsEvaluatorTemplatesResponseBodyTagsZhCN.

        **参数解释：** 业务场景标签。 **取值范围：** 如 AIGC。 

        :param business_scenario: The business_scenario of this ListOpsEvaluatorTemplatesResponseBodyTagsZhCN.
        :type business_scenario: list[str]
        """
        self._business_scenario = business_scenario

    @property
    def category(self):
        r"""Gets the category of this ListOpsEvaluatorTemplatesResponseBodyTagsZhCN.

        **参数解释：** 功能类别标签。 **取值范围：** 如 LLM。 

        :return: The category of this ListOpsEvaluatorTemplatesResponseBodyTagsZhCN.
        :rtype: list[str]
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListOpsEvaluatorTemplatesResponseBodyTagsZhCN.

        **参数解释：** 功能类别标签。 **取值范围：** 如 LLM。 

        :param category: The category of this ListOpsEvaluatorTemplatesResponseBodyTagsZhCN.
        :type category: list[str]
        """
        self._category = category

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
        if not isinstance(other, ListOpsEvaluatorTemplatesResponseBodyTagsZhCN):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
