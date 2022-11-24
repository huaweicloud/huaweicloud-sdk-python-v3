# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmNotifyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'front_alarm_notify_results': 'list[FrontAlarmNotifyResult]',
        'total_count': 'int'
    }

    attribute_map = {
        'front_alarm_notify_results': 'front_alarm_notify_results',
        'total_count': 'total_count'
    }

    def __init__(self, front_alarm_notify_results=None, total_count=None):
        """ListAlarmNotifyResponse

        The model defined in huaweicloud sdk

        :param front_alarm_notify_results: 告警通知列表。
        :type front_alarm_notify_results: list[:class:`huaweicloudsdkapm.v1.FrontAlarmNotifyResult`]
        :param total_count: 消息总数。
        :type total_count: int
        """
        
        super(ListAlarmNotifyResponse, self).__init__()

        self._front_alarm_notify_results = None
        self._total_count = None
        self.discriminator = None

        if front_alarm_notify_results is not None:
            self.front_alarm_notify_results = front_alarm_notify_results
        if total_count is not None:
            self.total_count = total_count

    @property
    def front_alarm_notify_results(self):
        """Gets the front_alarm_notify_results of this ListAlarmNotifyResponse.

        告警通知列表。

        :return: The front_alarm_notify_results of this ListAlarmNotifyResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.FrontAlarmNotifyResult`]
        """
        return self._front_alarm_notify_results

    @front_alarm_notify_results.setter
    def front_alarm_notify_results(self, front_alarm_notify_results):
        """Sets the front_alarm_notify_results of this ListAlarmNotifyResponse.

        告警通知列表。

        :param front_alarm_notify_results: The front_alarm_notify_results of this ListAlarmNotifyResponse.
        :type front_alarm_notify_results: list[:class:`huaweicloudsdkapm.v1.FrontAlarmNotifyResult`]
        """
        self._front_alarm_notify_results = front_alarm_notify_results

    @property
    def total_count(self):
        """Gets the total_count of this ListAlarmNotifyResponse.

        消息总数。

        :return: The total_count of this ListAlarmNotifyResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListAlarmNotifyResponse.

        消息总数。

        :param total_count: The total_count of this ListAlarmNotifyResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListAlarmNotifyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
