# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Workitems:

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
        'description': 'str',
        'actual_work_hours': 'float',
        'assigned_user': 'WorkitemUser',
        'author': 'WorkitemUser',
        'begin_time': 'str',
        'created_time': 'str',
        'tags': 'list[WorkitemsTags]',
        'developer': 'WorkitemUser',
        'assigned_cc_user': 'list[WorkitemUser]',
        'discover_version': 'str',
        'end_time': 'str',
        'done_ratio': 'str',
        'expected_work_hours': 'float',
        'order': 'str',
        'parent_work_item_id': 'str',
        'release_version': 'str',
        'story_point': 'str',
        'domain': 'WorkitemsDomain',
        'iteration': 'WorkitemsIteration',
        'module': 'WorkitemsModule',
        'priority': 'str',
        'severity': 'str',
        'status': 'WorkitemsStatus',
        'subject': 'str',
        'updated_time': 'str',
        'sequence': 'str',
        'important': 'str',
        'custom_fields': 'list[WorkitemCustomField]'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'actual_work_hours': 'actual_work_hours',
        'assigned_user': 'assigned_user',
        'author': 'author',
        'begin_time': 'begin_time',
        'created_time': 'created_time',
        'tags': 'tags',
        'developer': 'developer',
        'assigned_cc_user': 'assigned_cc_user',
        'discover_version': 'discover_version',
        'end_time': 'end_time',
        'done_ratio': 'done_ratio',
        'expected_work_hours': 'expected_work_hours',
        'order': 'order',
        'parent_work_item_id': 'parent_work_item_id',
        'release_version': 'release_version',
        'story_point': 'story_point',
        'domain': 'domain',
        'iteration': 'iteration',
        'module': 'module',
        'priority': 'priority',
        'severity': 'severity',
        'status': 'status',
        'subject': 'subject',
        'updated_time': 'updated_time',
        'sequence': 'sequence',
        'important': 'important',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, description=None, actual_work_hours=None, assigned_user=None, author=None, begin_time=None, created_time=None, tags=None, developer=None, assigned_cc_user=None, discover_version=None, end_time=None, done_ratio=None, expected_work_hours=None, order=None, parent_work_item_id=None, release_version=None, story_point=None, domain=None, iteration=None, module=None, priority=None, severity=None, status=None, subject=None, updated_time=None, sequence=None, important=None, custom_fields=None):
        r"""Workitems

        The model defined in huaweicloud sdk

        :param id: 工作项id
        :type id: str
        :param description: 工作项描述
        :type description: str
        :param actual_work_hours: 实际工时
        :type actual_work_hours: float
        :param assigned_user: 
        :type assigned_user: :class:`huaweicloudsdkprojectman.v4.WorkitemUser`
        :param author: 
        :type author: :class:`huaweicloudsdkprojectman.v4.WorkitemUser`
        :param begin_time: 工作项开始时间
        :type begin_time: str
        :param created_time: 创建时间
        :type created_time: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkprojectman.v4.WorkitemsTags`]
        :param developer: 
        :type developer: :class:`huaweicloudsdkprojectman.v4.WorkitemUser`
        :param assigned_cc_user: 抄送人
        :type assigned_cc_user: list[:class:`huaweicloudsdkprojectman.v4.WorkitemUser`]
        :param discover_version: 发现问题的版本
        :type discover_version: str
        :param end_time: 工作项结束时间
        :type end_time: str
        :param done_ratio: 工作项进度值
        :type done_ratio: str
        :param expected_work_hours: 预计工时
        :type expected_work_hours: float
        :param order: 顺序
        :type order: str
        :param parent_work_item_id: 父工作项的id
        :type parent_work_item_id: str
        :param release_version: 发布的版本
        :type release_version: str
        :param story_point: 故事点
        :type story_point: str
        :param domain: 
        :type domain: :class:`huaweicloudsdkprojectman.v4.WorkitemsDomain`
        :param iteration: 
        :type iteration: :class:`huaweicloudsdkprojectman.v4.WorkitemsIteration`
        :param module: 
        :type module: :class:`huaweicloudsdkprojectman.v4.WorkitemsModule`
        :param priority: 工作项优先级
        :type priority: str
        :param severity: 严重的程度 \&quot;提示\&quot;, \&quot;一般\&quot;, \&quot;严重\&quot;, \&quot;致命\&quot;
        :type severity: str
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.WorkitemsStatus`
        :param subject: 工作项标题
        :type subject: str
        :param updated_time: 更新时间
        :type updated_time: str
        :param sequence: 工作项编号
        :type sequence: str
        :param important: 重要程度 \&quot;关键\&quot;, \&quot;重要\&quot;, \&quot;一般\&quot;, \&quot;提示\&quot;
        :type important: str
        :param custom_fields: 用户自定义字段
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.WorkitemCustomField`]
        """
        
        

        self._id = None
        self._description = None
        self._actual_work_hours = None
        self._assigned_user = None
        self._author = None
        self._begin_time = None
        self._created_time = None
        self._tags = None
        self._developer = None
        self._assigned_cc_user = None
        self._discover_version = None
        self._end_time = None
        self._done_ratio = None
        self._expected_work_hours = None
        self._order = None
        self._parent_work_item_id = None
        self._release_version = None
        self._story_point = None
        self._domain = None
        self._iteration = None
        self._module = None
        self._priority = None
        self._severity = None
        self._status = None
        self._subject = None
        self._updated_time = None
        self._sequence = None
        self._important = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if actual_work_hours is not None:
            self.actual_work_hours = actual_work_hours
        if assigned_user is not None:
            self.assigned_user = assigned_user
        if author is not None:
            self.author = author
        if begin_time is not None:
            self.begin_time = begin_time
        if created_time is not None:
            self.created_time = created_time
        if tags is not None:
            self.tags = tags
        if developer is not None:
            self.developer = developer
        if assigned_cc_user is not None:
            self.assigned_cc_user = assigned_cc_user
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
        if parent_work_item_id is not None:
            self.parent_work_item_id = parent_work_item_id
        if release_version is not None:
            self.release_version = release_version
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
        if subject is not None:
            self.subject = subject
        if updated_time is not None:
            self.updated_time = updated_time
        if sequence is not None:
            self.sequence = sequence
        if important is not None:
            self.important = important
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        r"""Gets the id of this Workitems.

        工作项id

        :return: The id of this Workitems.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Workitems.

        工作项id

        :param id: The id of this Workitems.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this Workitems.

        工作项描述

        :return: The description of this Workitems.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Workitems.

        工作项描述

        :param description: The description of this Workitems.
        :type description: str
        """
        self._description = description

    @property
    def actual_work_hours(self):
        r"""Gets the actual_work_hours of this Workitems.

        实际工时

        :return: The actual_work_hours of this Workitems.
        :rtype: float
        """
        return self._actual_work_hours

    @actual_work_hours.setter
    def actual_work_hours(self, actual_work_hours):
        r"""Sets the actual_work_hours of this Workitems.

        实际工时

        :param actual_work_hours: The actual_work_hours of this Workitems.
        :type actual_work_hours: float
        """
        self._actual_work_hours = actual_work_hours

    @property
    def assigned_user(self):
        r"""Gets the assigned_user of this Workitems.

        :return: The assigned_user of this Workitems.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkitemUser`
        """
        return self._assigned_user

    @assigned_user.setter
    def assigned_user(self, assigned_user):
        r"""Sets the assigned_user of this Workitems.

        :param assigned_user: The assigned_user of this Workitems.
        :type assigned_user: :class:`huaweicloudsdkprojectman.v4.WorkitemUser`
        """
        self._assigned_user = assigned_user

    @property
    def author(self):
        r"""Gets the author of this Workitems.

        :return: The author of this Workitems.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkitemUser`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this Workitems.

        :param author: The author of this Workitems.
        :type author: :class:`huaweicloudsdkprojectman.v4.WorkitemUser`
        """
        self._author = author

    @property
    def begin_time(self):
        r"""Gets the begin_time of this Workitems.

        工作项开始时间

        :return: The begin_time of this Workitems.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this Workitems.

        工作项开始时间

        :param begin_time: The begin_time of this Workitems.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def created_time(self):
        r"""Gets the created_time of this Workitems.

        创建时间

        :return: The created_time of this Workitems.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this Workitems.

        创建时间

        :param created_time: The created_time of this Workitems.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def tags(self):
        r"""Gets the tags of this Workitems.

        标签

        :return: The tags of this Workitems.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkitemsTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Workitems.

        标签

        :param tags: The tags of this Workitems.
        :type tags: list[:class:`huaweicloudsdkprojectman.v4.WorkitemsTags`]
        """
        self._tags = tags

    @property
    def developer(self):
        r"""Gets the developer of this Workitems.

        :return: The developer of this Workitems.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkitemUser`
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        r"""Sets the developer of this Workitems.

        :param developer: The developer of this Workitems.
        :type developer: :class:`huaweicloudsdkprojectman.v4.WorkitemUser`
        """
        self._developer = developer

    @property
    def assigned_cc_user(self):
        r"""Gets the assigned_cc_user of this Workitems.

        抄送人

        :return: The assigned_cc_user of this Workitems.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkitemUser`]
        """
        return self._assigned_cc_user

    @assigned_cc_user.setter
    def assigned_cc_user(self, assigned_cc_user):
        r"""Sets the assigned_cc_user of this Workitems.

        抄送人

        :param assigned_cc_user: The assigned_cc_user of this Workitems.
        :type assigned_cc_user: list[:class:`huaweicloudsdkprojectman.v4.WorkitemUser`]
        """
        self._assigned_cc_user = assigned_cc_user

    @property
    def discover_version(self):
        r"""Gets the discover_version of this Workitems.

        发现问题的版本

        :return: The discover_version of this Workitems.
        :rtype: str
        """
        return self._discover_version

    @discover_version.setter
    def discover_version(self, discover_version):
        r"""Sets the discover_version of this Workitems.

        发现问题的版本

        :param discover_version: The discover_version of this Workitems.
        :type discover_version: str
        """
        self._discover_version = discover_version

    @property
    def end_time(self):
        r"""Gets the end_time of this Workitems.

        工作项结束时间

        :return: The end_time of this Workitems.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this Workitems.

        工作项结束时间

        :param end_time: The end_time of this Workitems.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def done_ratio(self):
        r"""Gets the done_ratio of this Workitems.

        工作项进度值

        :return: The done_ratio of this Workitems.
        :rtype: str
        """
        return self._done_ratio

    @done_ratio.setter
    def done_ratio(self, done_ratio):
        r"""Sets the done_ratio of this Workitems.

        工作项进度值

        :param done_ratio: The done_ratio of this Workitems.
        :type done_ratio: str
        """
        self._done_ratio = done_ratio

    @property
    def expected_work_hours(self):
        r"""Gets the expected_work_hours of this Workitems.

        预计工时

        :return: The expected_work_hours of this Workitems.
        :rtype: float
        """
        return self._expected_work_hours

    @expected_work_hours.setter
    def expected_work_hours(self, expected_work_hours):
        r"""Sets the expected_work_hours of this Workitems.

        预计工时

        :param expected_work_hours: The expected_work_hours of this Workitems.
        :type expected_work_hours: float
        """
        self._expected_work_hours = expected_work_hours

    @property
    def order(self):
        r"""Gets the order of this Workitems.

        顺序

        :return: The order of this Workitems.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this Workitems.

        顺序

        :param order: The order of this Workitems.
        :type order: str
        """
        self._order = order

    @property
    def parent_work_item_id(self):
        r"""Gets the parent_work_item_id of this Workitems.

        父工作项的id

        :return: The parent_work_item_id of this Workitems.
        :rtype: str
        """
        return self._parent_work_item_id

    @parent_work_item_id.setter
    def parent_work_item_id(self, parent_work_item_id):
        r"""Sets the parent_work_item_id of this Workitems.

        父工作项的id

        :param parent_work_item_id: The parent_work_item_id of this Workitems.
        :type parent_work_item_id: str
        """
        self._parent_work_item_id = parent_work_item_id

    @property
    def release_version(self):
        r"""Gets the release_version of this Workitems.

        发布的版本

        :return: The release_version of this Workitems.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        r"""Sets the release_version of this Workitems.

        发布的版本

        :param release_version: The release_version of this Workitems.
        :type release_version: str
        """
        self._release_version = release_version

    @property
    def story_point(self):
        r"""Gets the story_point of this Workitems.

        故事点

        :return: The story_point of this Workitems.
        :rtype: str
        """
        return self._story_point

    @story_point.setter
    def story_point(self, story_point):
        r"""Sets the story_point of this Workitems.

        故事点

        :param story_point: The story_point of this Workitems.
        :type story_point: str
        """
        self._story_point = story_point

    @property
    def domain(self):
        r"""Gets the domain of this Workitems.

        :return: The domain of this Workitems.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkitemsDomain`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this Workitems.

        :param domain: The domain of this Workitems.
        :type domain: :class:`huaweicloudsdkprojectman.v4.WorkitemsDomain`
        """
        self._domain = domain

    @property
    def iteration(self):
        r"""Gets the iteration of this Workitems.

        :return: The iteration of this Workitems.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkitemsIteration`
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        r"""Sets the iteration of this Workitems.

        :param iteration: The iteration of this Workitems.
        :type iteration: :class:`huaweicloudsdkprojectman.v4.WorkitemsIteration`
        """
        self._iteration = iteration

    @property
    def module(self):
        r"""Gets the module of this Workitems.

        :return: The module of this Workitems.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkitemsModule`
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this Workitems.

        :param module: The module of this Workitems.
        :type module: :class:`huaweicloudsdkprojectman.v4.WorkitemsModule`
        """
        self._module = module

    @property
    def priority(self):
        r"""Gets the priority of this Workitems.

        工作项优先级

        :return: The priority of this Workitems.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this Workitems.

        工作项优先级

        :param priority: The priority of this Workitems.
        :type priority: str
        """
        self._priority = priority

    @property
    def severity(self):
        r"""Gets the severity of this Workitems.

        严重的程度 \"提示\", \"一般\", \"严重\", \"致命\"

        :return: The severity of this Workitems.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this Workitems.

        严重的程度 \"提示\", \"一般\", \"严重\", \"致命\"

        :param severity: The severity of this Workitems.
        :type severity: str
        """
        self._severity = severity

    @property
    def status(self):
        r"""Gets the status of this Workitems.

        :return: The status of this Workitems.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkitemsStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Workitems.

        :param status: The status of this Workitems.
        :type status: :class:`huaweicloudsdkprojectman.v4.WorkitemsStatus`
        """
        self._status = status

    @property
    def subject(self):
        r"""Gets the subject of this Workitems.

        工作项标题

        :return: The subject of this Workitems.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this Workitems.

        工作项标题

        :param subject: The subject of this Workitems.
        :type subject: str
        """
        self._subject = subject

    @property
    def updated_time(self):
        r"""Gets the updated_time of this Workitems.

        更新时间

        :return: The updated_time of this Workitems.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this Workitems.

        更新时间

        :param updated_time: The updated_time of this Workitems.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def sequence(self):
        r"""Gets the sequence of this Workitems.

        工作项编号

        :return: The sequence of this Workitems.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this Workitems.

        工作项编号

        :param sequence: The sequence of this Workitems.
        :type sequence: str
        """
        self._sequence = sequence

    @property
    def important(self):
        r"""Gets the important of this Workitems.

        重要程度 \"关键\", \"重要\", \"一般\", \"提示\"

        :return: The important of this Workitems.
        :rtype: str
        """
        return self._important

    @important.setter
    def important(self, important):
        r"""Sets the important of this Workitems.

        重要程度 \"关键\", \"重要\", \"一般\", \"提示\"

        :param important: The important of this Workitems.
        :type important: str
        """
        self._important = important

    @property
    def custom_fields(self):
        r"""Gets the custom_fields of this Workitems.

        用户自定义字段

        :return: The custom_fields of this Workitems.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkitemCustomField`]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        r"""Sets the custom_fields of this Workitems.

        用户自定义字段

        :param custom_fields: The custom_fields of this Workitems.
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.WorkitemCustomField`]
        """
        self._custom_fields = custom_fields

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
        if not isinstance(other, Workitems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
