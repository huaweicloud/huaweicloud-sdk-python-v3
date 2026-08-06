# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTaskCaseQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_user': 'str',
        'end_time': 'int',
        'key_word': 'str',
        'location_id': 'str',
        'more': 'bool',
        'page_num': 'int',
        'page_size': 'int',
        'pid': 'str',
        'results': 'list[int]',
        'sort_by': 'str',
        'stage': 'int',
        'start_time': 'int',
        'state': 'str',
        'subtask_ids': 'list[str]',
        'subtask_id': 'str',
        'suite_type': 'int',
        'task_id': 'str',
        'task_ids': 'list[str]',
        'task_type_id': 'str',
        'test_service_id': 'str',
        'testcase_id': 'str'
    }

    attribute_map = {
        'create_user': 'create_user',
        'end_time': 'endTime',
        'key_word': 'keyWord',
        'location_id': 'location_id',
        'more': 'more',
        'page_num': 'page_num',
        'page_size': 'page_size',
        'pid': 'pid',
        'results': 'results',
        'sort_by': 'sortBy',
        'stage': 'stage',
        'start_time': 'startTime',
        'state': 'state',
        'subtask_ids': 'subtask_ids',
        'subtask_id': 'subtask_id',
        'suite_type': 'suiteType',
        'task_id': 'task_id',
        'task_ids': 'task_ids',
        'task_type_id': 'taskTypeId',
        'test_service_id': 'test_service_id',
        'testcase_id': 'testcase_id'
    }

    def __init__(self, create_user=None, end_time=None, key_word=None, location_id=None, more=None, page_num=None, page_size=None, pid=None, results=None, sort_by=None, stage=None, start_time=None, state=None, subtask_ids=None, subtask_id=None, suite_type=None, task_id=None, task_ids=None, task_type_id=None, test_service_id=None, testcase_id=None):
        r"""SubTaskCaseQuery

        The model defined in huaweicloud sdk

        :param create_user: 用例创建者
        :type create_user: str
        :param end_time: 用例结束时间
        :type end_time: int
        :param key_word: 
        :type key_word: str
        :param location_id: 执行机区域ID
        :type location_id: str
        :param more: 
        :type more: bool
        :param page_num: 分页时页码
        :type page_num: int
        :param page_size: 分页时每页大小
        :type page_size: int
        :param pid: 告警策略选择失败后重试时有值
        :type pid: str
        :param results: cloudTest任务执行结果列表
        :type results: list[int]
        :param sort_by: 排序字段
        :type sort_by: str
        :param stage: 用例所处的阶段 0：前置， 1：测试用例 2：后置用例
        :type stage: int
        :param start_time: 用例开始时间
        :type start_time: int
        :param state: 状态
        :type state: str
        :param subtask_ids: 子任务ID列表
        :type subtask_ids: list[str]
        :param subtask_id: 子任务ID
        :type subtask_id: str
        :param suite_type: 
        :type suite_type: int
        :param task_id: 任务ID
        :type task_id: str
        :param task_ids: 任务ID列表
        :type task_ids: list[str]
        :param task_type_id: 任务类型
        :type task_type_id: str
        :param test_service_id: 服务ID
        :type test_service_id: str
        :param testcase_id: 用例ID
        :type testcase_id: str
        """
        
        

        self._create_user = None
        self._end_time = None
        self._key_word = None
        self._location_id = None
        self._more = None
        self._page_num = None
        self._page_size = None
        self._pid = None
        self._results = None
        self._sort_by = None
        self._stage = None
        self._start_time = None
        self._state = None
        self._subtask_ids = None
        self._subtask_id = None
        self._suite_type = None
        self._task_id = None
        self._task_ids = None
        self._task_type_id = None
        self._test_service_id = None
        self._testcase_id = None
        self.discriminator = None

        if create_user is not None:
            self.create_user = create_user
        if end_time is not None:
            self.end_time = end_time
        if key_word is not None:
            self.key_word = key_word
        if location_id is not None:
            self.location_id = location_id
        if more is not None:
            self.more = more
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if pid is not None:
            self.pid = pid
        if results is not None:
            self.results = results
        if sort_by is not None:
            self.sort_by = sort_by
        if stage is not None:
            self.stage = stage
        if start_time is not None:
            self.start_time = start_time
        if state is not None:
            self.state = state
        if subtask_ids is not None:
            self.subtask_ids = subtask_ids
        if subtask_id is not None:
            self.subtask_id = subtask_id
        if suite_type is not None:
            self.suite_type = suite_type
        if task_id is not None:
            self.task_id = task_id
        if task_ids is not None:
            self.task_ids = task_ids
        if task_type_id is not None:
            self.task_type_id = task_type_id
        if test_service_id is not None:
            self.test_service_id = test_service_id
        if testcase_id is not None:
            self.testcase_id = testcase_id

    @property
    def create_user(self):
        r"""Gets the create_user of this SubTaskCaseQuery.

        用例创建者

        :return: The create_user of this SubTaskCaseQuery.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this SubTaskCaseQuery.

        用例创建者

        :param create_user: The create_user of this SubTaskCaseQuery.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def end_time(self):
        r"""Gets the end_time of this SubTaskCaseQuery.

        用例结束时间

        :return: The end_time of this SubTaskCaseQuery.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SubTaskCaseQuery.

        用例结束时间

        :param end_time: The end_time of this SubTaskCaseQuery.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def key_word(self):
        r"""Gets the key_word of this SubTaskCaseQuery.

        :return: The key_word of this SubTaskCaseQuery.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this SubTaskCaseQuery.

        :param key_word: The key_word of this SubTaskCaseQuery.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def location_id(self):
        r"""Gets the location_id of this SubTaskCaseQuery.

        执行机区域ID

        :return: The location_id of this SubTaskCaseQuery.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        r"""Sets the location_id of this SubTaskCaseQuery.

        执行机区域ID

        :param location_id: The location_id of this SubTaskCaseQuery.
        :type location_id: str
        """
        self._location_id = location_id

    @property
    def more(self):
        r"""Gets the more of this SubTaskCaseQuery.

        :return: The more of this SubTaskCaseQuery.
        :rtype: bool
        """
        return self._more

    @more.setter
    def more(self, more):
        r"""Sets the more of this SubTaskCaseQuery.

        :param more: The more of this SubTaskCaseQuery.
        :type more: bool
        """
        self._more = more

    @property
    def page_num(self):
        r"""Gets the page_num of this SubTaskCaseQuery.

        分页时页码

        :return: The page_num of this SubTaskCaseQuery.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this SubTaskCaseQuery.

        分页时页码

        :param page_num: The page_num of this SubTaskCaseQuery.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this SubTaskCaseQuery.

        分页时每页大小

        :return: The page_size of this SubTaskCaseQuery.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this SubTaskCaseQuery.

        分页时每页大小

        :param page_size: The page_size of this SubTaskCaseQuery.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def pid(self):
        r"""Gets the pid of this SubTaskCaseQuery.

        告警策略选择失败后重试时有值

        :return: The pid of this SubTaskCaseQuery.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this SubTaskCaseQuery.

        告警策略选择失败后重试时有值

        :param pid: The pid of this SubTaskCaseQuery.
        :type pid: str
        """
        self._pid = pid

    @property
    def results(self):
        r"""Gets the results of this SubTaskCaseQuery.

        cloudTest任务执行结果列表

        :return: The results of this SubTaskCaseQuery.
        :rtype: list[int]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this SubTaskCaseQuery.

        cloudTest任务执行结果列表

        :param results: The results of this SubTaskCaseQuery.
        :type results: list[int]
        """
        self._results = results

    @property
    def sort_by(self):
        r"""Gets the sort_by of this SubTaskCaseQuery.

        排序字段

        :return: The sort_by of this SubTaskCaseQuery.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this SubTaskCaseQuery.

        排序字段

        :param sort_by: The sort_by of this SubTaskCaseQuery.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def stage(self):
        r"""Gets the stage of this SubTaskCaseQuery.

        用例所处的阶段 0：前置， 1：测试用例 2：后置用例

        :return: The stage of this SubTaskCaseQuery.
        :rtype: int
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this SubTaskCaseQuery.

        用例所处的阶段 0：前置， 1：测试用例 2：后置用例

        :param stage: The stage of this SubTaskCaseQuery.
        :type stage: int
        """
        self._stage = stage

    @property
    def start_time(self):
        r"""Gets the start_time of this SubTaskCaseQuery.

        用例开始时间

        :return: The start_time of this SubTaskCaseQuery.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SubTaskCaseQuery.

        用例开始时间

        :param start_time: The start_time of this SubTaskCaseQuery.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def state(self):
        r"""Gets the state of this SubTaskCaseQuery.

        状态

        :return: The state of this SubTaskCaseQuery.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this SubTaskCaseQuery.

        状态

        :param state: The state of this SubTaskCaseQuery.
        :type state: str
        """
        self._state = state

    @property
    def subtask_ids(self):
        r"""Gets the subtask_ids of this SubTaskCaseQuery.

        子任务ID列表

        :return: The subtask_ids of this SubTaskCaseQuery.
        :rtype: list[str]
        """
        return self._subtask_ids

    @subtask_ids.setter
    def subtask_ids(self, subtask_ids):
        r"""Sets the subtask_ids of this SubTaskCaseQuery.

        子任务ID列表

        :param subtask_ids: The subtask_ids of this SubTaskCaseQuery.
        :type subtask_ids: list[str]
        """
        self._subtask_ids = subtask_ids

    @property
    def subtask_id(self):
        r"""Gets the subtask_id of this SubTaskCaseQuery.

        子任务ID

        :return: The subtask_id of this SubTaskCaseQuery.
        :rtype: str
        """
        return self._subtask_id

    @subtask_id.setter
    def subtask_id(self, subtask_id):
        r"""Sets the subtask_id of this SubTaskCaseQuery.

        子任务ID

        :param subtask_id: The subtask_id of this SubTaskCaseQuery.
        :type subtask_id: str
        """
        self._subtask_id = subtask_id

    @property
    def suite_type(self):
        r"""Gets the suite_type of this SubTaskCaseQuery.

        :return: The suite_type of this SubTaskCaseQuery.
        :rtype: int
        """
        return self._suite_type

    @suite_type.setter
    def suite_type(self, suite_type):
        r"""Sets the suite_type of this SubTaskCaseQuery.

        :param suite_type: The suite_type of this SubTaskCaseQuery.
        :type suite_type: int
        """
        self._suite_type = suite_type

    @property
    def task_id(self):
        r"""Gets the task_id of this SubTaskCaseQuery.

        任务ID

        :return: The task_id of this SubTaskCaseQuery.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SubTaskCaseQuery.

        任务ID

        :param task_id: The task_id of this SubTaskCaseQuery.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_ids(self):
        r"""Gets the task_ids of this SubTaskCaseQuery.

        任务ID列表

        :return: The task_ids of this SubTaskCaseQuery.
        :rtype: list[str]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        r"""Sets the task_ids of this SubTaskCaseQuery.

        任务ID列表

        :param task_ids: The task_ids of this SubTaskCaseQuery.
        :type task_ids: list[str]
        """
        self._task_ids = task_ids

    @property
    def task_type_id(self):
        r"""Gets the task_type_id of this SubTaskCaseQuery.

        任务类型

        :return: The task_type_id of this SubTaskCaseQuery.
        :rtype: str
        """
        return self._task_type_id

    @task_type_id.setter
    def task_type_id(self, task_type_id):
        r"""Sets the task_type_id of this SubTaskCaseQuery.

        任务类型

        :param task_type_id: The task_type_id of this SubTaskCaseQuery.
        :type task_type_id: str
        """
        self._task_type_id = task_type_id

    @property
    def test_service_id(self):
        r"""Gets the test_service_id of this SubTaskCaseQuery.

        服务ID

        :return: The test_service_id of this SubTaskCaseQuery.
        :rtype: str
        """
        return self._test_service_id

    @test_service_id.setter
    def test_service_id(self, test_service_id):
        r"""Sets the test_service_id of this SubTaskCaseQuery.

        服务ID

        :param test_service_id: The test_service_id of this SubTaskCaseQuery.
        :type test_service_id: str
        """
        self._test_service_id = test_service_id

    @property
    def testcase_id(self):
        r"""Gets the testcase_id of this SubTaskCaseQuery.

        用例ID

        :return: The testcase_id of this SubTaskCaseQuery.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        r"""Sets the testcase_id of this SubTaskCaseQuery.

        用例ID

        :param testcase_id: The testcase_id of this SubTaskCaseQuery.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubTaskCaseQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
