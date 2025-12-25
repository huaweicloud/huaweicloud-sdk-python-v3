# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowRunStreamRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event': 'str',
        'conversation_id': 'str',
        'data': 'object',
        'created_time': 'int'
    }

    attribute_map = {
        'event': 'event',
        'conversation_id': 'conversation_id',
        'data': 'data',
        'created_time': 'createdTime'
    }

    def __init__(self, event=None, conversation_id=None, data=None, created_time=None):
        r"""WorkflowRunStreamRsp

        The model defined in huaweicloud sdk

        :param event: 事件类型：1、workflow_started 2、node_started 3、node_wait 4、node_finished 5、workflow_finished 6、text_chunk ：流式输出到对话框的信息
        :type event: str
        :param conversation_id: 执行的conversation_id
        :type conversation_id: str
        :param data: 类型说明：1. node_started，node_finished，node_wait data使用NodeInfo对象 2. workflow_started, workflow_finished  data使用 WorkflowInfo对象 3. text_chunk使用对象TextChunk
        :type data: object
        :param created_time: 事件发生时间
        :type created_time: int
        """
        
        

        self._event = None
        self._conversation_id = None
        self._data = None
        self._created_time = None
        self.discriminator = None

        if event is not None:
            self.event = event
        if conversation_id is not None:
            self.conversation_id = conversation_id
        if data is not None:
            self.data = data
        if created_time is not None:
            self.created_time = created_time

    @property
    def event(self):
        r"""Gets the event of this WorkflowRunStreamRsp.

        事件类型：1、workflow_started 2、node_started 3、node_wait 4、node_finished 5、workflow_finished 6、text_chunk ：流式输出到对话框的信息

        :return: The event of this WorkflowRunStreamRsp.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        r"""Sets the event of this WorkflowRunStreamRsp.

        事件类型：1、workflow_started 2、node_started 3、node_wait 4、node_finished 5、workflow_finished 6、text_chunk ：流式输出到对话框的信息

        :param event: The event of this WorkflowRunStreamRsp.
        :type event: str
        """
        self._event = event

    @property
    def conversation_id(self):
        r"""Gets the conversation_id of this WorkflowRunStreamRsp.

        执行的conversation_id

        :return: The conversation_id of this WorkflowRunStreamRsp.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        r"""Sets the conversation_id of this WorkflowRunStreamRsp.

        执行的conversation_id

        :param conversation_id: The conversation_id of this WorkflowRunStreamRsp.
        :type conversation_id: str
        """
        self._conversation_id = conversation_id

    @property
    def data(self):
        r"""Gets the data of this WorkflowRunStreamRsp.

        类型说明：1. node_started，node_finished，node_wait data使用NodeInfo对象 2. workflow_started, workflow_finished  data使用 WorkflowInfo对象 3. text_chunk使用对象TextChunk

        :return: The data of this WorkflowRunStreamRsp.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this WorkflowRunStreamRsp.

        类型说明：1. node_started，node_finished，node_wait data使用NodeInfo对象 2. workflow_started, workflow_finished  data使用 WorkflowInfo对象 3. text_chunk使用对象TextChunk

        :param data: The data of this WorkflowRunStreamRsp.
        :type data: object
        """
        self._data = data

    @property
    def created_time(self):
        r"""Gets the created_time of this WorkflowRunStreamRsp.

        事件发生时间

        :return: The created_time of this WorkflowRunStreamRsp.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this WorkflowRunStreamRsp.

        事件发生时间

        :param created_time: The created_time of this WorkflowRunStreamRsp.
        :type created_time: int
        """
        self._created_time = created_time

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
        if not isinstance(other, WorkflowRunStreamRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
