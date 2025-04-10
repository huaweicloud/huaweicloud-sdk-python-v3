# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueResponseV4:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'actual_work_hours': 'float',
        'assigned_cc_user': 'list[IssueUser]',
        'assigned_user': 'IssueUser',
        'begin_time': 'str',
        'created_time': 'str',
        'creator': 'IssueUser',
        'custom_fields': 'list[CustomField]',
        'new_custom_fields': 'list[NewCustomField]',
        'developer': 'IssueUser',
        'domain': 'IssueItemSfV4Domain',
        'done_ratio': 'int',
        'end_time': 'str',
        'expected_work_hours': 'float',
        'id': 'int',
        'project': 'IssueProjectResponseV4',
        'iteration': 'IssueItemSfV4Iteration',
        'module': 'IssueItemSfV4Module',
        'name': 'str',
        'parent_issue': 'CreateIssueResponseV4ParentIssue',
        'priority': 'IssueItemSfV4Priority',
        'order': 'IssueResponseV4Order',
        'severity': 'IssueItemSfV4Severity',
        'status': 'IssueItemSfV4Status',
        'release_dev': 'str',
        'find_release_dev': 'str',
        'env': 'IssueDetailResponseV4Env',
        'tracker': 'CreateIssueResponseV4Tracker',
        'updated_time': 'str',
        'closed_time': 'str'
    }

    attribute_map = {
        'actual_work_hours': 'actual_work_hours',
        'assigned_cc_user': 'assigned_cc_user',
        'assigned_user': 'assigned_user',
        'begin_time': 'begin_time',
        'created_time': 'created_time',
        'creator': 'creator',
        'custom_fields': 'custom_fields',
        'new_custom_fields': 'new_custom_fields',
        'developer': 'developer',
        'domain': 'domain',
        'done_ratio': 'done_ratio',
        'end_time': 'end_time',
        'expected_work_hours': 'expected_work_hours',
        'id': 'id',
        'project': 'project',
        'iteration': 'iteration',
        'module': 'module',
        'name': 'name',
        'parent_issue': 'parent_issue',
        'priority': 'priority',
        'order': 'order',
        'severity': 'severity',
        'status': 'status',
        'release_dev': 'release_dev',
        'find_release_dev': 'find_release_dev',
        'env': 'env',
        'tracker': 'tracker',
        'updated_time': 'updated_time',
        'closed_time': 'closed_time'
    }

    def __init__(self, actual_work_hours=None, assigned_cc_user=None, assigned_user=None, begin_time=None, created_time=None, creator=None, custom_fields=None, new_custom_fields=None, developer=None, domain=None, done_ratio=None, end_time=None, expected_work_hours=None, id=None, project=None, iteration=None, module=None, name=None, parent_issue=None, priority=None, order=None, severity=None, status=None, release_dev=None, find_release_dev=None, env=None, tracker=None, updated_time=None, closed_time=None):
        r"""IssueResponseV4

        The model defined in huaweicloud sdk

        :param actual_work_hours: 实际工时
        :type actual_work_hours: float
        :param assigned_cc_user: 抄送人
        :type assigned_cc_user: list[:class:`huaweicloudsdkprojectman.v4.IssueUser`]
        :param assigned_user: 
        :type assigned_user: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        :param begin_time: 预计开始时间，年-月-日
        :type begin_time: str
        :param created_time: 创建时间 年-月-日 时:分:秒
        :type created_time: str
        :param creator: 
        :type creator: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        :param custom_fields: 自定义属性值,不建议使用，建议参考new_custom_fields字段
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.CustomField`]
        :param new_custom_fields: 自定义属性值
        :type new_custom_fields: list[:class:`huaweicloudsdkprojectman.v4.NewCustomField`]
        :param developer: 
        :type developer: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        :param domain: 
        :type domain: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Domain`
        :param done_ratio: 工作项进度值
        :type done_ratio: int
        :param end_time: 预计结束时间，年-月-日
        :type end_time: str
        :param expected_work_hours: 预计工时
        :type expected_work_hours: float
        :param id: 工作项项id
        :type id: int
        :param project: 
        :type project: :class:`huaweicloudsdkprojectman.v4.IssueProjectResponseV4`
        :param iteration: 
        :type iteration: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Iteration`
        :param module: 
        :type module: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Module`
        :param name: 标题
        :type name: str
        :param parent_issue: 
        :type parent_issue: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4ParentIssue`
        :param priority: 
        :type priority: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Priority`
        :param order: 
        :type order: :class:`huaweicloudsdkprojectman.v4.IssueResponseV4Order`
        :param severity: 
        :type severity: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Severity`
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Status`
        :param release_dev: 工作项发布版本号
        :type release_dev: str
        :param find_release_dev: 缺陷发现版本号（仅Bug类型工作项具备该字段）
        :type find_release_dev: str
        :param env: 
        :type env: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV4Env`
        :param tracker: 
        :type tracker: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4Tracker`
        :param updated_time: 更新时间 年-月-日 时:分:秒
        :type updated_time: str
        :param closed_time: 关闭时间 年-月-日 时:分:秒
        :type closed_time: str
        """
        
        

        self._actual_work_hours = None
        self._assigned_cc_user = None
        self._assigned_user = None
        self._begin_time = None
        self._created_time = None
        self._creator = None
        self._custom_fields = None
        self._new_custom_fields = None
        self._developer = None
        self._domain = None
        self._done_ratio = None
        self._end_time = None
        self._expected_work_hours = None
        self._id = None
        self._project = None
        self._iteration = None
        self._module = None
        self._name = None
        self._parent_issue = None
        self._priority = None
        self._order = None
        self._severity = None
        self._status = None
        self._release_dev = None
        self._find_release_dev = None
        self._env = None
        self._tracker = None
        self._updated_time = None
        self._closed_time = None
        self.discriminator = None

        if actual_work_hours is not None:
            self.actual_work_hours = actual_work_hours
        if assigned_cc_user is not None:
            self.assigned_cc_user = assigned_cc_user
        if assigned_user is not None:
            self.assigned_user = assigned_user
        if begin_time is not None:
            self.begin_time = begin_time
        if created_time is not None:
            self.created_time = created_time
        if creator is not None:
            self.creator = creator
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if new_custom_fields is not None:
            self.new_custom_fields = new_custom_fields
        if developer is not None:
            self.developer = developer
        if domain is not None:
            self.domain = domain
        if done_ratio is not None:
            self.done_ratio = done_ratio
        if end_time is not None:
            self.end_time = end_time
        if expected_work_hours is not None:
            self.expected_work_hours = expected_work_hours
        if id is not None:
            self.id = id
        if project is not None:
            self.project = project
        if iteration is not None:
            self.iteration = iteration
        if module is not None:
            self.module = module
        if name is not None:
            self.name = name
        if parent_issue is not None:
            self.parent_issue = parent_issue
        if priority is not None:
            self.priority = priority
        if order is not None:
            self.order = order
        if severity is not None:
            self.severity = severity
        if status is not None:
            self.status = status
        if release_dev is not None:
            self.release_dev = release_dev
        if find_release_dev is not None:
            self.find_release_dev = find_release_dev
        if env is not None:
            self.env = env
        if tracker is not None:
            self.tracker = tracker
        if updated_time is not None:
            self.updated_time = updated_time
        if closed_time is not None:
            self.closed_time = closed_time

    @property
    def actual_work_hours(self):
        r"""Gets the actual_work_hours of this IssueResponseV4.

        实际工时

        :return: The actual_work_hours of this IssueResponseV4.
        :rtype: float
        """
        return self._actual_work_hours

    @actual_work_hours.setter
    def actual_work_hours(self, actual_work_hours):
        r"""Sets the actual_work_hours of this IssueResponseV4.

        实际工时

        :param actual_work_hours: The actual_work_hours of this IssueResponseV4.
        :type actual_work_hours: float
        """
        self._actual_work_hours = actual_work_hours

    @property
    def assigned_cc_user(self):
        r"""Gets the assigned_cc_user of this IssueResponseV4.

        抄送人

        :return: The assigned_cc_user of this IssueResponseV4.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueUser`]
        """
        return self._assigned_cc_user

    @assigned_cc_user.setter
    def assigned_cc_user(self, assigned_cc_user):
        r"""Sets the assigned_cc_user of this IssueResponseV4.

        抄送人

        :param assigned_cc_user: The assigned_cc_user of this IssueResponseV4.
        :type assigned_cc_user: list[:class:`huaweicloudsdkprojectman.v4.IssueUser`]
        """
        self._assigned_cc_user = assigned_cc_user

    @property
    def assigned_user(self):
        r"""Gets the assigned_user of this IssueResponseV4.

        :return: The assigned_user of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        return self._assigned_user

    @assigned_user.setter
    def assigned_user(self, assigned_user):
        r"""Sets the assigned_user of this IssueResponseV4.

        :param assigned_user: The assigned_user of this IssueResponseV4.
        :type assigned_user: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        self._assigned_user = assigned_user

    @property
    def begin_time(self):
        r"""Gets the begin_time of this IssueResponseV4.

        预计开始时间，年-月-日

        :return: The begin_time of this IssueResponseV4.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this IssueResponseV4.

        预计开始时间，年-月-日

        :param begin_time: The begin_time of this IssueResponseV4.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def created_time(self):
        r"""Gets the created_time of this IssueResponseV4.

        创建时间 年-月-日 时:分:秒

        :return: The created_time of this IssueResponseV4.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this IssueResponseV4.

        创建时间 年-月-日 时:分:秒

        :param created_time: The created_time of this IssueResponseV4.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def creator(self):
        r"""Gets the creator of this IssueResponseV4.

        :return: The creator of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this IssueResponseV4.

        :param creator: The creator of this IssueResponseV4.
        :type creator: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        self._creator = creator

    @property
    def custom_fields(self):
        r"""Gets the custom_fields of this IssueResponseV4.

        自定义属性值,不建议使用，建议参考new_custom_fields字段

        :return: The custom_fields of this IssueResponseV4.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CustomField`]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        r"""Sets the custom_fields of this IssueResponseV4.

        自定义属性值,不建议使用，建议参考new_custom_fields字段

        :param custom_fields: The custom_fields of this IssueResponseV4.
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.CustomField`]
        """
        self._custom_fields = custom_fields

    @property
    def new_custom_fields(self):
        r"""Gets the new_custom_fields of this IssueResponseV4.

        自定义属性值

        :return: The new_custom_fields of this IssueResponseV4.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.NewCustomField`]
        """
        return self._new_custom_fields

    @new_custom_fields.setter
    def new_custom_fields(self, new_custom_fields):
        r"""Sets the new_custom_fields of this IssueResponseV4.

        自定义属性值

        :param new_custom_fields: The new_custom_fields of this IssueResponseV4.
        :type new_custom_fields: list[:class:`huaweicloudsdkprojectman.v4.NewCustomField`]
        """
        self._new_custom_fields = new_custom_fields

    @property
    def developer(self):
        r"""Gets the developer of this IssueResponseV4.

        :return: The developer of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        r"""Sets the developer of this IssueResponseV4.

        :param developer: The developer of this IssueResponseV4.
        :type developer: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        self._developer = developer

    @property
    def domain(self):
        r"""Gets the domain of this IssueResponseV4.

        :return: The domain of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Domain`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this IssueResponseV4.

        :param domain: The domain of this IssueResponseV4.
        :type domain: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Domain`
        """
        self._domain = domain

    @property
    def done_ratio(self):
        r"""Gets the done_ratio of this IssueResponseV4.

        工作项进度值

        :return: The done_ratio of this IssueResponseV4.
        :rtype: int
        """
        return self._done_ratio

    @done_ratio.setter
    def done_ratio(self, done_ratio):
        r"""Sets the done_ratio of this IssueResponseV4.

        工作项进度值

        :param done_ratio: The done_ratio of this IssueResponseV4.
        :type done_ratio: int
        """
        self._done_ratio = done_ratio

    @property
    def end_time(self):
        r"""Gets the end_time of this IssueResponseV4.

        预计结束时间，年-月-日

        :return: The end_time of this IssueResponseV4.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this IssueResponseV4.

        预计结束时间，年-月-日

        :param end_time: The end_time of this IssueResponseV4.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def expected_work_hours(self):
        r"""Gets the expected_work_hours of this IssueResponseV4.

        预计工时

        :return: The expected_work_hours of this IssueResponseV4.
        :rtype: float
        """
        return self._expected_work_hours

    @expected_work_hours.setter
    def expected_work_hours(self, expected_work_hours):
        r"""Sets the expected_work_hours of this IssueResponseV4.

        预计工时

        :param expected_work_hours: The expected_work_hours of this IssueResponseV4.
        :type expected_work_hours: float
        """
        self._expected_work_hours = expected_work_hours

    @property
    def id(self):
        r"""Gets the id of this IssueResponseV4.

        工作项项id

        :return: The id of this IssueResponseV4.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueResponseV4.

        工作项项id

        :param id: The id of this IssueResponseV4.
        :type id: int
        """
        self._id = id

    @property
    def project(self):
        r"""Gets the project of this IssueResponseV4.

        :return: The project of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueProjectResponseV4`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this IssueResponseV4.

        :param project: The project of this IssueResponseV4.
        :type project: :class:`huaweicloudsdkprojectman.v4.IssueProjectResponseV4`
        """
        self._project = project

    @property
    def iteration(self):
        r"""Gets the iteration of this IssueResponseV4.

        :return: The iteration of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Iteration`
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        r"""Sets the iteration of this IssueResponseV4.

        :param iteration: The iteration of this IssueResponseV4.
        :type iteration: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Iteration`
        """
        self._iteration = iteration

    @property
    def module(self):
        r"""Gets the module of this IssueResponseV4.

        :return: The module of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Module`
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this IssueResponseV4.

        :param module: The module of this IssueResponseV4.
        :type module: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Module`
        """
        self._module = module

    @property
    def name(self):
        r"""Gets the name of this IssueResponseV4.

        标题

        :return: The name of this IssueResponseV4.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IssueResponseV4.

        标题

        :param name: The name of this IssueResponseV4.
        :type name: str
        """
        self._name = name

    @property
    def parent_issue(self):
        r"""Gets the parent_issue of this IssueResponseV4.

        :return: The parent_issue of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4ParentIssue`
        """
        return self._parent_issue

    @parent_issue.setter
    def parent_issue(self, parent_issue):
        r"""Sets the parent_issue of this IssueResponseV4.

        :param parent_issue: The parent_issue of this IssueResponseV4.
        :type parent_issue: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4ParentIssue`
        """
        self._parent_issue = parent_issue

    @property
    def priority(self):
        r"""Gets the priority of this IssueResponseV4.

        :return: The priority of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Priority`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this IssueResponseV4.

        :param priority: The priority of this IssueResponseV4.
        :type priority: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Priority`
        """
        self._priority = priority

    @property
    def order(self):
        r"""Gets the order of this IssueResponseV4.

        :return: The order of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueResponseV4Order`
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this IssueResponseV4.

        :param order: The order of this IssueResponseV4.
        :type order: :class:`huaweicloudsdkprojectman.v4.IssueResponseV4Order`
        """
        self._order = order

    @property
    def severity(self):
        r"""Gets the severity of this IssueResponseV4.

        :return: The severity of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Severity`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this IssueResponseV4.

        :param severity: The severity of this IssueResponseV4.
        :type severity: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Severity`
        """
        self._severity = severity

    @property
    def status(self):
        r"""Gets the status of this IssueResponseV4.

        :return: The status of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IssueResponseV4.

        :param status: The status of this IssueResponseV4.
        :type status: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Status`
        """
        self._status = status

    @property
    def release_dev(self):
        r"""Gets the release_dev of this IssueResponseV4.

        工作项发布版本号

        :return: The release_dev of this IssueResponseV4.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this IssueResponseV4.

        工作项发布版本号

        :param release_dev: The release_dev of this IssueResponseV4.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def find_release_dev(self):
        r"""Gets the find_release_dev of this IssueResponseV4.

        缺陷发现版本号（仅Bug类型工作项具备该字段）

        :return: The find_release_dev of this IssueResponseV4.
        :rtype: str
        """
        return self._find_release_dev

    @find_release_dev.setter
    def find_release_dev(self, find_release_dev):
        r"""Sets the find_release_dev of this IssueResponseV4.

        缺陷发现版本号（仅Bug类型工作项具备该字段）

        :param find_release_dev: The find_release_dev of this IssueResponseV4.
        :type find_release_dev: str
        """
        self._find_release_dev = find_release_dev

    @property
    def env(self):
        r"""Gets the env of this IssueResponseV4.

        :return: The env of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV4Env`
        """
        return self._env

    @env.setter
    def env(self, env):
        r"""Sets the env of this IssueResponseV4.

        :param env: The env of this IssueResponseV4.
        :type env: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV4Env`
        """
        self._env = env

    @property
    def tracker(self):
        r"""Gets the tracker of this IssueResponseV4.

        :return: The tracker of this IssueResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4Tracker`
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        r"""Sets the tracker of this IssueResponseV4.

        :param tracker: The tracker of this IssueResponseV4.
        :type tracker: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4Tracker`
        """
        self._tracker = tracker

    @property
    def updated_time(self):
        r"""Gets the updated_time of this IssueResponseV4.

        更新时间 年-月-日 时:分:秒

        :return: The updated_time of this IssueResponseV4.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this IssueResponseV4.

        更新时间 年-月-日 时:分:秒

        :param updated_time: The updated_time of this IssueResponseV4.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def closed_time(self):
        r"""Gets the closed_time of this IssueResponseV4.

        关闭时间 年-月-日 时:分:秒

        :return: The closed_time of this IssueResponseV4.
        :rtype: str
        """
        return self._closed_time

    @closed_time.setter
    def closed_time(self, closed_time):
        r"""Sets the closed_time of this IssueResponseV4.

        关闭时间 年-月-日 时:分:秒

        :param closed_time: The closed_time of this IssueResponseV4.
        :type closed_time: str
        """
        self._closed_time = closed_time

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
        if not isinstance(other, IssueResponseV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
