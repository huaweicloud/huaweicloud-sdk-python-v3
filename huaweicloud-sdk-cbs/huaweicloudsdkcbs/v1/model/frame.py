# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Frame:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'intention': 'str',
        'confidence': 'float',
        'current_slots': 'list[CurrentSlot]',
        'history_slots': 'list[HistorySlot]',
        'reply': 'str',
        'task_complete': 'bool',
        'flow_complete': 'bool',
        'candidate_words': 'list[str]',
        'intention_alias': 'str'
    }

    attribute_map = {
        'intention': 'intention',
        'confidence': 'confidence',
        'current_slots': 'current_slots',
        'history_slots': 'history_slots',
        'reply': 'reply',
        'task_complete': 'task_complete',
        'flow_complete': 'flow_complete',
        'candidate_words': 'candidate_words',
        'intention_alias': 'intention_alias'
    }

    def __init__(self, intention=None, confidence=None, current_slots=None, history_slots=None, reply=None, task_complete=None, flow_complete=None, candidate_words=None, intention_alias=None):
        """Frame

        The model defined in huaweicloud sdk

        :param intention: 意图
        :type intention: str
        :param confidence: 命中意图置信度。
        :type confidence: float
        :param current_slots: 当前槽位列表。
        :type current_slots: list[:class:`huaweicloudsdkcbs.v1.CurrentSlot`]
        :param history_slots: 历史槽位列表。
        :type history_slots: list[:class:`huaweicloudsdkcbs.v1.HistorySlot`]
        :param reply: 机器人回复。
        :type reply: str
        :param task_complete: 任务是否完成。
        :type task_complete: bool
        :param flow_complete: 对话流程是否完成。
        :type flow_complete: bool
        :param candidate_words: 候选词。
        :type candidate_words: list[str]
        :param intention_alias: 意图名称
        :type intention_alias: str
        """
        
        

        self._intention = None
        self._confidence = None
        self._current_slots = None
        self._history_slots = None
        self._reply = None
        self._task_complete = None
        self._flow_complete = None
        self._candidate_words = None
        self._intention_alias = None
        self.discriminator = None

        self.intention = intention
        self.confidence = confidence
        self.current_slots = current_slots
        self.history_slots = history_slots
        self.reply = reply
        self.task_complete = task_complete
        self.flow_complete = flow_complete
        if candidate_words is not None:
            self.candidate_words = candidate_words
        self.intention_alias = intention_alias

    @property
    def intention(self):
        """Gets the intention of this Frame.

        意图

        :return: The intention of this Frame.
        :rtype: str
        """
        return self._intention

    @intention.setter
    def intention(self, intention):
        """Sets the intention of this Frame.

        意图

        :param intention: The intention of this Frame.
        :type intention: str
        """
        self._intention = intention

    @property
    def confidence(self):
        """Gets the confidence of this Frame.

        命中意图置信度。

        :return: The confidence of this Frame.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Frame.

        命中意图置信度。

        :param confidence: The confidence of this Frame.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def current_slots(self):
        """Gets the current_slots of this Frame.

        当前槽位列表。

        :return: The current_slots of this Frame.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.CurrentSlot`]
        """
        return self._current_slots

    @current_slots.setter
    def current_slots(self, current_slots):
        """Sets the current_slots of this Frame.

        当前槽位列表。

        :param current_slots: The current_slots of this Frame.
        :type current_slots: list[:class:`huaweicloudsdkcbs.v1.CurrentSlot`]
        """
        self._current_slots = current_slots

    @property
    def history_slots(self):
        """Gets the history_slots of this Frame.

        历史槽位列表。

        :return: The history_slots of this Frame.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.HistorySlot`]
        """
        return self._history_slots

    @history_slots.setter
    def history_slots(self, history_slots):
        """Sets the history_slots of this Frame.

        历史槽位列表。

        :param history_slots: The history_slots of this Frame.
        :type history_slots: list[:class:`huaweicloudsdkcbs.v1.HistorySlot`]
        """
        self._history_slots = history_slots

    @property
    def reply(self):
        """Gets the reply of this Frame.

        机器人回复。

        :return: The reply of this Frame.
        :rtype: str
        """
        return self._reply

    @reply.setter
    def reply(self, reply):
        """Sets the reply of this Frame.

        机器人回复。

        :param reply: The reply of this Frame.
        :type reply: str
        """
        self._reply = reply

    @property
    def task_complete(self):
        """Gets the task_complete of this Frame.

        任务是否完成。

        :return: The task_complete of this Frame.
        :rtype: bool
        """
        return self._task_complete

    @task_complete.setter
    def task_complete(self, task_complete):
        """Sets the task_complete of this Frame.

        任务是否完成。

        :param task_complete: The task_complete of this Frame.
        :type task_complete: bool
        """
        self._task_complete = task_complete

    @property
    def flow_complete(self):
        """Gets the flow_complete of this Frame.

        对话流程是否完成。

        :return: The flow_complete of this Frame.
        :rtype: bool
        """
        return self._flow_complete

    @flow_complete.setter
    def flow_complete(self, flow_complete):
        """Sets the flow_complete of this Frame.

        对话流程是否完成。

        :param flow_complete: The flow_complete of this Frame.
        :type flow_complete: bool
        """
        self._flow_complete = flow_complete

    @property
    def candidate_words(self):
        """Gets the candidate_words of this Frame.

        候选词。

        :return: The candidate_words of this Frame.
        :rtype: list[str]
        """
        return self._candidate_words

    @candidate_words.setter
    def candidate_words(self, candidate_words):
        """Sets the candidate_words of this Frame.

        候选词。

        :param candidate_words: The candidate_words of this Frame.
        :type candidate_words: list[str]
        """
        self._candidate_words = candidate_words

    @property
    def intention_alias(self):
        """Gets the intention_alias of this Frame.

        意图名称

        :return: The intention_alias of this Frame.
        :rtype: str
        """
        return self._intention_alias

    @intention_alias.setter
    def intention_alias(self, intention_alias):
        """Sets the intention_alias of this Frame.

        意图名称

        :param intention_alias: The intention_alias of this Frame.
        :type intention_alias: str
        """
        self._intention_alias = intention_alias

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
        if not isinstance(other, Frame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
