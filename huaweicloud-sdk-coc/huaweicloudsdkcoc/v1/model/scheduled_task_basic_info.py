# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTaskBasicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'enterprise_project_id': 'str',
        'name': 'str',
        'scheduled_type': 'str',
        'task_type': 'str',
        'associated_task_type': 'str',
        'risk_level': 'str',
        'created_by': 'str',
        'update_by': 'str',
        'created_user_name': 'str',
        'reviewer': 'str',
        'reviewer_user_name': 'str',
        'approve_status': 'object',
        'last_execution_time': 'int',
        'last_execution_status': 'str',
        'execution_count': 'int',
        'enabled': 'bool',
        'created_time': 'int',
        'modified_time': 'int',
        'region_id': 'str',
        'associated_task_name': 'str',
        'associated_task_name_en': 'str'
    }

    attribute_map = {
        'id': 'id',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'scheduled_type': 'scheduled_type',
        'task_type': 'task_type',
        'associated_task_type': 'associated_task_type',
        'risk_level': 'risk_level',
        'created_by': 'created_by',
        'update_by': 'update_by',
        'created_user_name': 'created_user_name',
        'reviewer': 'reviewer',
        'reviewer_user_name': 'reviewer_user_name',
        'approve_status': 'approve_status',
        'last_execution_time': 'last_execution_time',
        'last_execution_status': 'last_execution_status',
        'execution_count': 'execution_count',
        'enabled': 'enabled',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'region_id': 'region_id',
        'associated_task_name': 'associated_task_name',
        'associated_task_name_en': 'associated_task_name_en'
    }

    def __init__(self, id=None, enterprise_project_id=None, name=None, scheduled_type=None, task_type=None, associated_task_type=None, risk_level=None, created_by=None, update_by=None, created_user_name=None, reviewer=None, reviewer_user_name=None, approve_status=None, last_execution_time=None, last_execution_status=None, execution_count=None, enabled=None, created_time=None, modified_time=None, region_id=None, associated_task_name=None, associated_task_name_en=None):
        r"""ScheduledTaskBasicInfo

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param name: 任务名称
        :type name: str
        :param scheduled_type: 定时类型
        :type scheduled_type: str
        :param task_type: 引用任务类型
        :type task_type: str
        :param associated_task_type: 关联的任务类型
        :type associated_task_type: str
        :param risk_level: 风险等级
        :type risk_level: str
        :param created_by: 创建人
        :type created_by: str
        :param update_by: 修改人
        :type update_by: str
        :param created_user_name: 创建人昵称
        :type created_user_name: str
        :param reviewer: 审批人
        :type reviewer: str
        :param reviewer_user_name: 审批人昵称
        :type reviewer_user_name: str
        :param approve_status: 审批状态
        :type approve_status: object
        :param last_execution_time: 最近执行时间时间戳
        :type last_execution_time: int
        :param last_execution_status: 最近执行状态
        :type last_execution_status: str
        :param execution_count: 执行次数
        :type execution_count: int
        :param enabled: 是否启用
        :type enabled: bool
        :param created_time: 创建时间
        :type created_time: int
        :param modified_time: 更新时间
        :type modified_time: int
        :param region_id: 区域
        :type region_id: str
        :param associated_task_name: 脚本/作业名称
        :type associated_task_name: str
        :param associated_task_name_en: 脚本/作业名称(英文)
        :type associated_task_name_en: str
        """
        
        

        self._id = None
        self._enterprise_project_id = None
        self._name = None
        self._scheduled_type = None
        self._task_type = None
        self._associated_task_type = None
        self._risk_level = None
        self._created_by = None
        self._update_by = None
        self._created_user_name = None
        self._reviewer = None
        self._reviewer_user_name = None
        self._approve_status = None
        self._last_execution_time = None
        self._last_execution_status = None
        self._execution_count = None
        self._enabled = None
        self._created_time = None
        self._modified_time = None
        self._region_id = None
        self._associated_task_name = None
        self._associated_task_name_en = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if name is not None:
            self.name = name
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
        if update_by is not None:
            self.update_by = update_by
        if created_user_name is not None:
            self.created_user_name = created_user_name
        if reviewer is not None:
            self.reviewer = reviewer
        if reviewer_user_name is not None:
            self.reviewer_user_name = reviewer_user_name
        if approve_status is not None:
            self.approve_status = approve_status
        if last_execution_time is not None:
            self.last_execution_time = last_execution_time
        if last_execution_status is not None:
            self.last_execution_status = last_execution_status
        if execution_count is not None:
            self.execution_count = execution_count
        if enabled is not None:
            self.enabled = enabled
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if region_id is not None:
            self.region_id = region_id
        if associated_task_name is not None:
            self.associated_task_name = associated_task_name
        if associated_task_name_en is not None:
            self.associated_task_name_en = associated_task_name_en

    @property
    def id(self):
        r"""Gets the id of this ScheduledTaskBasicInfo.

        任务ID

        :return: The id of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScheduledTaskBasicInfo.

        任务ID

        :param id: The id of this ScheduledTaskBasicInfo.
        :type id: str
        """
        self._id = id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ScheduledTaskBasicInfo.

        企业项目id

        :return: The enterprise_project_id of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ScheduledTaskBasicInfo.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ScheduledTaskBasicInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this ScheduledTaskBasicInfo.

        任务名称

        :return: The name of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScheduledTaskBasicInfo.

        任务名称

        :param name: The name of this ScheduledTaskBasicInfo.
        :type name: str
        """
        self._name = name

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this ScheduledTaskBasicInfo.

        定时类型

        :return: The scheduled_type of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this ScheduledTaskBasicInfo.

        定时类型

        :param scheduled_type: The scheduled_type of this ScheduledTaskBasicInfo.
        :type scheduled_type: str
        """
        self._scheduled_type = scheduled_type

    @property
    def task_type(self):
        r"""Gets the task_type of this ScheduledTaskBasicInfo.

        引用任务类型

        :return: The task_type of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ScheduledTaskBasicInfo.

        引用任务类型

        :param task_type: The task_type of this ScheduledTaskBasicInfo.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def associated_task_type(self):
        r"""Gets the associated_task_type of this ScheduledTaskBasicInfo.

        关联的任务类型

        :return: The associated_task_type of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._associated_task_type

    @associated_task_type.setter
    def associated_task_type(self, associated_task_type):
        r"""Sets the associated_task_type of this ScheduledTaskBasicInfo.

        关联的任务类型

        :param associated_task_type: The associated_task_type of this ScheduledTaskBasicInfo.
        :type associated_task_type: str
        """
        self._associated_task_type = associated_task_type

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ScheduledTaskBasicInfo.

        风险等级

        :return: The risk_level of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ScheduledTaskBasicInfo.

        风险等级

        :param risk_level: The risk_level of this ScheduledTaskBasicInfo.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def created_by(self):
        r"""Gets the created_by of this ScheduledTaskBasicInfo.

        创建人

        :return: The created_by of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ScheduledTaskBasicInfo.

        创建人

        :param created_by: The created_by of this ScheduledTaskBasicInfo.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def update_by(self):
        r"""Gets the update_by of this ScheduledTaskBasicInfo.

        修改人

        :return: The update_by of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this ScheduledTaskBasicInfo.

        修改人

        :param update_by: The update_by of this ScheduledTaskBasicInfo.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def created_user_name(self):
        r"""Gets the created_user_name of this ScheduledTaskBasicInfo.

        创建人昵称

        :return: The created_user_name of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._created_user_name

    @created_user_name.setter
    def created_user_name(self, created_user_name):
        r"""Sets the created_user_name of this ScheduledTaskBasicInfo.

        创建人昵称

        :param created_user_name: The created_user_name of this ScheduledTaskBasicInfo.
        :type created_user_name: str
        """
        self._created_user_name = created_user_name

    @property
    def reviewer(self):
        r"""Gets the reviewer of this ScheduledTaskBasicInfo.

        审批人

        :return: The reviewer of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        r"""Sets the reviewer of this ScheduledTaskBasicInfo.

        审批人

        :param reviewer: The reviewer of this ScheduledTaskBasicInfo.
        :type reviewer: str
        """
        self._reviewer = reviewer

    @property
    def reviewer_user_name(self):
        r"""Gets the reviewer_user_name of this ScheduledTaskBasicInfo.

        审批人昵称

        :return: The reviewer_user_name of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._reviewer_user_name

    @reviewer_user_name.setter
    def reviewer_user_name(self, reviewer_user_name):
        r"""Sets the reviewer_user_name of this ScheduledTaskBasicInfo.

        审批人昵称

        :param reviewer_user_name: The reviewer_user_name of this ScheduledTaskBasicInfo.
        :type reviewer_user_name: str
        """
        self._reviewer_user_name = reviewer_user_name

    @property
    def approve_status(self):
        r"""Gets the approve_status of this ScheduledTaskBasicInfo.

        审批状态

        :return: The approve_status of this ScheduledTaskBasicInfo.
        :rtype: object
        """
        return self._approve_status

    @approve_status.setter
    def approve_status(self, approve_status):
        r"""Sets the approve_status of this ScheduledTaskBasicInfo.

        审批状态

        :param approve_status: The approve_status of this ScheduledTaskBasicInfo.
        :type approve_status: object
        """
        self._approve_status = approve_status

    @property
    def last_execution_time(self):
        r"""Gets the last_execution_time of this ScheduledTaskBasicInfo.

        最近执行时间时间戳

        :return: The last_execution_time of this ScheduledTaskBasicInfo.
        :rtype: int
        """
        return self._last_execution_time

    @last_execution_time.setter
    def last_execution_time(self, last_execution_time):
        r"""Sets the last_execution_time of this ScheduledTaskBasicInfo.

        最近执行时间时间戳

        :param last_execution_time: The last_execution_time of this ScheduledTaskBasicInfo.
        :type last_execution_time: int
        """
        self._last_execution_time = last_execution_time

    @property
    def last_execution_status(self):
        r"""Gets the last_execution_status of this ScheduledTaskBasicInfo.

        最近执行状态

        :return: The last_execution_status of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._last_execution_status

    @last_execution_status.setter
    def last_execution_status(self, last_execution_status):
        r"""Sets the last_execution_status of this ScheduledTaskBasicInfo.

        最近执行状态

        :param last_execution_status: The last_execution_status of this ScheduledTaskBasicInfo.
        :type last_execution_status: str
        """
        self._last_execution_status = last_execution_status

    @property
    def execution_count(self):
        r"""Gets the execution_count of this ScheduledTaskBasicInfo.

        执行次数

        :return: The execution_count of this ScheduledTaskBasicInfo.
        :rtype: int
        """
        return self._execution_count

    @execution_count.setter
    def execution_count(self, execution_count):
        r"""Sets the execution_count of this ScheduledTaskBasicInfo.

        执行次数

        :param execution_count: The execution_count of this ScheduledTaskBasicInfo.
        :type execution_count: int
        """
        self._execution_count = execution_count

    @property
    def enabled(self):
        r"""Gets the enabled of this ScheduledTaskBasicInfo.

        是否启用

        :return: The enabled of this ScheduledTaskBasicInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ScheduledTaskBasicInfo.

        是否启用

        :param enabled: The enabled of this ScheduledTaskBasicInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def created_time(self):
        r"""Gets the created_time of this ScheduledTaskBasicInfo.

        创建时间

        :return: The created_time of this ScheduledTaskBasicInfo.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ScheduledTaskBasicInfo.

        创建时间

        :param created_time: The created_time of this ScheduledTaskBasicInfo.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this ScheduledTaskBasicInfo.

        更新时间

        :return: The modified_time of this ScheduledTaskBasicInfo.
        :rtype: int
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this ScheduledTaskBasicInfo.

        更新时间

        :param modified_time: The modified_time of this ScheduledTaskBasicInfo.
        :type modified_time: int
        """
        self._modified_time = modified_time

    @property
    def region_id(self):
        r"""Gets the region_id of this ScheduledTaskBasicInfo.

        区域

        :return: The region_id of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ScheduledTaskBasicInfo.

        区域

        :param region_id: The region_id of this ScheduledTaskBasicInfo.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def associated_task_name(self):
        r"""Gets the associated_task_name of this ScheduledTaskBasicInfo.

        脚本/作业名称

        :return: The associated_task_name of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._associated_task_name

    @associated_task_name.setter
    def associated_task_name(self, associated_task_name):
        r"""Sets the associated_task_name of this ScheduledTaskBasicInfo.

        脚本/作业名称

        :param associated_task_name: The associated_task_name of this ScheduledTaskBasicInfo.
        :type associated_task_name: str
        """
        self._associated_task_name = associated_task_name

    @property
    def associated_task_name_en(self):
        r"""Gets the associated_task_name_en of this ScheduledTaskBasicInfo.

        脚本/作业名称(英文)

        :return: The associated_task_name_en of this ScheduledTaskBasicInfo.
        :rtype: str
        """
        return self._associated_task_name_en

    @associated_task_name_en.setter
    def associated_task_name_en(self, associated_task_name_en):
        r"""Sets the associated_task_name_en of this ScheduledTaskBasicInfo.

        脚本/作业名称(英文)

        :param associated_task_name_en: The associated_task_name_en of this ScheduledTaskBasicInfo.
        :type associated_task_name_en: str
        """
        self._associated_task_name_en = associated_task_name_en

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
        if not isinstance(other, ScheduledTaskBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
