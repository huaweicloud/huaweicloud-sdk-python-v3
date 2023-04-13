# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'int',
        'db_enable': 'bool',
        'db_shadow_repository': 'str',
        'db_shadow_type': 'str',
        'log_level': 'str',
        'log_path': 'str',
        'main_switch': 'bool',
        'redis_enable': 'bool',
        'redis_shadow_key_prefix': 'str',
        'redis_shadow_repository': 'str',
        'redis_shadow_type': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'db_enable': 'db_enable',
        'db_shadow_repository': 'db_shadow_repository',
        'db_shadow_type': 'db_shadow_type',
        'log_level': 'log_level',
        'log_path': 'log_path',
        'main_switch': 'main_switch',
        'redis_enable': 'redis_enable',
        'redis_shadow_key_prefix': 'redis_shadow_key_prefix',
        'redis_shadow_repository': 'redis_shadow_repository',
        'redis_shadow_type': 'redis_shadow_type'
    }

    def __init__(self, agent_id=None, db_enable=None, db_shadow_repository=None, db_shadow_type=None, log_level=None, log_path=None, main_switch=None, redis_enable=None, redis_shadow_key_prefix=None, redis_shadow_repository=None, redis_shadow_type=None):
        """AgentConfig

        The model defined in huaweicloud sdk

        :param agent_id: 探针id
        :type agent_id: int
        :param db_enable: 是否开启数据库影子规则
        :type db_enable: bool
        :param db_shadow_repository: 数据库影子库名称
        :type db_shadow_repository: str
        :param db_shadow_type: 数据库影子库类型
        :type db_shadow_type: str
        :param log_level: 日志级别，枚举值：INFO，DEBUG，WARN，ERROR
        :type log_level: str
        :param log_path: 日志路径
        :type log_path: str
        :param main_switch: 影子规则开关
        :type main_switch: bool
        :param redis_enable: 是否开启redis影子库规则
        :type redis_enable: bool
        :param redis_shadow_key_prefix: redis影子库key前缀
        :type redis_shadow_key_prefix: str
        :param redis_shadow_repository: redis影子库名称
        :type redis_shadow_repository: str
        :param redis_shadow_type: redis影子库类型
        :type redis_shadow_type: str
        """
        
        

        self._agent_id = None
        self._db_enable = None
        self._db_shadow_repository = None
        self._db_shadow_type = None
        self._log_level = None
        self._log_path = None
        self._main_switch = None
        self._redis_enable = None
        self._redis_shadow_key_prefix = None
        self._redis_shadow_repository = None
        self._redis_shadow_type = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if db_enable is not None:
            self.db_enable = db_enable
        if db_shadow_repository is not None:
            self.db_shadow_repository = db_shadow_repository
        if db_shadow_type is not None:
            self.db_shadow_type = db_shadow_type
        if log_level is not None:
            self.log_level = log_level
        if log_path is not None:
            self.log_path = log_path
        if main_switch is not None:
            self.main_switch = main_switch
        if redis_enable is not None:
            self.redis_enable = redis_enable
        if redis_shadow_key_prefix is not None:
            self.redis_shadow_key_prefix = redis_shadow_key_prefix
        if redis_shadow_repository is not None:
            self.redis_shadow_repository = redis_shadow_repository
        if redis_shadow_type is not None:
            self.redis_shadow_type = redis_shadow_type

    @property
    def agent_id(self):
        """Gets the agent_id of this AgentConfig.

        探针id

        :return: The agent_id of this AgentConfig.
        :rtype: int
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this AgentConfig.

        探针id

        :param agent_id: The agent_id of this AgentConfig.
        :type agent_id: int
        """
        self._agent_id = agent_id

    @property
    def db_enable(self):
        """Gets the db_enable of this AgentConfig.

        是否开启数据库影子规则

        :return: The db_enable of this AgentConfig.
        :rtype: bool
        """
        return self._db_enable

    @db_enable.setter
    def db_enable(self, db_enable):
        """Sets the db_enable of this AgentConfig.

        是否开启数据库影子规则

        :param db_enable: The db_enable of this AgentConfig.
        :type db_enable: bool
        """
        self._db_enable = db_enable

    @property
    def db_shadow_repository(self):
        """Gets the db_shadow_repository of this AgentConfig.

        数据库影子库名称

        :return: The db_shadow_repository of this AgentConfig.
        :rtype: str
        """
        return self._db_shadow_repository

    @db_shadow_repository.setter
    def db_shadow_repository(self, db_shadow_repository):
        """Sets the db_shadow_repository of this AgentConfig.

        数据库影子库名称

        :param db_shadow_repository: The db_shadow_repository of this AgentConfig.
        :type db_shadow_repository: str
        """
        self._db_shadow_repository = db_shadow_repository

    @property
    def db_shadow_type(self):
        """Gets the db_shadow_type of this AgentConfig.

        数据库影子库类型

        :return: The db_shadow_type of this AgentConfig.
        :rtype: str
        """
        return self._db_shadow_type

    @db_shadow_type.setter
    def db_shadow_type(self, db_shadow_type):
        """Sets the db_shadow_type of this AgentConfig.

        数据库影子库类型

        :param db_shadow_type: The db_shadow_type of this AgentConfig.
        :type db_shadow_type: str
        """
        self._db_shadow_type = db_shadow_type

    @property
    def log_level(self):
        """Gets the log_level of this AgentConfig.

        日志级别，枚举值：INFO，DEBUG，WARN，ERROR

        :return: The log_level of this AgentConfig.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this AgentConfig.

        日志级别，枚举值：INFO，DEBUG，WARN，ERROR

        :param log_level: The log_level of this AgentConfig.
        :type log_level: str
        """
        self._log_level = log_level

    @property
    def log_path(self):
        """Gets the log_path of this AgentConfig.

        日志路径

        :return: The log_path of this AgentConfig.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        """Sets the log_path of this AgentConfig.

        日志路径

        :param log_path: The log_path of this AgentConfig.
        :type log_path: str
        """
        self._log_path = log_path

    @property
    def main_switch(self):
        """Gets the main_switch of this AgentConfig.

        影子规则开关

        :return: The main_switch of this AgentConfig.
        :rtype: bool
        """
        return self._main_switch

    @main_switch.setter
    def main_switch(self, main_switch):
        """Sets the main_switch of this AgentConfig.

        影子规则开关

        :param main_switch: The main_switch of this AgentConfig.
        :type main_switch: bool
        """
        self._main_switch = main_switch

    @property
    def redis_enable(self):
        """Gets the redis_enable of this AgentConfig.

        是否开启redis影子库规则

        :return: The redis_enable of this AgentConfig.
        :rtype: bool
        """
        return self._redis_enable

    @redis_enable.setter
    def redis_enable(self, redis_enable):
        """Sets the redis_enable of this AgentConfig.

        是否开启redis影子库规则

        :param redis_enable: The redis_enable of this AgentConfig.
        :type redis_enable: bool
        """
        self._redis_enable = redis_enable

    @property
    def redis_shadow_key_prefix(self):
        """Gets the redis_shadow_key_prefix of this AgentConfig.

        redis影子库key前缀

        :return: The redis_shadow_key_prefix of this AgentConfig.
        :rtype: str
        """
        return self._redis_shadow_key_prefix

    @redis_shadow_key_prefix.setter
    def redis_shadow_key_prefix(self, redis_shadow_key_prefix):
        """Sets the redis_shadow_key_prefix of this AgentConfig.

        redis影子库key前缀

        :param redis_shadow_key_prefix: The redis_shadow_key_prefix of this AgentConfig.
        :type redis_shadow_key_prefix: str
        """
        self._redis_shadow_key_prefix = redis_shadow_key_prefix

    @property
    def redis_shadow_repository(self):
        """Gets the redis_shadow_repository of this AgentConfig.

        redis影子库名称

        :return: The redis_shadow_repository of this AgentConfig.
        :rtype: str
        """
        return self._redis_shadow_repository

    @redis_shadow_repository.setter
    def redis_shadow_repository(self, redis_shadow_repository):
        """Sets the redis_shadow_repository of this AgentConfig.

        redis影子库名称

        :param redis_shadow_repository: The redis_shadow_repository of this AgentConfig.
        :type redis_shadow_repository: str
        """
        self._redis_shadow_repository = redis_shadow_repository

    @property
    def redis_shadow_type(self):
        """Gets the redis_shadow_type of this AgentConfig.

        redis影子库类型

        :return: The redis_shadow_type of this AgentConfig.
        :rtype: str
        """
        return self._redis_shadow_type

    @redis_shadow_type.setter
    def redis_shadow_type(self, redis_shadow_type):
        """Sets the redis_shadow_type of this AgentConfig.

        redis影子库类型

        :param redis_shadow_type: The redis_shadow_type of this AgentConfig.
        :type redis_shadow_type: str
        """
        self._redis_shadow_type = redis_shadow_type

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
        if not isinstance(other, AgentConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
