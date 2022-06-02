# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSystemIssueRequestV4:

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
        'assigned_id': 'int',
        'begin_time': 'str',
        'description': 'str',
        'developer_id': 'int',
        'domain_id': 'int',
        'done_ratio': 'int',
        'end_time': 'str',
        'expected_work_hours': 'float',
        'iteration_id': 'int',
        'module_id': 'int',
        'name': 'str',
        'parent_issue_id': 'int',
        'priority_id': 'int',
        'severity_id': 'int',
        'status_id': 'int',
        'tracker_id': 'int',
        'new_custom_fields': 'list[NewCustomField]',
        'creator': 'Creator',
        'custom_fields': 'list[ScrumCustomField]'
    }

    attribute_map = {
        'actual_work_hours': 'actual_work_hours',
        'assigned_id': 'assigned_id',
        'begin_time': 'begin_time',
        'description': 'description',
        'developer_id': 'developer_id',
        'domain_id': 'domain_id',
        'done_ratio': 'done_ratio',
        'end_time': 'end_time',
        'expected_work_hours': 'expected_work_hours',
        'iteration_id': 'iteration_id',
        'module_id': 'module_id',
        'name': 'name',
        'parent_issue_id': 'parent_issue_id',
        'priority_id': 'priority_id',
        'severity_id': 'severity_id',
        'status_id': 'status_id',
        'tracker_id': 'tracker_id',
        'new_custom_fields': 'new_custom_fields',
        'creator': 'creator',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, actual_work_hours=None, assigned_id=None, begin_time=None, description=None, developer_id=None, domain_id=None, done_ratio=None, end_time=None, expected_work_hours=None, iteration_id=None, module_id=None, name=None, parent_issue_id=None, priority_id=None, severity_id=None, status_id=None, tracker_id=None, new_custom_fields=None, creator=None, custom_fields=None):
        """CreateSystemIssueRequestV4

        The model defined in huaweicloud sdk

        :param actual_work_hours: 实际工时
        :type actual_work_hours: float
        :param assigned_id: 处理人id,对应用户信息的数字id
        :type assigned_id: int
        :param begin_time: 开始时间，年-月-日
        :type begin_time: str
        :param description: 描述信息
        :type description: str
        :param developer_id: 开发者id,对应用户信息的数字id
        :type developer_id: int
        :param domain_id: id 领域, 14 &#39;性能&#39;, 15 &#39;功能&#39;, 16 &#39;可靠性&#39; 17 &#39;网络安全&#39; 18 &#39;可维护性&#39; 19 &#39;其他DFX&#39; 20 &#39;可用性&#39;
        :type domain_id: int
        :param done_ratio: 工作项进度值
        :type done_ratio: int
        :param end_time: 结束时间，年-月-日
        :type end_time: str
        :param expected_work_hours: 预计工时
        :type expected_work_hours: float
        :param iteration_id: 迭代id
        :type iteration_id: int
        :param module_id: 模块id
        :type module_id: int
        :param name: 标题
        :type name: str
        :param parent_issue_id: 父工作项的id,创建子工作项时必填，父工作项的类型tracker_id不能为2,3
        :type parent_issue_id: int
        :param priority_id: 优先级,   1 低,   2 中,   3 高,
        :type priority_id: int
        :param severity_id: 重要程度,   10 关键,   11 重要,   12 一般,   13 提示,
        :type severity_id: int
        :param status_id: 状态   id, 新建   1, 进行中 2, 已解决 3, 测试中 4, 已关闭 5, 已拒绝 6,
        :type status_id: int
        :param tracker_id: 工作项类型, 2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story;     5 只能为 6 的父工作项类型;     6 只能为 7 的父工作项类型;     7 只能为 2,3的父;
        :type tracker_id: int
        :param new_custom_fields: 用户自定义字段
        :type new_custom_fields: list[:class:`huaweicloudsdkprojectman.v4.NewCustomField`]
        :param creator: 
        :type creator: :class:`huaweicloudsdkprojectman.v4.Creator`
        :param custom_fields: 用户自定义字段
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.ScrumCustomField`]
        """
        
        

        self._actual_work_hours = None
        self._assigned_id = None
        self._begin_time = None
        self._description = None
        self._developer_id = None
        self._domain_id = None
        self._done_ratio = None
        self._end_time = None
        self._expected_work_hours = None
        self._iteration_id = None
        self._module_id = None
        self._name = None
        self._parent_issue_id = None
        self._priority_id = None
        self._severity_id = None
        self._status_id = None
        self._tracker_id = None
        self._new_custom_fields = None
        self._creator = None
        self._custom_fields = None
        self.discriminator = None

        if actual_work_hours is not None:
            self.actual_work_hours = actual_work_hours
        if assigned_id is not None:
            self.assigned_id = assigned_id
        if begin_time is not None:
            self.begin_time = begin_time
        if description is not None:
            self.description = description
        if developer_id is not None:
            self.developer_id = developer_id
        if domain_id is not None:
            self.domain_id = domain_id
        if done_ratio is not None:
            self.done_ratio = done_ratio
        if end_time is not None:
            self.end_time = end_time
        if expected_work_hours is not None:
            self.expected_work_hours = expected_work_hours
        if iteration_id is not None:
            self.iteration_id = iteration_id
        if module_id is not None:
            self.module_id = module_id
        self.name = name
        if parent_issue_id is not None:
            self.parent_issue_id = parent_issue_id
        self.priority_id = priority_id
        if severity_id is not None:
            self.severity_id = severity_id
        if status_id is not None:
            self.status_id = status_id
        self.tracker_id = tracker_id
        if new_custom_fields is not None:
            self.new_custom_fields = new_custom_fields
        self.creator = creator
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def actual_work_hours(self):
        """Gets the actual_work_hours of this CreateSystemIssueRequestV4.

        实际工时

        :return: The actual_work_hours of this CreateSystemIssueRequestV4.
        :rtype: float
        """
        return self._actual_work_hours

    @actual_work_hours.setter
    def actual_work_hours(self, actual_work_hours):
        """Sets the actual_work_hours of this CreateSystemIssueRequestV4.

        实际工时

        :param actual_work_hours: The actual_work_hours of this CreateSystemIssueRequestV4.
        :type actual_work_hours: float
        """
        self._actual_work_hours = actual_work_hours

    @property
    def assigned_id(self):
        """Gets the assigned_id of this CreateSystemIssueRequestV4.

        处理人id,对应用户信息的数字id

        :return: The assigned_id of this CreateSystemIssueRequestV4.
        :rtype: int
        """
        return self._assigned_id

    @assigned_id.setter
    def assigned_id(self, assigned_id):
        """Sets the assigned_id of this CreateSystemIssueRequestV4.

        处理人id,对应用户信息的数字id

        :param assigned_id: The assigned_id of this CreateSystemIssueRequestV4.
        :type assigned_id: int
        """
        self._assigned_id = assigned_id

    @property
    def begin_time(self):
        """Gets the begin_time of this CreateSystemIssueRequestV4.

        开始时间，年-月-日

        :return: The begin_time of this CreateSystemIssueRequestV4.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this CreateSystemIssueRequestV4.

        开始时间，年-月-日

        :param begin_time: The begin_time of this CreateSystemIssueRequestV4.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def description(self):
        """Gets the description of this CreateSystemIssueRequestV4.

        描述信息

        :return: The description of this CreateSystemIssueRequestV4.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSystemIssueRequestV4.

        描述信息

        :param description: The description of this CreateSystemIssueRequestV4.
        :type description: str
        """
        self._description = description

    @property
    def developer_id(self):
        """Gets the developer_id of this CreateSystemIssueRequestV4.

        开发者id,对应用户信息的数字id

        :return: The developer_id of this CreateSystemIssueRequestV4.
        :rtype: int
        """
        return self._developer_id

    @developer_id.setter
    def developer_id(self, developer_id):
        """Sets the developer_id of this CreateSystemIssueRequestV4.

        开发者id,对应用户信息的数字id

        :param developer_id: The developer_id of this CreateSystemIssueRequestV4.
        :type developer_id: int
        """
        self._developer_id = developer_id

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateSystemIssueRequestV4.

        id 领域, 14 '性能', 15 '功能', 16 '可靠性' 17 '网络安全' 18 '可维护性' 19 '其他DFX' 20 '可用性'

        :return: The domain_id of this CreateSystemIssueRequestV4.
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateSystemIssueRequestV4.

        id 领域, 14 '性能', 15 '功能', 16 '可靠性' 17 '网络安全' 18 '可维护性' 19 '其他DFX' 20 '可用性'

        :param domain_id: The domain_id of this CreateSystemIssueRequestV4.
        :type domain_id: int
        """
        self._domain_id = domain_id

    @property
    def done_ratio(self):
        """Gets the done_ratio of this CreateSystemIssueRequestV4.

        工作项进度值

        :return: The done_ratio of this CreateSystemIssueRequestV4.
        :rtype: int
        """
        return self._done_ratio

    @done_ratio.setter
    def done_ratio(self, done_ratio):
        """Sets the done_ratio of this CreateSystemIssueRequestV4.

        工作项进度值

        :param done_ratio: The done_ratio of this CreateSystemIssueRequestV4.
        :type done_ratio: int
        """
        self._done_ratio = done_ratio

    @property
    def end_time(self):
        """Gets the end_time of this CreateSystemIssueRequestV4.

        结束时间，年-月-日

        :return: The end_time of this CreateSystemIssueRequestV4.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CreateSystemIssueRequestV4.

        结束时间，年-月-日

        :param end_time: The end_time of this CreateSystemIssueRequestV4.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def expected_work_hours(self):
        """Gets the expected_work_hours of this CreateSystemIssueRequestV4.

        预计工时

        :return: The expected_work_hours of this CreateSystemIssueRequestV4.
        :rtype: float
        """
        return self._expected_work_hours

    @expected_work_hours.setter
    def expected_work_hours(self, expected_work_hours):
        """Sets the expected_work_hours of this CreateSystemIssueRequestV4.

        预计工时

        :param expected_work_hours: The expected_work_hours of this CreateSystemIssueRequestV4.
        :type expected_work_hours: float
        """
        self._expected_work_hours = expected_work_hours

    @property
    def iteration_id(self):
        """Gets the iteration_id of this CreateSystemIssueRequestV4.

        迭代id

        :return: The iteration_id of this CreateSystemIssueRequestV4.
        :rtype: int
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        """Sets the iteration_id of this CreateSystemIssueRequestV4.

        迭代id

        :param iteration_id: The iteration_id of this CreateSystemIssueRequestV4.
        :type iteration_id: int
        """
        self._iteration_id = iteration_id

    @property
    def module_id(self):
        """Gets the module_id of this CreateSystemIssueRequestV4.

        模块id

        :return: The module_id of this CreateSystemIssueRequestV4.
        :rtype: int
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this CreateSystemIssueRequestV4.

        模块id

        :param module_id: The module_id of this CreateSystemIssueRequestV4.
        :type module_id: int
        """
        self._module_id = module_id

    @property
    def name(self):
        """Gets the name of this CreateSystemIssueRequestV4.

        标题

        :return: The name of this CreateSystemIssueRequestV4.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSystemIssueRequestV4.

        标题

        :param name: The name of this CreateSystemIssueRequestV4.
        :type name: str
        """
        self._name = name

    @property
    def parent_issue_id(self):
        """Gets the parent_issue_id of this CreateSystemIssueRequestV4.

        父工作项的id,创建子工作项时必填，父工作项的类型tracker_id不能为2,3

        :return: The parent_issue_id of this CreateSystemIssueRequestV4.
        :rtype: int
        """
        return self._parent_issue_id

    @parent_issue_id.setter
    def parent_issue_id(self, parent_issue_id):
        """Sets the parent_issue_id of this CreateSystemIssueRequestV4.

        父工作项的id,创建子工作项时必填，父工作项的类型tracker_id不能为2,3

        :param parent_issue_id: The parent_issue_id of this CreateSystemIssueRequestV4.
        :type parent_issue_id: int
        """
        self._parent_issue_id = parent_issue_id

    @property
    def priority_id(self):
        """Gets the priority_id of this CreateSystemIssueRequestV4.

        优先级,   1 低,   2 中,   3 高,

        :return: The priority_id of this CreateSystemIssueRequestV4.
        :rtype: int
        """
        return self._priority_id

    @priority_id.setter
    def priority_id(self, priority_id):
        """Sets the priority_id of this CreateSystemIssueRequestV4.

        优先级,   1 低,   2 中,   3 高,

        :param priority_id: The priority_id of this CreateSystemIssueRequestV4.
        :type priority_id: int
        """
        self._priority_id = priority_id

    @property
    def severity_id(self):
        """Gets the severity_id of this CreateSystemIssueRequestV4.

        重要程度,   10 关键,   11 重要,   12 一般,   13 提示,

        :return: The severity_id of this CreateSystemIssueRequestV4.
        :rtype: int
        """
        return self._severity_id

    @severity_id.setter
    def severity_id(self, severity_id):
        """Sets the severity_id of this CreateSystemIssueRequestV4.

        重要程度,   10 关键,   11 重要,   12 一般,   13 提示,

        :param severity_id: The severity_id of this CreateSystemIssueRequestV4.
        :type severity_id: int
        """
        self._severity_id = severity_id

    @property
    def status_id(self):
        """Gets the status_id of this CreateSystemIssueRequestV4.

        状态   id, 新建   1, 进行中 2, 已解决 3, 测试中 4, 已关闭 5, 已拒绝 6,

        :return: The status_id of this CreateSystemIssueRequestV4.
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this CreateSystemIssueRequestV4.

        状态   id, 新建   1, 进行中 2, 已解决 3, 测试中 4, 已关闭 5, 已拒绝 6,

        :param status_id: The status_id of this CreateSystemIssueRequestV4.
        :type status_id: int
        """
        self._status_id = status_id

    @property
    def tracker_id(self):
        """Gets the tracker_id of this CreateSystemIssueRequestV4.

        工作项类型, 2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story;     5 只能为 6 的父工作项类型;     6 只能为 7 的父工作项类型;     7 只能为 2,3的父;

        :return: The tracker_id of this CreateSystemIssueRequestV4.
        :rtype: int
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        """Sets the tracker_id of this CreateSystemIssueRequestV4.

        工作项类型, 2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story;     5 只能为 6 的父工作项类型;     6 只能为 7 的父工作项类型;     7 只能为 2,3的父;

        :param tracker_id: The tracker_id of this CreateSystemIssueRequestV4.
        :type tracker_id: int
        """
        self._tracker_id = tracker_id

    @property
    def new_custom_fields(self):
        """Gets the new_custom_fields of this CreateSystemIssueRequestV4.

        用户自定义字段

        :return: The new_custom_fields of this CreateSystemIssueRequestV4.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.NewCustomField`]
        """
        return self._new_custom_fields

    @new_custom_fields.setter
    def new_custom_fields(self, new_custom_fields):
        """Sets the new_custom_fields of this CreateSystemIssueRequestV4.

        用户自定义字段

        :param new_custom_fields: The new_custom_fields of this CreateSystemIssueRequestV4.
        :type new_custom_fields: list[:class:`huaweicloudsdkprojectman.v4.NewCustomField`]
        """
        self._new_custom_fields = new_custom_fields

    @property
    def creator(self):
        """Gets the creator of this CreateSystemIssueRequestV4.


        :return: The creator of this CreateSystemIssueRequestV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.Creator`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this CreateSystemIssueRequestV4.


        :param creator: The creator of this CreateSystemIssueRequestV4.
        :type creator: :class:`huaweicloudsdkprojectman.v4.Creator`
        """
        self._creator = creator

    @property
    def custom_fields(self):
        """Gets the custom_fields of this CreateSystemIssueRequestV4.

        用户自定义字段

        :return: The custom_fields of this CreateSystemIssueRequestV4.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ScrumCustomField`]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this CreateSystemIssueRequestV4.

        用户自定义字段

        :param custom_fields: The custom_fields of this CreateSystemIssueRequestV4.
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.ScrumCustomField`]
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
        if not isinstance(other, CreateSystemIssueRequestV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
