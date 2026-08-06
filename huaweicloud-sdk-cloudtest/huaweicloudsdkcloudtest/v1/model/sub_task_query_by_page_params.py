# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTaskQueryByPageParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'more': 'bool',
        'not_set_release_dev': 'bool',
        'page_number': 'int',
        'page_size': 'int',
        'parent_sub_task_id': 'str',
        'plan_id': 'str',
        'release_dev': 'list[str]',
        'results': 'list[int]',
        'start_time_begin': 'int',
        'start_time_end': 'int',
        'state': 'int',
        'states': 'list[int]',
        'sub_task_id': 'str',
        'suite_type': 'int',
        'task_id': 'str',
        'task_type_id': 'str',
        'test_service_id': 'str'
    }

    attribute_map = {
        'more': 'more',
        'not_set_release_dev': 'notSetReleaseDev',
        'page_number': 'page_number',
        'page_size': 'page_size',
        'parent_sub_task_id': 'parent_sub_task_id',
        'plan_id': 'plan_id',
        'release_dev': 'release_dev',
        'results': 'results',
        'start_time_begin': 'start_time_begin',
        'start_time_end': 'start_time_end',
        'state': 'state',
        'states': 'states',
        'sub_task_id': 'sub_task_id',
        'suite_type': 'suite_type',
        'task_id': 'task_id',
        'task_type_id': 'task_type_id',
        'test_service_id': 'test_service_id'
    }

    def __init__(self, more=None, not_set_release_dev=None, page_number=None, page_size=None, parent_sub_task_id=None, plan_id=None, release_dev=None, results=None, start_time_begin=None, start_time_end=None, state=None, states=None, sub_task_id=None, suite_type=None, task_id=None, task_type_id=None, test_service_id=None):
        r"""SubTaskQueryByPageParams

        The model defined in huaweicloud sdk

        :param more: 
        :type more: bool
        :param not_set_release_dev: 未设置发布版本
        :type not_set_release_dev: bool
        :param page_number: 页码
        :type page_number: int
        :param page_size: 每页大小
        :type page_size: int
        :param parent_sub_task_id: 父任务id
        :type parent_sub_task_id: str
        :param plan_id: 测试计划id
        :type plan_id: str
        :param release_dev: -| 发布的版本，空数组：代表所有未设置的； null或者无此字段，搜索所有版本 有内容：搜索所有版本
        :type release_dev: list[str]
        :param results: 
        :type results: list[int]
        :param start_time_begin: 任务执行第一次时间
        :type start_time_begin: int
        :param start_time_end: 任务执行最后一次时间
        :type start_time_end: int
        :param state: 状态
        :type state: int
        :param states: 子任务状态列表
        :type states: list[int]
        :param sub_task_id: 子任务任务id
        :type sub_task_id: str
        :param suite_type: 测试套类型
        :type suite_type: int
        :param task_id: 任务id
        :type task_id: str
        :param task_type_id: 任务类型，1&#x3D;拨测，2&#x3D;冒烟
        :type task_type_id: str
        :param test_service_id: 项目id
        :type test_service_id: str
        """
        
        

        self._more = None
        self._not_set_release_dev = None
        self._page_number = None
        self._page_size = None
        self._parent_sub_task_id = None
        self._plan_id = None
        self._release_dev = None
        self._results = None
        self._start_time_begin = None
        self._start_time_end = None
        self._state = None
        self._states = None
        self._sub_task_id = None
        self._suite_type = None
        self._task_id = None
        self._task_type_id = None
        self._test_service_id = None
        self.discriminator = None

        if more is not None:
            self.more = more
        if not_set_release_dev is not None:
            self.not_set_release_dev = not_set_release_dev
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if parent_sub_task_id is not None:
            self.parent_sub_task_id = parent_sub_task_id
        if plan_id is not None:
            self.plan_id = plan_id
        if release_dev is not None:
            self.release_dev = release_dev
        if results is not None:
            self.results = results
        if start_time_begin is not None:
            self.start_time_begin = start_time_begin
        if start_time_end is not None:
            self.start_time_end = start_time_end
        if state is not None:
            self.state = state
        if states is not None:
            self.states = states
        if sub_task_id is not None:
            self.sub_task_id = sub_task_id
        if suite_type is not None:
            self.suite_type = suite_type
        if task_id is not None:
            self.task_id = task_id
        if task_type_id is not None:
            self.task_type_id = task_type_id
        if test_service_id is not None:
            self.test_service_id = test_service_id

    @property
    def more(self):
        r"""Gets the more of this SubTaskQueryByPageParams.

        :return: The more of this SubTaskQueryByPageParams.
        :rtype: bool
        """
        return self._more

    @more.setter
    def more(self, more):
        r"""Sets the more of this SubTaskQueryByPageParams.

        :param more: The more of this SubTaskQueryByPageParams.
        :type more: bool
        """
        self._more = more

    @property
    def not_set_release_dev(self):
        r"""Gets the not_set_release_dev of this SubTaskQueryByPageParams.

        未设置发布版本

        :return: The not_set_release_dev of this SubTaskQueryByPageParams.
        :rtype: bool
        """
        return self._not_set_release_dev

    @not_set_release_dev.setter
    def not_set_release_dev(self, not_set_release_dev):
        r"""Sets the not_set_release_dev of this SubTaskQueryByPageParams.

        未设置发布版本

        :param not_set_release_dev: The not_set_release_dev of this SubTaskQueryByPageParams.
        :type not_set_release_dev: bool
        """
        self._not_set_release_dev = not_set_release_dev

    @property
    def page_number(self):
        r"""Gets the page_number of this SubTaskQueryByPageParams.

        页码

        :return: The page_number of this SubTaskQueryByPageParams.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this SubTaskQueryByPageParams.

        页码

        :param page_number: The page_number of this SubTaskQueryByPageParams.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def page_size(self):
        r"""Gets the page_size of this SubTaskQueryByPageParams.

        每页大小

        :return: The page_size of this SubTaskQueryByPageParams.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this SubTaskQueryByPageParams.

        每页大小

        :param page_size: The page_size of this SubTaskQueryByPageParams.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def parent_sub_task_id(self):
        r"""Gets the parent_sub_task_id of this SubTaskQueryByPageParams.

        父任务id

        :return: The parent_sub_task_id of this SubTaskQueryByPageParams.
        :rtype: str
        """
        return self._parent_sub_task_id

    @parent_sub_task_id.setter
    def parent_sub_task_id(self, parent_sub_task_id):
        r"""Sets the parent_sub_task_id of this SubTaskQueryByPageParams.

        父任务id

        :param parent_sub_task_id: The parent_sub_task_id of this SubTaskQueryByPageParams.
        :type parent_sub_task_id: str
        """
        self._parent_sub_task_id = parent_sub_task_id

    @property
    def plan_id(self):
        r"""Gets the plan_id of this SubTaskQueryByPageParams.

        测试计划id

        :return: The plan_id of this SubTaskQueryByPageParams.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this SubTaskQueryByPageParams.

        测试计划id

        :param plan_id: The plan_id of this SubTaskQueryByPageParams.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def release_dev(self):
        r"""Gets the release_dev of this SubTaskQueryByPageParams.

        -| 发布的版本，空数组：代表所有未设置的； null或者无此字段，搜索所有版本 有内容：搜索所有版本

        :return: The release_dev of this SubTaskQueryByPageParams.
        :rtype: list[str]
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this SubTaskQueryByPageParams.

        -| 发布的版本，空数组：代表所有未设置的； null或者无此字段，搜索所有版本 有内容：搜索所有版本

        :param release_dev: The release_dev of this SubTaskQueryByPageParams.
        :type release_dev: list[str]
        """
        self._release_dev = release_dev

    @property
    def results(self):
        r"""Gets the results of this SubTaskQueryByPageParams.

        :return: The results of this SubTaskQueryByPageParams.
        :rtype: list[int]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this SubTaskQueryByPageParams.

        :param results: The results of this SubTaskQueryByPageParams.
        :type results: list[int]
        """
        self._results = results

    @property
    def start_time_begin(self):
        r"""Gets the start_time_begin of this SubTaskQueryByPageParams.

        任务执行第一次时间

        :return: The start_time_begin of this SubTaskQueryByPageParams.
        :rtype: int
        """
        return self._start_time_begin

    @start_time_begin.setter
    def start_time_begin(self, start_time_begin):
        r"""Sets the start_time_begin of this SubTaskQueryByPageParams.

        任务执行第一次时间

        :param start_time_begin: The start_time_begin of this SubTaskQueryByPageParams.
        :type start_time_begin: int
        """
        self._start_time_begin = start_time_begin

    @property
    def start_time_end(self):
        r"""Gets the start_time_end of this SubTaskQueryByPageParams.

        任务执行最后一次时间

        :return: The start_time_end of this SubTaskQueryByPageParams.
        :rtype: int
        """
        return self._start_time_end

    @start_time_end.setter
    def start_time_end(self, start_time_end):
        r"""Sets the start_time_end of this SubTaskQueryByPageParams.

        任务执行最后一次时间

        :param start_time_end: The start_time_end of this SubTaskQueryByPageParams.
        :type start_time_end: int
        """
        self._start_time_end = start_time_end

    @property
    def state(self):
        r"""Gets the state of this SubTaskQueryByPageParams.

        状态

        :return: The state of this SubTaskQueryByPageParams.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this SubTaskQueryByPageParams.

        状态

        :param state: The state of this SubTaskQueryByPageParams.
        :type state: int
        """
        self._state = state

    @property
    def states(self):
        r"""Gets the states of this SubTaskQueryByPageParams.

        子任务状态列表

        :return: The states of this SubTaskQueryByPageParams.
        :rtype: list[int]
        """
        return self._states

    @states.setter
    def states(self, states):
        r"""Sets the states of this SubTaskQueryByPageParams.

        子任务状态列表

        :param states: The states of this SubTaskQueryByPageParams.
        :type states: list[int]
        """
        self._states = states

    @property
    def sub_task_id(self):
        r"""Gets the sub_task_id of this SubTaskQueryByPageParams.

        子任务任务id

        :return: The sub_task_id of this SubTaskQueryByPageParams.
        :rtype: str
        """
        return self._sub_task_id

    @sub_task_id.setter
    def sub_task_id(self, sub_task_id):
        r"""Sets the sub_task_id of this SubTaskQueryByPageParams.

        子任务任务id

        :param sub_task_id: The sub_task_id of this SubTaskQueryByPageParams.
        :type sub_task_id: str
        """
        self._sub_task_id = sub_task_id

    @property
    def suite_type(self):
        r"""Gets the suite_type of this SubTaskQueryByPageParams.

        测试套类型

        :return: The suite_type of this SubTaskQueryByPageParams.
        :rtype: int
        """
        return self._suite_type

    @suite_type.setter
    def suite_type(self, suite_type):
        r"""Sets the suite_type of this SubTaskQueryByPageParams.

        测试套类型

        :param suite_type: The suite_type of this SubTaskQueryByPageParams.
        :type suite_type: int
        """
        self._suite_type = suite_type

    @property
    def task_id(self):
        r"""Gets the task_id of this SubTaskQueryByPageParams.

        任务id

        :return: The task_id of this SubTaskQueryByPageParams.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SubTaskQueryByPageParams.

        任务id

        :param task_id: The task_id of this SubTaskQueryByPageParams.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_type_id(self):
        r"""Gets the task_type_id of this SubTaskQueryByPageParams.

        任务类型，1=拨测，2=冒烟

        :return: The task_type_id of this SubTaskQueryByPageParams.
        :rtype: str
        """
        return self._task_type_id

    @task_type_id.setter
    def task_type_id(self, task_type_id):
        r"""Sets the task_type_id of this SubTaskQueryByPageParams.

        任务类型，1=拨测，2=冒烟

        :param task_type_id: The task_type_id of this SubTaskQueryByPageParams.
        :type task_type_id: str
        """
        self._task_type_id = task_type_id

    @property
    def test_service_id(self):
        r"""Gets the test_service_id of this SubTaskQueryByPageParams.

        项目id

        :return: The test_service_id of this SubTaskQueryByPageParams.
        :rtype: str
        """
        return self._test_service_id

    @test_service_id.setter
    def test_service_id(self, test_service_id):
        r"""Sets the test_service_id of this SubTaskQueryByPageParams.

        项目id

        :param test_service_id: The test_service_id of this SubTaskQueryByPageParams.
        :type test_service_id: str
        """
        self._test_service_id = test_service_id

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
        if not isinstance(other, SubTaskQueryByPageParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
