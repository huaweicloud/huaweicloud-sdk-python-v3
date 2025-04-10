# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'task_id': 'str',
        'task_name': 'str',
        'scheduled_type': 'str',
        'task_type': 'str',
        'associated_task_type': 'str',
        'risk_level': 'str',
        'created_by': 'str',
        'reviewer': 'str',
        'reviewer_user_name': 'str',
        'approve_status': 'str',
        'last_execution_status': 'str',
        'last_execution_start_time': 'int',
        'last_execution_end_time': 'int',
        'marker': 'str',
        'region_id': 'str',
        'resource_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'scheduled_type': 'scheduled_type',
        'task_type': 'task_type',
        'associated_task_type': 'associated_task_type',
        'risk_level': 'risk_level',
        'created_by': 'created_by',
        'reviewer': 'reviewer',
        'reviewer_user_name': 'reviewer_user_name',
        'approve_status': 'approve_status',
        'last_execution_status': 'last_execution_status',
        'last_execution_start_time': 'last_execution_start_time',
        'last_execution_end_time': 'last_execution_end_time',
        'marker': 'marker',
        'region_id': 'region_id',
        'resource_id': 'resource_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, enterprise_project_id=None, task_id=None, task_name=None, scheduled_type=None, task_type=None, associated_task_type=None, risk_level=None, created_by=None, reviewer=None, reviewer_user_name=None, approve_status=None, last_execution_status=None, last_execution_start_time=None, last_execution_end_time=None, marker=None, region_id=None, resource_id=None, offset=None, limit=None):
        r"""ListScheduledTaskRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param task_id: 任务ID
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        :param scheduled_type: 定时类型(ONCE,PERIODIC,CRON)
        :type scheduled_type: str
        :param task_type: 引用任务类型(SCRIPT,RUNBOOK)
        :type task_type: str
        :param associated_task_type: 任务类型(CUSTOMIZATION,COMMUNAL)
        :type associated_task_type: str
        :param risk_level: 风险等级
        :type risk_level: str
        :param created_by: 创建人
        :type created_by: str
        :param reviewer: 审批人ID
        :type reviewer: str
        :param reviewer_user_name: 审批人昵称
        :type reviewer_user_name: str
        :param approve_status: 审批状态(PENDING,REJECTED,PASSED)
        :type approve_status: str
        :param last_execution_status: 最近执行状态(READY,PROCESSING,ABNORMAL,FINISHED,PAUSED,CANCELED)
        :type last_execution_status: str
        :param last_execution_start_time: 最近执行时间的查询开始时间
        :type last_execution_start_time: int
        :param last_execution_end_time: 最近执行时间的查询结束时间
        :type last_execution_end_time: int
        :param marker: 上一页数据的最后一条记录的id
        :type marker: str
        :param region_id: 区域
        :type region_id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param offset: 分页指针
        :type offset: int
        :param limit: 每页数量
        :type limit: int
        """
        
        

        self._enterprise_project_id = None
        self._task_id = None
        self._task_name = None
        self._scheduled_type = None
        self._task_type = None
        self._associated_task_type = None
        self._risk_level = None
        self._created_by = None
        self._reviewer = None
        self._reviewer_user_name = None
        self._approve_status = None
        self._last_execution_status = None
        self._last_execution_start_time = None
        self._last_execution_end_time = None
        self._marker = None
        self._region_id = None
        self._resource_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if scheduled_type is not None:
            self.scheduled_type = scheduled_type
        if task_type is not None:
            self.task_type = task_type
        if associated_task_type is not None:
            self.associated_task_type = associated_task_type
        if risk_level is not None:
            self.risk_level = risk_level
        if created_by is not None:
            self.created_by = created_by
        if reviewer is not None:
            self.reviewer = reviewer
        if reviewer_user_name is not None:
            self.reviewer_user_name = reviewer_user_name
        if approve_status is not None:
            self.approve_status = approve_status
        if last_execution_status is not None:
            self.last_execution_status = last_execution_status
        if last_execution_start_time is not None:
            self.last_execution_start_time = last_execution_start_time
        if last_execution_end_time is not None:
            self.last_execution_end_time = last_execution_end_time
        if marker is not None:
            self.marker = marker
        if region_id is not None:
            self.region_id = region_id
        if resource_id is not None:
            self.resource_id = resource_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListScheduledTaskRequest.

        企业项目id

        :return: The enterprise_project_id of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListScheduledTaskRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListScheduledTaskRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ListScheduledTaskRequest.

        任务ID

        :return: The task_id of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListScheduledTaskRequest.

        任务ID

        :param task_id: The task_id of this ListScheduledTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ListScheduledTaskRequest.

        任务名称

        :return: The task_name of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListScheduledTaskRequest.

        任务名称

        :param task_name: The task_name of this ListScheduledTaskRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this ListScheduledTaskRequest.

        定时类型(ONCE,PERIODIC,CRON)

        :return: The scheduled_type of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this ListScheduledTaskRequest.

        定时类型(ONCE,PERIODIC,CRON)

        :param scheduled_type: The scheduled_type of this ListScheduledTaskRequest.
        :type scheduled_type: str
        """
        self._scheduled_type = scheduled_type

    @property
    def task_type(self):
        r"""Gets the task_type of this ListScheduledTaskRequest.

        引用任务类型(SCRIPT,RUNBOOK)

        :return: The task_type of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListScheduledTaskRequest.

        引用任务类型(SCRIPT,RUNBOOK)

        :param task_type: The task_type of this ListScheduledTaskRequest.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def associated_task_type(self):
        r"""Gets the associated_task_type of this ListScheduledTaskRequest.

        任务类型(CUSTOMIZATION,COMMUNAL)

        :return: The associated_task_type of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._associated_task_type

    @associated_task_type.setter
    def associated_task_type(self, associated_task_type):
        r"""Sets the associated_task_type of this ListScheduledTaskRequest.

        任务类型(CUSTOMIZATION,COMMUNAL)

        :param associated_task_type: The associated_task_type of this ListScheduledTaskRequest.
        :type associated_task_type: str
        """
        self._associated_task_type = associated_task_type

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ListScheduledTaskRequest.

        风险等级

        :return: The risk_level of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ListScheduledTaskRequest.

        风险等级

        :param risk_level: The risk_level of this ListScheduledTaskRequest.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def created_by(self):
        r"""Gets the created_by of this ListScheduledTaskRequest.

        创建人

        :return: The created_by of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ListScheduledTaskRequest.

        创建人

        :param created_by: The created_by of this ListScheduledTaskRequest.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def reviewer(self):
        r"""Gets the reviewer of this ListScheduledTaskRequest.

        审批人ID

        :return: The reviewer of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        r"""Sets the reviewer of this ListScheduledTaskRequest.

        审批人ID

        :param reviewer: The reviewer of this ListScheduledTaskRequest.
        :type reviewer: str
        """
        self._reviewer = reviewer

    @property
    def reviewer_user_name(self):
        r"""Gets the reviewer_user_name of this ListScheduledTaskRequest.

        审批人昵称

        :return: The reviewer_user_name of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._reviewer_user_name

    @reviewer_user_name.setter
    def reviewer_user_name(self, reviewer_user_name):
        r"""Sets the reviewer_user_name of this ListScheduledTaskRequest.

        审批人昵称

        :param reviewer_user_name: The reviewer_user_name of this ListScheduledTaskRequest.
        :type reviewer_user_name: str
        """
        self._reviewer_user_name = reviewer_user_name

    @property
    def approve_status(self):
        r"""Gets the approve_status of this ListScheduledTaskRequest.

        审批状态(PENDING,REJECTED,PASSED)

        :return: The approve_status of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._approve_status

    @approve_status.setter
    def approve_status(self, approve_status):
        r"""Sets the approve_status of this ListScheduledTaskRequest.

        审批状态(PENDING,REJECTED,PASSED)

        :param approve_status: The approve_status of this ListScheduledTaskRequest.
        :type approve_status: str
        """
        self._approve_status = approve_status

    @property
    def last_execution_status(self):
        r"""Gets the last_execution_status of this ListScheduledTaskRequest.

        最近执行状态(READY,PROCESSING,ABNORMAL,FINISHED,PAUSED,CANCELED)

        :return: The last_execution_status of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._last_execution_status

    @last_execution_status.setter
    def last_execution_status(self, last_execution_status):
        r"""Sets the last_execution_status of this ListScheduledTaskRequest.

        最近执行状态(READY,PROCESSING,ABNORMAL,FINISHED,PAUSED,CANCELED)

        :param last_execution_status: The last_execution_status of this ListScheduledTaskRequest.
        :type last_execution_status: str
        """
        self._last_execution_status = last_execution_status

    @property
    def last_execution_start_time(self):
        r"""Gets the last_execution_start_time of this ListScheduledTaskRequest.

        最近执行时间的查询开始时间

        :return: The last_execution_start_time of this ListScheduledTaskRequest.
        :rtype: int
        """
        return self._last_execution_start_time

    @last_execution_start_time.setter
    def last_execution_start_time(self, last_execution_start_time):
        r"""Sets the last_execution_start_time of this ListScheduledTaskRequest.

        最近执行时间的查询开始时间

        :param last_execution_start_time: The last_execution_start_time of this ListScheduledTaskRequest.
        :type last_execution_start_time: int
        """
        self._last_execution_start_time = last_execution_start_time

    @property
    def last_execution_end_time(self):
        r"""Gets the last_execution_end_time of this ListScheduledTaskRequest.

        最近执行时间的查询结束时间

        :return: The last_execution_end_time of this ListScheduledTaskRequest.
        :rtype: int
        """
        return self._last_execution_end_time

    @last_execution_end_time.setter
    def last_execution_end_time(self, last_execution_end_time):
        r"""Sets the last_execution_end_time of this ListScheduledTaskRequest.

        最近执行时间的查询结束时间

        :param last_execution_end_time: The last_execution_end_time of this ListScheduledTaskRequest.
        :type last_execution_end_time: int
        """
        self._last_execution_end_time = last_execution_end_time

    @property
    def marker(self):
        r"""Gets the marker of this ListScheduledTaskRequest.

        上一页数据的最后一条记录的id

        :return: The marker of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListScheduledTaskRequest.

        上一页数据的最后一条记录的id

        :param marker: The marker of this ListScheduledTaskRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def region_id(self):
        r"""Gets the region_id of this ListScheduledTaskRequest.

        区域

        :return: The region_id of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListScheduledTaskRequest.

        区域

        :param region_id: The region_id of this ListScheduledTaskRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListScheduledTaskRequest.

        资源ID

        :return: The resource_id of this ListScheduledTaskRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListScheduledTaskRequest.

        资源ID

        :param resource_id: The resource_id of this ListScheduledTaskRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def offset(self):
        r"""Gets the offset of this ListScheduledTaskRequest.

        分页指针

        :return: The offset of this ListScheduledTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScheduledTaskRequest.

        分页指针

        :param offset: The offset of this ListScheduledTaskRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduledTaskRequest.

        每页数量

        :return: The limit of this ListScheduledTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduledTaskRequest.

        每页数量

        :param limit: The limit of this ListScheduledTaskRequest.
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
        if not isinstance(other, ListScheduledTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
