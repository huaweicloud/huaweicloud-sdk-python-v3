# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteInfoVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'timestamp': 'int',
        'duration': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'execute_times': 'int'
    }

    attribute_map = {
        'time': 'time',
        'timestamp': 'timestamp',
        'duration': 'duration',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'execute_times': 'execute_times'
    }

    def __init__(self, time=None, timestamp=None, duration=None, user_id=None, user_name=None, execute_times=None):
        """ExecuteInfoVo

        The model defined in huaweicloud sdk

        :param time: 执行开始时间
        :type time: str
        :param timestamp: 执行开始时间时间戳
        :type timestamp: int
        :param duration: 执行时长
        :type duration: str
        :param user_id: 用户ID
        :type user_id: str
        :param user_name: 用户名称
        :type user_name: str
        :param execute_times: 执行次数
        :type execute_times: int
        """
        
        

        self._time = None
        self._timestamp = None
        self._duration = None
        self._user_id = None
        self._user_name = None
        self._execute_times = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if timestamp is not None:
            self.timestamp = timestamp
        if duration is not None:
            self.duration = duration
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if execute_times is not None:
            self.execute_times = execute_times

    @property
    def time(self):
        """Gets the time of this ExecuteInfoVo.

        执行开始时间

        :return: The time of this ExecuteInfoVo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ExecuteInfoVo.

        执行开始时间

        :param time: The time of this ExecuteInfoVo.
        :type time: str
        """
        self._time = time

    @property
    def timestamp(self):
        """Gets the timestamp of this ExecuteInfoVo.

        执行开始时间时间戳

        :return: The timestamp of this ExecuteInfoVo.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ExecuteInfoVo.

        执行开始时间时间戳

        :param timestamp: The timestamp of this ExecuteInfoVo.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def duration(self):
        """Gets the duration of this ExecuteInfoVo.

        执行时长

        :return: The duration of this ExecuteInfoVo.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ExecuteInfoVo.

        执行时长

        :param duration: The duration of this ExecuteInfoVo.
        :type duration: str
        """
        self._duration = duration

    @property
    def user_id(self):
        """Gets the user_id of this ExecuteInfoVo.

        用户ID

        :return: The user_id of this ExecuteInfoVo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ExecuteInfoVo.

        用户ID

        :param user_id: The user_id of this ExecuteInfoVo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this ExecuteInfoVo.

        用户名称

        :return: The user_name of this ExecuteInfoVo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ExecuteInfoVo.

        用户名称

        :param user_name: The user_name of this ExecuteInfoVo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def execute_times(self):
        """Gets the execute_times of this ExecuteInfoVo.

        执行次数

        :return: The execute_times of this ExecuteInfoVo.
        :rtype: int
        """
        return self._execute_times

    @execute_times.setter
    def execute_times(self, execute_times):
        """Sets the execute_times of this ExecuteInfoVo.

        执行次数

        :param execute_times: The execute_times of this ExecuteInfoVo.
        :type execute_times: int
        """
        self._execute_times = execute_times

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
        if not isinstance(other, ExecuteInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
