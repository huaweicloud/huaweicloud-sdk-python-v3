# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResumePluginExtensionsRequestBody:

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
        'db_list': 'list[str]',
        'extension_name': 'str',
        'extension_action': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'db_list': 'db_list',
        'extension_name': 'extension_name',
        'extension_action': 'extension_action'
    }

    def __init__(self, plugin_name=None, db_list=None, extension_name=None, extension_action=None):
        r"""ResumePluginExtensionsRequestBody

        The model defined in huaweicloud sdk

        :param plugin_name: 插件名称
        :type plugin_name: str
        :param db_list: 数据库列表
        :type db_list: list[str]
        :param extension_name: 拓展模块名称
        :type extension_name: str
        :param extension_action: 扩展开关。on表示开启，off表示关闭。
        :type extension_action: str
        """
        
        

        self._plugin_name = None
        self._db_list = None
        self._extension_name = None
        self._extension_action = None
        self.discriminator = None

        self.plugin_name = plugin_name
        self.db_list = db_list
        self.extension_name = extension_name
        self.extension_action = extension_action

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this ResumePluginExtensionsRequestBody.

        插件名称

        :return: The plugin_name of this ResumePluginExtensionsRequestBody.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this ResumePluginExtensionsRequestBody.

        插件名称

        :param plugin_name: The plugin_name of this ResumePluginExtensionsRequestBody.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def db_list(self):
        r"""Gets the db_list of this ResumePluginExtensionsRequestBody.

        数据库列表

        :return: The db_list of this ResumePluginExtensionsRequestBody.
        :rtype: list[str]
        """
        return self._db_list

    @db_list.setter
    def db_list(self, db_list):
        r"""Sets the db_list of this ResumePluginExtensionsRequestBody.

        数据库列表

        :param db_list: The db_list of this ResumePluginExtensionsRequestBody.
        :type db_list: list[str]
        """
        self._db_list = db_list

    @property
    def extension_name(self):
        r"""Gets the extension_name of this ResumePluginExtensionsRequestBody.

        拓展模块名称

        :return: The extension_name of this ResumePluginExtensionsRequestBody.
        :rtype: str
        """
        return self._extension_name

    @extension_name.setter
    def extension_name(self, extension_name):
        r"""Sets the extension_name of this ResumePluginExtensionsRequestBody.

        拓展模块名称

        :param extension_name: The extension_name of this ResumePluginExtensionsRequestBody.
        :type extension_name: str
        """
        self._extension_name = extension_name

    @property
    def extension_action(self):
        r"""Gets the extension_action of this ResumePluginExtensionsRequestBody.

        扩展开关。on表示开启，off表示关闭。

        :return: The extension_action of this ResumePluginExtensionsRequestBody.
        :rtype: str
        """
        return self._extension_action

    @extension_action.setter
    def extension_action(self, extension_action):
        r"""Sets the extension_action of this ResumePluginExtensionsRequestBody.

        扩展开关。on表示开启，off表示关闭。

        :param extension_action: The extension_action of this ResumePluginExtensionsRequestBody.
        :type extension_action: str
        """
        self._extension_action = extension_action

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
        if not isinstance(other, ResumePluginExtensionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
