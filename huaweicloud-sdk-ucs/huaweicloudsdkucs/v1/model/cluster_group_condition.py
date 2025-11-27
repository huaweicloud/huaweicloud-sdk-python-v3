# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterGroupCondition:

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
        'reason': 'str',
        'message': 'str',
        'last_transition_time': 'datetime'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'reason': 'reason',
        'message': 'message',
        'last_transition_time': 'lastTransitionTime'
    }

    def __init__(self, type=None, status=None, reason=None, message=None, last_transition_time=None):
        r"""ClusterGroupCondition

        The model defined in huaweicloud sdk

        :param type: 类型。 - Federation：舰队启用联邦状态类型 - Policy：权限策略
        :type type: str
        :param status: 舰队启用的联邦或权限策略的状态
        :type status: str
        :param reason: 状态原因
        :type reason: str
        :param message: 状态信息
        :type message: str
        :param last_transition_time: 状态更新时间
        :type last_transition_time: datetime
        """
        
        

        self._type = None
        self._status = None
        self._reason = None
        self._message = None
        self._last_transition_time = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message
        if last_transition_time is not None:
            self.last_transition_time = last_transition_time

    @property
    def type(self):
        r"""Gets the type of this ClusterGroupCondition.

        类型。 - Federation：舰队启用联邦状态类型 - Policy：权限策略

        :return: The type of this ClusterGroupCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ClusterGroupCondition.

        类型。 - Federation：舰队启用联邦状态类型 - Policy：权限策略

        :param type: The type of this ClusterGroupCondition.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ClusterGroupCondition.

        舰队启用的联邦或权限策略的状态

        :return: The status of this ClusterGroupCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ClusterGroupCondition.

        舰队启用的联邦或权限策略的状态

        :param status: The status of this ClusterGroupCondition.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        r"""Gets the reason of this ClusterGroupCondition.

        状态原因

        :return: The reason of this ClusterGroupCondition.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ClusterGroupCondition.

        状态原因

        :param reason: The reason of this ClusterGroupCondition.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        r"""Gets the message of this ClusterGroupCondition.

        状态信息

        :return: The message of this ClusterGroupCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ClusterGroupCondition.

        状态信息

        :param message: The message of this ClusterGroupCondition.
        :type message: str
        """
        self._message = message

    @property
    def last_transition_time(self):
        r"""Gets the last_transition_time of this ClusterGroupCondition.

        状态更新时间

        :return: The last_transition_time of this ClusterGroupCondition.
        :rtype: datetime
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        r"""Sets the last_transition_time of this ClusterGroupCondition.

        状态更新时间

        :param last_transition_time: The last_transition_time of this ClusterGroupCondition.
        :type last_transition_time: datetime
        """
        self._last_transition_time = last_transition_time

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
        if not isinstance(other, ClusterGroupCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
