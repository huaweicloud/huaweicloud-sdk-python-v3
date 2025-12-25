# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowRunReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inputs': 'dict(str, object)',
        'memory_inputs': 'dict(str, object)',
        'globals': 'dict(str, object)',
        'messages': 'list[Message]',
        'user_profile': 'UserProfile',
        'plugin_configs': 'list[PluginConfig]',
        'version': 'int',
        'user_id': 'str',
        'conversation': 'Conversation',
        'enable_history': 'bool'
    }

    attribute_map = {
        'inputs': 'inputs',
        'memory_inputs': 'memory_inputs',
        'globals': 'globals',
        'messages': 'messages',
        'user_profile': 'user_profile',
        'plugin_configs': 'plugin_configs',
        'version': 'version',
        'user_id': 'userId',
        'conversation': 'conversation',
        'enable_history': 'enable_history'
    }

    def __init__(self, inputs=None, memory_inputs=None, globals=None, messages=None, user_profile=None, plugin_configs=None, version=None, user_id=None, conversation=None, enable_history=None):
        r"""WorkflowRunReq

        The model defined in huaweicloud sdk

        :param inputs: 
        :type inputs: dict(str, object)
        :param memory_inputs: 
        :type memory_inputs: dict(str, object)
        :param globals: 
        :type globals: dict(str, object)
        :param messages: user消息
        :type messages: list[:class:`huaweicloudsdkversatile.v1.Message`]
        :param user_profile: 
        :type user_profile: :class:`huaweicloudsdkversatile.v1.UserProfile`
        :param plugin_configs: 插件参数数组
        :type plugin_configs: list[:class:`huaweicloudsdkversatile.v1.PluginConfig`]
        :param version: 
        :type version: int
        :param user_id: 用户ID
        :type user_id: str
        :param conversation: 
        :type conversation: :class:`huaweicloudsdkversatile.v1.Conversation`
        :param enable_history: 会话历史写入
        :type enable_history: bool
        """
        
        

        self._inputs = None
        self._memory_inputs = None
        self._globals = None
        self._messages = None
        self._user_profile = None
        self._plugin_configs = None
        self._version = None
        self._user_id = None
        self._conversation = None
        self._enable_history = None
        self.discriminator = None

        self.inputs = inputs
        if memory_inputs is not None:
            self.memory_inputs = memory_inputs
        if globals is not None:
            self.globals = globals
        if messages is not None:
            self.messages = messages
        if user_profile is not None:
            self.user_profile = user_profile
        if plugin_configs is not None:
            self.plugin_configs = plugin_configs
        if version is not None:
            self.version = version
        if user_id is not None:
            self.user_id = user_id
        if conversation is not None:
            self.conversation = conversation
        if enable_history is not None:
            self.enable_history = enable_history

    @property
    def inputs(self):
        r"""Gets the inputs of this WorkflowRunReq.

        :return: The inputs of this WorkflowRunReq.
        :rtype: dict(str, object)
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this WorkflowRunReq.

        :param inputs: The inputs of this WorkflowRunReq.
        :type inputs: dict(str, object)
        """
        self._inputs = inputs

    @property
    def memory_inputs(self):
        r"""Gets the memory_inputs of this WorkflowRunReq.

        :return: The memory_inputs of this WorkflowRunReq.
        :rtype: dict(str, object)
        """
        return self._memory_inputs

    @memory_inputs.setter
    def memory_inputs(self, memory_inputs):
        r"""Sets the memory_inputs of this WorkflowRunReq.

        :param memory_inputs: The memory_inputs of this WorkflowRunReq.
        :type memory_inputs: dict(str, object)
        """
        self._memory_inputs = memory_inputs

    @property
    def globals(self):
        r"""Gets the globals of this WorkflowRunReq.

        :return: The globals of this WorkflowRunReq.
        :rtype: dict(str, object)
        """
        return self._globals

    @globals.setter
    def globals(self, globals):
        r"""Sets the globals of this WorkflowRunReq.

        :param globals: The globals of this WorkflowRunReq.
        :type globals: dict(str, object)
        """
        self._globals = globals

    @property
    def messages(self):
        r"""Gets the messages of this WorkflowRunReq.

        user消息

        :return: The messages of this WorkflowRunReq.
        :rtype: list[:class:`huaweicloudsdkversatile.v1.Message`]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        r"""Sets the messages of this WorkflowRunReq.

        user消息

        :param messages: The messages of this WorkflowRunReq.
        :type messages: list[:class:`huaweicloudsdkversatile.v1.Message`]
        """
        self._messages = messages

    @property
    def user_profile(self):
        r"""Gets the user_profile of this WorkflowRunReq.

        :return: The user_profile of this WorkflowRunReq.
        :rtype: :class:`huaweicloudsdkversatile.v1.UserProfile`
        """
        return self._user_profile

    @user_profile.setter
    def user_profile(self, user_profile):
        r"""Sets the user_profile of this WorkflowRunReq.

        :param user_profile: The user_profile of this WorkflowRunReq.
        :type user_profile: :class:`huaweicloudsdkversatile.v1.UserProfile`
        """
        self._user_profile = user_profile

    @property
    def plugin_configs(self):
        r"""Gets the plugin_configs of this WorkflowRunReq.

        插件参数数组

        :return: The plugin_configs of this WorkflowRunReq.
        :rtype: list[:class:`huaweicloudsdkversatile.v1.PluginConfig`]
        """
        return self._plugin_configs

    @plugin_configs.setter
    def plugin_configs(self, plugin_configs):
        r"""Sets the plugin_configs of this WorkflowRunReq.

        插件参数数组

        :param plugin_configs: The plugin_configs of this WorkflowRunReq.
        :type plugin_configs: list[:class:`huaweicloudsdkversatile.v1.PluginConfig`]
        """
        self._plugin_configs = plugin_configs

    @property
    def version(self):
        r"""Gets the version of this WorkflowRunReq.

        :return: The version of this WorkflowRunReq.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this WorkflowRunReq.

        :param version: The version of this WorkflowRunReq.
        :type version: int
        """
        self._version = version

    @property
    def user_id(self):
        r"""Gets the user_id of this WorkflowRunReq.

        用户ID

        :return: The user_id of this WorkflowRunReq.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this WorkflowRunReq.

        用户ID

        :param user_id: The user_id of this WorkflowRunReq.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def conversation(self):
        r"""Gets the conversation of this WorkflowRunReq.

        :return: The conversation of this WorkflowRunReq.
        :rtype: :class:`huaweicloudsdkversatile.v1.Conversation`
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        r"""Sets the conversation of this WorkflowRunReq.

        :param conversation: The conversation of this WorkflowRunReq.
        :type conversation: :class:`huaweicloudsdkversatile.v1.Conversation`
        """
        self._conversation = conversation

    @property
    def enable_history(self):
        r"""Gets the enable_history of this WorkflowRunReq.

        会话历史写入

        :return: The enable_history of this WorkflowRunReq.
        :rtype: bool
        """
        return self._enable_history

    @enable_history.setter
    def enable_history(self, enable_history):
        r"""Sets the enable_history of this WorkflowRunReq.

        会话历史写入

        :param enable_history: The enable_history of this WorkflowRunReq.
        :type enable_history: bool
        """
        self._enable_history = enable_history

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkflowRunReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
