# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullDeadLockListRespMysqlDeadlock:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'raw': 'str',
        'happen_time': 'int',
        'rollback_trx_id': 'str',
        'mysql_transactions': 'list[FullDeadLockListRespMysqlDeadlockMysqlTransactions]'
    }

    attribute_map = {
        'raw': 'raw',
        'happen_time': 'happen_time',
        'rollback_trx_id': 'rollback_trx_id',
        'mysql_transactions': 'mysql_transactions'
    }

    def __init__(self, raw=None, happen_time=None, rollback_trx_id=None, mysql_transactions=None):
        r"""FullDeadLockListRespMysqlDeadlock

        The model defined in huaweicloud sdk

        :param raw: 死锁事件详细信息
        :type raw: str
        :param happen_time: 死锁事件发生的 Unix 时间戳（毫秒级）
        :type happen_time: int
        :param rollback_trx_id: MySQL InnoDB 引擎在检测到死锁后，会自动选择一个事务进行回滚以解除死锁。
        :type rollback_trx_id: str
        :param mysql_transactions: 参与这次死锁的每个事务的详细结构化信息
        :type mysql_transactions: list[:class:`huaweicloudsdkdas.v3.FullDeadLockListRespMysqlDeadlockMysqlTransactions`]
        """
        
        

        self._raw = None
        self._happen_time = None
        self._rollback_trx_id = None
        self._mysql_transactions = None
        self.discriminator = None

        if raw is not None:
            self.raw = raw
        if happen_time is not None:
            self.happen_time = happen_time
        if rollback_trx_id is not None:
            self.rollback_trx_id = rollback_trx_id
        if mysql_transactions is not None:
            self.mysql_transactions = mysql_transactions

    @property
    def raw(self):
        r"""Gets the raw of this FullDeadLockListRespMysqlDeadlock.

        死锁事件详细信息

        :return: The raw of this FullDeadLockListRespMysqlDeadlock.
        :rtype: str
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        r"""Sets the raw of this FullDeadLockListRespMysqlDeadlock.

        死锁事件详细信息

        :param raw: The raw of this FullDeadLockListRespMysqlDeadlock.
        :type raw: str
        """
        self._raw = raw

    @property
    def happen_time(self):
        r"""Gets the happen_time of this FullDeadLockListRespMysqlDeadlock.

        死锁事件发生的 Unix 时间戳（毫秒级）

        :return: The happen_time of this FullDeadLockListRespMysqlDeadlock.
        :rtype: int
        """
        return self._happen_time

    @happen_time.setter
    def happen_time(self, happen_time):
        r"""Sets the happen_time of this FullDeadLockListRespMysqlDeadlock.

        死锁事件发生的 Unix 时间戳（毫秒级）

        :param happen_time: The happen_time of this FullDeadLockListRespMysqlDeadlock.
        :type happen_time: int
        """
        self._happen_time = happen_time

    @property
    def rollback_trx_id(self):
        r"""Gets the rollback_trx_id of this FullDeadLockListRespMysqlDeadlock.

        MySQL InnoDB 引擎在检测到死锁后，会自动选择一个事务进行回滚以解除死锁。

        :return: The rollback_trx_id of this FullDeadLockListRespMysqlDeadlock.
        :rtype: str
        """
        return self._rollback_trx_id

    @rollback_trx_id.setter
    def rollback_trx_id(self, rollback_trx_id):
        r"""Sets the rollback_trx_id of this FullDeadLockListRespMysqlDeadlock.

        MySQL InnoDB 引擎在检测到死锁后，会自动选择一个事务进行回滚以解除死锁。

        :param rollback_trx_id: The rollback_trx_id of this FullDeadLockListRespMysqlDeadlock.
        :type rollback_trx_id: str
        """
        self._rollback_trx_id = rollback_trx_id

    @property
    def mysql_transactions(self):
        r"""Gets the mysql_transactions of this FullDeadLockListRespMysqlDeadlock.

        参与这次死锁的每个事务的详细结构化信息

        :return: The mysql_transactions of this FullDeadLockListRespMysqlDeadlock.
        :rtype: list[:class:`huaweicloudsdkdas.v3.FullDeadLockListRespMysqlDeadlockMysqlTransactions`]
        """
        return self._mysql_transactions

    @mysql_transactions.setter
    def mysql_transactions(self, mysql_transactions):
        r"""Sets the mysql_transactions of this FullDeadLockListRespMysqlDeadlock.

        参与这次死锁的每个事务的详细结构化信息

        :param mysql_transactions: The mysql_transactions of this FullDeadLockListRespMysqlDeadlock.
        :type mysql_transactions: list[:class:`huaweicloudsdkdas.v3.FullDeadLockListRespMysqlDeadlockMysqlTransactions`]
        """
        self._mysql_transactions = mysql_transactions

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
        if not isinstance(other, FullDeadLockListRespMysqlDeadlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
