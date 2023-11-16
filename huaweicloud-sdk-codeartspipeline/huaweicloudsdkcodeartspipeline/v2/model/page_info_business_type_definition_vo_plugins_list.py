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
        'plugin_attribution': 'str',
        'plugin_composition_type': 'str',
        'runtime_attribution': 'str',
        'all_steps': 'list[FullStagePluginsRelationVOAllSteps]',
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
        'plugin_attribution': 'plugin_attribution',
        'plugin_composition_type': 'plugin_composition_type',
        'runtime_attribution': 'runtime_attribution',
        'all_steps': 'all_steps',
        'description': 'description',
        'version_attribution': 'version_attribution',
        'icon_url': 'icon_url',
        'multi_step_editable': 'multi_step_editable',
        'location': 'location',
        'publisher_unique_id': 'publisherUniqueId',
        'manifest_version': 'manifestVersion'
    }

    def __init__(self, unique_id=None, display_name=None, plugin_name=None, disabled=None, group_name=None, group_type=None, plugin_attribution=None, plugin_composition_type=None, runtime_attribution=None, all_steps=None, description=None, version_attribution=None, icon_url=None, multi_step_editable=None, location=None, publisher_unique_id=None, manifest_version=None):
        """PageInfoBusinessTypeDefinitionVOPluginsList

        The model defined in huaweicloud sdk

        :param unique_id: 唯一ID
        :type unique_id: str
        :param display_name: 展示名
        :type display_name: str
        :param plugin_name: 插件名
        :type plugin_name: str
        :param disabled: 禁用
        :type disabled: bool
        :param group_name: 组名
        :type group_name: str
        :param group_type: 组类型
        :type group_type: str
        :param plugin_attribution: 属性
        :type plugin_attribution: str
        :param plugin_composition_type: 组合插件
        :type plugin_composition_type: str
        :param runtime_attribution: 运行属性
        :type runtime_attribution: str
        :param all_steps: 基础插件列表
        :type all_steps: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOAllSteps`]
        :param description: 描述
        :type description: str
        :param version_attribution: 版本属性
        :type version_attribution: str
        :param icon_url: 图标URL
        :type icon_url: str
        :param multi_step_editable: 可编辑
        :type multi_step_editable: int
        :param location: 地址
        :type location: str
        :param publisher_unique_id: 发布商ID
        :type publisher_unique_id: str
        :param manifest_version: 版本
        :type manifest_version: str
        """
        
        

        self._unique_id = None
        self._display_name = None
        self._plugin_name = None
        self._disabled = None
        self._group_name = None
        self._group_type = None
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
        """Gets the unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.

        唯一ID

        :return: The unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.

        唯一ID

        :param unique_id: The unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def display_name(self):
        """Gets the display_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        展示名

        :return: The display_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        展示名

        :param display_name: The display_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def plugin_name(self):
        """Gets the plugin_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        插件名

        :return: The plugin_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        插件名

        :param plugin_name: The plugin_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def disabled(self):
        """Gets the disabled of this PageInfoBusinessTypeDefinitionVOPluginsList.

        禁用

        :return: The disabled of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this PageInfoBusinessTypeDefinitionVOPluginsList.

        禁用

        :param disabled: The disabled of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def group_name(self):
        """Gets the group_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        组名

        :return: The group_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this PageInfoBusinessTypeDefinitionVOPluginsList.

        组名

        :param group_name: The group_name of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_type(self):
        """Gets the group_type of this PageInfoBusinessTypeDefinitionVOPluginsList.

        组类型

        :return: The group_type of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this PageInfoBusinessTypeDefinitionVOPluginsList.

        组类型

        :param group_type: The group_type of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def plugin_attribution(self):
        """Gets the plugin_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        属性

        :return: The plugin_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._plugin_attribution

    @plugin_attribution.setter
    def plugin_attribution(self, plugin_attribution):
        """Sets the plugin_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        属性

        :param plugin_attribution: The plugin_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type plugin_attribution: str
        """
        self._plugin_attribution = plugin_attribution

    @property
    def plugin_composition_type(self):
        """Gets the plugin_composition_type of this PageInfoBusinessTypeDefinitionVOPluginsList.

        组合插件

        :return: The plugin_composition_type of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._plugin_composition_type

    @plugin_composition_type.setter
    def plugin_composition_type(self, plugin_composition_type):
        """Sets the plugin_composition_type of this PageInfoBusinessTypeDefinitionVOPluginsList.

        组合插件

        :param plugin_composition_type: The plugin_composition_type of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type plugin_composition_type: str
        """
        self._plugin_composition_type = plugin_composition_type

    @property
    def runtime_attribution(self):
        """Gets the runtime_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        运行属性

        :return: The runtime_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._runtime_attribution

    @runtime_attribution.setter
    def runtime_attribution(self, runtime_attribution):
        """Sets the runtime_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        运行属性

        :param runtime_attribution: The runtime_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type runtime_attribution: str
        """
        self._runtime_attribution = runtime_attribution

    @property
    def all_steps(self):
        """Gets the all_steps of this PageInfoBusinessTypeDefinitionVOPluginsList.

        基础插件列表

        :return: The all_steps of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOAllSteps`]
        """
        return self._all_steps

    @all_steps.setter
    def all_steps(self, all_steps):
        """Sets the all_steps of this PageInfoBusinessTypeDefinitionVOPluginsList.

        基础插件列表

        :param all_steps: The all_steps of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type all_steps: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOAllSteps`]
        """
        self._all_steps = all_steps

    @property
    def description(self):
        """Gets the description of this PageInfoBusinessTypeDefinitionVOPluginsList.

        描述

        :return: The description of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PageInfoBusinessTypeDefinitionVOPluginsList.

        描述

        :param description: The description of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type description: str
        """
        self._description = description

    @property
    def version_attribution(self):
        """Gets the version_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        版本属性

        :return: The version_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._version_attribution

    @version_attribution.setter
    def version_attribution(self, version_attribution):
        """Sets the version_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.

        版本属性

        :param version_attribution: The version_attribution of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type version_attribution: str
        """
        self._version_attribution = version_attribution

    @property
    def icon_url(self):
        """Gets the icon_url of this PageInfoBusinessTypeDefinitionVOPluginsList.

        图标URL

        :return: The icon_url of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this PageInfoBusinessTypeDefinitionVOPluginsList.

        图标URL

        :param icon_url: The icon_url of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type icon_url: str
        """
        self._icon_url = icon_url

    @property
    def multi_step_editable(self):
        """Gets the multi_step_editable of this PageInfoBusinessTypeDefinitionVOPluginsList.

        可编辑

        :return: The multi_step_editable of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: int
        """
        return self._multi_step_editable

    @multi_step_editable.setter
    def multi_step_editable(self, multi_step_editable):
        """Sets the multi_step_editable of this PageInfoBusinessTypeDefinitionVOPluginsList.

        可编辑

        :param multi_step_editable: The multi_step_editable of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type multi_step_editable: int
        """
        self._multi_step_editable = multi_step_editable

    @property
    def location(self):
        """Gets the location of this PageInfoBusinessTypeDefinitionVOPluginsList.

        地址

        :return: The location of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PageInfoBusinessTypeDefinitionVOPluginsList.

        地址

        :param location: The location of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type location: str
        """
        self._location = location

    @property
    def publisher_unique_id(self):
        """Gets the publisher_unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.

        发布商ID

        :return: The publisher_unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._publisher_unique_id

    @publisher_unique_id.setter
    def publisher_unique_id(self, publisher_unique_id):
        """Sets the publisher_unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.

        发布商ID

        :param publisher_unique_id: The publisher_unique_id of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :type publisher_unique_id: str
        """
        self._publisher_unique_id = publisher_unique_id

    @property
    def manifest_version(self):
        """Gets the manifest_version of this PageInfoBusinessTypeDefinitionVOPluginsList.

        版本

        :return: The manifest_version of this PageInfoBusinessTypeDefinitionVOPluginsList.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        """Sets the manifest_version of this PageInfoBusinessTypeDefinitionVOPluginsList.

        版本

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
