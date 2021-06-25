# coding: utf-8

import pprint
import re

import six





class UrlObject:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'url': 'str',
        'status': 'str',
        'create_time': 'int',
        'task_id': 'str',
        'process_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'status': 'status',
        'create_time': 'create_time',
        'task_id': 'task_id',
        'process_reason': 'process_reason'
    }

    def __init__(self, id=None, url=None, status=None, create_time=None, task_id=None, process_reason=None):
        """UrlObject - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._url = None
        self._status = None
        self._create_time = None
        self._task_id = None
        self._process_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if task_id is not None:
            self.task_id = task_id
        if process_reason is not None:
            self.process_reason = process_reason

    @property
    def id(self):
        """Gets the id of this UrlObject.

        任务id

        :return: The id of this UrlObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UrlObject.

        任务id

        :param id: The id of this UrlObject.
        :type: str
        """
        self._id = id

    @property
    def url(self):
        """Gets the url of this UrlObject.

        url的地址。

        :return: The url of this UrlObject.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UrlObject.

        url的地址。

        :param url: The url of this UrlObject.
        :type: str
        """
        self._url = url

    @property
    def status(self):
        """Gets the status of this UrlObject.

        url的状态 processing， succeed， failed，分别表示处理中，完成，失败。

        :return: The status of this UrlObject.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UrlObject.

        url的状态 processing， succeed， failed，分别表示处理中，完成，失败。

        :param status: The status of this UrlObject.
        :type: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this UrlObject.

        url创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The create_time of this UrlObject.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UrlObject.

        url创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param create_time: The create_time of this UrlObject.
        :type: int
        """
        self._create_time = create_time

    @property
    def task_id(self):
        """Gets the task_id of this UrlObject.

        url所属task的id。

        :return: The task_id of this UrlObject.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this UrlObject.

        url所属task的id。

        :param task_id: The task_id of this UrlObject.
        :type: str
        """
        self._task_id = task_id

    @property
    def process_reason(self):
        """Gets the process_reason of this UrlObject.

        标记处理原因。

        :return: The process_reason of this UrlObject.
        :rtype: str
        """
        return self._process_reason

    @process_reason.setter
    def process_reason(self, process_reason):
        """Sets the process_reason of this UrlObject.

        标记处理原因。

        :param process_reason: The process_reason of this UrlObject.
        :type: str
        """
        self._process_reason = process_reason

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
        if not isinstance(other, UrlObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other