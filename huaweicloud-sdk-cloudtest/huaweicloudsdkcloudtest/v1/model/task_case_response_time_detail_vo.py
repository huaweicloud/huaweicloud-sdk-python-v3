# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskCaseResponseTimeDetailVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_id': 'str',
        'case_name': 'str',
        'end_time': 'int',
        'error_reason': 'str',
        'response_time': 'int',
        'service_id': 'str',
        'service_name': 'str',
        'start_time': 'int',
        'state': 'str',
        'sub_task_id': 'str',
        'tag_id': 'str',
        'tag_name': 'str',
        'task_case_id': 'str',
        'task_id': 'str',
        'task_name': 'str',
        'task_type_id': 'str',
        'test_suite_type': 'int'
    }

    attribute_map = {
        'case_id': 'case_id',
        'case_name': 'case_name',
        'end_time': 'end_time',
        'error_reason': 'error_reason',
        'response_time': 'response_time',
        'service_id': 'service_id',
        'service_name': 'service_name',
        'start_time': 'start_time',
        'state': 'state',
        'sub_task_id': 'sub_task_id',
        'tag_id': 'tag_id',
        'tag_name': 'tag_name',
        'task_case_id': 'task_case_id',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_type_id': 'task_type_id',
        'test_suite_type': 'test_suite_type'
    }

    def __init__(self, case_id=None, case_name=None, end_time=None, error_reason=None, response_time=None, service_id=None, service_name=None, start_time=None, state=None, sub_task_id=None, tag_id=None, tag_name=None, task_case_id=None, task_id=None, task_name=None, task_type_id=None, test_suite_type=None):
        r"""TaskCaseResponseTimeDetailVo

        The model defined in huaweicloud sdk

        :param case_id: 用例ID
        :type case_id: str
        :param case_name: 用例名称
        :type case_name: str
        :param end_time: 用例结束时间
        :type end_time: int
        :param error_reason: 用例状态
        :type error_reason: str
        :param response_time: 用例响应时间
        :type response_time: int
        :param service_id: 服务ID
        :type service_id: str
        :param service_name: 服务名称
        :type service_name: str
        :param start_time: 用例开始时间
        :type start_time: int
        :param state: 用例状态
        :type state: str
        :param sub_task_id: 子任务ID
        :type sub_task_id: str
        :param tag_id: 已废弃
        :type tag_id: str
        :param tag_name: 已废弃
        :type tag_name: str
        :param task_case_id: 任务和用例关联关系的ID
        :type task_case_id: str
        :param task_id: 任务ID
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        :param task_type_id: 任务类型，1&#x3D;拨测，2&#x3D;冒烟，4&#x3D;部署测试，5&#x3D;小网拨测
        :type task_type_id: str
        :param test_suite_type: 测试套类型
        :type test_suite_type: int
        """
        
        

        self._case_id = None
        self._case_name = None
        self._end_time = None
        self._error_reason = None
        self._response_time = None
        self._service_id = None
        self._service_name = None
        self._start_time = None
        self._state = None
        self._sub_task_id = None
        self._tag_id = None
        self._tag_name = None
        self._task_case_id = None
        self._task_id = None
        self._task_name = None
        self._task_type_id = None
        self._test_suite_type = None
        self.discriminator = None

        if case_id is not None:
            self.case_id = case_id
        if case_name is not None:
            self.case_name = case_name
        if end_time is not None:
            self.end_time = end_time
        if error_reason is not None:
            self.error_reason = error_reason
        if response_time is not None:
            self.response_time = response_time
        if service_id is not None:
            self.service_id = service_id
        if service_name is not None:
            self.service_name = service_name
        if start_time is not None:
            self.start_time = start_time
        if state is not None:
            self.state = state
        if sub_task_id is not None:
            self.sub_task_id = sub_task_id
        if tag_id is not None:
            self.tag_id = tag_id
        if tag_name is not None:
            self.tag_name = tag_name
        if task_case_id is not None:
            self.task_case_id = task_case_id
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_type_id is not None:
            self.task_type_id = task_type_id
        if test_suite_type is not None:
            self.test_suite_type = test_suite_type

    @property
    def case_id(self):
        r"""Gets the case_id of this TaskCaseResponseTimeDetailVo.

        用例ID

        :return: The case_id of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        r"""Sets the case_id of this TaskCaseResponseTimeDetailVo.

        用例ID

        :param case_id: The case_id of this TaskCaseResponseTimeDetailVo.
        :type case_id: str
        """
        self._case_id = case_id

    @property
    def case_name(self):
        r"""Gets the case_name of this TaskCaseResponseTimeDetailVo.

        用例名称

        :return: The case_name of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._case_name

    @case_name.setter
    def case_name(self, case_name):
        r"""Sets the case_name of this TaskCaseResponseTimeDetailVo.

        用例名称

        :param case_name: The case_name of this TaskCaseResponseTimeDetailVo.
        :type case_name: str
        """
        self._case_name = case_name

    @property
    def end_time(self):
        r"""Gets the end_time of this TaskCaseResponseTimeDetailVo.

        用例结束时间

        :return: The end_time of this TaskCaseResponseTimeDetailVo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TaskCaseResponseTimeDetailVo.

        用例结束时间

        :param end_time: The end_time of this TaskCaseResponseTimeDetailVo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def error_reason(self):
        r"""Gets the error_reason of this TaskCaseResponseTimeDetailVo.

        用例状态

        :return: The error_reason of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        r"""Sets the error_reason of this TaskCaseResponseTimeDetailVo.

        用例状态

        :param error_reason: The error_reason of this TaskCaseResponseTimeDetailVo.
        :type error_reason: str
        """
        self._error_reason = error_reason

    @property
    def response_time(self):
        r"""Gets the response_time of this TaskCaseResponseTimeDetailVo.

        用例响应时间

        :return: The response_time of this TaskCaseResponseTimeDetailVo.
        :rtype: int
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        r"""Sets the response_time of this TaskCaseResponseTimeDetailVo.

        用例响应时间

        :param response_time: The response_time of this TaskCaseResponseTimeDetailVo.
        :type response_time: int
        """
        self._response_time = response_time

    @property
    def service_id(self):
        r"""Gets the service_id of this TaskCaseResponseTimeDetailVo.

        服务ID

        :return: The service_id of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this TaskCaseResponseTimeDetailVo.

        服务ID

        :param service_id: The service_id of this TaskCaseResponseTimeDetailVo.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def service_name(self):
        r"""Gets the service_name of this TaskCaseResponseTimeDetailVo.

        服务名称

        :return: The service_name of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this TaskCaseResponseTimeDetailVo.

        服务名称

        :param service_name: The service_name of this TaskCaseResponseTimeDetailVo.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def start_time(self):
        r"""Gets the start_time of this TaskCaseResponseTimeDetailVo.

        用例开始时间

        :return: The start_time of this TaskCaseResponseTimeDetailVo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TaskCaseResponseTimeDetailVo.

        用例开始时间

        :param start_time: The start_time of this TaskCaseResponseTimeDetailVo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def state(self):
        r"""Gets the state of this TaskCaseResponseTimeDetailVo.

        用例状态

        :return: The state of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this TaskCaseResponseTimeDetailVo.

        用例状态

        :param state: The state of this TaskCaseResponseTimeDetailVo.
        :type state: str
        """
        self._state = state

    @property
    def sub_task_id(self):
        r"""Gets the sub_task_id of this TaskCaseResponseTimeDetailVo.

        子任务ID

        :return: The sub_task_id of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._sub_task_id

    @sub_task_id.setter
    def sub_task_id(self, sub_task_id):
        r"""Sets the sub_task_id of this TaskCaseResponseTimeDetailVo.

        子任务ID

        :param sub_task_id: The sub_task_id of this TaskCaseResponseTimeDetailVo.
        :type sub_task_id: str
        """
        self._sub_task_id = sub_task_id

    @property
    def tag_id(self):
        r"""Gets the tag_id of this TaskCaseResponseTimeDetailVo.

        已废弃

        :return: The tag_id of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this TaskCaseResponseTimeDetailVo.

        已废弃

        :param tag_id: The tag_id of this TaskCaseResponseTimeDetailVo.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def tag_name(self):
        r"""Gets the tag_name of this TaskCaseResponseTimeDetailVo.

        已废弃

        :return: The tag_name of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        r"""Sets the tag_name of this TaskCaseResponseTimeDetailVo.

        已废弃

        :param tag_name: The tag_name of this TaskCaseResponseTimeDetailVo.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def task_case_id(self):
        r"""Gets the task_case_id of this TaskCaseResponseTimeDetailVo.

        任务和用例关联关系的ID

        :return: The task_case_id of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._task_case_id

    @task_case_id.setter
    def task_case_id(self, task_case_id):
        r"""Sets the task_case_id of this TaskCaseResponseTimeDetailVo.

        任务和用例关联关系的ID

        :param task_case_id: The task_case_id of this TaskCaseResponseTimeDetailVo.
        :type task_case_id: str
        """
        self._task_case_id = task_case_id

    @property
    def task_id(self):
        r"""Gets the task_id of this TaskCaseResponseTimeDetailVo.

        任务ID

        :return: The task_id of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this TaskCaseResponseTimeDetailVo.

        任务ID

        :param task_id: The task_id of this TaskCaseResponseTimeDetailVo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this TaskCaseResponseTimeDetailVo.

        任务名称

        :return: The task_name of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this TaskCaseResponseTimeDetailVo.

        任务名称

        :param task_name: The task_name of this TaskCaseResponseTimeDetailVo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type_id(self):
        r"""Gets the task_type_id of this TaskCaseResponseTimeDetailVo.

        任务类型，1=拨测，2=冒烟，4=部署测试，5=小网拨测

        :return: The task_type_id of this TaskCaseResponseTimeDetailVo.
        :rtype: str
        """
        return self._task_type_id

    @task_type_id.setter
    def task_type_id(self, task_type_id):
        r"""Sets the task_type_id of this TaskCaseResponseTimeDetailVo.

        任务类型，1=拨测，2=冒烟，4=部署测试，5=小网拨测

        :param task_type_id: The task_type_id of this TaskCaseResponseTimeDetailVo.
        :type task_type_id: str
        """
        self._task_type_id = task_type_id

    @property
    def test_suite_type(self):
        r"""Gets the test_suite_type of this TaskCaseResponseTimeDetailVo.

        测试套类型

        :return: The test_suite_type of this TaskCaseResponseTimeDetailVo.
        :rtype: int
        """
        return self._test_suite_type

    @test_suite_type.setter
    def test_suite_type(self, test_suite_type):
        r"""Sets the test_suite_type of this TaskCaseResponseTimeDetailVo.

        测试套类型

        :param test_suite_type: The test_suite_type of this TaskCaseResponseTimeDetailVo.
        :type test_suite_type: int
        """
        self._test_suite_type = test_suite_type

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
        if not isinstance(other, TaskCaseResponseTimeDetailVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
