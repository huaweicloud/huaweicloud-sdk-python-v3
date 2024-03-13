# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'instance_id': 'int',
        'status': 'str',
        'plan_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'execute_time': 'int',
        'total': 'int',
        'nodes': 'list[NodeInstance]',
        'instance_type': 'int',
        'force_success': 'bool',
        'ignore_success': 'bool'
    }

    attribute_map = {
        'job_name': 'jobName',
        'instance_id': 'instanceId',
        'status': 'status',
        'plan_time': 'planTime',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'execute_time': 'executeTime',
        'total': 'total',
        'nodes': 'nodes',
        'instance_type': 'instanceType',
        'force_success': 'forceSuccess',
        'ignore_success': 'ignoreSuccess'
    }

    def __init__(self, job_name=None, instance_id=None, status=None, plan_time=None, start_time=None, end_time=None, execute_time=None, total=None, nodes=None, instance_type=None, force_success=None, ignore_success=None):
        """ShowJobInstanceResponse

        The model defined in huaweicloud sdk

        :param job_name: 作业名称
        :type job_name: str
        :param instance_id: 作业实例ID
        :type instance_id: int
        :param status: 作业实例状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消
        :type status: str
        :param plan_time: 作业实例计划执行时间
        :type plan_time: int
        :param start_time: 作业实例实际执行开始时间
        :type start_time: int
        :param end_time: 作业实例实际执行结束时间
        :type end_time: int
        :param execute_time: 执行耗时，单位：毫秒
        :type execute_time: int
        :param total: 总的节点数据条数
        :type total: int
        :param nodes: 节点实例状态
        :type nodes: list[:class:`huaweicloudsdkdgc.v1.NodeInstance`]
        :param instance_type: 作业调度方式： - 0：正常调度 - 2：手工调度 - 5：补数据 - 6：子作业调度 - 7：单次调度
        :type instance_type: int
        :param force_success: 作业实例状态筛选为强制成功，默认值：false
        :type force_success: bool
        :param ignore_success: 作业实例状态筛选为忽略失败，默认值：false
        :type ignore_success: bool
        """
        
        super(ShowJobInstanceResponse, self).__init__()

        self._job_name = None
        self._instance_id = None
        self._status = None
        self._plan_time = None
        self._start_time = None
        self._end_time = None
        self._execute_time = None
        self._total = None
        self._nodes = None
        self._instance_type = None
        self._force_success = None
        self._ignore_success = None
        self.discriminator = None

        if job_name is not None:
            self.job_name = job_name
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if plan_time is not None:
            self.plan_time = plan_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if execute_time is not None:
            self.execute_time = execute_time
        if total is not None:
            self.total = total
        if nodes is not None:
            self.nodes = nodes
        if instance_type is not None:
            self.instance_type = instance_type
        if force_success is not None:
            self.force_success = force_success
        if ignore_success is not None:
            self.ignore_success = ignore_success

    @property
    def job_name(self):
        """Gets the job_name of this ShowJobInstanceResponse.

        作业名称

        :return: The job_name of this ShowJobInstanceResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ShowJobInstanceResponse.

        作业名称

        :param job_name: The job_name of this ShowJobInstanceResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowJobInstanceResponse.

        作业实例ID

        :return: The instance_id of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowJobInstanceResponse.

        作业实例ID

        :param instance_id: The instance_id of this ShowJobInstanceResponse.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def status(self):
        """Gets the status of this ShowJobInstanceResponse.

        作业实例状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消

        :return: The status of this ShowJobInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowJobInstanceResponse.

        作业实例状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消

        :param status: The status of this ShowJobInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def plan_time(self):
        """Gets the plan_time of this ShowJobInstanceResponse.

        作业实例计划执行时间

        :return: The plan_time of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        """Sets the plan_time of this ShowJobInstanceResponse.

        作业实例计划执行时间

        :param plan_time: The plan_time of this ShowJobInstanceResponse.
        :type plan_time: int
        """
        self._plan_time = plan_time

    @property
    def start_time(self):
        """Gets the start_time of this ShowJobInstanceResponse.

        作业实例实际执行开始时间

        :return: The start_time of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowJobInstanceResponse.

        作业实例实际执行开始时间

        :param start_time: The start_time of this ShowJobInstanceResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowJobInstanceResponse.

        作业实例实际执行结束时间

        :return: The end_time of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowJobInstanceResponse.

        作业实例实际执行结束时间

        :param end_time: The end_time of this ShowJobInstanceResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def execute_time(self):
        """Gets the execute_time of this ShowJobInstanceResponse.

        执行耗时，单位：毫秒

        :return: The execute_time of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        """Sets the execute_time of this ShowJobInstanceResponse.

        执行耗时，单位：毫秒

        :param execute_time: The execute_time of this ShowJobInstanceResponse.
        :type execute_time: int
        """
        self._execute_time = execute_time

    @property
    def total(self):
        """Gets the total of this ShowJobInstanceResponse.

        总的节点数据条数

        :return: The total of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowJobInstanceResponse.

        总的节点数据条数

        :param total: The total of this ShowJobInstanceResponse.
        :type total: int
        """
        self._total = total

    @property
    def nodes(self):
        """Gets the nodes of this ShowJobInstanceResponse.

        节点实例状态

        :return: The nodes of this ShowJobInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.NodeInstance`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ShowJobInstanceResponse.

        节点实例状态

        :param nodes: The nodes of this ShowJobInstanceResponse.
        :type nodes: list[:class:`huaweicloudsdkdgc.v1.NodeInstance`]
        """
        self._nodes = nodes

    @property
    def instance_type(self):
        """Gets the instance_type of this ShowJobInstanceResponse.

        作业调度方式： - 0：正常调度 - 2：手工调度 - 5：补数据 - 6：子作业调度 - 7：单次调度

        :return: The instance_type of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ShowJobInstanceResponse.

        作业调度方式： - 0：正常调度 - 2：手工调度 - 5：补数据 - 6：子作业调度 - 7：单次调度

        :param instance_type: The instance_type of this ShowJobInstanceResponse.
        :type instance_type: int
        """
        self._instance_type = instance_type

    @property
    def force_success(self):
        """Gets the force_success of this ShowJobInstanceResponse.

        作业实例状态筛选为强制成功，默认值：false

        :return: The force_success of this ShowJobInstanceResponse.
        :rtype: bool
        """
        return self._force_success

    @force_success.setter
    def force_success(self, force_success):
        """Sets the force_success of this ShowJobInstanceResponse.

        作业实例状态筛选为强制成功，默认值：false

        :param force_success: The force_success of this ShowJobInstanceResponse.
        :type force_success: bool
        """
        self._force_success = force_success

    @property
    def ignore_success(self):
        """Gets the ignore_success of this ShowJobInstanceResponse.

        作业实例状态筛选为忽略失败，默认值：false

        :return: The ignore_success of this ShowJobInstanceResponse.
        :rtype: bool
        """
        return self._ignore_success

    @ignore_success.setter
    def ignore_success(self, ignore_success):
        """Sets the ignore_success of this ShowJobInstanceResponse.

        作业实例状态筛选为忽略失败，默认值：false

        :param ignore_success: The ignore_success of this ShowJobInstanceResponse.
        :type ignore_success: bool
        """
        self._ignore_success = ignore_success

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
        if not isinstance(other, ShowJobInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
