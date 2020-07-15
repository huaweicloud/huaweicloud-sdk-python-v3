# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowBatchTaskResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'batchtask': 'Task',
        'task_details': 'list[TaskDetail]',
        'page': 'Page'
    }

    attribute_map = {
        'batchtask': 'batchtask',
        'task_details': 'task_details',
        'page': 'page'
    }

    def __init__(self, batchtask=None, task_details=None, page=None):
        """ShowBatchTaskResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._batchtask = None
        self._task_details = None
        self._page = None
        self.discriminator = None

        if batchtask is not None:
            self.batchtask = batchtask
        if task_details is not None:
            self.task_details = task_details
        if page is not None:
            self.page = page

    @property
    def batchtask(self):
        """Gets the batchtask of this ShowBatchTaskResponse.


        :return: The batchtask of this ShowBatchTaskResponse.
        :rtype: Task
        """
        return self._batchtask

    @batchtask.setter
    def batchtask(self, batchtask):
        """Sets the batchtask of this ShowBatchTaskResponse.


        :param batchtask: The batchtask of this ShowBatchTaskResponse.
        :type: Task
        """
        self._batchtask = batchtask

    @property
    def task_details(self):
        """Gets the task_details of this ShowBatchTaskResponse.

        子任务详情列表。

        :return: The task_details of this ShowBatchTaskResponse.
        :rtype: list[TaskDetail]
        """
        return self._task_details

    @task_details.setter
    def task_details(self, task_details):
        """Sets the task_details of this ShowBatchTaskResponse.

        子任务详情列表。

        :param task_details: The task_details of this ShowBatchTaskResponse.
        :type: list[TaskDetail]
        """
        self._task_details = task_details

    @property
    def page(self):
        """Gets the page of this ShowBatchTaskResponse.


        :return: The page of this ShowBatchTaskResponse.
        :rtype: Page
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ShowBatchTaskResponse.


        :param page: The page of this ShowBatchTaskResponse.
        :type: Page
        """
        self._page = page

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowBatchTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
