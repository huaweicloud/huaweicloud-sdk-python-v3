# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'str',
        'workspace_id': 'str',
        'task_id': 'str',
        'job_name': 'str',
        'start_time': 'float',
        'end_time': 'float',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance': 'instance',
        'workspace_id': 'workspace_id',
        'task_id': 'task_id',
        'job_name': 'job_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance=None, workspace_id=None, task_id=None, job_name=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ShowInstanceInfosRequest

        The model defined in huaweicloud sdk

        :param instance: 实例id
        :type instance: str
        :param workspace_id: 空间id
        :type workspace_id: str
        :param task_id: 作业算子id
        :type task_id: str
        :param job_name: 作业算子名称
        :type job_name: str
        :param start_time: 搜索参数时间范围的开始时间，例：1705248000000
        :type start_time: float
        :param end_time: 搜索参数时间范围的结束时间,例：1705311669796
        :type end_time: float
        :param offset: 分页参数偏移量
        :type offset: int
        :param limit: 分页参每页数量
        :type limit: int
        """
        
        

        self._instance = None
        self._workspace_id = None
        self._task_id = None
        self._job_name = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance = instance
        if workspace_id is not None:
            self.workspace_id = workspace_id
        self.task_id = task_id
        self.job_name = job_name
        self.start_time = start_time
        self.end_time = end_time
        self.offset = offset
        self.limit = limit

    @property
    def instance(self):
        r"""Gets the instance of this ShowInstanceInfosRequest.

        实例id

        :return: The instance of this ShowInstanceInfosRequest.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this ShowInstanceInfosRequest.

        实例id

        :param instance: The instance of this ShowInstanceInfosRequest.
        :type instance: str
        """
        self._instance = instance

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowInstanceInfosRequest.

        空间id

        :return: The workspace_id of this ShowInstanceInfosRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowInstanceInfosRequest.

        空间id

        :param workspace_id: The workspace_id of this ShowInstanceInfosRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowInstanceInfosRequest.

        作业算子id

        :return: The task_id of this ShowInstanceInfosRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowInstanceInfosRequest.

        作业算子id

        :param task_id: The task_id of this ShowInstanceInfosRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ShowInstanceInfosRequest.

        作业算子名称

        :return: The job_name of this ShowInstanceInfosRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ShowInstanceInfosRequest.

        作业算子名称

        :param job_name: The job_name of this ShowInstanceInfosRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowInstanceInfosRequest.

        搜索参数时间范围的开始时间，例：1705248000000

        :return: The start_time of this ShowInstanceInfosRequest.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowInstanceInfosRequest.

        搜索参数时间范围的开始时间，例：1705248000000

        :param start_time: The start_time of this ShowInstanceInfosRequest.
        :type start_time: float
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowInstanceInfosRequest.

        搜索参数时间范围的结束时间,例：1705311669796

        :return: The end_time of this ShowInstanceInfosRequest.
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowInstanceInfosRequest.

        搜索参数时间范围的结束时间,例：1705311669796

        :param end_time: The end_time of this ShowInstanceInfosRequest.
        :type end_time: float
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ShowInstanceInfosRequest.

        分页参数偏移量

        :return: The offset of this ShowInstanceInfosRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowInstanceInfosRequest.

        分页参数偏移量

        :param offset: The offset of this ShowInstanceInfosRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowInstanceInfosRequest.

        分页参每页数量

        :return: The limit of this ShowInstanceInfosRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowInstanceInfosRequest.

        分页参每页数量

        :param limit: The limit of this ShowInstanceInfosRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowInstanceInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
