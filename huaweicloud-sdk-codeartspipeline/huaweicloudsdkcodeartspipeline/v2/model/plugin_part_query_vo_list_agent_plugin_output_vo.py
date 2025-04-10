# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginPartQueryVOListAgentPluginOutputVO:

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
        'data': 'list[PluginPartQueryVOListAgentPluginOutputVOData]'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'display_name': 'display_name',
        'data': 'data'
    }

    def __init__(self, plugin_name=None, display_name=None, data=None):
        r"""PluginPartQueryVOListAgentPluginOutputVO

        The model defined in huaweicloud sdk

        :param plugin_name: 插件名
        :type plugin_name: str
        :param display_name: 展示名
        :type display_name: str
        :param data: 结果集
        :type data: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginPartQueryVOListAgentPluginOutputVOData`]
        """
        
        

        self._plugin_name = None
        self._display_name = None
        self._data = None
        self.discriminator = None

        if plugin_name is not None:
            self.plugin_name = plugin_name
        if display_name is not None:
            self.display_name = display_name
        if data is not None:
            self.data = data

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this PluginPartQueryVOListAgentPluginOutputVO.

        插件名

        :return: The plugin_name of this PluginPartQueryVOListAgentPluginOutputVO.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this PluginPartQueryVOListAgentPluginOutputVO.

        插件名

        :param plugin_name: The plugin_name of this PluginPartQueryVOListAgentPluginOutputVO.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def display_name(self):
        r"""Gets the display_name of this PluginPartQueryVOListAgentPluginOutputVO.

        展示名

        :return: The display_name of this PluginPartQueryVOListAgentPluginOutputVO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this PluginPartQueryVOListAgentPluginOutputVO.

        展示名

        :param display_name: The display_name of this PluginPartQueryVOListAgentPluginOutputVO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def data(self):
        r"""Gets the data of this PluginPartQueryVOListAgentPluginOutputVO.

        结果集

        :return: The data of this PluginPartQueryVOListAgentPluginOutputVO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginPartQueryVOListAgentPluginOutputVOData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this PluginPartQueryVOListAgentPluginOutputVO.

        结果集

        :param data: The data of this PluginPartQueryVOListAgentPluginOutputVO.
        :type data: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginPartQueryVOListAgentPluginOutputVOData`]
        """
        self._data = data

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
        if not isinstance(other, PluginPartQueryVOListAgentPluginOutputVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
