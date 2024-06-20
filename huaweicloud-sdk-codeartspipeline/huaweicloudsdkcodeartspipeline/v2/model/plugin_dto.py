# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginDTO:

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
        'icon_url': 'str',
        'runtime_attribution': 'str',
        'plugin_name': 'str',
        'display_name': 'str',
        'business_type': 'str',
        'business_type_display_name': 'str',
        'description': 'str',
        'is_private': 'int',
        'region': 'str',
        'maintainers': 'str',
        'version': 'str',
        'version_description': 'str',
        'execution_info': 'PluginDTOExecutionInfo',
        'input_info': 'list[PluginDTOInputInfo]'
    }

    attribute_map = {
        'unique_id': 'unique_id',
        'icon_url': 'icon_url',
        'runtime_attribution': 'runtime_attribution',
        'plugin_name': 'plugin_name',
        'display_name': 'display_name',
        'business_type': 'business_type',
        'business_type_display_name': 'business_type_display_name',
        'description': 'description',
        'is_private': 'is_private',
        'region': 'region',
        'maintainers': 'maintainers',
        'version': 'version',
        'version_description': 'version_description',
        'execution_info': 'execution_info',
        'input_info': 'input_info'
    }

    def __init__(self, unique_id=None, icon_url=None, runtime_attribution=None, plugin_name=None, display_name=None, business_type=None, business_type_display_name=None, description=None, is_private=None, region=None, maintainers=None, version=None, version_description=None, execution_info=None, input_info=None):
        """PluginDTO

        The model defined in huaweicloud sdk

        :param unique_id: 唯一ID
        :type unique_id: str
        :param icon_url: 图标URL
        :type icon_url: str
        :param runtime_attribution: 运行属性
        :type runtime_attribution: str
        :param plugin_name: 插件名
        :type plugin_name: str
        :param display_name: 展示名
        :type display_name: str
        :param business_type: 业务类型
        :type business_type: str
        :param business_type_display_name: 业务类型展示名
        :type business_type_display_name: str
        :param description: 描述
        :type description: str
        :param is_private: 是否私有
        :type is_private: int
        :param region: 局点
        :type region: str
        :param maintainers: 维护者
        :type maintainers: str
        :param version: 版本号
        :type version: str
        :param version_description: 版本号说明
        :type version_description: str
        :param execution_info: 
        :type execution_info: :class:`huaweicloudsdkcodeartspipeline.v2.PluginDTOExecutionInfo`
        :param input_info: 输入信息
        :type input_info: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginDTOInputInfo`]
        """
        
        

        self._unique_id = None
        self._icon_url = None
        self._runtime_attribution = None
        self._plugin_name = None
        self._display_name = None
        self._business_type = None
        self._business_type_display_name = None
        self._description = None
        self._is_private = None
        self._region = None
        self._maintainers = None
        self._version = None
        self._version_description = None
        self._execution_info = None
        self._input_info = None
        self.discriminator = None

        if unique_id is not None:
            self.unique_id = unique_id
        if icon_url is not None:
            self.icon_url = icon_url
        self.runtime_attribution = runtime_attribution
        self.plugin_name = plugin_name
        self.display_name = display_name
        self.business_type = business_type
        self.business_type_display_name = business_type_display_name
        self.description = description
        if is_private is not None:
            self.is_private = is_private
        if region is not None:
            self.region = region
        if maintainers is not None:
            self.maintainers = maintainers
        self.version = version
        if version_description is not None:
            self.version_description = version_description
        self.execution_info = execution_info
        if input_info is not None:
            self.input_info = input_info

    @property
    def unique_id(self):
        """Gets the unique_id of this PluginDTO.

        唯一ID

        :return: The unique_id of this PluginDTO.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this PluginDTO.

        唯一ID

        :param unique_id: The unique_id of this PluginDTO.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def icon_url(self):
        """Gets the icon_url of this PluginDTO.

        图标URL

        :return: The icon_url of this PluginDTO.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this PluginDTO.

        图标URL

        :param icon_url: The icon_url of this PluginDTO.
        :type icon_url: str
        """
        self._icon_url = icon_url

    @property
    def runtime_attribution(self):
        """Gets the runtime_attribution of this PluginDTO.

        运行属性

        :return: The runtime_attribution of this PluginDTO.
        :rtype: str
        """
        return self._runtime_attribution

    @runtime_attribution.setter
    def runtime_attribution(self, runtime_attribution):
        """Sets the runtime_attribution of this PluginDTO.

        运行属性

        :param runtime_attribution: The runtime_attribution of this PluginDTO.
        :type runtime_attribution: str
        """
        self._runtime_attribution = runtime_attribution

    @property
    def plugin_name(self):
        """Gets the plugin_name of this PluginDTO.

        插件名

        :return: The plugin_name of this PluginDTO.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this PluginDTO.

        插件名

        :param plugin_name: The plugin_name of this PluginDTO.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def display_name(self):
        """Gets the display_name of this PluginDTO.

        展示名

        :return: The display_name of this PluginDTO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PluginDTO.

        展示名

        :param display_name: The display_name of this PluginDTO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def business_type(self):
        """Gets the business_type of this PluginDTO.

        业务类型

        :return: The business_type of this PluginDTO.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this PluginDTO.

        业务类型

        :param business_type: The business_type of this PluginDTO.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def business_type_display_name(self):
        """Gets the business_type_display_name of this PluginDTO.

        业务类型展示名

        :return: The business_type_display_name of this PluginDTO.
        :rtype: str
        """
        return self._business_type_display_name

    @business_type_display_name.setter
    def business_type_display_name(self, business_type_display_name):
        """Sets the business_type_display_name of this PluginDTO.

        业务类型展示名

        :param business_type_display_name: The business_type_display_name of this PluginDTO.
        :type business_type_display_name: str
        """
        self._business_type_display_name = business_type_display_name

    @property
    def description(self):
        """Gets the description of this PluginDTO.

        描述

        :return: The description of this PluginDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PluginDTO.

        描述

        :param description: The description of this PluginDTO.
        :type description: str
        """
        self._description = description

    @property
    def is_private(self):
        """Gets the is_private of this PluginDTO.

        是否私有

        :return: The is_private of this PluginDTO.
        :rtype: int
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this PluginDTO.

        是否私有

        :param is_private: The is_private of this PluginDTO.
        :type is_private: int
        """
        self._is_private = is_private

    @property
    def region(self):
        """Gets the region of this PluginDTO.

        局点

        :return: The region of this PluginDTO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this PluginDTO.

        局点

        :param region: The region of this PluginDTO.
        :type region: str
        """
        self._region = region

    @property
    def maintainers(self):
        """Gets the maintainers of this PluginDTO.

        维护者

        :return: The maintainers of this PluginDTO.
        :rtype: str
        """
        return self._maintainers

    @maintainers.setter
    def maintainers(self, maintainers):
        """Sets the maintainers of this PluginDTO.

        维护者

        :param maintainers: The maintainers of this PluginDTO.
        :type maintainers: str
        """
        self._maintainers = maintainers

    @property
    def version(self):
        """Gets the version of this PluginDTO.

        版本号

        :return: The version of this PluginDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PluginDTO.

        版本号

        :param version: The version of this PluginDTO.
        :type version: str
        """
        self._version = version

    @property
    def version_description(self):
        """Gets the version_description of this PluginDTO.

        版本号说明

        :return: The version_description of this PluginDTO.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        """Sets the version_description of this PluginDTO.

        版本号说明

        :param version_description: The version_description of this PluginDTO.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def execution_info(self):
        """Gets the execution_info of this PluginDTO.

        :return: The execution_info of this PluginDTO.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PluginDTOExecutionInfo`
        """
        return self._execution_info

    @execution_info.setter
    def execution_info(self, execution_info):
        """Sets the execution_info of this PluginDTO.

        :param execution_info: The execution_info of this PluginDTO.
        :type execution_info: :class:`huaweicloudsdkcodeartspipeline.v2.PluginDTOExecutionInfo`
        """
        self._execution_info = execution_info

    @property
    def input_info(self):
        """Gets the input_info of this PluginDTO.

        输入信息

        :return: The input_info of this PluginDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginDTOInputInfo`]
        """
        return self._input_info

    @input_info.setter
    def input_info(self, input_info):
        """Sets the input_info of this PluginDTO.

        输入信息

        :param input_info: The input_info of this PluginDTO.
        :type input_info: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginDTOInputInfo`]
        """
        self._input_info = input_info

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
        if not isinstance(other, PluginDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
