# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsCurrentVersion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'evaluator_content': 'object',
        'version': 'str'
    }

    attribute_map = {
        'description': 'description',
        'evaluator_content': 'evaluator_content',
        'version': 'version'
    }

    def __init__(self, description=None, evaluator_content=None, version=None):
        r"""EvaluationOpsCurrentVersion

        The model defined in huaweicloud sdk

        :param description: **参数解释：** 当前版本的详细描述信息。 **约束限制：** 长度为0到10000个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type description: str
        :param evaluator_content: **参数解释：** 评估器的核心配置JSON内容，包含评估逻辑、评分规则等配置项。 **约束限制：** 符合评估器配置JSON结构定义。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type evaluator_content: object
        :param version: **参数解释：** 评估器的版本标识符。 **约束限制：** 0到10000字符。 **取值范围：** 符合语义化版本格式的字符串，如\&quot;v1.0.0\&quot;。 **默认取值：** 不涉及。 
        :type version: str
        """
        
        

        self._description = None
        self._evaluator_content = None
        self._version = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if evaluator_content is not None:
            self.evaluator_content = evaluator_content
        if version is not None:
            self.version = version

    @property
    def description(self):
        r"""Gets the description of this EvaluationOpsCurrentVersion.

        **参数解释：** 当前版本的详细描述信息。 **约束限制：** 长度为0到10000个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The description of this EvaluationOpsCurrentVersion.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EvaluationOpsCurrentVersion.

        **参数解释：** 当前版本的详细描述信息。 **约束限制：** 长度为0到10000个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param description: The description of this EvaluationOpsCurrentVersion.
        :type description: str
        """
        self._description = description

    @property
    def evaluator_content(self):
        r"""Gets the evaluator_content of this EvaluationOpsCurrentVersion.

        **参数解释：** 评估器的核心配置JSON内容，包含评估逻辑、评分规则等配置项。 **约束限制：** 符合评估器配置JSON结构定义。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The evaluator_content of this EvaluationOpsCurrentVersion.
        :rtype: object
        """
        return self._evaluator_content

    @evaluator_content.setter
    def evaluator_content(self, evaluator_content):
        r"""Sets the evaluator_content of this EvaluationOpsCurrentVersion.

        **参数解释：** 评估器的核心配置JSON内容，包含评估逻辑、评分规则等配置项。 **约束限制：** 符合评估器配置JSON结构定义。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param evaluator_content: The evaluator_content of this EvaluationOpsCurrentVersion.
        :type evaluator_content: object
        """
        self._evaluator_content = evaluator_content

    @property
    def version(self):
        r"""Gets the version of this EvaluationOpsCurrentVersion.

        **参数解释：** 评估器的版本标识符。 **约束限制：** 0到10000字符。 **取值范围：** 符合语义化版本格式的字符串，如\"v1.0.0\"。 **默认取值：** 不涉及。 

        :return: The version of this EvaluationOpsCurrentVersion.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this EvaluationOpsCurrentVersion.

        **参数解释：** 评估器的版本标识符。 **约束限制：** 0到10000字符。 **取值范围：** 符合语义化版本格式的字符串，如\"v1.0.0\"。 **默认取值：** 不涉及。 

        :param version: The version of this EvaluationOpsCurrentVersion.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, EvaluationOpsCurrentVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
