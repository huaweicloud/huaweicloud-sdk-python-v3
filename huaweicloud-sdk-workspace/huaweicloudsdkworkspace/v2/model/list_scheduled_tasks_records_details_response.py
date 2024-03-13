# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledTasksRecordsDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks_records_details': 'list[ScheduledTasksRecordsDetails]',
        'total_count': 'int'
    }

    attribute_map = {
        'tasks_records_details': 'tasks_records_details',
        'total_count': 'total_count'
    }

    def __init__(self, tasks_records_details=None, total_count=None):
        """ListScheduledTasksRecordsDetailsResponse

        The model defined in huaweicloud sdk

        :param tasks_records_details: 定时任务执行记录详情列表。
        :type tasks_records_details: list[:class:`huaweicloudsdkworkspace.v2.ScheduledTasksRecordsDetails`]
        :param total_count: 总个数。
        :type total_count: int
        """
        
        super(ListScheduledTasksRecordsDetailsResponse, self).__init__()

        self._tasks_records_details = None
        self._total_count = None
        self.discriminator = None

        if tasks_records_details is not None:
            self.tasks_records_details = tasks_records_details
        if total_count is not None:
            self.total_count = total_count

    @property
    def tasks_records_details(self):
        """Gets the tasks_records_details of this ListScheduledTasksRecordsDetailsResponse.

        定时任务执行记录详情列表。

        :return: The tasks_records_details of this ListScheduledTasksRecordsDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ScheduledTasksRecordsDetails`]
        """
        return self._tasks_records_details

    @tasks_records_details.setter
    def tasks_records_details(self, tasks_records_details):
        """Sets the tasks_records_details of this ListScheduledTasksRecordsDetailsResponse.

        定时任务执行记录详情列表。

        :param tasks_records_details: The tasks_records_details of this ListScheduledTasksRecordsDetailsResponse.
        :type tasks_records_details: list[:class:`huaweicloudsdkworkspace.v2.ScheduledTasksRecordsDetails`]
        """
        self._tasks_records_details = tasks_records_details

    @property
    def total_count(self):
        """Gets the total_count of this ListScheduledTasksRecordsDetailsResponse.

        总个数。

        :return: The total_count of this ListScheduledTasksRecordsDetailsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListScheduledTasksRecordsDetailsResponse.

        总个数。

        :param total_count: The total_count of this ListScheduledTasksRecordsDetailsResponse.
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
        if not isinstance(other, ListScheduledTasksRecordsDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
