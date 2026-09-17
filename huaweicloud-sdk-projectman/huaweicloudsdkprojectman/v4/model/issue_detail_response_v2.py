# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueDetailResponseV2:

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
        'assigned_cc_user': 'list[UserVO]',
        'assigned_to': 'UserVO',
        'start_date': 'str',
        'created_on': 'str',
        'author': 'UserVO',
        'custom_fields': 'list[CustomFieldV2]',
        'custom_value_new': 'IssueDetailCustomFieldV2',
        'developer': 'UserVO',
        'domain': 'IssueDetailResponseV2Domain',
        'done_ratio': 'int',
        'end_time': 'str',
        'expected_work_hours': 'float',
        'id': 'int',
        'project': 'ProjectVO',
        'iteration': 'IssueDetailResponseV2Iteration',
        'story_point': 'IssueDetailResponseV2StoryPoint',
        'module': 'IssueDetailResponseV2Module',
        'subject': 'str',
        'parent_issue': 'IssueDetailResponseV2ParentIssue',
        'priority': 'IssueDetailResponseV2Priority',
        'severity': 'IssueDetailResponseV2Severity',
        'status': 'IssueDetailResponseV2Status',
        'release_dev': 'str',
        'find_release_dev': 'str',
        'env': 'IssueDetailResponseV2Env',
        'tracker': 'IssueDetailResponseV2Tracker',
        'updated_on': 'str',
        'closed_time': 'str',
        'description': 'str',
        'accessories_list': 'list[IssueAccessoryV2]',
        'inner_text': 'str'
    }

    attribute_map = {
        'actual_work_hours': 'actual_work_hours',
        'assigned_cc_user': 'assigned_cc_user',
        'assigned_to': 'assigned_to',
        'start_date': 'start_date',
        'created_on': 'created_on',
        'author': 'author',
        'custom_fields': 'custom_fields',
        'custom_value_new': 'custom_value_new',
        'developer': 'developer',
        'domain': 'domain',
        'done_ratio': 'done_ratio',
        'end_time': 'end_time',
        'expected_work_hours': 'expected_work_hours',
        'id': 'id',
        'project': 'project',
        'iteration': 'iteration',
        'story_point': 'story_point',
        'module': 'module',
        'subject': 'subject',
        'parent_issue': 'parent_issue',
        'priority': 'priority',
        'severity': 'severity',
        'status': 'status',
        'release_dev': 'release_dev',
        'find_release_dev': 'find_release_dev',
        'env': 'env',
        'tracker': 'tracker',
        'updated_on': 'updated_on',
        'closed_time': 'closed_time',
        'description': 'description',
        'accessories_list': 'accessories_list',
        'inner_text': 'inner_text'
    }

    def __init__(self, actual_work_hours=None, assigned_cc_user=None, assigned_to=None, start_date=None, created_on=None, author=None, custom_fields=None, custom_value_new=None, developer=None, domain=None, done_ratio=None, end_time=None, expected_work_hours=None, id=None, project=None, iteration=None, story_point=None, module=None, subject=None, parent_issue=None, priority=None, severity=None, status=None, release_dev=None, find_release_dev=None, env=None, tracker=None, updated_on=None, closed_time=None, description=None, accessories_list=None, inner_text=None):
        r"""IssueDetailResponseV2

        The model defined in huaweicloud sdk

        :param actual_work_hours: **参数解释：** 工作项的实际工时（单位：人/时）。 **取值范围：** 不涉及。
        :type actual_work_hours: float
        :param assigned_cc_user: **参数解释：** 当前工作项的抄送人。
        :type assigned_cc_user: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        :param assigned_to: 
        :type assigned_to: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param start_date: **参数解释：** 工作项的预计开始时间，时间戳格式（示例：1754323200000）。 **取值范围：** 不涉及。
        :type start_date: str
        :param created_on: **参数解释：** 工作项创建时间，时间戳格式（示例：1754374102000）。 **取值范围：** 不涉及。
        :type created_on: str
        :param author: 
        :type author: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param custom_fields: **参数解释：** 工作项的自定义字段。
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.CustomFieldV2`]
        :param custom_value_new: 
        :type custom_value_new: :class:`huaweicloudsdkprojectman.v4.IssueDetailCustomFieldV2`
        :param developer: 
        :type developer: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param domain: 
        :type domain: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Domain`
        :param done_ratio: **参数解释：** 工作项完成度。 **取值范围：** 不涉及。
        :type done_ratio: int
        :param end_time: **参数解释：** 工作项的预计结束时间，时间戳格式（示例：1754323200000）。 **取值范围：** 不涉及。
        :type end_time: str
        :param expected_work_hours: **参数解释：** 工作项的预计完成工时（单位：人/时）。 **取值范围：** 不涉及。
        :type expected_work_hours: float
        :param id: **参数解释：** 工作项id。 **取值范围：** 不涉及。
        :type id: int
        :param project: 
        :type project: :class:`huaweicloudsdkprojectman.v4.ProjectVO`
        :param iteration: 
        :type iteration: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Iteration`
        :param story_point: 
        :type story_point: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2StoryPoint`
        :param module: 
        :type module: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Module`
        :param subject: **参数解释：** 工作项的标题。 **取值范围：** 不涉及。
        :type subject: str
        :param parent_issue: 
        :type parent_issue: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2ParentIssue`
        :param priority: 
        :type priority: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Priority`
        :param severity: 
        :type severity: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Severity`
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Status`
        :param release_dev: **参数解释：** 工作项发布版本号。 **取值范围：** 不涉及。
        :type release_dev: str
        :param find_release_dev: **参数解释：** 缺陷发现版本号（仅Bug类型工作项具备该字段）。 **取值范围：** 不涉及。
        :type find_release_dev: str
        :param env: 
        :type env: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Env`
        :param tracker: 
        :type tracker: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Tracker`
        :param updated_on: **参数解释：** 工作项的最后更新时间，时间戳格式（示例：1754374102000）。 **取值范围：** 不涉及。
        :type updated_on: str
        :param closed_time: **参数解释：** 工作项的关闭时间，时间戳格式（示例：1754374102000）。 **取值范围：** 不涉及。
        :type closed_time: str
        :param description: **参数解释：** 工作项描述。 **取值范围：** 不涉及。
        :type description: str
        :param accessories_list: **参数解释：** 工作项的附件列表。
        :type accessories_list: list[:class:`huaweicloudsdkprojectman.v4.IssueAccessoryV2`]
        :param inner_text: **参数解释：** 工作项更新的评论内容。 **取值范围：** 不涉及。
        :type inner_text: str
        """
        
        

        self._actual_work_hours = None
        self._assigned_cc_user = None
        self._assigned_to = None
        self._start_date = None
        self._created_on = None
        self._author = None
        self._custom_fields = None
        self._custom_value_new = None
        self._developer = None
        self._domain = None
        self._done_ratio = None
        self._end_time = None
        self._expected_work_hours = None
        self._id = None
        self._project = None
        self._iteration = None
        self._story_point = None
        self._module = None
        self._subject = None
        self._parent_issue = None
        self._priority = None
        self._severity = None
        self._status = None
        self._release_dev = None
        self._find_release_dev = None
        self._env = None
        self._tracker = None
        self._updated_on = None
        self._closed_time = None
        self._description = None
        self._accessories_list = None
        self._inner_text = None
        self.discriminator = None

        if actual_work_hours is not None:
            self.actual_work_hours = actual_work_hours
        if assigned_cc_user is not None:
            self.assigned_cc_user = assigned_cc_user
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if start_date is not None:
            self.start_date = start_date
        if created_on is not None:
            self.created_on = created_on
        if author is not None:
            self.author = author
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if custom_value_new is not None:
            self.custom_value_new = custom_value_new
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
        if story_point is not None:
            self.story_point = story_point
        if module is not None:
            self.module = module
        if subject is not None:
            self.subject = subject
        if parent_issue is not None:
            self.parent_issue = parent_issue
        if priority is not None:
            self.priority = priority
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
        if updated_on is not None:
            self.updated_on = updated_on
        if closed_time is not None:
            self.closed_time = closed_time
        if description is not None:
            self.description = description
        if accessories_list is not None:
            self.accessories_list = accessories_list
        if inner_text is not None:
            self.inner_text = inner_text

    @property
    def actual_work_hours(self):
        r"""Gets the actual_work_hours of this IssueDetailResponseV2.

        **参数解释：** 工作项的实际工时（单位：人/时）。 **取值范围：** 不涉及。

        :return: The actual_work_hours of this IssueDetailResponseV2.
        :rtype: float
        """
        return self._actual_work_hours

    @actual_work_hours.setter
    def actual_work_hours(self, actual_work_hours):
        r"""Sets the actual_work_hours of this IssueDetailResponseV2.

        **参数解释：** 工作项的实际工时（单位：人/时）。 **取值范围：** 不涉及。

        :param actual_work_hours: The actual_work_hours of this IssueDetailResponseV2.
        :type actual_work_hours: float
        """
        self._actual_work_hours = actual_work_hours

    @property
    def assigned_cc_user(self):
        r"""Gets the assigned_cc_user of this IssueDetailResponseV2.

        **参数解释：** 当前工作项的抄送人。

        :return: The assigned_cc_user of this IssueDetailResponseV2.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        """
        return self._assigned_cc_user

    @assigned_cc_user.setter
    def assigned_cc_user(self, assigned_cc_user):
        r"""Sets the assigned_cc_user of this IssueDetailResponseV2.

        **参数解释：** 当前工作项的抄送人。

        :param assigned_cc_user: The assigned_cc_user of this IssueDetailResponseV2.
        :type assigned_cc_user: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        """
        self._assigned_cc_user = assigned_cc_user

    @property
    def assigned_to(self):
        r"""Gets the assigned_to of this IssueDetailResponseV2.

        :return: The assigned_to of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        r"""Sets the assigned_to of this IssueDetailResponseV2.

        :param assigned_to: The assigned_to of this IssueDetailResponseV2.
        :type assigned_to: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._assigned_to = assigned_to

    @property
    def start_date(self):
        r"""Gets the start_date of this IssueDetailResponseV2.

        **参数解释：** 工作项的预计开始时间，时间戳格式（示例：1754323200000）。 **取值范围：** 不涉及。

        :return: The start_date of this IssueDetailResponseV2.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this IssueDetailResponseV2.

        **参数解释：** 工作项的预计开始时间，时间戳格式（示例：1754323200000）。 **取值范围：** 不涉及。

        :param start_date: The start_date of this IssueDetailResponseV2.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def created_on(self):
        r"""Gets the created_on of this IssueDetailResponseV2.

        **参数解释：** 工作项创建时间，时间戳格式（示例：1754374102000）。 **取值范围：** 不涉及。

        :return: The created_on of this IssueDetailResponseV2.
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        r"""Sets the created_on of this IssueDetailResponseV2.

        **参数解释：** 工作项创建时间，时间戳格式（示例：1754374102000）。 **取值范围：** 不涉及。

        :param created_on: The created_on of this IssueDetailResponseV2.
        :type created_on: str
        """
        self._created_on = created_on

    @property
    def author(self):
        r"""Gets the author of this IssueDetailResponseV2.

        :return: The author of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this IssueDetailResponseV2.

        :param author: The author of this IssueDetailResponseV2.
        :type author: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._author = author

    @property
    def custom_fields(self):
        r"""Gets the custom_fields of this IssueDetailResponseV2.

        **参数解释：** 工作项的自定义字段。

        :return: The custom_fields of this IssueDetailResponseV2.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CustomFieldV2`]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        r"""Sets the custom_fields of this IssueDetailResponseV2.

        **参数解释：** 工作项的自定义字段。

        :param custom_fields: The custom_fields of this IssueDetailResponseV2.
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.CustomFieldV2`]
        """
        self._custom_fields = custom_fields

    @property
    def custom_value_new(self):
        r"""Gets the custom_value_new of this IssueDetailResponseV2.

        :return: The custom_value_new of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailCustomFieldV2`
        """
        return self._custom_value_new

    @custom_value_new.setter
    def custom_value_new(self, custom_value_new):
        r"""Sets the custom_value_new of this IssueDetailResponseV2.

        :param custom_value_new: The custom_value_new of this IssueDetailResponseV2.
        :type custom_value_new: :class:`huaweicloudsdkprojectman.v4.IssueDetailCustomFieldV2`
        """
        self._custom_value_new = custom_value_new

    @property
    def developer(self):
        r"""Gets the developer of this IssueDetailResponseV2.

        :return: The developer of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        r"""Sets the developer of this IssueDetailResponseV2.

        :param developer: The developer of this IssueDetailResponseV2.
        :type developer: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._developer = developer

    @property
    def domain(self):
        r"""Gets the domain of this IssueDetailResponseV2.

        :return: The domain of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Domain`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this IssueDetailResponseV2.

        :param domain: The domain of this IssueDetailResponseV2.
        :type domain: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Domain`
        """
        self._domain = domain

    @property
    def done_ratio(self):
        r"""Gets the done_ratio of this IssueDetailResponseV2.

        **参数解释：** 工作项完成度。 **取值范围：** 不涉及。

        :return: The done_ratio of this IssueDetailResponseV2.
        :rtype: int
        """
        return self._done_ratio

    @done_ratio.setter
    def done_ratio(self, done_ratio):
        r"""Sets the done_ratio of this IssueDetailResponseV2.

        **参数解释：** 工作项完成度。 **取值范围：** 不涉及。

        :param done_ratio: The done_ratio of this IssueDetailResponseV2.
        :type done_ratio: int
        """
        self._done_ratio = done_ratio

    @property
    def end_time(self):
        r"""Gets the end_time of this IssueDetailResponseV2.

        **参数解释：** 工作项的预计结束时间，时间戳格式（示例：1754323200000）。 **取值范围：** 不涉及。

        :return: The end_time of this IssueDetailResponseV2.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this IssueDetailResponseV2.

        **参数解释：** 工作项的预计结束时间，时间戳格式（示例：1754323200000）。 **取值范围：** 不涉及。

        :param end_time: The end_time of this IssueDetailResponseV2.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def expected_work_hours(self):
        r"""Gets the expected_work_hours of this IssueDetailResponseV2.

        **参数解释：** 工作项的预计完成工时（单位：人/时）。 **取值范围：** 不涉及。

        :return: The expected_work_hours of this IssueDetailResponseV2.
        :rtype: float
        """
        return self._expected_work_hours

    @expected_work_hours.setter
    def expected_work_hours(self, expected_work_hours):
        r"""Sets the expected_work_hours of this IssueDetailResponseV2.

        **参数解释：** 工作项的预计完成工时（单位：人/时）。 **取值范围：** 不涉及。

        :param expected_work_hours: The expected_work_hours of this IssueDetailResponseV2.
        :type expected_work_hours: float
        """
        self._expected_work_hours = expected_work_hours

    @property
    def id(self):
        r"""Gets the id of this IssueDetailResponseV2.

        **参数解释：** 工作项id。 **取值范围：** 不涉及。

        :return: The id of this IssueDetailResponseV2.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueDetailResponseV2.

        **参数解释：** 工作项id。 **取值范围：** 不涉及。

        :param id: The id of this IssueDetailResponseV2.
        :type id: int
        """
        self._id = id

    @property
    def project(self):
        r"""Gets the project of this IssueDetailResponseV2.

        :return: The project of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ProjectVO`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this IssueDetailResponseV2.

        :param project: The project of this IssueDetailResponseV2.
        :type project: :class:`huaweicloudsdkprojectman.v4.ProjectVO`
        """
        self._project = project

    @property
    def iteration(self):
        r"""Gets the iteration of this IssueDetailResponseV2.

        :return: The iteration of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Iteration`
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        r"""Sets the iteration of this IssueDetailResponseV2.

        :param iteration: The iteration of this IssueDetailResponseV2.
        :type iteration: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Iteration`
        """
        self._iteration = iteration

    @property
    def story_point(self):
        r"""Gets the story_point of this IssueDetailResponseV2.

        :return: The story_point of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2StoryPoint`
        """
        return self._story_point

    @story_point.setter
    def story_point(self, story_point):
        r"""Sets the story_point of this IssueDetailResponseV2.

        :param story_point: The story_point of this IssueDetailResponseV2.
        :type story_point: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2StoryPoint`
        """
        self._story_point = story_point

    @property
    def module(self):
        r"""Gets the module of this IssueDetailResponseV2.

        :return: The module of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Module`
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this IssueDetailResponseV2.

        :param module: The module of this IssueDetailResponseV2.
        :type module: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Module`
        """
        self._module = module

    @property
    def subject(self):
        r"""Gets the subject of this IssueDetailResponseV2.

        **参数解释：** 工作项的标题。 **取值范围：** 不涉及。

        :return: The subject of this IssueDetailResponseV2.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this IssueDetailResponseV2.

        **参数解释：** 工作项的标题。 **取值范围：** 不涉及。

        :param subject: The subject of this IssueDetailResponseV2.
        :type subject: str
        """
        self._subject = subject

    @property
    def parent_issue(self):
        r"""Gets the parent_issue of this IssueDetailResponseV2.

        :return: The parent_issue of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2ParentIssue`
        """
        return self._parent_issue

    @parent_issue.setter
    def parent_issue(self, parent_issue):
        r"""Sets the parent_issue of this IssueDetailResponseV2.

        :param parent_issue: The parent_issue of this IssueDetailResponseV2.
        :type parent_issue: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2ParentIssue`
        """
        self._parent_issue = parent_issue

    @property
    def priority(self):
        r"""Gets the priority of this IssueDetailResponseV2.

        :return: The priority of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Priority`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this IssueDetailResponseV2.

        :param priority: The priority of this IssueDetailResponseV2.
        :type priority: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Priority`
        """
        self._priority = priority

    @property
    def severity(self):
        r"""Gets the severity of this IssueDetailResponseV2.

        :return: The severity of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Severity`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this IssueDetailResponseV2.

        :param severity: The severity of this IssueDetailResponseV2.
        :type severity: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Severity`
        """
        self._severity = severity

    @property
    def status(self):
        r"""Gets the status of this IssueDetailResponseV2.

        :return: The status of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IssueDetailResponseV2.

        :param status: The status of this IssueDetailResponseV2.
        :type status: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Status`
        """
        self._status = status

    @property
    def release_dev(self):
        r"""Gets the release_dev of this IssueDetailResponseV2.

        **参数解释：** 工作项发布版本号。 **取值范围：** 不涉及。

        :return: The release_dev of this IssueDetailResponseV2.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this IssueDetailResponseV2.

        **参数解释：** 工作项发布版本号。 **取值范围：** 不涉及。

        :param release_dev: The release_dev of this IssueDetailResponseV2.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def find_release_dev(self):
        r"""Gets the find_release_dev of this IssueDetailResponseV2.

        **参数解释：** 缺陷发现版本号（仅Bug类型工作项具备该字段）。 **取值范围：** 不涉及。

        :return: The find_release_dev of this IssueDetailResponseV2.
        :rtype: str
        """
        return self._find_release_dev

    @find_release_dev.setter
    def find_release_dev(self, find_release_dev):
        r"""Sets the find_release_dev of this IssueDetailResponseV2.

        **参数解释：** 缺陷发现版本号（仅Bug类型工作项具备该字段）。 **取值范围：** 不涉及。

        :param find_release_dev: The find_release_dev of this IssueDetailResponseV2.
        :type find_release_dev: str
        """
        self._find_release_dev = find_release_dev

    @property
    def env(self):
        r"""Gets the env of this IssueDetailResponseV2.

        :return: The env of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Env`
        """
        return self._env

    @env.setter
    def env(self, env):
        r"""Sets the env of this IssueDetailResponseV2.

        :param env: The env of this IssueDetailResponseV2.
        :type env: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Env`
        """
        self._env = env

    @property
    def tracker(self):
        r"""Gets the tracker of this IssueDetailResponseV2.

        :return: The tracker of this IssueDetailResponseV2.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Tracker`
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        r"""Sets the tracker of this IssueDetailResponseV2.

        :param tracker: The tracker of this IssueDetailResponseV2.
        :type tracker: :class:`huaweicloudsdkprojectman.v4.IssueDetailResponseV2Tracker`
        """
        self._tracker = tracker

    @property
    def updated_on(self):
        r"""Gets the updated_on of this IssueDetailResponseV2.

        **参数解释：** 工作项的最后更新时间，时间戳格式（示例：1754374102000）。 **取值范围：** 不涉及。

        :return: The updated_on of this IssueDetailResponseV2.
        :rtype: str
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        r"""Sets the updated_on of this IssueDetailResponseV2.

        **参数解释：** 工作项的最后更新时间，时间戳格式（示例：1754374102000）。 **取值范围：** 不涉及。

        :param updated_on: The updated_on of this IssueDetailResponseV2.
        :type updated_on: str
        """
        self._updated_on = updated_on

    @property
    def closed_time(self):
        r"""Gets the closed_time of this IssueDetailResponseV2.

        **参数解释：** 工作项的关闭时间，时间戳格式（示例：1754374102000）。 **取值范围：** 不涉及。

        :return: The closed_time of this IssueDetailResponseV2.
        :rtype: str
        """
        return self._closed_time

    @closed_time.setter
    def closed_time(self, closed_time):
        r"""Sets the closed_time of this IssueDetailResponseV2.

        **参数解释：** 工作项的关闭时间，时间戳格式（示例：1754374102000）。 **取值范围：** 不涉及。

        :param closed_time: The closed_time of this IssueDetailResponseV2.
        :type closed_time: str
        """
        self._closed_time = closed_time

    @property
    def description(self):
        r"""Gets the description of this IssueDetailResponseV2.

        **参数解释：** 工作项描述。 **取值范围：** 不涉及。

        :return: The description of this IssueDetailResponseV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IssueDetailResponseV2.

        **参数解释：** 工作项描述。 **取值范围：** 不涉及。

        :param description: The description of this IssueDetailResponseV2.
        :type description: str
        """
        self._description = description

    @property
    def accessories_list(self):
        r"""Gets the accessories_list of this IssueDetailResponseV2.

        **参数解释：** 工作项的附件列表。

        :return: The accessories_list of this IssueDetailResponseV2.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueAccessoryV2`]
        """
        return self._accessories_list

    @accessories_list.setter
    def accessories_list(self, accessories_list):
        r"""Sets the accessories_list of this IssueDetailResponseV2.

        **参数解释：** 工作项的附件列表。

        :param accessories_list: The accessories_list of this IssueDetailResponseV2.
        :type accessories_list: list[:class:`huaweicloudsdkprojectman.v4.IssueAccessoryV2`]
        """
        self._accessories_list = accessories_list

    @property
    def inner_text(self):
        r"""Gets the inner_text of this IssueDetailResponseV2.

        **参数解释：** 工作项更新的评论内容。 **取值范围：** 不涉及。

        :return: The inner_text of this IssueDetailResponseV2.
        :rtype: str
        """
        return self._inner_text

    @inner_text.setter
    def inner_text(self, inner_text):
        r"""Sets the inner_text of this IssueDetailResponseV2.

        **参数解释：** 工作项更新的评论内容。 **取值范围：** 不涉及。

        :param inner_text: The inner_text of this IssueDetailResponseV2.
        :type inner_text: str
        """
        self._inner_text = inner_text

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
        if not isinstance(other, IssueDetailResponseV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
