# coding: utf-8

import pprint
import re

import six





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
        'developer': 'IssueUser',
        'domain': 'IssueItemSFV4Domain',
        'done_ratio': 'int',
        'end_time': 'str',
        'expected_work_hours': 'float',
        'id': 'int',
        'iteration': 'IssueItemSFV4Iteration',
        'module': 'IssueItemSFV4Module',
        'name': 'str',
        'parent_issue': 'CreateIssueResponseV4ParentIssue',
        'priority': 'IssueItemSFV4Priority',
        'project': 'IssueProjectResponseV4',
        'severity': 'IssueItemSFV4Severity',
        'status': 'IssueItemSFV4Status',
        'tracker': 'IssueItemSFV4Tracker',
        'updated_time': 'str'
    }

    attribute_map = {
        'actual_work_hours': 'actual_work_hours',
        'assigned_cc_user': 'assigned_cc_user',
        'assigned_user': 'assigned_user',
        'begin_time': 'begin_time',
        'created_time': 'created_time',
        'creator': 'creator',
        'custom_fields': 'custom_fields',
        'developer': 'developer',
        'domain': 'domain',
        'done_ratio': 'done_ratio',
        'end_time': 'end_time',
        'expected_work_hours': 'expected_work_hours',
        'id': 'id',
        'iteration': 'iteration',
        'module': 'module',
        'name': 'name',
        'parent_issue': 'parent_issue',
        'priority': 'priority',
        'project': 'project',
        'severity': 'severity',
        'status': 'status',
        'tracker': 'tracker',
        'updated_time': 'updated_time'
    }

    def __init__(self, actual_work_hours=None, assigned_cc_user=None, assigned_user=None, begin_time=None, created_time=None, creator=None, custom_fields=None, developer=None, domain=None, done_ratio=None, end_time=None, expected_work_hours=None, id=None, iteration=None, module=None, name=None, parent_issue=None, priority=None, project=None, severity=None, status=None, tracker=None, updated_time=None):
        """IssueResponseV4 - a model defined in huaweicloud sdk"""
        
        

        self._actual_work_hours = None
        self._assigned_cc_user = None
        self._assigned_user = None
        self._begin_time = None
        self._created_time = None
        self._creator = None
        self._custom_fields = None
        self._developer = None
        self._domain = None
        self._done_ratio = None
        self._end_time = None
        self._expected_work_hours = None
        self._id = None
        self._iteration = None
        self._module = None
        self._name = None
        self._parent_issue = None
        self._priority = None
        self._project = None
        self._severity = None
        self._status = None
        self._tracker = None
        self._updated_time = None
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
        if project is not None:
            self.project = project
        if severity is not None:
            self.severity = severity
        if status is not None:
            self.status = status
        if tracker is not None:
            self.tracker = tracker
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def actual_work_hours(self):
        """Gets the actual_work_hours of this IssueResponseV4.

        实际工时

        :return: The actual_work_hours of this IssueResponseV4.
        :rtype: float
        """
        return self._actual_work_hours

    @actual_work_hours.setter
    def actual_work_hours(self, actual_work_hours):
        """Sets the actual_work_hours of this IssueResponseV4.

        实际工时

        :param actual_work_hours: The actual_work_hours of this IssueResponseV4.
        :type: float
        """
        self._actual_work_hours = actual_work_hours

    @property
    def assigned_cc_user(self):
        """Gets the assigned_cc_user of this IssueResponseV4.

        抄送人

        :return: The assigned_cc_user of this IssueResponseV4.
        :rtype: list[IssueUser]
        """
        return self._assigned_cc_user

    @assigned_cc_user.setter
    def assigned_cc_user(self, assigned_cc_user):
        """Sets the assigned_cc_user of this IssueResponseV4.

        抄送人

        :param assigned_cc_user: The assigned_cc_user of this IssueResponseV4.
        :type: list[IssueUser]
        """
        self._assigned_cc_user = assigned_cc_user

    @property
    def assigned_user(self):
        """Gets the assigned_user of this IssueResponseV4.


        :return: The assigned_user of this IssueResponseV4.
        :rtype: IssueUser
        """
        return self._assigned_user

    @assigned_user.setter
    def assigned_user(self, assigned_user):
        """Sets the assigned_user of this IssueResponseV4.


        :param assigned_user: The assigned_user of this IssueResponseV4.
        :type: IssueUser
        """
        self._assigned_user = assigned_user

    @property
    def begin_time(self):
        """Gets the begin_time of this IssueResponseV4.

        开始时间，年-月-日

        :return: The begin_time of this IssueResponseV4.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this IssueResponseV4.

        开始时间，年-月-日

        :param begin_time: The begin_time of this IssueResponseV4.
        :type: str
        """
        self._begin_time = begin_time

    @property
    def created_time(self):
        """Gets the created_time of this IssueResponseV4.

        更新时间 年-月-日 时:分:秒

        :return: The created_time of this IssueResponseV4.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this IssueResponseV4.

        更新时间 年-月-日 时:分:秒

        :param created_time: The created_time of this IssueResponseV4.
        :type: str
        """
        self._created_time = created_time

    @property
    def creator(self):
        """Gets the creator of this IssueResponseV4.


        :return: The creator of this IssueResponseV4.
        :rtype: IssueUser
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this IssueResponseV4.


        :param creator: The creator of this IssueResponseV4.
        :type: IssueUser
        """
        self._creator = creator

    @property
    def custom_fields(self):
        """Gets the custom_fields of this IssueResponseV4.

        自定义属性值

        :return: The custom_fields of this IssueResponseV4.
        :rtype: list[CustomField]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this IssueResponseV4.

        自定义属性值

        :param custom_fields: The custom_fields of this IssueResponseV4.
        :type: list[CustomField]
        """
        self._custom_fields = custom_fields

    @property
    def developer(self):
        """Gets the developer of this IssueResponseV4.


        :return: The developer of this IssueResponseV4.
        :rtype: IssueUser
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        """Sets the developer of this IssueResponseV4.


        :param developer: The developer of this IssueResponseV4.
        :type: IssueUser
        """
        self._developer = developer

    @property
    def domain(self):
        """Gets the domain of this IssueResponseV4.


        :return: The domain of this IssueResponseV4.
        :rtype: IssueItemSFV4Domain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this IssueResponseV4.


        :param domain: The domain of this IssueResponseV4.
        :type: IssueItemSFV4Domain
        """
        self._domain = domain

    @property
    def done_ratio(self):
        """Gets the done_ratio of this IssueResponseV4.

        工作项进度值

        :return: The done_ratio of this IssueResponseV4.
        :rtype: int
        """
        return self._done_ratio

    @done_ratio.setter
    def done_ratio(self, done_ratio):
        """Sets the done_ratio of this IssueResponseV4.

        工作项进度值

        :param done_ratio: The done_ratio of this IssueResponseV4.
        :type: int
        """
        self._done_ratio = done_ratio

    @property
    def end_time(self):
        """Gets the end_time of this IssueResponseV4.

        结束时间，年-月-日

        :return: The end_time of this IssueResponseV4.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this IssueResponseV4.

        结束时间，年-月-日

        :param end_time: The end_time of this IssueResponseV4.
        :type: str
        """
        self._end_time = end_time

    @property
    def expected_work_hours(self):
        """Gets the expected_work_hours of this IssueResponseV4.

        预计工时

        :return: The expected_work_hours of this IssueResponseV4.
        :rtype: float
        """
        return self._expected_work_hours

    @expected_work_hours.setter
    def expected_work_hours(self, expected_work_hours):
        """Sets the expected_work_hours of this IssueResponseV4.

        预计工时

        :param expected_work_hours: The expected_work_hours of this IssueResponseV4.
        :type: float
        """
        self._expected_work_hours = expected_work_hours

    @property
    def id(self):
        """Gets the id of this IssueResponseV4.

        工作项项id

        :return: The id of this IssueResponseV4.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IssueResponseV4.

        工作项项id

        :param id: The id of this IssueResponseV4.
        :type: int
        """
        self._id = id

    @property
    def iteration(self):
        """Gets the iteration of this IssueResponseV4.


        :return: The iteration of this IssueResponseV4.
        :rtype: IssueItemSFV4Iteration
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        """Sets the iteration of this IssueResponseV4.


        :param iteration: The iteration of this IssueResponseV4.
        :type: IssueItemSFV4Iteration
        """
        self._iteration = iteration

    @property
    def module(self):
        """Gets the module of this IssueResponseV4.


        :return: The module of this IssueResponseV4.
        :rtype: IssueItemSFV4Module
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this IssueResponseV4.


        :param module: The module of this IssueResponseV4.
        :type: IssueItemSFV4Module
        """
        self._module = module

    @property
    def name(self):
        """Gets the name of this IssueResponseV4.

        标题

        :return: The name of this IssueResponseV4.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IssueResponseV4.

        标题

        :param name: The name of this IssueResponseV4.
        :type: str
        """
        self._name = name

    @property
    def parent_issue(self):
        """Gets the parent_issue of this IssueResponseV4.


        :return: The parent_issue of this IssueResponseV4.
        :rtype: CreateIssueResponseV4ParentIssue
        """
        return self._parent_issue

    @parent_issue.setter
    def parent_issue(self, parent_issue):
        """Sets the parent_issue of this IssueResponseV4.


        :param parent_issue: The parent_issue of this IssueResponseV4.
        :type: CreateIssueResponseV4ParentIssue
        """
        self._parent_issue = parent_issue

    @property
    def priority(self):
        """Gets the priority of this IssueResponseV4.


        :return: The priority of this IssueResponseV4.
        :rtype: IssueItemSFV4Priority
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this IssueResponseV4.


        :param priority: The priority of this IssueResponseV4.
        :type: IssueItemSFV4Priority
        """
        self._priority = priority

    @property
    def project(self):
        """Gets the project of this IssueResponseV4.


        :return: The project of this IssueResponseV4.
        :rtype: IssueProjectResponseV4
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this IssueResponseV4.


        :param project: The project of this IssueResponseV4.
        :type: IssueProjectResponseV4
        """
        self._project = project

    @property
    def severity(self):
        """Gets the severity of this IssueResponseV4.


        :return: The severity of this IssueResponseV4.
        :rtype: IssueItemSFV4Severity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this IssueResponseV4.


        :param severity: The severity of this IssueResponseV4.
        :type: IssueItemSFV4Severity
        """
        self._severity = severity

    @property
    def status(self):
        """Gets the status of this IssueResponseV4.


        :return: The status of this IssueResponseV4.
        :rtype: IssueItemSFV4Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IssueResponseV4.


        :param status: The status of this IssueResponseV4.
        :type: IssueItemSFV4Status
        """
        self._status = status

    @property
    def tracker(self):
        """Gets the tracker of this IssueResponseV4.


        :return: The tracker of this IssueResponseV4.
        :rtype: IssueItemSFV4Tracker
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        """Sets the tracker of this IssueResponseV4.


        :param tracker: The tracker of this IssueResponseV4.
        :type: IssueItemSFV4Tracker
        """
        self._tracker = tracker

    @property
    def updated_time(self):
        """Gets the updated_time of this IssueResponseV4.

        更新时间 年-月-日 时:分:秒

        :return: The updated_time of this IssueResponseV4.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this IssueResponseV4.

        更新时间 年-月-日 时:分:秒

        :param updated_time: The updated_time of this IssueResponseV4.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IssueResponseV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
