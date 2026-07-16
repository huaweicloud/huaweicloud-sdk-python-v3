# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Event:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'level': 'str',
        'time': 'str',
        'source': 'str'
    }

    attribute_map = {
        'message': 'message',
        'level': 'level',
        'time': 'time',
        'source': 'source'
    }

    def __init__(self, message=None, level=None, time=None, source=None):
        r"""Event

        The model defined in huaweicloud sdk

        :param message: 事件信息。
        :type message: str
        :param level: 事件级别。
        :type level: str
        :param time: 事件发生的时间。
        :type time: str
        :param source: **参数解释**：事件来源。 **取值范围**：不涉及。
        :type source: str
        """
        
        

        self._message = None
        self._level = None
        self._time = None
        self._source = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if level is not None:
            self.level = level
        if time is not None:
            self.time = time
        if source is not None:
            self.source = source

    @property
    def message(self):
        r"""Gets the message of this Event.

        事件信息。

        :return: The message of this Event.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this Event.

        事件信息。

        :param message: The message of this Event.
        :type message: str
        """
        self._message = message

    @property
    def level(self):
        r"""Gets the level of this Event.

        事件级别。

        :return: The level of this Event.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this Event.

        事件级别。

        :param level: The level of this Event.
        :type level: str
        """
        self._level = level

    @property
    def time(self):
        r"""Gets the time of this Event.

        事件发生的时间。

        :return: The time of this Event.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this Event.

        事件发生的时间。

        :param time: The time of this Event.
        :type time: str
        """
        self._time = time

    @property
    def source(self):
        r"""Gets the source of this Event.

        **参数解释**：事件来源。 **取值范围**：不涉及。

        :return: The source of this Event.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this Event.

        **参数解释**：事件来源。 **取值范围**：不涉及。

        :param source: The source of this Event.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
