# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginBasicVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_name': 'str',
        'display_name': 'str',
        'db_record_name': 'str',
        'version': 'str',
        'version_description': 'str',
        'description': 'str',
        'version_attribution': 'str',
        'unique_id': 'str',
        'op_user': 'str',
        'op_time': 'str',
        'plugin_composition_type': 'str',
        'plugin_attribution': 'str',
        'workspace_id': 'str',
        'business_type': 'str',
        'business_type_display_name': 'str',
        'maintainers': 'str',
        'icon_url': 'str',
        'refer_count': 'int',
        'usage_count': 'int',
        'runtime_attribution': 'str',
        'active': 'int',
        'version_state': 'str',
        'publisher_unique_id': 'str',
        'creator': 'str',
        'create_time': 'str',
        'manifest_version': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'display_name': 'display_name',
        'db_record_name': 'db_record_name',
        'version': 'version',
        'version_description': 'version_description',
        'description': 'description',
        'version_attribution': 'version_attribution',
        'unique_id': 'unique_id',
        'op_user': 'op_user',
        'op_time': 'op_time',
        'plugin_composition_type': 'plugin_composition_type',
        'plugin_attribution': 'plugin_attribution',
        'workspace_id': 'workspace_id',
        'business_type': 'business_type',
        'business_type_display_name': 'business_type_display_name',
        'maintainers': 'maintainers',
        'icon_url': 'icon_url',
        'refer_count': 'refer_count',
        'usage_count': 'usage_count',
        'runtime_attribution': 'runtime_attribution',
        'active': 'active',
        'version_state': 'version_state',
        'publisher_unique_id': 'publisher_unique_id',
        'creator': 'creator',
        'create_time': 'create_time',
        'manifest_version': 'manifest_version'
    }

    def __init__(self, plugin_name=None, display_name=None, db_record_name=None, version=None, version_description=None, description=None, version_attribution=None, unique_id=None, op_user=None, op_time=None, plugin_composition_type=None, plugin_attribution=None, workspace_id=None, business_type=None, business_type_display_name=None, maintainers=None, icon_url=None, refer_count=None, usage_count=None, runtime_attribution=None, active=None, version_state=None, publisher_unique_id=None, creator=None, create_time=None, manifest_version=None):
        r"""PluginBasicVO

        The model defined in huaweicloud sdk

        :param plugin_name: **参数解释**： 扩展插件名称。 **取值范围**： 1到50位字符。 
        :type plugin_name: str
        :param display_name: **参数解释**： 扩展插件名称。 **取值范围**： 不涉及。 
        :type display_name: str
        :param db_record_name: **参数解释**： 插件记录展示名称。 **取值范围**： 不涉及。 
        :type db_record_name: str
        :param version: **参数解释**： 扩展插件版本号。 **取值范围**： 不涉及。 
        :type version: str
        :param version_description: **参数解释**： 扩展插件版本号说明。 **取值范围**： 不涉及。 
        :type version_description: str
        :param description: **参数解释**： 扩展插件描述。 **取值范围**： 不涉及。 
        :type description: str
        :param version_attribution: **参数解释**： 扩展插件版本属性。 **取值范围**： - draft：草稿版本。 - formal：正式版本。 
        :type version_attribution: str
        :param unique_id: **参数解释**： 扩展插件唯一ID。 **取值范围**： 不涉及。 
        :type unique_id: str
        :param op_user: **参数解释**： 扩展插件最后更新人。 **取值范围**： 不涉及。 
        :type op_user: str
        :param op_time: **参数解释**： 扩展插件最后更新时间。 **取值范围**： 不涉及。 
        :type op_time: str
        :param plugin_composition_type: **参数解释**： 用于标识插件是否为多个step组成的组合插件。 **取值范围**： - multi：组合插件。 - single：非组合插件。 
        :type plugin_composition_type: str
        :param plugin_attribution: **参数解释**： 扩展插件属性。 **取值范围**： - custom：自定义插件。 - official：官方插件。 - published：已发布的发布商插件。 
        :type plugin_attribution: str
        :param workspace_id: **参数解释**： 租户ID，用户的domainId。 **取值范围**： 32位字符，仅由数字和字母组成。 
        :type workspace_id: str
        :param business_type: **参数解释**： 扩展插件业务类型。 **取值范围**： 不涉及。 
        :type business_type: str
        :param business_type_display_name: **参数解释**： 扩展插件业务类型展示名称。 **取值范围**： 不涉及。 
        :type business_type_display_name: str
        :param maintainers: **参数解释**： 扩展插件维护人。 **取值范围**： 不涉及。 
        :type maintainers: str
        :param icon_url: **参数解释**： 扩展插件图标地址。 **取值范围**： 不涉及。 
        :type icon_url: str
        :param refer_count: **参数解释**： 扩展插件被流水线引用次数。 **取值范围**： 不涉及。 
        :type refer_count: int
        :param usage_count: **参数解释**： 扩展插件被流水线使用次数。 **取值范围**： 不涉及。 
        :type usage_count: int
        :param runtime_attribution: **参数解释**： 运行属性。 **取值范围**： - agent：运行基于流水线agent。 - agentLess：运行无需流水线agent。 
        :type runtime_attribution: str
        :param active: **参数解释**： 扩展插件是否激活。 **取值范围**： - true：激活。 - false：未激活。 
        :type active: int
        :param version_state: **参数解释**： 当前插件版本状态。 **取值范围**： 不涉及。 
        :type version_state: str
        :param publisher_unique_id: **参数解释**： 发布商ID。 **取值范围**： 不涉及。 
        :type publisher_unique_id: str
        :param creator: **参数解释**： 创建者名称。 **取值范围**： 不涉及。 
        :type creator: str
        :param create_time: **参数解释**： 创建时间。 **取值范围**： 不涉及。 
        :type create_time: str
        :param manifest_version: **参数解释**： 插件版本标识符。 **取值范围**： 不涉及。 
        :type manifest_version: str
        """
        
        

        self._plugin_name = None
        self._display_name = None
        self._db_record_name = None
        self._version = None
        self._version_description = None
        self._description = None
        self._version_attribution = None
        self._unique_id = None
        self._op_user = None
        self._op_time = None
        self._plugin_composition_type = None
        self._plugin_attribution = None
        self._workspace_id = None
        self._business_type = None
        self._business_type_display_name = None
        self._maintainers = None
        self._icon_url = None
        self._refer_count = None
        self._usage_count = None
        self._runtime_attribution = None
        self._active = None
        self._version_state = None
        self._publisher_unique_id = None
        self._creator = None
        self._create_time = None
        self._manifest_version = None
        self.discriminator = None

        if plugin_name is not None:
            self.plugin_name = plugin_name
        if display_name is not None:
            self.display_name = display_name
        if db_record_name is not None:
            self.db_record_name = db_record_name
        if version is not None:
            self.version = version
        if version_description is not None:
            self.version_description = version_description
        if description is not None:
            self.description = description
        if version_attribution is not None:
            self.version_attribution = version_attribution
        if unique_id is not None:
            self.unique_id = unique_id
        if op_user is not None:
            self.op_user = op_user
        if op_time is not None:
            self.op_time = op_time
        if plugin_composition_type is not None:
            self.plugin_composition_type = plugin_composition_type
        if plugin_attribution is not None:
            self.plugin_attribution = plugin_attribution
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if business_type is not None:
            self.business_type = business_type
        if business_type_display_name is not None:
            self.business_type_display_name = business_type_display_name
        if maintainers is not None:
            self.maintainers = maintainers
        if icon_url is not None:
            self.icon_url = icon_url
        if refer_count is not None:
            self.refer_count = refer_count
        if usage_count is not None:
            self.usage_count = usage_count
        if runtime_attribution is not None:
            self.runtime_attribution = runtime_attribution
        if active is not None:
            self.active = active
        if version_state is not None:
            self.version_state = version_state
        if publisher_unique_id is not None:
            self.publisher_unique_id = publisher_unique_id
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if manifest_version is not None:
            self.manifest_version = manifest_version

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this PluginBasicVO.

        **参数解释**： 扩展插件名称。 **取值范围**： 1到50位字符。 

        :return: The plugin_name of this PluginBasicVO.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this PluginBasicVO.

        **参数解释**： 扩展插件名称。 **取值范围**： 1到50位字符。 

        :param plugin_name: The plugin_name of this PluginBasicVO.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def display_name(self):
        r"""Gets the display_name of this PluginBasicVO.

        **参数解释**： 扩展插件名称。 **取值范围**： 不涉及。 

        :return: The display_name of this PluginBasicVO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this PluginBasicVO.

        **参数解释**： 扩展插件名称。 **取值范围**： 不涉及。 

        :param display_name: The display_name of this PluginBasicVO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def db_record_name(self):
        r"""Gets the db_record_name of this PluginBasicVO.

        **参数解释**： 插件记录展示名称。 **取值范围**： 不涉及。 

        :return: The db_record_name of this PluginBasicVO.
        :rtype: str
        """
        return self._db_record_name

    @db_record_name.setter
    def db_record_name(self, db_record_name):
        r"""Sets the db_record_name of this PluginBasicVO.

        **参数解释**： 插件记录展示名称。 **取值范围**： 不涉及。 

        :param db_record_name: The db_record_name of this PluginBasicVO.
        :type db_record_name: str
        """
        self._db_record_name = db_record_name

    @property
    def version(self):
        r"""Gets the version of this PluginBasicVO.

        **参数解释**： 扩展插件版本号。 **取值范围**： 不涉及。 

        :return: The version of this PluginBasicVO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PluginBasicVO.

        **参数解释**： 扩展插件版本号。 **取值范围**： 不涉及。 

        :param version: The version of this PluginBasicVO.
        :type version: str
        """
        self._version = version

    @property
    def version_description(self):
        r"""Gets the version_description of this PluginBasicVO.

        **参数解释**： 扩展插件版本号说明。 **取值范围**： 不涉及。 

        :return: The version_description of this PluginBasicVO.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this PluginBasicVO.

        **参数解释**： 扩展插件版本号说明。 **取值范围**： 不涉及。 

        :param version_description: The version_description of this PluginBasicVO.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def description(self):
        r"""Gets the description of this PluginBasicVO.

        **参数解释**： 扩展插件描述。 **取值范围**： 不涉及。 

        :return: The description of this PluginBasicVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PluginBasicVO.

        **参数解释**： 扩展插件描述。 **取值范围**： 不涉及。 

        :param description: The description of this PluginBasicVO.
        :type description: str
        """
        self._description = description

    @property
    def version_attribution(self):
        r"""Gets the version_attribution of this PluginBasicVO.

        **参数解释**： 扩展插件版本属性。 **取值范围**： - draft：草稿版本。 - formal：正式版本。 

        :return: The version_attribution of this PluginBasicVO.
        :rtype: str
        """
        return self._version_attribution

    @version_attribution.setter
    def version_attribution(self, version_attribution):
        r"""Sets the version_attribution of this PluginBasicVO.

        **参数解释**： 扩展插件版本属性。 **取值范围**： - draft：草稿版本。 - formal：正式版本。 

        :param version_attribution: The version_attribution of this PluginBasicVO.
        :type version_attribution: str
        """
        self._version_attribution = version_attribution

    @property
    def unique_id(self):
        r"""Gets the unique_id of this PluginBasicVO.

        **参数解释**： 扩展插件唯一ID。 **取值范围**： 不涉及。 

        :return: The unique_id of this PluginBasicVO.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        r"""Sets the unique_id of this PluginBasicVO.

        **参数解释**： 扩展插件唯一ID。 **取值范围**： 不涉及。 

        :param unique_id: The unique_id of this PluginBasicVO.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def op_user(self):
        r"""Gets the op_user of this PluginBasicVO.

        **参数解释**： 扩展插件最后更新人。 **取值范围**： 不涉及。 

        :return: The op_user of this PluginBasicVO.
        :rtype: str
        """
        return self._op_user

    @op_user.setter
    def op_user(self, op_user):
        r"""Sets the op_user of this PluginBasicVO.

        **参数解释**： 扩展插件最后更新人。 **取值范围**： 不涉及。 

        :param op_user: The op_user of this PluginBasicVO.
        :type op_user: str
        """
        self._op_user = op_user

    @property
    def op_time(self):
        r"""Gets the op_time of this PluginBasicVO.

        **参数解释**： 扩展插件最后更新时间。 **取值范围**： 不涉及。 

        :return: The op_time of this PluginBasicVO.
        :rtype: str
        """
        return self._op_time

    @op_time.setter
    def op_time(self, op_time):
        r"""Sets the op_time of this PluginBasicVO.

        **参数解释**： 扩展插件最后更新时间。 **取值范围**： 不涉及。 

        :param op_time: The op_time of this PluginBasicVO.
        :type op_time: str
        """
        self._op_time = op_time

    @property
    def plugin_composition_type(self):
        r"""Gets the plugin_composition_type of this PluginBasicVO.

        **参数解释**： 用于标识插件是否为多个step组成的组合插件。 **取值范围**： - multi：组合插件。 - single：非组合插件。 

        :return: The plugin_composition_type of this PluginBasicVO.
        :rtype: str
        """
        return self._plugin_composition_type

    @plugin_composition_type.setter
    def plugin_composition_type(self, plugin_composition_type):
        r"""Sets the plugin_composition_type of this PluginBasicVO.

        **参数解释**： 用于标识插件是否为多个step组成的组合插件。 **取值范围**： - multi：组合插件。 - single：非组合插件。 

        :param plugin_composition_type: The plugin_composition_type of this PluginBasicVO.
        :type plugin_composition_type: str
        """
        self._plugin_composition_type = plugin_composition_type

    @property
    def plugin_attribution(self):
        r"""Gets the plugin_attribution of this PluginBasicVO.

        **参数解释**： 扩展插件属性。 **取值范围**： - custom：自定义插件。 - official：官方插件。 - published：已发布的发布商插件。 

        :return: The plugin_attribution of this PluginBasicVO.
        :rtype: str
        """
        return self._plugin_attribution

    @plugin_attribution.setter
    def plugin_attribution(self, plugin_attribution):
        r"""Sets the plugin_attribution of this PluginBasicVO.

        **参数解释**： 扩展插件属性。 **取值范围**： - custom：自定义插件。 - official：官方插件。 - published：已发布的发布商插件。 

        :param plugin_attribution: The plugin_attribution of this PluginBasicVO.
        :type plugin_attribution: str
        """
        self._plugin_attribution = plugin_attribution

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this PluginBasicVO.

        **参数解释**： 租户ID，用户的domainId。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :return: The workspace_id of this PluginBasicVO.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this PluginBasicVO.

        **参数解释**： 租户ID，用户的domainId。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :param workspace_id: The workspace_id of this PluginBasicVO.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def business_type(self):
        r"""Gets the business_type of this PluginBasicVO.

        **参数解释**： 扩展插件业务类型。 **取值范围**： 不涉及。 

        :return: The business_type of this PluginBasicVO.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this PluginBasicVO.

        **参数解释**： 扩展插件业务类型。 **取值范围**： 不涉及。 

        :param business_type: The business_type of this PluginBasicVO.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def business_type_display_name(self):
        r"""Gets the business_type_display_name of this PluginBasicVO.

        **参数解释**： 扩展插件业务类型展示名称。 **取值范围**： 不涉及。 

        :return: The business_type_display_name of this PluginBasicVO.
        :rtype: str
        """
        return self._business_type_display_name

    @business_type_display_name.setter
    def business_type_display_name(self, business_type_display_name):
        r"""Sets the business_type_display_name of this PluginBasicVO.

        **参数解释**： 扩展插件业务类型展示名称。 **取值范围**： 不涉及。 

        :param business_type_display_name: The business_type_display_name of this PluginBasicVO.
        :type business_type_display_name: str
        """
        self._business_type_display_name = business_type_display_name

    @property
    def maintainers(self):
        r"""Gets the maintainers of this PluginBasicVO.

        **参数解释**： 扩展插件维护人。 **取值范围**： 不涉及。 

        :return: The maintainers of this PluginBasicVO.
        :rtype: str
        """
        return self._maintainers

    @maintainers.setter
    def maintainers(self, maintainers):
        r"""Sets the maintainers of this PluginBasicVO.

        **参数解释**： 扩展插件维护人。 **取值范围**： 不涉及。 

        :param maintainers: The maintainers of this PluginBasicVO.
        :type maintainers: str
        """
        self._maintainers = maintainers

    @property
    def icon_url(self):
        r"""Gets the icon_url of this PluginBasicVO.

        **参数解释**： 扩展插件图标地址。 **取值范围**： 不涉及。 

        :return: The icon_url of this PluginBasicVO.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        r"""Sets the icon_url of this PluginBasicVO.

        **参数解释**： 扩展插件图标地址。 **取值范围**： 不涉及。 

        :param icon_url: The icon_url of this PluginBasicVO.
        :type icon_url: str
        """
        self._icon_url = icon_url

    @property
    def refer_count(self):
        r"""Gets the refer_count of this PluginBasicVO.

        **参数解释**： 扩展插件被流水线引用次数。 **取值范围**： 不涉及。 

        :return: The refer_count of this PluginBasicVO.
        :rtype: int
        """
        return self._refer_count

    @refer_count.setter
    def refer_count(self, refer_count):
        r"""Sets the refer_count of this PluginBasicVO.

        **参数解释**： 扩展插件被流水线引用次数。 **取值范围**： 不涉及。 

        :param refer_count: The refer_count of this PluginBasicVO.
        :type refer_count: int
        """
        self._refer_count = refer_count

    @property
    def usage_count(self):
        r"""Gets the usage_count of this PluginBasicVO.

        **参数解释**： 扩展插件被流水线使用次数。 **取值范围**： 不涉及。 

        :return: The usage_count of this PluginBasicVO.
        :rtype: int
        """
        return self._usage_count

    @usage_count.setter
    def usage_count(self, usage_count):
        r"""Sets the usage_count of this PluginBasicVO.

        **参数解释**： 扩展插件被流水线使用次数。 **取值范围**： 不涉及。 

        :param usage_count: The usage_count of this PluginBasicVO.
        :type usage_count: int
        """
        self._usage_count = usage_count

    @property
    def runtime_attribution(self):
        r"""Gets the runtime_attribution of this PluginBasicVO.

        **参数解释**： 运行属性。 **取值范围**： - agent：运行基于流水线agent。 - agentLess：运行无需流水线agent。 

        :return: The runtime_attribution of this PluginBasicVO.
        :rtype: str
        """
        return self._runtime_attribution

    @runtime_attribution.setter
    def runtime_attribution(self, runtime_attribution):
        r"""Sets the runtime_attribution of this PluginBasicVO.

        **参数解释**： 运行属性。 **取值范围**： - agent：运行基于流水线agent。 - agentLess：运行无需流水线agent。 

        :param runtime_attribution: The runtime_attribution of this PluginBasicVO.
        :type runtime_attribution: str
        """
        self._runtime_attribution = runtime_attribution

    @property
    def active(self):
        r"""Gets the active of this PluginBasicVO.

        **参数解释**： 扩展插件是否激活。 **取值范围**： - true：激活。 - false：未激活。 

        :return: The active of this PluginBasicVO.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        r"""Sets the active of this PluginBasicVO.

        **参数解释**： 扩展插件是否激活。 **取值范围**： - true：激活。 - false：未激活。 

        :param active: The active of this PluginBasicVO.
        :type active: int
        """
        self._active = active

    @property
    def version_state(self):
        r"""Gets the version_state of this PluginBasicVO.

        **参数解释**： 当前插件版本状态。 **取值范围**： 不涉及。 

        :return: The version_state of this PluginBasicVO.
        :rtype: str
        """
        return self._version_state

    @version_state.setter
    def version_state(self, version_state):
        r"""Sets the version_state of this PluginBasicVO.

        **参数解释**： 当前插件版本状态。 **取值范围**： 不涉及。 

        :param version_state: The version_state of this PluginBasicVO.
        :type version_state: str
        """
        self._version_state = version_state

    @property
    def publisher_unique_id(self):
        r"""Gets the publisher_unique_id of this PluginBasicVO.

        **参数解释**： 发布商ID。 **取值范围**： 不涉及。 

        :return: The publisher_unique_id of this PluginBasicVO.
        :rtype: str
        """
        return self._publisher_unique_id

    @publisher_unique_id.setter
    def publisher_unique_id(self, publisher_unique_id):
        r"""Sets the publisher_unique_id of this PluginBasicVO.

        **参数解释**： 发布商ID。 **取值范围**： 不涉及。 

        :param publisher_unique_id: The publisher_unique_id of this PluginBasicVO.
        :type publisher_unique_id: str
        """
        self._publisher_unique_id = publisher_unique_id

    @property
    def creator(self):
        r"""Gets the creator of this PluginBasicVO.

        **参数解释**： 创建者名称。 **取值范围**： 不涉及。 

        :return: The creator of this PluginBasicVO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this PluginBasicVO.

        **参数解释**： 创建者名称。 **取值范围**： 不涉及。 

        :param creator: The creator of this PluginBasicVO.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this PluginBasicVO.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。 

        :return: The create_time of this PluginBasicVO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PluginBasicVO.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。 

        :param create_time: The create_time of this PluginBasicVO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def manifest_version(self):
        r"""Gets the manifest_version of this PluginBasicVO.

        **参数解释**： 插件版本标识符。 **取值范围**： 不涉及。 

        :return: The manifest_version of this PluginBasicVO.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        r"""Sets the manifest_version of this PluginBasicVO.

        **参数解释**： 插件版本标识符。 **取值范围**： 不涉及。 

        :param manifest_version: The manifest_version of this PluginBasicVO.
        :type manifest_version: str
        """
        self._manifest_version = manifest_version

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
        if not isinstance(other, PluginBasicVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
