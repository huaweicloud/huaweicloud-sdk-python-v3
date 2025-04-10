# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'min_plan_time': 'int',
        'max_plan_time': 'int',
        'status': 'str',
        'precise_query': 'bool',
        'job_name': 'str',
        'instance_type': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'min_plan_time': 'minPlanTime',
        'max_plan_time': 'maxPlanTime',
        'status': 'status',
        'precise_query': 'preciseQuery',
        'job_name': 'jobName',
        'instance_type': 'instanceType'
    }

    def __init__(self, workspace=None, limit=None, offset=None, min_plan_time=None, max_plan_time=None, status=None, precise_query=None, job_name=None, instance_type=None):
        r"""ListJobInstancesRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param limit: 分页参数:每页限定数量
        :type limit: int
        :param offset: 分页参数：页数
        :type offset: int
        :param min_plan_time: 返回作业实际开始时间大于minPlanTime的作业实例，单位为毫秒ms。
        :type min_plan_time: int
        :param max_plan_time: 返回作业实际开始时间小于maxPlanTime的作业实例，单位为毫秒ms。
        :type max_plan_time: int
        :param status: 实例运行状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消
        :type status: str
        :param precise_query: 支持通过作业名进行精确查询。
        :type precise_query: bool
        :param job_name: 作业名称。如果要查询指定批处理作业的实例列表，jobName就是批处理作业名称；如果要查询实时作业下某个节点关联的子作业，jobName格式为[实时作业名称]_[节点名称]。
        :type job_name: str
        :param instance_type: 作业调度方式： - 0：正常调度 - 2：手工调度 - 5：补数据 - 6：子作业调度 - 7：单次调度
        :type instance_type: str
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._min_plan_time = None
        self._max_plan_time = None
        self._status = None
        self._precise_query = None
        self._job_name = None
        self._instance_type = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if min_plan_time is not None:
            self.min_plan_time = min_plan_time
        if max_plan_time is not None:
            self.max_plan_time = max_plan_time
        if status is not None:
            self.status = status
        if precise_query is not None:
            self.precise_query = precise_query
        if job_name is not None:
            self.job_name = job_name
        if instance_type is not None:
            self.instance_type = instance_type

    @property
    def workspace(self):
        r"""Gets the workspace of this ListJobInstancesRequest.

        工作空间id

        :return: The workspace of this ListJobInstancesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListJobInstancesRequest.

        工作空间id

        :param workspace: The workspace of this ListJobInstancesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        r"""Gets the limit of this ListJobInstancesRequest.

        分页参数:每页限定数量

        :return: The limit of this ListJobInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListJobInstancesRequest.

        分页参数:每页限定数量

        :param limit: The limit of this ListJobInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListJobInstancesRequest.

        分页参数：页数

        :return: The offset of this ListJobInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListJobInstancesRequest.

        分页参数：页数

        :param offset: The offset of this ListJobInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def min_plan_time(self):
        r"""Gets the min_plan_time of this ListJobInstancesRequest.

        返回作业实际开始时间大于minPlanTime的作业实例，单位为毫秒ms。

        :return: The min_plan_time of this ListJobInstancesRequest.
        :rtype: int
        """
        return self._min_plan_time

    @min_plan_time.setter
    def min_plan_time(self, min_plan_time):
        r"""Sets the min_plan_time of this ListJobInstancesRequest.

        返回作业实际开始时间大于minPlanTime的作业实例，单位为毫秒ms。

        :param min_plan_time: The min_plan_time of this ListJobInstancesRequest.
        :type min_plan_time: int
        """
        self._min_plan_time = min_plan_time

    @property
    def max_plan_time(self):
        r"""Gets the max_plan_time of this ListJobInstancesRequest.

        返回作业实际开始时间小于maxPlanTime的作业实例，单位为毫秒ms。

        :return: The max_plan_time of this ListJobInstancesRequest.
        :rtype: int
        """
        return self._max_plan_time

    @max_plan_time.setter
    def max_plan_time(self, max_plan_time):
        r"""Sets the max_plan_time of this ListJobInstancesRequest.

        返回作业实际开始时间小于maxPlanTime的作业实例，单位为毫秒ms。

        :param max_plan_time: The max_plan_time of this ListJobInstancesRequest.
        :type max_plan_time: int
        """
        self._max_plan_time = max_plan_time

    @property
    def status(self):
        r"""Gets the status of this ListJobInstancesRequest.

        实例运行状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消

        :return: The status of this ListJobInstancesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListJobInstancesRequest.

        实例运行状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消

        :param status: The status of this ListJobInstancesRequest.
        :type status: str
        """
        self._status = status

    @property
    def precise_query(self):
        r"""Gets the precise_query of this ListJobInstancesRequest.

        支持通过作业名进行精确查询。

        :return: The precise_query of this ListJobInstancesRequest.
        :rtype: bool
        """
        return self._precise_query

    @precise_query.setter
    def precise_query(self, precise_query):
        r"""Sets the precise_query of this ListJobInstancesRequest.

        支持通过作业名进行精确查询。

        :param precise_query: The precise_query of this ListJobInstancesRequest.
        :type precise_query: bool
        """
        self._precise_query = precise_query

    @property
    def job_name(self):
        r"""Gets the job_name of this ListJobInstancesRequest.

        作业名称。如果要查询指定批处理作业的实例列表，jobName就是批处理作业名称；如果要查询实时作业下某个节点关联的子作业，jobName格式为[实时作业名称]_[节点名称]。

        :return: The job_name of this ListJobInstancesRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListJobInstancesRequest.

        作业名称。如果要查询指定批处理作业的实例列表，jobName就是批处理作业名称；如果要查询实时作业下某个节点关联的子作业，jobName格式为[实时作业名称]_[节点名称]。

        :param job_name: The job_name of this ListJobInstancesRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def instance_type(self):
        r"""Gets the instance_type of this ListJobInstancesRequest.

        作业调度方式： - 0：正常调度 - 2：手工调度 - 5：补数据 - 6：子作业调度 - 7：单次调度

        :return: The instance_type of this ListJobInstancesRequest.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this ListJobInstancesRequest.

        作业调度方式： - 0：正常调度 - 2：手工调度 - 5：补数据 - 6：子作业调度 - 7：单次调度

        :param instance_type: The instance_type of this ListJobInstancesRequest.
        :type instance_type: str
        """
        self._instance_type = instance_type

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
        if not isinstance(other, ListJobInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
