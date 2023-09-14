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
        'create_time': 'int',
        'update_time': 'int',
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
        'create_time': 'create_time',
        'update_time': 'update_time',
        'is_collect': 'is_collect',
        'is_show_source': 'is_show_source',
        'definition': 'definition'
    }

    def __init__(self, id=None, name=None, icon=None, manifest_version=None, language=None, description=None, is_system=None, region=None, domain_id=None, variables=None, creator_id=None, updater_id=None, create_time=None, update_time=None, is_collect=None, is_show_source=None, definition=None):
        """ShowPipelineTemplateDetailResponse

        The model defined in huaweicloud sdk

        :param id: 模板ID
        :type id: str
        :param name: 模板名称
        :type name: str
        :param icon: 模板图标
        :type icon: str
        :param manifest_version: 流水线结构定义版本，新版默认为3.0
        :type manifest_version: str
        :param language: 模板语言
        :type language: str
        :param description: 模板描述
        :type description: str
        :param is_system: 是否系统模板
        :type is_system: bool
        :param region: 所属局点
        :type region: str
        :param domain_id: 所属租户ID
        :type domain_id: str
        :param variables: 使用的自定义参数
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        :param creator_id: 创建人ID
        :type creator_id: str
        :param updater_id: 编辑人ID
        :type updater_id: str
        :param create_time: 创建日期
        :type create_time: int
        :param update_time: 更新日期
        :type update_time: int
        :param is_collect: 是否收藏
        :type is_collect: str
        :param is_show_source: 是否显示流水线源
        :type is_show_source: bool
        :param definition: 模板编排json，包含stages
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
        self._create_time = None
        self._update_time = None
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
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if is_collect is not None:
            self.is_collect = is_collect
        if is_show_source is not None:
            self.is_show_source = is_show_source
        if definition is not None:
            self.definition = definition

    @property
    def id(self):
        """Gets the id of this ShowPipelineTemplateDetailResponse.

        模板ID

        :return: The id of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowPipelineTemplateDetailResponse.

        模板ID

        :param id: The id of this ShowPipelineTemplateDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowPipelineTemplateDetailResponse.

        模板名称

        :return: The name of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowPipelineTemplateDetailResponse.

        模板名称

        :param name: The name of this ShowPipelineTemplateDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def icon(self):
        """Gets the icon of this ShowPipelineTemplateDetailResponse.

        模板图标

        :return: The icon of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ShowPipelineTemplateDetailResponse.

        模板图标

        :param icon: The icon of this ShowPipelineTemplateDetailResponse.
        :type icon: str
        """
        self._icon = icon

    @property
    def manifest_version(self):
        """Gets the manifest_version of this ShowPipelineTemplateDetailResponse.

        流水线结构定义版本，新版默认为3.0

        :return: The manifest_version of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        """Sets the manifest_version of this ShowPipelineTemplateDetailResponse.

        流水线结构定义版本，新版默认为3.0

        :param manifest_version: The manifest_version of this ShowPipelineTemplateDetailResponse.
        :type manifest_version: str
        """
        self._manifest_version = manifest_version

    @property
    def language(self):
        """Gets the language of this ShowPipelineTemplateDetailResponse.

        模板语言

        :return: The language of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ShowPipelineTemplateDetailResponse.

        模板语言

        :param language: The language of this ShowPipelineTemplateDetailResponse.
        :type language: str
        """
        self._language = language

    @property
    def description(self):
        """Gets the description of this ShowPipelineTemplateDetailResponse.

        模板描述

        :return: The description of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowPipelineTemplateDetailResponse.

        模板描述

        :param description: The description of this ShowPipelineTemplateDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def is_system(self):
        """Gets the is_system of this ShowPipelineTemplateDetailResponse.

        是否系统模板

        :return: The is_system of this ShowPipelineTemplateDetailResponse.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """Sets the is_system of this ShowPipelineTemplateDetailResponse.

        是否系统模板

        :param is_system: The is_system of this ShowPipelineTemplateDetailResponse.
        :type is_system: bool
        """
        self._is_system = is_system

    @property
    def region(self):
        """Gets the region of this ShowPipelineTemplateDetailResponse.

        所属局点

        :return: The region of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowPipelineTemplateDetailResponse.

        所属局点

        :param region: The region of this ShowPipelineTemplateDetailResponse.
        :type region: str
        """
        self._region = region

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowPipelineTemplateDetailResponse.

        所属租户ID

        :return: The domain_id of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowPipelineTemplateDetailResponse.

        所属租户ID

        :param domain_id: The domain_id of this ShowPipelineTemplateDetailResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def variables(self):
        """Gets the variables of this ShowPipelineTemplateDetailResponse.

        使用的自定义参数

        :return: The variables of this ShowPipelineTemplateDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this ShowPipelineTemplateDetailResponse.

        使用的自定义参数

        :param variables: The variables of this ShowPipelineTemplateDetailResponse.
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.CustomVariable`]
        """
        self._variables = variables

    @property
    def creator_id(self):
        """Gets the creator_id of this ShowPipelineTemplateDetailResponse.

        创建人ID

        :return: The creator_id of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this ShowPipelineTemplateDetailResponse.

        创建人ID

        :param creator_id: The creator_id of this ShowPipelineTemplateDetailResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def updater_id(self):
        """Gets the updater_id of this ShowPipelineTemplateDetailResponse.

        编辑人ID

        :return: The updater_id of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this ShowPipelineTemplateDetailResponse.

        编辑人ID

        :param updater_id: The updater_id of this ShowPipelineTemplateDetailResponse.
        :type updater_id: str
        """
        self._updater_id = updater_id

    @property
    def create_time(self):
        """Gets the create_time of this ShowPipelineTemplateDetailResponse.

        创建日期

        :return: The create_time of this ShowPipelineTemplateDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowPipelineTemplateDetailResponse.

        创建日期

        :param create_time: The create_time of this ShowPipelineTemplateDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowPipelineTemplateDetailResponse.

        更新日期

        :return: The update_time of this ShowPipelineTemplateDetailResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowPipelineTemplateDetailResponse.

        更新日期

        :param update_time: The update_time of this ShowPipelineTemplateDetailResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def is_collect(self):
        """Gets the is_collect of this ShowPipelineTemplateDetailResponse.

        是否收藏

        :return: The is_collect of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._is_collect

    @is_collect.setter
    def is_collect(self, is_collect):
        """Sets the is_collect of this ShowPipelineTemplateDetailResponse.

        是否收藏

        :param is_collect: The is_collect of this ShowPipelineTemplateDetailResponse.
        :type is_collect: str
        """
        self._is_collect = is_collect

    @property
    def is_show_source(self):
        """Gets the is_show_source of this ShowPipelineTemplateDetailResponse.

        是否显示流水线源

        :return: The is_show_source of this ShowPipelineTemplateDetailResponse.
        :rtype: bool
        """
        return self._is_show_source

    @is_show_source.setter
    def is_show_source(self, is_show_source):
        """Sets the is_show_source of this ShowPipelineTemplateDetailResponse.

        是否显示流水线源

        :param is_show_source: The is_show_source of this ShowPipelineTemplateDetailResponse.
        :type is_show_source: bool
        """
        self._is_show_source = is_show_source

    @property
    def definition(self):
        """Gets the definition of this ShowPipelineTemplateDetailResponse.

        模板编排json，包含stages

        :return: The definition of this ShowPipelineTemplateDetailResponse.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this ShowPipelineTemplateDetailResponse.

        模板编排json，包含stages

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
