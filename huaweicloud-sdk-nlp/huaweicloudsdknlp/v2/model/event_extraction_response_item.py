# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventExtractionResponseItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'argument': 'list[EventExtractionResponseItemArgument]',
        'event_trigger': 'str',
        'event_type': 'str',
        'trigger_span': 'list[int]'
    }

    attribute_map = {
        'argument': 'argument',
        'event_trigger': 'event_trigger',
        'event_type': 'event_type',
        'trigger_span': 'trigger_span'
    }

    def __init__(self, argument=None, event_trigger=None, event_type=None, trigger_span=None):
        """EventExtractionResponseItem

        The model defined in huaweicloud sdk

        :param argument: 事件元素列表。
        :type argument: list[:class:`huaweicloudsdknlp.v2.EventExtractionResponseItemArgument`]
        :param event_trigger: 事件触发词。触发词是事件描述中最能代表事件发生的词汇，决定事件类别的重要特征。
        :type event_trigger: str
        :param event_type: 事件类型。
        :type event_type: str
        :param trigger_span: 事件触发词在待分析文本中的起始和终止位置。
        :type trigger_span: list[int]
        """
        
        

        self._argument = None
        self._event_trigger = None
        self._event_type = None
        self._trigger_span = None
        self.discriminator = None

        self.argument = argument
        self.event_trigger = event_trigger
        if event_type is not None:
            self.event_type = event_type
        self.trigger_span = trigger_span

    @property
    def argument(self):
        """Gets the argument of this EventExtractionResponseItem.

        事件元素列表。

        :return: The argument of this EventExtractionResponseItem.
        :rtype: list[:class:`huaweicloudsdknlp.v2.EventExtractionResponseItemArgument`]
        """
        return self._argument

    @argument.setter
    def argument(self, argument):
        """Sets the argument of this EventExtractionResponseItem.

        事件元素列表。

        :param argument: The argument of this EventExtractionResponseItem.
        :type argument: list[:class:`huaweicloudsdknlp.v2.EventExtractionResponseItemArgument`]
        """
        self._argument = argument

    @property
    def event_trigger(self):
        """Gets the event_trigger of this EventExtractionResponseItem.

        事件触发词。触发词是事件描述中最能代表事件发生的词汇，决定事件类别的重要特征。

        :return: The event_trigger of this EventExtractionResponseItem.
        :rtype: str
        """
        return self._event_trigger

    @event_trigger.setter
    def event_trigger(self, event_trigger):
        """Sets the event_trigger of this EventExtractionResponseItem.

        事件触发词。触发词是事件描述中最能代表事件发生的词汇，决定事件类别的重要特征。

        :param event_trigger: The event_trigger of this EventExtractionResponseItem.
        :type event_trigger: str
        """
        self._event_trigger = event_trigger

    @property
    def event_type(self):
        """Gets the event_type of this EventExtractionResponseItem.

        事件类型。

        :return: The event_type of this EventExtractionResponseItem.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EventExtractionResponseItem.

        事件类型。

        :param event_type: The event_type of this EventExtractionResponseItem.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def trigger_span(self):
        """Gets the trigger_span of this EventExtractionResponseItem.

        事件触发词在待分析文本中的起始和终止位置。

        :return: The trigger_span of this EventExtractionResponseItem.
        :rtype: list[int]
        """
        return self._trigger_span

    @trigger_span.setter
    def trigger_span(self, trigger_span):
        """Sets the trigger_span of this EventExtractionResponseItem.

        事件触发词在待分析文本中的起始和终止位置。

        :param trigger_span: The trigger_span of this EventExtractionResponseItem.
        :type trigger_span: list[int]
        """
        self._trigger_span = trigger_span

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
        if not isinstance(other, EventExtractionResponseItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
