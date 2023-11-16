# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineTemplateDTO:

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
        'language': 'str',
        'variables': 'CustomVariable',
        'definition': 'str',
        'is_system': 'bool',
        'domain_id': 'str',
        'is_show_source': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'language': 'language',
        'variables': 'variables',
        'definition': 'definition',
        'is_system': 'is_system',
        'domain_id': 'domain_id',
        'is_show_source': 'is_show_source'
    }

    def __init__(self, name=None, description=None, language=None, variables=None, definition=None, is_system=None, domain_id=None, is_show_source=None):
        """PipelineTemplateDTO

        The model defined in huaweicloud sdk

        :param name: 模板名称
        :type name: str
        :param description: 模板描述
        :type description: str
        :param language: 模板语言
        :type language: str
        :param variables: 
        :type variables: :class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`
        :param definition: 模板编排json，包含stages
        :type definition: str
        :param is_system: 是否系统模板
        :type is_system: bool
        :param domain_id: 所属租户ID
        :type domain_id: str
        :param is_show_source: 是否显示流水线源
        :type is_show_source: bool
        """
        
        

        self._name = None
        self._description = None
        self._language = None
        self._variables = None
        self._definition = None
        self._is_system = None
        self._domain_id = None
        self._is_show_source = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.language = language
        if variables is not None:
            self.variables = variables
        self.definition = definition
        self.is_system = is_system
        self.domain_id = domain_id
        self.is_show_source = is_show_source

    @property
    def name(self):
        """Gets the name of this PipelineTemplateDTO.

        模板名称

        :return: The name of this PipelineTemplateDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineTemplateDTO.

        模板名称

        :param name: The name of this PipelineTemplateDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PipelineTemplateDTO.

        模板描述

        :return: The description of this PipelineTemplateDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PipelineTemplateDTO.

        模板描述

        :param description: The description of this PipelineTemplateDTO.
        :type description: str
        """
        self._description = description

    @property
    def language(self):
        """Gets the language of this PipelineTemplateDTO.

        模板语言

        :return: The language of this PipelineTemplateDTO.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PipelineTemplateDTO.

        模板语言

        :param language: The language of this PipelineTemplateDTO.
        :type language: str
        """
        self._language = language

    @property
    def variables(self):
        """Gets the variables of this PipelineTemplateDTO.

        :return: The variables of this PipelineTemplateDTO.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this PipelineTemplateDTO.

        :param variables: The variables of this PipelineTemplateDTO.
        :type variables: :class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`
        """
        self._variables = variables

    @property
    def definition(self):
        """Gets the definition of this PipelineTemplateDTO.

        模板编排json，包含stages

        :return: The definition of this PipelineTemplateDTO.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this PipelineTemplateDTO.

        模板编排json，包含stages

        :param definition: The definition of this PipelineTemplateDTO.
        :type definition: str
        """
        self._definition = definition

    @property
    def is_system(self):
        """Gets the is_system of this PipelineTemplateDTO.

        是否系统模板

        :return: The is_system of this PipelineTemplateDTO.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """Sets the is_system of this PipelineTemplateDTO.

        是否系统模板

        :param is_system: The is_system of this PipelineTemplateDTO.
        :type is_system: bool
        """
        self._is_system = is_system

    @property
    def domain_id(self):
        """Gets the domain_id of this PipelineTemplateDTO.

        所属租户ID

        :return: The domain_id of this PipelineTemplateDTO.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this PipelineTemplateDTO.

        所属租户ID

        :param domain_id: The domain_id of this PipelineTemplateDTO.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def is_show_source(self):
        """Gets the is_show_source of this PipelineTemplateDTO.

        是否显示流水线源

        :return: The is_show_source of this PipelineTemplateDTO.
        :rtype: bool
        """
        return self._is_show_source

    @is_show_source.setter
    def is_show_source(self, is_show_source):
        """Sets the is_show_source of this PipelineTemplateDTO.

        是否显示流水线源

        :param is_show_source: The is_show_source of this PipelineTemplateDTO.
        :type is_show_source: bool
        """
        self._is_show_source = is_show_source

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
        if not isinstance(other, PipelineTemplateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
