# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowChatResponse(SdkResponse):

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
        'title': 'str',
        'alias': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'repo_ids': 'list[str]',
        'agent_type': 'AgentType',
        'agent_role': 'AgentRole',
        'chat_messages': 'list[ChatMessageRsp]',
        'x_chat_route_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'alias': 'alias',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'repo_ids': 'repo_ids',
        'agent_type': 'agent_type',
        'agent_role': 'agent_role',
        'chat_messages': 'chat_messages',
        'x_chat_route_id': 'X-Chat-Route-Id'
    }

    def __init__(self, id=None, title=None, alias=None, create_time=None, update_time=None, repo_ids=None, agent_type=None, agent_role=None, chat_messages=None, x_chat_route_id=None):
        r"""ShowChatResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type id: str
        :param title: **参数解释**： 对话名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type title: str
        :param alias: **参数解释**： 对话别名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type alias: str
        :param create_time: **参数解释**： 对话创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type create_time: str
        :param update_time: **参数解释**： 对话更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type update_time: str
        :param repo_ids: **参数解释**： 绑定的知识库ID列表。 **约束限制**： 绑定的知识库数量范围为[0-5]。 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type repo_ids: list[str]
        :param agent_type: 
        :type agent_type: :class:`huaweicloudsdkeihealth.v1.AgentType`
        :param agent_role: 
        :type agent_role: :class:`huaweicloudsdkeihealth.v1.AgentRole`
        :param chat_messages: **参数解释**： 对话问答列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type chat_messages: list[:class:`huaweicloudsdkeihealth.v1.ChatMessageRsp`]
        :param x_chat_route_id: 
        :type x_chat_route_id: str
        """
        
        super(ShowChatResponse, self).__init__()

        self._id = None
        self._title = None
        self._alias = None
        self._create_time = None
        self._update_time = None
        self._repo_ids = None
        self._agent_type = None
        self._agent_role = None
        self._chat_messages = None
        self._x_chat_route_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if alias is not None:
            self.alias = alias
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if repo_ids is not None:
            self.repo_ids = repo_ids
        if agent_type is not None:
            self.agent_type = agent_type
        if agent_role is not None:
            self.agent_role = agent_role
        if chat_messages is not None:
            self.chat_messages = chat_messages
        if x_chat_route_id is not None:
            self.x_chat_route_id = x_chat_route_id

    @property
    def id(self):
        r"""Gets the id of this ShowChatResponse.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The id of this ShowChatResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowChatResponse.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param id: The id of this ShowChatResponse.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this ShowChatResponse.

        **参数解释**： 对话名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The title of this ShowChatResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ShowChatResponse.

        **参数解释**： 对话名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param title: The title of this ShowChatResponse.
        :type title: str
        """
        self._title = title

    @property
    def alias(self):
        r"""Gets the alias of this ShowChatResponse.

        **参数解释**： 对话别名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The alias of this ShowChatResponse.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this ShowChatResponse.

        **参数解释**： 对话别名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param alias: The alias of this ShowChatResponse.
        :type alias: str
        """
        self._alias = alias

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowChatResponse.

        **参数解释**： 对话创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The create_time of this ShowChatResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowChatResponse.

        **参数解释**： 对话创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param create_time: The create_time of this ShowChatResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowChatResponse.

        **参数解释**： 对话更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The update_time of this ShowChatResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowChatResponse.

        **参数解释**： 对话更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param update_time: The update_time of this ShowChatResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def repo_ids(self):
        r"""Gets the repo_ids of this ShowChatResponse.

        **参数解释**： 绑定的知识库ID列表。 **约束限制**： 绑定的知识库数量范围为[0-5]。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The repo_ids of this ShowChatResponse.
        :rtype: list[str]
        """
        return self._repo_ids

    @repo_ids.setter
    def repo_ids(self, repo_ids):
        r"""Sets the repo_ids of this ShowChatResponse.

        **参数解释**： 绑定的知识库ID列表。 **约束限制**： 绑定的知识库数量范围为[0-5]。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param repo_ids: The repo_ids of this ShowChatResponse.
        :type repo_ids: list[str]
        """
        self._repo_ids = repo_ids

    @property
    def agent_type(self):
        r"""Gets the agent_type of this ShowChatResponse.

        :return: The agent_type of this ShowChatResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.AgentType`
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this ShowChatResponse.

        :param agent_type: The agent_type of this ShowChatResponse.
        :type agent_type: :class:`huaweicloudsdkeihealth.v1.AgentType`
        """
        self._agent_type = agent_type

    @property
    def agent_role(self):
        r"""Gets the agent_role of this ShowChatResponse.

        :return: The agent_role of this ShowChatResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.AgentRole`
        """
        return self._agent_role

    @agent_role.setter
    def agent_role(self, agent_role):
        r"""Sets the agent_role of this ShowChatResponse.

        :param agent_role: The agent_role of this ShowChatResponse.
        :type agent_role: :class:`huaweicloudsdkeihealth.v1.AgentRole`
        """
        self._agent_role = agent_role

    @property
    def chat_messages(self):
        r"""Gets the chat_messages of this ShowChatResponse.

        **参数解释**： 对话问答列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The chat_messages of this ShowChatResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ChatMessageRsp`]
        """
        return self._chat_messages

    @chat_messages.setter
    def chat_messages(self, chat_messages):
        r"""Sets the chat_messages of this ShowChatResponse.

        **参数解释**： 对话问答列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param chat_messages: The chat_messages of this ShowChatResponse.
        :type chat_messages: list[:class:`huaweicloudsdkeihealth.v1.ChatMessageRsp`]
        """
        self._chat_messages = chat_messages

    @property
    def x_chat_route_id(self):
        r"""Gets the x_chat_route_id of this ShowChatResponse.

        :return: The x_chat_route_id of this ShowChatResponse.
        :rtype: str
        """
        return self._x_chat_route_id

    @x_chat_route_id.setter
    def x_chat_route_id(self, x_chat_route_id):
        r"""Sets the x_chat_route_id of this ShowChatResponse.

        :param x_chat_route_id: The x_chat_route_id of this ShowChatResponse.
        :type x_chat_route_id: str
        """
        self._x_chat_route_id = x_chat_route_id

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
        if not isinstance(other, ShowChatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
