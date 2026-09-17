# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueNew:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'updated_on': 'str',
        'story_point': 'StoryPoint',
        'subject': 'str',
        'project': 'Project',
        'is_parent': 'bool',
        'done_ratio': 'int',
        'find_release_dev': 'str',
        'tracker': 'Tracker',
        'id': 'int',
        'start_date': 'str',
        'assigned_to': 'IssueNewAssignedTo',
        'status_attribute': 'StatusAttributeVO',
        'severity': 'Severity',
        'release_dev': 'str',
        'author': 'IssueNewAuthor',
        'module': 'object',
        'due_date': 'str',
        'expected_work_hours': 'int',
        'priority': 'Priority',
        'actual_work_hours': 'int',
        'is_watcher': 'bool',
        'deleted': 'bool',
        'fixed_version': 'object',
        'is_archived': 'bool',
        'created_on': 'str',
        'domain': 'object',
        'developer': 'object',
        'closeder': 'object',
        'position': 'str',
        'closed_flag': 'int',
        'assigned_cc_user': 'str',
        'custom_value_new': 'object',
        'status': 'Status'
    }

    attribute_map = {
        'updated_on': 'updated_on',
        'story_point': 'story_point',
        'subject': 'subject',
        'project': 'project',
        'is_parent': 'isParent',
        'done_ratio': 'done_ratio',
        'find_release_dev': 'findReleaseDev',
        'tracker': 'tracker',
        'id': 'id',
        'start_date': 'start_date',
        'assigned_to': 'assigned_to',
        'status_attribute': 'status_attribute',
        'severity': 'severity',
        'release_dev': 'releaseDev',
        'author': 'author',
        'module': 'module',
        'due_date': 'due_date',
        'expected_work_hours': 'expected_work_hours',
        'priority': 'priority',
        'actual_work_hours': 'actual_work_hours',
        'is_watcher': 'is_watcher',
        'deleted': 'deleted',
        'fixed_version': 'fixed_version',
        'is_archived': 'is_archived',
        'created_on': 'created_on',
        'domain': 'domain',
        'developer': 'developer',
        'closeder': 'closeder',
        'position': 'position',
        'closed_flag': 'closed_flag',
        'assigned_cc_user': 'assigned_cc_user',
        'custom_value_new': 'custom_value_new',
        'status': 'status'
    }

    def __init__(self, updated_on=None, story_point=None, subject=None, project=None, is_parent=None, done_ratio=None, find_release_dev=None, tracker=None, id=None, start_date=None, assigned_to=None, status_attribute=None, severity=None, release_dev=None, author=None, module=None, due_date=None, expected_work_hours=None, priority=None, actual_work_hours=None, is_watcher=None, deleted=None, fixed_version=None, is_archived=None, created_on=None, domain=None, developer=None, closeder=None, position=None, closed_flag=None, assigned_cc_user=None, custom_value_new=None, status=None):
        r"""IssueNew

        The model defined in huaweicloud sdk

        :param updated_on: **参数解释：** 工作项的更新日期。时间戳格式（示例：1839340800000） 。 **取值范围：** 不涉及。
        :type updated_on: str
        :param story_point: 
        :type story_point: :class:`huaweicloudsdkprojectman.v4.StoryPoint`
        :param subject: **参数解释：** 工作项的负责者。 **取值范围：** 不涉及。
        :type subject: str
        :param project: 
        :type project: :class:`huaweicloudsdkprojectman.v4.Project`
        :param is_parent: **参数解释：** 是否有子工作项。 **取值范围：** true（有子工作项） false（没有子工作项）
        :type is_parent: bool
        :param done_ratio: **参数解释：** 工作项完成度。 **取值范围：** 不涉及。
        :type done_ratio: int
        :param find_release_dev: **参数解释：** 发布人 。 **取值范围：** 不涉及。
        :type find_release_dev: str
        :param tracker: 
        :type tracker: :class:`huaweicloudsdkprojectman.v4.Tracker`
        :param id: **参数解释：** 工作项列表id。 **取值范围：** 不涉及。
        :type id: int
        :param start_date: **参数解释：** 工作项的开始日期。时间戳格式（示例：1839340800000）。 **取值范围：** 不涉及。
        :type start_date: str
        :param assigned_to: 
        :type assigned_to: :class:`huaweicloudsdkprojectman.v4.IssueNewAssignedTo`
        :param status_attribute: 
        :type status_attribute: :class:`huaweicloudsdkprojectman.v4.StatusAttributeVO`
        :param severity: 
        :type severity: :class:`huaweicloudsdkprojectman.v4.Severity`
        :param release_dev: **参数解释：** 工作项发布版本号。 **取值范围：** 不涉及。
        :type release_dev: str
        :param author: 
        :type author: :class:`huaweicloudsdkprojectman.v4.IssueNewAuthor`
        :param module: **参数解释：** 工作项的模块。 **取值范围：** 不涉及。
        :type module: object
        :param due_date: **参数解释：** 工作项的截止日期，时间戳格式（示例：1839340800000）。 **取值范围：** 不涉及。
        :type due_date: str
        :param expected_work_hours: **参数解释：** 工作项的预计工时(单位：人时)。 **取值范围：** 不涉及。
        :type expected_work_hours: int
        :param priority: 
        :type priority: :class:`huaweicloudsdkprojectman.v4.Priority`
        :param actual_work_hours: **参数解释：** 工作项的实际工时（单位：人/时）。 **取值范围：** 不涉及。
        :type actual_work_hours: int
        :param is_watcher: **参数解释：** 是否关注 。 **取值范围：** true（是） false（不是）
        :type is_watcher: bool
        :param deleted: **参数解释：** 是否删除 。 **取值范围：** true（是） false（不是）
        :type deleted: bool
        :param fixed_version: **参数解释：** 问题解决版本。 **取值范围：** 不涉及。
        :type fixed_version: object
        :param is_archived: **参数解释：** 是否归档。 **取值范围：** true（是） false（不是）
        :type is_archived: bool
        :param created_on: **参数解释：** 工作项的创建时间，时间戳格式（示例：1839340800000）。 **取值范围：** 不涉及。
        :type created_on: str
        :param domain: **参数解释：** 工作项的领域 。 **取值范围：** 不涉及。
        :type domain: object
        :param developer: **参数解释：** 工作项的开发人员。 **取值范围：** 不涉及。
        :type developer: object
        :param closeder: **参数解释：** 关闭人员。 **取值范围：** 不涉及。
        :type closeder: object
        :param position: **参数解释：** 工作项在列表的展示位置 。 **取值范围：** 不涉及。
        :type position: str
        :param closed_flag: **参数解释：** 关闭标志 。 **取值范围：** 0（打开） 1（关闭）
        :type closed_flag: int
        :param assigned_cc_user: **参数解释：** 工作项的抄送人。 **取值范围：** 不涉及。
        :type assigned_cc_user: str
        :param custom_value_new: **参数解释：** 自定义字段。 **取值范围：** 不涉及。
        :type custom_value_new: object
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.Status`
        """
        
        

        self._updated_on = None
        self._story_point = None
        self._subject = None
        self._project = None
        self._is_parent = None
        self._done_ratio = None
        self._find_release_dev = None
        self._tracker = None
        self._id = None
        self._start_date = None
        self._assigned_to = None
        self._status_attribute = None
        self._severity = None
        self._release_dev = None
        self._author = None
        self._module = None
        self._due_date = None
        self._expected_work_hours = None
        self._priority = None
        self._actual_work_hours = None
        self._is_watcher = None
        self._deleted = None
        self._fixed_version = None
        self._is_archived = None
        self._created_on = None
        self._domain = None
        self._developer = None
        self._closeder = None
        self._position = None
        self._closed_flag = None
        self._assigned_cc_user = None
        self._custom_value_new = None
        self._status = None
        self.discriminator = None

        if updated_on is not None:
            self.updated_on = updated_on
        if story_point is not None:
            self.story_point = story_point
        if subject is not None:
            self.subject = subject
        if project is not None:
            self.project = project
        if is_parent is not None:
            self.is_parent = is_parent
        if done_ratio is not None:
            self.done_ratio = done_ratio
        if find_release_dev is not None:
            self.find_release_dev = find_release_dev
        if tracker is not None:
            self.tracker = tracker
        if id is not None:
            self.id = id
        if start_date is not None:
            self.start_date = start_date
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if status_attribute is not None:
            self.status_attribute = status_attribute
        if severity is not None:
            self.severity = severity
        if release_dev is not None:
            self.release_dev = release_dev
        if author is not None:
            self.author = author
        if module is not None:
            self.module = module
        if due_date is not None:
            self.due_date = due_date
        if expected_work_hours is not None:
            self.expected_work_hours = expected_work_hours
        if priority is not None:
            self.priority = priority
        if actual_work_hours is not None:
            self.actual_work_hours = actual_work_hours
        if is_watcher is not None:
            self.is_watcher = is_watcher
        if deleted is not None:
            self.deleted = deleted
        if fixed_version is not None:
            self.fixed_version = fixed_version
        if is_archived is not None:
            self.is_archived = is_archived
        if created_on is not None:
            self.created_on = created_on
        if domain is not None:
            self.domain = domain
        if developer is not None:
            self.developer = developer
        if closeder is not None:
            self.closeder = closeder
        if position is not None:
            self.position = position
        if closed_flag is not None:
            self.closed_flag = closed_flag
        if assigned_cc_user is not None:
            self.assigned_cc_user = assigned_cc_user
        if custom_value_new is not None:
            self.custom_value_new = custom_value_new
        if status is not None:
            self.status = status

    @property
    def updated_on(self):
        r"""Gets the updated_on of this IssueNew.

        **参数解释：** 工作项的更新日期。时间戳格式（示例：1839340800000） 。 **取值范围：** 不涉及。

        :return: The updated_on of this IssueNew.
        :rtype: str
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        r"""Sets the updated_on of this IssueNew.

        **参数解释：** 工作项的更新日期。时间戳格式（示例：1839340800000） 。 **取值范围：** 不涉及。

        :param updated_on: The updated_on of this IssueNew.
        :type updated_on: str
        """
        self._updated_on = updated_on

    @property
    def story_point(self):
        r"""Gets the story_point of this IssueNew.

        :return: The story_point of this IssueNew.
        :rtype: :class:`huaweicloudsdkprojectman.v4.StoryPoint`
        """
        return self._story_point

    @story_point.setter
    def story_point(self, story_point):
        r"""Sets the story_point of this IssueNew.

        :param story_point: The story_point of this IssueNew.
        :type story_point: :class:`huaweicloudsdkprojectman.v4.StoryPoint`
        """
        self._story_point = story_point

    @property
    def subject(self):
        r"""Gets the subject of this IssueNew.

        **参数解释：** 工作项的负责者。 **取值范围：** 不涉及。

        :return: The subject of this IssueNew.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this IssueNew.

        **参数解释：** 工作项的负责者。 **取值范围：** 不涉及。

        :param subject: The subject of this IssueNew.
        :type subject: str
        """
        self._subject = subject

    @property
    def project(self):
        r"""Gets the project of this IssueNew.

        :return: The project of this IssueNew.
        :rtype: :class:`huaweicloudsdkprojectman.v4.Project`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this IssueNew.

        :param project: The project of this IssueNew.
        :type project: :class:`huaweicloudsdkprojectman.v4.Project`
        """
        self._project = project

    @property
    def is_parent(self):
        r"""Gets the is_parent of this IssueNew.

        **参数解释：** 是否有子工作项。 **取值范围：** true（有子工作项） false（没有子工作项）

        :return: The is_parent of this IssueNew.
        :rtype: bool
        """
        return self._is_parent

    @is_parent.setter
    def is_parent(self, is_parent):
        r"""Sets the is_parent of this IssueNew.

        **参数解释：** 是否有子工作项。 **取值范围：** true（有子工作项） false（没有子工作项）

        :param is_parent: The is_parent of this IssueNew.
        :type is_parent: bool
        """
        self._is_parent = is_parent

    @property
    def done_ratio(self):
        r"""Gets the done_ratio of this IssueNew.

        **参数解释：** 工作项完成度。 **取值范围：** 不涉及。

        :return: The done_ratio of this IssueNew.
        :rtype: int
        """
        return self._done_ratio

    @done_ratio.setter
    def done_ratio(self, done_ratio):
        r"""Sets the done_ratio of this IssueNew.

        **参数解释：** 工作项完成度。 **取值范围：** 不涉及。

        :param done_ratio: The done_ratio of this IssueNew.
        :type done_ratio: int
        """
        self._done_ratio = done_ratio

    @property
    def find_release_dev(self):
        r"""Gets the find_release_dev of this IssueNew.

        **参数解释：** 发布人 。 **取值范围：** 不涉及。

        :return: The find_release_dev of this IssueNew.
        :rtype: str
        """
        return self._find_release_dev

    @find_release_dev.setter
    def find_release_dev(self, find_release_dev):
        r"""Sets the find_release_dev of this IssueNew.

        **参数解释：** 发布人 。 **取值范围：** 不涉及。

        :param find_release_dev: The find_release_dev of this IssueNew.
        :type find_release_dev: str
        """
        self._find_release_dev = find_release_dev

    @property
    def tracker(self):
        r"""Gets the tracker of this IssueNew.

        :return: The tracker of this IssueNew.
        :rtype: :class:`huaweicloudsdkprojectman.v4.Tracker`
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        r"""Sets the tracker of this IssueNew.

        :param tracker: The tracker of this IssueNew.
        :type tracker: :class:`huaweicloudsdkprojectman.v4.Tracker`
        """
        self._tracker = tracker

    @property
    def id(self):
        r"""Gets the id of this IssueNew.

        **参数解释：** 工作项列表id。 **取值范围：** 不涉及。

        :return: The id of this IssueNew.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueNew.

        **参数解释：** 工作项列表id。 **取值范围：** 不涉及。

        :param id: The id of this IssueNew.
        :type id: int
        """
        self._id = id

    @property
    def start_date(self):
        r"""Gets the start_date of this IssueNew.

        **参数解释：** 工作项的开始日期。时间戳格式（示例：1839340800000）。 **取值范围：** 不涉及。

        :return: The start_date of this IssueNew.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this IssueNew.

        **参数解释：** 工作项的开始日期。时间戳格式（示例：1839340800000）。 **取值范围：** 不涉及。

        :param start_date: The start_date of this IssueNew.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def assigned_to(self):
        r"""Gets the assigned_to of this IssueNew.

        :return: The assigned_to of this IssueNew.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueNewAssignedTo`
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        r"""Sets the assigned_to of this IssueNew.

        :param assigned_to: The assigned_to of this IssueNew.
        :type assigned_to: :class:`huaweicloudsdkprojectman.v4.IssueNewAssignedTo`
        """
        self._assigned_to = assigned_to

    @property
    def status_attribute(self):
        r"""Gets the status_attribute of this IssueNew.

        :return: The status_attribute of this IssueNew.
        :rtype: :class:`huaweicloudsdkprojectman.v4.StatusAttributeVO`
        """
        return self._status_attribute

    @status_attribute.setter
    def status_attribute(self, status_attribute):
        r"""Sets the status_attribute of this IssueNew.

        :param status_attribute: The status_attribute of this IssueNew.
        :type status_attribute: :class:`huaweicloudsdkprojectman.v4.StatusAttributeVO`
        """
        self._status_attribute = status_attribute

    @property
    def severity(self):
        r"""Gets the severity of this IssueNew.

        :return: The severity of this IssueNew.
        :rtype: :class:`huaweicloudsdkprojectman.v4.Severity`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this IssueNew.

        :param severity: The severity of this IssueNew.
        :type severity: :class:`huaweicloudsdkprojectman.v4.Severity`
        """
        self._severity = severity

    @property
    def release_dev(self):
        r"""Gets the release_dev of this IssueNew.

        **参数解释：** 工作项发布版本号。 **取值范围：** 不涉及。

        :return: The release_dev of this IssueNew.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this IssueNew.

        **参数解释：** 工作项发布版本号。 **取值范围：** 不涉及。

        :param release_dev: The release_dev of this IssueNew.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def author(self):
        r"""Gets the author of this IssueNew.

        :return: The author of this IssueNew.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueNewAuthor`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this IssueNew.

        :param author: The author of this IssueNew.
        :type author: :class:`huaweicloudsdkprojectman.v4.IssueNewAuthor`
        """
        self._author = author

    @property
    def module(self):
        r"""Gets the module of this IssueNew.

        **参数解释：** 工作项的模块。 **取值范围：** 不涉及。

        :return: The module of this IssueNew.
        :rtype: object
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this IssueNew.

        **参数解释：** 工作项的模块。 **取值范围：** 不涉及。

        :param module: The module of this IssueNew.
        :type module: object
        """
        self._module = module

    @property
    def due_date(self):
        r"""Gets the due_date of this IssueNew.

        **参数解释：** 工作项的截止日期，时间戳格式（示例：1839340800000）。 **取值范围：** 不涉及。

        :return: The due_date of this IssueNew.
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        r"""Sets the due_date of this IssueNew.

        **参数解释：** 工作项的截止日期，时间戳格式（示例：1839340800000）。 **取值范围：** 不涉及。

        :param due_date: The due_date of this IssueNew.
        :type due_date: str
        """
        self._due_date = due_date

    @property
    def expected_work_hours(self):
        r"""Gets the expected_work_hours of this IssueNew.

        **参数解释：** 工作项的预计工时(单位：人时)。 **取值范围：** 不涉及。

        :return: The expected_work_hours of this IssueNew.
        :rtype: int
        """
        return self._expected_work_hours

    @expected_work_hours.setter
    def expected_work_hours(self, expected_work_hours):
        r"""Sets the expected_work_hours of this IssueNew.

        **参数解释：** 工作项的预计工时(单位：人时)。 **取值范围：** 不涉及。

        :param expected_work_hours: The expected_work_hours of this IssueNew.
        :type expected_work_hours: int
        """
        self._expected_work_hours = expected_work_hours

    @property
    def priority(self):
        r"""Gets the priority of this IssueNew.

        :return: The priority of this IssueNew.
        :rtype: :class:`huaweicloudsdkprojectman.v4.Priority`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this IssueNew.

        :param priority: The priority of this IssueNew.
        :type priority: :class:`huaweicloudsdkprojectman.v4.Priority`
        """
        self._priority = priority

    @property
    def actual_work_hours(self):
        r"""Gets the actual_work_hours of this IssueNew.

        **参数解释：** 工作项的实际工时（单位：人/时）。 **取值范围：** 不涉及。

        :return: The actual_work_hours of this IssueNew.
        :rtype: int
        """
        return self._actual_work_hours

    @actual_work_hours.setter
    def actual_work_hours(self, actual_work_hours):
        r"""Sets the actual_work_hours of this IssueNew.

        **参数解释：** 工作项的实际工时（单位：人/时）。 **取值范围：** 不涉及。

        :param actual_work_hours: The actual_work_hours of this IssueNew.
        :type actual_work_hours: int
        """
        self._actual_work_hours = actual_work_hours

    @property
    def is_watcher(self):
        r"""Gets the is_watcher of this IssueNew.

        **参数解释：** 是否关注 。 **取值范围：** true（是） false（不是）

        :return: The is_watcher of this IssueNew.
        :rtype: bool
        """
        return self._is_watcher

    @is_watcher.setter
    def is_watcher(self, is_watcher):
        r"""Sets the is_watcher of this IssueNew.

        **参数解释：** 是否关注 。 **取值范围：** true（是） false（不是）

        :param is_watcher: The is_watcher of this IssueNew.
        :type is_watcher: bool
        """
        self._is_watcher = is_watcher

    @property
    def deleted(self):
        r"""Gets the deleted of this IssueNew.

        **参数解释：** 是否删除 。 **取值范围：** true（是） false（不是）

        :return: The deleted of this IssueNew.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this IssueNew.

        **参数解释：** 是否删除 。 **取值范围：** true（是） false（不是）

        :param deleted: The deleted of this IssueNew.
        :type deleted: bool
        """
        self._deleted = deleted

    @property
    def fixed_version(self):
        r"""Gets the fixed_version of this IssueNew.

        **参数解释：** 问题解决版本。 **取值范围：** 不涉及。

        :return: The fixed_version of this IssueNew.
        :rtype: object
        """
        return self._fixed_version

    @fixed_version.setter
    def fixed_version(self, fixed_version):
        r"""Sets the fixed_version of this IssueNew.

        **参数解释：** 问题解决版本。 **取值范围：** 不涉及。

        :param fixed_version: The fixed_version of this IssueNew.
        :type fixed_version: object
        """
        self._fixed_version = fixed_version

    @property
    def is_archived(self):
        r"""Gets the is_archived of this IssueNew.

        **参数解释：** 是否归档。 **取值范围：** true（是） false（不是）

        :return: The is_archived of this IssueNew.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        r"""Sets the is_archived of this IssueNew.

        **参数解释：** 是否归档。 **取值范围：** true（是） false（不是）

        :param is_archived: The is_archived of this IssueNew.
        :type is_archived: bool
        """
        self._is_archived = is_archived

    @property
    def created_on(self):
        r"""Gets the created_on of this IssueNew.

        **参数解释：** 工作项的创建时间，时间戳格式（示例：1839340800000）。 **取值范围：** 不涉及。

        :return: The created_on of this IssueNew.
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        r"""Sets the created_on of this IssueNew.

        **参数解释：** 工作项的创建时间，时间戳格式（示例：1839340800000）。 **取值范围：** 不涉及。

        :param created_on: The created_on of this IssueNew.
        :type created_on: str
        """
        self._created_on = created_on

    @property
    def domain(self):
        r"""Gets the domain of this IssueNew.

        **参数解释：** 工作项的领域 。 **取值范围：** 不涉及。

        :return: The domain of this IssueNew.
        :rtype: object
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this IssueNew.

        **参数解释：** 工作项的领域 。 **取值范围：** 不涉及。

        :param domain: The domain of this IssueNew.
        :type domain: object
        """
        self._domain = domain

    @property
    def developer(self):
        r"""Gets the developer of this IssueNew.

        **参数解释：** 工作项的开发人员。 **取值范围：** 不涉及。

        :return: The developer of this IssueNew.
        :rtype: object
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        r"""Sets the developer of this IssueNew.

        **参数解释：** 工作项的开发人员。 **取值范围：** 不涉及。

        :param developer: The developer of this IssueNew.
        :type developer: object
        """
        self._developer = developer

    @property
    def closeder(self):
        r"""Gets the closeder of this IssueNew.

        **参数解释：** 关闭人员。 **取值范围：** 不涉及。

        :return: The closeder of this IssueNew.
        :rtype: object
        """
        return self._closeder

    @closeder.setter
    def closeder(self, closeder):
        r"""Sets the closeder of this IssueNew.

        **参数解释：** 关闭人员。 **取值范围：** 不涉及。

        :param closeder: The closeder of this IssueNew.
        :type closeder: object
        """
        self._closeder = closeder

    @property
    def position(self):
        r"""Gets the position of this IssueNew.

        **参数解释：** 工作项在列表的展示位置 。 **取值范围：** 不涉及。

        :return: The position of this IssueNew.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this IssueNew.

        **参数解释：** 工作项在列表的展示位置 。 **取值范围：** 不涉及。

        :param position: The position of this IssueNew.
        :type position: str
        """
        self._position = position

    @property
    def closed_flag(self):
        r"""Gets the closed_flag of this IssueNew.

        **参数解释：** 关闭标志 。 **取值范围：** 0（打开） 1（关闭）

        :return: The closed_flag of this IssueNew.
        :rtype: int
        """
        return self._closed_flag

    @closed_flag.setter
    def closed_flag(self, closed_flag):
        r"""Sets the closed_flag of this IssueNew.

        **参数解释：** 关闭标志 。 **取值范围：** 0（打开） 1（关闭）

        :param closed_flag: The closed_flag of this IssueNew.
        :type closed_flag: int
        """
        self._closed_flag = closed_flag

    @property
    def assigned_cc_user(self):
        r"""Gets the assigned_cc_user of this IssueNew.

        **参数解释：** 工作项的抄送人。 **取值范围：** 不涉及。

        :return: The assigned_cc_user of this IssueNew.
        :rtype: str
        """
        return self._assigned_cc_user

    @assigned_cc_user.setter
    def assigned_cc_user(self, assigned_cc_user):
        r"""Sets the assigned_cc_user of this IssueNew.

        **参数解释：** 工作项的抄送人。 **取值范围：** 不涉及。

        :param assigned_cc_user: The assigned_cc_user of this IssueNew.
        :type assigned_cc_user: str
        """
        self._assigned_cc_user = assigned_cc_user

    @property
    def custom_value_new(self):
        r"""Gets the custom_value_new of this IssueNew.

        **参数解释：** 自定义字段。 **取值范围：** 不涉及。

        :return: The custom_value_new of this IssueNew.
        :rtype: object
        """
        return self._custom_value_new

    @custom_value_new.setter
    def custom_value_new(self, custom_value_new):
        r"""Sets the custom_value_new of this IssueNew.

        **参数解释：** 自定义字段。 **取值范围：** 不涉及。

        :param custom_value_new: The custom_value_new of this IssueNew.
        :type custom_value_new: object
        """
        self._custom_value_new = custom_value_new

    @property
    def status(self):
        r"""Gets the status of this IssueNew.

        :return: The status of this IssueNew.
        :rtype: :class:`huaweicloudsdkprojectman.v4.Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IssueNew.

        :param status: The status of this IssueNew.
        :type status: :class:`huaweicloudsdkprojectman.v4.Status`
        """
        self._status = status

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IssueNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
