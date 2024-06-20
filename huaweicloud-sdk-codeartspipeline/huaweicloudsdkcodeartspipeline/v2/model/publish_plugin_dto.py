# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishPluginDTO:

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
        'version': 'str',
        'publisher_unique_id': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'version': 'version',
        'publisher_unique_id': 'publisher_unique_id'
    }

    def __init__(self, plugin_name=None, version=None, publisher_unique_id=None):
        """PublishPluginDTO

        The model defined in huaweicloud sdk

        :param plugin_name: 插件名
        :type plugin_name: str
        :param version: 版本
        :type version: str
        :param publisher_unique_id: 发布商ID
        :type publisher_unique_id: str
        """
        
        

        self._plugin_name = None
        self._version = None
        self._publisher_unique_id = None
        self.discriminator = None

        self.plugin_name = plugin_name
        self.version = version
        self.publisher_unique_id = publisher_unique_id

    @property
    def plugin_name(self):
        """Gets the plugin_name of this PublishPluginDTO.

        插件名

        :return: The plugin_name of this PublishPluginDTO.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this PublishPluginDTO.

        插件名

        :param plugin_name: The plugin_name of this PublishPluginDTO.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def version(self):
        """Gets the version of this PublishPluginDTO.

        版本

        :return: The version of this PublishPluginDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PublishPluginDTO.

        版本

        :param version: The version of this PublishPluginDTO.
        :type version: str
        """
        self._version = version

    @property
    def publisher_unique_id(self):
        """Gets the publisher_unique_id of this PublishPluginDTO.

        发布商ID

        :return: The publisher_unique_id of this PublishPluginDTO.
        :rtype: str
        """
        return self._publisher_unique_id

    @publisher_unique_id.setter
    def publisher_unique_id(self, publisher_unique_id):
        """Sets the publisher_unique_id of this PublishPluginDTO.

        发布商ID

        :param publisher_unique_id: The publisher_unique_id of this PublishPluginDTO.
        :type publisher_unique_id: str
        """
        self._publisher_unique_id = publisher_unique_id

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
        if not isinstance(other, PublishPluginDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
