# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvolveTaskCreateReq:

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
        'description': 'str',
        'output_path': 'str',
        'algorithm_id': 'str',
        'algorithm_file': 'str',
        'algorithm_func_name': 'str',
        'evaluator_file': 'str',
        'evaluator_func_name': 'str',
        'evaluator_baseline': 'str',
        'evaluator_baseline_func_name': 'str',
        'evaluator_parameter': 'EvaluatorParameter'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'output_path': 'output_path',
        'algorithm_id': 'algorithm_id',
        'algorithm_file': 'algorithm_file',
        'algorithm_func_name': 'algorithm_func_name',
        'evaluator_file': 'evaluator_file',
        'evaluator_func_name': 'evaluator_func_name',
        'evaluator_baseline': 'evaluator_baseline',
        'evaluator_baseline_func_name': 'evaluator_baseline_func_name',
        'evaluator_parameter': 'evaluator_parameter'
    }

    def __init__(self, name=None, description=None, output_path=None, algorithm_id=None, algorithm_file=None, algorithm_func_name=None, evaluator_file=None, evaluator_func_name=None, evaluator_baseline=None, evaluator_baseline_func_name=None, evaluator_parameter=None):
        r"""EvolveTaskCreateReq

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 优化任务名称。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,64]。 **默认取值**： 不涉及 
        :type name: str
        :param description: **参数解释**： 优化任务描述。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,65536]。 **默认取值**： 不涉及 
        :type description: str
        :param output_path: **参数解释**： 优化结果存储路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,256]。 **默认取值**： 不涉及 
        :type output_path: str
        :param algorithm_id: **参数解释**： 关联的算法设计项目。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 
        :type algorithm_id: str
        :param algorithm_file: **参数解释**： 关联的算法文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,256]。 **默认取值**： 不涉及 
        :type algorithm_file: str
        :param algorithm_func_name: **参数解释**： 算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,256]。 **默认取值**： 不涉及 
        :type algorithm_func_name: str
        :param evaluator_file: **参数解释**： 评估器文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,65536]。 **默认取值**： 不涉及 
        :type evaluator_file: str
        :param evaluator_func_name: **参数解释**： 评估器算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 
        :type evaluator_func_name: str
        :param evaluator_baseline: **参数解释**： 评估基线文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,65536]。 **默认取值**： 不涉及 
        :type evaluator_baseline: str
        :param evaluator_baseline_func_name: **参数解释**： 评估基线算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 
        :type evaluator_baseline_func_name: str
        :param evaluator_parameter: 
        :type evaluator_parameter: :class:`huaweicloudsdkoptverse.v1.EvaluatorParameter`
        """
        
        

        self._name = None
        self._description = None
        self._output_path = None
        self._algorithm_id = None
        self._algorithm_file = None
        self._algorithm_func_name = None
        self._evaluator_file = None
        self._evaluator_func_name = None
        self._evaluator_baseline = None
        self._evaluator_baseline_func_name = None
        self._evaluator_parameter = None
        self.discriminator = None

        self.name = name
        self.description = description
        self.output_path = output_path
        self.algorithm_id = algorithm_id
        if algorithm_file is not None:
            self.algorithm_file = algorithm_file
        if algorithm_func_name is not None:
            self.algorithm_func_name = algorithm_func_name
        self.evaluator_file = evaluator_file
        self.evaluator_func_name = evaluator_func_name
        self.evaluator_baseline = evaluator_baseline
        self.evaluator_baseline_func_name = evaluator_baseline_func_name
        self.evaluator_parameter = evaluator_parameter

    @property
    def name(self):
        r"""Gets the name of this EvolveTaskCreateReq.

        **参数解释**： 优化任务名称。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,64]。 **默认取值**： 不涉及 

        :return: The name of this EvolveTaskCreateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EvolveTaskCreateReq.

        **参数解释**： 优化任务名称。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,64]。 **默认取值**： 不涉及 

        :param name: The name of this EvolveTaskCreateReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EvolveTaskCreateReq.

        **参数解释**： 优化任务描述。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,65536]。 **默认取值**： 不涉及 

        :return: The description of this EvolveTaskCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EvolveTaskCreateReq.

        **参数解释**： 优化任务描述。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,65536]。 **默认取值**： 不涉及 

        :param description: The description of this EvolveTaskCreateReq.
        :type description: str
        """
        self._description = description

    @property
    def output_path(self):
        r"""Gets the output_path of this EvolveTaskCreateReq.

        **参数解释**： 优化结果存储路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,256]。 **默认取值**： 不涉及 

        :return: The output_path of this EvolveTaskCreateReq.
        :rtype: str
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        r"""Sets the output_path of this EvolveTaskCreateReq.

        **参数解释**： 优化结果存储路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,256]。 **默认取值**： 不涉及 

        :param output_path: The output_path of this EvolveTaskCreateReq.
        :type output_path: str
        """
        self._output_path = output_path

    @property
    def algorithm_id(self):
        r"""Gets the algorithm_id of this EvolveTaskCreateReq.

        **参数解释**： 关联的算法设计项目。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :return: The algorithm_id of this EvolveTaskCreateReq.
        :rtype: str
        """
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, algorithm_id):
        r"""Sets the algorithm_id of this EvolveTaskCreateReq.

        **参数解释**： 关联的算法设计项目。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :param algorithm_id: The algorithm_id of this EvolveTaskCreateReq.
        :type algorithm_id: str
        """
        self._algorithm_id = algorithm_id

    @property
    def algorithm_file(self):
        r"""Gets the algorithm_file of this EvolveTaskCreateReq.

        **参数解释**： 关联的算法文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,256]。 **默认取值**： 不涉及 

        :return: The algorithm_file of this EvolveTaskCreateReq.
        :rtype: str
        """
        return self._algorithm_file

    @algorithm_file.setter
    def algorithm_file(self, algorithm_file):
        r"""Sets the algorithm_file of this EvolveTaskCreateReq.

        **参数解释**： 关联的算法文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,256]。 **默认取值**： 不涉及 

        :param algorithm_file: The algorithm_file of this EvolveTaskCreateReq.
        :type algorithm_file: str
        """
        self._algorithm_file = algorithm_file

    @property
    def algorithm_func_name(self):
        r"""Gets the algorithm_func_name of this EvolveTaskCreateReq.

        **参数解释**： 算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,256]。 **默认取值**： 不涉及 

        :return: The algorithm_func_name of this EvolveTaskCreateReq.
        :rtype: str
        """
        return self._algorithm_func_name

    @algorithm_func_name.setter
    def algorithm_func_name(self, algorithm_func_name):
        r"""Sets the algorithm_func_name of this EvolveTaskCreateReq.

        **参数解释**： 算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,256]。 **默认取值**： 不涉及 

        :param algorithm_func_name: The algorithm_func_name of this EvolveTaskCreateReq.
        :type algorithm_func_name: str
        """
        self._algorithm_func_name = algorithm_func_name

    @property
    def evaluator_file(self):
        r"""Gets the evaluator_file of this EvolveTaskCreateReq.

        **参数解释**： 评估器文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,65536]。 **默认取值**： 不涉及 

        :return: The evaluator_file of this EvolveTaskCreateReq.
        :rtype: str
        """
        return self._evaluator_file

    @evaluator_file.setter
    def evaluator_file(self, evaluator_file):
        r"""Sets the evaluator_file of this EvolveTaskCreateReq.

        **参数解释**： 评估器文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,65536]。 **默认取值**： 不涉及 

        :param evaluator_file: The evaluator_file of this EvolveTaskCreateReq.
        :type evaluator_file: str
        """
        self._evaluator_file = evaluator_file

    @property
    def evaluator_func_name(self):
        r"""Gets the evaluator_func_name of this EvolveTaskCreateReq.

        **参数解释**： 评估器算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :return: The evaluator_func_name of this EvolveTaskCreateReq.
        :rtype: str
        """
        return self._evaluator_func_name

    @evaluator_func_name.setter
    def evaluator_func_name(self, evaluator_func_name):
        r"""Sets the evaluator_func_name of this EvolveTaskCreateReq.

        **参数解释**： 评估器算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :param evaluator_func_name: The evaluator_func_name of this EvolveTaskCreateReq.
        :type evaluator_func_name: str
        """
        self._evaluator_func_name = evaluator_func_name

    @property
    def evaluator_baseline(self):
        r"""Gets the evaluator_baseline of this EvolveTaskCreateReq.

        **参数解释**： 评估基线文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,65536]。 **默认取值**： 不涉及 

        :return: The evaluator_baseline of this EvolveTaskCreateReq.
        :rtype: str
        """
        return self._evaluator_baseline

    @evaluator_baseline.setter
    def evaluator_baseline(self, evaluator_baseline):
        r"""Sets the evaluator_baseline of this EvolveTaskCreateReq.

        **参数解释**： 评估基线文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,65536]。 **默认取值**： 不涉及 

        :param evaluator_baseline: The evaluator_baseline of this EvolveTaskCreateReq.
        :type evaluator_baseline: str
        """
        self._evaluator_baseline = evaluator_baseline

    @property
    def evaluator_baseline_func_name(self):
        r"""Gets the evaluator_baseline_func_name of this EvolveTaskCreateReq.

        **参数解释**： 评估基线算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :return: The evaluator_baseline_func_name of this EvolveTaskCreateReq.
        :rtype: str
        """
        return self._evaluator_baseline_func_name

    @evaluator_baseline_func_name.setter
    def evaluator_baseline_func_name(self, evaluator_baseline_func_name):
        r"""Sets the evaluator_baseline_func_name of this EvolveTaskCreateReq.

        **参数解释**： 评估基线算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :param evaluator_baseline_func_name: The evaluator_baseline_func_name of this EvolveTaskCreateReq.
        :type evaluator_baseline_func_name: str
        """
        self._evaluator_baseline_func_name = evaluator_baseline_func_name

    @property
    def evaluator_parameter(self):
        r"""Gets the evaluator_parameter of this EvolveTaskCreateReq.

        :return: The evaluator_parameter of this EvolveTaskCreateReq.
        :rtype: :class:`huaweicloudsdkoptverse.v1.EvaluatorParameter`
        """
        return self._evaluator_parameter

    @evaluator_parameter.setter
    def evaluator_parameter(self, evaluator_parameter):
        r"""Sets the evaluator_parameter of this EvolveTaskCreateReq.

        :param evaluator_parameter: The evaluator_parameter of this EvolveTaskCreateReq.
        :type evaluator_parameter: :class:`huaweicloudsdkoptverse.v1.EvaluatorParameter`
        """
        self._evaluator_parameter = evaluator_parameter

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
        if not isinstance(other, EvolveTaskCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
