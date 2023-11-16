# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequestRuleInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'name': 'str',
        'is_valid': 'bool',
        'layout_content': 'str',
        'plugin_id': 'str',
        'plugin_name': 'str',
        'plugin_version': 'str',
        'content': 'list[RuleInstanceContent]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name',
        'is_valid': 'is_valid',
        'layout_content': 'layout_content',
        'plugin_id': 'plugin_id',
        'plugin_name': 'plugin_name',
        'plugin_version': 'plugin_version',
        'content': 'content'
    }

    def __init__(self, id=None, type=None, name=None, is_valid=None, layout_content=None, plugin_id=None, plugin_name=None, plugin_version=None, content=None):
        """RequestRuleInstance

        The model defined in huaweicloud sdk

        :param id: 规则实例ID
        :type id: str
        :param type: 规则类型
        :type type: str
        :param name: 规则名称
        :type name: str
        :param is_valid: 规则实例状态
        :type is_valid: bool
        :param layout_content: 规则部署
        :type layout_content: str
        :param plugin_id: 插件Id
        :type plugin_id: str
        :param plugin_name: 插件名称
        :type plugin_name: str
        :param plugin_version: 插件版本
        :type plugin_version: str
        :param content: 规则属性列表
        :type content: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleInstanceContent`]
        """
        
        

        self._id = None
        self._type = None
        self._name = None
        self._is_valid = None
        self._layout_content = None
        self._plugin_id = None
        self._plugin_name = None
        self._plugin_version = None
        self._content = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.type = type
        self.name = name
        if is_valid is not None:
            self.is_valid = is_valid
        if layout_content is not None:
            self.layout_content = layout_content
        if plugin_id is not None:
            self.plugin_id = plugin_id
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_version is not None:
            self.plugin_version = plugin_version
        self.content = content

    @property
    def id(self):
        """Gets the id of this RequestRuleInstance.

        规则实例ID

        :return: The id of this RequestRuleInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RequestRuleInstance.

        规则实例ID

        :param id: The id of this RequestRuleInstance.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this RequestRuleInstance.

        规则类型

        :return: The type of this RequestRuleInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RequestRuleInstance.

        规则类型

        :param type: The type of this RequestRuleInstance.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this RequestRuleInstance.

        规则名称

        :return: The name of this RequestRuleInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RequestRuleInstance.

        规则名称

        :param name: The name of this RequestRuleInstance.
        :type name: str
        """
        self._name = name

    @property
    def is_valid(self):
        """Gets the is_valid of this RequestRuleInstance.

        规则实例状态

        :return: The is_valid of this RequestRuleInstance.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this RequestRuleInstance.

        规则实例状态

        :param is_valid: The is_valid of this RequestRuleInstance.
        :type is_valid: bool
        """
        self._is_valid = is_valid

    @property
    def layout_content(self):
        """Gets the layout_content of this RequestRuleInstance.

        规则部署

        :return: The layout_content of this RequestRuleInstance.
        :rtype: str
        """
        return self._layout_content

    @layout_content.setter
    def layout_content(self, layout_content):
        """Sets the layout_content of this RequestRuleInstance.

        规则部署

        :param layout_content: The layout_content of this RequestRuleInstance.
        :type layout_content: str
        """
        self._layout_content = layout_content

    @property
    def plugin_id(self):
        """Gets the plugin_id of this RequestRuleInstance.

        插件Id

        :return: The plugin_id of this RequestRuleInstance.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this RequestRuleInstance.

        插件Id

        :param plugin_id: The plugin_id of this RequestRuleInstance.
        :type plugin_id: str
        """
        self._plugin_id = plugin_id

    @property
    def plugin_name(self):
        """Gets the plugin_name of this RequestRuleInstance.

        插件名称

        :return: The plugin_name of this RequestRuleInstance.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this RequestRuleInstance.

        插件名称

        :param plugin_name: The plugin_name of this RequestRuleInstance.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_version(self):
        """Gets the plugin_version of this RequestRuleInstance.

        插件版本

        :return: The plugin_version of this RequestRuleInstance.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """Sets the plugin_version of this RequestRuleInstance.

        插件版本

        :param plugin_version: The plugin_version of this RequestRuleInstance.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def content(self):
        """Gets the content of this RequestRuleInstance.

        规则属性列表

        :return: The content of this RequestRuleInstance.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleInstanceContent`]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this RequestRuleInstance.

        规则属性列表

        :param content: The content of this RequestRuleInstance.
        :type content: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleInstanceContent`]
        """
        self._content = content

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
        if not isinstance(other, RequestRuleInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
