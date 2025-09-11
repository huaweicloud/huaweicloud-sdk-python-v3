# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIpdProjectIssueRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'description': 'str',
        'status': 'str',
        'src_domain': 'str',
        'submitted_by': 'str',
        'domain_id': 'str',
        'recipient': 'list[str]',
        'expect_delivery_time': 'int',
        'priority': 'str',
        'assigned_cc': 'list[str]',
        'category': 'str',
        'assignee': 'str',
        'plan_pi': 'str',
        'plan_iteration': 'str',
        'plan_start_date': 'int',
        'plan_end_date': 'int',
        'workload_man_day': 'int',
        'business_domain': 'str',
        'need_break': 'str'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'status': 'status',
        'src_domain': 'src_domain',
        'submitted_by': 'submitted_by',
        'domain_id': 'domain_id',
        'recipient': 'recipient',
        'expect_delivery_time': 'expect_delivery_time',
        'priority': 'priority',
        'assigned_cc': 'assigned_cc',
        'category': 'category',
        'assignee': 'assignee',
        'plan_pi': 'plan_pi',
        'plan_iteration': 'plan_iteration',
        'plan_start_date': 'plan_start_date',
        'plan_end_date': 'plan_end_date',
        'workload_man_day': 'workload_man_day',
        'business_domain': 'business_domain',
        'need_break': 'need_break'
    }

    def __init__(self, title=None, description=None, status=None, src_domain=None, submitted_by=None, domain_id=None, recipient=None, expect_delivery_time=None, priority=None, assigned_cc=None, category=None, assignee=None, plan_pi=None, plan_iteration=None, plan_start_date=None, plan_end_date=None, workload_man_day=None, business_domain=None, need_break=None):
        r"""CreateIpdProjectIssueRequestBody

        The model defined in huaweicloud sdk

        :param title: 工作项名称
        :type title: str
        :param description: 描述信息
        :type description: str
        :param status: 状态[\&quot;Committed\&quot;, \&quot;Analyse\&quot;, \&quot;ToBeConfirmed\&quot;, \&quot;Plan\&quot;, \&quot;Doing\&quot;, \&quot;Delivered\&quot;, \&quot;Checking\&quot;]
        :type status: str
        :param src_domain: 提出项目domainId
        :type src_domain: str
        :param submitted_by: 提交人Id
        :type submitted_by: str
        :param domain_id: 归属项目domainId
        :type domain_id: str
        :param recipient: 承接人id
        :type recipient: list[str]
        :param expect_delivery_time: 期望完成时间
        :type expect_delivery_time: int
        :param priority: 优先级
        :type priority: str
        :param assigned_cc: 抄送人id
        :type assigned_cc: list[str]
        :param category: 工作项分类：[Epic,FE,IR,RR,SR,US,AR,Bug,Task]
        :type category: str
        :param assignee: 责任人
        :type assignee: str
        :param plan_pi: PI ID
        :type plan_pi: str
        :param plan_iteration: 迭代ID
        :type plan_iteration: str
        :param plan_start_date: 计划开始时间
        :type plan_start_date: int
        :param plan_end_date: 计划结束时间
        :type plan_end_date: int
        :param workload_man_day: 计划工时
        :type workload_man_day: int
        :param business_domain: 领域
        :type business_domain: str
        :param need_break: 是否需要分解
        :type need_break: str
        """
        
        

        self._title = None
        self._description = None
        self._status = None
        self._src_domain = None
        self._submitted_by = None
        self._domain_id = None
        self._recipient = None
        self._expect_delivery_time = None
        self._priority = None
        self._assigned_cc = None
        self._category = None
        self._assignee = None
        self._plan_pi = None
        self._plan_iteration = None
        self._plan_start_date = None
        self._plan_end_date = None
        self._workload_man_day = None
        self._business_domain = None
        self._need_break = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if src_domain is not None:
            self.src_domain = src_domain
        if submitted_by is not None:
            self.submitted_by = submitted_by
        if domain_id is not None:
            self.domain_id = domain_id
        if recipient is not None:
            self.recipient = recipient
        if expect_delivery_time is not None:
            self.expect_delivery_time = expect_delivery_time
        if priority is not None:
            self.priority = priority
        if assigned_cc is not None:
            self.assigned_cc = assigned_cc
        if category is not None:
            self.category = category
        if assignee is not None:
            self.assignee = assignee
        if plan_pi is not None:
            self.plan_pi = plan_pi
        if plan_iteration is not None:
            self.plan_iteration = plan_iteration
        if plan_start_date is not None:
            self.plan_start_date = plan_start_date
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if workload_man_day is not None:
            self.workload_man_day = workload_man_day
        if business_domain is not None:
            self.business_domain = business_domain
        if need_break is not None:
            self.need_break = need_break

    @property
    def title(self):
        r"""Gets the title of this CreateIpdProjectIssueRequestBody.

        工作项名称

        :return: The title of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateIpdProjectIssueRequestBody.

        工作项名称

        :param title: The title of this CreateIpdProjectIssueRequestBody.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this CreateIpdProjectIssueRequestBody.

        描述信息

        :return: The description of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateIpdProjectIssueRequestBody.

        描述信息

        :param description: The description of this CreateIpdProjectIssueRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CreateIpdProjectIssueRequestBody.

        状态[\"Committed\", \"Analyse\", \"ToBeConfirmed\", \"Plan\", \"Doing\", \"Delivered\", \"Checking\"]

        :return: The status of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateIpdProjectIssueRequestBody.

        状态[\"Committed\", \"Analyse\", \"ToBeConfirmed\", \"Plan\", \"Doing\", \"Delivered\", \"Checking\"]

        :param status: The status of this CreateIpdProjectIssueRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def src_domain(self):
        r"""Gets the src_domain of this CreateIpdProjectIssueRequestBody.

        提出项目domainId

        :return: The src_domain of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._src_domain

    @src_domain.setter
    def src_domain(self, src_domain):
        r"""Sets the src_domain of this CreateIpdProjectIssueRequestBody.

        提出项目domainId

        :param src_domain: The src_domain of this CreateIpdProjectIssueRequestBody.
        :type src_domain: str
        """
        self._src_domain = src_domain

    @property
    def submitted_by(self):
        r"""Gets the submitted_by of this CreateIpdProjectIssueRequestBody.

        提交人Id

        :return: The submitted_by of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._submitted_by

    @submitted_by.setter
    def submitted_by(self, submitted_by):
        r"""Sets the submitted_by of this CreateIpdProjectIssueRequestBody.

        提交人Id

        :param submitted_by: The submitted_by of this CreateIpdProjectIssueRequestBody.
        :type submitted_by: str
        """
        self._submitted_by = submitted_by

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateIpdProjectIssueRequestBody.

        归属项目domainId

        :return: The domain_id of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateIpdProjectIssueRequestBody.

        归属项目domainId

        :param domain_id: The domain_id of this CreateIpdProjectIssueRequestBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def recipient(self):
        r"""Gets the recipient of this CreateIpdProjectIssueRequestBody.

        承接人id

        :return: The recipient of this CreateIpdProjectIssueRequestBody.
        :rtype: list[str]
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        r"""Sets the recipient of this CreateIpdProjectIssueRequestBody.

        承接人id

        :param recipient: The recipient of this CreateIpdProjectIssueRequestBody.
        :type recipient: list[str]
        """
        self._recipient = recipient

    @property
    def expect_delivery_time(self):
        r"""Gets the expect_delivery_time of this CreateIpdProjectIssueRequestBody.

        期望完成时间

        :return: The expect_delivery_time of this CreateIpdProjectIssueRequestBody.
        :rtype: int
        """
        return self._expect_delivery_time

    @expect_delivery_time.setter
    def expect_delivery_time(self, expect_delivery_time):
        r"""Sets the expect_delivery_time of this CreateIpdProjectIssueRequestBody.

        期望完成时间

        :param expect_delivery_time: The expect_delivery_time of this CreateIpdProjectIssueRequestBody.
        :type expect_delivery_time: int
        """
        self._expect_delivery_time = expect_delivery_time

    @property
    def priority(self):
        r"""Gets the priority of this CreateIpdProjectIssueRequestBody.

        优先级

        :return: The priority of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this CreateIpdProjectIssueRequestBody.

        优先级

        :param priority: The priority of this CreateIpdProjectIssueRequestBody.
        :type priority: str
        """
        self._priority = priority

    @property
    def assigned_cc(self):
        r"""Gets the assigned_cc of this CreateIpdProjectIssueRequestBody.

        抄送人id

        :return: The assigned_cc of this CreateIpdProjectIssueRequestBody.
        :rtype: list[str]
        """
        return self._assigned_cc

    @assigned_cc.setter
    def assigned_cc(self, assigned_cc):
        r"""Sets the assigned_cc of this CreateIpdProjectIssueRequestBody.

        抄送人id

        :param assigned_cc: The assigned_cc of this CreateIpdProjectIssueRequestBody.
        :type assigned_cc: list[str]
        """
        self._assigned_cc = assigned_cc

    @property
    def category(self):
        r"""Gets the category of this CreateIpdProjectIssueRequestBody.

        工作项分类：[Epic,FE,IR,RR,SR,US,AR,Bug,Task]

        :return: The category of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateIpdProjectIssueRequestBody.

        工作项分类：[Epic,FE,IR,RR,SR,US,AR,Bug,Task]

        :param category: The category of this CreateIpdProjectIssueRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def assignee(self):
        r"""Gets the assignee of this CreateIpdProjectIssueRequestBody.

        责任人

        :return: The assignee of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this CreateIpdProjectIssueRequestBody.

        责任人

        :param assignee: The assignee of this CreateIpdProjectIssueRequestBody.
        :type assignee: str
        """
        self._assignee = assignee

    @property
    def plan_pi(self):
        r"""Gets the plan_pi of this CreateIpdProjectIssueRequestBody.

        PI ID

        :return: The plan_pi of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._plan_pi

    @plan_pi.setter
    def plan_pi(self, plan_pi):
        r"""Sets the plan_pi of this CreateIpdProjectIssueRequestBody.

        PI ID

        :param plan_pi: The plan_pi of this CreateIpdProjectIssueRequestBody.
        :type plan_pi: str
        """
        self._plan_pi = plan_pi

    @property
    def plan_iteration(self):
        r"""Gets the plan_iteration of this CreateIpdProjectIssueRequestBody.

        迭代ID

        :return: The plan_iteration of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._plan_iteration

    @plan_iteration.setter
    def plan_iteration(self, plan_iteration):
        r"""Sets the plan_iteration of this CreateIpdProjectIssueRequestBody.

        迭代ID

        :param plan_iteration: The plan_iteration of this CreateIpdProjectIssueRequestBody.
        :type plan_iteration: str
        """
        self._plan_iteration = plan_iteration

    @property
    def plan_start_date(self):
        r"""Gets the plan_start_date of this CreateIpdProjectIssueRequestBody.

        计划开始时间

        :return: The plan_start_date of this CreateIpdProjectIssueRequestBody.
        :rtype: int
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        r"""Sets the plan_start_date of this CreateIpdProjectIssueRequestBody.

        计划开始时间

        :param plan_start_date: The plan_start_date of this CreateIpdProjectIssueRequestBody.
        :type plan_start_date: int
        """
        self._plan_start_date = plan_start_date

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this CreateIpdProjectIssueRequestBody.

        计划结束时间

        :return: The plan_end_date of this CreateIpdProjectIssueRequestBody.
        :rtype: int
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this CreateIpdProjectIssueRequestBody.

        计划结束时间

        :param plan_end_date: The plan_end_date of this CreateIpdProjectIssueRequestBody.
        :type plan_end_date: int
        """
        self._plan_end_date = plan_end_date

    @property
    def workload_man_day(self):
        r"""Gets the workload_man_day of this CreateIpdProjectIssueRequestBody.

        计划工时

        :return: The workload_man_day of this CreateIpdProjectIssueRequestBody.
        :rtype: int
        """
        return self._workload_man_day

    @workload_man_day.setter
    def workload_man_day(self, workload_man_day):
        r"""Sets the workload_man_day of this CreateIpdProjectIssueRequestBody.

        计划工时

        :param workload_man_day: The workload_man_day of this CreateIpdProjectIssueRequestBody.
        :type workload_man_day: int
        """
        self._workload_man_day = workload_man_day

    @property
    def business_domain(self):
        r"""Gets the business_domain of this CreateIpdProjectIssueRequestBody.

        领域

        :return: The business_domain of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._business_domain

    @business_domain.setter
    def business_domain(self, business_domain):
        r"""Sets the business_domain of this CreateIpdProjectIssueRequestBody.

        领域

        :param business_domain: The business_domain of this CreateIpdProjectIssueRequestBody.
        :type business_domain: str
        """
        self._business_domain = business_domain

    @property
    def need_break(self):
        r"""Gets the need_break of this CreateIpdProjectIssueRequestBody.

        是否需要分解

        :return: The need_break of this CreateIpdProjectIssueRequestBody.
        :rtype: str
        """
        return self._need_break

    @need_break.setter
    def need_break(self, need_break):
        r"""Sets the need_break of this CreateIpdProjectIssueRequestBody.

        是否需要分解

        :param need_break: The need_break of this CreateIpdProjectIssueRequestBody.
        :type need_break: str
        """
        self._need_break = need_break

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
        if not isinstance(other, CreateIpdProjectIssueRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
