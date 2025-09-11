# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditTaskStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_time': 'int',
        'busi_type': 'str',
        'completed_num': 'int',
        'end_time': 'int',
        'id': 'int',
        'project_id': 'str',
        'query_begin_time': 'int',
        'query_end_time': 'int',
        'task_status': 'str',
        'task_switch': 'str',
        'total_num': 'int'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'busi_type': 'busi_type',
        'completed_num': 'completed_num',
        'end_time': 'end_time',
        'id': 'id',
        'project_id': 'project_id',
        'query_begin_time': 'query_begin_time',
        'query_end_time': 'query_end_time',
        'task_status': 'task_status',
        'task_switch': 'task_switch',
        'total_num': 'total_num'
    }

    def __init__(self, begin_time=None, busi_type=None, completed_num=None, end_time=None, id=None, project_id=None, query_begin_time=None, query_end_time=None, task_status=None, task_switch=None, total_num=None):
        r"""ShowAuditTaskStatusResponse

        The model defined in huaweicloud sdk

        :param begin_time: 开始时间
        :type begin_time: int
        :param busi_type: 业务类型  - audit: 审计  - risk: 风险
        :type busi_type: str
        :param completed_num: 已统计实例数
        :type completed_num: int
        :param end_time: 结束时间
        :type end_time: int
        :param id: Task任务ID
        :type id: int
        :param project_id: 项目ID
        :type project_id: str
        :param query_begin_time: 查询条件：开始时间
        :type query_begin_time: int
        :param query_end_time: 查询条件：结束时间
        :type query_end_time: int
        :param task_status: 任务状态  - 0：已就绪  - 1：运行中  - 2：成功  - 3：失败
        :type task_status: str
        :param task_switch: 任务开关
        :type task_switch: str
        :param total_num: 总实例数
        :type total_num: int
        """
        
        super(ShowAuditTaskStatusResponse, self).__init__()

        self._begin_time = None
        self._busi_type = None
        self._completed_num = None
        self._end_time = None
        self._id = None
        self._project_id = None
        self._query_begin_time = None
        self._query_end_time = None
        self._task_status = None
        self._task_switch = None
        self._total_num = None
        self.discriminator = None

        if begin_time is not None:
            self.begin_time = begin_time
        if busi_type is not None:
            self.busi_type = busi_type
        if completed_num is not None:
            self.completed_num = completed_num
        if end_time is not None:
            self.end_time = end_time
        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if query_begin_time is not None:
            self.query_begin_time = query_begin_time
        if query_end_time is not None:
            self.query_end_time = query_end_time
        if task_status is not None:
            self.task_status = task_status
        if task_switch is not None:
            self.task_switch = task_switch
        if total_num is not None:
            self.total_num = total_num

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowAuditTaskStatusResponse.

        开始时间

        :return: The begin_time of this ShowAuditTaskStatusResponse.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowAuditTaskStatusResponse.

        开始时间

        :param begin_time: The begin_time of this ShowAuditTaskStatusResponse.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def busi_type(self):
        r"""Gets the busi_type of this ShowAuditTaskStatusResponse.

        业务类型  - audit: 审计  - risk: 风险

        :return: The busi_type of this ShowAuditTaskStatusResponse.
        :rtype: str
        """
        return self._busi_type

    @busi_type.setter
    def busi_type(self, busi_type):
        r"""Sets the busi_type of this ShowAuditTaskStatusResponse.

        业务类型  - audit: 审计  - risk: 风险

        :param busi_type: The busi_type of this ShowAuditTaskStatusResponse.
        :type busi_type: str
        """
        self._busi_type = busi_type

    @property
    def completed_num(self):
        r"""Gets the completed_num of this ShowAuditTaskStatusResponse.

        已统计实例数

        :return: The completed_num of this ShowAuditTaskStatusResponse.
        :rtype: int
        """
        return self._completed_num

    @completed_num.setter
    def completed_num(self, completed_num):
        r"""Sets the completed_num of this ShowAuditTaskStatusResponse.

        已统计实例数

        :param completed_num: The completed_num of this ShowAuditTaskStatusResponse.
        :type completed_num: int
        """
        self._completed_num = completed_num

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowAuditTaskStatusResponse.

        结束时间

        :return: The end_time of this ShowAuditTaskStatusResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowAuditTaskStatusResponse.

        结束时间

        :param end_time: The end_time of this ShowAuditTaskStatusResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def id(self):
        r"""Gets the id of this ShowAuditTaskStatusResponse.

        Task任务ID

        :return: The id of this ShowAuditTaskStatusResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAuditTaskStatusResponse.

        Task任务ID

        :param id: The id of this ShowAuditTaskStatusResponse.
        :type id: int
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowAuditTaskStatusResponse.

        项目ID

        :return: The project_id of this ShowAuditTaskStatusResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowAuditTaskStatusResponse.

        项目ID

        :param project_id: The project_id of this ShowAuditTaskStatusResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def query_begin_time(self):
        r"""Gets the query_begin_time of this ShowAuditTaskStatusResponse.

        查询条件：开始时间

        :return: The query_begin_time of this ShowAuditTaskStatusResponse.
        :rtype: int
        """
        return self._query_begin_time

    @query_begin_time.setter
    def query_begin_time(self, query_begin_time):
        r"""Sets the query_begin_time of this ShowAuditTaskStatusResponse.

        查询条件：开始时间

        :param query_begin_time: The query_begin_time of this ShowAuditTaskStatusResponse.
        :type query_begin_time: int
        """
        self._query_begin_time = query_begin_time

    @property
    def query_end_time(self):
        r"""Gets the query_end_time of this ShowAuditTaskStatusResponse.

        查询条件：结束时间

        :return: The query_end_time of this ShowAuditTaskStatusResponse.
        :rtype: int
        """
        return self._query_end_time

    @query_end_time.setter
    def query_end_time(self, query_end_time):
        r"""Sets the query_end_time of this ShowAuditTaskStatusResponse.

        查询条件：结束时间

        :param query_end_time: The query_end_time of this ShowAuditTaskStatusResponse.
        :type query_end_time: int
        """
        self._query_end_time = query_end_time

    @property
    def task_status(self):
        r"""Gets the task_status of this ShowAuditTaskStatusResponse.

        任务状态  - 0：已就绪  - 1：运行中  - 2：成功  - 3：失败

        :return: The task_status of this ShowAuditTaskStatusResponse.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ShowAuditTaskStatusResponse.

        任务状态  - 0：已就绪  - 1：运行中  - 2：成功  - 3：失败

        :param task_status: The task_status of this ShowAuditTaskStatusResponse.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def task_switch(self):
        r"""Gets the task_switch of this ShowAuditTaskStatusResponse.

        任务开关

        :return: The task_switch of this ShowAuditTaskStatusResponse.
        :rtype: str
        """
        return self._task_switch

    @task_switch.setter
    def task_switch(self, task_switch):
        r"""Sets the task_switch of this ShowAuditTaskStatusResponse.

        任务开关

        :param task_switch: The task_switch of this ShowAuditTaskStatusResponse.
        :type task_switch: str
        """
        self._task_switch = task_switch

    @property
    def total_num(self):
        r"""Gets the total_num of this ShowAuditTaskStatusResponse.

        总实例数

        :return: The total_num of this ShowAuditTaskStatusResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ShowAuditTaskStatusResponse.

        总实例数

        :param total_num: The total_num of this ShowAuditTaskStatusResponse.
        :type total_num: int
        """
        self._total_num = total_num

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
        if not isinstance(other, ShowAuditTaskStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
