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
        'alarm_handle_histories': 'list[AlarmHandleHistory]',
        'resolved_record': 'ResolvedRecordDTO'
    }

    attribute_map = {
        'count': 'count',
        'alarm_handle_histories': 'alarm_handle_histories',
        'resolved_record': 'resolved_record'
    }

    def __init__(self, count=None, alarm_handle_histories=None, resolved_record=None):
        r"""ListAlarmHandleHistoriesResponse

        The model defined in huaweicloud sdk

        :param count: 总数量
        :type count: int
        :param alarm_handle_histories: 告警工单执行结果
        :type alarm_handle_histories: list[:class:`huaweicloudsdkcoc.v1.AlarmHandleHistory`]
        :param resolved_record: 
        :type resolved_record: :class:`huaweicloudsdkcoc.v1.ResolvedRecordDTO`
        """
        
        super(ListAlarmHandleHistoriesResponse, self).__init__()

        self._count = None
        self._alarm_handle_histories = None
        self._resolved_record = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if alarm_handle_histories is not None:
            self.alarm_handle_histories = alarm_handle_histories
        if resolved_record is not None:
            self.resolved_record = resolved_record

    @property
    def count(self):
        r"""Gets the count of this ListAlarmHandleHistoriesResponse.

        总数量

        :return: The count of this ListAlarmHandleHistoriesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAlarmHandleHistoriesResponse.

        总数量

        :param count: The count of this ListAlarmHandleHistoriesResponse.
        :type count: int
        """
        self._count = count

    @property
    def alarm_handle_histories(self):
        r"""Gets the alarm_handle_histories of this ListAlarmHandleHistoriesResponse.

        告警工单执行结果

        :return: The alarm_handle_histories of this ListAlarmHandleHistoriesResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.AlarmHandleHistory`]
        """
        return self._alarm_handle_histories

    @alarm_handle_histories.setter
    def alarm_handle_histories(self, alarm_handle_histories):
        r"""Sets the alarm_handle_histories of this ListAlarmHandleHistoriesResponse.

        告警工单执行结果

        :param alarm_handle_histories: The alarm_handle_histories of this ListAlarmHandleHistoriesResponse.
        :type alarm_handle_histories: list[:class:`huaweicloudsdkcoc.v1.AlarmHandleHistory`]
        """
        self._alarm_handle_histories = alarm_handle_histories

    @property
    def resolved_record(self):
        r"""Gets the resolved_record of this ListAlarmHandleHistoriesResponse.

        :return: The resolved_record of this ListAlarmHandleHistoriesResponse.
        :rtype: :class:`huaweicloudsdkcoc.v1.ResolvedRecordDTO`
        """
        return self._resolved_record

    @resolved_record.setter
    def resolved_record(self, resolved_record):
        r"""Sets the resolved_record of this ListAlarmHandleHistoriesResponse.

        :param resolved_record: The resolved_record of this ListAlarmHandleHistoriesResponse.
        :type resolved_record: :class:`huaweicloudsdkcoc.v1.ResolvedRecordDTO`
        """
        self._resolved_record = resolved_record

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
