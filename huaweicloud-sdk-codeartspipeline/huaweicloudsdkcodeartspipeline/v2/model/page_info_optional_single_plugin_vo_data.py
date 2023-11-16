# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageInfoOptionalSinglePluginVOData:

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
        'display_name': 'str',
        'plugin_attribution': 'str',
        'icon_url': 'str',
        'description': 'str',
        'publisher_id': 'str',
        'manifest_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'display_name',
        'plugin_attribution': 'plugin_attribution',
        'icon_url': 'icon_url',
        'description': 'description',
        'publisher_id': 'publisher_id',
        'manifest_version': 'manifest_version'
    }

    def __init__(self, name=None, display_name=None, plugin_attribution=None, icon_url=None, description=None, publisher_id=None, manifest_version=None):
        """PageInfoOptionalSinglePluginVOData

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param display_name: 展示名
        :type display_name: str
        :param plugin_attribution: 属性
        :type plugin_attribution: str
        :param icon_url: 图标URL
        :type icon_url: str
        :param description: 描述
        :type description: str
        :param publisher_id: 发布商ID
        :type publisher_id: str
        :param manifest_version: 版本
        :type manifest_version: str
        """
        
        

        self._name = None
        self._display_name = None
        self._plugin_attribution = None
        self._icon_url = None
        self._description = None
        self._publisher_id = None
        self._manifest_version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if plugin_attribution is not None:
            self.plugin_attribution = plugin_attribution
        if icon_url is not None:
            self.icon_url = icon_url
        if description is not None:
            self.description = description
        if publisher_id is not None:
            self.publisher_id = publisher_id
        if manifest_version is not None:
            self.manifest_version = manifest_version

    @property
    def name(self):
        """Gets the name of this PageInfoOptionalSinglePluginVOData.

        名称

        :return: The name of this PageInfoOptionalSinglePluginVOData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PageInfoOptionalSinglePluginVOData.

        名称

        :param name: The name of this PageInfoOptionalSinglePluginVOData.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this PageInfoOptionalSinglePluginVOData.

        展示名

        :return: The display_name of this PageInfoOptionalSinglePluginVOData.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PageInfoOptionalSinglePluginVOData.

        展示名

        :param display_name: The display_name of this PageInfoOptionalSinglePluginVOData.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def plugin_attribution(self):
        """Gets the plugin_attribution of this PageInfoOptionalSinglePluginVOData.

        属性

        :return: The plugin_attribution of this PageInfoOptionalSinglePluginVOData.
        :rtype: str
        """
        return self._plugin_attribution

    @plugin_attribution.setter
    def plugin_attribution(self, plugin_attribution):
        """Sets the plugin_attribution of this PageInfoOptionalSinglePluginVOData.

        属性

        :param plugin_attribution: The plugin_attribution of this PageInfoOptionalSinglePluginVOData.
        :type plugin_attribution: str
        """
        self._plugin_attribution = plugin_attribution

    @property
    def icon_url(self):
        """Gets the icon_url of this PageInfoOptionalSinglePluginVOData.

        图标URL

        :return: The icon_url of this PageInfoOptionalSinglePluginVOData.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this PageInfoOptionalSinglePluginVOData.

        图标URL

        :param icon_url: The icon_url of this PageInfoOptionalSinglePluginVOData.
        :type icon_url: str
        """
        self._icon_url = icon_url

    @property
    def description(self):
        """Gets the description of this PageInfoOptionalSinglePluginVOData.

        描述

        :return: The description of this PageInfoOptionalSinglePluginVOData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PageInfoOptionalSinglePluginVOData.

        描述

        :param description: The description of this PageInfoOptionalSinglePluginVOData.
        :type description: str
        """
        self._description = description

    @property
    def publisher_id(self):
        """Gets the publisher_id of this PageInfoOptionalSinglePluginVOData.

        发布商ID

        :return: The publisher_id of this PageInfoOptionalSinglePluginVOData.
        :rtype: str
        """
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, publisher_id):
        """Sets the publisher_id of this PageInfoOptionalSinglePluginVOData.

        发布商ID

        :param publisher_id: The publisher_id of this PageInfoOptionalSinglePluginVOData.
        :type publisher_id: str
        """
        self._publisher_id = publisher_id

    @property
    def manifest_version(self):
        """Gets the manifest_version of this PageInfoOptionalSinglePluginVOData.

        版本

        :return: The manifest_version of this PageInfoOptionalSinglePluginVOData.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        """Sets the manifest_version of this PageInfoOptionalSinglePluginVOData.

        版本

        :param manifest_version: The manifest_version of this PageInfoOptionalSinglePluginVOData.
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
        if not isinstance(other, PageInfoOptionalSinglePluginVOData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
