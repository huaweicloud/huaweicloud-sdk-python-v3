# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UCSTaskSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'target': 'str',
        'target_type': 'str',
        'wait_time_out': 'int',
        'type': 'str',
        'runway': 'str'
    }

    attribute_map = {
        'job_id': 'jobID',
        'target': 'target',
        'target_type': 'targetType',
        'wait_time_out': 'waitTimeOut',
        'type': 'type',
        'runway': 'runway'
    }

    def __init__(self, job_id=None, target=None, target_type=None, wait_time_out=None, type=None, runway=None):
        r"""UCSTaskSpec

        The model defined in huaweicloud sdk

        :param job_id: 所属job的ID
        :type job_id: str
        :param target: 执行目标
        :type target: str
        :param target_type: 执行目标类型
        :type target_type: str
        :param wait_time_out: Task执行等待时间，单位：秒
        :type wait_time_out: int
        :param type: Task类别
        :type type: str
        :param runway: 执行方式：parallel和serial二选一
        :type runway: str
        """
        
        

        self._job_id = None
        self._target = None
        self._target_type = None
        self._wait_time_out = None
        self._type = None
        self._runway = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if target is not None:
            self.target = target
        if target_type is not None:
            self.target_type = target_type
        if wait_time_out is not None:
            self.wait_time_out = wait_time_out
        if type is not None:
            self.type = type
        if runway is not None:
            self.runway = runway

    @property
    def job_id(self):
        r"""Gets the job_id of this UCSTaskSpec.

        所属job的ID

        :return: The job_id of this UCSTaskSpec.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this UCSTaskSpec.

        所属job的ID

        :param job_id: The job_id of this UCSTaskSpec.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def target(self):
        r"""Gets the target of this UCSTaskSpec.

        执行目标

        :return: The target of this UCSTaskSpec.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this UCSTaskSpec.

        执行目标

        :param target: The target of this UCSTaskSpec.
        :type target: str
        """
        self._target = target

    @property
    def target_type(self):
        r"""Gets the target_type of this UCSTaskSpec.

        执行目标类型

        :return: The target_type of this UCSTaskSpec.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this UCSTaskSpec.

        执行目标类型

        :param target_type: The target_type of this UCSTaskSpec.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def wait_time_out(self):
        r"""Gets the wait_time_out of this UCSTaskSpec.

        Task执行等待时间，单位：秒

        :return: The wait_time_out of this UCSTaskSpec.
        :rtype: int
        """
        return self._wait_time_out

    @wait_time_out.setter
    def wait_time_out(self, wait_time_out):
        r"""Sets the wait_time_out of this UCSTaskSpec.

        Task执行等待时间，单位：秒

        :param wait_time_out: The wait_time_out of this UCSTaskSpec.
        :type wait_time_out: int
        """
        self._wait_time_out = wait_time_out

    @property
    def type(self):
        r"""Gets the type of this UCSTaskSpec.

        Task类别

        :return: The type of this UCSTaskSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UCSTaskSpec.

        Task类别

        :param type: The type of this UCSTaskSpec.
        :type type: str
        """
        self._type = type

    @property
    def runway(self):
        r"""Gets the runway of this UCSTaskSpec.

        执行方式：parallel和serial二选一

        :return: The runway of this UCSTaskSpec.
        :rtype: str
        """
        return self._runway

    @runway.setter
    def runway(self, runway):
        r"""Sets the runway of this UCSTaskSpec.

        执行方式：parallel和serial二选一

        :param runway: The runway of this UCSTaskSpec.
        :type runway: str
        """
        self._runway = runway

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
        if not isinstance(other, UCSTaskSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
