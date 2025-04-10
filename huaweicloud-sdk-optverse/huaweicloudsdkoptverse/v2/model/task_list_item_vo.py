# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskListItemVo:

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
        'start_time': 'str',
        'end_time': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'create_time': 'create_time'
    }

    def __init__(self, task_id=None, status=None, start_time=None, end_time=None, create_time=None):
        r"""TaskListItemVo

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param status: 任务状态
        :type status: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param create_time: 创建时间
        :type create_time: str
        """
        
        

        self._task_id = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._create_time = None
        self.discriminator = None

        self.task_id = task_id
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.create_time = create_time

    @property
    def task_id(self):
        r"""Gets the task_id of this TaskListItemVo.

        任务ID

        :return: The task_id of this TaskListItemVo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this TaskListItemVo.

        任务ID

        :param task_id: The task_id of this TaskListItemVo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this TaskListItemVo.

        任务状态

        :return: The status of this TaskListItemVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TaskListItemVo.

        任务状态

        :param status: The status of this TaskListItemVo.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this TaskListItemVo.

        开始时间

        :return: The start_time of this TaskListItemVo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TaskListItemVo.

        开始时间

        :param start_time: The start_time of this TaskListItemVo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this TaskListItemVo.

        结束时间

        :return: The end_time of this TaskListItemVo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TaskListItemVo.

        结束时间

        :param end_time: The end_time of this TaskListItemVo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def create_time(self):
        r"""Gets the create_time of this TaskListItemVo.

        创建时间

        :return: The create_time of this TaskListItemVo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TaskListItemVo.

        创建时间

        :param create_time: The create_time of this TaskListItemVo.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, TaskListItemVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
