# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginPartQueryVOListAgentPluginOutputVOData:

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
        'plugin_name': 'str',
        'version': 'str',
        'workspace_id': 'str',
        'output_key': 'str',
        'output_value': 'str'
    }

    attribute_map = {
        'unique_id': 'unique_id',
        'plugin_name': 'plugin_name',
        'version': 'version',
        'workspace_id': 'workspace_id',
        'output_key': 'output_key',
        'output_value': 'output_value'
    }

    def __init__(self, unique_id=None, plugin_name=None, version=None, workspace_id=None, output_key=None, output_value=None):
        r"""PluginPartQueryVOListAgentPluginOutputVOData

        The model defined in huaweicloud sdk

        :param unique_id: 唯一ID
        :type unique_id: str
        :param plugin_name: 插件名
        :type plugin_name: str
        :param version: 版本
        :type version: str
        :param workspace_id: 租户ID
        :type workspace_id: str
        :param output_key: 名称
        :type output_key: str
        :param output_value: 值
        :type output_value: str
        """
        
        

        self._unique_id = None
        self._plugin_name = None
        self._version = None
        self._workspace_id = None
        self._output_key = None
        self._output_value = None
        self.discriminator = None

        if unique_id is not None:
            self.unique_id = unique_id
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if version is not None:
            self.version = version
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if output_key is not None:
            self.output_key = output_key
        if output_value is not None:
            self.output_value = output_value

    @property
    def unique_id(self):
        r"""Gets the unique_id of this PluginPartQueryVOListAgentPluginOutputVOData.

        唯一ID

        :return: The unique_id of this PluginPartQueryVOListAgentPluginOutputVOData.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        r"""Sets the unique_id of this PluginPartQueryVOListAgentPluginOutputVOData.

        唯一ID

        :param unique_id: The unique_id of this PluginPartQueryVOListAgentPluginOutputVOData.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this PluginPartQueryVOListAgentPluginOutputVOData.

        插件名

        :return: The plugin_name of this PluginPartQueryVOListAgentPluginOutputVOData.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this PluginPartQueryVOListAgentPluginOutputVOData.

        插件名

        :param plugin_name: The plugin_name of this PluginPartQueryVOListAgentPluginOutputVOData.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def version(self):
        r"""Gets the version of this PluginPartQueryVOListAgentPluginOutputVOData.

        版本

        :return: The version of this PluginPartQueryVOListAgentPluginOutputVOData.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PluginPartQueryVOListAgentPluginOutputVOData.

        版本

        :param version: The version of this PluginPartQueryVOListAgentPluginOutputVOData.
        :type version: str
        """
        self._version = version

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this PluginPartQueryVOListAgentPluginOutputVOData.

        租户ID

        :return: The workspace_id of this PluginPartQueryVOListAgentPluginOutputVOData.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this PluginPartQueryVOListAgentPluginOutputVOData.

        租户ID

        :param workspace_id: The workspace_id of this PluginPartQueryVOListAgentPluginOutputVOData.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def output_key(self):
        r"""Gets the output_key of this PluginPartQueryVOListAgentPluginOutputVOData.

        名称

        :return: The output_key of this PluginPartQueryVOListAgentPluginOutputVOData.
        :rtype: str
        """
        return self._output_key

    @output_key.setter
    def output_key(self, output_key):
        r"""Sets the output_key of this PluginPartQueryVOListAgentPluginOutputVOData.

        名称

        :param output_key: The output_key of this PluginPartQueryVOListAgentPluginOutputVOData.
        :type output_key: str
        """
        self._output_key = output_key

    @property
    def output_value(self):
        r"""Gets the output_value of this PluginPartQueryVOListAgentPluginOutputVOData.

        值

        :return: The output_value of this PluginPartQueryVOListAgentPluginOutputVOData.
        :rtype: str
        """
        return self._output_value

    @output_value.setter
    def output_value(self, output_value):
        r"""Sets the output_value of this PluginPartQueryVOListAgentPluginOutputVOData.

        值

        :param output_value: The output_value of this PluginPartQueryVOListAgentPluginOutputVOData.
        :type output_value: str
        """
        self._output_value = output_value

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
        if not isinstance(other, PluginPartQueryVOListAgentPluginOutputVOData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
