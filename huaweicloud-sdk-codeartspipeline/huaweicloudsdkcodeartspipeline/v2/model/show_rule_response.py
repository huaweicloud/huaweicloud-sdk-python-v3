# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRuleResponse(SdkResponse):

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
        'layout_content': 'str',
        'plugin_id': 'str',
        'plugin_name': 'str',
        'plugin_version': 'str',
        'creator': 'str',
        'create_time': 'str',
        'updater': 'str',
        'update_time': 'str',
        'content': 'list[RuleContent]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name',
        'version': 'version',
        'layout_content': 'layout_content',
        'plugin_id': 'plugin_id',
        'plugin_name': 'plugin_name',
        'plugin_version': 'plugin_version',
        'creator': 'creator',
        'create_time': 'create_time',
        'updater': 'updater',
        'update_time': 'update_time',
        'content': 'content'
    }

    def __init__(self, id=None, type=None, name=None, version=None, layout_content=None, plugin_id=None, plugin_name=None, plugin_version=None, creator=None, create_time=None, updater=None, update_time=None, content=None):
        r"""ShowRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则ID
        :type id: str
        :param type: 规则类型
        :type type: str
        :param name: 规则名称
        :type name: str
        :param version: 规则版本
        :type version: str
        :param layout_content: 布局内容
        :type layout_content: str
        :param plugin_id: 插件ID
        :type plugin_id: str
        :param plugin_name: 插件名称
        :type plugin_name: str
        :param plugin_version: 插件版本号
        :type plugin_version: str
        :param creator: 创建人
        :type creator: str
        :param create_time: 创建时间
        :type create_time: str
        :param updater: 更新人
        :type updater: str
        :param update_time: 更新时间
        :type update_time: str
        :param content: 规则属性列表
        :type content: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleContent`]
        """
        
        super(ShowRuleResponse, self).__init__()

        self._id = None
        self._type = None
        self._name = None
        self._version = None
        self._layout_content = None
        self._plugin_id = None
        self._plugin_name = None
        self._plugin_version = None
        self._creator = None
        self._create_time = None
        self._updater = None
        self._update_time = None
        self._content = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if layout_content is not None:
            self.layout_content = layout_content
        if plugin_id is not None:
            self.plugin_id = plugin_id
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_version is not None:
            self.plugin_version = plugin_version
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if updater is not None:
            self.updater = updater
        if update_time is not None:
            self.update_time = update_time
        if content is not None:
            self.content = content

    @property
    def id(self):
        r"""Gets the id of this ShowRuleResponse.

        规则ID

        :return: The id of this ShowRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowRuleResponse.

        规则ID

        :param id: The id of this ShowRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ShowRuleResponse.

        规则类型

        :return: The type of this ShowRuleResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowRuleResponse.

        规则类型

        :param type: The type of this ShowRuleResponse.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ShowRuleResponse.

        规则名称

        :return: The name of this ShowRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowRuleResponse.

        规则名称

        :param name: The name of this ShowRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this ShowRuleResponse.

        规则版本

        :return: The version of this ShowRuleResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowRuleResponse.

        规则版本

        :param version: The version of this ShowRuleResponse.
        :type version: str
        """
        self._version = version

    @property
    def layout_content(self):
        r"""Gets the layout_content of this ShowRuleResponse.

        布局内容

        :return: The layout_content of this ShowRuleResponse.
        :rtype: str
        """
        return self._layout_content

    @layout_content.setter
    def layout_content(self, layout_content):
        r"""Sets the layout_content of this ShowRuleResponse.

        布局内容

        :param layout_content: The layout_content of this ShowRuleResponse.
        :type layout_content: str
        """
        self._layout_content = layout_content

    @property
    def plugin_id(self):
        r"""Gets the plugin_id of this ShowRuleResponse.

        插件ID

        :return: The plugin_id of this ShowRuleResponse.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        r"""Sets the plugin_id of this ShowRuleResponse.

        插件ID

        :param plugin_id: The plugin_id of this ShowRuleResponse.
        :type plugin_id: str
        """
        self._plugin_id = plugin_id

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this ShowRuleResponse.

        插件名称

        :return: The plugin_name of this ShowRuleResponse.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this ShowRuleResponse.

        插件名称

        :param plugin_name: The plugin_name of this ShowRuleResponse.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this ShowRuleResponse.

        插件版本号

        :return: The plugin_version of this ShowRuleResponse.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this ShowRuleResponse.

        插件版本号

        :param plugin_version: The plugin_version of this ShowRuleResponse.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def creator(self):
        r"""Gets the creator of this ShowRuleResponse.

        创建人

        :return: The creator of this ShowRuleResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ShowRuleResponse.

        创建人

        :param creator: The creator of this ShowRuleResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowRuleResponse.

        创建时间

        :return: The create_time of this ShowRuleResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowRuleResponse.

        创建时间

        :param create_time: The create_time of this ShowRuleResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def updater(self):
        r"""Gets the updater of this ShowRuleResponse.

        更新人

        :return: The updater of this ShowRuleResponse.
        :rtype: str
        """
        return self._updater

    @updater.setter
    def updater(self, updater):
        r"""Sets the updater of this ShowRuleResponse.

        更新人

        :param updater: The updater of this ShowRuleResponse.
        :type updater: str
        """
        self._updater = updater

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowRuleResponse.

        更新时间

        :return: The update_time of this ShowRuleResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowRuleResponse.

        更新时间

        :param update_time: The update_time of this ShowRuleResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def content(self):
        r"""Gets the content of this ShowRuleResponse.

        规则属性列表

        :return: The content of this ShowRuleResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleContent`]
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowRuleResponse.

        规则属性列表

        :param content: The content of this ShowRuleResponse.
        :type content: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleContent`]
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
        if not isinstance(other, ShowRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
