# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUrlTaskInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'offset': 'int',
        'limit': 'int',
        'url': 'str',
        'task_type': 'str',
        'status': 'str',
        'file_type': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit',
        'url': 'url',
        'task_type': 'task_type',
        'status': 'status',
        'file_type': 'file_type'
    }

    def __init__(self, start_time=None, end_time=None, offset=None, limit=None, url=None, task_type=None, status=None, file_type=None):
        """ShowUrlTaskInfoRequest

        The model defined in huaweicloud sdk

        :param start_time: 起始时间戳（毫秒），默认当天00:00
        :type start_time: int
        :param end_time: 结束时间戳（毫秒），默认次日00:00
        :type end_time: int
        :param offset: 偏移量
        :type offset: int
        :param limit: 单次查询数据条数，上限为100
        :type limit: int
        :param url: 刷新预热url
        :type url: str
        :param task_type: 任务类型，REFRESH：刷新任务；PREHEATING：预热任务
        :type task_type: str
        :param status: url状态，状态类型：processing：处理中；succeed：完成；failed：失败；waiting：等待；refreshing：刷新中; preheating : 预热中
        :type status: str
        :param file_type: 文件类型，file:文件;directory:目录
        :type file_type: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self._url = None
        self._task_type = None
        self._status = None
        self._file_type = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if url is not None:
            self.url = url
        if task_type is not None:
            self.task_type = task_type
        if status is not None:
            self.status = status
        if file_type is not None:
            self.file_type = file_type

    @property
    def start_time(self):
        """Gets the start_time of this ShowUrlTaskInfoRequest.

        起始时间戳（毫秒），默认当天00:00

        :return: The start_time of this ShowUrlTaskInfoRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowUrlTaskInfoRequest.

        起始时间戳（毫秒），默认当天00:00

        :param start_time: The start_time of this ShowUrlTaskInfoRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowUrlTaskInfoRequest.

        结束时间戳（毫秒），默认次日00:00

        :return: The end_time of this ShowUrlTaskInfoRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowUrlTaskInfoRequest.

        结束时间戳（毫秒），默认次日00:00

        :param end_time: The end_time of this ShowUrlTaskInfoRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this ShowUrlTaskInfoRequest.

        偏移量

        :return: The offset of this ShowUrlTaskInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowUrlTaskInfoRequest.

        偏移量

        :param offset: The offset of this ShowUrlTaskInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowUrlTaskInfoRequest.

        单次查询数据条数，上限为100

        :return: The limit of this ShowUrlTaskInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowUrlTaskInfoRequest.

        单次查询数据条数，上限为100

        :param limit: The limit of this ShowUrlTaskInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def url(self):
        """Gets the url of this ShowUrlTaskInfoRequest.

        刷新预热url

        :return: The url of this ShowUrlTaskInfoRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ShowUrlTaskInfoRequest.

        刷新预热url

        :param url: The url of this ShowUrlTaskInfoRequest.
        :type url: str
        """
        self._url = url

    @property
    def task_type(self):
        """Gets the task_type of this ShowUrlTaskInfoRequest.

        任务类型，REFRESH：刷新任务；PREHEATING：预热任务

        :return: The task_type of this ShowUrlTaskInfoRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ShowUrlTaskInfoRequest.

        任务类型，REFRESH：刷新任务；PREHEATING：预热任务

        :param task_type: The task_type of this ShowUrlTaskInfoRequest.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def status(self):
        """Gets the status of this ShowUrlTaskInfoRequest.

        url状态，状态类型：processing：处理中；succeed：完成；failed：失败；waiting：等待；refreshing：刷新中; preheating : 预热中

        :return: The status of this ShowUrlTaskInfoRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowUrlTaskInfoRequest.

        url状态，状态类型：processing：处理中；succeed：完成；failed：失败；waiting：等待；refreshing：刷新中; preheating : 预热中

        :param status: The status of this ShowUrlTaskInfoRequest.
        :type status: str
        """
        self._status = status

    @property
    def file_type(self):
        """Gets the file_type of this ShowUrlTaskInfoRequest.

        文件类型，file:文件;directory:目录

        :return: The file_type of this ShowUrlTaskInfoRequest.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ShowUrlTaskInfoRequest.

        文件类型，file:文件;directory:目录

        :param file_type: The file_type of this ShowUrlTaskInfoRequest.
        :type file_type: str
        """
        self._file_type = file_type

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
        if not isinstance(other, ShowUrlTaskInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
