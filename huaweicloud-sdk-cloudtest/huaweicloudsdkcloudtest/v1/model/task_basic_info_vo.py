# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskBasicInfoVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_reason': 'str',
        'id': 'str',
        'name': 'str',
        'task_state': 'int',
        'test_suite_type': 'int'
    }

    attribute_map = {
        'error_reason': 'error_reason',
        'id': 'id',
        'name': 'name',
        'task_state': 'task_state',
        'test_suite_type': 'test_suite_type'
    }

    def __init__(self, error_reason=None, id=None, name=None, task_state=None, test_suite_type=None):
        r"""TaskBasicInfoVo

        The model defined in huaweicloud sdk

        :param error_reason: 任务状态
        :type error_reason: str
        :param id: 任务ID
        :type id: str
        :param name: 任务名称
        :type name: str
        :param task_state: 任务类型
        :type task_state: int
        :param test_suite_type: 测试套类型
        :type test_suite_type: int
        """
        
        

        self._error_reason = None
        self._id = None
        self._name = None
        self._task_state = None
        self._test_suite_type = None
        self.discriminator = None

        if error_reason is not None:
            self.error_reason = error_reason
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if task_state is not None:
            self.task_state = task_state
        if test_suite_type is not None:
            self.test_suite_type = test_suite_type

    @property
    def error_reason(self):
        r"""Gets the error_reason of this TaskBasicInfoVo.

        任务状态

        :return: The error_reason of this TaskBasicInfoVo.
        :rtype: str
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        r"""Sets the error_reason of this TaskBasicInfoVo.

        任务状态

        :param error_reason: The error_reason of this TaskBasicInfoVo.
        :type error_reason: str
        """
        self._error_reason = error_reason

    @property
    def id(self):
        r"""Gets the id of this TaskBasicInfoVo.

        任务ID

        :return: The id of this TaskBasicInfoVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskBasicInfoVo.

        任务ID

        :param id: The id of this TaskBasicInfoVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TaskBasicInfoVo.

        任务名称

        :return: The name of this TaskBasicInfoVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskBasicInfoVo.

        任务名称

        :param name: The name of this TaskBasicInfoVo.
        :type name: str
        """
        self._name = name

    @property
    def task_state(self):
        r"""Gets the task_state of this TaskBasicInfoVo.

        任务类型

        :return: The task_state of this TaskBasicInfoVo.
        :rtype: int
        """
        return self._task_state

    @task_state.setter
    def task_state(self, task_state):
        r"""Sets the task_state of this TaskBasicInfoVo.

        任务类型

        :param task_state: The task_state of this TaskBasicInfoVo.
        :type task_state: int
        """
        self._task_state = task_state

    @property
    def test_suite_type(self):
        r"""Gets the test_suite_type of this TaskBasicInfoVo.

        测试套类型

        :return: The test_suite_type of this TaskBasicInfoVo.
        :rtype: int
        """
        return self._test_suite_type

    @test_suite_type.setter
    def test_suite_type(self, test_suite_type):
        r"""Sets the test_suite_type of this TaskBasicInfoVo.

        测试套类型

        :param test_suite_type: The test_suite_type of this TaskBasicInfoVo.
        :type test_suite_type: int
        """
        self._test_suite_type = test_suite_type

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
        if not isinstance(other, TaskBasicInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
