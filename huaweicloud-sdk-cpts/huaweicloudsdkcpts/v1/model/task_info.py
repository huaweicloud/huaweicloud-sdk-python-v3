# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bench_concurrent': 'int',
        'case_list': 'list[CaseInfo]',
        'create_time': 'datetime',
        'description': 'str',
        'name': 'str',
        'operate_mode': 'int',
        'project_id': 'int',
        'related_temp_running_data': 'list[RelatedTempRunningData]',
        'run_status': 'int',
        'update_time': 'str',
        'parallel': 'bool'
    }

    attribute_map = {
        'bench_concurrent': 'bench_concurrent',
        'case_list': 'case_list',
        'create_time': 'create_time',
        'description': 'description',
        'name': 'name',
        'operate_mode': 'operate_mode',
        'project_id': 'project_id',
        'related_temp_running_data': 'related_temp_running_data',
        'run_status': 'run_status',
        'update_time': 'update_time',
        'parallel': 'parallel'
    }

    def __init__(self, bench_concurrent=None, case_list=None, create_time=None, description=None, name=None, operate_mode=None, project_id=None, related_temp_running_data=None, run_status=None, update_time=None, parallel=None):
        """TaskInfo

        The model defined in huaweicloud sdk

        :param bench_concurrent: bench_concurrent
        :type bench_concurrent: int
        :param case_list: case_list
        :type case_list: list[:class:`huaweicloudsdkcpts.v1.CaseInfo`]
        :param create_time: 创建时间
        :type create_time: datetime
        :param description: description
        :type description: str
        :param name: name
        :type name: str
        :param operate_mode: operate_mode
        :type operate_mode: int
        :param project_id: project_id
        :type project_id: int
        :param related_temp_running_data: related_temp_running_data
        :type related_temp_running_data: list[:class:`huaweicloudsdkcpts.v1.RelatedTempRunningData`]
        :param run_status: run_status
        :type run_status: int
        :param update_time: update_time
        :type update_time: str
        :param parallel: parallel
        :type parallel: bool
        """
        
        

        self._bench_concurrent = None
        self._case_list = None
        self._create_time = None
        self._description = None
        self._name = None
        self._operate_mode = None
        self._project_id = None
        self._related_temp_running_data = None
        self._run_status = None
        self._update_time = None
        self._parallel = None
        self.discriminator = None

        if bench_concurrent is not None:
            self.bench_concurrent = bench_concurrent
        if case_list is not None:
            self.case_list = case_list
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if operate_mode is not None:
            self.operate_mode = operate_mode
        if project_id is not None:
            self.project_id = project_id
        if related_temp_running_data is not None:
            self.related_temp_running_data = related_temp_running_data
        if run_status is not None:
            self.run_status = run_status
        if update_time is not None:
            self.update_time = update_time
        if parallel is not None:
            self.parallel = parallel

    @property
    def bench_concurrent(self):
        """Gets the bench_concurrent of this TaskInfo.

        bench_concurrent

        :return: The bench_concurrent of this TaskInfo.
        :rtype: int
        """
        return self._bench_concurrent

    @bench_concurrent.setter
    def bench_concurrent(self, bench_concurrent):
        """Sets the bench_concurrent of this TaskInfo.

        bench_concurrent

        :param bench_concurrent: The bench_concurrent of this TaskInfo.
        :type bench_concurrent: int
        """
        self._bench_concurrent = bench_concurrent

    @property
    def case_list(self):
        """Gets the case_list of this TaskInfo.

        case_list

        :return: The case_list of this TaskInfo.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.CaseInfo`]
        """
        return self._case_list

    @case_list.setter
    def case_list(self, case_list):
        """Sets the case_list of this TaskInfo.

        case_list

        :param case_list: The case_list of this TaskInfo.
        :type case_list: list[:class:`huaweicloudsdkcpts.v1.CaseInfo`]
        """
        self._case_list = case_list

    @property
    def create_time(self):
        """Gets the create_time of this TaskInfo.

        创建时间

        :return: The create_time of this TaskInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TaskInfo.

        创建时间

        :param create_time: The create_time of this TaskInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this TaskInfo.

        description

        :return: The description of this TaskInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskInfo.

        description

        :param description: The description of this TaskInfo.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this TaskInfo.

        name

        :return: The name of this TaskInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskInfo.

        name

        :param name: The name of this TaskInfo.
        :type name: str
        """
        self._name = name

    @property
    def operate_mode(self):
        """Gets the operate_mode of this TaskInfo.

        operate_mode

        :return: The operate_mode of this TaskInfo.
        :rtype: int
        """
        return self._operate_mode

    @operate_mode.setter
    def operate_mode(self, operate_mode):
        """Sets the operate_mode of this TaskInfo.

        operate_mode

        :param operate_mode: The operate_mode of this TaskInfo.
        :type operate_mode: int
        """
        self._operate_mode = operate_mode

    @property
    def project_id(self):
        """Gets the project_id of this TaskInfo.

        project_id

        :return: The project_id of this TaskInfo.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TaskInfo.

        project_id

        :param project_id: The project_id of this TaskInfo.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def related_temp_running_data(self):
        """Gets the related_temp_running_data of this TaskInfo.

        related_temp_running_data

        :return: The related_temp_running_data of this TaskInfo.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.RelatedTempRunningData`]
        """
        return self._related_temp_running_data

    @related_temp_running_data.setter
    def related_temp_running_data(self, related_temp_running_data):
        """Sets the related_temp_running_data of this TaskInfo.

        related_temp_running_data

        :param related_temp_running_data: The related_temp_running_data of this TaskInfo.
        :type related_temp_running_data: list[:class:`huaweicloudsdkcpts.v1.RelatedTempRunningData`]
        """
        self._related_temp_running_data = related_temp_running_data

    @property
    def run_status(self):
        """Gets the run_status of this TaskInfo.

        run_status

        :return: The run_status of this TaskInfo.
        :rtype: int
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """Sets the run_status of this TaskInfo.

        run_status

        :param run_status: The run_status of this TaskInfo.
        :type run_status: int
        """
        self._run_status = run_status

    @property
    def update_time(self):
        """Gets the update_time of this TaskInfo.

        update_time

        :return: The update_time of this TaskInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TaskInfo.

        update_time

        :param update_time: The update_time of this TaskInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def parallel(self):
        """Gets the parallel of this TaskInfo.

        parallel

        :return: The parallel of this TaskInfo.
        :rtype: bool
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        """Sets the parallel of this TaskInfo.

        parallel

        :param parallel: The parallel of this TaskInfo.
        :type parallel: bool
        """
        self._parallel = parallel

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
        if not isinstance(other, TaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
