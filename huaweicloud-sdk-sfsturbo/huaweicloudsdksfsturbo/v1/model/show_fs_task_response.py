# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFsTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'status': 'str',
        'dir_usage': 'FsDuInfo',
        'begin_time': 'str',
        'end_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'dir_usage': 'dir_usage',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, task_id=None, status=None, dir_usage=None, begin_time=None, end_time=None, x_request_id=None):
        r"""ShowFsTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param status: 任务状态, SUCCESS表示成功，DOING表示正在执行，FAIL表示失败
        :type status: str
        :param dir_usage: 
        :type dir_usage: :class:`huaweicloudsdksfsturbo.v1.FsDuInfo`
        :param begin_time: 任务开始时间，UTC时间，例如：2006-01-02 15:04:05&#39;
        :type begin_time: str
        :param end_time: 任务结束时间，UTC时间，例如：2006-01-02 15:04:06&#39;
        :type end_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowFsTaskResponse, self).__init__()

        self._task_id = None
        self._status = None
        self._dir_usage = None
        self._begin_time = None
        self._end_time = None
        self._x_request_id = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if dir_usage is not None:
            self.dir_usage = dir_usage
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowFsTaskResponse.

        任务ID

        :return: The task_id of this ShowFsTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowFsTaskResponse.

        任务ID

        :param task_id: The task_id of this ShowFsTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this ShowFsTaskResponse.

        任务状态, SUCCESS表示成功，DOING表示正在执行，FAIL表示失败

        :return: The status of this ShowFsTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowFsTaskResponse.

        任务状态, SUCCESS表示成功，DOING表示正在执行，FAIL表示失败

        :param status: The status of this ShowFsTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def dir_usage(self):
        r"""Gets the dir_usage of this ShowFsTaskResponse.

        :return: The dir_usage of this ShowFsTaskResponse.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.FsDuInfo`
        """
        return self._dir_usage

    @dir_usage.setter
    def dir_usage(self, dir_usage):
        r"""Sets the dir_usage of this ShowFsTaskResponse.

        :param dir_usage: The dir_usage of this ShowFsTaskResponse.
        :type dir_usage: :class:`huaweicloudsdksfsturbo.v1.FsDuInfo`
        """
        self._dir_usage = dir_usage

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowFsTaskResponse.

        任务开始时间，UTC时间，例如：2006-01-02 15:04:05'

        :return: The begin_time of this ShowFsTaskResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowFsTaskResponse.

        任务开始时间，UTC时间，例如：2006-01-02 15:04:05'

        :param begin_time: The begin_time of this ShowFsTaskResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowFsTaskResponse.

        任务结束时间，UTC时间，例如：2006-01-02 15:04:06'

        :return: The end_time of this ShowFsTaskResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowFsTaskResponse.

        任务结束时间，UTC时间，例如：2006-01-02 15:04:06'

        :param end_time: The end_time of this ShowFsTaskResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowFsTaskResponse.

        :return: The x_request_id of this ShowFsTaskResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowFsTaskResponse.

        :param x_request_id: The x_request_id of this ShowFsTaskResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowFsTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
