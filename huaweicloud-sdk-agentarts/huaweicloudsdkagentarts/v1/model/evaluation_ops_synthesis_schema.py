# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsSynthesisSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'synthesis_requirement': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'synthesis_requirement': 'synthesis_requirement'
    }

    def __init__(self, id=None, name=None, description=None, synthesis_requirement=None):
        r"""EvaluationOpsSynthesisSchema

        The model defined in huaweicloud sdk

        :param id: **参数解释：**   合成字段的id。 **取值范围：**   由字母、数字、下划线组成。
        :type id: str
        :param name: **参数解释：**   合成字段的名称。 **取值范围：**   长度1-100字符，由字母、数字、下划线组成。
        :type name: str
        :param description: **参数解释：**   合成字段的业务含义描述。 **取值范围：**   任意字符串。
        :type description: str
        :param synthesis_requirement: **参数解释：**   合成要求，用于指导LLM生成该字段的思考路径。 **取值范围：**   0-4000字符，详细的指令说明。
        :type synthesis_requirement: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._synthesis_requirement = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if synthesis_requirement is not None:
            self.synthesis_requirement = synthesis_requirement

    @property
    def id(self):
        r"""Gets the id of this EvaluationOpsSynthesisSchema.

        **参数解释：**   合成字段的id。 **取值范围：**   由字母、数字、下划线组成。

        :return: The id of this EvaluationOpsSynthesisSchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EvaluationOpsSynthesisSchema.

        **参数解释：**   合成字段的id。 **取值范围：**   由字母、数字、下划线组成。

        :param id: The id of this EvaluationOpsSynthesisSchema.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EvaluationOpsSynthesisSchema.

        **参数解释：**   合成字段的名称。 **取值范围：**   长度1-100字符，由字母、数字、下划线组成。

        :return: The name of this EvaluationOpsSynthesisSchema.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EvaluationOpsSynthesisSchema.

        **参数解释：**   合成字段的名称。 **取值范围：**   长度1-100字符，由字母、数字、下划线组成。

        :param name: The name of this EvaluationOpsSynthesisSchema.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EvaluationOpsSynthesisSchema.

        **参数解释：**   合成字段的业务含义描述。 **取值范围：**   任意字符串。

        :return: The description of this EvaluationOpsSynthesisSchema.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EvaluationOpsSynthesisSchema.

        **参数解释：**   合成字段的业务含义描述。 **取值范围：**   任意字符串。

        :param description: The description of this EvaluationOpsSynthesisSchema.
        :type description: str
        """
        self._description = description

    @property
    def synthesis_requirement(self):
        r"""Gets the synthesis_requirement of this EvaluationOpsSynthesisSchema.

        **参数解释：**   合成要求，用于指导LLM生成该字段的思考路径。 **取值范围：**   0-4000字符，详细的指令说明。

        :return: The synthesis_requirement of this EvaluationOpsSynthesisSchema.
        :rtype: str
        """
        return self._synthesis_requirement

    @synthesis_requirement.setter
    def synthesis_requirement(self, synthesis_requirement):
        r"""Sets the synthesis_requirement of this EvaluationOpsSynthesisSchema.

        **参数解释：**   合成要求，用于指导LLM生成该字段的思考路径。 **取值范围：**   0-4000字符，详细的指令说明。

        :param synthesis_requirement: The synthesis_requirement of this EvaluationOpsSynthesisSchema.
        :type synthesis_requirement: str
        """
        self._synthesis_requirement = synthesis_requirement

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
        if not isinstance(other, EvaluationOpsSynthesisSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
