# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorTemplateResponseBodyTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_info': 'OpsEvaluatorBaseInfo',
        'description': 'str',
        'evaluator_content': 'ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent',
        'evaluator_info': 'ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo',
        'evaluator_type': 'int',
        'name': 'str',
        'popularity': 'str',
        'tags': 'ShowOpsEvaluatorTemplateResponseBodyTemplateTags',
        'template_id': 'str'
    }

    attribute_map = {
        'base_info': 'base_info',
        'description': 'description',
        'evaluator_content': 'evaluator_content',
        'evaluator_info': 'evaluator_info',
        'evaluator_type': 'evaluator_type',
        'name': 'name',
        'popularity': 'popularity',
        'tags': 'tags',
        'template_id': 'template_id'
    }

    def __init__(self, base_info=None, description=None, evaluator_content=None, evaluator_info=None, evaluator_type=None, name=None, popularity=None, tags=None, template_id=None):
        r"""ShowOpsEvaluatorTemplateResponseBodyTemplate

        The model defined in huaweicloud sdk

        :param base_info: 
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        :param description: **参数解释：** 描述用于详细说明评估器的功能、用途和应用场景。 **取值范围：** 描述性字符串。 
        :type description: str
        :param evaluator_content: 
        :type evaluator_content: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent`
        :param evaluator_info: 
        :type evaluator_info: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo`
        :param evaluator_type: **参数解释：** 评估器的分类类型。 **取值范围：** 不涉及。 
        :type evaluator_type: int
        :param name: **参数解释：** 评估器的名字。 **取值范围：** 不涉及。 
        :type name: str
        :param popularity: **参数解释：** 受欢迎程度分值。 **取值范围：** 字符串形式的数字。 
        :type popularity: str
        :param tags: 
        :type tags: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateTags`
        :param template_id: **参数解释：** 评估器模板的唯一ID。 **取值范围：** 不涉及。 
        :type template_id: str
        """
        
        

        self._base_info = None
        self._description = None
        self._evaluator_content = None
        self._evaluator_info = None
        self._evaluator_type = None
        self._name = None
        self._popularity = None
        self._tags = None
        self._template_id = None
        self.discriminator = None

        self.base_info = base_info
        self.description = description
        self.evaluator_content = evaluator_content
        if evaluator_info is not None:
            self.evaluator_info = evaluator_info
        if evaluator_type is not None:
            self.evaluator_type = evaluator_type
        self.name = name
        self.popularity = popularity
        self.tags = tags
        self.template_id = template_id

    @property
    def base_info(self):
        r"""Gets the base_info of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        :return: The base_info of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        :param base_info: The base_info of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        """
        self._base_info = base_info

    @property
    def description(self):
        r"""Gets the description of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        **参数解释：** 描述用于详细说明评估器的功能、用途和应用场景。 **取值范围：** 描述性字符串。 

        :return: The description of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        **参数解释：** 描述用于详细说明评估器的功能、用途和应用场景。 **取值范围：** 描述性字符串。 

        :param description: The description of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :type description: str
        """
        self._description = description

    @property
    def evaluator_content(self):
        r"""Gets the evaluator_content of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        :return: The evaluator_content of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent`
        """
        return self._evaluator_content

    @evaluator_content.setter
    def evaluator_content(self, evaluator_content):
        r"""Sets the evaluator_content of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        :param evaluator_content: The evaluator_content of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :type evaluator_content: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent`
        """
        self._evaluator_content = evaluator_content

    @property
    def evaluator_info(self):
        r"""Gets the evaluator_info of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        :return: The evaluator_info of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo`
        """
        return self._evaluator_info

    @evaluator_info.setter
    def evaluator_info(self, evaluator_info):
        r"""Sets the evaluator_info of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        :param evaluator_info: The evaluator_info of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :type evaluator_info: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorInfo`
        """
        self._evaluator_info = evaluator_info

    @property
    def evaluator_type(self):
        r"""Gets the evaluator_type of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        **参数解释：** 评估器的分类类型。 **取值范围：** 不涉及。 

        :return: The evaluator_type of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :rtype: int
        """
        return self._evaluator_type

    @evaluator_type.setter
    def evaluator_type(self, evaluator_type):
        r"""Sets the evaluator_type of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        **参数解释：** 评估器的分类类型。 **取值范围：** 不涉及。 

        :param evaluator_type: The evaluator_type of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :type evaluator_type: int
        """
        self._evaluator_type = evaluator_type

    @property
    def name(self):
        r"""Gets the name of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        **参数解释：** 评估器的名字。 **取值范围：** 不涉及。 

        :return: The name of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        **参数解释：** 评估器的名字。 **取值范围：** 不涉及。 

        :param name: The name of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :type name: str
        """
        self._name = name

    @property
    def popularity(self):
        r"""Gets the popularity of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        **参数解释：** 受欢迎程度分值。 **取值范围：** 字符串形式的数字。 

        :return: The popularity of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :rtype: str
        """
        return self._popularity

    @popularity.setter
    def popularity(self, popularity):
        r"""Sets the popularity of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        **参数解释：** 受欢迎程度分值。 **取值范围：** 字符串形式的数字。 

        :param popularity: The popularity of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :type popularity: str
        """
        self._popularity = popularity

    @property
    def tags(self):
        r"""Gets the tags of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        :return: The tags of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateTags`
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        :param tags: The tags of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :type tags: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateTags`
        """
        self._tags = tags

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        **参数解释：** 评估器模板的唯一ID。 **取值范围：** 不涉及。 

        :return: The template_id of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowOpsEvaluatorTemplateResponseBodyTemplate.

        **参数解释：** 评估器模板的唯一ID。 **取值范围：** 不涉及。 

        :param template_id: The template_id of this ShowOpsEvaluatorTemplateResponseBodyTemplate.
        :type template_id: str
        """
        self._template_id = template_id

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
        if not isinstance(other, ShowOpsEvaluatorTemplateResponseBodyTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
