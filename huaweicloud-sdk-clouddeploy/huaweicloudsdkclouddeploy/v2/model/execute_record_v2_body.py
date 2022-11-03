# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteRecordV2Body:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'duration': 'str',
        'state': 'str',
        'operator': 'str',
        'execution_id': 'str',
        'start_time': 'str',
        'nickname': 'str',
        'end_time': 'str',
        'release_id': 'int',
        'type': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'state': 'state',
        'operator': 'operator',
        'execution_id': 'execution_id',
        'start_time': 'start_time',
        'nickname': 'nickname',
        'end_time': 'end_time',
        'release_id': 'release_id',
        'type': 'type'
    }

    def __init__(self, duration=None, state=None, operator=None, execution_id=None, start_time=None, nickname=None, end_time=None, release_id=None, type=None):
        """ExecuteRecordV2Body

        The model defined in huaweicloud sdk

        :param duration: 执行用时
        :type duration: str
        :param state: 任务状态
        :type state: str
        :param operator: 操作人用户名
        :type operator: str
        :param execution_id: 执行记录ID
        :type execution_id: str
        :param start_time: 执行任务的开始时间
        :type start_time: str
        :param nickname: 操作人昵称
        :type nickname: str
        :param end_time: 执行任务的结束时间
        :type end_time: str
        :param release_id: 执行序列号
        :type release_id: int
        :param type: 类型
        :type type: str
        """
        
        

        self._duration = None
        self._state = None
        self._operator = None
        self._execution_id = None
        self._start_time = None
        self._nickname = None
        self._end_time = None
        self._release_id = None
        self._type = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if state is not None:
            self.state = state
        if operator is not None:
            self.operator = operator
        if execution_id is not None:
            self.execution_id = execution_id
        if start_time is not None:
            self.start_time = start_time
        if nickname is not None:
            self.nickname = nickname
        if end_time is not None:
            self.end_time = end_time
        if release_id is not None:
            self.release_id = release_id
        if type is not None:
            self.type = type

    @property
    def duration(self):
        """Gets the duration of this ExecuteRecordV2Body.

        执行用时

        :return: The duration of this ExecuteRecordV2Body.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ExecuteRecordV2Body.

        执行用时

        :param duration: The duration of this ExecuteRecordV2Body.
        :type duration: str
        """
        self._duration = duration

    @property
    def state(self):
        """Gets the state of this ExecuteRecordV2Body.

        任务状态

        :return: The state of this ExecuteRecordV2Body.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ExecuteRecordV2Body.

        任务状态

        :param state: The state of this ExecuteRecordV2Body.
        :type state: str
        """
        self._state = state

    @property
    def operator(self):
        """Gets the operator of this ExecuteRecordV2Body.

        操作人用户名

        :return: The operator of this ExecuteRecordV2Body.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ExecuteRecordV2Body.

        操作人用户名

        :param operator: The operator of this ExecuteRecordV2Body.
        :type operator: str
        """
        self._operator = operator

    @property
    def execution_id(self):
        """Gets the execution_id of this ExecuteRecordV2Body.

        执行记录ID

        :return: The execution_id of this ExecuteRecordV2Body.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this ExecuteRecordV2Body.

        执行记录ID

        :param execution_id: The execution_id of this ExecuteRecordV2Body.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def start_time(self):
        """Gets the start_time of this ExecuteRecordV2Body.

        执行任务的开始时间

        :return: The start_time of this ExecuteRecordV2Body.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ExecuteRecordV2Body.

        执行任务的开始时间

        :param start_time: The start_time of this ExecuteRecordV2Body.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def nickname(self):
        """Gets the nickname of this ExecuteRecordV2Body.

        操作人昵称

        :return: The nickname of this ExecuteRecordV2Body.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this ExecuteRecordV2Body.

        操作人昵称

        :param nickname: The nickname of this ExecuteRecordV2Body.
        :type nickname: str
        """
        self._nickname = nickname

    @property
    def end_time(self):
        """Gets the end_time of this ExecuteRecordV2Body.

        执行任务的结束时间

        :return: The end_time of this ExecuteRecordV2Body.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ExecuteRecordV2Body.

        执行任务的结束时间

        :param end_time: The end_time of this ExecuteRecordV2Body.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def release_id(self):
        """Gets the release_id of this ExecuteRecordV2Body.

        执行序列号

        :return: The release_id of this ExecuteRecordV2Body.
        :rtype: int
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this ExecuteRecordV2Body.

        执行序列号

        :param release_id: The release_id of this ExecuteRecordV2Body.
        :type release_id: int
        """
        self._release_id = release_id

    @property
    def type(self):
        """Gets the type of this ExecuteRecordV2Body.

        类型

        :return: The type of this ExecuteRecordV2Body.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExecuteRecordV2Body.

        类型

        :param type: The type of this ExecuteRecordV2Body.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ExecuteRecordV2Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
