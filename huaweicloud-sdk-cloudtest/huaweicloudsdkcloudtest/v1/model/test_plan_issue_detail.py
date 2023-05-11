# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestPlanIssueDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'plan_id': 'str',
        'workitem_id': 'str',
        'parent_issue': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'name': 'str',
        'region_id': 'str',
        'owner': 'NameAndId',
        'severity': 'NameAndId',
        'status': 'NameAndId',
        'tracker': 'NameAndId',
        'iteration': 'NameAndId',
        'module': 'NameAndId'
    }

    attribute_map = {
        'project_id': 'project_id',
        'plan_id': 'plan_id',
        'workitem_id': 'workitem_id',
        'parent_issue': 'parent_issue',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'name': 'name',
        'region_id': 'region_id',
        'owner': 'owner',
        'severity': 'severity',
        'status': 'status',
        'tracker': 'tracker',
        'iteration': 'iteration',
        'module': 'module'
    }

    def __init__(self, project_id=None, plan_id=None, workitem_id=None, parent_issue=None, start_date=None, end_date=None, name=None, region_id=None, owner=None, severity=None, status=None, tracker=None, iteration=None, module=None):
        """TestPlanIssueDetail

        The model defined in huaweicloud sdk

        :param project_id: 项目id，项目唯一标识，固定长度32位字符
        :type project_id: str
        :param plan_id: 测试计划id
        :type plan_id: str
        :param workitem_id: 工作项id
        :type workitem_id: str
        :param parent_issue: 父工作项
        :type parent_issue: str
        :param start_date: 预计开始日期
        :type start_date: str
        :param end_date: 预计结束日期
        :type end_date: str
        :param name: 工作项名称
        :type name: str
        :param region_id: region信息
        :type region_id: str
        :param owner: 
        :type owner: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        :param severity: 
        :type severity: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        :param status: 
        :type status: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        :param tracker: 
        :type tracker: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        :param iteration: 
        :type iteration: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        :param module: 
        :type module: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        
        

        self._project_id = None
        self._plan_id = None
        self._workitem_id = None
        self._parent_issue = None
        self._start_date = None
        self._end_date = None
        self._name = None
        self._region_id = None
        self._owner = None
        self._severity = None
        self._status = None
        self._tracker = None
        self._iteration = None
        self._module = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if plan_id is not None:
            self.plan_id = plan_id
        if workitem_id is not None:
            self.workitem_id = workitem_id
        if parent_issue is not None:
            self.parent_issue = parent_issue
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if name is not None:
            self.name = name
        if region_id is not None:
            self.region_id = region_id
        if owner is not None:
            self.owner = owner
        if severity is not None:
            self.severity = severity
        if status is not None:
            self.status = status
        if tracker is not None:
            self.tracker = tracker
        if iteration is not None:
            self.iteration = iteration
        if module is not None:
            self.module = module

    @property
    def project_id(self):
        """Gets the project_id of this TestPlanIssueDetail.

        项目id，项目唯一标识，固定长度32位字符

        :return: The project_id of this TestPlanIssueDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TestPlanIssueDetail.

        项目id，项目唯一标识，固定长度32位字符

        :param project_id: The project_id of this TestPlanIssueDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def plan_id(self):
        """Gets the plan_id of this TestPlanIssueDetail.

        测试计划id

        :return: The plan_id of this TestPlanIssueDetail.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this TestPlanIssueDetail.

        测试计划id

        :param plan_id: The plan_id of this TestPlanIssueDetail.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def workitem_id(self):
        """Gets the workitem_id of this TestPlanIssueDetail.

        工作项id

        :return: The workitem_id of this TestPlanIssueDetail.
        :rtype: str
        """
        return self._workitem_id

    @workitem_id.setter
    def workitem_id(self, workitem_id):
        """Sets the workitem_id of this TestPlanIssueDetail.

        工作项id

        :param workitem_id: The workitem_id of this TestPlanIssueDetail.
        :type workitem_id: str
        """
        self._workitem_id = workitem_id

    @property
    def parent_issue(self):
        """Gets the parent_issue of this TestPlanIssueDetail.

        父工作项

        :return: The parent_issue of this TestPlanIssueDetail.
        :rtype: str
        """
        return self._parent_issue

    @parent_issue.setter
    def parent_issue(self, parent_issue):
        """Sets the parent_issue of this TestPlanIssueDetail.

        父工作项

        :param parent_issue: The parent_issue of this TestPlanIssueDetail.
        :type parent_issue: str
        """
        self._parent_issue = parent_issue

    @property
    def start_date(self):
        """Gets the start_date of this TestPlanIssueDetail.

        预计开始日期

        :return: The start_date of this TestPlanIssueDetail.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TestPlanIssueDetail.

        预计开始日期

        :param start_date: The start_date of this TestPlanIssueDetail.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this TestPlanIssueDetail.

        预计结束日期

        :return: The end_date of this TestPlanIssueDetail.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TestPlanIssueDetail.

        预计结束日期

        :param end_date: The end_date of this TestPlanIssueDetail.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def name(self):
        """Gets the name of this TestPlanIssueDetail.

        工作项名称

        :return: The name of this TestPlanIssueDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestPlanIssueDetail.

        工作项名称

        :param name: The name of this TestPlanIssueDetail.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        """Gets the region_id of this TestPlanIssueDetail.

        region信息

        :return: The region_id of this TestPlanIssueDetail.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this TestPlanIssueDetail.

        region信息

        :param region_id: The region_id of this TestPlanIssueDetail.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def owner(self):
        """Gets the owner of this TestPlanIssueDetail.

        :return: The owner of this TestPlanIssueDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this TestPlanIssueDetail.

        :param owner: The owner of this TestPlanIssueDetail.
        :type owner: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        self._owner = owner

    @property
    def severity(self):
        """Gets the severity of this TestPlanIssueDetail.

        :return: The severity of this TestPlanIssueDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this TestPlanIssueDetail.

        :param severity: The severity of this TestPlanIssueDetail.
        :type severity: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        self._severity = severity

    @property
    def status(self):
        """Gets the status of this TestPlanIssueDetail.

        :return: The status of this TestPlanIssueDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TestPlanIssueDetail.

        :param status: The status of this TestPlanIssueDetail.
        :type status: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        self._status = status

    @property
    def tracker(self):
        """Gets the tracker of this TestPlanIssueDetail.

        :return: The tracker of this TestPlanIssueDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        """Sets the tracker of this TestPlanIssueDetail.

        :param tracker: The tracker of this TestPlanIssueDetail.
        :type tracker: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        self._tracker = tracker

    @property
    def iteration(self):
        """Gets the iteration of this TestPlanIssueDetail.

        :return: The iteration of this TestPlanIssueDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        """Sets the iteration of this TestPlanIssueDetail.

        :param iteration: The iteration of this TestPlanIssueDetail.
        :type iteration: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        self._iteration = iteration

    @property
    def module(self):
        """Gets the module of this TestPlanIssueDetail.

        :return: The module of this TestPlanIssueDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this TestPlanIssueDetail.

        :param module: The module of this TestPlanIssueDetail.
        :type module: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        self._module = module

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
        if not isinstance(other, TestPlanIssueDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
