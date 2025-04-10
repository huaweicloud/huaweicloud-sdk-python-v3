# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueItemSfV4:

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
        'assigned_user': 'IssueUser',
        'author': 'IssueUser',
        'begin_time': 'int',
        'closed_time': 'int',
        'created_time': 'int',
        'custom_feilds': 'list[CustomFeildRecord]',
        'developer': 'IssueUser',
        'discover_version': 'str',
        'end_time': 'int',
        'done_ratio': 'int',
        'expected_work_hours': 'float',
        'order': 'int',
        'parent_issue_id': 'int',
        'release_version': 'str',
        'root_issue_id': 'int',
        'story_point': 'IssueItemSfV4StoryPoint',
        'domain': 'IssueItemSfV4Domain',
        'iteration': 'IssueItemSfV4Iteration',
        'module': 'IssueItemSfV4Module',
        'priority': 'IssueItemSfV4Priority',
        'severity': 'IssueItemSfV4Severity',
        'status': 'IssueItemSfV4Status',
        'tracker': 'IssueItemSfV4Tracker',
        'subject': 'str',
        'updated_time': 'int'
    }

    attribute_map = {
        'actual_work_hours': 'actual_work_hours',
        'assigned_user': 'assigned_user',
        'author': 'author',
        'begin_time': 'begin_time',
        'closed_time': 'closed_time',
        'created_time': 'created_time',
        'custom_feilds': 'custom_feilds',
        'developer': 'developer',
        'discover_version': 'discover_version',
        'end_time': 'end_time',
        'done_ratio': 'done_ratio',
        'expected_work_hours': 'expected_work_hours',
        'order': 'order',
        'parent_issue_id': 'parent_issue_id',
        'release_version': 'release_version',
        'root_issue_id': 'root_issue_id',
        'story_point': 'story_point',
        'domain': 'domain',
        'iteration': 'iteration',
        'module': 'module',
        'priority': 'priority',
        'severity': 'severity',
        'status': 'status',
        'tracker': 'tracker',
        'subject': 'subject',
        'updated_time': 'updated_time'
    }

    def __init__(self, actual_work_hours=None, assigned_user=None, author=None, begin_time=None, closed_time=None, created_time=None, custom_feilds=None, developer=None, discover_version=None, end_time=None, done_ratio=None, expected_work_hours=None, order=None, parent_issue_id=None, release_version=None, root_issue_id=None, story_point=None, domain=None, iteration=None, module=None, priority=None, severity=None, status=None, tracker=None, subject=None, updated_time=None):
        r"""IssueItemSfV4

        The model defined in huaweicloud sdk

        :param actual_work_hours: 实际工时
        :type actual_work_hours: float
        :param assigned_user: 
        :type assigned_user: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        :param author: 
        :type author: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        :param begin_time: 工作项开始时间
        :type begin_time: int
        :param closed_time: 关闭工作项的时间
        :type closed_time: int
        :param created_time: 创建时间
        :type created_time: int
        :param custom_feilds: 自定义属性
        :type custom_feilds: list[:class:`huaweicloudsdkprojectman.v4.CustomFeildRecord`]
        :param developer: 
        :type developer: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        :param discover_version: 发现问题的版本
        :type discover_version: str
        :param end_time: 工作项结束时间
        :type end_time: int
        :param done_ratio: 工作项进度值
        :type done_ratio: int
        :param expected_work_hours: 预计工时
        :type expected_work_hours: float
        :param order: 顺序
        :type order: int
        :param parent_issue_id: 父工作项的id
        :type parent_issue_id: int
        :param release_version: 发布的版本
        :type release_version: str
        :param root_issue_id: 根工作项的id
        :type root_issue_id: int
        :param story_point: 
        :type story_point: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4StoryPoint`
        :param domain: 
        :type domain: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Domain`
        :param iteration: 
        :type iteration: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Iteration`
        :param module: 
        :type module: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Module`
        :param priority: 
        :type priority: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Priority`
        :param severity: 
        :type severity: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Severity`
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Status`
        :param tracker: 
        :type tracker: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Tracker`
        :param subject: 工作项标题
        :type subject: str
        :param updated_time: 工作项更新时间
        :type updated_time: int
        """
        
        

        self._actual_work_hours = None
        self._assigned_user = None
        self._author = None
        self._begin_time = None
        self._closed_time = None
        self._created_time = None
        self._custom_feilds = None
        self._developer = None
        self._discover_version = None
        self._end_time = None
        self._done_ratio = None
        self._expected_work_hours = None
        self._order = None
        self._parent_issue_id = None
        self._release_version = None
        self._root_issue_id = None
        self._story_point = None
        self._domain = None
        self._iteration = None
        self._module = None
        self._priority = None
        self._severity = None
        self._status = None
        self._tracker = None
        self._subject = None
        self._updated_time = None
        self.discriminator = None

        if actual_work_hours is not None:
            self.actual_work_hours = actual_work_hours
        if assigned_user is not None:
            self.assigned_user = assigned_user
        if author is not None:
            self.author = author
        if begin_time is not None:
            self.begin_time = begin_time
        if closed_time is not None:
            self.closed_time = closed_time
        if created_time is not None:
            self.created_time = created_time
        if custom_feilds is not None:
            self.custom_feilds = custom_feilds
        if developer is not None:
            self.developer = developer
        if discover_version is not None:
            self.discover_version = discover_version
        if end_time is not None:
            self.end_time = end_time
        if done_ratio is not None:
            self.done_ratio = done_ratio
        if expected_work_hours is not None:
            self.expected_work_hours = expected_work_hours
        if order is not None:
            self.order = order
        if parent_issue_id is not None:
            self.parent_issue_id = parent_issue_id
        if release_version is not None:
            self.release_version = release_version
        if root_issue_id is not None:
            self.root_issue_id = root_issue_id
        if story_point is not None:
            self.story_point = story_point
        if domain is not None:
            self.domain = domain
        if iteration is not None:
            self.iteration = iteration
        if module is not None:
            self.module = module
        if priority is not None:
            self.priority = priority
        if severity is not None:
            self.severity = severity
        if status is not None:
            self.status = status
        if tracker is not None:
            self.tracker = tracker
        if subject is not None:
            self.subject = subject
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def actual_work_hours(self):
        r"""Gets the actual_work_hours of this IssueItemSfV4.

        实际工时

        :return: The actual_work_hours of this IssueItemSfV4.
        :rtype: float
        """
        return self._actual_work_hours

    @actual_work_hours.setter
    def actual_work_hours(self, actual_work_hours):
        r"""Sets the actual_work_hours of this IssueItemSfV4.

        实际工时

        :param actual_work_hours: The actual_work_hours of this IssueItemSfV4.
        :type actual_work_hours: float
        """
        self._actual_work_hours = actual_work_hours

    @property
    def assigned_user(self):
        r"""Gets the assigned_user of this IssueItemSfV4.

        :return: The assigned_user of this IssueItemSfV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        return self._assigned_user

    @assigned_user.setter
    def assigned_user(self, assigned_user):
        r"""Sets the assigned_user of this IssueItemSfV4.

        :param assigned_user: The assigned_user of this IssueItemSfV4.
        :type assigned_user: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        self._assigned_user = assigned_user

    @property
    def author(self):
        r"""Gets the author of this IssueItemSfV4.

        :return: The author of this IssueItemSfV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this IssueItemSfV4.

        :param author: The author of this IssueItemSfV4.
        :type author: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        self._author = author

    @property
    def begin_time(self):
        r"""Gets the begin_time of this IssueItemSfV4.

        工作项开始时间

        :return: The begin_time of this IssueItemSfV4.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this IssueItemSfV4.

        工作项开始时间

        :param begin_time: The begin_time of this IssueItemSfV4.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def closed_time(self):
        r"""Gets the closed_time of this IssueItemSfV4.

        关闭工作项的时间

        :return: The closed_time of this IssueItemSfV4.
        :rtype: int
        """
        return self._closed_time

    @closed_time.setter
    def closed_time(self, closed_time):
        r"""Sets the closed_time of this IssueItemSfV4.

        关闭工作项的时间

        :param closed_time: The closed_time of this IssueItemSfV4.
        :type closed_time: int
        """
        self._closed_time = closed_time

    @property
    def created_time(self):
        r"""Gets the created_time of this IssueItemSfV4.

        创建时间

        :return: The created_time of this IssueItemSfV4.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this IssueItemSfV4.

        创建时间

        :param created_time: The created_time of this IssueItemSfV4.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def custom_feilds(self):
        r"""Gets the custom_feilds of this IssueItemSfV4.

        自定义属性

        :return: The custom_feilds of this IssueItemSfV4.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CustomFeildRecord`]
        """
        return self._custom_feilds

    @custom_feilds.setter
    def custom_feilds(self, custom_feilds):
        r"""Sets the custom_feilds of this IssueItemSfV4.

        自定义属性

        :param custom_feilds: The custom_feilds of this IssueItemSfV4.
        :type custom_feilds: list[:class:`huaweicloudsdkprojectman.v4.CustomFeildRecord`]
        """
        self._custom_feilds = custom_feilds

    @property
    def developer(self):
        r"""Gets the developer of this IssueItemSfV4.

        :return: The developer of this IssueItemSfV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        r"""Sets the developer of this IssueItemSfV4.

        :param developer: The developer of this IssueItemSfV4.
        :type developer: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        self._developer = developer

    @property
    def discover_version(self):
        r"""Gets the discover_version of this IssueItemSfV4.

        发现问题的版本

        :return: The discover_version of this IssueItemSfV4.
        :rtype: str
        """
        return self._discover_version

    @discover_version.setter
    def discover_version(self, discover_version):
        r"""Sets the discover_version of this IssueItemSfV4.

        发现问题的版本

        :param discover_version: The discover_version of this IssueItemSfV4.
        :type discover_version: str
        """
        self._discover_version = discover_version

    @property
    def end_time(self):
        r"""Gets the end_time of this IssueItemSfV4.

        工作项结束时间

        :return: The end_time of this IssueItemSfV4.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this IssueItemSfV4.

        工作项结束时间

        :param end_time: The end_time of this IssueItemSfV4.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def done_ratio(self):
        r"""Gets the done_ratio of this IssueItemSfV4.

        工作项进度值

        :return: The done_ratio of this IssueItemSfV4.
        :rtype: int
        """
        return self._done_ratio

    @done_ratio.setter
    def done_ratio(self, done_ratio):
        r"""Sets the done_ratio of this IssueItemSfV4.

        工作项进度值

        :param done_ratio: The done_ratio of this IssueItemSfV4.
        :type done_ratio: int
        """
        self._done_ratio = done_ratio

    @property
    def expected_work_hours(self):
        r"""Gets the expected_work_hours of this IssueItemSfV4.

        预计工时

        :return: The expected_work_hours of this IssueItemSfV4.
        :rtype: float
        """
        return self._expected_work_hours

    @expected_work_hours.setter
    def expected_work_hours(self, expected_work_hours):
        r"""Sets the expected_work_hours of this IssueItemSfV4.

        预计工时

        :param expected_work_hours: The expected_work_hours of this IssueItemSfV4.
        :type expected_work_hours: float
        """
        self._expected_work_hours = expected_work_hours

    @property
    def order(self):
        r"""Gets the order of this IssueItemSfV4.

        顺序

        :return: The order of this IssueItemSfV4.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this IssueItemSfV4.

        顺序

        :param order: The order of this IssueItemSfV4.
        :type order: int
        """
        self._order = order

    @property
    def parent_issue_id(self):
        r"""Gets the parent_issue_id of this IssueItemSfV4.

        父工作项的id

        :return: The parent_issue_id of this IssueItemSfV4.
        :rtype: int
        """
        return self._parent_issue_id

    @parent_issue_id.setter
    def parent_issue_id(self, parent_issue_id):
        r"""Sets the parent_issue_id of this IssueItemSfV4.

        父工作项的id

        :param parent_issue_id: The parent_issue_id of this IssueItemSfV4.
        :type parent_issue_id: int
        """
        self._parent_issue_id = parent_issue_id

    @property
    def release_version(self):
        r"""Gets the release_version of this IssueItemSfV4.

        发布的版本

        :return: The release_version of this IssueItemSfV4.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        r"""Sets the release_version of this IssueItemSfV4.

        发布的版本

        :param release_version: The release_version of this IssueItemSfV4.
        :type release_version: str
        """
        self._release_version = release_version

    @property
    def root_issue_id(self):
        r"""Gets the root_issue_id of this IssueItemSfV4.

        根工作项的id

        :return: The root_issue_id of this IssueItemSfV4.
        :rtype: int
        """
        return self._root_issue_id

    @root_issue_id.setter
    def root_issue_id(self, root_issue_id):
        r"""Sets the root_issue_id of this IssueItemSfV4.

        根工作项的id

        :param root_issue_id: The root_issue_id of this IssueItemSfV4.
        :type root_issue_id: int
        """
        self._root_issue_id = root_issue_id

    @property
    def story_point(self):
        r"""Gets the story_point of this IssueItemSfV4.

        :return: The story_point of this IssueItemSfV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4StoryPoint`
        """
        return self._story_point

    @story_point.setter
    def story_point(self, story_point):
        r"""Sets the story_point of this IssueItemSfV4.

        :param story_point: The story_point of this IssueItemSfV4.
        :type story_point: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4StoryPoint`
        """
        self._story_point = story_point

    @property
    def domain(self):
        r"""Gets the domain of this IssueItemSfV4.

        :return: The domain of this IssueItemSfV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Domain`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this IssueItemSfV4.

        :param domain: The domain of this IssueItemSfV4.
        :type domain: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Domain`
        """
        self._domain = domain

    @property
    def iteration(self):
        r"""Gets the iteration of this IssueItemSfV4.

        :return: The iteration of this IssueItemSfV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Iteration`
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        r"""Sets the iteration of this IssueItemSfV4.

        :param iteration: The iteration of this IssueItemSfV4.
        :type iteration: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Iteration`
        """
        self._iteration = iteration

    @property
    def module(self):
        r"""Gets the module of this IssueItemSfV4.

        :return: The module of this IssueItemSfV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Module`
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this IssueItemSfV4.

        :param module: The module of this IssueItemSfV4.
        :type module: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Module`
        """
        self._module = module

    @property
    def priority(self):
        r"""Gets the priority of this IssueItemSfV4.

        :return: The priority of this IssueItemSfV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Priority`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this IssueItemSfV4.

        :param priority: The priority of this IssueItemSfV4.
        :type priority: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Priority`
        """
        self._priority = priority

    @property
    def severity(self):
        r"""Gets the severity of this IssueItemSfV4.

        :return: The severity of this IssueItemSfV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Severity`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this IssueItemSfV4.

        :param severity: The severity of this IssueItemSfV4.
        :type severity: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Severity`
        """
        self._severity = severity

    @property
    def status(self):
        r"""Gets the status of this IssueItemSfV4.

        :return: The status of this IssueItemSfV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IssueItemSfV4.

        :param status: The status of this IssueItemSfV4.
        :type status: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Status`
        """
        self._status = status

    @property
    def tracker(self):
        r"""Gets the tracker of this IssueItemSfV4.

        :return: The tracker of this IssueItemSfV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Tracker`
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        r"""Sets the tracker of this IssueItemSfV4.

        :param tracker: The tracker of this IssueItemSfV4.
        :type tracker: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Tracker`
        """
        self._tracker = tracker

    @property
    def subject(self):
        r"""Gets the subject of this IssueItemSfV4.

        工作项标题

        :return: The subject of this IssueItemSfV4.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this IssueItemSfV4.

        工作项标题

        :param subject: The subject of this IssueItemSfV4.
        :type subject: str
        """
        self._subject = subject

    @property
    def updated_time(self):
        r"""Gets the updated_time of this IssueItemSfV4.

        工作项更新时间

        :return: The updated_time of this IssueItemSfV4.
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this IssueItemSfV4.

        工作项更新时间

        :param updated_time: The updated_time of this IssueItemSfV4.
        :type updated_time: int
        """
        self._updated_time = updated_time

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
        if not isinstance(other, IssueItemSfV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
