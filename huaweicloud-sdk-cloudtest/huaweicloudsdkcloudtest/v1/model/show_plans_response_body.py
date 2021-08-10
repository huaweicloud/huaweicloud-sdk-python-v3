# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPlansResponseBody:


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
        'owner': 'ShowPlansResponseOwner',
        'design_stage': 'ShowPlansResponseDesignStage',
        'execute_stage': 'ShowPlansResponseExecuteStage',
        'report_stage': 'ShowPlansResponseReportStage'
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
        'owner': 'owner',
        'design_stage': 'design_stage',
        'execute_stage': 'execute_stage',
        'report_stage': 'report_stage'
    }

    def __init__(self, plan_id=None, name=None, start_date=None, end_date=None, finish_date=None, project_id=None, current_stage=None, expire_day=None, owner=None, design_stage=None, execute_stage=None, report_stage=None):
        """ShowPlansResponseBody - a model defined in huaweicloud sdk"""
        
        

        self._plan_id = None
        self._name = None
        self._start_date = None
        self._end_date = None
        self._finish_date = None
        self._project_id = None
        self._current_stage = None
        self._expire_day = None
        self._owner = None
        self._design_stage = None
        self._execute_stage = None
        self._report_stage = None
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
        if owner is not None:
            self.owner = owner
        if design_stage is not None:
            self.design_stage = design_stage
        if execute_stage is not None:
            self.execute_stage = execute_stage
        if report_stage is not None:
            self.report_stage = report_stage

    @property
    def plan_id(self):
        """Gets the plan_id of this ShowPlansResponseBody.

        测试计划id

        :return: The plan_id of this ShowPlansResponseBody.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this ShowPlansResponseBody.

        测试计划id

        :param plan_id: The plan_id of this ShowPlansResponseBody.
        :type: str
        """
        self._plan_id = plan_id

    @property
    def name(self):
        """Gets the name of this ShowPlansResponseBody.

        测试计划名称

        :return: The name of this ShowPlansResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowPlansResponseBody.

        测试计划名称

        :param name: The name of this ShowPlansResponseBody.
        :type: str
        """
        self._name = name

    @property
    def start_date(self):
        """Gets the start_date of this ShowPlansResponseBody.

        测试计划开始日期

        :return: The start_date of this ShowPlansResponseBody.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ShowPlansResponseBody.

        测试计划开始日期

        :param start_date: The start_date of this ShowPlansResponseBody.
        :type: date
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ShowPlansResponseBody.

        测试计划截止日期

        :return: The end_date of this ShowPlansResponseBody.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ShowPlansResponseBody.

        测试计划截止日期

        :param end_date: The end_date of this ShowPlansResponseBody.
        :type: date
        """
        self._end_date = end_date

    @property
    def finish_date(self):
        """Gets the finish_date of this ShowPlansResponseBody.

        测试计划实际完成日期（测试计划实际完成指测试计划下所有测试用例处于完成状态）

        :return: The finish_date of this ShowPlansResponseBody.
        :rtype: date
        """
        return self._finish_date

    @finish_date.setter
    def finish_date(self, finish_date):
        """Sets the finish_date of this ShowPlansResponseBody.

        测试计划实际完成日期（测试计划实际完成指测试计划下所有测试用例处于完成状态）

        :param finish_date: The finish_date of this ShowPlansResponseBody.
        :type: date
        """
        self._finish_date = finish_date

    @property
    def project_id(self):
        """Gets the project_id of this ShowPlansResponseBody.

        项目id

        :return: The project_id of this ShowPlansResponseBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowPlansResponseBody.

        项目id

        :param project_id: The project_id of this ShowPlansResponseBody.
        :type: str
        """
        self._project_id = project_id

    @property
    def current_stage(self):
        """Gets the current_stage of this ShowPlansResponseBody.

        当前测试计划所处的阶段

        :return: The current_stage of this ShowPlansResponseBody.
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage):
        """Sets the current_stage of this ShowPlansResponseBody.

        当前测试计划所处的阶段

        :param current_stage: The current_stage of this ShowPlansResponseBody.
        :type: str
        """
        self._current_stage = current_stage

    @property
    def expire_day(self):
        """Gets the expire_day of this ShowPlansResponseBody.

        获取超期时间,正值表示已超期

        :return: The expire_day of this ShowPlansResponseBody.
        :rtype: str
        """
        return self._expire_day

    @expire_day.setter
    def expire_day(self, expire_day):
        """Sets the expire_day of this ShowPlansResponseBody.

        获取超期时间,正值表示已超期

        :param expire_day: The expire_day of this ShowPlansResponseBody.
        :type: str
        """
        self._expire_day = expire_day

    @property
    def owner(self):
        """Gets the owner of this ShowPlansResponseBody.


        :return: The owner of this ShowPlansResponseBody.
        :rtype: ShowPlansResponseOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ShowPlansResponseBody.


        :param owner: The owner of this ShowPlansResponseBody.
        :type: ShowPlansResponseOwner
        """
        self._owner = owner

    @property
    def design_stage(self):
        """Gets the design_stage of this ShowPlansResponseBody.


        :return: The design_stage of this ShowPlansResponseBody.
        :rtype: ShowPlansResponseDesignStage
        """
        return self._design_stage

    @design_stage.setter
    def design_stage(self, design_stage):
        """Sets the design_stage of this ShowPlansResponseBody.


        :param design_stage: The design_stage of this ShowPlansResponseBody.
        :type: ShowPlansResponseDesignStage
        """
        self._design_stage = design_stage

    @property
    def execute_stage(self):
        """Gets the execute_stage of this ShowPlansResponseBody.


        :return: The execute_stage of this ShowPlansResponseBody.
        :rtype: ShowPlansResponseExecuteStage
        """
        return self._execute_stage

    @execute_stage.setter
    def execute_stage(self, execute_stage):
        """Sets the execute_stage of this ShowPlansResponseBody.


        :param execute_stage: The execute_stage of this ShowPlansResponseBody.
        :type: ShowPlansResponseExecuteStage
        """
        self._execute_stage = execute_stage

    @property
    def report_stage(self):
        """Gets the report_stage of this ShowPlansResponseBody.


        :return: The report_stage of this ShowPlansResponseBody.
        :rtype: ShowPlansResponseReportStage
        """
        return self._report_stage

    @report_stage.setter
    def report_stage(self, report_stage):
        """Sets the report_stage of this ShowPlansResponseBody.


        :param report_stage: The report_stage of this ShowPlansResponseBody.
        :type: ShowPlansResponseReportStage
        """
        self._report_stage = report_stage

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
        if not isinstance(other, ShowPlansResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
