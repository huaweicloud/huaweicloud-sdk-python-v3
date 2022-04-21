# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySmnInfoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'subscriptions': 'list[SubscriptionInfo]',
        'topic_name': 'str',
        'delay_time': 'int',
        'rto_delay': 'int',
        'rpo_delay': 'int',
        'alarm_to_user': 'bool'
    }

    attribute_map = {
        'subscriptions': 'subscriptions',
        'topic_name': 'topic_name',
        'delay_time': 'delay_time',
        'rto_delay': 'rto_delay',
        'rpo_delay': 'rpo_delay',
        'alarm_to_user': 'alarm_to_user'
    }

    def __init__(self, subscriptions=None, topic_name=None, delay_time=None, rto_delay=None, rpo_delay=None, alarm_to_user=None):
        """QuerySmnInfoResp

        The model defined in huaweicloud sdk

        :param subscriptions: SMN信息
        :type subscriptions: list[:class:`huaweicloudsdkdrs.v3.SubscriptionInfo`]
        :param topic_name: 主题名称
        :type topic_name: str
        :param delay_time: 订阅延迟时间
        :type delay_time: int
        :param rto_delay: rto延迟时间
        :type rto_delay: int
        :param rpo_delay: rpo延迟时间
        :type rpo_delay: int
        :param alarm_to_user: 异常告警是否通知用户
        :type alarm_to_user: bool
        """
        
        

        self._subscriptions = None
        self._topic_name = None
        self._delay_time = None
        self._rto_delay = None
        self._rpo_delay = None
        self._alarm_to_user = None
        self.discriminator = None

        if subscriptions is not None:
            self.subscriptions = subscriptions
        if topic_name is not None:
            self.topic_name = topic_name
        if delay_time is not None:
            self.delay_time = delay_time
        if rto_delay is not None:
            self.rto_delay = rto_delay
        if rpo_delay is not None:
            self.rpo_delay = rpo_delay
        if alarm_to_user is not None:
            self.alarm_to_user = alarm_to_user

    @property
    def subscriptions(self):
        """Gets the subscriptions of this QuerySmnInfoResp.

        SMN信息

        :return: The subscriptions of this QuerySmnInfoResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.SubscriptionInfo`]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this QuerySmnInfoResp.

        SMN信息

        :param subscriptions: The subscriptions of this QuerySmnInfoResp.
        :type subscriptions: list[:class:`huaweicloudsdkdrs.v3.SubscriptionInfo`]
        """
        self._subscriptions = subscriptions

    @property
    def topic_name(self):
        """Gets the topic_name of this QuerySmnInfoResp.

        主题名称

        :return: The topic_name of this QuerySmnInfoResp.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this QuerySmnInfoResp.

        主题名称

        :param topic_name: The topic_name of this QuerySmnInfoResp.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def delay_time(self):
        """Gets the delay_time of this QuerySmnInfoResp.

        订阅延迟时间

        :return: The delay_time of this QuerySmnInfoResp.
        :rtype: int
        """
        return self._delay_time

    @delay_time.setter
    def delay_time(self, delay_time):
        """Sets the delay_time of this QuerySmnInfoResp.

        订阅延迟时间

        :param delay_time: The delay_time of this QuerySmnInfoResp.
        :type delay_time: int
        """
        self._delay_time = delay_time

    @property
    def rto_delay(self):
        """Gets the rto_delay of this QuerySmnInfoResp.

        rto延迟时间

        :return: The rto_delay of this QuerySmnInfoResp.
        :rtype: int
        """
        return self._rto_delay

    @rto_delay.setter
    def rto_delay(self, rto_delay):
        """Sets the rto_delay of this QuerySmnInfoResp.

        rto延迟时间

        :param rto_delay: The rto_delay of this QuerySmnInfoResp.
        :type rto_delay: int
        """
        self._rto_delay = rto_delay

    @property
    def rpo_delay(self):
        """Gets the rpo_delay of this QuerySmnInfoResp.

        rpo延迟时间

        :return: The rpo_delay of this QuerySmnInfoResp.
        :rtype: int
        """
        return self._rpo_delay

    @rpo_delay.setter
    def rpo_delay(self, rpo_delay):
        """Sets the rpo_delay of this QuerySmnInfoResp.

        rpo延迟时间

        :param rpo_delay: The rpo_delay of this QuerySmnInfoResp.
        :type rpo_delay: int
        """
        self._rpo_delay = rpo_delay

    @property
    def alarm_to_user(self):
        """Gets the alarm_to_user of this QuerySmnInfoResp.

        异常告警是否通知用户

        :return: The alarm_to_user of this QuerySmnInfoResp.
        :rtype: bool
        """
        return self._alarm_to_user

    @alarm_to_user.setter
    def alarm_to_user(self, alarm_to_user):
        """Sets the alarm_to_user of this QuerySmnInfoResp.

        异常告警是否通知用户

        :param alarm_to_user: The alarm_to_user of this QuerySmnInfoResp.
        :type alarm_to_user: bool
        """
        self._alarm_to_user = alarm_to_user

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
        if not isinstance(other, QuerySmnInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
