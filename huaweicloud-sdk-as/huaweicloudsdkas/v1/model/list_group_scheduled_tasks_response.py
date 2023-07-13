# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupScheduledTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_info': 'PageInfo',
        'scheduled_tasks': 'list[ScheduledTaskDetail]'
    }

    attribute_map = {
        'page_info': 'page_info',
        'scheduled_tasks': 'scheduled_tasks'
    }

    def __init__(self, page_info=None, scheduled_tasks=None):
        """ListGroupScheduledTasksResponse

        The model defined in huaweicloud sdk

        :param page_info: 
        :type page_info: :class:`huaweicloudsdkas.v1.PageInfo`
        :param scheduled_tasks: 计划任务列表
        :type scheduled_tasks: list[:class:`huaweicloudsdkas.v1.ScheduledTaskDetail`]
        """
        
        super(ListGroupScheduledTasksResponse, self).__init__()

        self._page_info = None
        self._scheduled_tasks = None
        self.discriminator = None

        if page_info is not None:
            self.page_info = page_info
        if scheduled_tasks is not None:
            self.scheduled_tasks = scheduled_tasks

    @property
    def page_info(self):
        """Gets the page_info of this ListGroupScheduledTasksResponse.

        :return: The page_info of this ListGroupScheduledTasksResponse.
        :rtype: :class:`huaweicloudsdkas.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListGroupScheduledTasksResponse.

        :param page_info: The page_info of this ListGroupScheduledTasksResponse.
        :type page_info: :class:`huaweicloudsdkas.v1.PageInfo`
        """
        self._page_info = page_info

    @property
    def scheduled_tasks(self):
        """Gets the scheduled_tasks of this ListGroupScheduledTasksResponse.

        计划任务列表

        :return: The scheduled_tasks of this ListGroupScheduledTasksResponse.
        :rtype: list[:class:`huaweicloudsdkas.v1.ScheduledTaskDetail`]
        """
        return self._scheduled_tasks

    @scheduled_tasks.setter
    def scheduled_tasks(self, scheduled_tasks):
        """Sets the scheduled_tasks of this ListGroupScheduledTasksResponse.

        计划任务列表

        :param scheduled_tasks: The scheduled_tasks of this ListGroupScheduledTasksResponse.
        :type scheduled_tasks: list[:class:`huaweicloudsdkas.v1.ScheduledTaskDetail`]
        """
        self._scheduled_tasks = scheduled_tasks

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
        if not isinstance(other, ListGroupScheduledTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
