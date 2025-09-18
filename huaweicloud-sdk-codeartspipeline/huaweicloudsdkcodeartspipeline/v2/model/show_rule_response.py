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
        'is_valid': 'bool',
        'version': 'str',
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
        'is_valid': 'is_valid',
        'version': 'version',
        'plugin_id': 'plugin_id',
        'plugin_name': 'plugin_name',
        'plugin_version': 'plugin_version',
        'creator': 'creator',
        'create_time': 'create_time',
        'updater': 'updater',
        'update_time': 'update_time',
        'content': 'content'
    }

    def __init__(self, id=None, type=None, name=None, is_valid=None, version=None, plugin_id=None, plugin_name=None, plugin_version=None, creator=None, create_time=None, updater=None, update_time=None, content=None):
        r"""ShowRuleResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 规则ID。 **取值范围**： 32位字符，由数字和字母组成。 
        :type id: str
        :param type: **参数解释**： 规则类型。 **取值范围**： - Build：构建。 - Gate：代码检查。 - Test：测试。 
        :type type: str
        :param name: **参数解释**： 规则名称。 **取值范围**： 不涉及。 
        :type name: str
        :param is_valid: **参数解释**： 规则是否有效。 **取值范围**： true:有效，false:无效 
        :type is_valid: bool
        :param version: **参数解释**： 规则版本。 **取值范围**： 不涉及。 
        :type version: str
        :param plugin_id: **参数解释**： 扩展插件唯一ID。 **取值范围**： 不涉及。 
        :type plugin_id: str
        :param plugin_name: **参数解释**： 扩展插件名称。 **取值范围**： 不涉及。 
        :type plugin_name: str
        :param plugin_version: **参数解释**： 扩展插件版本号。 **取值范围**： 不涉及。 
        :type plugin_version: str
        :param creator: **参数解释**： 规则创建人。 **取值范围**： 不涉及。 
        :type creator: str
        :param create_time: **参数解释**： 规则创建时间。 **取值范围**： 不涉及。 
        :type create_time: str
        :param updater: **参数解释**： 规则最后更新人。 **取值范围**： 不涉及。 
        :type updater: str
        :param update_time: **参数解释**： 规则最后更新时间。 **取值范围**： 不涉及。 
        :type update_time: str
        :param content: **参数解释**： 规则详细属性。 **取值范围**： 不涉及。 
        :type content: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleContent`]
        """
        
        super(ShowRuleResponse, self).__init__()

        self._id = None
        self._type = None
        self._name = None
        self._is_valid = None
        self._version = None
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
        if is_valid is not None:
            self.is_valid = is_valid
        if version is not None:
            self.version = version
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

        **参数解释**： 规则ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :return: The id of this ShowRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowRuleResponse.

        **参数解释**： 规则ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :param id: The id of this ShowRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ShowRuleResponse.

        **参数解释**： 规则类型。 **取值范围**： - Build：构建。 - Gate：代码检查。 - Test：测试。 

        :return: The type of this ShowRuleResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowRuleResponse.

        **参数解释**： 规则类型。 **取值范围**： - Build：构建。 - Gate：代码检查。 - Test：测试。 

        :param type: The type of this ShowRuleResponse.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ShowRuleResponse.

        **参数解释**： 规则名称。 **取值范围**： 不涉及。 

        :return: The name of this ShowRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowRuleResponse.

        **参数解释**： 规则名称。 **取值范围**： 不涉及。 

        :param name: The name of this ShowRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def is_valid(self):
        r"""Gets the is_valid of this ShowRuleResponse.

        **参数解释**： 规则是否有效。 **取值范围**： true:有效，false:无效 

        :return: The is_valid of this ShowRuleResponse.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        r"""Sets the is_valid of this ShowRuleResponse.

        **参数解释**： 规则是否有效。 **取值范围**： true:有效，false:无效 

        :param is_valid: The is_valid of this ShowRuleResponse.
        :type is_valid: bool
        """
        self._is_valid = is_valid

    @property
    def version(self):
        r"""Gets the version of this ShowRuleResponse.

        **参数解释**： 规则版本。 **取值范围**： 不涉及。 

        :return: The version of this ShowRuleResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowRuleResponse.

        **参数解释**： 规则版本。 **取值范围**： 不涉及。 

        :param version: The version of this ShowRuleResponse.
        :type version: str
        """
        self._version = version

    @property
    def plugin_id(self):
        r"""Gets the plugin_id of this ShowRuleResponse.

        **参数解释**： 扩展插件唯一ID。 **取值范围**： 不涉及。 

        :return: The plugin_id of this ShowRuleResponse.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        r"""Sets the plugin_id of this ShowRuleResponse.

        **参数解释**： 扩展插件唯一ID。 **取值范围**： 不涉及。 

        :param plugin_id: The plugin_id of this ShowRuleResponse.
        :type plugin_id: str
        """
        self._plugin_id = plugin_id

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this ShowRuleResponse.

        **参数解释**： 扩展插件名称。 **取值范围**： 不涉及。 

        :return: The plugin_name of this ShowRuleResponse.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this ShowRuleResponse.

        **参数解释**： 扩展插件名称。 **取值范围**： 不涉及。 

        :param plugin_name: The plugin_name of this ShowRuleResponse.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this ShowRuleResponse.

        **参数解释**： 扩展插件版本号。 **取值范围**： 不涉及。 

        :return: The plugin_version of this ShowRuleResponse.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this ShowRuleResponse.

        **参数解释**： 扩展插件版本号。 **取值范围**： 不涉及。 

        :param plugin_version: The plugin_version of this ShowRuleResponse.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def creator(self):
        r"""Gets the creator of this ShowRuleResponse.

        **参数解释**： 规则创建人。 **取值范围**： 不涉及。 

        :return: The creator of this ShowRuleResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ShowRuleResponse.

        **参数解释**： 规则创建人。 **取值范围**： 不涉及。 

        :param creator: The creator of this ShowRuleResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowRuleResponse.

        **参数解释**： 规则创建时间。 **取值范围**： 不涉及。 

        :return: The create_time of this ShowRuleResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowRuleResponse.

        **参数解释**： 规则创建时间。 **取值范围**： 不涉及。 

        :param create_time: The create_time of this ShowRuleResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def updater(self):
        r"""Gets the updater of this ShowRuleResponse.

        **参数解释**： 规则最后更新人。 **取值范围**： 不涉及。 

        :return: The updater of this ShowRuleResponse.
        :rtype: str
        """
        return self._updater

    @updater.setter
    def updater(self, updater):
        r"""Sets the updater of this ShowRuleResponse.

        **参数解释**： 规则最后更新人。 **取值范围**： 不涉及。 

        :param updater: The updater of this ShowRuleResponse.
        :type updater: str
        """
        self._updater = updater

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowRuleResponse.

        **参数解释**： 规则最后更新时间。 **取值范围**： 不涉及。 

        :return: The update_time of this ShowRuleResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowRuleResponse.

        **参数解释**： 规则最后更新时间。 **取值范围**： 不涉及。 

        :param update_time: The update_time of this ShowRuleResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def content(self):
        r"""Gets the content of this ShowRuleResponse.

        **参数解释**： 规则详细属性。 **取值范围**： 不涉及。 

        :return: The content of this ShowRuleResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleContent`]
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowRuleResponse.

        **参数解释**： 规则详细属性。 **取值范围**： 不涉及。 

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
