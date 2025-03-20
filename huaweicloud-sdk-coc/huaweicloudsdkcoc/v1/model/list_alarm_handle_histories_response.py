# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmHandleHistoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'alarm_handle_histories': 'list[AlarmHandleHistory]'
    }

    attribute_map = {
        'count': 'count',
        'alarm_handle_histories': 'alarm_handle_histories'
    }

    def __init__(self, count=None, alarm_handle_histories=None):
        """ListAlarmHandleHistoriesResponse

        The model defined in huaweicloud sdk

        :param count: 总数量
        :type count: int
        :param alarm_handle_histories: 告警工单执行结果
        :type alarm_handle_histories: list[:class:`huaweicloudsdkcoc.v1.AlarmHandleHistory`]
        """
        
        super(ListAlarmHandleHistoriesResponse, self).__init__()

        self._count = None
        self._alarm_handle_histories = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if alarm_handle_histories is not None:
            self.alarm_handle_histories = alarm_handle_histories

    @property
    def count(self):
        """Gets the count of this ListAlarmHandleHistoriesResponse.

        总数量

        :return: The count of this ListAlarmHandleHistoriesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAlarmHandleHistoriesResponse.

        总数量

        :param count: The count of this ListAlarmHandleHistoriesResponse.
        :type count: int
        """
        self._count = count

    @property
    def alarm_handle_histories(self):
        """Gets the alarm_handle_histories of this ListAlarmHandleHistoriesResponse.

        告警工单执行结果

        :return: The alarm_handle_histories of this ListAlarmHandleHistoriesResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.AlarmHandleHistory`]
        """
        return self._alarm_handle_histories

    @alarm_handle_histories.setter
    def alarm_handle_histories(self, alarm_handle_histories):
        """Sets the alarm_handle_histories of this ListAlarmHandleHistoriesResponse.

        告警工单执行结果

        :param alarm_handle_histories: The alarm_handle_histories of this ListAlarmHandleHistoriesResponse.
        :type alarm_handle_histories: list[:class:`huaweicloudsdkcoc.v1.AlarmHandleHistory`]
        """
        self._alarm_handle_histories = alarm_handle_histories

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
        if not isinstance(other, ListAlarmHandleHistoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
