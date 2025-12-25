# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunAgentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conversation_id': 'str',
        'outputs': 'dict(str, object)',
        'messages': 'list[NodeMessage]',
        'error_code': 'str',
        'error_message': 'str',
        'metadata': 'dict(str, object)',
        'status': 'Status',
        'start_time': 'int',
        'end_time': 'int',
        'node_info': 'list[NodeRunInfo]',
        'events': 'list[WorkflowRunStreamRsp]'
    }

    attribute_map = {
        'conversation_id': 'conversation_id',
        'outputs': 'outputs',
        'messages': 'messages',
        'error_code': 'error_code',
        'error_message': 'error_message',
        'metadata': 'metadata',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'node_info': 'node_info',
        'events': 'events'
    }

    def __init__(self, conversation_id=None, outputs=None, messages=None, error_code=None, error_message=None, metadata=None, status=None, start_time=None, end_time=None, node_info=None, events=None):
        r"""RunAgentResponse

        The model defined in huaweicloud sdk

        :param conversation_id: 会话id
        :type conversation_id: str
        :param outputs: 
        :type outputs: dict(str, object)
        :param messages: 
        :type messages: list[:class:`huaweicloudsdkversatile.v1.NodeMessage`]
        :param error_code: 会话id
        :type error_code: str
        :param error_message: 会话id
        :type error_message: str
        :param metadata: 
        :type metadata: dict(str, object)
        :param status: 
        :type status: :class:`huaweicloudsdkversatile.v1.Status`
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param node_info: 
        :type node_info: list[:class:`huaweicloudsdkversatile.v1.NodeRunInfo`]
        :param events: 
        :type events: list[:class:`huaweicloudsdkversatile.v1.WorkflowRunStreamRsp`]
        """
        
        super().__init__()

        self._conversation_id = None
        self._outputs = None
        self._messages = None
        self._error_code = None
        self._error_message = None
        self._metadata = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._node_info = None
        self._events = None
        self.discriminator = None

        if conversation_id is not None:
            self.conversation_id = conversation_id
        if outputs is not None:
            self.outputs = outputs
        if messages is not None:
            self.messages = messages
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if metadata is not None:
            self.metadata = metadata
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if node_info is not None:
            self.node_info = node_info
        if events is not None:
            self.events = events

    @property
    def conversation_id(self):
        r"""Gets the conversation_id of this RunAgentResponse.

        会话id

        :return: The conversation_id of this RunAgentResponse.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        r"""Sets the conversation_id of this RunAgentResponse.

        会话id

        :param conversation_id: The conversation_id of this RunAgentResponse.
        :type conversation_id: str
        """
        self._conversation_id = conversation_id

    @property
    def outputs(self):
        r"""Gets the outputs of this RunAgentResponse.

        :return: The outputs of this RunAgentResponse.
        :rtype: dict(str, object)
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this RunAgentResponse.

        :param outputs: The outputs of this RunAgentResponse.
        :type outputs: dict(str, object)
        """
        self._outputs = outputs

    @property
    def messages(self):
        r"""Gets the messages of this RunAgentResponse.

        :return: The messages of this RunAgentResponse.
        :rtype: list[:class:`huaweicloudsdkversatile.v1.NodeMessage`]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        r"""Sets the messages of this RunAgentResponse.

        :param messages: The messages of this RunAgentResponse.
        :type messages: list[:class:`huaweicloudsdkversatile.v1.NodeMessage`]
        """
        self._messages = messages

    @property
    def error_code(self):
        r"""Gets the error_code of this RunAgentResponse.

        会话id

        :return: The error_code of this RunAgentResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this RunAgentResponse.

        会话id

        :param error_code: The error_code of this RunAgentResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this RunAgentResponse.

        会话id

        :return: The error_message of this RunAgentResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this RunAgentResponse.

        会话id

        :param error_message: The error_message of this RunAgentResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def metadata(self):
        r"""Gets the metadata of this RunAgentResponse.

        :return: The metadata of this RunAgentResponse.
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this RunAgentResponse.

        :param metadata: The metadata of this RunAgentResponse.
        :type metadata: dict(str, object)
        """
        self._metadata = metadata

    @property
    def status(self):
        r"""Gets the status of this RunAgentResponse.

        :return: The status of this RunAgentResponse.
        :rtype: :class:`huaweicloudsdkversatile.v1.Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RunAgentResponse.

        :param status: The status of this RunAgentResponse.
        :type status: :class:`huaweicloudsdkversatile.v1.Status`
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this RunAgentResponse.

        开始时间

        :return: The start_time of this RunAgentResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this RunAgentResponse.

        开始时间

        :param start_time: The start_time of this RunAgentResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this RunAgentResponse.

        结束时间

        :return: The end_time of this RunAgentResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this RunAgentResponse.

        结束时间

        :param end_time: The end_time of this RunAgentResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def node_info(self):
        r"""Gets the node_info of this RunAgentResponse.

        :return: The node_info of this RunAgentResponse.
        :rtype: list[:class:`huaweicloudsdkversatile.v1.NodeRunInfo`]
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        r"""Sets the node_info of this RunAgentResponse.

        :param node_info: The node_info of this RunAgentResponse.
        :type node_info: list[:class:`huaweicloudsdkversatile.v1.NodeRunInfo`]
        """
        self._node_info = node_info

    @property
    def events(self):
        r"""Gets the events of this RunAgentResponse.

        :return: The events of this RunAgentResponse.
        :rtype: list[:class:`huaweicloudsdkversatile.v1.WorkflowRunStreamRsp`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this RunAgentResponse.

        :param events: The events of this RunAgentResponse.
        :type events: list[:class:`huaweicloudsdkversatile.v1.WorkflowRunStreamRsp`]
        """
        self._events = events

    def to_dict(self):
        import warnings
        warnings.warn("RunAgentResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, RunAgentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
