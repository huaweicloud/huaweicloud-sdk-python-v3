# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledTaskHistoryResponse(SdkResponse):

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
        'next_maker': 'str',
        'scheduled_task_history_list': 'list[ScheduledTaskHistory]'
    }

    attribute_map = {
        'count': 'count',
        'next_maker': 'next_maker',
        'scheduled_task_history_list': 'scheduled_task_history_list'
    }

    def __init__(self, count=None, next_maker=None, scheduled_task_history_list=None):
        r"""ListScheduledTaskHistoryResponse

        The model defined in huaweicloud sdk

        :param count: 定时运维历史记录总数量
        :type count: int
        :param next_maker: 分页标记
        :type next_maker: str
        :param scheduled_task_history_list: 定时运维历史记录列表
        :type scheduled_task_history_list: list[:class:`huaweicloudsdkcoc.v1.ScheduledTaskHistory`]
        """
        
        super(ListScheduledTaskHistoryResponse, self).__init__()

        self._count = None
        self._next_maker = None
        self._scheduled_task_history_list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if next_maker is not None:
            self.next_maker = next_maker
        if scheduled_task_history_list is not None:
            self.scheduled_task_history_list = scheduled_task_history_list

    @property
    def count(self):
        r"""Gets the count of this ListScheduledTaskHistoryResponse.

        定时运维历史记录总数量

        :return: The count of this ListScheduledTaskHistoryResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListScheduledTaskHistoryResponse.

        定时运维历史记录总数量

        :param count: The count of this ListScheduledTaskHistoryResponse.
        :type count: int
        """
        self._count = count

    @property
    def next_maker(self):
        r"""Gets the next_maker of this ListScheduledTaskHistoryResponse.

        分页标记

        :return: The next_maker of this ListScheduledTaskHistoryResponse.
        :rtype: str
        """
        return self._next_maker

    @next_maker.setter
    def next_maker(self, next_maker):
        r"""Sets the next_maker of this ListScheduledTaskHistoryResponse.

        分页标记

        :param next_maker: The next_maker of this ListScheduledTaskHistoryResponse.
        :type next_maker: str
        """
        self._next_maker = next_maker

    @property
    def scheduled_task_history_list(self):
        r"""Gets the scheduled_task_history_list of this ListScheduledTaskHistoryResponse.

        定时运维历史记录列表

        :return: The scheduled_task_history_list of this ListScheduledTaskHistoryResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ScheduledTaskHistory`]
        """
        return self._scheduled_task_history_list

    @scheduled_task_history_list.setter
    def scheduled_task_history_list(self, scheduled_task_history_list):
        r"""Sets the scheduled_task_history_list of this ListScheduledTaskHistoryResponse.

        定时运维历史记录列表

        :param scheduled_task_history_list: The scheduled_task_history_list of this ListScheduledTaskHistoryResponse.
        :type scheduled_task_history_list: list[:class:`huaweicloudsdkcoc.v1.ScheduledTaskHistory`]
        """
        self._scheduled_task_history_list = scheduled_task_history_list

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
        if not isinstance(other, ListScheduledTaskHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
