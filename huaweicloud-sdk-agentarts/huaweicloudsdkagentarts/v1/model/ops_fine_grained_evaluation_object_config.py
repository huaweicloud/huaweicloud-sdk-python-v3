# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsFineGrainedEvaluationObjectConfig:

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
        'type': 'str',
        'name': 'str',
        'version': 'str',
        'inputs_mapping': 'OpsFineGrainedEvaluationObjectConfigInputsMapping'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name',
        'version': 'version',
        'inputs_mapping': 'inputs_mapping'
    }

    def __init__(self, id=None, type=None, name=None, version=None, inputs_mapping=None):
        r"""OpsFineGrainedEvaluationObjectConfig

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 评估对象的唯一标识符。 **约束限制：** 字符长度1到36。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。
        :type id: str
        :param type: **参数解释：** 评估对象的类型。 **约束限制：** 必须为枚举值之一。 **取值范围：** WORKFLOW, AGENT, MULTI_AGENT。 **默认取值：** 不涉及。
        :type type: str
        :param name: **参数解释：** 评估对象的名称。 **约束限制：** 字符长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param version: **参数解释：** 评估对象的版本号。 **约束限制：** 字符长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type version: str
        :param inputs_mapping: 
        :type inputs_mapping: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationObjectConfigInputsMapping`
        """
        
        

        self._id = None
        self._type = None
        self._name = None
        self._version = None
        self._inputs_mapping = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.name = name
        self.version = version
        if inputs_mapping is not None:
            self.inputs_mapping = inputs_mapping

    @property
    def id(self):
        r"""Gets the id of this OpsFineGrainedEvaluationObjectConfig.

        **参数解释：** 评估对象的唯一标识符。 **约束限制：** 字符长度1到36。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。

        :return: The id of this OpsFineGrainedEvaluationObjectConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsFineGrainedEvaluationObjectConfig.

        **参数解释：** 评估对象的唯一标识符。 **约束限制：** 字符长度1到36。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。

        :param id: The id of this OpsFineGrainedEvaluationObjectConfig.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this OpsFineGrainedEvaluationObjectConfig.

        **参数解释：** 评估对象的类型。 **约束限制：** 必须为枚举值之一。 **取值范围：** WORKFLOW, AGENT, MULTI_AGENT。 **默认取值：** 不涉及。

        :return: The type of this OpsFineGrainedEvaluationObjectConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsFineGrainedEvaluationObjectConfig.

        **参数解释：** 评估对象的类型。 **约束限制：** 必须为枚举值之一。 **取值范围：** WORKFLOW, AGENT, MULTI_AGENT。 **默认取值：** 不涉及。

        :param type: The type of this OpsFineGrainedEvaluationObjectConfig.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this OpsFineGrainedEvaluationObjectConfig.

        **参数解释：** 评估对象的名称。 **约束限制：** 字符长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this OpsFineGrainedEvaluationObjectConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpsFineGrainedEvaluationObjectConfig.

        **参数解释：** 评估对象的名称。 **约束限制：** 字符长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this OpsFineGrainedEvaluationObjectConfig.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this OpsFineGrainedEvaluationObjectConfig.

        **参数解释：** 评估对象的版本号。 **约束限制：** 字符长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The version of this OpsFineGrainedEvaluationObjectConfig.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this OpsFineGrainedEvaluationObjectConfig.

        **参数解释：** 评估对象的版本号。 **约束限制：** 字符长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param version: The version of this OpsFineGrainedEvaluationObjectConfig.
        :type version: str
        """
        self._version = version

    @property
    def inputs_mapping(self):
        r"""Gets the inputs_mapping of this OpsFineGrainedEvaluationObjectConfig.

        :return: The inputs_mapping of this OpsFineGrainedEvaluationObjectConfig.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationObjectConfigInputsMapping`
        """
        return self._inputs_mapping

    @inputs_mapping.setter
    def inputs_mapping(self, inputs_mapping):
        r"""Sets the inputs_mapping of this OpsFineGrainedEvaluationObjectConfig.

        :param inputs_mapping: The inputs_mapping of this OpsFineGrainedEvaluationObjectConfig.
        :type inputs_mapping: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationObjectConfigInputsMapping`
        """
        self._inputs_mapping = inputs_mapping

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
        if not isinstance(other, OpsFineGrainedEvaluationObjectConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
