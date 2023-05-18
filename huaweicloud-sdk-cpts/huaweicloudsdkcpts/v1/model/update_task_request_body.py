# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'project_id': 'int',
        'run_status': 'int',
        'run_type': 'int',
        'task_run_info': 'TaskRunInfo',
        'case_list': 'list[CaseInfoDetail]',
        'operate_mode': 'int',
        'bench_concurrent': 'int',
        'related_temp_running_data': 'list[RelatedTempRunningData]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'run_status': 'run_status',
        'run_type': 'run_type',
        'task_run_info': 'task_run_info',
        'case_list': 'case_list',
        'operate_mode': 'operate_mode',
        'bench_concurrent': 'bench_concurrent',
        'related_temp_running_data': 'related_temp_running_data'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, run_status=None, run_type=None, task_run_info=None, case_list=None, operate_mode=None, bench_concurrent=None, related_temp_running_data=None):
        """UpdateTaskRequestBody

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param name: name
        :type name: str
        :param description: description
        :type description: str
        :param project_id: project_id
        :type project_id: int
        :param run_status: run_status
        :type run_status: int
        :param run_type: run_type
        :type run_type: int
        :param task_run_info: 
        :type task_run_info: :class:`huaweicloudsdkcpts.v1.TaskRunInfo`
        :param case_list: case_list
        :type case_list: list[:class:`huaweicloudsdkcpts.v1.CaseInfoDetail`]
        :param operate_mode: operate_mode
        :type operate_mode: int
        :param bench_concurrent: bench_concurrent
        :type bench_concurrent: int
        :param related_temp_running_data: related_temp_running_data
        :type related_temp_running_data: list[:class:`huaweicloudsdkcpts.v1.RelatedTempRunningData`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._run_status = None
        self._run_type = None
        self._task_run_info = None
        self._case_list = None
        self._operate_mode = None
        self._bench_concurrent = None
        self._related_temp_running_data = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.project_id = project_id
        if run_status is not None:
            self.run_status = run_status
        if run_type is not None:
            self.run_type = run_type
        if task_run_info is not None:
            self.task_run_info = task_run_info
        if case_list is not None:
            self.case_list = case_list
        if operate_mode is not None:
            self.operate_mode = operate_mode
        if bench_concurrent is not None:
            self.bench_concurrent = bench_concurrent
        if related_temp_running_data is not None:
            self.related_temp_running_data = related_temp_running_data

    @property
    def id(self):
        """Gets the id of this UpdateTaskRequestBody.

        id

        :return: The id of this UpdateTaskRequestBody.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateTaskRequestBody.

        id

        :param id: The id of this UpdateTaskRequestBody.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateTaskRequestBody.

        name

        :return: The name of this UpdateTaskRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTaskRequestBody.

        name

        :param name: The name of this UpdateTaskRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateTaskRequestBody.

        description

        :return: The description of this UpdateTaskRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTaskRequestBody.

        description

        :param description: The description of this UpdateTaskRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this UpdateTaskRequestBody.

        project_id

        :return: The project_id of this UpdateTaskRequestBody.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateTaskRequestBody.

        project_id

        :param project_id: The project_id of this UpdateTaskRequestBody.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def run_status(self):
        """Gets the run_status of this UpdateTaskRequestBody.

        run_status

        :return: The run_status of this UpdateTaskRequestBody.
        :rtype: int
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """Sets the run_status of this UpdateTaskRequestBody.

        run_status

        :param run_status: The run_status of this UpdateTaskRequestBody.
        :type run_status: int
        """
        self._run_status = run_status

    @property
    def run_type(self):
        """Gets the run_type of this UpdateTaskRequestBody.

        run_type

        :return: The run_type of this UpdateTaskRequestBody.
        :rtype: int
        """
        return self._run_type

    @run_type.setter
    def run_type(self, run_type):
        """Sets the run_type of this UpdateTaskRequestBody.

        run_type

        :param run_type: The run_type of this UpdateTaskRequestBody.
        :type run_type: int
        """
        self._run_type = run_type

    @property
    def task_run_info(self):
        """Gets the task_run_info of this UpdateTaskRequestBody.

        :return: The task_run_info of this UpdateTaskRequestBody.
        :rtype: :class:`huaweicloudsdkcpts.v1.TaskRunInfo`
        """
        return self._task_run_info

    @task_run_info.setter
    def task_run_info(self, task_run_info):
        """Sets the task_run_info of this UpdateTaskRequestBody.

        :param task_run_info: The task_run_info of this UpdateTaskRequestBody.
        :type task_run_info: :class:`huaweicloudsdkcpts.v1.TaskRunInfo`
        """
        self._task_run_info = task_run_info

    @property
    def case_list(self):
        """Gets the case_list of this UpdateTaskRequestBody.

        case_list

        :return: The case_list of this UpdateTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.CaseInfoDetail`]
        """
        return self._case_list

    @case_list.setter
    def case_list(self, case_list):
        """Sets the case_list of this UpdateTaskRequestBody.

        case_list

        :param case_list: The case_list of this UpdateTaskRequestBody.
        :type case_list: list[:class:`huaweicloudsdkcpts.v1.CaseInfoDetail`]
        """
        self._case_list = case_list

    @property
    def operate_mode(self):
        """Gets the operate_mode of this UpdateTaskRequestBody.

        operate_mode

        :return: The operate_mode of this UpdateTaskRequestBody.
        :rtype: int
        """
        return self._operate_mode

    @operate_mode.setter
    def operate_mode(self, operate_mode):
        """Sets the operate_mode of this UpdateTaskRequestBody.

        operate_mode

        :param operate_mode: The operate_mode of this UpdateTaskRequestBody.
        :type operate_mode: int
        """
        self._operate_mode = operate_mode

    @property
    def bench_concurrent(self):
        """Gets the bench_concurrent of this UpdateTaskRequestBody.

        bench_concurrent

        :return: The bench_concurrent of this UpdateTaskRequestBody.
        :rtype: int
        """
        return self._bench_concurrent

    @bench_concurrent.setter
    def bench_concurrent(self, bench_concurrent):
        """Sets the bench_concurrent of this UpdateTaskRequestBody.

        bench_concurrent

        :param bench_concurrent: The bench_concurrent of this UpdateTaskRequestBody.
        :type bench_concurrent: int
        """
        self._bench_concurrent = bench_concurrent

    @property
    def related_temp_running_data(self):
        """Gets the related_temp_running_data of this UpdateTaskRequestBody.

        related_temp_running_data

        :return: The related_temp_running_data of this UpdateTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.RelatedTempRunningData`]
        """
        return self._related_temp_running_data

    @related_temp_running_data.setter
    def related_temp_running_data(self, related_temp_running_data):
        """Sets the related_temp_running_data of this UpdateTaskRequestBody.

        related_temp_running_data

        :param related_temp_running_data: The related_temp_running_data of this UpdateTaskRequestBody.
        :type related_temp_running_data: list[:class:`huaweicloudsdkcpts.v1.RelatedTempRunningData`]
        """
        self._related_temp_running_data = related_temp_running_data

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
        if not isinstance(other, UpdateTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
