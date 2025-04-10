# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginExtensionsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'plugin_name': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'plugin_name': 'plugin_name'
    }

    def __init__(self, db_name=None, plugin_name=None):
        r"""ListPluginExtensionsRequestBody

        The model defined in huaweicloud sdk

        :param db_name: 数据库名称
        :type db_name: str
        :param plugin_name: 插件名称
        :type plugin_name: str
        """
        
        

        self._db_name = None
        self._plugin_name = None
        self.discriminator = None

        self.db_name = db_name
        self.plugin_name = plugin_name

    @property
    def db_name(self):
        r"""Gets the db_name of this ListPluginExtensionsRequestBody.

        数据库名称

        :return: The db_name of this ListPluginExtensionsRequestBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListPluginExtensionsRequestBody.

        数据库名称

        :param db_name: The db_name of this ListPluginExtensionsRequestBody.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this ListPluginExtensionsRequestBody.

        插件名称

        :return: The plugin_name of this ListPluginExtensionsRequestBody.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this ListPluginExtensionsRequestBody.

        插件名称

        :param plugin_name: The plugin_name of this ListPluginExtensionsRequestBody.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

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
        if not isinstance(other, ListPluginExtensionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
