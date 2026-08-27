# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluatorParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'llm_models': 'list[str]',
        'evaluator_max_workers': 'int',
        'search_max_workers': 'int',
        'search_iterations': 'int',
        'smaller_better': 'bool',
        'search_population_size': 'int'
    }

    attribute_map = {
        'llm_models': 'llm_models',
        'evaluator_max_workers': 'evaluator_max_workers',
        'search_max_workers': 'search_max_workers',
        'search_iterations': 'search_iterations',
        'smaller_better': 'smaller_better',
        'search_population_size': 'search_population_size'
    }

    def __init__(self, llm_models=None, evaluator_max_workers=None, search_max_workers=None, search_iterations=None, smaller_better=None, search_population_size=None):
        r"""EvaluatorParameter

        The model defined in huaweicloud sdk

        :param llm_models: **参数解释**： 使用的llm模型列表。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,30]。 **默认取值**： 不涉及 
        :type llm_models: list[str]
        :param evaluator_max_workers: **参数解释**： 最大评估数量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,32]。 **默认取值**： 不涉及 
        :type evaluator_max_workers: int
        :param search_max_workers: **参数解释**： 最大生成数量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,32]。 **默认取值**： 不涉及 
        :type search_max_workers: int
        :param search_iterations: **参数解释**： 最大演化轮次。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,100]。 **默认取值**： 不涉及 
        :type search_iterations: int
        :param smaller_better: **参数解释**： 评估器返回值是越大越好还是越小越好。 **约束限制**： 不涉及 **取值范围**： 取值范围true，false。 **默认取值**： true 
        :type smaller_better: bool
        :param search_population_size: **参数解释**： 种群数量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,32]。 **默认取值**： 不涉及 
        :type search_population_size: int
        """
        
        

        self._llm_models = None
        self._evaluator_max_workers = None
        self._search_max_workers = None
        self._search_iterations = None
        self._smaller_better = None
        self._search_population_size = None
        self.discriminator = None

        self.llm_models = llm_models
        self.evaluator_max_workers = evaluator_max_workers
        self.search_max_workers = search_max_workers
        self.search_iterations = search_iterations
        if smaller_better is not None:
            self.smaller_better = smaller_better
        self.search_population_size = search_population_size

    @property
    def llm_models(self):
        r"""Gets the llm_models of this EvaluatorParameter.

        **参数解释**： 使用的llm模型列表。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,30]。 **默认取值**： 不涉及 

        :return: The llm_models of this EvaluatorParameter.
        :rtype: list[str]
        """
        return self._llm_models

    @llm_models.setter
    def llm_models(self, llm_models):
        r"""Sets the llm_models of this EvaluatorParameter.

        **参数解释**： 使用的llm模型列表。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,30]。 **默认取值**： 不涉及 

        :param llm_models: The llm_models of this EvaluatorParameter.
        :type llm_models: list[str]
        """
        self._llm_models = llm_models

    @property
    def evaluator_max_workers(self):
        r"""Gets the evaluator_max_workers of this EvaluatorParameter.

        **参数解释**： 最大评估数量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,32]。 **默认取值**： 不涉及 

        :return: The evaluator_max_workers of this EvaluatorParameter.
        :rtype: int
        """
        return self._evaluator_max_workers

    @evaluator_max_workers.setter
    def evaluator_max_workers(self, evaluator_max_workers):
        r"""Sets the evaluator_max_workers of this EvaluatorParameter.

        **参数解释**： 最大评估数量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,32]。 **默认取值**： 不涉及 

        :param evaluator_max_workers: The evaluator_max_workers of this EvaluatorParameter.
        :type evaluator_max_workers: int
        """
        self._evaluator_max_workers = evaluator_max_workers

    @property
    def search_max_workers(self):
        r"""Gets the search_max_workers of this EvaluatorParameter.

        **参数解释**： 最大生成数量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,32]。 **默认取值**： 不涉及 

        :return: The search_max_workers of this EvaluatorParameter.
        :rtype: int
        """
        return self._search_max_workers

    @search_max_workers.setter
    def search_max_workers(self, search_max_workers):
        r"""Sets the search_max_workers of this EvaluatorParameter.

        **参数解释**： 最大生成数量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,32]。 **默认取值**： 不涉及 

        :param search_max_workers: The search_max_workers of this EvaluatorParameter.
        :type search_max_workers: int
        """
        self._search_max_workers = search_max_workers

    @property
    def search_iterations(self):
        r"""Gets the search_iterations of this EvaluatorParameter.

        **参数解释**： 最大演化轮次。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,100]。 **默认取值**： 不涉及 

        :return: The search_iterations of this EvaluatorParameter.
        :rtype: int
        """
        return self._search_iterations

    @search_iterations.setter
    def search_iterations(self, search_iterations):
        r"""Sets the search_iterations of this EvaluatorParameter.

        **参数解释**： 最大演化轮次。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,100]。 **默认取值**： 不涉及 

        :param search_iterations: The search_iterations of this EvaluatorParameter.
        :type search_iterations: int
        """
        self._search_iterations = search_iterations

    @property
    def smaller_better(self):
        r"""Gets the smaller_better of this EvaluatorParameter.

        **参数解释**： 评估器返回值是越大越好还是越小越好。 **约束限制**： 不涉及 **取值范围**： 取值范围true，false。 **默认取值**： true 

        :return: The smaller_better of this EvaluatorParameter.
        :rtype: bool
        """
        return self._smaller_better

    @smaller_better.setter
    def smaller_better(self, smaller_better):
        r"""Sets the smaller_better of this EvaluatorParameter.

        **参数解释**： 评估器返回值是越大越好还是越小越好。 **约束限制**： 不涉及 **取值范围**： 取值范围true，false。 **默认取值**： true 

        :param smaller_better: The smaller_better of this EvaluatorParameter.
        :type smaller_better: bool
        """
        self._smaller_better = smaller_better

    @property
    def search_population_size(self):
        r"""Gets the search_population_size of this EvaluatorParameter.

        **参数解释**： 种群数量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,32]。 **默认取值**： 不涉及 

        :return: The search_population_size of this EvaluatorParameter.
        :rtype: int
        """
        return self._search_population_size

    @search_population_size.setter
    def search_population_size(self, search_population_size):
        r"""Sets the search_population_size of this EvaluatorParameter.

        **参数解释**： 种群数量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,32]。 **默认取值**： 不涉及 

        :param search_population_size: The search_population_size of this EvaluatorParameter.
        :type search_population_size: int
        """
        self._search_population_size = search_population_size

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
        if not isinstance(other, EvaluatorParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
