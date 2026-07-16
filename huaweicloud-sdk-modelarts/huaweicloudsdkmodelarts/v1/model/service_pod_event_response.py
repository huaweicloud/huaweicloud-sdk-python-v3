# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServicePodEventResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'first_timestamp': 'datetime',
        'last_timestamp': 'datetime',
        'message': 'str',
        'reason': 'str',
        'reporting_component': 'str',
        'type': 'str'
    }

    attribute_map = {
        'count': 'count',
        'first_timestamp': 'first_timestamp',
        'last_timestamp': 'last_timestamp',
        'message': 'message',
        'reason': 'reason',
        'reporting_component': 'reporting_component',
        'type': 'type'
    }

    def __init__(self, count=None, first_timestamp=None, last_timestamp=None, message=None, reason=None, reporting_component=None, type=None):
        r"""ServicePodEventResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释：** 事件发生次数。 **取值范围：** 不涉及。
        :type count: int
        :param first_timestamp: **参数解释：** 首次发生时间。 **取值范围：** 不涉及。
        :type first_timestamp: datetime
        :param last_timestamp: **参数解释：** 最近发生时间。 **取值范围：** 不涉及。
        :type last_timestamp: datetime
        :param message: **参数解释：** 事件信息。 **取值范围：** 不涉及。
        :type message: str
        :param reason: **参数解释：** 事件名称。 **取值范围：** 不涉及。
        :type reason: str
        :param reporting_component: **参数解释：** 上报该事件的k8s组件名。 **取值范围：** 不涉及。
        :type reporting_component: str
        :param type: **参数解释：** 事件类型。 **取值范围：** Normal/Warning。
        :type type: str
        """
        
        

        self._count = None
        self._first_timestamp = None
        self._last_timestamp = None
        self._message = None
        self._reason = None
        self._reporting_component = None
        self._type = None
        self.discriminator = None

        self.count = count
        self.first_timestamp = first_timestamp
        self.last_timestamp = last_timestamp
        self.message = message
        self.reason = reason
        self.reporting_component = reporting_component
        self.type = type

    @property
    def count(self):
        r"""Gets the count of this ServicePodEventResponse.

        **参数解释：** 事件发生次数。 **取值范围：** 不涉及。

        :return: The count of this ServicePodEventResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ServicePodEventResponse.

        **参数解释：** 事件发生次数。 **取值范围：** 不涉及。

        :param count: The count of this ServicePodEventResponse.
        :type count: int
        """
        self._count = count

    @property
    def first_timestamp(self):
        r"""Gets the first_timestamp of this ServicePodEventResponse.

        **参数解释：** 首次发生时间。 **取值范围：** 不涉及。

        :return: The first_timestamp of this ServicePodEventResponse.
        :rtype: datetime
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        r"""Sets the first_timestamp of this ServicePodEventResponse.

        **参数解释：** 首次发生时间。 **取值范围：** 不涉及。

        :param first_timestamp: The first_timestamp of this ServicePodEventResponse.
        :type first_timestamp: datetime
        """
        self._first_timestamp = first_timestamp

    @property
    def last_timestamp(self):
        r"""Gets the last_timestamp of this ServicePodEventResponse.

        **参数解释：** 最近发生时间。 **取值范围：** 不涉及。

        :return: The last_timestamp of this ServicePodEventResponse.
        :rtype: datetime
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        r"""Sets the last_timestamp of this ServicePodEventResponse.

        **参数解释：** 最近发生时间。 **取值范围：** 不涉及。

        :param last_timestamp: The last_timestamp of this ServicePodEventResponse.
        :type last_timestamp: datetime
        """
        self._last_timestamp = last_timestamp

    @property
    def message(self):
        r"""Gets the message of this ServicePodEventResponse.

        **参数解释：** 事件信息。 **取值范围：** 不涉及。

        :return: The message of this ServicePodEventResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ServicePodEventResponse.

        **参数解释：** 事件信息。 **取值范围：** 不涉及。

        :param message: The message of this ServicePodEventResponse.
        :type message: str
        """
        self._message = message

    @property
    def reason(self):
        r"""Gets the reason of this ServicePodEventResponse.

        **参数解释：** 事件名称。 **取值范围：** 不涉及。

        :return: The reason of this ServicePodEventResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ServicePodEventResponse.

        **参数解释：** 事件名称。 **取值范围：** 不涉及。

        :param reason: The reason of this ServicePodEventResponse.
        :type reason: str
        """
        self._reason = reason

    @property
    def reporting_component(self):
        r"""Gets the reporting_component of this ServicePodEventResponse.

        **参数解释：** 上报该事件的k8s组件名。 **取值范围：** 不涉及。

        :return: The reporting_component of this ServicePodEventResponse.
        :rtype: str
        """
        return self._reporting_component

    @reporting_component.setter
    def reporting_component(self, reporting_component):
        r"""Sets the reporting_component of this ServicePodEventResponse.

        **参数解释：** 上报该事件的k8s组件名。 **取值范围：** 不涉及。

        :param reporting_component: The reporting_component of this ServicePodEventResponse.
        :type reporting_component: str
        """
        self._reporting_component = reporting_component

    @property
    def type(self):
        r"""Gets the type of this ServicePodEventResponse.

        **参数解释：** 事件类型。 **取值范围：** Normal/Warning。

        :return: The type of this ServicePodEventResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ServicePodEventResponse.

        **参数解释：** 事件类型。 **取值范围：** Normal/Warning。

        :param type: The type of this ServicePodEventResponse.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ServicePodEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
