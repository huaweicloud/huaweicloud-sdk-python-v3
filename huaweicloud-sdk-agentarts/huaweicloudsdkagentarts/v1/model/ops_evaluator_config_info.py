# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsEvaluatorConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_id': 'str',
        'evaluator_version': 'str',
        'evaluator_name': 'str',
        'evaluator_variable_mapping': 'dict(str, OpsEvaluatorVariableMapping)'
    }

    attribute_map = {
        'evaluator_id': 'evaluator_id',
        'evaluator_version': 'evaluator_version',
        'evaluator_name': 'evaluator_name',
        'evaluator_variable_mapping': 'evaluator_variable_mapping'
    }

    def __init__(self, evaluator_id=None, evaluator_version=None, evaluator_name=None, evaluator_variable_mapping=None):
        r"""OpsEvaluatorConfigInfo

        The model defined in huaweicloud sdk

        :param evaluator_id: **参数解释：** 评估器的唯一标识符。 **约束限制：** 1到36字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type evaluator_id: str
        :param evaluator_version: **参数解释：** 评估器的版本号。 **约束限制：** 1到36字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type evaluator_version: str
        :param evaluator_name: **参数解释：** 评估器的显示名称。 **约束限制：** 1到100字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type evaluator_name: str
        :param evaluator_variable_mapping: **参数解释：** 变量映射字典配置。 **约束限制：** 符合 Map 结构的 JSON。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type evaluator_variable_mapping: dict(str, OpsEvaluatorVariableMapping)
        """
        
        

        self._evaluator_id = None
        self._evaluator_version = None
        self._evaluator_name = None
        self._evaluator_variable_mapping = None
        self.discriminator = None

        self.evaluator_id = evaluator_id
        self.evaluator_version = evaluator_version
        self.evaluator_name = evaluator_name
        self.evaluator_variable_mapping = evaluator_variable_mapping

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this OpsEvaluatorConfigInfo.

        **参数解释：** 评估器的唯一标识符。 **约束限制：** 1到36字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The evaluator_id of this OpsEvaluatorConfigInfo.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this OpsEvaluatorConfigInfo.

        **参数解释：** 评估器的唯一标识符。 **约束限制：** 1到36字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param evaluator_id: The evaluator_id of this OpsEvaluatorConfigInfo.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def evaluator_version(self):
        r"""Gets the evaluator_version of this OpsEvaluatorConfigInfo.

        **参数解释：** 评估器的版本号。 **约束限制：** 1到36字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The evaluator_version of this OpsEvaluatorConfigInfo.
        :rtype: str
        """
        return self._evaluator_version

    @evaluator_version.setter
    def evaluator_version(self, evaluator_version):
        r"""Sets the evaluator_version of this OpsEvaluatorConfigInfo.

        **参数解释：** 评估器的版本号。 **约束限制：** 1到36字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param evaluator_version: The evaluator_version of this OpsEvaluatorConfigInfo.
        :type evaluator_version: str
        """
        self._evaluator_version = evaluator_version

    @property
    def evaluator_name(self):
        r"""Gets the evaluator_name of this OpsEvaluatorConfigInfo.

        **参数解释：** 评估器的显示名称。 **约束限制：** 1到100字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The evaluator_name of this OpsEvaluatorConfigInfo.
        :rtype: str
        """
        return self._evaluator_name

    @evaluator_name.setter
    def evaluator_name(self, evaluator_name):
        r"""Sets the evaluator_name of this OpsEvaluatorConfigInfo.

        **参数解释：** 评估器的显示名称。 **约束限制：** 1到100字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param evaluator_name: The evaluator_name of this OpsEvaluatorConfigInfo.
        :type evaluator_name: str
        """
        self._evaluator_name = evaluator_name

    @property
    def evaluator_variable_mapping(self):
        r"""Gets the evaluator_variable_mapping of this OpsEvaluatorConfigInfo.

        **参数解释：** 变量映射字典配置。 **约束限制：** 符合 Map 结构的 JSON。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The evaluator_variable_mapping of this OpsEvaluatorConfigInfo.
        :rtype: dict(str, OpsEvaluatorVariableMapping)
        """
        return self._evaluator_variable_mapping

    @evaluator_variable_mapping.setter
    def evaluator_variable_mapping(self, evaluator_variable_mapping):
        r"""Sets the evaluator_variable_mapping of this OpsEvaluatorConfigInfo.

        **参数解释：** 变量映射字典配置。 **约束限制：** 符合 Map 结构的 JSON。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param evaluator_variable_mapping: The evaluator_variable_mapping of this OpsEvaluatorConfigInfo.
        :type evaluator_variable_mapping: dict(str, OpsEvaluatorVariableMapping)
        """
        self._evaluator_variable_mapping = evaluator_variable_mapping

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
        if not isinstance(other, OpsEvaluatorConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
