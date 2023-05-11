# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchStartOrStopTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_count': 'int',
        'failure_count': 'int',
        'failure': 'list[TaskBeanFacade]',
        'success': 'list[TaskBeanFacade]'
    }

    attribute_map = {
        'success_count': 'success_count',
        'failure_count': 'failure_count',
        'failure': 'failure',
        'success': 'success'
    }

    def __init__(self, success_count=None, failure_count=None, failure=None, success=None):
        """BatchStartOrStopTasksResponse

        The model defined in huaweicloud sdk

        :param success_count: 成功的个数
        :type success_count: int
        :param failure_count: 失败的个数
        :type failure_count: int
        :param failure: 失败的详情
        :type failure: list[:class:`huaweicloudsdkroma.v2.TaskBeanFacade`]
        :param success: 成功的任务信息
        :type success: list[:class:`huaweicloudsdkroma.v2.TaskBeanFacade`]
        """
        
        super(BatchStartOrStopTasksResponse, self).__init__()

        self._success_count = None
        self._failure_count = None
        self._failure = None
        self._success = None
        self.discriminator = None

        if success_count is not None:
            self.success_count = success_count
        if failure_count is not None:
            self.failure_count = failure_count
        if failure is not None:
            self.failure = failure
        if success is not None:
            self.success = success

    @property
    def success_count(self):
        """Gets the success_count of this BatchStartOrStopTasksResponse.

        成功的个数

        :return: The success_count of this BatchStartOrStopTasksResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this BatchStartOrStopTasksResponse.

        成功的个数

        :param success_count: The success_count of this BatchStartOrStopTasksResponse.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def failure_count(self):
        """Gets the failure_count of this BatchStartOrStopTasksResponse.

        失败的个数

        :return: The failure_count of this BatchStartOrStopTasksResponse.
        :rtype: int
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        """Sets the failure_count of this BatchStartOrStopTasksResponse.

        失败的个数

        :param failure_count: The failure_count of this BatchStartOrStopTasksResponse.
        :type failure_count: int
        """
        self._failure_count = failure_count

    @property
    def failure(self):
        """Gets the failure of this BatchStartOrStopTasksResponse.

        失败的详情

        :return: The failure of this BatchStartOrStopTasksResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.TaskBeanFacade`]
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """Sets the failure of this BatchStartOrStopTasksResponse.

        失败的详情

        :param failure: The failure of this BatchStartOrStopTasksResponse.
        :type failure: list[:class:`huaweicloudsdkroma.v2.TaskBeanFacade`]
        """
        self._failure = failure

    @property
    def success(self):
        """Gets the success of this BatchStartOrStopTasksResponse.

        成功的任务信息

        :return: The success of this BatchStartOrStopTasksResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.TaskBeanFacade`]
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this BatchStartOrStopTasksResponse.

        成功的任务信息

        :param success: The success of this BatchStartOrStopTasksResponse.
        :type success: list[:class:`huaweicloudsdkroma.v2.TaskBeanFacade`]
        """
        self._success = success

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
        if not isinstance(other, BatchStartOrStopTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
