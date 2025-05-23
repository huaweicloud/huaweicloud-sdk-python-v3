# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmNotifyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delay_time': 'int',
        'rto_delay': 'int',
        'rpo_delay': 'int',
        'alarm_to_user': 'bool',
        'subscriptions': 'list[SubscriptionInfo]'
    }

    attribute_map = {
        'delay_time': 'delay_time',
        'rto_delay': 'rto_delay',
        'rpo_delay': 'rpo_delay',
        'alarm_to_user': 'alarm_to_user',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, delay_time=None, rto_delay=None, rpo_delay=None, alarm_to_user=None, subscriptions=None):
        r"""AlarmNotifyInfo

        The model defined in huaweicloud sdk

        :param delay_time: 订阅延迟时间(单位为s)
        :type delay_time: int
        :param rto_delay: rto延迟时间
        :type rto_delay: int
        :param rpo_delay: rpo延迟时间
        :type rpo_delay: int
        :param alarm_to_user: 异常告警是否通知用户
        :type alarm_to_user: bool
        :param subscriptions: 收件方式与信息体
        :type subscriptions: list[:class:`huaweicloudsdkdrs.v3.SubscriptionInfo`]
        """
        
        

        self._delay_time = None
        self._rto_delay = None
        self._rpo_delay = None
        self._alarm_to_user = None
        self._subscriptions = None
        self.discriminator = None

        if delay_time is not None:
            self.delay_time = delay_time
        if rto_delay is not None:
            self.rto_delay = rto_delay
        if rpo_delay is not None:
            self.rpo_delay = rpo_delay
        if alarm_to_user is not None:
            self.alarm_to_user = alarm_to_user
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def delay_time(self):
        r"""Gets the delay_time of this AlarmNotifyInfo.

        订阅延迟时间(单位为s)

        :return: The delay_time of this AlarmNotifyInfo.
        :rtype: int
        """
        return self._delay_time

    @delay_time.setter
    def delay_time(self, delay_time):
        r"""Sets the delay_time of this AlarmNotifyInfo.

        订阅延迟时间(单位为s)

        :param delay_time: The delay_time of this AlarmNotifyInfo.
        :type delay_time: int
        """
        self._delay_time = delay_time

    @property
    def rto_delay(self):
        r"""Gets the rto_delay of this AlarmNotifyInfo.

        rto延迟时间

        :return: The rto_delay of this AlarmNotifyInfo.
        :rtype: int
        """
        return self._rto_delay

    @rto_delay.setter
    def rto_delay(self, rto_delay):
        r"""Sets the rto_delay of this AlarmNotifyInfo.

        rto延迟时间

        :param rto_delay: The rto_delay of this AlarmNotifyInfo.
        :type rto_delay: int
        """
        self._rto_delay = rto_delay

    @property
    def rpo_delay(self):
        r"""Gets the rpo_delay of this AlarmNotifyInfo.

        rpo延迟时间

        :return: The rpo_delay of this AlarmNotifyInfo.
        :rtype: int
        """
        return self._rpo_delay

    @rpo_delay.setter
    def rpo_delay(self, rpo_delay):
        r"""Sets the rpo_delay of this AlarmNotifyInfo.

        rpo延迟时间

        :param rpo_delay: The rpo_delay of this AlarmNotifyInfo.
        :type rpo_delay: int
        """
        self._rpo_delay = rpo_delay

    @property
    def alarm_to_user(self):
        r"""Gets the alarm_to_user of this AlarmNotifyInfo.

        异常告警是否通知用户

        :return: The alarm_to_user of this AlarmNotifyInfo.
        :rtype: bool
        """
        return self._alarm_to_user

    @alarm_to_user.setter
    def alarm_to_user(self, alarm_to_user):
        r"""Sets the alarm_to_user of this AlarmNotifyInfo.

        异常告警是否通知用户

        :param alarm_to_user: The alarm_to_user of this AlarmNotifyInfo.
        :type alarm_to_user: bool
        """
        self._alarm_to_user = alarm_to_user

    @property
    def subscriptions(self):
        r"""Gets the subscriptions of this AlarmNotifyInfo.

        收件方式与信息体

        :return: The subscriptions of this AlarmNotifyInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.SubscriptionInfo`]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        r"""Sets the subscriptions of this AlarmNotifyInfo.

        收件方式与信息体

        :param subscriptions: The subscriptions of this AlarmNotifyInfo.
        :type subscriptions: list[:class:`huaweicloudsdkdrs.v3.SubscriptionInfo`]
        """
        self._subscriptions = subscriptions

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
        if not isinstance(other, AlarmNotifyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
