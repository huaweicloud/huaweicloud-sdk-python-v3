# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineByTemplateDTO:

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
        'is_publish': 'bool',
        'sources': 'list[CodeSource]',
        'security_level': 'int',
        'confidentiality_code': 'str',
        'variables': 'list[PipelineByTemplateDTOVariables]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'is_publish': 'is_publish',
        'sources': 'sources',
        'security_level': 'security_level',
        'confidentiality_code': 'confidentiality_code',
        'variables': 'variables'
    }

    def __init__(self, name=None, description=None, is_publish=None, sources=None, security_level=None, confidentiality_code=None, variables=None):
        r"""PipelineByTemplateDTO

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 流水线名称。 **约束限制**： 不涉及。 **取值范围**： 仅包含中文、大小写英文字母、数字、&#39;-&#39;和&#39;_&#39;，且长度为[1,128]个字符。 **默认取值**： 不涉及。 
        :type name: str
        :param description: **参数解释**： 流水线描述。 **约束限制**： 不涉及。 **取值范围**： 不超过1024字符。 **默认取值**： 不涉及。 
        :type description: str
        :param is_publish: **参数解释**： 是否为变更流水线。 **约束限制**： 不涉及。 **取值范围**： - true：是变更流水线。 - false：不是变更流水线。 **默认取值**： 不涉及。 
        :type is_publish: bool
        :param sources: **参数解释**： 流水线源列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        :param security_level: **参数解释**： 流水线涉密等级，非涉密场景不涉及，涉密场景必填。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type security_level: int
        :param confidentiality_code: **参数解释**： 流水线涉密等级编码，非涉密场景不涉及。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type confidentiality_code: str
        :param variables: **参数解释**： 流水线参数列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineByTemplateDTOVariables`]
        """
        
        

        self._name = None
        self._description = None
        self._is_publish = None
        self._sources = None
        self._security_level = None
        self._confidentiality_code = None
        self._variables = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.is_publish = is_publish
        self.sources = sources
        if security_level is not None:
            self.security_level = security_level
        if confidentiality_code is not None:
            self.confidentiality_code = confidentiality_code
        if variables is not None:
            self.variables = variables

    @property
    def name(self):
        r"""Gets the name of this PipelineByTemplateDTO.

        **参数解释**： 流水线名称。 **约束限制**： 不涉及。 **取值范围**： 仅包含中文、大小写英文字母、数字、'-'和'_'，且长度为[1,128]个字符。 **默认取值**： 不涉及。 

        :return: The name of this PipelineByTemplateDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PipelineByTemplateDTO.

        **参数解释**： 流水线名称。 **约束限制**： 不涉及。 **取值范围**： 仅包含中文、大小写英文字母、数字、'-'和'_'，且长度为[1,128]个字符。 **默认取值**： 不涉及。 

        :param name: The name of this PipelineByTemplateDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this PipelineByTemplateDTO.

        **参数解释**： 流水线描述。 **约束限制**： 不涉及。 **取值范围**： 不超过1024字符。 **默认取值**： 不涉及。 

        :return: The description of this PipelineByTemplateDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PipelineByTemplateDTO.

        **参数解释**： 流水线描述。 **约束限制**： 不涉及。 **取值范围**： 不超过1024字符。 **默认取值**： 不涉及。 

        :param description: The description of this PipelineByTemplateDTO.
        :type description: str
        """
        self._description = description

    @property
    def is_publish(self):
        r"""Gets the is_publish of this PipelineByTemplateDTO.

        **参数解释**： 是否为变更流水线。 **约束限制**： 不涉及。 **取值范围**： - true：是变更流水线。 - false：不是变更流水线。 **默认取值**： 不涉及。 

        :return: The is_publish of this PipelineByTemplateDTO.
        :rtype: bool
        """
        return self._is_publish

    @is_publish.setter
    def is_publish(self, is_publish):
        r"""Sets the is_publish of this PipelineByTemplateDTO.

        **参数解释**： 是否为变更流水线。 **约束限制**： 不涉及。 **取值范围**： - true：是变更流水线。 - false：不是变更流水线。 **默认取值**： 不涉及。 

        :param is_publish: The is_publish of this PipelineByTemplateDTO.
        :type is_publish: bool
        """
        self._is_publish = is_publish

    @property
    def sources(self):
        r"""Gets the sources of this PipelineByTemplateDTO.

        **参数解释**： 流水线源列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The sources of this PipelineByTemplateDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this PipelineByTemplateDTO.

        **参数解释**： 流水线源列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param sources: The sources of this PipelineByTemplateDTO.
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        """
        self._sources = sources

    @property
    def security_level(self):
        r"""Gets the security_level of this PipelineByTemplateDTO.

        **参数解释**： 流水线涉密等级，非涉密场景不涉及，涉密场景必填。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The security_level of this PipelineByTemplateDTO.
        :rtype: int
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this PipelineByTemplateDTO.

        **参数解释**： 流水线涉密等级，非涉密场景不涉及，涉密场景必填。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param security_level: The security_level of this PipelineByTemplateDTO.
        :type security_level: int
        """
        self._security_level = security_level

    @property
    def confidentiality_code(self):
        r"""Gets the confidentiality_code of this PipelineByTemplateDTO.

        **参数解释**： 流水线涉密等级编码，非涉密场景不涉及。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The confidentiality_code of this PipelineByTemplateDTO.
        :rtype: str
        """
        return self._confidentiality_code

    @confidentiality_code.setter
    def confidentiality_code(self, confidentiality_code):
        r"""Sets the confidentiality_code of this PipelineByTemplateDTO.

        **参数解释**： 流水线涉密等级编码，非涉密场景不涉及。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param confidentiality_code: The confidentiality_code of this PipelineByTemplateDTO.
        :type confidentiality_code: str
        """
        self._confidentiality_code = confidentiality_code

    @property
    def variables(self):
        r"""Gets the variables of this PipelineByTemplateDTO.

        **参数解释**： 流水线参数列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The variables of this PipelineByTemplateDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineByTemplateDTOVariables`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this PipelineByTemplateDTO.

        **参数解释**： 流水线参数列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param variables: The variables of this PipelineByTemplateDTO.
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineByTemplateDTOVariables`]
        """
        self._variables = variables

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PipelineByTemplateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
