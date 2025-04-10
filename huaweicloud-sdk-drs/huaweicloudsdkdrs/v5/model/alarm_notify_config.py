# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmNotifyConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_to_user': 'bool',
        'topic_urn': 'str',
        'delay_time': 'int',
        'rpo_delay': 'int',
        'rto_delay': 'int'
    }

    attribute_map = {
        'alarm_to_user': 'alarm_to_user',
        'topic_urn': 'topic_urn',
        'delay_time': 'delay_time',
        'rpo_delay': 'rpo_delay',
        'rto_delay': 'rto_delay'
    }

    def __init__(self, alarm_to_user=None, topic_urn=None, delay_time=None, rpo_delay=None, rto_delay=None):
        r"""AlarmNotifyConfig

        The model defined in huaweicloud sdk

        :param alarm_to_user: 异常告警是否通知用户。
        :type alarm_to_user: bool
        :param topic_urn: SMN主题URN。
        :type topic_urn: str
        :param delay_time: 时延阈值(单位为s)。取值： - 最小值：1 - 最大值：3600 - 缺省值：0 - 说明： 1.源数据库和目标数据库之间的同步有时会存在一个时间差，称为时延，单位为秒。 2.时延阈值设置是指时延超过一定的值并持续6分钟后，DRS可以发送通知给指定收件人。（初次进入增量迁移阶段，会有较多数据等待同步，存在较大的时延，属于正常情况，不在此功能的监控范围之内。） 3.只有全量+增量的任务支持此选项。
        :type delay_time: int
        :param rpo_delay: RPO时延阈值(单位为s)。取值： - 最小值：1 - 最大值：3600 - 缺省值：0 - 说明： RPO时延阈值设置是业务数据库与DRS实例间同步的时延超过一定的值并持续6分钟后，DRS可以发送通知给指定收件人。（初次进入增量灾备阶段，会有较多数据等待同步，存在较大的时延，属于正常情况，不在此功能的监控范围之内。）
        :type rpo_delay: int
        :param rto_delay: RTO时延阈值(s)。取值： - 最小值：1 - 最大值：3600 - 缺省值：0 - 说明： RTO时延阈值设置是DRS实例与灾备数据库间同步的时延超过一定的值并持续6分钟后，DRS可以发送通知给指定收件人。
        :type rto_delay: int
        """
        
        

        self._alarm_to_user = None
        self._topic_urn = None
        self._delay_time = None
        self._rpo_delay = None
        self._rto_delay = None
        self.discriminator = None

        self.alarm_to_user = alarm_to_user
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if delay_time is not None:
            self.delay_time = delay_time
        if rpo_delay is not None:
            self.rpo_delay = rpo_delay
        if rto_delay is not None:
            self.rto_delay = rto_delay

    @property
    def alarm_to_user(self):
        r"""Gets the alarm_to_user of this AlarmNotifyConfig.

        异常告警是否通知用户。

        :return: The alarm_to_user of this AlarmNotifyConfig.
        :rtype: bool
        """
        return self._alarm_to_user

    @alarm_to_user.setter
    def alarm_to_user(self, alarm_to_user):
        r"""Sets the alarm_to_user of this AlarmNotifyConfig.

        异常告警是否通知用户。

        :param alarm_to_user: The alarm_to_user of this AlarmNotifyConfig.
        :type alarm_to_user: bool
        """
        self._alarm_to_user = alarm_to_user

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this AlarmNotifyConfig.

        SMN主题URN。

        :return: The topic_urn of this AlarmNotifyConfig.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this AlarmNotifyConfig.

        SMN主题URN。

        :param topic_urn: The topic_urn of this AlarmNotifyConfig.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def delay_time(self):
        r"""Gets the delay_time of this AlarmNotifyConfig.

        时延阈值(单位为s)。取值： - 最小值：1 - 最大值：3600 - 缺省值：0 - 说明： 1.源数据库和目标数据库之间的同步有时会存在一个时间差，称为时延，单位为秒。 2.时延阈值设置是指时延超过一定的值并持续6分钟后，DRS可以发送通知给指定收件人。（初次进入增量迁移阶段，会有较多数据等待同步，存在较大的时延，属于正常情况，不在此功能的监控范围之内。） 3.只有全量+增量的任务支持此选项。

        :return: The delay_time of this AlarmNotifyConfig.
        :rtype: int
        """
        return self._delay_time

    @delay_time.setter
    def delay_time(self, delay_time):
        r"""Sets the delay_time of this AlarmNotifyConfig.

        时延阈值(单位为s)。取值： - 最小值：1 - 最大值：3600 - 缺省值：0 - 说明： 1.源数据库和目标数据库之间的同步有时会存在一个时间差，称为时延，单位为秒。 2.时延阈值设置是指时延超过一定的值并持续6分钟后，DRS可以发送通知给指定收件人。（初次进入增量迁移阶段，会有较多数据等待同步，存在较大的时延，属于正常情况，不在此功能的监控范围之内。） 3.只有全量+增量的任务支持此选项。

        :param delay_time: The delay_time of this AlarmNotifyConfig.
        :type delay_time: int
        """
        self._delay_time = delay_time

    @property
    def rpo_delay(self):
        r"""Gets the rpo_delay of this AlarmNotifyConfig.

        RPO时延阈值(单位为s)。取值： - 最小值：1 - 最大值：3600 - 缺省值：0 - 说明： RPO时延阈值设置是业务数据库与DRS实例间同步的时延超过一定的值并持续6分钟后，DRS可以发送通知给指定收件人。（初次进入增量灾备阶段，会有较多数据等待同步，存在较大的时延，属于正常情况，不在此功能的监控范围之内。）

        :return: The rpo_delay of this AlarmNotifyConfig.
        :rtype: int
        """
        return self._rpo_delay

    @rpo_delay.setter
    def rpo_delay(self, rpo_delay):
        r"""Sets the rpo_delay of this AlarmNotifyConfig.

        RPO时延阈值(单位为s)。取值： - 最小值：1 - 最大值：3600 - 缺省值：0 - 说明： RPO时延阈值设置是业务数据库与DRS实例间同步的时延超过一定的值并持续6分钟后，DRS可以发送通知给指定收件人。（初次进入增量灾备阶段，会有较多数据等待同步，存在较大的时延，属于正常情况，不在此功能的监控范围之内。）

        :param rpo_delay: The rpo_delay of this AlarmNotifyConfig.
        :type rpo_delay: int
        """
        self._rpo_delay = rpo_delay

    @property
    def rto_delay(self):
        r"""Gets the rto_delay of this AlarmNotifyConfig.

        RTO时延阈值(s)。取值： - 最小值：1 - 最大值：3600 - 缺省值：0 - 说明： RTO时延阈值设置是DRS实例与灾备数据库间同步的时延超过一定的值并持续6分钟后，DRS可以发送通知给指定收件人。

        :return: The rto_delay of this AlarmNotifyConfig.
        :rtype: int
        """
        return self._rto_delay

    @rto_delay.setter
    def rto_delay(self, rto_delay):
        r"""Sets the rto_delay of this AlarmNotifyConfig.

        RTO时延阈值(s)。取值： - 最小值：1 - 最大值：3600 - 缺省值：0 - 说明： RTO时延阈值设置是DRS实例与灾备数据库间同步的时延超过一定的值并持续6分钟后，DRS可以发送通知给指定收件人。

        :param rto_delay: The rto_delay of this AlarmNotifyConfig.
        :type rto_delay: int
        """
        self._rto_delay = rto_delay

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
        if not isinstance(other, AlarmNotifyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
