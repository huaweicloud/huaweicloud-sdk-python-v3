# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolCondition:

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
        'last_probe_time': 'str',
        'last_transit_time': 'str',
        'reason': 'str',
        'message': 'str'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'last_probe_time': 'lastProbeTime',
        'last_transit_time': 'lastTransitTime',
        'reason': 'reason',
        'message': 'message'
    }

    def __init__(self, type=None, status=None, last_probe_time=None, last_transit_time=None, reason=None, message=None):
        r"""NodePoolCondition

        The model defined in huaweicloud sdk

        :param type: Condition类型，当前支持类型如下 - \&quot;Scalable\&quot;：节点池实际的可扩容状态，如果状态为\&quot;False\&quot;时则不会再次触发节点池扩容行为。 - \&quot;QuotaInsufficient\&quot;：节点池扩容依赖的配额不足，影响节点池可扩容状态。 - \&quot;ResourceInsufficient\&quot;：节点池扩容依赖的资源不足，影响节点池可扩容状态。 - \&quot;UnexpectedError\&quot;：节点池非预期扩容失败，影响节点池可扩容状态。 [- \&quot;LockedByOrder\&quot;：包周期节点池被订单锁定，此时Reason为待支付订单ID。](tag:hws,hws_hk) - \&quot;Error\&quot;：节点池错误，通常由于删除失败触发。 
        :type type: str
        :param status: Condition当前状态，取值如下 - \&quot;True\&quot; - \&quot;False\&quot; 
        :type status: str
        :param last_probe_time: 上次状态检查时间。
        :type last_probe_time: str
        :param last_transit_time: 上次状态变更时间。
        :type last_transit_time: str
        :param reason: 上次状态变更原因。
        :type reason: str
        :param message: Condition详细描述。
        :type message: str
        """
        
        

        self._type = None
        self._status = None
        self._last_probe_time = None
        self._last_transit_time = None
        self._reason = None
        self._message = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if last_probe_time is not None:
            self.last_probe_time = last_probe_time
        if last_transit_time is not None:
            self.last_transit_time = last_transit_time
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message

    @property
    def type(self):
        r"""Gets the type of this NodePoolCondition.

        Condition类型，当前支持类型如下 - \"Scalable\"：节点池实际的可扩容状态，如果状态为\"False\"时则不会再次触发节点池扩容行为。 - \"QuotaInsufficient\"：节点池扩容依赖的配额不足，影响节点池可扩容状态。 - \"ResourceInsufficient\"：节点池扩容依赖的资源不足，影响节点池可扩容状态。 - \"UnexpectedError\"：节点池非预期扩容失败，影响节点池可扩容状态。 [- \"LockedByOrder\"：包周期节点池被订单锁定，此时Reason为待支付订单ID。](tag:hws,hws_hk) - \"Error\"：节点池错误，通常由于删除失败触发。 

        :return: The type of this NodePoolCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NodePoolCondition.

        Condition类型，当前支持类型如下 - \"Scalable\"：节点池实际的可扩容状态，如果状态为\"False\"时则不会再次触发节点池扩容行为。 - \"QuotaInsufficient\"：节点池扩容依赖的配额不足，影响节点池可扩容状态。 - \"ResourceInsufficient\"：节点池扩容依赖的资源不足，影响节点池可扩容状态。 - \"UnexpectedError\"：节点池非预期扩容失败，影响节点池可扩容状态。 [- \"LockedByOrder\"：包周期节点池被订单锁定，此时Reason为待支付订单ID。](tag:hws,hws_hk) - \"Error\"：节点池错误，通常由于删除失败触发。 

        :param type: The type of this NodePoolCondition.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this NodePoolCondition.

        Condition当前状态，取值如下 - \"True\" - \"False\" 

        :return: The status of this NodePoolCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NodePoolCondition.

        Condition当前状态，取值如下 - \"True\" - \"False\" 

        :param status: The status of this NodePoolCondition.
        :type status: str
        """
        self._status = status

    @property
    def last_probe_time(self):
        r"""Gets the last_probe_time of this NodePoolCondition.

        上次状态检查时间。

        :return: The last_probe_time of this NodePoolCondition.
        :rtype: str
        """
        return self._last_probe_time

    @last_probe_time.setter
    def last_probe_time(self, last_probe_time):
        r"""Sets the last_probe_time of this NodePoolCondition.

        上次状态检查时间。

        :param last_probe_time: The last_probe_time of this NodePoolCondition.
        :type last_probe_time: str
        """
        self._last_probe_time = last_probe_time

    @property
    def last_transit_time(self):
        r"""Gets the last_transit_time of this NodePoolCondition.

        上次状态变更时间。

        :return: The last_transit_time of this NodePoolCondition.
        :rtype: str
        """
        return self._last_transit_time

    @last_transit_time.setter
    def last_transit_time(self, last_transit_time):
        r"""Sets the last_transit_time of this NodePoolCondition.

        上次状态变更时间。

        :param last_transit_time: The last_transit_time of this NodePoolCondition.
        :type last_transit_time: str
        """
        self._last_transit_time = last_transit_time

    @property
    def reason(self):
        r"""Gets the reason of this NodePoolCondition.

        上次状态变更原因。

        :return: The reason of this NodePoolCondition.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this NodePoolCondition.

        上次状态变更原因。

        :param reason: The reason of this NodePoolCondition.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        r"""Gets the message of this NodePoolCondition.

        Condition详细描述。

        :return: The message of this NodePoolCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this NodePoolCondition.

        Condition详细描述。

        :param message: The message of this NodePoolCondition.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, NodePoolCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
