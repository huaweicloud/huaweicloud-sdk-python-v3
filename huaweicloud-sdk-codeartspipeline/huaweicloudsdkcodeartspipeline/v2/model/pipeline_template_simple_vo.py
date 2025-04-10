# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineTemplateSimpleVO:

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
        'creator_id': 'str',
        'creator_name': 'str',
        'updater_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'is_collect': 'bool',
        'is_show_source': 'str',
        'stages': 'list[PipelineTemplateSimpleVOStages]'
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
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'updater_id': 'updater_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'is_collect': 'is_collect',
        'is_show_source': 'is_show_source',
        'stages': 'stages'
    }

    def __init__(self, id=None, name=None, icon=None, manifest_version=None, language=None, description=None, is_system=None, region=None, domain_id=None, creator_id=None, creator_name=None, updater_id=None, create_time=None, update_time=None, is_collect=None, is_show_source=None, stages=None):
        r"""PipelineTemplateSimpleVO

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
        :param region: 模板局点
        :type region: str
        :param domain_id: 模板所属租户ID
        :type domain_id: str
        :param creator_id: 模板创建人ID
        :type creator_id: str
        :param creator_name: 模板创建人名称
        :type creator_name: str
        :param updater_id: 模板更新人ID
        :type updater_id: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param is_collect: 是否收藏
        :type is_collect: bool
        :param is_show_source: 是否展示流水线源
        :type is_show_source: str
        :param stages: 模板编排stages
        :type stages: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTemplateSimpleVOStages`]
        """
        
        

        self._id = None
        self._name = None
        self._icon = None
        self._manifest_version = None
        self._language = None
        self._description = None
        self._is_system = None
        self._region = None
        self._domain_id = None
        self._creator_id = None
        self._creator_name = None
        self._updater_id = None
        self._create_time = None
        self._update_time = None
        self._is_collect = None
        self._is_show_source = None
        self._stages = None
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
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
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
        if stages is not None:
            self.stages = stages

    @property
    def id(self):
        r"""Gets the id of this PipelineTemplateSimpleVO.

        模板ID

        :return: The id of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PipelineTemplateSimpleVO.

        模板ID

        :param id: The id of this PipelineTemplateSimpleVO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PipelineTemplateSimpleVO.

        模板名称

        :return: The name of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PipelineTemplateSimpleVO.

        模板名称

        :param name: The name of this PipelineTemplateSimpleVO.
        :type name: str
        """
        self._name = name

    @property
    def icon(self):
        r"""Gets the icon of this PipelineTemplateSimpleVO.

        模板图标

        :return: The icon of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        r"""Sets the icon of this PipelineTemplateSimpleVO.

        模板图标

        :param icon: The icon of this PipelineTemplateSimpleVO.
        :type icon: str
        """
        self._icon = icon

    @property
    def manifest_version(self):
        r"""Gets the manifest_version of this PipelineTemplateSimpleVO.

        流水线结构定义版本，新版默认为3.0

        :return: The manifest_version of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        r"""Sets the manifest_version of this PipelineTemplateSimpleVO.

        流水线结构定义版本，新版默认为3.0

        :param manifest_version: The manifest_version of this PipelineTemplateSimpleVO.
        :type manifest_version: str
        """
        self._manifest_version = manifest_version

    @property
    def language(self):
        r"""Gets the language of this PipelineTemplateSimpleVO.

        模板语言

        :return: The language of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this PipelineTemplateSimpleVO.

        模板语言

        :param language: The language of this PipelineTemplateSimpleVO.
        :type language: str
        """
        self._language = language

    @property
    def description(self):
        r"""Gets the description of this PipelineTemplateSimpleVO.

        模板描述

        :return: The description of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PipelineTemplateSimpleVO.

        模板描述

        :param description: The description of this PipelineTemplateSimpleVO.
        :type description: str
        """
        self._description = description

    @property
    def is_system(self):
        r"""Gets the is_system of this PipelineTemplateSimpleVO.

        是否系统模板

        :return: The is_system of this PipelineTemplateSimpleVO.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        r"""Sets the is_system of this PipelineTemplateSimpleVO.

        是否系统模板

        :param is_system: The is_system of this PipelineTemplateSimpleVO.
        :type is_system: bool
        """
        self._is_system = is_system

    @property
    def region(self):
        r"""Gets the region of this PipelineTemplateSimpleVO.

        模板局点

        :return: The region of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this PipelineTemplateSimpleVO.

        模板局点

        :param region: The region of this PipelineTemplateSimpleVO.
        :type region: str
        """
        self._region = region

    @property
    def domain_id(self):
        r"""Gets the domain_id of this PipelineTemplateSimpleVO.

        模板所属租户ID

        :return: The domain_id of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this PipelineTemplateSimpleVO.

        模板所属租户ID

        :param domain_id: The domain_id of this PipelineTemplateSimpleVO.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def creator_id(self):
        r"""Gets the creator_id of this PipelineTemplateSimpleVO.

        模板创建人ID

        :return: The creator_id of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this PipelineTemplateSimpleVO.

        模板创建人ID

        :param creator_id: The creator_id of this PipelineTemplateSimpleVO.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this PipelineTemplateSimpleVO.

        模板创建人名称

        :return: The creator_name of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this PipelineTemplateSimpleVO.

        模板创建人名称

        :param creator_name: The creator_name of this PipelineTemplateSimpleVO.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def updater_id(self):
        r"""Gets the updater_id of this PipelineTemplateSimpleVO.

        模板更新人ID

        :return: The updater_id of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        r"""Sets the updater_id of this PipelineTemplateSimpleVO.

        模板更新人ID

        :param updater_id: The updater_id of this PipelineTemplateSimpleVO.
        :type updater_id: str
        """
        self._updater_id = updater_id

    @property
    def create_time(self):
        r"""Gets the create_time of this PipelineTemplateSimpleVO.

        创建时间

        :return: The create_time of this PipelineTemplateSimpleVO.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PipelineTemplateSimpleVO.

        创建时间

        :param create_time: The create_time of this PipelineTemplateSimpleVO.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this PipelineTemplateSimpleVO.

        更新时间

        :return: The update_time of this PipelineTemplateSimpleVO.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PipelineTemplateSimpleVO.

        更新时间

        :param update_time: The update_time of this PipelineTemplateSimpleVO.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def is_collect(self):
        r"""Gets the is_collect of this PipelineTemplateSimpleVO.

        是否收藏

        :return: The is_collect of this PipelineTemplateSimpleVO.
        :rtype: bool
        """
        return self._is_collect

    @is_collect.setter
    def is_collect(self, is_collect):
        r"""Sets the is_collect of this PipelineTemplateSimpleVO.

        是否收藏

        :param is_collect: The is_collect of this PipelineTemplateSimpleVO.
        :type is_collect: bool
        """
        self._is_collect = is_collect

    @property
    def is_show_source(self):
        r"""Gets the is_show_source of this PipelineTemplateSimpleVO.

        是否展示流水线源

        :return: The is_show_source of this PipelineTemplateSimpleVO.
        :rtype: str
        """
        return self._is_show_source

    @is_show_source.setter
    def is_show_source(self, is_show_source):
        r"""Sets the is_show_source of this PipelineTemplateSimpleVO.

        是否展示流水线源

        :param is_show_source: The is_show_source of this PipelineTemplateSimpleVO.
        :type is_show_source: str
        """
        self._is_show_source = is_show_source

    @property
    def stages(self):
        r"""Gets the stages of this PipelineTemplateSimpleVO.

        模板编排stages

        :return: The stages of this PipelineTemplateSimpleVO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTemplateSimpleVOStages`]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        r"""Sets the stages of this PipelineTemplateSimpleVO.

        模板编排stages

        :param stages: The stages of this PipelineTemplateSimpleVO.
        :type stages: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTemplateSimpleVOStages`]
        """
        self._stages = stages

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
        if not isinstance(other, PipelineTemplateSimpleVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
