# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistorySessionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'pid': 'str',
        'x_language': 'str',
        'user_name': 'str',
        'database_name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'pid': 'pid',
        'x_language': 'X-Language',
        'user_name': 'user_name',
        'database_name': 'database_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, pid=None, x_language=None, user_name=None, database_name=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ListHistorySessionsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param pid: 进程ID
        :type pid: str
        :param x_language: 语言。默认en-us。
        :type x_language: str
        :param user_name: 用户名
        :type user_name: str
        :param database_name: 数据库名
        :type database_name: str
        :param start_time: 参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。
        :type start_time: int
        :param end_time: 参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。
        :type end_time: int
        :param offset: 参数解释： 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，值为0表示从第一条数据开始查询）。 约束限制： 必须为数字，不能为负数。 取值范围： 大于等于0的整数。 默认取值： 0
        :type offset: int
        :param limit: 参数解释： 查询记录数。 约束限制： 不涉及。 取值范围： [1, 1000] 默认取值： 100
        :type limit: int
        """
        
        

        self._instance_id = None
        self._pid = None
        self._x_language = None
        self._user_name = None
        self._database_name = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if pid is not None:
            self.pid = pid
        if x_language is not None:
            self.x_language = x_language
        if user_name is not None:
            self.user_name = user_name
        if database_name is not None:
            self.database_name = database_name
        self.start_time = start_time
        self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListHistorySessionsRequest.

        实例ID。

        :return: The instance_id of this ListHistorySessionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListHistorySessionsRequest.

        实例ID。

        :param instance_id: The instance_id of this ListHistorySessionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def pid(self):
        r"""Gets the pid of this ListHistorySessionsRequest.

        进程ID

        :return: The pid of this ListHistorySessionsRequest.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this ListHistorySessionsRequest.

        进程ID

        :param pid: The pid of this ListHistorySessionsRequest.
        :type pid: str
        """
        self._pid = pid

    @property
    def x_language(self):
        r"""Gets the x_language of this ListHistorySessionsRequest.

        语言。默认en-us。

        :return: The x_language of this ListHistorySessionsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListHistorySessionsRequest.

        语言。默认en-us。

        :param x_language: The x_language of this ListHistorySessionsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def user_name(self):
        r"""Gets the user_name of this ListHistorySessionsRequest.

        用户名

        :return: The user_name of this ListHistorySessionsRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListHistorySessionsRequest.

        用户名

        :param user_name: The user_name of this ListHistorySessionsRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ListHistorySessionsRequest.

        数据库名

        :return: The database_name of this ListHistorySessionsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListHistorySessionsRequest.

        数据库名

        :param database_name: The database_name of this ListHistorySessionsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ListHistorySessionsRequest.

        参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :return: The start_time of this ListHistorySessionsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListHistorySessionsRequest.

        参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :param start_time: The start_time of this ListHistorySessionsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListHistorySessionsRequest.

        参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :return: The end_time of this ListHistorySessionsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListHistorySessionsRequest.

        参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :param end_time: The end_time of this ListHistorySessionsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListHistorySessionsRequest.

        参数解释： 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，值为0表示从第一条数据开始查询）。 约束限制： 必须为数字，不能为负数。 取值范围： 大于等于0的整数。 默认取值： 0

        :return: The offset of this ListHistorySessionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHistorySessionsRequest.

        参数解释： 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，值为0表示从第一条数据开始查询）。 约束限制： 必须为数字，不能为负数。 取值范围： 大于等于0的整数。 默认取值： 0

        :param offset: The offset of this ListHistorySessionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListHistorySessionsRequest.

        参数解释： 查询记录数。 约束限制： 不涉及。 取值范围： [1, 1000] 默认取值： 100

        :return: The limit of this ListHistorySessionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHistorySessionsRequest.

        参数解释： 查询记录数。 约束限制： 不涉及。 取值范围： [1, 1000] 默认取值： 100

        :param limit: The limit of this ListHistorySessionsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListHistorySessionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
