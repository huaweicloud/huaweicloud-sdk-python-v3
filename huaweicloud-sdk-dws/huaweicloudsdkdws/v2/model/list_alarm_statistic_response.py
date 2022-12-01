# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_statistics': 'list[AlarmStatisticResponse]'
    }

    attribute_map = {
        'alarm_statistics': 'alarm_statistics'
    }

    def __init__(self, alarm_statistics=None):
        """ListAlarmStatisticResponse

        The model defined in huaweicloud sdk

        :param alarm_statistics: 告警统计列表
        :type alarm_statistics: list[:class:`huaweicloudsdkdws.v2.AlarmStatisticResponse`]
        """
        
        super(ListAlarmStatisticResponse, self).__init__()

        self._alarm_statistics = None
        self.discriminator = None

        if alarm_statistics is not None:
            self.alarm_statistics = alarm_statistics

    @property
    def alarm_statistics(self):
        """Gets the alarm_statistics of this ListAlarmStatisticResponse.

        告警统计列表

        :return: The alarm_statistics of this ListAlarmStatisticResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.AlarmStatisticResponse`]
        """
        return self._alarm_statistics

    @alarm_statistics.setter
    def alarm_statistics(self, alarm_statistics):
        """Sets the alarm_statistics of this ListAlarmStatisticResponse.

        告警统计列表

        :param alarm_statistics: The alarm_statistics of this ListAlarmStatisticResponse.
        :type alarm_statistics: list[:class:`huaweicloudsdkdws.v2.AlarmStatisticResponse`]
        """
        self._alarm_statistics = alarm_statistics

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
        if not isinstance(other, ListAlarmStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
