# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangePaymentModeForConsoleBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id_list': 'list[str]',
        'engine_type': 'str',
        'payment_mode': 'bool',
        'resource_type': 'str',
        'open_full_sql': 'bool',
        'open_slow_sql': 'bool',
        'open_dead_lock': 'bool',
        'open_lock_blocking': 'bool',
        'open_transaction': 'bool'
    }

    attribute_map = {
        'instance_id_list': 'instance_id_list',
        'engine_type': 'engine_type',
        'payment_mode': 'payment_mode',
        'resource_type': 'resource_type',
        'open_full_sql': 'open_full_sql',
        'open_slow_sql': 'open_slow_sql',
        'open_dead_lock': 'open_dead_lock',
        'open_lock_blocking': 'open_lock_blocking',
        'open_transaction': 'open_transaction'
    }

    def __init__(self, instance_id_list=None, engine_type=None, payment_mode=None, resource_type=None, open_full_sql=None, open_slow_sql=None, open_dead_lock=None, open_lock_blocking=None, open_transaction=None):
        r"""ChangePaymentModeForConsoleBody

        The model defined in huaweicloud sdk

        :param instance_id_list: 实例ID列表
        :type instance_id_list: list[str]
        :param engine_type: 引擎类型
        :type engine_type: str
        :param payment_mode: true: 设置为付费, false: 设置为免费
        :type payment_mode: bool
        :param resource_type: 资源类型
        :type resource_type: str
        :param open_full_sql: 是否打开全量SQL
        :type open_full_sql: bool
        :param open_slow_sql: 是否打开慢SQL
        :type open_slow_sql: bool
        :param open_dead_lock: 是否打开死锁分析
        :type open_dead_lock: bool
        :param open_lock_blocking: 是否打开锁阻塞
        :type open_lock_blocking: bool
        :param open_transaction: 是否打开历史事务
        :type open_transaction: bool
        """
        
        

        self._instance_id_list = None
        self._engine_type = None
        self._payment_mode = None
        self._resource_type = None
        self._open_full_sql = None
        self._open_slow_sql = None
        self._open_dead_lock = None
        self._open_lock_blocking = None
        self._open_transaction = None
        self.discriminator = None

        self.instance_id_list = instance_id_list
        if engine_type is not None:
            self.engine_type = engine_type
        if payment_mode is not None:
            self.payment_mode = payment_mode
        if resource_type is not None:
            self.resource_type = resource_type
        if open_full_sql is not None:
            self.open_full_sql = open_full_sql
        if open_slow_sql is not None:
            self.open_slow_sql = open_slow_sql
        if open_dead_lock is not None:
            self.open_dead_lock = open_dead_lock
        if open_lock_blocking is not None:
            self.open_lock_blocking = open_lock_blocking
        if open_transaction is not None:
            self.open_transaction = open_transaction

    @property
    def instance_id_list(self):
        r"""Gets the instance_id_list of this ChangePaymentModeForConsoleBody.

        实例ID列表

        :return: The instance_id_list of this ChangePaymentModeForConsoleBody.
        :rtype: list[str]
        """
        return self._instance_id_list

    @instance_id_list.setter
    def instance_id_list(self, instance_id_list):
        r"""Sets the instance_id_list of this ChangePaymentModeForConsoleBody.

        实例ID列表

        :param instance_id_list: The instance_id_list of this ChangePaymentModeForConsoleBody.
        :type instance_id_list: list[str]
        """
        self._instance_id_list = instance_id_list

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ChangePaymentModeForConsoleBody.

        引擎类型

        :return: The engine_type of this ChangePaymentModeForConsoleBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ChangePaymentModeForConsoleBody.

        引擎类型

        :param engine_type: The engine_type of this ChangePaymentModeForConsoleBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def payment_mode(self):
        r"""Gets the payment_mode of this ChangePaymentModeForConsoleBody.

        true: 设置为付费, false: 设置为免费

        :return: The payment_mode of this ChangePaymentModeForConsoleBody.
        :rtype: bool
        """
        return self._payment_mode

    @payment_mode.setter
    def payment_mode(self, payment_mode):
        r"""Sets the payment_mode of this ChangePaymentModeForConsoleBody.

        true: 设置为付费, false: 设置为免费

        :param payment_mode: The payment_mode of this ChangePaymentModeForConsoleBody.
        :type payment_mode: bool
        """
        self._payment_mode = payment_mode

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ChangePaymentModeForConsoleBody.

        资源类型

        :return: The resource_type of this ChangePaymentModeForConsoleBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ChangePaymentModeForConsoleBody.

        资源类型

        :param resource_type: The resource_type of this ChangePaymentModeForConsoleBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def open_full_sql(self):
        r"""Gets the open_full_sql of this ChangePaymentModeForConsoleBody.

        是否打开全量SQL

        :return: The open_full_sql of this ChangePaymentModeForConsoleBody.
        :rtype: bool
        """
        return self._open_full_sql

    @open_full_sql.setter
    def open_full_sql(self, open_full_sql):
        r"""Sets the open_full_sql of this ChangePaymentModeForConsoleBody.

        是否打开全量SQL

        :param open_full_sql: The open_full_sql of this ChangePaymentModeForConsoleBody.
        :type open_full_sql: bool
        """
        self._open_full_sql = open_full_sql

    @property
    def open_slow_sql(self):
        r"""Gets the open_slow_sql of this ChangePaymentModeForConsoleBody.

        是否打开慢SQL

        :return: The open_slow_sql of this ChangePaymentModeForConsoleBody.
        :rtype: bool
        """
        return self._open_slow_sql

    @open_slow_sql.setter
    def open_slow_sql(self, open_slow_sql):
        r"""Sets the open_slow_sql of this ChangePaymentModeForConsoleBody.

        是否打开慢SQL

        :param open_slow_sql: The open_slow_sql of this ChangePaymentModeForConsoleBody.
        :type open_slow_sql: bool
        """
        self._open_slow_sql = open_slow_sql

    @property
    def open_dead_lock(self):
        r"""Gets the open_dead_lock of this ChangePaymentModeForConsoleBody.

        是否打开死锁分析

        :return: The open_dead_lock of this ChangePaymentModeForConsoleBody.
        :rtype: bool
        """
        return self._open_dead_lock

    @open_dead_lock.setter
    def open_dead_lock(self, open_dead_lock):
        r"""Sets the open_dead_lock of this ChangePaymentModeForConsoleBody.

        是否打开死锁分析

        :param open_dead_lock: The open_dead_lock of this ChangePaymentModeForConsoleBody.
        :type open_dead_lock: bool
        """
        self._open_dead_lock = open_dead_lock

    @property
    def open_lock_blocking(self):
        r"""Gets the open_lock_blocking of this ChangePaymentModeForConsoleBody.

        是否打开锁阻塞

        :return: The open_lock_blocking of this ChangePaymentModeForConsoleBody.
        :rtype: bool
        """
        return self._open_lock_blocking

    @open_lock_blocking.setter
    def open_lock_blocking(self, open_lock_blocking):
        r"""Sets the open_lock_blocking of this ChangePaymentModeForConsoleBody.

        是否打开锁阻塞

        :param open_lock_blocking: The open_lock_blocking of this ChangePaymentModeForConsoleBody.
        :type open_lock_blocking: bool
        """
        self._open_lock_blocking = open_lock_blocking

    @property
    def open_transaction(self):
        r"""Gets the open_transaction of this ChangePaymentModeForConsoleBody.

        是否打开历史事务

        :return: The open_transaction of this ChangePaymentModeForConsoleBody.
        :rtype: bool
        """
        return self._open_transaction

    @open_transaction.setter
    def open_transaction(self, open_transaction):
        r"""Sets the open_transaction of this ChangePaymentModeForConsoleBody.

        是否打开历史事务

        :param open_transaction: The open_transaction of this ChangePaymentModeForConsoleBody.
        :type open_transaction: bool
        """
        self._open_transaction = open_transaction

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
        if not isinstance(other, ChangePaymentModeForConsoleBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
