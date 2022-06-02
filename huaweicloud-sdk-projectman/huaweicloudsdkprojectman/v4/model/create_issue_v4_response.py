# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIssueV4Response(SdkResponse):

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
        'creator': 'IssueUser',
        'custom_fields': 'list[CustomField]',
        'new_custom_fields': 'list[NewCustomField]',
        'developer': 'IssueUser',
        'domain': 'CreateIssueResponseV4Domain',
        'done_ratio': 'int',
        'end_time': 'str',
        'expected_work_hours': 'float',
        'id': 'int',
        'project': 'IssueProjectResponseV4',
        'iteration': 'IssueItemSfV4Iteration',
        'module': 'IssueItemSfV4Module',
        'parent_issue': 'CreateIssueResponseV4ParentIssue',
        'priority': 'IssueItemSfV4Priority',
        'severity': 'IssueItemSfV4Severity',
        'status': 'IssueItemSfV4Status',
        'tracker': 'CreateIssueResponseV4Tracker'
    }

    attribute_map = {
        'actual_work_hours': 'actual_work_hours',
        'assigned_cc_user': 'assigned_cc_user',
        'assigned_user': 'assigned_user',
        'begin_time': 'begin_time',
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
        'parent_issue': 'parent_issue',
        'priority': 'priority',
        'severity': 'severity',
        'status': 'status',
        'tracker': 'tracker'
    }

    def __init__(self, actual_work_hours=None, assigned_cc_user=None, assigned_user=None, begin_time=None, creator=None, custom_fields=None, new_custom_fields=None, developer=None, domain=None, done_ratio=None, end_time=None, expected_work_hours=None, id=None, project=None, iteration=None, module=None, parent_issue=None, priority=None, severity=None, status=None, tracker=None):
        """CreateIssueV4Response

        The model defined in huaweicloud sdk

        :param actual_work_hours: 实际工时
        :type actual_work_hours: float
        :param assigned_cc_user: 抄送人
        :type assigned_cc_user: list[:class:`huaweicloudsdkprojectman.v4.IssueUser`]
        :param assigned_user: 
        :type assigned_user: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        :param begin_time: 开始时间，年-月-日
        :type begin_time: str
        :param creator: 
        :type creator: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        :param custom_fields: 自定义属性值,不建议使用，建议参考new_custom_fields字段
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.CustomField`]
        :param new_custom_fields: 自定义属性值
        :type new_custom_fields: list[:class:`huaweicloudsdkprojectman.v4.NewCustomField`]
        :param developer: 
        :type developer: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        :param domain: 
        :type domain: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4Domain`
        :param done_ratio: 工作项进度值
        :type done_ratio: int
        :param end_time: 结束时间，年-月-日
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
        :param parent_issue: 
        :type parent_issue: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4ParentIssue`
        :param priority: 
        :type priority: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Priority`
        :param severity: 
        :type severity: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Severity`
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Status`
        :param tracker: 
        :type tracker: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4Tracker`
        """
        
        super(CreateIssueV4Response, self).__init__()

        self._actual_work_hours = None
        self._assigned_cc_user = None
        self._assigned_user = None
        self._begin_time = None
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
        self._parent_issue = None
        self._priority = None
        self._severity = None
        self._status = None
        self._tracker = None
        self.discriminator = None

        if actual_work_hours is not None:
            self.actual_work_hours = actual_work_hours
        if assigned_cc_user is not None:
            self.assigned_cc_user = assigned_cc_user
        if assigned_user is not None:
            self.assigned_user = assigned_user
        if begin_time is not None:
            self.begin_time = begin_time
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
        if parent_issue is not None:
            self.parent_issue = parent_issue
        if priority is not None:
            self.priority = priority
        if severity is not None:
            self.severity = severity
        if status is not None:
            self.status = status
        if tracker is not None:
            self.tracker = tracker

    @property
    def actual_work_hours(self):
        """Gets the actual_work_hours of this CreateIssueV4Response.

        实际工时

        :return: The actual_work_hours of this CreateIssueV4Response.
        :rtype: float
        """
        return self._actual_work_hours

    @actual_work_hours.setter
    def actual_work_hours(self, actual_work_hours):
        """Sets the actual_work_hours of this CreateIssueV4Response.

        实际工时

        :param actual_work_hours: The actual_work_hours of this CreateIssueV4Response.
        :type actual_work_hours: float
        """
        self._actual_work_hours = actual_work_hours

    @property
    def assigned_cc_user(self):
        """Gets the assigned_cc_user of this CreateIssueV4Response.

        抄送人

        :return: The assigned_cc_user of this CreateIssueV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueUser`]
        """
        return self._assigned_cc_user

    @assigned_cc_user.setter
    def assigned_cc_user(self, assigned_cc_user):
        """Sets the assigned_cc_user of this CreateIssueV4Response.

        抄送人

        :param assigned_cc_user: The assigned_cc_user of this CreateIssueV4Response.
        :type assigned_cc_user: list[:class:`huaweicloudsdkprojectman.v4.IssueUser`]
        """
        self._assigned_cc_user = assigned_cc_user

    @property
    def assigned_user(self):
        """Gets the assigned_user of this CreateIssueV4Response.


        :return: The assigned_user of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        return self._assigned_user

    @assigned_user.setter
    def assigned_user(self, assigned_user):
        """Sets the assigned_user of this CreateIssueV4Response.


        :param assigned_user: The assigned_user of this CreateIssueV4Response.
        :type assigned_user: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        self._assigned_user = assigned_user

    @property
    def begin_time(self):
        """Gets the begin_time of this CreateIssueV4Response.

        开始时间，年-月-日

        :return: The begin_time of this CreateIssueV4Response.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this CreateIssueV4Response.

        开始时间，年-月-日

        :param begin_time: The begin_time of this CreateIssueV4Response.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def creator(self):
        """Gets the creator of this CreateIssueV4Response.


        :return: The creator of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this CreateIssueV4Response.


        :param creator: The creator of this CreateIssueV4Response.
        :type creator: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        self._creator = creator

    @property
    def custom_fields(self):
        """Gets the custom_fields of this CreateIssueV4Response.

        自定义属性值,不建议使用，建议参考new_custom_fields字段

        :return: The custom_fields of this CreateIssueV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CustomField`]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this CreateIssueV4Response.

        自定义属性值,不建议使用，建议参考new_custom_fields字段

        :param custom_fields: The custom_fields of this CreateIssueV4Response.
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.CustomField`]
        """
        self._custom_fields = custom_fields

    @property
    def new_custom_fields(self):
        """Gets the new_custom_fields of this CreateIssueV4Response.

        自定义属性值

        :return: The new_custom_fields of this CreateIssueV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.NewCustomField`]
        """
        return self._new_custom_fields

    @new_custom_fields.setter
    def new_custom_fields(self, new_custom_fields):
        """Sets the new_custom_fields of this CreateIssueV4Response.

        自定义属性值

        :param new_custom_fields: The new_custom_fields of this CreateIssueV4Response.
        :type new_custom_fields: list[:class:`huaweicloudsdkprojectman.v4.NewCustomField`]
        """
        self._new_custom_fields = new_custom_fields

    @property
    def developer(self):
        """Gets the developer of this CreateIssueV4Response.


        :return: The developer of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        """Sets the developer of this CreateIssueV4Response.


        :param developer: The developer of this CreateIssueV4Response.
        :type developer: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        self._developer = developer

    @property
    def domain(self):
        """Gets the domain of this CreateIssueV4Response.


        :return: The domain of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4Domain`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateIssueV4Response.


        :param domain: The domain of this CreateIssueV4Response.
        :type domain: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4Domain`
        """
        self._domain = domain

    @property
    def done_ratio(self):
        """Gets the done_ratio of this CreateIssueV4Response.

        工作项进度值

        :return: The done_ratio of this CreateIssueV4Response.
        :rtype: int
        """
        return self._done_ratio

    @done_ratio.setter
    def done_ratio(self, done_ratio):
        """Sets the done_ratio of this CreateIssueV4Response.

        工作项进度值

        :param done_ratio: The done_ratio of this CreateIssueV4Response.
        :type done_ratio: int
        """
        self._done_ratio = done_ratio

    @property
    def end_time(self):
        """Gets the end_time of this CreateIssueV4Response.

        结束时间，年-月-日

        :return: The end_time of this CreateIssueV4Response.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CreateIssueV4Response.

        结束时间，年-月-日

        :param end_time: The end_time of this CreateIssueV4Response.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def expected_work_hours(self):
        """Gets the expected_work_hours of this CreateIssueV4Response.

        预计工时

        :return: The expected_work_hours of this CreateIssueV4Response.
        :rtype: float
        """
        return self._expected_work_hours

    @expected_work_hours.setter
    def expected_work_hours(self, expected_work_hours):
        """Sets the expected_work_hours of this CreateIssueV4Response.

        预计工时

        :param expected_work_hours: The expected_work_hours of this CreateIssueV4Response.
        :type expected_work_hours: float
        """
        self._expected_work_hours = expected_work_hours

    @property
    def id(self):
        """Gets the id of this CreateIssueV4Response.

        工作项项id

        :return: The id of this CreateIssueV4Response.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateIssueV4Response.

        工作项项id

        :param id: The id of this CreateIssueV4Response.
        :type id: int
        """
        self._id = id

    @property
    def project(self):
        """Gets the project of this CreateIssueV4Response.


        :return: The project of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueProjectResponseV4`
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this CreateIssueV4Response.


        :param project: The project of this CreateIssueV4Response.
        :type project: :class:`huaweicloudsdkprojectman.v4.IssueProjectResponseV4`
        """
        self._project = project

    @property
    def iteration(self):
        """Gets the iteration of this CreateIssueV4Response.


        :return: The iteration of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Iteration`
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        """Sets the iteration of this CreateIssueV4Response.


        :param iteration: The iteration of this CreateIssueV4Response.
        :type iteration: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Iteration`
        """
        self._iteration = iteration

    @property
    def module(self):
        """Gets the module of this CreateIssueV4Response.


        :return: The module of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Module`
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this CreateIssueV4Response.


        :param module: The module of this CreateIssueV4Response.
        :type module: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Module`
        """
        self._module = module

    @property
    def parent_issue(self):
        """Gets the parent_issue of this CreateIssueV4Response.


        :return: The parent_issue of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4ParentIssue`
        """
        return self._parent_issue

    @parent_issue.setter
    def parent_issue(self, parent_issue):
        """Sets the parent_issue of this CreateIssueV4Response.


        :param parent_issue: The parent_issue of this CreateIssueV4Response.
        :type parent_issue: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4ParentIssue`
        """
        self._parent_issue = parent_issue

    @property
    def priority(self):
        """Gets the priority of this CreateIssueV4Response.


        :return: The priority of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Priority`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateIssueV4Response.


        :param priority: The priority of this CreateIssueV4Response.
        :type priority: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Priority`
        """
        self._priority = priority

    @property
    def severity(self):
        """Gets the severity of this CreateIssueV4Response.


        :return: The severity of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Severity`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this CreateIssueV4Response.


        :param severity: The severity of this CreateIssueV4Response.
        :type severity: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Severity`
        """
        self._severity = severity

    @property
    def status(self):
        """Gets the status of this CreateIssueV4Response.


        :return: The status of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateIssueV4Response.


        :param status: The status of this CreateIssueV4Response.
        :type status: :class:`huaweicloudsdkprojectman.v4.IssueItemSfV4Status`
        """
        self._status = status

    @property
    def tracker(self):
        """Gets the tracker of this CreateIssueV4Response.


        :return: The tracker of this CreateIssueV4Response.
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4Tracker`
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        """Sets the tracker of this CreateIssueV4Response.


        :param tracker: The tracker of this CreateIssueV4Response.
        :type tracker: :class:`huaweicloudsdkprojectman.v4.CreateIssueResponseV4Tracker`
        """
        self._tracker = tracker

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
        if not isinstance(other, CreateIssueV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
