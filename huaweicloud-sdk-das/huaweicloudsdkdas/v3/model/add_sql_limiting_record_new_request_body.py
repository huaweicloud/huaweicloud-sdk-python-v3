# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSqlLimitingRecordNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'type': 'str',
        'key_str': 'str',
        'max_waiting': 'int',
        'max_connection': 'int',
        'his_sql_limiting_switch': 'bool',
        'node_ids': 'list[str]',
        'automaticity': 'bool',
        'duration': 'int'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'type': 'type',
        'key_str': 'key_str',
        'max_waiting': 'max_waiting',
        'max_connection': 'max_connection',
        'his_sql_limiting_switch': 'his_sql_limiting_switch',
        'node_ids': 'node_ids',
        'automaticity': 'automaticity',
        'duration': 'duration'
    }

    def __init__(self, engine_type=None, type=None, key_str=None, max_waiting=None, max_connection=None, his_sql_limiting_switch=None, node_ids=None, automaticity=None, duration=None):
        r"""AddSqlLimitingRecordNewRequestBody

        The model defined in huaweicloud sdk

        :param engine_type: 引擎类型
        :type engine_type: str
        :param type: SQL类型
        :type type: str
        :param key_str: 限流规则
        :type key_str: str
        :param max_waiting: 最大等待时间
        :type max_waiting: int
        :param max_connection: 最大并发数
        :type max_connection: int
        :param his_sql_limiting_switch: 历史会话限流开关
        :type his_sql_limiting_switch: bool
        :param node_ids: 节点ID列表
        :type node_ids: list[str]
        :param automaticity: 是否自动化
        :type automaticity: bool
        :param duration: 过期时间
        :type duration: int
        """
        
        

        self._engine_type = None
        self._type = None
        self._key_str = None
        self._max_waiting = None
        self._max_connection = None
        self._his_sql_limiting_switch = None
        self._node_ids = None
        self._automaticity = None
        self._duration = None
        self.discriminator = None

        self.engine_type = engine_type
        self.type = type
        self.key_str = key_str
        if max_waiting is not None:
            self.max_waiting = max_waiting
        self.max_connection = max_connection
        if his_sql_limiting_switch is not None:
            self.his_sql_limiting_switch = his_sql_limiting_switch
        if node_ids is not None:
            self.node_ids = node_ids
        if automaticity is not None:
            self.automaticity = automaticity
        if duration is not None:
            self.duration = duration

    @property
    def engine_type(self):
        r"""Gets the engine_type of this AddSqlLimitingRecordNewRequestBody.

        引擎类型

        :return: The engine_type of this AddSqlLimitingRecordNewRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this AddSqlLimitingRecordNewRequestBody.

        引擎类型

        :param engine_type: The engine_type of this AddSqlLimitingRecordNewRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def type(self):
        r"""Gets the type of this AddSqlLimitingRecordNewRequestBody.

        SQL类型

        :return: The type of this AddSqlLimitingRecordNewRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AddSqlLimitingRecordNewRequestBody.

        SQL类型

        :param type: The type of this AddSqlLimitingRecordNewRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def key_str(self):
        r"""Gets the key_str of this AddSqlLimitingRecordNewRequestBody.

        限流规则

        :return: The key_str of this AddSqlLimitingRecordNewRequestBody.
        :rtype: str
        """
        return self._key_str

    @key_str.setter
    def key_str(self, key_str):
        r"""Sets the key_str of this AddSqlLimitingRecordNewRequestBody.

        限流规则

        :param key_str: The key_str of this AddSqlLimitingRecordNewRequestBody.
        :type key_str: str
        """
        self._key_str = key_str

    @property
    def max_waiting(self):
        r"""Gets the max_waiting of this AddSqlLimitingRecordNewRequestBody.

        最大等待时间

        :return: The max_waiting of this AddSqlLimitingRecordNewRequestBody.
        :rtype: int
        """
        return self._max_waiting

    @max_waiting.setter
    def max_waiting(self, max_waiting):
        r"""Sets the max_waiting of this AddSqlLimitingRecordNewRequestBody.

        最大等待时间

        :param max_waiting: The max_waiting of this AddSqlLimitingRecordNewRequestBody.
        :type max_waiting: int
        """
        self._max_waiting = max_waiting

    @property
    def max_connection(self):
        r"""Gets the max_connection of this AddSqlLimitingRecordNewRequestBody.

        最大并发数

        :return: The max_connection of this AddSqlLimitingRecordNewRequestBody.
        :rtype: int
        """
        return self._max_connection

    @max_connection.setter
    def max_connection(self, max_connection):
        r"""Sets the max_connection of this AddSqlLimitingRecordNewRequestBody.

        最大并发数

        :param max_connection: The max_connection of this AddSqlLimitingRecordNewRequestBody.
        :type max_connection: int
        """
        self._max_connection = max_connection

    @property
    def his_sql_limiting_switch(self):
        r"""Gets the his_sql_limiting_switch of this AddSqlLimitingRecordNewRequestBody.

        历史会话限流开关

        :return: The his_sql_limiting_switch of this AddSqlLimitingRecordNewRequestBody.
        :rtype: bool
        """
        return self._his_sql_limiting_switch

    @his_sql_limiting_switch.setter
    def his_sql_limiting_switch(self, his_sql_limiting_switch):
        r"""Sets the his_sql_limiting_switch of this AddSqlLimitingRecordNewRequestBody.

        历史会话限流开关

        :param his_sql_limiting_switch: The his_sql_limiting_switch of this AddSqlLimitingRecordNewRequestBody.
        :type his_sql_limiting_switch: bool
        """
        self._his_sql_limiting_switch = his_sql_limiting_switch

    @property
    def node_ids(self):
        r"""Gets the node_ids of this AddSqlLimitingRecordNewRequestBody.

        节点ID列表

        :return: The node_ids of this AddSqlLimitingRecordNewRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this AddSqlLimitingRecordNewRequestBody.

        节点ID列表

        :param node_ids: The node_ids of this AddSqlLimitingRecordNewRequestBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def automaticity(self):
        r"""Gets the automaticity of this AddSqlLimitingRecordNewRequestBody.

        是否自动化

        :return: The automaticity of this AddSqlLimitingRecordNewRequestBody.
        :rtype: bool
        """
        return self._automaticity

    @automaticity.setter
    def automaticity(self, automaticity):
        r"""Sets the automaticity of this AddSqlLimitingRecordNewRequestBody.

        是否自动化

        :param automaticity: The automaticity of this AddSqlLimitingRecordNewRequestBody.
        :type automaticity: bool
        """
        self._automaticity = automaticity

    @property
    def duration(self):
        r"""Gets the duration of this AddSqlLimitingRecordNewRequestBody.

        过期时间

        :return: The duration of this AddSqlLimitingRecordNewRequestBody.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this AddSqlLimitingRecordNewRequestBody.

        过期时间

        :param duration: The duration of this AddSqlLimitingRecordNewRequestBody.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, AddSqlLimitingRecordNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
