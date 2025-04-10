# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkTableIssuseListResponseBodyIssueList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'subject': 'str',
        'parent_issue_id': 'int',
        'parent_issue': 'WorkTableIssuseListResponseBodyParentIssue',
        'project': 'WorkTableIssuseListResponseBodyProject',
        'release_dev': 'str',
        'find_release_dev': 'str',
        'done_ratio': 'int',
        'expected_work_hours': 'float',
        'actual_work_hours': 'float',
        'tracker': 'WorkTableIssuseListResponseBodyTracker',
        'order': 'WorkTableIssuseListResponseBodyOrder',
        'severity': 'WorkTableIssuseListResponseBodySeverity',
        'priority': 'WorkTableIssuseListResponseBodyPriority',
        'domain': 'WorkTableIssuseListResponseBodyDomain',
        'position': 'float',
        'module': 'WorkTableIssuseListResponseBodyModule',
        'assigned_to': 'SimpleUserIn',
        'author': 'SimpleUserIn',
        'developer': 'SimpleUserIn',
        'closeder': 'SimpleUserIn',
        'status': 'WorkTableIssuseListResponseBodyStatus',
        'deleted': 'bool',
        'is_watcher': 'bool',
        'closed_flag': 'int',
        'created_on': 'str',
        'updated_on': 'str',
        'due_date': 'str'
    }

    attribute_map = {
        'id': 'id',
        'subject': 'subject',
        'parent_issue_id': 'parent_issue_id',
        'parent_issue': 'parent_issue',
        'project': 'project',
        'release_dev': 'release_dev',
        'find_release_dev': 'find_release_dev',
        'done_ratio': 'done_ratio',
        'expected_work_hours': 'expected_work_hours',
        'actual_work_hours': 'actual_work_hours',
        'tracker': 'tracker',
        'order': 'order',
        'severity': 'severity',
        'priority': 'priority',
        'domain': 'domain',
        'position': 'position',
        'module': 'module',
        'assigned_to': 'assigned_to',
        'author': 'author',
        'developer': 'developer',
        'closeder': 'closeder',
        'status': 'status',
        'deleted': 'deleted',
        'is_watcher': 'is_watcher',
        'closed_flag': 'closed_flag',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'due_date': 'due_date'
    }

    def __init__(self, id=None, subject=None, parent_issue_id=None, parent_issue=None, project=None, release_dev=None, find_release_dev=None, done_ratio=None, expected_work_hours=None, actual_work_hours=None, tracker=None, order=None, severity=None, priority=None, domain=None, position=None, module=None, assigned_to=None, author=None, developer=None, closeder=None, status=None, deleted=None, is_watcher=None, closed_flag=None, created_on=None, updated_on=None, due_date=None):
        r"""WorkTableIssuseListResponseBodyIssueList

        The model defined in huaweicloud sdk

        :param id: 工作项id
        :type id: int
        :param subject: 工作项标题
        :type subject: str
        :param parent_issue_id: 父工作项id
        :type parent_issue_id: int
        :param parent_issue: 
        :type parent_issue: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyParentIssue`
        :param project: 
        :type project: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyProject`
        :param release_dev: 发布版本
        :type release_dev: str
        :param find_release_dev: 发现发布版本
        :type find_release_dev: str
        :param done_ratio: 工作项完成度
        :type done_ratio: int
        :param expected_work_hours: 预计工时
        :type expected_work_hours: float
        :param actual_work_hours: 实际工时
        :type actual_work_hours: float
        :param tracker: 
        :type tracker: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyTracker`
        :param order: 
        :type order: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyOrder`
        :param severity: 
        :type severity: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodySeverity`
        :param priority: 
        :type priority: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyPriority`
        :param domain: 
        :type domain: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyDomain`
        :param position: 排序数值
        :type position: float
        :param module: 
        :type module: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyModule`
        :param assigned_to: 
        :type assigned_to: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        :param author: 
        :type author: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        :param developer: 
        :type developer: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        :param closeder: 
        :type closeder: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyStatus`
        :param deleted: 是否删除工作项
        :type deleted: bool
        :param is_watcher: 是否关注工作项
        :type is_watcher: bool
        :param closed_flag: 关闭标志
        :type closed_flag: int
        :param created_on: 工作项新建时间戳
        :type created_on: str
        :param updated_on: 工作项更新时间戳
        :type updated_on: str
        :param due_date: 工作项预计结束时间戳
        :type due_date: str
        """
        
        

        self._id = None
        self._subject = None
        self._parent_issue_id = None
        self._parent_issue = None
        self._project = None
        self._release_dev = None
        self._find_release_dev = None
        self._done_ratio = None
        self._expected_work_hours = None
        self._actual_work_hours = None
        self._tracker = None
        self._order = None
        self._severity = None
        self._priority = None
        self._domain = None
        self._position = None
        self._module = None
        self._assigned_to = None
        self._author = None
        self._developer = None
        self._closeder = None
        self._status = None
        self._deleted = None
        self._is_watcher = None
        self._closed_flag = None
        self._created_on = None
        self._updated_on = None
        self._due_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if subject is not None:
            self.subject = subject
        if parent_issue_id is not None:
            self.parent_issue_id = parent_issue_id
        if parent_issue is not None:
            self.parent_issue = parent_issue
        if project is not None:
            self.project = project
        if release_dev is not None:
            self.release_dev = release_dev
        if find_release_dev is not None:
            self.find_release_dev = find_release_dev
        if done_ratio is not None:
            self.done_ratio = done_ratio
        if expected_work_hours is not None:
            self.expected_work_hours = expected_work_hours
        if actual_work_hours is not None:
            self.actual_work_hours = actual_work_hours
        if tracker is not None:
            self.tracker = tracker
        if order is not None:
            self.order = order
        if severity is not None:
            self.severity = severity
        if priority is not None:
            self.priority = priority
        if domain is not None:
            self.domain = domain
        if position is not None:
            self.position = position
        if module is not None:
            self.module = module
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if author is not None:
            self.author = author
        if developer is not None:
            self.developer = developer
        if closeder is not None:
            self.closeder = closeder
        if status is not None:
            self.status = status
        if deleted is not None:
            self.deleted = deleted
        if is_watcher is not None:
            self.is_watcher = is_watcher
        if closed_flag is not None:
            self.closed_flag = closed_flag
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if due_date is not None:
            self.due_date = due_date

    @property
    def id(self):
        r"""Gets the id of this WorkTableIssuseListResponseBodyIssueList.

        工作项id

        :return: The id of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkTableIssuseListResponseBodyIssueList.

        工作项id

        :param id: The id of this WorkTableIssuseListResponseBodyIssueList.
        :type id: int
        """
        self._id = id

    @property
    def subject(self):
        r"""Gets the subject of this WorkTableIssuseListResponseBodyIssueList.

        工作项标题

        :return: The subject of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this WorkTableIssuseListResponseBodyIssueList.

        工作项标题

        :param subject: The subject of this WorkTableIssuseListResponseBodyIssueList.
        :type subject: str
        """
        self._subject = subject

    @property
    def parent_issue_id(self):
        r"""Gets the parent_issue_id of this WorkTableIssuseListResponseBodyIssueList.

        父工作项id

        :return: The parent_issue_id of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: int
        """
        return self._parent_issue_id

    @parent_issue_id.setter
    def parent_issue_id(self, parent_issue_id):
        r"""Sets the parent_issue_id of this WorkTableIssuseListResponseBodyIssueList.

        父工作项id

        :param parent_issue_id: The parent_issue_id of this WorkTableIssuseListResponseBodyIssueList.
        :type parent_issue_id: int
        """
        self._parent_issue_id = parent_issue_id

    @property
    def parent_issue(self):
        r"""Gets the parent_issue of this WorkTableIssuseListResponseBodyIssueList.

        :return: The parent_issue of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyParentIssue`
        """
        return self._parent_issue

    @parent_issue.setter
    def parent_issue(self, parent_issue):
        r"""Sets the parent_issue of this WorkTableIssuseListResponseBodyIssueList.

        :param parent_issue: The parent_issue of this WorkTableIssuseListResponseBodyIssueList.
        :type parent_issue: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyParentIssue`
        """
        self._parent_issue = parent_issue

    @property
    def project(self):
        r"""Gets the project of this WorkTableIssuseListResponseBodyIssueList.

        :return: The project of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyProject`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this WorkTableIssuseListResponseBodyIssueList.

        :param project: The project of this WorkTableIssuseListResponseBodyIssueList.
        :type project: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyProject`
        """
        self._project = project

    @property
    def release_dev(self):
        r"""Gets the release_dev of this WorkTableIssuseListResponseBodyIssueList.

        发布版本

        :return: The release_dev of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this WorkTableIssuseListResponseBodyIssueList.

        发布版本

        :param release_dev: The release_dev of this WorkTableIssuseListResponseBodyIssueList.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def find_release_dev(self):
        r"""Gets the find_release_dev of this WorkTableIssuseListResponseBodyIssueList.

        发现发布版本

        :return: The find_release_dev of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: str
        """
        return self._find_release_dev

    @find_release_dev.setter
    def find_release_dev(self, find_release_dev):
        r"""Sets the find_release_dev of this WorkTableIssuseListResponseBodyIssueList.

        发现发布版本

        :param find_release_dev: The find_release_dev of this WorkTableIssuseListResponseBodyIssueList.
        :type find_release_dev: str
        """
        self._find_release_dev = find_release_dev

    @property
    def done_ratio(self):
        r"""Gets the done_ratio of this WorkTableIssuseListResponseBodyIssueList.

        工作项完成度

        :return: The done_ratio of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: int
        """
        return self._done_ratio

    @done_ratio.setter
    def done_ratio(self, done_ratio):
        r"""Sets the done_ratio of this WorkTableIssuseListResponseBodyIssueList.

        工作项完成度

        :param done_ratio: The done_ratio of this WorkTableIssuseListResponseBodyIssueList.
        :type done_ratio: int
        """
        self._done_ratio = done_ratio

    @property
    def expected_work_hours(self):
        r"""Gets the expected_work_hours of this WorkTableIssuseListResponseBodyIssueList.

        预计工时

        :return: The expected_work_hours of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: float
        """
        return self._expected_work_hours

    @expected_work_hours.setter
    def expected_work_hours(self, expected_work_hours):
        r"""Sets the expected_work_hours of this WorkTableIssuseListResponseBodyIssueList.

        预计工时

        :param expected_work_hours: The expected_work_hours of this WorkTableIssuseListResponseBodyIssueList.
        :type expected_work_hours: float
        """
        self._expected_work_hours = expected_work_hours

    @property
    def actual_work_hours(self):
        r"""Gets the actual_work_hours of this WorkTableIssuseListResponseBodyIssueList.

        实际工时

        :return: The actual_work_hours of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: float
        """
        return self._actual_work_hours

    @actual_work_hours.setter
    def actual_work_hours(self, actual_work_hours):
        r"""Sets the actual_work_hours of this WorkTableIssuseListResponseBodyIssueList.

        实际工时

        :param actual_work_hours: The actual_work_hours of this WorkTableIssuseListResponseBodyIssueList.
        :type actual_work_hours: float
        """
        self._actual_work_hours = actual_work_hours

    @property
    def tracker(self):
        r"""Gets the tracker of this WorkTableIssuseListResponseBodyIssueList.

        :return: The tracker of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyTracker`
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        r"""Sets the tracker of this WorkTableIssuseListResponseBodyIssueList.

        :param tracker: The tracker of this WorkTableIssuseListResponseBodyIssueList.
        :type tracker: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyTracker`
        """
        self._tracker = tracker

    @property
    def order(self):
        r"""Gets the order of this WorkTableIssuseListResponseBodyIssueList.

        :return: The order of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyOrder`
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this WorkTableIssuseListResponseBodyIssueList.

        :param order: The order of this WorkTableIssuseListResponseBodyIssueList.
        :type order: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyOrder`
        """
        self._order = order

    @property
    def severity(self):
        r"""Gets the severity of this WorkTableIssuseListResponseBodyIssueList.

        :return: The severity of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodySeverity`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this WorkTableIssuseListResponseBodyIssueList.

        :param severity: The severity of this WorkTableIssuseListResponseBodyIssueList.
        :type severity: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodySeverity`
        """
        self._severity = severity

    @property
    def priority(self):
        r"""Gets the priority of this WorkTableIssuseListResponseBodyIssueList.

        :return: The priority of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyPriority`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this WorkTableIssuseListResponseBodyIssueList.

        :param priority: The priority of this WorkTableIssuseListResponseBodyIssueList.
        :type priority: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyPriority`
        """
        self._priority = priority

    @property
    def domain(self):
        r"""Gets the domain of this WorkTableIssuseListResponseBodyIssueList.

        :return: The domain of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyDomain`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this WorkTableIssuseListResponseBodyIssueList.

        :param domain: The domain of this WorkTableIssuseListResponseBodyIssueList.
        :type domain: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyDomain`
        """
        self._domain = domain

    @property
    def position(self):
        r"""Gets the position of this WorkTableIssuseListResponseBodyIssueList.

        排序数值

        :return: The position of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this WorkTableIssuseListResponseBodyIssueList.

        排序数值

        :param position: The position of this WorkTableIssuseListResponseBodyIssueList.
        :type position: float
        """
        self._position = position

    @property
    def module(self):
        r"""Gets the module of this WorkTableIssuseListResponseBodyIssueList.

        :return: The module of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyModule`
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this WorkTableIssuseListResponseBodyIssueList.

        :param module: The module of this WorkTableIssuseListResponseBodyIssueList.
        :type module: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyModule`
        """
        self._module = module

    @property
    def assigned_to(self):
        r"""Gets the assigned_to of this WorkTableIssuseListResponseBodyIssueList.

        :return: The assigned_to of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        r"""Sets the assigned_to of this WorkTableIssuseListResponseBodyIssueList.

        :param assigned_to: The assigned_to of this WorkTableIssuseListResponseBodyIssueList.
        :type assigned_to: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        """
        self._assigned_to = assigned_to

    @property
    def author(self):
        r"""Gets the author of this WorkTableIssuseListResponseBodyIssueList.

        :return: The author of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this WorkTableIssuseListResponseBodyIssueList.

        :param author: The author of this WorkTableIssuseListResponseBodyIssueList.
        :type author: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        """
        self._author = author

    @property
    def developer(self):
        r"""Gets the developer of this WorkTableIssuseListResponseBodyIssueList.

        :return: The developer of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        r"""Sets the developer of this WorkTableIssuseListResponseBodyIssueList.

        :param developer: The developer of this WorkTableIssuseListResponseBodyIssueList.
        :type developer: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        """
        self._developer = developer

    @property
    def closeder(self):
        r"""Gets the closeder of this WorkTableIssuseListResponseBodyIssueList.

        :return: The closeder of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        """
        return self._closeder

    @closeder.setter
    def closeder(self, closeder):
        r"""Sets the closeder of this WorkTableIssuseListResponseBodyIssueList.

        :param closeder: The closeder of this WorkTableIssuseListResponseBodyIssueList.
        :type closeder: :class:`huaweicloudsdkprojectman.v4.SimpleUserIn`
        """
        self._closeder = closeder

    @property
    def status(self):
        r"""Gets the status of this WorkTableIssuseListResponseBodyIssueList.

        :return: The status of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WorkTableIssuseListResponseBodyIssueList.

        :param status: The status of this WorkTableIssuseListResponseBodyIssueList.
        :type status: :class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyStatus`
        """
        self._status = status

    @property
    def deleted(self):
        r"""Gets the deleted of this WorkTableIssuseListResponseBodyIssueList.

        是否删除工作项

        :return: The deleted of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this WorkTableIssuseListResponseBodyIssueList.

        是否删除工作项

        :param deleted: The deleted of this WorkTableIssuseListResponseBodyIssueList.
        :type deleted: bool
        """
        self._deleted = deleted

    @property
    def is_watcher(self):
        r"""Gets the is_watcher of this WorkTableIssuseListResponseBodyIssueList.

        是否关注工作项

        :return: The is_watcher of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: bool
        """
        return self._is_watcher

    @is_watcher.setter
    def is_watcher(self, is_watcher):
        r"""Sets the is_watcher of this WorkTableIssuseListResponseBodyIssueList.

        是否关注工作项

        :param is_watcher: The is_watcher of this WorkTableIssuseListResponseBodyIssueList.
        :type is_watcher: bool
        """
        self._is_watcher = is_watcher

    @property
    def closed_flag(self):
        r"""Gets the closed_flag of this WorkTableIssuseListResponseBodyIssueList.

        关闭标志

        :return: The closed_flag of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: int
        """
        return self._closed_flag

    @closed_flag.setter
    def closed_flag(self, closed_flag):
        r"""Sets the closed_flag of this WorkTableIssuseListResponseBodyIssueList.

        关闭标志

        :param closed_flag: The closed_flag of this WorkTableIssuseListResponseBodyIssueList.
        :type closed_flag: int
        """
        self._closed_flag = closed_flag

    @property
    def created_on(self):
        r"""Gets the created_on of this WorkTableIssuseListResponseBodyIssueList.

        工作项新建时间戳

        :return: The created_on of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        r"""Sets the created_on of this WorkTableIssuseListResponseBodyIssueList.

        工作项新建时间戳

        :param created_on: The created_on of this WorkTableIssuseListResponseBodyIssueList.
        :type created_on: str
        """
        self._created_on = created_on

    @property
    def updated_on(self):
        r"""Gets the updated_on of this WorkTableIssuseListResponseBodyIssueList.

        工作项更新时间戳

        :return: The updated_on of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: str
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        r"""Sets the updated_on of this WorkTableIssuseListResponseBodyIssueList.

        工作项更新时间戳

        :param updated_on: The updated_on of this WorkTableIssuseListResponseBodyIssueList.
        :type updated_on: str
        """
        self._updated_on = updated_on

    @property
    def due_date(self):
        r"""Gets the due_date of this WorkTableIssuseListResponseBodyIssueList.

        工作项预计结束时间戳

        :return: The due_date of this WorkTableIssuseListResponseBodyIssueList.
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        r"""Sets the due_date of this WorkTableIssuseListResponseBodyIssueList.

        工作项预计结束时间戳

        :param due_date: The due_date of this WorkTableIssuseListResponseBodyIssueList.
        :type due_date: str
        """
        self._due_date = due_date

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
        if not isinstance(other, WorkTableIssuseListResponseBodyIssueList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
