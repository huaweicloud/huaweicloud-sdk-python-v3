# coding: utf-8

import pprint
import re

import six





class ShowHistoryTaskDetailsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'history_tasks_id': 'str',
        'page_size': 'int',
        'page_number': 'int',
        'status': 'int',
        'url': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'history_tasks_id': 'history_tasks_id',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'status': 'status',
        'url': 'url'
    }

    def __init__(self, enterprise_project_id=None, history_tasks_id=None, page_size=None, page_number=None, status=None, url=None):
        """ShowHistoryTaskDetailsRequest - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self._history_tasks_id = None
        self._page_size = None
        self._page_number = None
        self._status = None
        self._url = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.history_tasks_id = history_tasks_id
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowHistoryTaskDetailsRequest.

        当用户开启企业项目功能时，该参数生效，表示资源所属企业项目，不传表示默认项目。

        :return: The enterprise_project_id of this ShowHistoryTaskDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowHistoryTaskDetailsRequest.

        当用户开启企业项目功能时，该参数生效，表示资源所属企业项目，不传表示默认项目。

        :param enterprise_project_id: The enterprise_project_id of this ShowHistoryTaskDetailsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def history_tasks_id(self):
        """Gets the history_tasks_id of this ShowHistoryTaskDetailsRequest.

        刷新任务ID。

        :return: The history_tasks_id of this ShowHistoryTaskDetailsRequest.
        :rtype: str
        """
        return self._history_tasks_id

    @history_tasks_id.setter
    def history_tasks_id(self, history_tasks_id):
        """Sets the history_tasks_id of this ShowHistoryTaskDetailsRequest.

        刷新任务ID。

        :param history_tasks_id: The history_tasks_id of this ShowHistoryTaskDetailsRequest.
        :type: str
        """
        self._history_tasks_id = history_tasks_id

    @property
    def page_size(self):
        """Gets the page_size of this ShowHistoryTaskDetailsRequest.

        刷新预热的urls所显示单页最大数量，取值范围为1-10000。

        :return: The page_size of this ShowHistoryTaskDetailsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowHistoryTaskDetailsRequest.

        刷新预热的urls所显示单页最大数量，取值范围为1-10000。

        :param page_size: The page_size of this ShowHistoryTaskDetailsRequest.
        :type: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this ShowHistoryTaskDetailsRequest.

        刷新预热的urls当前查询为第几页，取值范围为1-65535。

        :return: The page_number of this ShowHistoryTaskDetailsRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ShowHistoryTaskDetailsRequest.

        刷新预热的urls当前查询为第几页，取值范围为1-65535。

        :param page_number: The page_number of this ShowHistoryTaskDetailsRequest.
        :type: int
        """
        self._page_number = page_number

    @property
    def status(self):
        """Gets the status of this ShowHistoryTaskDetailsRequest.

        url的状态 processing， succeed， failed，分别表示处理中，完成，失败。

        :return: The status of this ShowHistoryTaskDetailsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowHistoryTaskDetailsRequest.

        url的状态 processing， succeed， failed，分别表示处理中，完成，失败。

        :param status: The status of this ShowHistoryTaskDetailsRequest.
        :type: int
        """
        self._status = status

    @property
    def url(self):
        """Gets the url of this ShowHistoryTaskDetailsRequest.

        url的地址，支持同一任务id的多个url,多个url用分号隔开。

        :return: The url of this ShowHistoryTaskDetailsRequest.
        :rtype: int
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ShowHistoryTaskDetailsRequest.

        url的地址，支持同一任务id的多个url,多个url用分号隔开。

        :param url: The url of this ShowHistoryTaskDetailsRequest.
        :type: int
        """
        self._url = url

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
        if not isinstance(other, ShowHistoryTaskDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
