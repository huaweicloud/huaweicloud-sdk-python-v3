# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginPartQueryVOListAgentPluginInputVOData:

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
        'name': 'str',
        'default_value': 'str',
        'plugin_name': 'str',
        'version': 'str',
        'type': 'str',
        'workspace_id': 'str',
        'validation': 'ExtensionValidation',
        'layout_content': 'str'
    }

    attribute_map = {
        'unique_id': 'unique_id',
        'name': 'name',
        'default_value': 'default_value',
        'plugin_name': 'plugin_name',
        'version': 'version',
        'type': 'type',
        'workspace_id': 'workspace_id',
        'validation': 'validation',
        'layout_content': 'layout_content'
    }

    def __init__(self, unique_id=None, name=None, default_value=None, plugin_name=None, version=None, type=None, workspace_id=None, validation=None, layout_content=None):
        r"""PluginPartQueryVOListAgentPluginInputVOData

        The model defined in huaweicloud sdk

        :param unique_id: 唯一ID
        :type unique_id: str
        :param name: 名称
        :type name: str
        :param default_value: 默认值
        :type default_value: str
        :param plugin_name: 插件名
        :type plugin_name: str
        :param version: 版本
        :type version: str
        :param type: 类型
        :type type: str
        :param workspace_id: 租户ID
        :type workspace_id: str
        :param validation: 
        :type validation: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionValidation`
        :param layout_content: 样式信息
        :type layout_content: str
        """
        
        

        self._unique_id = None
        self._name = None
        self._default_value = None
        self._plugin_name = None
        self._version = None
        self._type = None
        self._workspace_id = None
        self._validation = None
        self._layout_content = None
        self.discriminator = None

        if unique_id is not None:
            self.unique_id = unique_id
        if name is not None:
            self.name = name
        if default_value is not None:
            self.default_value = default_value
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if version is not None:
            self.version = version
        if type is not None:
            self.type = type
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if validation is not None:
            self.validation = validation
        if layout_content is not None:
            self.layout_content = layout_content

    @property
    def unique_id(self):
        r"""Gets the unique_id of this PluginPartQueryVOListAgentPluginInputVOData.

        唯一ID

        :return: The unique_id of this PluginPartQueryVOListAgentPluginInputVOData.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        r"""Sets the unique_id of this PluginPartQueryVOListAgentPluginInputVOData.

        唯一ID

        :param unique_id: The unique_id of this PluginPartQueryVOListAgentPluginInputVOData.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def name(self):
        r"""Gets the name of this PluginPartQueryVOListAgentPluginInputVOData.

        名称

        :return: The name of this PluginPartQueryVOListAgentPluginInputVOData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PluginPartQueryVOListAgentPluginInputVOData.

        名称

        :param name: The name of this PluginPartQueryVOListAgentPluginInputVOData.
        :type name: str
        """
        self._name = name

    @property
    def default_value(self):
        r"""Gets the default_value of this PluginPartQueryVOListAgentPluginInputVOData.

        默认值

        :return: The default_value of this PluginPartQueryVOListAgentPluginInputVOData.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this PluginPartQueryVOListAgentPluginInputVOData.

        默认值

        :param default_value: The default_value of this PluginPartQueryVOListAgentPluginInputVOData.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this PluginPartQueryVOListAgentPluginInputVOData.

        插件名

        :return: The plugin_name of this PluginPartQueryVOListAgentPluginInputVOData.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this PluginPartQueryVOListAgentPluginInputVOData.

        插件名

        :param plugin_name: The plugin_name of this PluginPartQueryVOListAgentPluginInputVOData.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def version(self):
        r"""Gets the version of this PluginPartQueryVOListAgentPluginInputVOData.

        版本

        :return: The version of this PluginPartQueryVOListAgentPluginInputVOData.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PluginPartQueryVOListAgentPluginInputVOData.

        版本

        :param version: The version of this PluginPartQueryVOListAgentPluginInputVOData.
        :type version: str
        """
        self._version = version

    @property
    def type(self):
        r"""Gets the type of this PluginPartQueryVOListAgentPluginInputVOData.

        类型

        :return: The type of this PluginPartQueryVOListAgentPluginInputVOData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PluginPartQueryVOListAgentPluginInputVOData.

        类型

        :param type: The type of this PluginPartQueryVOListAgentPluginInputVOData.
        :type type: str
        """
        self._type = type

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this PluginPartQueryVOListAgentPluginInputVOData.

        租户ID

        :return: The workspace_id of this PluginPartQueryVOListAgentPluginInputVOData.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this PluginPartQueryVOListAgentPluginInputVOData.

        租户ID

        :param workspace_id: The workspace_id of this PluginPartQueryVOListAgentPluginInputVOData.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def validation(self):
        r"""Gets the validation of this PluginPartQueryVOListAgentPluginInputVOData.

        :return: The validation of this PluginPartQueryVOListAgentPluginInputVOData.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionValidation`
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        r"""Sets the validation of this PluginPartQueryVOListAgentPluginInputVOData.

        :param validation: The validation of this PluginPartQueryVOListAgentPluginInputVOData.
        :type validation: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionValidation`
        """
        self._validation = validation

    @property
    def layout_content(self):
        r"""Gets the layout_content of this PluginPartQueryVOListAgentPluginInputVOData.

        样式信息

        :return: The layout_content of this PluginPartQueryVOListAgentPluginInputVOData.
        :rtype: str
        """
        return self._layout_content

    @layout_content.setter
    def layout_content(self, layout_content):
        r"""Sets the layout_content of this PluginPartQueryVOListAgentPluginInputVOData.

        样式信息

        :param layout_content: The layout_content of this PluginPartQueryVOListAgentPluginInputVOData.
        :type layout_content: str
        """
        self._layout_content = layout_content

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
        if not isinstance(other, PluginPartQueryVOListAgentPluginInputVOData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
