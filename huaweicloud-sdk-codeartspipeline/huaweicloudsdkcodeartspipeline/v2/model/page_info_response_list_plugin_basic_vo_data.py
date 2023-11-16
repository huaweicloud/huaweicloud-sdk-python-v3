# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageInfoResponseListPluginBasicVOData:

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
        'active': 'int'
    }

    attribute_map = {
        'plugin_name': 'pluginName',
        'display_name': 'displayName',
        'version': 'version',
        'version_description': 'versionDescription',
        'description': 'description',
        'version_attribution': 'versionAttribution',
        'unique_id': 'uniqueId',
        'op_user': 'opUser',
        'op_time': 'opTime',
        'plugin_composition_type': 'pluginCompositionType',
        'plugin_attribution': 'pluginAttribution',
        'workspace_id': 'workspaceId',
        'business_type': 'businessType',
        'business_type_display_name': 'businessTypeDisplayName',
        'maintainers': 'maintainers',
        'icon_url': 'iconUrl',
        'refer_count': 'referCount',
        'usage_count': 'usageCount',
        'runtime_attribution': 'runtimeAttribution',
        'active': 'active'
    }

    def __init__(self, plugin_name=None, display_name=None, version=None, version_description=None, description=None, version_attribution=None, unique_id=None, op_user=None, op_time=None, plugin_composition_type=None, plugin_attribution=None, workspace_id=None, business_type=None, business_type_display_name=None, maintainers=None, icon_url=None, refer_count=None, usage_count=None, runtime_attribution=None, active=None):
        """PageInfoResponseListPluginBasicVOData

        The model defined in huaweicloud sdk

        :param plugin_name: 插件名
        :type plugin_name: str
        :param display_name: 展示名
        :type display_name: str
        :param version: 版本
        :type version: str
        :param version_description: 版本说明
        :type version_description: str
        :param description: 描述
        :type description: str
        :param version_attribution: 版本属性
        :type version_attribution: str
        :param unique_id: 唯一ID
        :type unique_id: str
        :param op_user: 操作人
        :type op_user: str
        :param op_time: 操作时间
        :type op_time: str
        :param plugin_composition_type: 组合类型
        :type plugin_composition_type: str
        :param plugin_attribution: 属性
        :type plugin_attribution: str
        :param workspace_id: 租户ID
        :type workspace_id: str
        :param business_type: 业务类型
        :type business_type: str
        :param business_type_display_name: 业务类型展示名
        :type business_type_display_name: str
        :param maintainers: 维护者
        :type maintainers: str
        :param icon_url: 图标URL
        :type icon_url: str
        :param refer_count: 引用次数
        :type refer_count: int
        :param usage_count: 使用次数
        :type usage_count: int
        :param runtime_attribution: 运行属性
        :type runtime_attribution: str
        :param active: 是否激活
        :type active: int
        """
        
        

        self._plugin_name = None
        self._display_name = None
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
        self.discriminator = None

        if plugin_name is not None:
            self.plugin_name = plugin_name
        if display_name is not None:
            self.display_name = display_name
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

    @property
    def plugin_name(self):
        """Gets the plugin_name of this PageInfoResponseListPluginBasicVOData.

        插件名

        :return: The plugin_name of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this PageInfoResponseListPluginBasicVOData.

        插件名

        :param plugin_name: The plugin_name of this PageInfoResponseListPluginBasicVOData.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def display_name(self):
        """Gets the display_name of this PageInfoResponseListPluginBasicVOData.

        展示名

        :return: The display_name of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PageInfoResponseListPluginBasicVOData.

        展示名

        :param display_name: The display_name of this PageInfoResponseListPluginBasicVOData.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def version(self):
        """Gets the version of this PageInfoResponseListPluginBasicVOData.

        版本

        :return: The version of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PageInfoResponseListPluginBasicVOData.

        版本

        :param version: The version of this PageInfoResponseListPluginBasicVOData.
        :type version: str
        """
        self._version = version

    @property
    def version_description(self):
        """Gets the version_description of this PageInfoResponseListPluginBasicVOData.

        版本说明

        :return: The version_description of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        """Sets the version_description of this PageInfoResponseListPluginBasicVOData.

        版本说明

        :param version_description: The version_description of this PageInfoResponseListPluginBasicVOData.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def description(self):
        """Gets the description of this PageInfoResponseListPluginBasicVOData.

        描述

        :return: The description of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PageInfoResponseListPluginBasicVOData.

        描述

        :param description: The description of this PageInfoResponseListPluginBasicVOData.
        :type description: str
        """
        self._description = description

    @property
    def version_attribution(self):
        """Gets the version_attribution of this PageInfoResponseListPluginBasicVOData.

        版本属性

        :return: The version_attribution of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._version_attribution

    @version_attribution.setter
    def version_attribution(self, version_attribution):
        """Sets the version_attribution of this PageInfoResponseListPluginBasicVOData.

        版本属性

        :param version_attribution: The version_attribution of this PageInfoResponseListPluginBasicVOData.
        :type version_attribution: str
        """
        self._version_attribution = version_attribution

    @property
    def unique_id(self):
        """Gets the unique_id of this PageInfoResponseListPluginBasicVOData.

        唯一ID

        :return: The unique_id of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this PageInfoResponseListPluginBasicVOData.

        唯一ID

        :param unique_id: The unique_id of this PageInfoResponseListPluginBasicVOData.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def op_user(self):
        """Gets the op_user of this PageInfoResponseListPluginBasicVOData.

        操作人

        :return: The op_user of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._op_user

    @op_user.setter
    def op_user(self, op_user):
        """Sets the op_user of this PageInfoResponseListPluginBasicVOData.

        操作人

        :param op_user: The op_user of this PageInfoResponseListPluginBasicVOData.
        :type op_user: str
        """
        self._op_user = op_user

    @property
    def op_time(self):
        """Gets the op_time of this PageInfoResponseListPluginBasicVOData.

        操作时间

        :return: The op_time of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._op_time

    @op_time.setter
    def op_time(self, op_time):
        """Sets the op_time of this PageInfoResponseListPluginBasicVOData.

        操作时间

        :param op_time: The op_time of this PageInfoResponseListPluginBasicVOData.
        :type op_time: str
        """
        self._op_time = op_time

    @property
    def plugin_composition_type(self):
        """Gets the plugin_composition_type of this PageInfoResponseListPluginBasicVOData.

        组合类型

        :return: The plugin_composition_type of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._plugin_composition_type

    @plugin_composition_type.setter
    def plugin_composition_type(self, plugin_composition_type):
        """Sets the plugin_composition_type of this PageInfoResponseListPluginBasicVOData.

        组合类型

        :param plugin_composition_type: The plugin_composition_type of this PageInfoResponseListPluginBasicVOData.
        :type plugin_composition_type: str
        """
        self._plugin_composition_type = plugin_composition_type

    @property
    def plugin_attribution(self):
        """Gets the plugin_attribution of this PageInfoResponseListPluginBasicVOData.

        属性

        :return: The plugin_attribution of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._plugin_attribution

    @plugin_attribution.setter
    def plugin_attribution(self, plugin_attribution):
        """Sets the plugin_attribution of this PageInfoResponseListPluginBasicVOData.

        属性

        :param plugin_attribution: The plugin_attribution of this PageInfoResponseListPluginBasicVOData.
        :type plugin_attribution: str
        """
        self._plugin_attribution = plugin_attribution

    @property
    def workspace_id(self):
        """Gets the workspace_id of this PageInfoResponseListPluginBasicVOData.

        租户ID

        :return: The workspace_id of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this PageInfoResponseListPluginBasicVOData.

        租户ID

        :param workspace_id: The workspace_id of this PageInfoResponseListPluginBasicVOData.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def business_type(self):
        """Gets the business_type of this PageInfoResponseListPluginBasicVOData.

        业务类型

        :return: The business_type of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this PageInfoResponseListPluginBasicVOData.

        业务类型

        :param business_type: The business_type of this PageInfoResponseListPluginBasicVOData.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def business_type_display_name(self):
        """Gets the business_type_display_name of this PageInfoResponseListPluginBasicVOData.

        业务类型展示名

        :return: The business_type_display_name of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._business_type_display_name

    @business_type_display_name.setter
    def business_type_display_name(self, business_type_display_name):
        """Sets the business_type_display_name of this PageInfoResponseListPluginBasicVOData.

        业务类型展示名

        :param business_type_display_name: The business_type_display_name of this PageInfoResponseListPluginBasicVOData.
        :type business_type_display_name: str
        """
        self._business_type_display_name = business_type_display_name

    @property
    def maintainers(self):
        """Gets the maintainers of this PageInfoResponseListPluginBasicVOData.

        维护者

        :return: The maintainers of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._maintainers

    @maintainers.setter
    def maintainers(self, maintainers):
        """Sets the maintainers of this PageInfoResponseListPluginBasicVOData.

        维护者

        :param maintainers: The maintainers of this PageInfoResponseListPluginBasicVOData.
        :type maintainers: str
        """
        self._maintainers = maintainers

    @property
    def icon_url(self):
        """Gets the icon_url of this PageInfoResponseListPluginBasicVOData.

        图标URL

        :return: The icon_url of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this PageInfoResponseListPluginBasicVOData.

        图标URL

        :param icon_url: The icon_url of this PageInfoResponseListPluginBasicVOData.
        :type icon_url: str
        """
        self._icon_url = icon_url

    @property
    def refer_count(self):
        """Gets the refer_count of this PageInfoResponseListPluginBasicVOData.

        引用次数

        :return: The refer_count of this PageInfoResponseListPluginBasicVOData.
        :rtype: int
        """
        return self._refer_count

    @refer_count.setter
    def refer_count(self, refer_count):
        """Sets the refer_count of this PageInfoResponseListPluginBasicVOData.

        引用次数

        :param refer_count: The refer_count of this PageInfoResponseListPluginBasicVOData.
        :type refer_count: int
        """
        self._refer_count = refer_count

    @property
    def usage_count(self):
        """Gets the usage_count of this PageInfoResponseListPluginBasicVOData.

        使用次数

        :return: The usage_count of this PageInfoResponseListPluginBasicVOData.
        :rtype: int
        """
        return self._usage_count

    @usage_count.setter
    def usage_count(self, usage_count):
        """Sets the usage_count of this PageInfoResponseListPluginBasicVOData.

        使用次数

        :param usage_count: The usage_count of this PageInfoResponseListPluginBasicVOData.
        :type usage_count: int
        """
        self._usage_count = usage_count

    @property
    def runtime_attribution(self):
        """Gets the runtime_attribution of this PageInfoResponseListPluginBasicVOData.

        运行属性

        :return: The runtime_attribution of this PageInfoResponseListPluginBasicVOData.
        :rtype: str
        """
        return self._runtime_attribution

    @runtime_attribution.setter
    def runtime_attribution(self, runtime_attribution):
        """Sets the runtime_attribution of this PageInfoResponseListPluginBasicVOData.

        运行属性

        :param runtime_attribution: The runtime_attribution of this PageInfoResponseListPluginBasicVOData.
        :type runtime_attribution: str
        """
        self._runtime_attribution = runtime_attribution

    @property
    def active(self):
        """Gets the active of this PageInfoResponseListPluginBasicVOData.

        是否激活

        :return: The active of this PageInfoResponseListPluginBasicVOData.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PageInfoResponseListPluginBasicVOData.

        是否激活

        :param active: The active of this PageInfoResponseListPluginBasicVOData.
        :type active: int
        """
        self._active = active

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
        if not isinstance(other, PageInfoResponseListPluginBasicVOData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
