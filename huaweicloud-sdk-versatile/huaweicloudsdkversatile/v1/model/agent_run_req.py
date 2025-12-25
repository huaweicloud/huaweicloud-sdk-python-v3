# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentRunReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query': 'str',
        'inputs': 'dict(str, object)',
        'user_profile': 'UserProfile',
        'tool_switch_dict': 'dict(str, bool)',
        'model_deployment_id': 'str',
        'enable_history': 'bool',
        'histories': 'list[Message]',
        'files': 'list[str]'
    }

    attribute_map = {
        'query': 'query',
        'inputs': 'inputs',
        'user_profile': 'user_profile',
        'tool_switch_dict': 'tool_switch_dict',
        'model_deployment_id': 'model_deployment_id',
        'enable_history': 'enable_history',
        'histories': 'histories',
        'files': 'files'
    }

    def __init__(self, query=None, inputs=None, user_profile=None, tool_switch_dict=None, model_deployment_id=None, enable_history=None, histories=None, files=None):
        r"""AgentRunReq

        The model defined in huaweicloud sdk

        :param query: 请求问题
        :type query: str
        :param inputs: 
        :type inputs: dict(str, object)
        :param user_profile: 
        :type user_profile: :class:`huaweicloudsdkversatile.v1.UserProfile`
        :param tool_switch_dict: 插件是否开启
        :type tool_switch_dict: dict(str, bool)
        :param model_deployment_id: 模型ID
        :type model_deployment_id: str
        :param enable_history: 是否记录会话历史
        :type enable_history: bool
        :param histories: 传入的会话历史
        :type histories: list[:class:`huaweicloudsdkversatile.v1.Message`]
        :param files: 上传文件列表
        :type files: list[str]
        """
        
        

        self._query = None
        self._inputs = None
        self._user_profile = None
        self._tool_switch_dict = None
        self._model_deployment_id = None
        self._enable_history = None
        self._histories = None
        self._files = None
        self.discriminator = None

        self.query = query
        if inputs is not None:
            self.inputs = inputs
        if user_profile is not None:
            self.user_profile = user_profile
        if tool_switch_dict is not None:
            self.tool_switch_dict = tool_switch_dict
        if model_deployment_id is not None:
            self.model_deployment_id = model_deployment_id
        if enable_history is not None:
            self.enable_history = enable_history
        if histories is not None:
            self.histories = histories
        if files is not None:
            self.files = files

    @property
    def query(self):
        r"""Gets the query of this AgentRunReq.

        请求问题

        :return: The query of this AgentRunReq.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this AgentRunReq.

        请求问题

        :param query: The query of this AgentRunReq.
        :type query: str
        """
        self._query = query

    @property
    def inputs(self):
        r"""Gets the inputs of this AgentRunReq.

        :return: The inputs of this AgentRunReq.
        :rtype: dict(str, object)
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this AgentRunReq.

        :param inputs: The inputs of this AgentRunReq.
        :type inputs: dict(str, object)
        """
        self._inputs = inputs

    @property
    def user_profile(self):
        r"""Gets the user_profile of this AgentRunReq.

        :return: The user_profile of this AgentRunReq.
        :rtype: :class:`huaweicloudsdkversatile.v1.UserProfile`
        """
        return self._user_profile

    @user_profile.setter
    def user_profile(self, user_profile):
        r"""Sets the user_profile of this AgentRunReq.

        :param user_profile: The user_profile of this AgentRunReq.
        :type user_profile: :class:`huaweicloudsdkversatile.v1.UserProfile`
        """
        self._user_profile = user_profile

    @property
    def tool_switch_dict(self):
        r"""Gets the tool_switch_dict of this AgentRunReq.

        插件是否开启

        :return: The tool_switch_dict of this AgentRunReq.
        :rtype: dict(str, bool)
        """
        return self._tool_switch_dict

    @tool_switch_dict.setter
    def tool_switch_dict(self, tool_switch_dict):
        r"""Sets the tool_switch_dict of this AgentRunReq.

        插件是否开启

        :param tool_switch_dict: The tool_switch_dict of this AgentRunReq.
        :type tool_switch_dict: dict(str, bool)
        """
        self._tool_switch_dict = tool_switch_dict

    @property
    def model_deployment_id(self):
        r"""Gets the model_deployment_id of this AgentRunReq.

        模型ID

        :return: The model_deployment_id of this AgentRunReq.
        :rtype: str
        """
        return self._model_deployment_id

    @model_deployment_id.setter
    def model_deployment_id(self, model_deployment_id):
        r"""Sets the model_deployment_id of this AgentRunReq.

        模型ID

        :param model_deployment_id: The model_deployment_id of this AgentRunReq.
        :type model_deployment_id: str
        """
        self._model_deployment_id = model_deployment_id

    @property
    def enable_history(self):
        r"""Gets the enable_history of this AgentRunReq.

        是否记录会话历史

        :return: The enable_history of this AgentRunReq.
        :rtype: bool
        """
        return self._enable_history

    @enable_history.setter
    def enable_history(self, enable_history):
        r"""Sets the enable_history of this AgentRunReq.

        是否记录会话历史

        :param enable_history: The enable_history of this AgentRunReq.
        :type enable_history: bool
        """
        self._enable_history = enable_history

    @property
    def histories(self):
        r"""Gets the histories of this AgentRunReq.

        传入的会话历史

        :return: The histories of this AgentRunReq.
        :rtype: list[:class:`huaweicloudsdkversatile.v1.Message`]
        """
        return self._histories

    @histories.setter
    def histories(self, histories):
        r"""Sets the histories of this AgentRunReq.

        传入的会话历史

        :param histories: The histories of this AgentRunReq.
        :type histories: list[:class:`huaweicloudsdkversatile.v1.Message`]
        """
        self._histories = histories

    @property
    def files(self):
        r"""Gets the files of this AgentRunReq.

        上传文件列表

        :return: The files of this AgentRunReq.
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this AgentRunReq.

        上传文件列表

        :param files: The files of this AgentRunReq.
        :type files: list[str]
        """
        self._files = files

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
        if not isinstance(other, AgentRunReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
