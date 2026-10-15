# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateSmnTopicReqV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_urn': 'str',
        'increment_delay_threshold': 'int',
        'rto_delay_threshold': 'int',
        'rpo_delay_threshold': 'int',
        'is_alarm_to_user': 'bool'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'increment_delay_threshold': 'increment_delay_threshold',
        'rto_delay_threshold': 'rto_delay_threshold',
        'rpo_delay_threshold': 'rpo_delay_threshold',
        'is_alarm_to_user': 'is_alarm_to_user'
    }

    def __init__(self, topic_urn=None, increment_delay_threshold=None, rto_delay_threshold=None, rpo_delay_threshold=None, is_alarm_to_user=None):
        r"""AssociateSmnTopicReqV5

        The model defined in huaweicloud sdk

        :param topic_urn: 主题资源标识
        :type topic_urn: str
        :param increment_delay_threshold: 增量时延阈值, 单位：秒（s）
        :type increment_delay_threshold: int
        :param rto_delay_threshold: RTO时延阈值，灾备场景下可配置，单位：秒（s）
        :type rto_delay_threshold: int
        :param rpo_delay_threshold: RPO时延阈值，灾备场景下可配置，单位：秒（s）
        :type rpo_delay_threshold: int
        :param is_alarm_to_user: 异常告警是否通知用户，取值范围[true,false]
        :type is_alarm_to_user: bool
        """
        
        

        self._topic_urn = None
        self._increment_delay_threshold = None
        self._rto_delay_threshold = None
        self._rpo_delay_threshold = None
        self._is_alarm_to_user = None
        self.discriminator = None

        self.topic_urn = topic_urn
        if increment_delay_threshold is not None:
            self.increment_delay_threshold = increment_delay_threshold
        if rto_delay_threshold is not None:
            self.rto_delay_threshold = rto_delay_threshold
        if rpo_delay_threshold is not None:
            self.rpo_delay_threshold = rpo_delay_threshold
        self.is_alarm_to_user = is_alarm_to_user

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this AssociateSmnTopicReqV5.

        主题资源标识

        :return: The topic_urn of this AssociateSmnTopicReqV5.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this AssociateSmnTopicReqV5.

        主题资源标识

        :param topic_urn: The topic_urn of this AssociateSmnTopicReqV5.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def increment_delay_threshold(self):
        r"""Gets the increment_delay_threshold of this AssociateSmnTopicReqV5.

        增量时延阈值, 单位：秒（s）

        :return: The increment_delay_threshold of this AssociateSmnTopicReqV5.
        :rtype: int
        """
        return self._increment_delay_threshold

    @increment_delay_threshold.setter
    def increment_delay_threshold(self, increment_delay_threshold):
        r"""Sets the increment_delay_threshold of this AssociateSmnTopicReqV5.

        增量时延阈值, 单位：秒（s）

        :param increment_delay_threshold: The increment_delay_threshold of this AssociateSmnTopicReqV5.
        :type increment_delay_threshold: int
        """
        self._increment_delay_threshold = increment_delay_threshold

    @property
    def rto_delay_threshold(self):
        r"""Gets the rto_delay_threshold of this AssociateSmnTopicReqV5.

        RTO时延阈值，灾备场景下可配置，单位：秒（s）

        :return: The rto_delay_threshold of this AssociateSmnTopicReqV5.
        :rtype: int
        """
        return self._rto_delay_threshold

    @rto_delay_threshold.setter
    def rto_delay_threshold(self, rto_delay_threshold):
        r"""Sets the rto_delay_threshold of this AssociateSmnTopicReqV5.

        RTO时延阈值，灾备场景下可配置，单位：秒（s）

        :param rto_delay_threshold: The rto_delay_threshold of this AssociateSmnTopicReqV5.
        :type rto_delay_threshold: int
        """
        self._rto_delay_threshold = rto_delay_threshold

    @property
    def rpo_delay_threshold(self):
        r"""Gets the rpo_delay_threshold of this AssociateSmnTopicReqV5.

        RPO时延阈值，灾备场景下可配置，单位：秒（s）

        :return: The rpo_delay_threshold of this AssociateSmnTopicReqV5.
        :rtype: int
        """
        return self._rpo_delay_threshold

    @rpo_delay_threshold.setter
    def rpo_delay_threshold(self, rpo_delay_threshold):
        r"""Sets the rpo_delay_threshold of this AssociateSmnTopicReqV5.

        RPO时延阈值，灾备场景下可配置，单位：秒（s）

        :param rpo_delay_threshold: The rpo_delay_threshold of this AssociateSmnTopicReqV5.
        :type rpo_delay_threshold: int
        """
        self._rpo_delay_threshold = rpo_delay_threshold

    @property
    def is_alarm_to_user(self):
        r"""Gets the is_alarm_to_user of this AssociateSmnTopicReqV5.

        异常告警是否通知用户，取值范围[true,false]

        :return: The is_alarm_to_user of this AssociateSmnTopicReqV5.
        :rtype: bool
        """
        return self._is_alarm_to_user

    @is_alarm_to_user.setter
    def is_alarm_to_user(self, is_alarm_to_user):
        r"""Sets the is_alarm_to_user of this AssociateSmnTopicReqV5.

        异常告警是否通知用户，取值范围[true,false]

        :param is_alarm_to_user: The is_alarm_to_user of this AssociateSmnTopicReqV5.
        :type is_alarm_to_user: bool
        """
        self._is_alarm_to_user = is_alarm_to_user

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
        if not isinstance(other, AssociateSmnTopicReqV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
