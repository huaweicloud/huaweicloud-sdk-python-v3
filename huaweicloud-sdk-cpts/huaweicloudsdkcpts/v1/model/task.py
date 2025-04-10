# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Task:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bench_concurrent': 'int',
        'description': 'str',
        'id': 'int',
        'name': 'str',
        'operate_mode': 'int',
        'task_run_info': 'TaskRunInfo',
        'update_time': 'str',
        'parallel': 'bool'
    }

    attribute_map = {
        'bench_concurrent': 'bench_concurrent',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'operate_mode': 'operate_mode',
        'task_run_info': 'task_run_info',
        'update_time': 'update_time',
        'parallel': 'parallel'
    }

    def __init__(self, bench_concurrent=None, description=None, id=None, name=None, operate_mode=None, task_run_info=None, update_time=None, parallel=None):
        r"""Task

        The model defined in huaweicloud sdk

        :param bench_concurrent: 基准并发
        :type bench_concurrent: int
        :param description: 描述信息
        :type description: str
        :param id: 任务Id
        :type id: int
        :param name: 任务名称
        :type name: str
        :param operate_mode: 任务压测模式
        :type operate_mode: int
        :param task_run_info: 
        :type task_run_info: :class:`huaweicloudsdkcpts.v1.TaskRunInfo`
        :param update_time: 更新时间
        :type update_time: str
        :param parallel: 任务间用例是否并行执行
        :type parallel: bool
        """
        
        

        self._bench_concurrent = None
        self._description = None
        self._id = None
        self._name = None
        self._operate_mode = None
        self._task_run_info = None
        self._update_time = None
        self._parallel = None
        self.discriminator = None

        if bench_concurrent is not None:
            self.bench_concurrent = bench_concurrent
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if operate_mode is not None:
            self.operate_mode = operate_mode
        if task_run_info is not None:
            self.task_run_info = task_run_info
        if update_time is not None:
            self.update_time = update_time
        if parallel is not None:
            self.parallel = parallel

    @property
    def bench_concurrent(self):
        r"""Gets the bench_concurrent of this Task.

        基准并发

        :return: The bench_concurrent of this Task.
        :rtype: int
        """
        return self._bench_concurrent

    @bench_concurrent.setter
    def bench_concurrent(self, bench_concurrent):
        r"""Sets the bench_concurrent of this Task.

        基准并发

        :param bench_concurrent: The bench_concurrent of this Task.
        :type bench_concurrent: int
        """
        self._bench_concurrent = bench_concurrent

    @property
    def description(self):
        r"""Gets the description of this Task.

        描述信息

        :return: The description of this Task.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Task.

        描述信息

        :param description: The description of this Task.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this Task.

        任务Id

        :return: The id of this Task.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Task.

        任务Id

        :param id: The id of this Task.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Task.

        任务名称

        :return: The name of this Task.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Task.

        任务名称

        :param name: The name of this Task.
        :type name: str
        """
        self._name = name

    @property
    def operate_mode(self):
        r"""Gets the operate_mode of this Task.

        任务压测模式

        :return: The operate_mode of this Task.
        :rtype: int
        """
        return self._operate_mode

    @operate_mode.setter
    def operate_mode(self, operate_mode):
        r"""Sets the operate_mode of this Task.

        任务压测模式

        :param operate_mode: The operate_mode of this Task.
        :type operate_mode: int
        """
        self._operate_mode = operate_mode

    @property
    def task_run_info(self):
        r"""Gets the task_run_info of this Task.

        :return: The task_run_info of this Task.
        :rtype: :class:`huaweicloudsdkcpts.v1.TaskRunInfo`
        """
        return self._task_run_info

    @task_run_info.setter
    def task_run_info(self, task_run_info):
        r"""Sets the task_run_info of this Task.

        :param task_run_info: The task_run_info of this Task.
        :type task_run_info: :class:`huaweicloudsdkcpts.v1.TaskRunInfo`
        """
        self._task_run_info = task_run_info

    @property
    def update_time(self):
        r"""Gets the update_time of this Task.

        更新时间

        :return: The update_time of this Task.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Task.

        更新时间

        :param update_time: The update_time of this Task.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def parallel(self):
        r"""Gets the parallel of this Task.

        任务间用例是否并行执行

        :return: The parallel of this Task.
        :rtype: bool
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        r"""Sets the parallel of this Task.

        任务间用例是否并行执行

        :param parallel: The parallel of this Task.
        :type parallel: bool
        """
        self._parallel = parallel

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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
