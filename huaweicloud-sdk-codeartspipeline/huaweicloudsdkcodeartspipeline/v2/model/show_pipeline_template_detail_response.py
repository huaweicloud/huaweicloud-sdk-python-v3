# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPipelineTemplateDetailResponse(SdkResponse):

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
        'icon': 'str',
        'manifest_version': 'str',
        'language': 'str',
        'description': 'str',
        'is_system': 'bool',
        'region': 'str',
        'domain_id': 'str',
        'variables': 'list[CustomVariable]',
        'creator_id': 'str',
        'updater_id': 'str',
        'is_collect': 'str',
        'is_show_source': 'bool',
        'definition': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'icon': 'icon',
        'manifest_version': 'manifest_version',
        'language': 'language',
        'description': 'description',
        'is_system': 'is_system',
        'region': 'region',
        'domain_id': 'domain_id',
        'variables': 'variables',
        'creator_id': 'creator_id',
        'updater_id': 'updater_id',
        'is_collect': 'is_collect',
        'is_show_source': 'is_show_source',
        'definition': 'definition'
    }

    def __init__(self, id=None, name=None, icon=None, manifest_version=None, language=None, description=None, is_system=None, region=None, domain_id=None, variables=None, creator_id=None, updater_id=None, is_collect=None, is_show_source=None, definition=None):
        r"""ShowPipelineTemplateDetailResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 模板ID。 **取值范围**： 32位字符，由数字和字母组成。 
        :type id: str
        :param name: **参数解释**： 模板名称。 **取值范围**： 不涉及。 
        :type name: str
        :param icon: **参数解释**： 模板图标。 **取值范围**： 不涉及。 
        :type icon: str
        :param manifest_version: **参数解释**： 版本。 **取值范围**： 默认3.0。 
        :type manifest_version: str
        :param language: **参数解释**： 模板语言。 **取值范围**： - java。 - python。 - nodejs。 - go。 - net。 - cpp。 - php。 - other。 - none。 
        :type language: str
        :param description: **参数解释**： 模板描述。 **取值范围**： 不涉及。 
        :type description: str
        :param is_system: **参数解释**： 是否系统模板。 **取值范围**： - true：是系统模板。 - false：不是系统模板。 
        :type is_system: bool
        :param region: **参数解释**： 模板局点。 **取值范围**： 不涉及。 
        :type region: str
        :param domain_id: **参数解释**： 模板所属租户ID。 **取值范围**： 32位字符，由数字和字母组成。 
        :type domain_id: str
        :param variables: **参数解释**： 自定义参数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        :param creator_id: **参数解释**： 模板创建人ID。 **取值范围**： 32位字符，由数字和字母组成。 
        :type creator_id: str
        :param updater_id: **参数解释**： 模板更新人ID。 **取值范围**： 32位字符，由数字和字母组成。 
        :type updater_id: str
        :param is_collect: **参数解释**： 是否收藏。 **取值范围**： - true：收藏。 - false：不收藏。 
        :type is_collect: str
        :param is_show_source: **参数解释**： 是否展示流水线源。 **取值范围**： - true：展示流水线源。 - false：不展示流水线源。 
        :type is_show_source: bool
        :param definition: **参数解释**： 模板编排json，包含stages。 **取值范围**： 不涉及。 
        :type definition: str
        """
        
        super(ShowPipelineTemplateDetailResponse, self).__init__()

        self._id = None
        self._name = None
        self._icon = None
        self._manifest_version = None
        self._language = None
        self._description = None
        self._is_system = None
        self._region = None
        self._domain_id = None
        self._variables = None
        self._creator_id = None
        self._updater_id = None
        self._is_collect = None
        self._is_show_source = None
        self._definition = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if icon is not None:
            self.icon = icon
        if manifest_version is not None:
            self.manifest_version = manifest_version
        if language is not None:
            self.language = language
        if description is not None:
            self.description = description
        if is_system is not None:
            self.is_system = is_system
        if region is not None:
            self.region = region
        if domain_id is not None:
            self.domain_id = domain_id
        if variables is not None:
            self.variables = variables
        if creator_id is not None:
            self.creator_id = creator_id
        if updater_id is not None:
            self.updater_id = updater_id
        if is_collect is not None:
            self.is_collect = is_collect
        if is_show_source is not None:
            self.is_show_source = is_show_source
        if definition is not None:
            self.definition = definition

    @property
    def id(self):
        r"""Gets the id of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :return: The id of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :param id: The id of this ShowPipelineTemplateDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板名称。 **取值范围**： 不涉及。 

        :return: The name of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板名称。 **取值范围**： 不涉及。 

        :param name: The name of this ShowPipelineTemplateDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def icon(self):
        r"""Gets the icon of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板图标。 **取值范围**： 不涉及。 

        :return: The icon of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        r"""Sets the icon of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板图标。 **取值范围**： 不涉及。 

        :param icon: The icon of this ShowPipelineTemplateDetailResponse.
        :type icon: str
        """
        self._icon = icon

    @property
    def manifest_version(self):
        r"""Gets the manifest_version of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 版本。 **取值范围**： 默认3.0。 

        :return: The manifest_version of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        r"""Sets the manifest_version of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 版本。 **取值范围**： 默认3.0。 

        :param manifest_version: The manifest_version of this ShowPipelineTemplateDetailResponse.
        :type manifest_version: str
        """
        self._manifest_version = manifest_version

    @property
    def language(self):
        r"""Gets the language of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板语言。 **取值范围**： - java。 - python。 - nodejs。 - go。 - net。 - cpp。 - php。 - other。 - none。 

        :return: The language of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板语言。 **取值范围**： - java。 - python。 - nodejs。 - go。 - net。 - cpp。 - php。 - other。 - none。 

        :param language: The language of this ShowPipelineTemplateDetailResponse.
        :type language: str
        """
        self._language = language

    @property
    def description(self):
        r"""Gets the description of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板描述。 **取值范围**： 不涉及。 

        :return: The description of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板描述。 **取值范围**： 不涉及。 

        :param description: The description of this ShowPipelineTemplateDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def is_system(self):
        r"""Gets the is_system of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 是否系统模板。 **取值范围**： - true：是系统模板。 - false：不是系统模板。 

        :return: The is_system of this ShowPipelineTemplateDetailResponse.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        r"""Sets the is_system of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 是否系统模板。 **取值范围**： - true：是系统模板。 - false：不是系统模板。 

        :param is_system: The is_system of this ShowPipelineTemplateDetailResponse.
        :type is_system: bool
        """
        self._is_system = is_system

    @property
    def region(self):
        r"""Gets the region of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板局点。 **取值范围**： 不涉及。 

        :return: The region of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板局点。 **取值范围**： 不涉及。 

        :param region: The region of this ShowPipelineTemplateDetailResponse.
        :type region: str
        """
        self._region = region

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板所属租户ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :return: The domain_id of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板所属租户ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :param domain_id: The domain_id of this ShowPipelineTemplateDetailResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def variables(self):
        r"""Gets the variables of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 自定义参数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The variables of this ShowPipelineTemplateDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 自定义参数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param variables: The variables of this ShowPipelineTemplateDetailResponse.
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        """
        self._variables = variables

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板创建人ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :return: The creator_id of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板创建人ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :param creator_id: The creator_id of this ShowPipelineTemplateDetailResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def updater_id(self):
        r"""Gets the updater_id of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板更新人ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :return: The updater_id of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        r"""Sets the updater_id of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板更新人ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :param updater_id: The updater_id of this ShowPipelineTemplateDetailResponse.
        :type updater_id: str
        """
        self._updater_id = updater_id

    @property
    def is_collect(self):
        r"""Gets the is_collect of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 是否收藏。 **取值范围**： - true：收藏。 - false：不收藏。 

        :return: The is_collect of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._is_collect

    @is_collect.setter
    def is_collect(self, is_collect):
        r"""Sets the is_collect of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 是否收藏。 **取值范围**： - true：收藏。 - false：不收藏。 

        :param is_collect: The is_collect of this ShowPipelineTemplateDetailResponse.
        :type is_collect: str
        """
        self._is_collect = is_collect

    @property
    def is_show_source(self):
        r"""Gets the is_show_source of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 是否展示流水线源。 **取值范围**： - true：展示流水线源。 - false：不展示流水线源。 

        :return: The is_show_source of this ShowPipelineTemplateDetailResponse.
        :rtype: bool
        """
        return self._is_show_source

    @is_show_source.setter
    def is_show_source(self, is_show_source):
        r"""Sets the is_show_source of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 是否展示流水线源。 **取值范围**： - true：展示流水线源。 - false：不展示流水线源。 

        :param is_show_source: The is_show_source of this ShowPipelineTemplateDetailResponse.
        :type is_show_source: bool
        """
        self._is_show_source = is_show_source

    @property
    def definition(self):
        r"""Gets the definition of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板编排json，包含stages。 **取值范围**： 不涉及。 

        :return: The definition of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        r"""Sets the definition of this ShowPipelineTemplateDetailResponse.

        **参数解释**： 模板编排json，包含stages。 **取值范围**： 不涉及。 

        :param definition: The definition of this ShowPipelineTemplateDetailResponse.
        :type definition: str
        """
        self._definition = definition

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
        if not isinstance(other, ShowPipelineTemplateDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
