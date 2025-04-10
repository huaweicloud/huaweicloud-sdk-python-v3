# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecretTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'secret_name': 'str',
        'rotation_func_urn': 'str',
        'task_status': 'str',
        'operate_type': 'str',
        'task_time': 'int',
        'attempt_nums': 'int',
        'task_error_code': 'str',
        'task_error_msg': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'secret_name': 'secret_name',
        'rotation_func_urn': 'rotation_func_urn',
        'task_status': 'task_status',
        'operate_type': 'operate_type',
        'task_time': 'task_time',
        'attempt_nums': 'attempt_nums',
        'task_error_code': 'task_error_code',
        'task_error_msg': 'task_error_msg'
    }

    def __init__(self, task_id=None, secret_name=None, rotation_func_urn=None, task_status=None, operate_type=None, task_time=None, attempt_nums=None, task_error_code=None, task_error_msg=None):
        r"""SecretTask

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param secret_name: 凭据名称。
        :type secret_name: str
        :param rotation_func_urn: FunctionGraph函数的urn。
        :type rotation_func_urn: str
        :param task_status: 任务状态。
        :type task_status: str
        :param operate_type: 轮转类型。
        :type operate_type: str
        :param task_time: 任务创建时间。
        :type task_time: int
        :param attempt_nums: 轮转尝试次数。
        :type attempt_nums: int
        :param task_error_code: 任务错误码。
        :type task_error_code: str
        :param task_error_msg: 任务错误信息。
        :type task_error_msg: str
        """
        
        

        self._task_id = None
        self._secret_name = None
        self._rotation_func_urn = None
        self._task_status = None
        self._operate_type = None
        self._task_time = None
        self._attempt_nums = None
        self._task_error_code = None
        self._task_error_msg = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if secret_name is not None:
            self.secret_name = secret_name
        if rotation_func_urn is not None:
            self.rotation_func_urn = rotation_func_urn
        if task_status is not None:
            self.task_status = task_status
        if operate_type is not None:
            self.operate_type = operate_type
        if task_time is not None:
            self.task_time = task_time
        if attempt_nums is not None:
            self.attempt_nums = attempt_nums
        if task_error_code is not None:
            self.task_error_code = task_error_code
        if task_error_msg is not None:
            self.task_error_msg = task_error_msg

    @property
    def task_id(self):
        r"""Gets the task_id of this SecretTask.

        任务ID

        :return: The task_id of this SecretTask.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SecretTask.

        任务ID

        :param task_id: The task_id of this SecretTask.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def secret_name(self):
        r"""Gets the secret_name of this SecretTask.

        凭据名称。

        :return: The secret_name of this SecretTask.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this SecretTask.

        凭据名称。

        :param secret_name: The secret_name of this SecretTask.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def rotation_func_urn(self):
        r"""Gets the rotation_func_urn of this SecretTask.

        FunctionGraph函数的urn。

        :return: The rotation_func_urn of this SecretTask.
        :rtype: str
        """
        return self._rotation_func_urn

    @rotation_func_urn.setter
    def rotation_func_urn(self, rotation_func_urn):
        r"""Sets the rotation_func_urn of this SecretTask.

        FunctionGraph函数的urn。

        :param rotation_func_urn: The rotation_func_urn of this SecretTask.
        :type rotation_func_urn: str
        """
        self._rotation_func_urn = rotation_func_urn

    @property
    def task_status(self):
        r"""Gets the task_status of this SecretTask.

        任务状态。

        :return: The task_status of this SecretTask.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this SecretTask.

        任务状态。

        :param task_status: The task_status of this SecretTask.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def operate_type(self):
        r"""Gets the operate_type of this SecretTask.

        轮转类型。

        :return: The operate_type of this SecretTask.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this SecretTask.

        轮转类型。

        :param operate_type: The operate_type of this SecretTask.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def task_time(self):
        r"""Gets the task_time of this SecretTask.

        任务创建时间。

        :return: The task_time of this SecretTask.
        :rtype: int
        """
        return self._task_time

    @task_time.setter
    def task_time(self, task_time):
        r"""Sets the task_time of this SecretTask.

        任务创建时间。

        :param task_time: The task_time of this SecretTask.
        :type task_time: int
        """
        self._task_time = task_time

    @property
    def attempt_nums(self):
        r"""Gets the attempt_nums of this SecretTask.

        轮转尝试次数。

        :return: The attempt_nums of this SecretTask.
        :rtype: int
        """
        return self._attempt_nums

    @attempt_nums.setter
    def attempt_nums(self, attempt_nums):
        r"""Sets the attempt_nums of this SecretTask.

        轮转尝试次数。

        :param attempt_nums: The attempt_nums of this SecretTask.
        :type attempt_nums: int
        """
        self._attempt_nums = attempt_nums

    @property
    def task_error_code(self):
        r"""Gets the task_error_code of this SecretTask.

        任务错误码。

        :return: The task_error_code of this SecretTask.
        :rtype: str
        """
        return self._task_error_code

    @task_error_code.setter
    def task_error_code(self, task_error_code):
        r"""Sets the task_error_code of this SecretTask.

        任务错误码。

        :param task_error_code: The task_error_code of this SecretTask.
        :type task_error_code: str
        """
        self._task_error_code = task_error_code

    @property
    def task_error_msg(self):
        r"""Gets the task_error_msg of this SecretTask.

        任务错误信息。

        :return: The task_error_msg of this SecretTask.
        :rtype: str
        """
        return self._task_error_msg

    @task_error_msg.setter
    def task_error_msg(self, task_error_msg):
        r"""Sets the task_error_msg of this SecretTask.

        任务错误信息。

        :param task_error_msg: The task_error_msg of this SecretTask.
        :type task_error_msg: str
        """
        self._task_error_msg = task_error_msg

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
        if not isinstance(other, SecretTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
