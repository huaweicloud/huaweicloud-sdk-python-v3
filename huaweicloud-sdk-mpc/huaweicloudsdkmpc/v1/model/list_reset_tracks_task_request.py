# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResetTracksTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'list[str]',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, task_id=None, status=None, start_time=None, end_time=None, page=None, size=None):
        r"""ListResetTracksTaskRequest

        The model defined in huaweicloud sdk

        :param task_id: 任务ID。一次最多10个 
        :type task_id: list[str]
        :param status: 任务执行状态 
        :type status: str
        :param start_time: 起始时间。格式为yyyymmddhhmmss。必须是与时区无关的UTC时间，指定task_id时该参数无效 
        :type start_time: str
        :param end_time: 结束时间。格式为yyyymmddhhmmss。必须是与时区无关的UTC时间，指定task_id时该参数无效 
        :type end_time: str
        :param page: 分页编号。查询指定“task_id”时，该参数无效。  默认值：0。 
        :type page: int
        :param size: 每页记录数。查询指定“task_id”时，该参数无效。  取值范围：[1,100]。  默认值：10。 
        :type size: int
        """
        
        

        self._task_id = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._page = None
        self._size = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def task_id(self):
        r"""Gets the task_id of this ListResetTracksTaskRequest.

        任务ID。一次最多10个 

        :return: The task_id of this ListResetTracksTaskRequest.
        :rtype: list[str]
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListResetTracksTaskRequest.

        任务ID。一次最多10个 

        :param task_id: The task_id of this ListResetTracksTaskRequest.
        :type task_id: list[str]
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this ListResetTracksTaskRequest.

        任务执行状态 

        :return: The status of this ListResetTracksTaskRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListResetTracksTaskRequest.

        任务执行状态 

        :param status: The status of this ListResetTracksTaskRequest.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this ListResetTracksTaskRequest.

        起始时间。格式为yyyymmddhhmmss。必须是与时区无关的UTC时间，指定task_id时该参数无效 

        :return: The start_time of this ListResetTracksTaskRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListResetTracksTaskRequest.

        起始时间。格式为yyyymmddhhmmss。必须是与时区无关的UTC时间，指定task_id时该参数无效 

        :param start_time: The start_time of this ListResetTracksTaskRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListResetTracksTaskRequest.

        结束时间。格式为yyyymmddhhmmss。必须是与时区无关的UTC时间，指定task_id时该参数无效 

        :return: The end_time of this ListResetTracksTaskRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListResetTracksTaskRequest.

        结束时间。格式为yyyymmddhhmmss。必须是与时区无关的UTC时间，指定task_id时该参数无效 

        :param end_time: The end_time of this ListResetTracksTaskRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def page(self):
        r"""Gets the page of this ListResetTracksTaskRequest.

        分页编号。查询指定“task_id”时，该参数无效。  默认值：0。 

        :return: The page of this ListResetTracksTaskRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListResetTracksTaskRequest.

        分页编号。查询指定“task_id”时，该参数无效。  默认值：0。 

        :param page: The page of this ListResetTracksTaskRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this ListResetTracksTaskRequest.

        每页记录数。查询指定“task_id”时，该参数无效。  取值范围：[1,100]。  默认值：10。 

        :return: The size of this ListResetTracksTaskRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListResetTracksTaskRequest.

        每页记录数。查询指定“task_id”时，该参数无效。  取值范围：[1,100]。  默认值：10。 

        :param size: The size of this ListResetTracksTaskRequest.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ListResetTracksTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
