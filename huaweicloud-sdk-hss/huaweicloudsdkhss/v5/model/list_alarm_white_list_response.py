# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmWhiteListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'event_type_list': 'list[int]',
        'data_list': 'list[AlarmWhiteListResponseInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'event_type_list': 'event_type_list',
        'data_list': 'data_list'
    }

    def __init__(self, total_num=None, event_type_list=None, data_list=None):
        """ListAlarmWhiteListResponse

        The model defined in huaweicloud sdk

        :param total_num: 总数
        :type total_num: int
        :param event_type_list: 支持筛选的事件类型
        :type event_type_list: list[int]
        :param data_list: 告警白名单详情
        :type data_list: list[:class:`huaweicloudsdkhss.v5.AlarmWhiteListResponseInfo`]
        """
        
        super(ListAlarmWhiteListResponse, self).__init__()

        self._total_num = None
        self._event_type_list = None
        self._data_list = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if event_type_list is not None:
            self.event_type_list = event_type_list
        if data_list is not None:
            self.data_list = data_list

    @property
    def total_num(self):
        """Gets the total_num of this ListAlarmWhiteListResponse.

        总数

        :return: The total_num of this ListAlarmWhiteListResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this ListAlarmWhiteListResponse.

        总数

        :param total_num: The total_num of this ListAlarmWhiteListResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def event_type_list(self):
        """Gets the event_type_list of this ListAlarmWhiteListResponse.

        支持筛选的事件类型

        :return: The event_type_list of this ListAlarmWhiteListResponse.
        :rtype: list[int]
        """
        return self._event_type_list

    @event_type_list.setter
    def event_type_list(self, event_type_list):
        """Sets the event_type_list of this ListAlarmWhiteListResponse.

        支持筛选的事件类型

        :param event_type_list: The event_type_list of this ListAlarmWhiteListResponse.
        :type event_type_list: list[int]
        """
        self._event_type_list = event_type_list

    @property
    def data_list(self):
        """Gets the data_list of this ListAlarmWhiteListResponse.

        告警白名单详情

        :return: The data_list of this ListAlarmWhiteListResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AlarmWhiteListResponseInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        """Sets the data_list of this ListAlarmWhiteListResponse.

        告警白名单详情

        :param data_list: The data_list of this ListAlarmWhiteListResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.AlarmWhiteListResponseInfo`]
        """
        self._data_list = data_list

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
        if not isinstance(other, ListAlarmWhiteListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
