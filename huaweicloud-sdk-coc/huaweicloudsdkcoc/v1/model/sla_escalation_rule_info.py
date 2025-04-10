# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlaEscalationRuleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'day': 'int',
        'hour': 'int',
        'minute': 'int',
        'order': 'int',
        'protocol': 'str',
        'notification_obj_configuration': 'list[NotificationObjConfiguration]'
    }

    attribute_map = {
        'day': 'day',
        'hour': 'hour',
        'minute': 'minute',
        'order': 'order',
        'protocol': 'protocol',
        'notification_obj_configuration': 'notification_obj_configuration'
    }

    def __init__(self, day=None, hour=None, minute=None, order=None, protocol=None, notification_obj_configuration=None):
        r"""SlaEscalationRuleInfo

        The model defined in huaweicloud sdk

        :param day: 天
        :type day: int
        :param hour: 小时
        :type hour: int
        :param minute: 分钟
        :type minute: int
        :param order: 顺序
        :type order: int
        :param protocol: 通知类型
        :type protocol: str
        :param notification_obj_configuration: 通知配置
        :type notification_obj_configuration: list[:class:`huaweicloudsdkcoc.v1.NotificationObjConfiguration`]
        """
        
        

        self._day = None
        self._hour = None
        self._minute = None
        self._order = None
        self._protocol = None
        self._notification_obj_configuration = None
        self.discriminator = None

        if day is not None:
            self.day = day
        if hour is not None:
            self.hour = hour
        if minute is not None:
            self.minute = minute
        if order is not None:
            self.order = order
        if protocol is not None:
            self.protocol = protocol
        if notification_obj_configuration is not None:
            self.notification_obj_configuration = notification_obj_configuration

    @property
    def day(self):
        r"""Gets the day of this SlaEscalationRuleInfo.

        天

        :return: The day of this SlaEscalationRuleInfo.
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        r"""Sets the day of this SlaEscalationRuleInfo.

        天

        :param day: The day of this SlaEscalationRuleInfo.
        :type day: int
        """
        self._day = day

    @property
    def hour(self):
        r"""Gets the hour of this SlaEscalationRuleInfo.

        小时

        :return: The hour of this SlaEscalationRuleInfo.
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        r"""Sets the hour of this SlaEscalationRuleInfo.

        小时

        :param hour: The hour of this SlaEscalationRuleInfo.
        :type hour: int
        """
        self._hour = hour

    @property
    def minute(self):
        r"""Gets the minute of this SlaEscalationRuleInfo.

        分钟

        :return: The minute of this SlaEscalationRuleInfo.
        :rtype: int
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        r"""Sets the minute of this SlaEscalationRuleInfo.

        分钟

        :param minute: The minute of this SlaEscalationRuleInfo.
        :type minute: int
        """
        self._minute = minute

    @property
    def order(self):
        r"""Gets the order of this SlaEscalationRuleInfo.

        顺序

        :return: The order of this SlaEscalationRuleInfo.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this SlaEscalationRuleInfo.

        顺序

        :param order: The order of this SlaEscalationRuleInfo.
        :type order: int
        """
        self._order = order

    @property
    def protocol(self):
        r"""Gets the protocol of this SlaEscalationRuleInfo.

        通知类型

        :return: The protocol of this SlaEscalationRuleInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this SlaEscalationRuleInfo.

        通知类型

        :param protocol: The protocol of this SlaEscalationRuleInfo.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def notification_obj_configuration(self):
        r"""Gets the notification_obj_configuration of this SlaEscalationRuleInfo.

        通知配置

        :return: The notification_obj_configuration of this SlaEscalationRuleInfo.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.NotificationObjConfiguration`]
        """
        return self._notification_obj_configuration

    @notification_obj_configuration.setter
    def notification_obj_configuration(self, notification_obj_configuration):
        r"""Sets the notification_obj_configuration of this SlaEscalationRuleInfo.

        通知配置

        :param notification_obj_configuration: The notification_obj_configuration of this SlaEscalationRuleInfo.
        :type notification_obj_configuration: list[:class:`huaweicloudsdkcoc.v1.NotificationObjConfiguration`]
        """
        self._notification_obj_configuration = notification_obj_configuration

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
        if not isinstance(other, SlaEscalationRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
