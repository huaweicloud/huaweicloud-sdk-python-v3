# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageInfoBusinessTypeDefinitionVOPluginsList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unique_id': 'str',
        'display_name': 'str',
        'plugin_name': 'str',
        'disabled': 'bool',
        'group_name': 'str',
        'group_type': 'str',
        'standard': 'bool',
        'db_record_name': 'str',
        'plugin_attribution': 'str',
        'plugin_composition_type': 'str',
        'runtime_attribution': 'str',
        'all_steps': 'list[PageInfoBusinessTypeDefinitionVOAllSteps]',
        'description': 'str',
        'version_attribution': 'str',
        'icon_url': 'str',
        'multi_step_editable': 'int',
        'location': 'str',
        'publisher_unique_id': 'str',
        'manifest_version': 'str'
    }

    attribute_map = {
        'unique_id': 'unique_id',
        'display_name': 'display_name',
        'plugin_name': 'plugin_name',
        'disabled': 'disabled',
        'group_name': 'group_name',
        'group_type': 'group_type',
        'standard': 'standard',
        'db_record_name': 'db_record_name',
        'plugin_attribution': 'plugin_attribution',
        'plugin_composition_type': 'plugin_composition_type',
        'runtime_attribution': 'runtime_attribution',
        'all_steps': 'all_steps',
        'description': 'description',
        'version_attribution': 'version_attribution',
        'icon_url': 'icon_url',
        'multi_step_editable': 'multi_step_editable',
        'location': 'location',
        'publisher_unique_id': 'publisher_unique_id',
        'manifest_version': 'manifest_version'
    }

    def __init__(self, unique_id=None, display_name=None, plugin_name=None, disabled=None, group_name=None, group_type=None, standard=None, db_record_name=None, plugin_attribution=None, plugin_composition_type=None, runtime_attribution=None, all_steps=None, description=None, version_attribution=None, icon_url=None, multi_step_editable=None, location=None, publisher_unique_id=None, manifest_version=None):
        r"""PageInfoBusinessTypeDefinitionVOPluginsList

        The model defined in huaweicloud sdk

        :param unique_id: **参数解释**： 唯一ID。 **取值范围**： 不涉及。 
        :type unique_id: str
        :param display_name: **参数解释**： 展示名。 **取值范围**： 不涉及。 
        :type display_name: str
        :param plugin_name: **参数解释**： 插件名。 **取值范围**： 不涉及。 
        :type plugin_name: str
        :param disabled: **参数解释**： 是否禁用。 **取值范围**： - true：禁用。 - false：未禁用。 
        :type disabled: bool
        :param group_name: **参数解释**： 组名。 **取值范围**： 不涉及。 
        :type group_name: str
        :param group_type: **参数解释**： 组类型。 **取值范围**： 不涉及。 
        :type group_type: str
        :param standard: **参数解释**： 是否标准化的插件。 **取值范围**： - true：是。 - false：否。 
        :type standard: bool
        :param db_record_name: **参数解释**： 插件记录名称。 **取值范围**： 不涉及。 
        :type db_record_name: str
        :param plugin_attribution: **参数解释**： 插件属性。 **取值范围**： 不涉及。 
        :type plugin_attribution: str
        :param plugin_composition_type: **参数解释**： 组合插件。 **取值范围**： 不涉及。 
        :type plugin_composition_type: str
        :param runtime_attribution: **参数解释**： 插件运行属性。 **取值范围**： 不涉及。 
        :type runtime_attribution: str
        :param all_steps: **参数解释**： 基础插件列表。 **取值范围**： 不涉及。 
        :type all_steps: list[:class:`huaweicloudsdkcodeartspipeline.v2.PageInfoBusinessTypeDefinitionVOAllSteps`]
        :param description: **参数解释**： 插件描述。 **取值范围**： 不涉及。 
        :type description: str
        :param version_attribution: **参数解释**： 插件版本属性。 **取值范围**： 不涉及。 
        :type version_attribution: str
        :param icon_url: **参数解释**： 插件图标URL。 **取值范围**： 不涉及。 
        :type icon_url: str
        :param multi_step_editable: **参数解释**： 插件可编辑。 **取值范围**： 不涉及。 
        :type multi_step_editable: int
        :param location: **参数解释**： 插件地址。 **取值范围**： 不涉及。 
        :type location: str
        :param publisher_unique_id: **参数解释**： 插件发布商ID。 **取值范围**： 不涉及。 
        :type publisher_unique_id: str
        :param manifest_version: **参数解释**： 插件版本。 **取值范围**： 不涉及。 
        :type manifest_version: str
        """
        
        

        self._unique_id = None
        self._display_name = None
        self._plugin_name = None
        self._disabled = None
        self._group_name = None
        self._group_type = None
        self._standard = None
        self._db_record_name = None
        self._plugin_attribution = None
        self._plugin_composition_type = None
        self._runtime_attribution = None
        self._all_steps = None
        self._description = None
        self._version_attribution = None
        self._icon_url = None
        self._multi_step_editable = None
        self._location = None
        self._publisher_unique_id = None
        self._manifest_version = None
        self.discriminator = None

        if unique_id is not None:
            self.unique_id = unique_id
        if display_name is not None:
            self.display_name = display_name
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if disabled is not None:
            self.disabled = disabled
        if group_name is not None:
            self.group_name = group_name
        if group_type is not None:
            self.group_type = group_type
        if standard is not None:
            self.standard = standard
        if db_record_name is not None:
            self.db_record_name = db_record_name
        if plugin_attribution is not None:
            self.plugin_attribution = plugin_attribution
        if plugin_composition_type is not None:
            self.plugin_composition_type = plugin_composition_type
        if runtime_attribution is not None:
            self.runtime_attribution = runtime_attribution
        if all_steps is not None:
            self.all_steps = all_steps
        if description is not None:
            self.description = description
        if version_attribution is not None:
            self.version_attribution = version_attribution
        if icon_url is not None:
            self.icon_url = icon_url
        if multi_step_editable is not None:
            self.multi_step_editable = multi_step_editable
        if location is not None:
            self.location = location
        if publisher_unique_id is not None:
            self.publisher_unique_id = publisher_unique_id
        if manifest_version is not None:
            self.manifest_version = manifest_version

    @property
    def unique_id(self):
        r"""Gets the unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 唯一ID。 **取值范围**： 不涉及。 

        :return: The unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        r"""Sets the unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 唯一ID。 **取值范围**： 不涉及。 

        :param unique_id: The unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def display_name(self):
        r"""Gets the display_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 展示名。 **取值范围**： 不涉及。 

        :return: The display_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 展示名。 **取值范围**： 不涉及。 

        :param display_name: The display_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件名。 **取值范围**： 不涉及。 

        :return: The plugin_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件名。 **取值范围**： 不涉及。 

        :param plugin_name: The plugin_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def disabled(self):
        r"""Gets the disabled of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 是否禁用。 **取值范围**： - true：禁用。 - false：未禁用。 

        :return: The disabled of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 是否禁用。 **取值范围**： - true：禁用。 - false：未禁用。 

        :param disabled: The disabled of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def group_name(self):
        r"""Gets the group_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 组名。 **取值范围**： 不涉及。 

        :return: The group_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 组名。 **取值范围**： 不涉及。 

        :param group_name: The group_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_type(self):
        r"""Gets the group_type of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 组类型。 **取值范围**： 不涉及。 

        :return: The group_type of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 组类型。 **取值范围**： 不涉及。 

        :param group_type: The group_type of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def standard(self):
        r"""Gets the standard of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 是否标准化的插件。 **取值范围**： - true：是。 - false：否。 

        :return: The standard of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: bool
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 是否标准化的插件。 **取值范围**： - true：是。 - false：否。 

        :param standard: The standard of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type standard: bool
        """
        self._standard = standard

    @property
    def db_record_name(self):
        r"""Gets the db_record_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件记录名称。 **取值范围**： 不涉及。 

        :return: The db_record_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._db_record_name

    @db_record_name.setter
    def db_record_name(self, db_record_name):
        r"""Sets the db_record_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件记录名称。 **取值范围**： 不涉及。 

        :param db_record_name: The db_record_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type db_record_name: str
        """
        self._db_record_name = db_record_name

    @property
    def plugin_attribution(self):
        r"""Gets the plugin_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件属性。 **取值范围**： 不涉及。 

        :return: The plugin_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._plugin_attribution

    @plugin_attribution.setter
    def plugin_attribution(self, plugin_attribution):
        r"""Sets the plugin_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件属性。 **取值范围**： 不涉及。 

        :param plugin_attribution: The plugin_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type plugin_attribution: str
        """
        self._plugin_attribution = plugin_attribution

    @property
    def plugin_composition_type(self):
        r"""Gets the plugin_composition_type of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 组合插件。 **取值范围**： 不涉及。 

        :return: The plugin_composition_type of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._plugin_composition_type

    @plugin_composition_type.setter
    def plugin_composition_type(self, plugin_composition_type):
        r"""Sets the plugin_composition_type of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 组合插件。 **取值范围**： 不涉及。 

        :param plugin_composition_type: The plugin_composition_type of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type plugin_composition_type: str
        """
        self._plugin_composition_type = plugin_composition_type

    @property
    def runtime_attribution(self):
        r"""Gets the runtime_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件运行属性。 **取值范围**： 不涉及。 

        :return: The runtime_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._runtime_attribution

    @runtime_attribution.setter
    def runtime_attribution(self, runtime_attribution):
        r"""Sets the runtime_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件运行属性。 **取值范围**： 不涉及。 

        :param runtime_attribution: The runtime_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type runtime_attribution: str
        """
        self._runtime_attribution = runtime_attribution

    @property
    def all_steps(self):
        r"""Gets the all_steps of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 基础插件列表。 **取值范围**： 不涉及。 

        :return: The all_steps of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PageInfoBusinessTypeDefinitionVOAllSteps`]
        """
        return self._all_steps

    @all_steps.setter
    def all_steps(self, all_steps):
        r"""Sets the all_steps of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 基础插件列表。 **取值范围**： 不涉及。 

        :param all_steps: The all_steps of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type all_steps: list[:class:`huaweicloudsdkcodeartspipeline.v2.PageInfoBusinessTypeDefinitionVOAllSteps`]
        """
        self._all_steps = all_steps

    @property
    def description(self):
        r"""Gets the description of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件描述。 **取值范围**： 不涉及。 

        :return: The description of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件描述。 **取值范围**： 不涉及。 

        :param description: The description of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type description: str
        """
        self._description = description

    @property
    def version_attribution(self):
        r"""Gets the version_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件版本属性。 **取值范围**： 不涉及。 

        :return: The version_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._version_attribution

    @version_attribution.setter
    def version_attribution(self, version_attribution):
        r"""Sets the version_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件版本属性。 **取值范围**： 不涉及。 

        :param version_attribution: The version_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type version_attribution: str
        """
        self._version_attribution = version_attribution

    @property
    def icon_url(self):
        r"""Gets the icon_url of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件图标URL。 **取值范围**： 不涉及。 

        :return: The icon_url of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        r"""Sets the icon_url of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件图标URL。 **取值范围**： 不涉及。 

        :param icon_url: The icon_url of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type icon_url: str
        """
        self._icon_url = icon_url

    @property
    def multi_step_editable(self):
        r"""Gets the multi_step_editable of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件可编辑。 **取值范围**： 不涉及。 

        :return: The multi_step_editable of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: int
        """
        return self._multi_step_editable

    @multi_step_editable.setter
    def multi_step_editable(self, multi_step_editable):
        r"""Sets the multi_step_editable of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件可编辑。 **取值范围**： 不涉及。 

        :param multi_step_editable: The multi_step_editable of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type multi_step_editable: int
        """
        self._multi_step_editable = multi_step_editable

    @property
    def location(self):
        r"""Gets the location of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件地址。 **取值范围**： 不涉及。 

        :return: The location of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件地址。 **取值范围**： 不涉及。 

        :param location: The location of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type location: str
        """
        self._location = location

    @property
    def publisher_unique_id(self):
        r"""Gets the publisher_unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件发布商ID。 **取值范围**： 不涉及。 

        :return: The publisher_unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._publisher_unique_id

    @publisher_unique_id.setter
    def publisher_unique_id(self, publisher_unique_id):
        r"""Sets the publisher_unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件发布商ID。 **取值范围**： 不涉及。 

        :param publisher_unique_id: The publisher_unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type publisher_unique_id: str
        """
        self._publisher_unique_id = publisher_unique_id

    @property
    def manifest_version(self):
        r"""Gets the manifest_version of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件版本。 **取值范围**： 不涉及。 

        :return: The manifest_version of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        r"""Sets the manifest_version of this PageInfoBusinessTypeDefinitionVOPluginsList.

        **参数解释**： 插件版本。 **取值范围**： 不涉及。 

        :param manifest_version: The manifest_version of this PageInfoBusinessTypeDefinitionVOPluginsList.
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
        if not isinstance(other, PageInfoBusinessTypeDefinitionVOPluginsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
