# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetSqlSwitchNewRequestBody:

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
        'instance_id': 'str',
        'full_sql_switch_on': 'bool',
        'full_sql_retention_hours': 'int',
        'slow_sql_switch_on': 'bool',
        'slow_sql_retention_hours': 'int',
        'dead_lock_switch_on': 'bool',
        'dead_lock_retention_hours': 'int',
        'lock_blocking_switch_on': 'bool',
        'lock_blocking_retention_hours': 'int'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'instance_id': 'instance_id',
        'full_sql_switch_on': 'full_sql_switch_on',
        'full_sql_retention_hours': 'full_sql_retention_hours',
        'slow_sql_switch_on': 'slow_sql_switch_on',
        'slow_sql_retention_hours': 'slow_sql_retention_hours',
        'dead_lock_switch_on': 'dead_lock_switch_on',
        'dead_lock_retention_hours': 'dead_lock_retention_hours',
        'lock_blocking_switch_on': 'lock_blocking_switch_on',
        'lock_blocking_retention_hours': 'lock_blocking_retention_hours'
    }

    def __init__(self, engine_type=None, instance_id=None, full_sql_switch_on=None, full_sql_retention_hours=None, slow_sql_switch_on=None, slow_sql_retention_hours=None, dead_lock_switch_on=None, dead_lock_retention_hours=None, lock_blocking_switch_on=None, lock_blocking_retention_hours=None):
        r"""SetSqlSwitchNewRequestBody

        The model defined in huaweicloud sdk

        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param full_sql_switch_on: 全量SQL开关
        :type full_sql_switch_on: bool
        :param full_sql_retention_hours: 全量SQL存储时长
        :type full_sql_retention_hours: int
        :param slow_sql_switch_on: 慢SQL开关
        :type slow_sql_switch_on: bool
        :param slow_sql_retention_hours: 慢SQL存储时长
        :type slow_sql_retention_hours: int
        :param dead_lock_switch_on: 死锁开关
        :type dead_lock_switch_on: bool
        :param dead_lock_retention_hours: 死锁存储时长
        :type dead_lock_retention_hours: int
        :param lock_blocking_switch_on: 锁等待开关
        :type lock_blocking_switch_on: bool
        :param lock_blocking_retention_hours: 锁等待存储时长
        :type lock_blocking_retention_hours: int
        """
        
        

        self._engine_type = None
        self._instance_id = None
        self._full_sql_switch_on = None
        self._full_sql_retention_hours = None
        self._slow_sql_switch_on = None
        self._slow_sql_retention_hours = None
        self._dead_lock_switch_on = None
        self._dead_lock_retention_hours = None
        self._lock_blocking_switch_on = None
        self._lock_blocking_retention_hours = None
        self.discriminator = None

        self.engine_type = engine_type
        self.instance_id = instance_id
        if full_sql_switch_on is not None:
            self.full_sql_switch_on = full_sql_switch_on
        if full_sql_retention_hours is not None:
            self.full_sql_retention_hours = full_sql_retention_hours
        if slow_sql_switch_on is not None:
            self.slow_sql_switch_on = slow_sql_switch_on
        if slow_sql_retention_hours is not None:
            self.slow_sql_retention_hours = slow_sql_retention_hours
        if dead_lock_switch_on is not None:
            self.dead_lock_switch_on = dead_lock_switch_on
        if dead_lock_retention_hours is not None:
            self.dead_lock_retention_hours = dead_lock_retention_hours
        if lock_blocking_switch_on is not None:
            self.lock_blocking_switch_on = lock_blocking_switch_on
        if lock_blocking_retention_hours is not None:
            self.lock_blocking_retention_hours = lock_blocking_retention_hours

    @property
    def engine_type(self):
        r"""Gets the engine_type of this SetSqlSwitchNewRequestBody.

        数据库引擎类型

        :return: The engine_type of this SetSqlSwitchNewRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this SetSqlSwitchNewRequestBody.

        数据库引擎类型

        :param engine_type: The engine_type of this SetSqlSwitchNewRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SetSqlSwitchNewRequestBody.

        实例ID

        :return: The instance_id of this SetSqlSwitchNewRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SetSqlSwitchNewRequestBody.

        实例ID

        :param instance_id: The instance_id of this SetSqlSwitchNewRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def full_sql_switch_on(self):
        r"""Gets the full_sql_switch_on of this SetSqlSwitchNewRequestBody.

        全量SQL开关

        :return: The full_sql_switch_on of this SetSqlSwitchNewRequestBody.
        :rtype: bool
        """
        return self._full_sql_switch_on

    @full_sql_switch_on.setter
    def full_sql_switch_on(self, full_sql_switch_on):
        r"""Sets the full_sql_switch_on of this SetSqlSwitchNewRequestBody.

        全量SQL开关

        :param full_sql_switch_on: The full_sql_switch_on of this SetSqlSwitchNewRequestBody.
        :type full_sql_switch_on: bool
        """
        self._full_sql_switch_on = full_sql_switch_on

    @property
    def full_sql_retention_hours(self):
        r"""Gets the full_sql_retention_hours of this SetSqlSwitchNewRequestBody.

        全量SQL存储时长

        :return: The full_sql_retention_hours of this SetSqlSwitchNewRequestBody.
        :rtype: int
        """
        return self._full_sql_retention_hours

    @full_sql_retention_hours.setter
    def full_sql_retention_hours(self, full_sql_retention_hours):
        r"""Sets the full_sql_retention_hours of this SetSqlSwitchNewRequestBody.

        全量SQL存储时长

        :param full_sql_retention_hours: The full_sql_retention_hours of this SetSqlSwitchNewRequestBody.
        :type full_sql_retention_hours: int
        """
        self._full_sql_retention_hours = full_sql_retention_hours

    @property
    def slow_sql_switch_on(self):
        r"""Gets the slow_sql_switch_on of this SetSqlSwitchNewRequestBody.

        慢SQL开关

        :return: The slow_sql_switch_on of this SetSqlSwitchNewRequestBody.
        :rtype: bool
        """
        return self._slow_sql_switch_on

    @slow_sql_switch_on.setter
    def slow_sql_switch_on(self, slow_sql_switch_on):
        r"""Sets the slow_sql_switch_on of this SetSqlSwitchNewRequestBody.

        慢SQL开关

        :param slow_sql_switch_on: The slow_sql_switch_on of this SetSqlSwitchNewRequestBody.
        :type slow_sql_switch_on: bool
        """
        self._slow_sql_switch_on = slow_sql_switch_on

    @property
    def slow_sql_retention_hours(self):
        r"""Gets the slow_sql_retention_hours of this SetSqlSwitchNewRequestBody.

        慢SQL存储时长

        :return: The slow_sql_retention_hours of this SetSqlSwitchNewRequestBody.
        :rtype: int
        """
        return self._slow_sql_retention_hours

    @slow_sql_retention_hours.setter
    def slow_sql_retention_hours(self, slow_sql_retention_hours):
        r"""Sets the slow_sql_retention_hours of this SetSqlSwitchNewRequestBody.

        慢SQL存储时长

        :param slow_sql_retention_hours: The slow_sql_retention_hours of this SetSqlSwitchNewRequestBody.
        :type slow_sql_retention_hours: int
        """
        self._slow_sql_retention_hours = slow_sql_retention_hours

    @property
    def dead_lock_switch_on(self):
        r"""Gets the dead_lock_switch_on of this SetSqlSwitchNewRequestBody.

        死锁开关

        :return: The dead_lock_switch_on of this SetSqlSwitchNewRequestBody.
        :rtype: bool
        """
        return self._dead_lock_switch_on

    @dead_lock_switch_on.setter
    def dead_lock_switch_on(self, dead_lock_switch_on):
        r"""Sets the dead_lock_switch_on of this SetSqlSwitchNewRequestBody.

        死锁开关

        :param dead_lock_switch_on: The dead_lock_switch_on of this SetSqlSwitchNewRequestBody.
        :type dead_lock_switch_on: bool
        """
        self._dead_lock_switch_on = dead_lock_switch_on

    @property
    def dead_lock_retention_hours(self):
        r"""Gets the dead_lock_retention_hours of this SetSqlSwitchNewRequestBody.

        死锁存储时长

        :return: The dead_lock_retention_hours of this SetSqlSwitchNewRequestBody.
        :rtype: int
        """
        return self._dead_lock_retention_hours

    @dead_lock_retention_hours.setter
    def dead_lock_retention_hours(self, dead_lock_retention_hours):
        r"""Sets the dead_lock_retention_hours of this SetSqlSwitchNewRequestBody.

        死锁存储时长

        :param dead_lock_retention_hours: The dead_lock_retention_hours of this SetSqlSwitchNewRequestBody.
        :type dead_lock_retention_hours: int
        """
        self._dead_lock_retention_hours = dead_lock_retention_hours

    @property
    def lock_blocking_switch_on(self):
        r"""Gets the lock_blocking_switch_on of this SetSqlSwitchNewRequestBody.

        锁等待开关

        :return: The lock_blocking_switch_on of this SetSqlSwitchNewRequestBody.
        :rtype: bool
        """
        return self._lock_blocking_switch_on

    @lock_blocking_switch_on.setter
    def lock_blocking_switch_on(self, lock_blocking_switch_on):
        r"""Sets the lock_blocking_switch_on of this SetSqlSwitchNewRequestBody.

        锁等待开关

        :param lock_blocking_switch_on: The lock_blocking_switch_on of this SetSqlSwitchNewRequestBody.
        :type lock_blocking_switch_on: bool
        """
        self._lock_blocking_switch_on = lock_blocking_switch_on

    @property
    def lock_blocking_retention_hours(self):
        r"""Gets the lock_blocking_retention_hours of this SetSqlSwitchNewRequestBody.

        锁等待存储时长

        :return: The lock_blocking_retention_hours of this SetSqlSwitchNewRequestBody.
        :rtype: int
        """
        return self._lock_blocking_retention_hours

    @lock_blocking_retention_hours.setter
    def lock_blocking_retention_hours(self, lock_blocking_retention_hours):
        r"""Sets the lock_blocking_retention_hours of this SetSqlSwitchNewRequestBody.

        锁等待存储时长

        :param lock_blocking_retention_hours: The lock_blocking_retention_hours of this SetSqlSwitchNewRequestBody.
        :type lock_blocking_retention_hours: int
        """
        self._lock_blocking_retention_hours = lock_blocking_retention_hours

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
        if not isinstance(other, SetSqlSwitchNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
