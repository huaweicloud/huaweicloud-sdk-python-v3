# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSmnSubscriptionDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_name': 'str',
        'topic_urn': 'str',
        'delay_time': 'int',
        'rpo_delay': 'int',
        'rto_delay': 'int',
        'is_alarm_user': 'bool'
    }

    attribute_map = {
        'topic_name': 'topic_name',
        'topic_urn': 'topic_urn',
        'delay_time': 'delay_time',
        'rpo_delay': 'rpo_delay',
        'rto_delay': 'rto_delay',
        'is_alarm_user': 'is_alarm_user'
    }

    def __init__(self, topic_name=None, topic_urn=None, delay_time=None, rpo_delay=None, rto_delay=None, is_alarm_user=None):
        r"""ShowSmnSubscriptionDetailResponse

        The model defined in huaweicloud sdk

        :param topic_name: SMN主题名称
        :type topic_name: str
        :param topic_urn: SMN主题的唯一资源标识
        :type topic_urn: str
        :param delay_time: 延迟时间，单位秒
        :type delay_time: int
        :param rpo_delay: RPO延迟时间，单位秒
        :type rpo_delay: int
        :param rto_delay: RTO延迟时间，单位秒
        :type rto_delay: int
        :param is_alarm_user: 是否发送告警给订阅用户
        :type is_alarm_user: bool
        """
        
        super().__init__()

        self._topic_name = None
        self._topic_urn = None
        self._delay_time = None
        self._rpo_delay = None
        self._rto_delay = None
        self._is_alarm_user = None
        self.discriminator = None

        if topic_name is not None:
            self.topic_name = topic_name
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if delay_time is not None:
            self.delay_time = delay_time
        if rpo_delay is not None:
            self.rpo_delay = rpo_delay
        if rto_delay is not None:
            self.rto_delay = rto_delay
        if is_alarm_user is not None:
            self.is_alarm_user = is_alarm_user

    @property
    def topic_name(self):
        r"""Gets the topic_name of this ShowSmnSubscriptionDetailResponse.

        SMN主题名称

        :return: The topic_name of this ShowSmnSubscriptionDetailResponse.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        r"""Sets the topic_name of this ShowSmnSubscriptionDetailResponse.

        SMN主题名称

        :param topic_name: The topic_name of this ShowSmnSubscriptionDetailResponse.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ShowSmnSubscriptionDetailResponse.

        SMN主题的唯一资源标识

        :return: The topic_urn of this ShowSmnSubscriptionDetailResponse.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ShowSmnSubscriptionDetailResponse.

        SMN主题的唯一资源标识

        :param topic_urn: The topic_urn of this ShowSmnSubscriptionDetailResponse.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def delay_time(self):
        r"""Gets the delay_time of this ShowSmnSubscriptionDetailResponse.

        延迟时间，单位秒

        :return: The delay_time of this ShowSmnSubscriptionDetailResponse.
        :rtype: int
        """
        return self._delay_time

    @delay_time.setter
    def delay_time(self, delay_time):
        r"""Sets the delay_time of this ShowSmnSubscriptionDetailResponse.

        延迟时间，单位秒

        :param delay_time: The delay_time of this ShowSmnSubscriptionDetailResponse.
        :type delay_time: int
        """
        self._delay_time = delay_time

    @property
    def rpo_delay(self):
        r"""Gets the rpo_delay of this ShowSmnSubscriptionDetailResponse.

        RPO延迟时间，单位秒

        :return: The rpo_delay of this ShowSmnSubscriptionDetailResponse.
        :rtype: int
        """
        return self._rpo_delay

    @rpo_delay.setter
    def rpo_delay(self, rpo_delay):
        r"""Sets the rpo_delay of this ShowSmnSubscriptionDetailResponse.

        RPO延迟时间，单位秒

        :param rpo_delay: The rpo_delay of this ShowSmnSubscriptionDetailResponse.
        :type rpo_delay: int
        """
        self._rpo_delay = rpo_delay

    @property
    def rto_delay(self):
        r"""Gets the rto_delay of this ShowSmnSubscriptionDetailResponse.

        RTO延迟时间，单位秒

        :return: The rto_delay of this ShowSmnSubscriptionDetailResponse.
        :rtype: int
        """
        return self._rto_delay

    @rto_delay.setter
    def rto_delay(self, rto_delay):
        r"""Sets the rto_delay of this ShowSmnSubscriptionDetailResponse.

        RTO延迟时间，单位秒

        :param rto_delay: The rto_delay of this ShowSmnSubscriptionDetailResponse.
        :type rto_delay: int
        """
        self._rto_delay = rto_delay

    @property
    def is_alarm_user(self):
        r"""Gets the is_alarm_user of this ShowSmnSubscriptionDetailResponse.

        是否发送告警给订阅用户

        :return: The is_alarm_user of this ShowSmnSubscriptionDetailResponse.
        :rtype: bool
        """
        return self._is_alarm_user

    @is_alarm_user.setter
    def is_alarm_user(self, is_alarm_user):
        r"""Sets the is_alarm_user of this ShowSmnSubscriptionDetailResponse.

        是否发送告警给订阅用户

        :param is_alarm_user: The is_alarm_user of this ShowSmnSubscriptionDetailResponse.
        :type is_alarm_user: bool
        """
        self._is_alarm_user = is_alarm_user

    def to_dict(self):
        import warnings
        warnings.warn("ShowSmnSubscriptionDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowSmnSubscriptionDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
