# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamingJobInfoDto:

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
        'job_name': 'str',
        'job_input_type': 'str',
        'job_description': 'str',
        'job_state': 'str',
        'status': 'str',
        'rtu': 'int',
        'created_time': 'str',
        'modified_time': 'str',
        'user_id': 'str',
        'has_savepoint': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'job_input_type': 'job_input_type',
        'job_description': 'job_description',
        'job_state': 'job_state',
        'status': 'status',
        'rtu': 'rtu',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'user_id': 'user_id',
        'has_savepoint': 'has_savepoint'
    }

    def __init__(self, job_id=None, job_name=None, job_input_type=None, job_description=None, job_state=None, status=None, rtu=None, created_time=None, modified_time=None, user_id=None, has_savepoint=None):
        """StreamingJobInfoDto

        The model defined in huaweicloud sdk

        :param job_id: 作业ID
        :type job_id: str
        :param job_name: 作业名称
        :type job_name: str
        :param job_input_type: 接收数据类型
        :type job_input_type: str
        :param job_description: 作业描述
        :type job_description: str
        :param job_state: 作业状态
        :type job_state: str
        :param status: 操作状态
        :type status: str
        :param rtu: 运行作业的RTU个数
        :type rtu: int
        :param created_time: 创建时间
        :type created_time: str
        :param modified_time: 修改时间
        :type modified_time: str
        :param user_id: 用户ID
        :type user_id: str
        :param has_savepoint: 已停止作业是否有历史缓存数据
        :type has_savepoint: bool
        """
        
        

        self._job_id = None
        self._job_name = None
        self._job_input_type = None
        self._job_description = None
        self._job_state = None
        self._status = None
        self._rtu = None
        self._created_time = None
        self._modified_time = None
        self._user_id = None
        self._has_savepoint = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if job_input_type is not None:
            self.job_input_type = job_input_type
        if job_description is not None:
            self.job_description = job_description
        if job_state is not None:
            self.job_state = job_state
        if status is not None:
            self.status = status
        if rtu is not None:
            self.rtu = rtu
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if user_id is not None:
            self.user_id = user_id
        if has_savepoint is not None:
            self.has_savepoint = has_savepoint

    @property
    def job_id(self):
        """Gets the job_id of this StreamingJobInfoDto.

        作业ID

        :return: The job_id of this StreamingJobInfoDto.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this StreamingJobInfoDto.

        作业ID

        :param job_id: The job_id of this StreamingJobInfoDto.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this StreamingJobInfoDto.

        作业名称

        :return: The job_name of this StreamingJobInfoDto.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this StreamingJobInfoDto.

        作业名称

        :param job_name: The job_name of this StreamingJobInfoDto.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_input_type(self):
        """Gets the job_input_type of this StreamingJobInfoDto.

        接收数据类型

        :return: The job_input_type of this StreamingJobInfoDto.
        :rtype: str
        """
        return self._job_input_type

    @job_input_type.setter
    def job_input_type(self, job_input_type):
        """Sets the job_input_type of this StreamingJobInfoDto.

        接收数据类型

        :param job_input_type: The job_input_type of this StreamingJobInfoDto.
        :type job_input_type: str
        """
        self._job_input_type = job_input_type

    @property
    def job_description(self):
        """Gets the job_description of this StreamingJobInfoDto.

        作业描述

        :return: The job_description of this StreamingJobInfoDto.
        :rtype: str
        """
        return self._job_description

    @job_description.setter
    def job_description(self, job_description):
        """Sets the job_description of this StreamingJobInfoDto.

        作业描述

        :param job_description: The job_description of this StreamingJobInfoDto.
        :type job_description: str
        """
        self._job_description = job_description

    @property
    def job_state(self):
        """Gets the job_state of this StreamingJobInfoDto.

        作业状态

        :return: The job_state of this StreamingJobInfoDto.
        :rtype: str
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """Sets the job_state of this StreamingJobInfoDto.

        作业状态

        :param job_state: The job_state of this StreamingJobInfoDto.
        :type job_state: str
        """
        self._job_state = job_state

    @property
    def status(self):
        """Gets the status of this StreamingJobInfoDto.

        操作状态

        :return: The status of this StreamingJobInfoDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StreamingJobInfoDto.

        操作状态

        :param status: The status of this StreamingJobInfoDto.
        :type status: str
        """
        self._status = status

    @property
    def rtu(self):
        """Gets the rtu of this StreamingJobInfoDto.

        运行作业的RTU个数

        :return: The rtu of this StreamingJobInfoDto.
        :rtype: int
        """
        return self._rtu

    @rtu.setter
    def rtu(self, rtu):
        """Sets the rtu of this StreamingJobInfoDto.

        运行作业的RTU个数

        :param rtu: The rtu of this StreamingJobInfoDto.
        :type rtu: int
        """
        self._rtu = rtu

    @property
    def created_time(self):
        """Gets the created_time of this StreamingJobInfoDto.

        创建时间

        :return: The created_time of this StreamingJobInfoDto.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this StreamingJobInfoDto.

        创建时间

        :param created_time: The created_time of this StreamingJobInfoDto.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        """Gets the modified_time of this StreamingJobInfoDto.

        修改时间

        :return: The modified_time of this StreamingJobInfoDto.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this StreamingJobInfoDto.

        修改时间

        :param modified_time: The modified_time of this StreamingJobInfoDto.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def user_id(self):
        """Gets the user_id of this StreamingJobInfoDto.

        用户ID

        :return: The user_id of this StreamingJobInfoDto.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this StreamingJobInfoDto.

        用户ID

        :param user_id: The user_id of this StreamingJobInfoDto.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def has_savepoint(self):
        """Gets the has_savepoint of this StreamingJobInfoDto.

        已停止作业是否有历史缓存数据

        :return: The has_savepoint of this StreamingJobInfoDto.
        :rtype: bool
        """
        return self._has_savepoint

    @has_savepoint.setter
    def has_savepoint(self, has_savepoint):
        """Sets the has_savepoint of this StreamingJobInfoDto.

        已停止作业是否有历史缓存数据

        :param has_savepoint: The has_savepoint of this StreamingJobInfoDto.
        :type has_savepoint: bool
        """
        self._has_savepoint = has_savepoint

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
        if not isinstance(other, StreamingJobInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
