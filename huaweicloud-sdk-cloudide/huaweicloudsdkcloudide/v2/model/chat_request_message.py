# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChatRequestMessage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case': 'str',
        'chat_id': 'str',
        'message': 'str',
        'infer_end': 'bool',
        'meta_prompt': 'list[str]',
        'need_preprocess': 'bool',
        'user_id': 'str',
        'task_parameters': 'object'
    }

    attribute_map = {
        'case': 'case',
        'chat_id': 'chat_id',
        'message': 'message',
        'infer_end': 'infer_end',
        'meta_prompt': 'meta_prompt',
        'need_preprocess': 'need_preprocess',
        'user_id': 'user_id',
        'task_parameters': 'task_parameters'
    }

    def __init__(self, case=None, chat_id=None, message=None, infer_end=None, meta_prompt=None, need_preprocess=None, user_id=None, task_parameters=None):
        """ChatRequestMessage

        The model defined in huaweicloud sdk

        :param case: case
        :type case: str
        :param chat_id: chat id
        :type chat_id: str
        :param message: message
        :type message: str
        :param infer_end: infer end
        :type infer_end: bool
        :param meta_prompt: prompt
        :type meta_prompt: list[str]
        :param need_preprocess: need or not
        :type need_preprocess: bool
        :param user_id: user id
        :type user_id: str
        :param task_parameters: task parameters
        :type task_parameters: object
        """
        
        

        self._case = None
        self._chat_id = None
        self._message = None
        self._infer_end = None
        self._meta_prompt = None
        self._need_preprocess = None
        self._user_id = None
        self._task_parameters = None
        self.discriminator = None

        if case is not None:
            self.case = case
        self.chat_id = chat_id
        self.message = message
        if infer_end is not None:
            self.infer_end = infer_end
        if meta_prompt is not None:
            self.meta_prompt = meta_prompt
        if need_preprocess is not None:
            self.need_preprocess = need_preprocess
        if user_id is not None:
            self.user_id = user_id
        if task_parameters is not None:
            self.task_parameters = task_parameters

    @property
    def case(self):
        """Gets the case of this ChatRequestMessage.

        case

        :return: The case of this ChatRequestMessage.
        :rtype: str
        """
        return self._case

    @case.setter
    def case(self, case):
        """Sets the case of this ChatRequestMessage.

        case

        :param case: The case of this ChatRequestMessage.
        :type case: str
        """
        self._case = case

    @property
    def chat_id(self):
        """Gets the chat_id of this ChatRequestMessage.

        chat id

        :return: The chat_id of this ChatRequestMessage.
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        """Sets the chat_id of this ChatRequestMessage.

        chat id

        :param chat_id: The chat_id of this ChatRequestMessage.
        :type chat_id: str
        """
        self._chat_id = chat_id

    @property
    def message(self):
        """Gets the message of this ChatRequestMessage.

        message

        :return: The message of this ChatRequestMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ChatRequestMessage.

        message

        :param message: The message of this ChatRequestMessage.
        :type message: str
        """
        self._message = message

    @property
    def infer_end(self):
        """Gets the infer_end of this ChatRequestMessage.

        infer end

        :return: The infer_end of this ChatRequestMessage.
        :rtype: bool
        """
        return self._infer_end

    @infer_end.setter
    def infer_end(self, infer_end):
        """Sets the infer_end of this ChatRequestMessage.

        infer end

        :param infer_end: The infer_end of this ChatRequestMessage.
        :type infer_end: bool
        """
        self._infer_end = infer_end

    @property
    def meta_prompt(self):
        """Gets the meta_prompt of this ChatRequestMessage.

        prompt

        :return: The meta_prompt of this ChatRequestMessage.
        :rtype: list[str]
        """
        return self._meta_prompt

    @meta_prompt.setter
    def meta_prompt(self, meta_prompt):
        """Sets the meta_prompt of this ChatRequestMessage.

        prompt

        :param meta_prompt: The meta_prompt of this ChatRequestMessage.
        :type meta_prompt: list[str]
        """
        self._meta_prompt = meta_prompt

    @property
    def need_preprocess(self):
        """Gets the need_preprocess of this ChatRequestMessage.

        need or not

        :return: The need_preprocess of this ChatRequestMessage.
        :rtype: bool
        """
        return self._need_preprocess

    @need_preprocess.setter
    def need_preprocess(self, need_preprocess):
        """Sets the need_preprocess of this ChatRequestMessage.

        need or not

        :param need_preprocess: The need_preprocess of this ChatRequestMessage.
        :type need_preprocess: bool
        """
        self._need_preprocess = need_preprocess

    @property
    def user_id(self):
        """Gets the user_id of this ChatRequestMessage.

        user id

        :return: The user_id of this ChatRequestMessage.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ChatRequestMessage.

        user id

        :param user_id: The user_id of this ChatRequestMessage.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def task_parameters(self):
        """Gets the task_parameters of this ChatRequestMessage.

        task parameters

        :return: The task_parameters of this ChatRequestMessage.
        :rtype: object
        """
        return self._task_parameters

    @task_parameters.setter
    def task_parameters(self, task_parameters):
        """Sets the task_parameters of this ChatRequestMessage.

        task parameters

        :param task_parameters: The task_parameters of this ChatRequestMessage.
        :type task_parameters: object
        """
        self._task_parameters = task_parameters

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
        if not isinstance(other, ChatRequestMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
