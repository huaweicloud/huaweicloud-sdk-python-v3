# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'kind': 'str',
        'type': 'str',
        'first_timestamp': 'str',
        'last_timestamp': 'str',
        'count': 'int',
        'reason': 'str',
        'message': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'type': 'type',
        'first_timestamp': 'firstTimestamp',
        'last_timestamp': 'lastTimestamp',
        'count': 'count',
        'reason': 'reason',
        'message': 'message'
    }

    def __init__(self, api_version=None, kind=None, type=None, first_timestamp=None, last_timestamp=None, count=None, reason=None, message=None):
        r"""EventModel

        The model defined in huaweicloud sdk

        :param api_version: **参数描述**：API版本。 **取值范围**：可选值如下： - v1
        :type api_version: str
        :param kind: **参数描述**：资源类型。 **取值范围**：可选值如下： - Event：事件
        :type kind: str
        :param type: **参数描述**：事件类型。 **取值范围**：可选值如下： - Normal：正常 - Warning：异常
        :type type: str
        :param first_timestamp: **参数描述**：事件第一次出现时间。 **取值范围**：不涉及。
        :type first_timestamp: str
        :param last_timestamp: **参数描述**：事件最后一次出现时间。 **取值范围**：不涉及。
        :type last_timestamp: str
        :param count: **参数描述**：事件连续出现次数。 **取值范围**：不涉及。
        :type count: int
        :param reason: **参数描述**：事件产生的原因。 **取值范围**：不涉及。
        :type reason: str
        :param message: **参数描述**：事件详细信息。 **取值范围**：不涉及。
        :type message: str
        """
        
        

        self._api_version = None
        self._kind = None
        self._type = None
        self._first_timestamp = None
        self._last_timestamp = None
        self._count = None
        self._reason = None
        self._message = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        self.type = type
        if first_timestamp is not None:
            self.first_timestamp = first_timestamp
        if last_timestamp is not None:
            self.last_timestamp = last_timestamp
        if count is not None:
            self.count = count
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message

    @property
    def api_version(self):
        r"""Gets the api_version of this EventModel.

        **参数描述**：API版本。 **取值范围**：可选值如下： - v1

        :return: The api_version of this EventModel.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this EventModel.

        **参数描述**：API版本。 **取值范围**：可选值如下： - v1

        :param api_version: The api_version of this EventModel.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this EventModel.

        **参数描述**：资源类型。 **取值范围**：可选值如下： - Event：事件

        :return: The kind of this EventModel.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this EventModel.

        **参数描述**：资源类型。 **取值范围**：可选值如下： - Event：事件

        :param kind: The kind of this EventModel.
        :type kind: str
        """
        self._kind = kind

    @property
    def type(self):
        r"""Gets the type of this EventModel.

        **参数描述**：事件类型。 **取值范围**：可选值如下： - Normal：正常 - Warning：异常

        :return: The type of this EventModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EventModel.

        **参数描述**：事件类型。 **取值范围**：可选值如下： - Normal：正常 - Warning：异常

        :param type: The type of this EventModel.
        :type type: str
        """
        self._type = type

    @property
    def first_timestamp(self):
        r"""Gets the first_timestamp of this EventModel.

        **参数描述**：事件第一次出现时间。 **取值范围**：不涉及。

        :return: The first_timestamp of this EventModel.
        :rtype: str
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        r"""Sets the first_timestamp of this EventModel.

        **参数描述**：事件第一次出现时间。 **取值范围**：不涉及。

        :param first_timestamp: The first_timestamp of this EventModel.
        :type first_timestamp: str
        """
        self._first_timestamp = first_timestamp

    @property
    def last_timestamp(self):
        r"""Gets the last_timestamp of this EventModel.

        **参数描述**：事件最后一次出现时间。 **取值范围**：不涉及。

        :return: The last_timestamp of this EventModel.
        :rtype: str
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        r"""Sets the last_timestamp of this EventModel.

        **参数描述**：事件最后一次出现时间。 **取值范围**：不涉及。

        :param last_timestamp: The last_timestamp of this EventModel.
        :type last_timestamp: str
        """
        self._last_timestamp = last_timestamp

    @property
    def count(self):
        r"""Gets the count of this EventModel.

        **参数描述**：事件连续出现次数。 **取值范围**：不涉及。

        :return: The count of this EventModel.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this EventModel.

        **参数描述**：事件连续出现次数。 **取值范围**：不涉及。

        :param count: The count of this EventModel.
        :type count: int
        """
        self._count = count

    @property
    def reason(self):
        r"""Gets the reason of this EventModel.

        **参数描述**：事件产生的原因。 **取值范围**：不涉及。

        :return: The reason of this EventModel.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this EventModel.

        **参数描述**：事件产生的原因。 **取值范围**：不涉及。

        :param reason: The reason of this EventModel.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        r"""Gets the message of this EventModel.

        **参数描述**：事件详细信息。 **取值范围**：不涉及。

        :return: The message of this EventModel.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this EventModel.

        **参数描述**：事件详细信息。 **取值范围**：不涉及。

        :param message: The message of this EventModel.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, EventModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
