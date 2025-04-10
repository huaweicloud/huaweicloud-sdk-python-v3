# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskAssignCaseDetailVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'sort': 'int',
        'owner': 'str',
        'stage': 'int',
        'project_uuid': 'str',
        'task_uri': 'str',
        'update_time': 'datetime',
        'updator_name': 'str',
        'updator': 'str',
        'case_uri': 'str',
        'is_available': 'int',
        'test_case_name': 'str',
        'feature_uri': 'str',
        'test_case_number': 'str',
        'svn_script_path': 'str',
        'status_code': 'str',
        'status_name': 'str',
        'result_code': 'str',
        'result_name': 'str',
        'owner_name': 'str',
        'execute_latest_time': 'datetime',
        'execute_duration': 'str',
        'is_keyword': 'int',
        'net_work_script_name': 'str',
        'rank_id': 'int'
    }

    attribute_map = {
        'uri': 'uri',
        'sort': 'sort',
        'owner': 'owner',
        'stage': 'stage',
        'project_uuid': 'project_uuid',
        'task_uri': 'task_uri',
        'update_time': 'update_time',
        'updator_name': 'updator_name',
        'updator': 'updator',
        'case_uri': 'case_uri',
        'is_available': 'is_available',
        'test_case_name': 'test_case_name',
        'feature_uri': 'feature_uri',
        'test_case_number': 'test_case_number',
        'svn_script_path': 'svn_script_path',
        'status_code': 'status_code',
        'status_name': 'status_name',
        'result_code': 'result_code',
        'result_name': 'result_name',
        'owner_name': 'owner_name',
        'execute_latest_time': 'execute_latest_time',
        'execute_duration': 'execute_duration',
        'is_keyword': 'is_keyword',
        'net_work_script_name': 'net_work_script_name',
        'rank_id': 'rank_id'
    }

    def __init__(self, uri=None, sort=None, owner=None, stage=None, project_uuid=None, task_uri=None, update_time=None, updator_name=None, updator=None, case_uri=None, is_available=None, test_case_name=None, feature_uri=None, test_case_number=None, svn_script_path=None, status_code=None, status_name=None, result_code=None, result_name=None, owner_name=None, execute_latest_time=None, execute_duration=None, is_keyword=None, net_work_script_name=None, rank_id=None):
        r"""TaskAssignCaseDetailVo

        The model defined in huaweicloud sdk

        :param uri: 关联关系uri
        :type uri: str
        :param sort: 排序顺序
        :type sort: int
        :param owner: 责任人id
        :type owner: str
        :param stage: 测试阶段
        :type stage: int
        :param project_uuid: 项目id
        :type project_uuid: str
        :param task_uri: 任务uri
        :type task_uri: str
        :param update_time: 更新时间
        :type update_time: datetime
        :param updator_name: 更新人
        :type updator_name: str
        :param updator: 更新人id
        :type updator: str
        :param case_uri: 用例uri
        :type case_uri: str
        :param is_available: 是否可用
        :type is_available: int
        :param test_case_name: 用例名称
        :type test_case_name: str
        :param feature_uri: 用例目录Uri
        :type feature_uri: str
        :param test_case_number: 用例编号
        :type test_case_number: str
        :param svn_script_path: 脚本路径
        :type svn_script_path: str
        :param status_code: 状态
        :type status_code: str
        :param status_name: 状态名称
        :type status_name: str
        :param result_code: 结果id
        :type result_code: str
        :param result_name: 结果名称
        :type result_name: str
        :param owner_name: 责任人名称
        :type owner_name: str
        :param execute_latest_time: 最新执行时间
        :type execute_latest_time: datetime
        :param execute_duration: 执行时长
        :type execute_duration: str
        :param is_keyword: 是否是关键用例
        :type is_keyword: int
        :param net_work_script_name: 脚本名称
        :type net_work_script_name: str
        :param rank_id: 用例等级
        :type rank_id: int
        """
        
        

        self._uri = None
        self._sort = None
        self._owner = None
        self._stage = None
        self._project_uuid = None
        self._task_uri = None
        self._update_time = None
        self._updator_name = None
        self._updator = None
        self._case_uri = None
        self._is_available = None
        self._test_case_name = None
        self._feature_uri = None
        self._test_case_number = None
        self._svn_script_path = None
        self._status_code = None
        self._status_name = None
        self._result_code = None
        self._result_name = None
        self._owner_name = None
        self._execute_latest_time = None
        self._execute_duration = None
        self._is_keyword = None
        self._net_work_script_name = None
        self._rank_id = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if sort is not None:
            self.sort = sort
        if owner is not None:
            self.owner = owner
        if stage is not None:
            self.stage = stage
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if task_uri is not None:
            self.task_uri = task_uri
        if update_time is not None:
            self.update_time = update_time
        if updator_name is not None:
            self.updator_name = updator_name
        if updator is not None:
            self.updator = updator
        if case_uri is not None:
            self.case_uri = case_uri
        if is_available is not None:
            self.is_available = is_available
        if test_case_name is not None:
            self.test_case_name = test_case_name
        if feature_uri is not None:
            self.feature_uri = feature_uri
        if test_case_number is not None:
            self.test_case_number = test_case_number
        if svn_script_path is not None:
            self.svn_script_path = svn_script_path
        if status_code is not None:
            self.status_code = status_code
        if status_name is not None:
            self.status_name = status_name
        if result_code is not None:
            self.result_code = result_code
        if result_name is not None:
            self.result_name = result_name
        if owner_name is not None:
            self.owner_name = owner_name
        if execute_latest_time is not None:
            self.execute_latest_time = execute_latest_time
        if execute_duration is not None:
            self.execute_duration = execute_duration
        if is_keyword is not None:
            self.is_keyword = is_keyword
        if net_work_script_name is not None:
            self.net_work_script_name = net_work_script_name
        if rank_id is not None:
            self.rank_id = rank_id

    @property
    def uri(self):
        r"""Gets the uri of this TaskAssignCaseDetailVo.

        关联关系uri

        :return: The uri of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this TaskAssignCaseDetailVo.

        关联关系uri

        :param uri: The uri of this TaskAssignCaseDetailVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def sort(self):
        r"""Gets the sort of this TaskAssignCaseDetailVo.

        排序顺序

        :return: The sort of this TaskAssignCaseDetailVo.
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this TaskAssignCaseDetailVo.

        排序顺序

        :param sort: The sort of this TaskAssignCaseDetailVo.
        :type sort: int
        """
        self._sort = sort

    @property
    def owner(self):
        r"""Gets the owner of this TaskAssignCaseDetailVo.

        责任人id

        :return: The owner of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TaskAssignCaseDetailVo.

        责任人id

        :param owner: The owner of this TaskAssignCaseDetailVo.
        :type owner: str
        """
        self._owner = owner

    @property
    def stage(self):
        r"""Gets the stage of this TaskAssignCaseDetailVo.

        测试阶段

        :return: The stage of this TaskAssignCaseDetailVo.
        :rtype: int
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this TaskAssignCaseDetailVo.

        测试阶段

        :param stage: The stage of this TaskAssignCaseDetailVo.
        :type stage: int
        """
        self._stage = stage

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this TaskAssignCaseDetailVo.

        项目id

        :return: The project_uuid of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this TaskAssignCaseDetailVo.

        项目id

        :param project_uuid: The project_uuid of this TaskAssignCaseDetailVo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def task_uri(self):
        r"""Gets the task_uri of this TaskAssignCaseDetailVo.

        任务uri

        :return: The task_uri of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this TaskAssignCaseDetailVo.

        任务uri

        :param task_uri: The task_uri of this TaskAssignCaseDetailVo.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def update_time(self):
        r"""Gets the update_time of this TaskAssignCaseDetailVo.

        更新时间

        :return: The update_time of this TaskAssignCaseDetailVo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TaskAssignCaseDetailVo.

        更新时间

        :param update_time: The update_time of this TaskAssignCaseDetailVo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def updator_name(self):
        r"""Gets the updator_name of this TaskAssignCaseDetailVo.

        更新人

        :return: The updator_name of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._updator_name

    @updator_name.setter
    def updator_name(self, updator_name):
        r"""Sets the updator_name of this TaskAssignCaseDetailVo.

        更新人

        :param updator_name: The updator_name of this TaskAssignCaseDetailVo.
        :type updator_name: str
        """
        self._updator_name = updator_name

    @property
    def updator(self):
        r"""Gets the updator of this TaskAssignCaseDetailVo.

        更新人id

        :return: The updator of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._updator

    @updator.setter
    def updator(self, updator):
        r"""Sets the updator of this TaskAssignCaseDetailVo.

        更新人id

        :param updator: The updator of this TaskAssignCaseDetailVo.
        :type updator: str
        """
        self._updator = updator

    @property
    def case_uri(self):
        r"""Gets the case_uri of this TaskAssignCaseDetailVo.

        用例uri

        :return: The case_uri of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._case_uri

    @case_uri.setter
    def case_uri(self, case_uri):
        r"""Sets the case_uri of this TaskAssignCaseDetailVo.

        用例uri

        :param case_uri: The case_uri of this TaskAssignCaseDetailVo.
        :type case_uri: str
        """
        self._case_uri = case_uri

    @property
    def is_available(self):
        r"""Gets the is_available of this TaskAssignCaseDetailVo.

        是否可用

        :return: The is_available of this TaskAssignCaseDetailVo.
        :rtype: int
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        r"""Sets the is_available of this TaskAssignCaseDetailVo.

        是否可用

        :param is_available: The is_available of this TaskAssignCaseDetailVo.
        :type is_available: int
        """
        self._is_available = is_available

    @property
    def test_case_name(self):
        r"""Gets the test_case_name of this TaskAssignCaseDetailVo.

        用例名称

        :return: The test_case_name of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._test_case_name

    @test_case_name.setter
    def test_case_name(self, test_case_name):
        r"""Sets the test_case_name of this TaskAssignCaseDetailVo.

        用例名称

        :param test_case_name: The test_case_name of this TaskAssignCaseDetailVo.
        :type test_case_name: str
        """
        self._test_case_name = test_case_name

    @property
    def feature_uri(self):
        r"""Gets the feature_uri of this TaskAssignCaseDetailVo.

        用例目录Uri

        :return: The feature_uri of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._feature_uri

    @feature_uri.setter
    def feature_uri(self, feature_uri):
        r"""Sets the feature_uri of this TaskAssignCaseDetailVo.

        用例目录Uri

        :param feature_uri: The feature_uri of this TaskAssignCaseDetailVo.
        :type feature_uri: str
        """
        self._feature_uri = feature_uri

    @property
    def test_case_number(self):
        r"""Gets the test_case_number of this TaskAssignCaseDetailVo.

        用例编号

        :return: The test_case_number of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._test_case_number

    @test_case_number.setter
    def test_case_number(self, test_case_number):
        r"""Sets the test_case_number of this TaskAssignCaseDetailVo.

        用例编号

        :param test_case_number: The test_case_number of this TaskAssignCaseDetailVo.
        :type test_case_number: str
        """
        self._test_case_number = test_case_number

    @property
    def svn_script_path(self):
        r"""Gets the svn_script_path of this TaskAssignCaseDetailVo.

        脚本路径

        :return: The svn_script_path of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._svn_script_path

    @svn_script_path.setter
    def svn_script_path(self, svn_script_path):
        r"""Sets the svn_script_path of this TaskAssignCaseDetailVo.

        脚本路径

        :param svn_script_path: The svn_script_path of this TaskAssignCaseDetailVo.
        :type svn_script_path: str
        """
        self._svn_script_path = svn_script_path

    @property
    def status_code(self):
        r"""Gets the status_code of this TaskAssignCaseDetailVo.

        状态

        :return: The status_code of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this TaskAssignCaseDetailVo.

        状态

        :param status_code: The status_code of this TaskAssignCaseDetailVo.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def status_name(self):
        r"""Gets the status_name of this TaskAssignCaseDetailVo.

        状态名称

        :return: The status_name of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._status_name

    @status_name.setter
    def status_name(self, status_name):
        r"""Sets the status_name of this TaskAssignCaseDetailVo.

        状态名称

        :param status_name: The status_name of this TaskAssignCaseDetailVo.
        :type status_name: str
        """
        self._status_name = status_name

    @property
    def result_code(self):
        r"""Gets the result_code of this TaskAssignCaseDetailVo.

        结果id

        :return: The result_code of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        r"""Sets the result_code of this TaskAssignCaseDetailVo.

        结果id

        :param result_code: The result_code of this TaskAssignCaseDetailVo.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def result_name(self):
        r"""Gets the result_name of this TaskAssignCaseDetailVo.

        结果名称

        :return: The result_name of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._result_name

    @result_name.setter
    def result_name(self, result_name):
        r"""Sets the result_name of this TaskAssignCaseDetailVo.

        结果名称

        :param result_name: The result_name of this TaskAssignCaseDetailVo.
        :type result_name: str
        """
        self._result_name = result_name

    @property
    def owner_name(self):
        r"""Gets the owner_name of this TaskAssignCaseDetailVo.

        责任人名称

        :return: The owner_name of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this TaskAssignCaseDetailVo.

        责任人名称

        :param owner_name: The owner_name of this TaskAssignCaseDetailVo.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def execute_latest_time(self):
        r"""Gets the execute_latest_time of this TaskAssignCaseDetailVo.

        最新执行时间

        :return: The execute_latest_time of this TaskAssignCaseDetailVo.
        :rtype: datetime
        """
        return self._execute_latest_time

    @execute_latest_time.setter
    def execute_latest_time(self, execute_latest_time):
        r"""Sets the execute_latest_time of this TaskAssignCaseDetailVo.

        最新执行时间

        :param execute_latest_time: The execute_latest_time of this TaskAssignCaseDetailVo.
        :type execute_latest_time: datetime
        """
        self._execute_latest_time = execute_latest_time

    @property
    def execute_duration(self):
        r"""Gets the execute_duration of this TaskAssignCaseDetailVo.

        执行时长

        :return: The execute_duration of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._execute_duration

    @execute_duration.setter
    def execute_duration(self, execute_duration):
        r"""Sets the execute_duration of this TaskAssignCaseDetailVo.

        执行时长

        :param execute_duration: The execute_duration of this TaskAssignCaseDetailVo.
        :type execute_duration: str
        """
        self._execute_duration = execute_duration

    @property
    def is_keyword(self):
        r"""Gets the is_keyword of this TaskAssignCaseDetailVo.

        是否是关键用例

        :return: The is_keyword of this TaskAssignCaseDetailVo.
        :rtype: int
        """
        return self._is_keyword

    @is_keyword.setter
    def is_keyword(self, is_keyword):
        r"""Sets the is_keyword of this TaskAssignCaseDetailVo.

        是否是关键用例

        :param is_keyword: The is_keyword of this TaskAssignCaseDetailVo.
        :type is_keyword: int
        """
        self._is_keyword = is_keyword

    @property
    def net_work_script_name(self):
        r"""Gets the net_work_script_name of this TaskAssignCaseDetailVo.

        脚本名称

        :return: The net_work_script_name of this TaskAssignCaseDetailVo.
        :rtype: str
        """
        return self._net_work_script_name

    @net_work_script_name.setter
    def net_work_script_name(self, net_work_script_name):
        r"""Sets the net_work_script_name of this TaskAssignCaseDetailVo.

        脚本名称

        :param net_work_script_name: The net_work_script_name of this TaskAssignCaseDetailVo.
        :type net_work_script_name: str
        """
        self._net_work_script_name = net_work_script_name

    @property
    def rank_id(self):
        r"""Gets the rank_id of this TaskAssignCaseDetailVo.

        用例等级

        :return: The rank_id of this TaskAssignCaseDetailVo.
        :rtype: int
        """
        return self._rank_id

    @rank_id.setter
    def rank_id(self, rank_id):
        r"""Sets the rank_id of this TaskAssignCaseDetailVo.

        用例等级

        :param rank_id: The rank_id of this TaskAssignCaseDetailVo.
        :type rank_id: int
        """
        self._rank_id = rank_id

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
        if not isinstance(other, TaskAssignCaseDetailVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
