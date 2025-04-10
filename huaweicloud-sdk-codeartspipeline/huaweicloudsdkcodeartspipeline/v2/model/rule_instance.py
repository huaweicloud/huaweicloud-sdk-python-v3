# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleInstance:

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
        'version': 'str',
        'plugin_id': 'str',
        'plugin_name': 'str',
        'plugin_version': 'str',
        'is_valid': 'bool',
        'editable': 'bool',
        'content': 'list[RuleInstanceContent]',
        'parent': 'RuleSet'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name',
        'version': 'version',
        'plugin_id': 'plugin_id',
        'plugin_name': 'plugin_name',
        'plugin_version': 'plugin_version',
        'is_valid': 'is_valid',
        'editable': 'editable',
        'content': 'content',
        'parent': 'parent'
    }

    def __init__(self, id=None, type=None, name=None, version=None, plugin_id=None, plugin_name=None, plugin_version=None, is_valid=None, editable=None, content=None, parent=None):
        r"""RuleInstance

        The model defined in huaweicloud sdk

        :param id: 规则实例ID
        :type id: str
        :param type: 规则类型ID
        :type type: str
        :param name: 规则名称
        :type name: str
        :param version: 规则版本
        :type version: str
        :param plugin_id: 插件ID
        :type plugin_id: str
        :param plugin_name: 插件名称
        :type plugin_name: str
        :param plugin_version: 插件版本号
        :type plugin_version: str
        :param is_valid: 是否生效
        :type is_valid: bool
        :param editable: 是否可编辑
        :type editable: bool
        :param content: 规则属性列表
        :type content: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleInstanceContent`]
        :param parent: 
        :type parent: :class:`huaweicloudsdkcodeartspipeline.v2.RuleSet`
        """
        
        

        self._id = None
        self._type = None
        self._name = None
        self._version = None
        self._plugin_id = None
        self._plugin_name = None
        self._plugin_version = None
        self._is_valid = None
        self._editable = None
        self._content = None
        self._parent = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.name = name
        self.version = version
        if plugin_id is not None:
            self.plugin_id = plugin_id
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_version is not None:
            self.plugin_version = plugin_version
        self.is_valid = is_valid
        if editable is not None:
            self.editable = editable
        self.content = content
        if parent is not None:
            self.parent = parent

    @property
    def id(self):
        r"""Gets the id of this RuleInstance.

        规则实例ID

        :return: The id of this RuleInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RuleInstance.

        规则实例ID

        :param id: The id of this RuleInstance.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this RuleInstance.

        规则类型ID

        :return: The type of this RuleInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RuleInstance.

        规则类型ID

        :param type: The type of this RuleInstance.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this RuleInstance.

        规则名称

        :return: The name of this RuleInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RuleInstance.

        规则名称

        :param name: The name of this RuleInstance.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this RuleInstance.

        规则版本

        :return: The version of this RuleInstance.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this RuleInstance.

        规则版本

        :param version: The version of this RuleInstance.
        :type version: str
        """
        self._version = version

    @property
    def plugin_id(self):
        r"""Gets the plugin_id of this RuleInstance.

        插件ID

        :return: The plugin_id of this RuleInstance.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        r"""Sets the plugin_id of this RuleInstance.

        插件ID

        :param plugin_id: The plugin_id of this RuleInstance.
        :type plugin_id: str
        """
        self._plugin_id = plugin_id

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this RuleInstance.

        插件名称

        :return: The plugin_name of this RuleInstance.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this RuleInstance.

        插件名称

        :param plugin_name: The plugin_name of this RuleInstance.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this RuleInstance.

        插件版本号

        :return: The plugin_version of this RuleInstance.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this RuleInstance.

        插件版本号

        :param plugin_version: The plugin_version of this RuleInstance.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def is_valid(self):
        r"""Gets the is_valid of this RuleInstance.

        是否生效

        :return: The is_valid of this RuleInstance.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        r"""Sets the is_valid of this RuleInstance.

        是否生效

        :param is_valid: The is_valid of this RuleInstance.
        :type is_valid: bool
        """
        self._is_valid = is_valid

    @property
    def editable(self):
        r"""Gets the editable of this RuleInstance.

        是否可编辑

        :return: The editable of this RuleInstance.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        r"""Sets the editable of this RuleInstance.

        是否可编辑

        :param editable: The editable of this RuleInstance.
        :type editable: bool
        """
        self._editable = editable

    @property
    def content(self):
        r"""Gets the content of this RuleInstance.

        规则属性列表

        :return: The content of this RuleInstance.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleInstanceContent`]
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this RuleInstance.

        规则属性列表

        :param content: The content of this RuleInstance.
        :type content: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleInstanceContent`]
        """
        self._content = content

    @property
    def parent(self):
        r"""Gets the parent of this RuleInstance.

        :return: The parent of this RuleInstance.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.RuleSet`
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        r"""Sets the parent of this RuleInstance.

        :param parent: The parent of this RuleInstance.
        :type parent: :class:`huaweicloudsdkcodeartspipeline.v2.RuleSet`
        """
        self._parent = parent

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
        if not isinstance(other, RuleInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
