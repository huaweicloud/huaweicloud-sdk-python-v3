# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListBatchTasksResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'batchtasks': 'list[Task]',
        'page': 'Page'
    }

    attribute_map = {
        'batchtasks': 'batchtasks',
        'page': 'page'
    }

    def __init__(self, batchtasks=None, page=None):
        """ListBatchTasksResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._batchtasks = None
        self._page = None
        self.discriminator = None

        if batchtasks is not None:
            self.batchtasks = batchtasks
        if page is not None:
            self.page = page

    @property
    def batchtasks(self):
        """Gets the batchtasks of this ListBatchTasksResponse.

        批量任务列表。

        :return: The batchtasks of this ListBatchTasksResponse.
        :rtype: list[Task]
        """
        return self._batchtasks

    @batchtasks.setter
    def batchtasks(self, batchtasks):
        """Sets the batchtasks of this ListBatchTasksResponse.

        批量任务列表。

        :param batchtasks: The batchtasks of this ListBatchTasksResponse.
        :type: list[Task]
        """
        self._batchtasks = batchtasks

    @property
    def page(self):
        """Gets the page of this ListBatchTasksResponse.


        :return: The page of this ListBatchTasksResponse.
        :rtype: Page
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListBatchTasksResponse.


        :param page: The page of this ListBatchTasksResponse.
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
        if not isinstance(other, ListBatchTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
