# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConditionStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'status': 'str',
        'observedgeneration': 'int',
        'last_transition_time': 'datetime',
        'reason': 'str',
        'message': 'str'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'observedgeneration': 'observedgeneration',
        'last_transition_time': 'lastTransitionTime',
        'reason': 'reason',
        'message': 'message'
    }

    def __init__(self, type=None, status=None, observedgeneration=None, last_transition_time=None, reason=None, message=None):
        r"""ConditionStatus

        The model defined in huaweicloud sdk

        :param type: 状态类型
        :type type: str
        :param status: 状态
        :type status: str
        :param observedgeneration: 状态对象的版本
        :type observedgeneration: int
        :param last_transition_time: 上次状态更新的时间
        :type last_transition_time: datetime
        :param reason: 状态原因
        :type reason: str
        :param message: 状态信息
        :type message: str
        """
        
        

        self._type = None
        self._status = None
        self._observedgeneration = None
        self._last_transition_time = None
        self._reason = None
        self._message = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if observedgeneration is not None:
            self.observedgeneration = observedgeneration
        if last_transition_time is not None:
            self.last_transition_time = last_transition_time
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message

    @property
    def type(self):
        r"""Gets the type of this ConditionStatus.

        状态类型

        :return: The type of this ConditionStatus.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConditionStatus.

        状态类型

        :param type: The type of this ConditionStatus.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ConditionStatus.

        状态

        :return: The status of this ConditionStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ConditionStatus.

        状态

        :param status: The status of this ConditionStatus.
        :type status: str
        """
        self._status = status

    @property
    def observedgeneration(self):
        r"""Gets the observedgeneration of this ConditionStatus.

        状态对象的版本

        :return: The observedgeneration of this ConditionStatus.
        :rtype: int
        """
        return self._observedgeneration

    @observedgeneration.setter
    def observedgeneration(self, observedgeneration):
        r"""Sets the observedgeneration of this ConditionStatus.

        状态对象的版本

        :param observedgeneration: The observedgeneration of this ConditionStatus.
        :type observedgeneration: int
        """
        self._observedgeneration = observedgeneration

    @property
    def last_transition_time(self):
        r"""Gets the last_transition_time of this ConditionStatus.

        上次状态更新的时间

        :return: The last_transition_time of this ConditionStatus.
        :rtype: datetime
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        r"""Sets the last_transition_time of this ConditionStatus.

        上次状态更新的时间

        :param last_transition_time: The last_transition_time of this ConditionStatus.
        :type last_transition_time: datetime
        """
        self._last_transition_time = last_transition_time

    @property
    def reason(self):
        r"""Gets the reason of this ConditionStatus.

        状态原因

        :return: The reason of this ConditionStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ConditionStatus.

        状态原因

        :param reason: The reason of this ConditionStatus.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        r"""Gets the message of this ConditionStatus.

        状态信息

        :return: The message of this ConditionStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ConditionStatus.

        状态信息

        :param message: The message of this ConditionStatus.
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
        if not isinstance(other, ConditionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
