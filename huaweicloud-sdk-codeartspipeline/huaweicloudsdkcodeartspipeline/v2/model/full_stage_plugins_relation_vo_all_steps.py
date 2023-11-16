# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullStagePluginsRelationVOAllSteps:

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
        'version': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'display_name': 'display_name',
        'version': 'version'
    }

    def __init__(self, plugin_name=None, display_name=None, version=None):
        """FullStagePluginsRelationVOAllSteps

        The model defined in huaweicloud sdk

        :param plugin_name: 插件名
        :type plugin_name: str
        :param display_name: 展示名
        :type display_name: str
        :param version: 版本
        :type version: str
        """
        
        

        self._plugin_name = None
        self._display_name = None
        self._version = None
        self.discriminator = None

        if plugin_name is not None:
            self.plugin_name = plugin_name
        if display_name is not None:
            self.display_name = display_name
        if version is not None:
            self.version = version

    @property
    def plugin_name(self):
        """Gets the plugin_name of this FullStagePluginsRelationVOAllSteps.

        插件名

        :return: The plugin_name of this FullStagePluginsRelationVOAllSteps.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this FullStagePluginsRelationVOAllSteps.

        插件名

        :param plugin_name: The plugin_name of this FullStagePluginsRelationVOAllSteps.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def display_name(self):
        """Gets the display_name of this FullStagePluginsRelationVOAllSteps.

        展示名

        :return: The display_name of this FullStagePluginsRelationVOAllSteps.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FullStagePluginsRelationVOAllSteps.

        展示名

        :param display_name: The display_name of this FullStagePluginsRelationVOAllSteps.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def version(self):
        """Gets the version of this FullStagePluginsRelationVOAllSteps.

        版本

        :return: The version of this FullStagePluginsRelationVOAllSteps.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FullStagePluginsRelationVOAllSteps.

        版本

        :param version: The version of this FullStagePluginsRelationVOAllSteps.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, FullStagePluginsRelationVOAllSteps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
