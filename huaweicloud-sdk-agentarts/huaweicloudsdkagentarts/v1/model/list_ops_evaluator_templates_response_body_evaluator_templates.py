# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_type': 'int',
        'template_id': 'str',
        'popularity': 'str',
        'base_info': 'OpsEvaluatorBaseInfo',
        'description': 'str',
        'evaluator_info': 'ListOpsEvaluatorTemplatesResponseBodyEvaluatorInfo',
        'evaluator_content': 'ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent',
        'name': 'str',
        'tags': 'ListOpsEvaluatorTemplatesResponseBodyTags'
    }

    attribute_map = {
        'evaluator_type': 'evaluator_type',
        'template_id': 'template_id',
        'popularity': 'popularity',
        'base_info': 'base_info',
        'description': 'description',
        'evaluator_info': 'evaluator_info',
        'evaluator_content': 'evaluator_content',
        'name': 'name',
        'tags': 'tags'
    }

    def __init__(self, evaluator_type=None, template_id=None, popularity=None, base_info=None, description=None, evaluator_info=None, evaluator_content=None, name=None, tags=None):
        r"""ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates

        The model defined in huaweicloud sdk

        :param evaluator_type: **参数解释：** 评估器类型标识。 **取值范围：** 0到2,147,483,647。 
        :type evaluator_type: int
        :param template_id: **参数解释：** 评估器模板的唯一ID。 **取值范围：** 由系统生成的数字字符串。 
        :type template_id: str
        :param popularity: **参数解释：** 流行度表示评估器在用户中的受欢迎程度和使用频率。 **取值范围：** 数字形式的字符串。 
        :type popularity: str
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        :param description: **参数解释：** 评估器描述用于说明评估器的功能、用途和使用场景。 **取值范围：** 描述性文本。 
        :type description: str
        :param evaluator_info: 
        :type evaluator_info: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorInfo`
        :param evaluator_content: 
        :type evaluator_content: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent`
        :param name: **参数解释：** 评估器显示名称。 **取值范围：** 不涉及。 
        :type name: str
        :param tags: 
        :type tags: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyTags`
        """
        
        

        self._evaluator_type = None
        self._template_id = None
        self._popularity = None
        self._base_info = None
        self._description = None
        self._evaluator_info = None
        self._evaluator_content = None
        self._name = None
        self._tags = None
        self.discriminator = None

        self.evaluator_type = evaluator_type
        self.template_id = template_id
        self.popularity = popularity
        self.base_info = base_info
        self.description = description
        self.evaluator_info = evaluator_info
        self.evaluator_content = evaluator_content
        self.name = name
        self.tags = tags

    @property
    def evaluator_type(self):
        r"""Gets the evaluator_type of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        **参数解释：** 评估器类型标识。 **取值范围：** 0到2,147,483,647。 

        :return: The evaluator_type of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :rtype: int
        """
        return self._evaluator_type

    @evaluator_type.setter
    def evaluator_type(self, evaluator_type):
        r"""Sets the evaluator_type of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        **参数解释：** 评估器类型标识。 **取值范围：** 0到2,147,483,647。 

        :param evaluator_type: The evaluator_type of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :type evaluator_type: int
        """
        self._evaluator_type = evaluator_type

    @property
    def template_id(self):
        r"""Gets the template_id of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        **参数解释：** 评估器模板的唯一ID。 **取值范围：** 由系统生成的数字字符串。 

        :return: The template_id of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        **参数解释：** 评估器模板的唯一ID。 **取值范围：** 由系统生成的数字字符串。 

        :param template_id: The template_id of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def popularity(self):
        r"""Gets the popularity of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        **参数解释：** 流行度表示评估器在用户中的受欢迎程度和使用频率。 **取值范围：** 数字形式的字符串。 

        :return: The popularity of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :rtype: str
        """
        return self._popularity

    @popularity.setter
    def popularity(self, popularity):
        r"""Sets the popularity of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        **参数解释：** 流行度表示评估器在用户中的受欢迎程度和使用频率。 **取值范围：** 数字形式的字符串。 

        :param popularity: The popularity of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :type popularity: str
        """
        self._popularity = popularity

    @property
    def base_info(self):
        r"""Gets the base_info of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        :return: The base_info of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        :param base_info: The base_info of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        """
        self._base_info = base_info

    @property
    def description(self):
        r"""Gets the description of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        **参数解释：** 评估器描述用于说明评估器的功能、用途和使用场景。 **取值范围：** 描述性文本。 

        :return: The description of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        **参数解释：** 评估器描述用于说明评估器的功能、用途和使用场景。 **取值范围：** 描述性文本。 

        :param description: The description of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :type description: str
        """
        self._description = description

    @property
    def evaluator_info(self):
        r"""Gets the evaluator_info of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        :return: The evaluator_info of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorInfo`
        """
        return self._evaluator_info

    @evaluator_info.setter
    def evaluator_info(self, evaluator_info):
        r"""Sets the evaluator_info of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        :param evaluator_info: The evaluator_info of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :type evaluator_info: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorInfo`
        """
        self._evaluator_info = evaluator_info

    @property
    def evaluator_content(self):
        r"""Gets the evaluator_content of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        :return: The evaluator_content of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent`
        """
        return self._evaluator_content

    @evaluator_content.setter
    def evaluator_content(self, evaluator_content):
        r"""Sets the evaluator_content of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        :param evaluator_content: The evaluator_content of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :type evaluator_content: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent`
        """
        self._evaluator_content = evaluator_content

    @property
    def name(self):
        r"""Gets the name of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        **参数解释：** 评估器显示名称。 **取值范围：** 不涉及。 

        :return: The name of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        **参数解释：** 评估器显示名称。 **取值范围：** 不涉及。 

        :param name: The name of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        r"""Gets the tags of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        :return: The tags of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyTags`
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.

        :param tags: The tags of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates.
        :type tags: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyTags`
        """
        self._tags = tags

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
        if not isinstance(other, ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
