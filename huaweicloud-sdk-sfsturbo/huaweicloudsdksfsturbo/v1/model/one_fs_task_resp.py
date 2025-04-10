# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OneFsTaskResp:

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
        'end_time': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'dir_usage': 'dir_usage',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, task_id=None, status=None, dir_usage=None, begin_time=None, end_time=None):
        r"""OneFsTaskResp

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
        """
        
        

        self._task_id = None
        self._status = None
        self._dir_usage = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        self.task_id = task_id
        self.status = status
        if dir_usage is not None:
            self.dir_usage = dir_usage
        self.begin_time = begin_time
        self.end_time = end_time

    @property
    def task_id(self):
        r"""Gets the task_id of this OneFsTaskResp.

        任务ID

        :return: The task_id of this OneFsTaskResp.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this OneFsTaskResp.

        任务ID

        :param task_id: The task_id of this OneFsTaskResp.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this OneFsTaskResp.

        任务状态, SUCCESS表示成功，DOING表示正在执行，FAIL表示失败

        :return: The status of this OneFsTaskResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OneFsTaskResp.

        任务状态, SUCCESS表示成功，DOING表示正在执行，FAIL表示失败

        :param status: The status of this OneFsTaskResp.
        :type status: str
        """
        self._status = status

    @property
    def dir_usage(self):
        r"""Gets the dir_usage of this OneFsTaskResp.

        :return: The dir_usage of this OneFsTaskResp.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.FsDuInfo`
        """
        return self._dir_usage

    @dir_usage.setter
    def dir_usage(self, dir_usage):
        r"""Sets the dir_usage of this OneFsTaskResp.

        :param dir_usage: The dir_usage of this OneFsTaskResp.
        :type dir_usage: :class:`huaweicloudsdksfsturbo.v1.FsDuInfo`
        """
        self._dir_usage = dir_usage

    @property
    def begin_time(self):
        r"""Gets the begin_time of this OneFsTaskResp.

        任务开始时间，UTC时间，例如：2006-01-02 15:04:05'

        :return: The begin_time of this OneFsTaskResp.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this OneFsTaskResp.

        任务开始时间，UTC时间，例如：2006-01-02 15:04:05'

        :param begin_time: The begin_time of this OneFsTaskResp.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this OneFsTaskResp.

        任务结束时间，UTC时间，例如：2006-01-02 15:04:06'

        :return: The end_time of this OneFsTaskResp.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this OneFsTaskResp.

        任务结束时间，UTC时间，例如：2006-01-02 15:04:06'

        :param end_time: The end_time of this OneFsTaskResp.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, OneFsTaskResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
