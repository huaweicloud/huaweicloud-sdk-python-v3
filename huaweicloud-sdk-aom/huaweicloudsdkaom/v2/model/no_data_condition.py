# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoDataCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'no_data_timeframe': 'int',
        'no_data_alert_state': 'str',
        'notify_no_data': 'bool'
    }

    attribute_map = {
        'no_data_timeframe': 'no_data_timeframe',
        'no_data_alert_state': 'no_data_alert_state',
        'notify_no_data': 'notify_no_data'
    }

    def __init__(self, no_data_timeframe=None, no_data_alert_state=None, notify_no_data=None):
        """NoDataCondition

        The model defined in huaweicloud sdk

        :param no_data_timeframe: 无数据周期的个数。
        :type no_data_timeframe: int
        :param no_data_alert_state: 数据不足时，阈值规则的状态。 - “no_data”：数据不足并发送通知 - “alerting”：告警 - “ok”：正常 - “pre_state”：保持上一个状态
        :type no_data_alert_state: str
        :param notify_no_data: 数据不足是否通知。
        :type notify_no_data: bool
        """
        
        

        self._no_data_timeframe = None
        self._no_data_alert_state = None
        self._notify_no_data = None
        self.discriminator = None

        if no_data_timeframe is not None:
            self.no_data_timeframe = no_data_timeframe
        if no_data_alert_state is not None:
            self.no_data_alert_state = no_data_alert_state
        if notify_no_data is not None:
            self.notify_no_data = notify_no_data

    @property
    def no_data_timeframe(self):
        """Gets the no_data_timeframe of this NoDataCondition.

        无数据周期的个数。

        :return: The no_data_timeframe of this NoDataCondition.
        :rtype: int
        """
        return self._no_data_timeframe

    @no_data_timeframe.setter
    def no_data_timeframe(self, no_data_timeframe):
        """Sets the no_data_timeframe of this NoDataCondition.

        无数据周期的个数。

        :param no_data_timeframe: The no_data_timeframe of this NoDataCondition.
        :type no_data_timeframe: int
        """
        self._no_data_timeframe = no_data_timeframe

    @property
    def no_data_alert_state(self):
        """Gets the no_data_alert_state of this NoDataCondition.

        数据不足时，阈值规则的状态。 - “no_data”：数据不足并发送通知 - “alerting”：告警 - “ok”：正常 - “pre_state”：保持上一个状态

        :return: The no_data_alert_state of this NoDataCondition.
        :rtype: str
        """
        return self._no_data_alert_state

    @no_data_alert_state.setter
    def no_data_alert_state(self, no_data_alert_state):
        """Sets the no_data_alert_state of this NoDataCondition.

        数据不足时，阈值规则的状态。 - “no_data”：数据不足并发送通知 - “alerting”：告警 - “ok”：正常 - “pre_state”：保持上一个状态

        :param no_data_alert_state: The no_data_alert_state of this NoDataCondition.
        :type no_data_alert_state: str
        """
        self._no_data_alert_state = no_data_alert_state

    @property
    def notify_no_data(self):
        """Gets the notify_no_data of this NoDataCondition.

        数据不足是否通知。

        :return: The notify_no_data of this NoDataCondition.
        :rtype: bool
        """
        return self._notify_no_data

    @notify_no_data.setter
    def notify_no_data(self, notify_no_data):
        """Sets the notify_no_data of this NoDataCondition.

        数据不足是否通知。

        :param notify_no_data: The notify_no_data of this NoDataCondition.
        :type notify_no_data: bool
        """
        self._notify_no_data = notify_no_data

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
        if not isinstance(other, NoDataCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
