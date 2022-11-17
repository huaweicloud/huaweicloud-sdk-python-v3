# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestPlanDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plan_id': 'str',
        'name': 'str',
        'start_date': 'date',
        'end_date': 'date',
        'finish_date': 'date',
        'project_id': 'str',
        'current_stage': 'str',
        'expire_day': 'str',
        'creator': 'TestPlanDetailCreator',
        'owner': 'TestPlanDetailOwner',
        'design_stage': 'TestPlanDetailDesignStage',
        'execute_stage': 'TestPlanDetailExecuteStage',
        'report_stage': 'TestPlanDetailReportStage',
        'iteration': 'NameAndId'
    }

    attribute_map = {
        'plan_id': 'plan_id',
        'name': 'name',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'finish_date': 'finish_date',
        'project_id': 'project_id',
        'current_stage': 'current_stage',
        'expire_day': 'expire_day',
        'creator': 'creator',
        'owner': 'owner',
        'design_stage': 'design_stage',
        'execute_stage': 'execute_stage',
        'report_stage': 'report_stage',
        'iteration': 'iteration'
    }

    def __init__(self, plan_id=None, name=None, start_date=None, end_date=None, finish_date=None, project_id=None, current_stage=None, expire_day=None, creator=None, owner=None, design_stage=None, execute_stage=None, report_stage=None, iteration=None):
        """TestPlanDetail

        The model defined in huaweicloud sdk

        :param plan_id: 测试计划id
        :type plan_id: str
        :param name: 测试计划名称
        :type name: str
        :param start_date: 测试计划开始时间
        :type start_date: date
        :param end_date: 测试计划截止时间
        :type end_date: date
        :param finish_date: 测试计划实际完成时间（测试计划实际完成指测试计划下所有测试用例处于完成状态）
        :type finish_date: date
        :param project_id: 项目id
        :type project_id: str
        :param current_stage: 当前测试计划所处的阶段
        :type current_stage: str
        :param expire_day: 获取超期时间,正值表示已超期
        :type expire_day: str
        :param creator: 
        :type creator: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailCreator`
        :param owner: 
        :type owner: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailOwner`
        :param design_stage: 
        :type design_stage: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailDesignStage`
        :param execute_stage: 
        :type execute_stage: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailExecuteStage`
        :param report_stage: 
        :type report_stage: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailReportStage`
        :param iteration: 
        :type iteration: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        
        

        self._plan_id = None
        self._name = None
        self._start_date = None
        self._end_date = None
        self._finish_date = None
        self._project_id = None
        self._current_stage = None
        self._expire_day = None
        self._creator = None
        self._owner = None
        self._design_stage = None
        self._execute_stage = None
        self._report_stage = None
        self._iteration = None
        self.discriminator = None

        if plan_id is not None:
            self.plan_id = plan_id
        if name is not None:
            self.name = name
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if finish_date is not None:
            self.finish_date = finish_date
        if project_id is not None:
            self.project_id = project_id
        if current_stage is not None:
            self.current_stage = current_stage
        if expire_day is not None:
            self.expire_day = expire_day
        if creator is not None:
            self.creator = creator
        if owner is not None:
            self.owner = owner
        if design_stage is not None:
            self.design_stage = design_stage
        if execute_stage is not None:
            self.execute_stage = execute_stage
        if report_stage is not None:
            self.report_stage = report_stage
        if iteration is not None:
            self.iteration = iteration

    @property
    def plan_id(self):
        """Gets the plan_id of this TestPlanDetail.

        测试计划id

        :return: The plan_id of this TestPlanDetail.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this TestPlanDetail.

        测试计划id

        :param plan_id: The plan_id of this TestPlanDetail.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def name(self):
        """Gets the name of this TestPlanDetail.

        测试计划名称

        :return: The name of this TestPlanDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestPlanDetail.

        测试计划名称

        :param name: The name of this TestPlanDetail.
        :type name: str
        """
        self._name = name

    @property
    def start_date(self):
        """Gets the start_date of this TestPlanDetail.

        测试计划开始时间

        :return: The start_date of this TestPlanDetail.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TestPlanDetail.

        测试计划开始时间

        :param start_date: The start_date of this TestPlanDetail.
        :type start_date: date
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this TestPlanDetail.

        测试计划截止时间

        :return: The end_date of this TestPlanDetail.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TestPlanDetail.

        测试计划截止时间

        :param end_date: The end_date of this TestPlanDetail.
        :type end_date: date
        """
        self._end_date = end_date

    @property
    def finish_date(self):
        """Gets the finish_date of this TestPlanDetail.

        测试计划实际完成时间（测试计划实际完成指测试计划下所有测试用例处于完成状态）

        :return: The finish_date of this TestPlanDetail.
        :rtype: date
        """
        return self._finish_date

    @finish_date.setter
    def finish_date(self, finish_date):
        """Sets the finish_date of this TestPlanDetail.

        测试计划实际完成时间（测试计划实际完成指测试计划下所有测试用例处于完成状态）

        :param finish_date: The finish_date of this TestPlanDetail.
        :type finish_date: date
        """
        self._finish_date = finish_date

    @property
    def project_id(self):
        """Gets the project_id of this TestPlanDetail.

        项目id

        :return: The project_id of this TestPlanDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TestPlanDetail.

        项目id

        :param project_id: The project_id of this TestPlanDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def current_stage(self):
        """Gets the current_stage of this TestPlanDetail.

        当前测试计划所处的阶段

        :return: The current_stage of this TestPlanDetail.
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage):
        """Sets the current_stage of this TestPlanDetail.

        当前测试计划所处的阶段

        :param current_stage: The current_stage of this TestPlanDetail.
        :type current_stage: str
        """
        self._current_stage = current_stage

    @property
    def expire_day(self):
        """Gets the expire_day of this TestPlanDetail.

        获取超期时间,正值表示已超期

        :return: The expire_day of this TestPlanDetail.
        :rtype: str
        """
        return self._expire_day

    @expire_day.setter
    def expire_day(self, expire_day):
        """Sets the expire_day of this TestPlanDetail.

        获取超期时间,正值表示已超期

        :param expire_day: The expire_day of this TestPlanDetail.
        :type expire_day: str
        """
        self._expire_day = expire_day

    @property
    def creator(self):
        """Gets the creator of this TestPlanDetail.

        :return: The creator of this TestPlanDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailCreator`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this TestPlanDetail.

        :param creator: The creator of this TestPlanDetail.
        :type creator: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailCreator`
        """
        self._creator = creator

    @property
    def owner(self):
        """Gets the owner of this TestPlanDetail.

        :return: The owner of this TestPlanDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailOwner`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this TestPlanDetail.

        :param owner: The owner of this TestPlanDetail.
        :type owner: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailOwner`
        """
        self._owner = owner

    @property
    def design_stage(self):
        """Gets the design_stage of this TestPlanDetail.

        :return: The design_stage of this TestPlanDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailDesignStage`
        """
        return self._design_stage

    @design_stage.setter
    def design_stage(self, design_stage):
        """Sets the design_stage of this TestPlanDetail.

        :param design_stage: The design_stage of this TestPlanDetail.
        :type design_stage: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailDesignStage`
        """
        self._design_stage = design_stage

    @property
    def execute_stage(self):
        """Gets the execute_stage of this TestPlanDetail.

        :return: The execute_stage of this TestPlanDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailExecuteStage`
        """
        return self._execute_stage

    @execute_stage.setter
    def execute_stage(self, execute_stage):
        """Sets the execute_stage of this TestPlanDetail.

        :param execute_stage: The execute_stage of this TestPlanDetail.
        :type execute_stage: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailExecuteStage`
        """
        self._execute_stage = execute_stage

    @property
    def report_stage(self):
        """Gets the report_stage of this TestPlanDetail.

        :return: The report_stage of this TestPlanDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailReportStage`
        """
        return self._report_stage

    @report_stage.setter
    def report_stage(self, report_stage):
        """Sets the report_stage of this TestPlanDetail.

        :param report_stage: The report_stage of this TestPlanDetail.
        :type report_stage: :class:`huaweicloudsdkcloudtest.v1.TestPlanDetailReportStage`
        """
        self._report_stage = report_stage

    @property
    def iteration(self):
        """Gets the iteration of this TestPlanDetail.

        :return: The iteration of this TestPlanDetail.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        """Sets the iteration of this TestPlanDetail.

        :param iteration: The iteration of this TestPlanDetail.
        :type iteration: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        self._iteration = iteration

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
        if not isinstance(other, TestPlanDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
