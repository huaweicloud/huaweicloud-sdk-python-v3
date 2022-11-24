# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_data_list': 'list[AlarmDataVO]',
        'total_count': 'int'
    }

    attribute_map = {
        'alarm_data_list': 'alarm_data_list',
        'total_count': 'total_count'
    }

    def __init__(self, alarm_data_list=None, total_count=None):
        """ListAlarmDataResponse

        The model defined in huaweicloud sdk

        :param alarm_data_list: 告警列表。
        :type alarm_data_list: list[:class:`huaweicloudsdkapm.v1.AlarmDataVO`]
        :param total_count: 消息总数。
        :type total_count: int
        """
        
        super(ListAlarmDataResponse, self).__init__()

        self._alarm_data_list = None
        self._total_count = None
        self.discriminator = None

        if alarm_data_list is not None:
            self.alarm_data_list = alarm_data_list
        if total_count is not None:
            self.total_count = total_count

    @property
    def alarm_data_list(self):
        """Gets the alarm_data_list of this ListAlarmDataResponse.

        告警列表。

        :return: The alarm_data_list of this ListAlarmDataResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.AlarmDataVO`]
        """
        return self._alarm_data_list

    @alarm_data_list.setter
    def alarm_data_list(self, alarm_data_list):
        """Sets the alarm_data_list of this ListAlarmDataResponse.

        告警列表。

        :param alarm_data_list: The alarm_data_list of this ListAlarmDataResponse.
        :type alarm_data_list: list[:class:`huaweicloudsdkapm.v1.AlarmDataVO`]
        """
        self._alarm_data_list = alarm_data_list

    @property
    def total_count(self):
        """Gets the total_count of this ListAlarmDataResponse.

        消息总数。

        :return: The total_count of this ListAlarmDataResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListAlarmDataResponse.

        消息总数。

        :param total_count: The total_count of this ListAlarmDataResponse.
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
        if not isinstance(other, ListAlarmDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
