# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MySQLLatestDeadLock:

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
        'time': 'str',
        'rollback_trx_id': 'str',
        'mysql_transactions': 'list[MySQLTransaction]'
    }

    attribute_map = {
        'raw': 'raw',
        'happen_time': 'happen_time',
        'time': 'time',
        'rollback_trx_id': 'rollback_trx_id',
        'mysql_transactions': 'mysql_transactions'
    }

    def __init__(self, raw=None, happen_time=None, time=None, rollback_trx_id=None, mysql_transactions=None):
        r"""MySQLLatestDeadLock

        The model defined in huaweicloud sdk

        :param raw: 原始死锁内容
        :type raw: str
        :param happen_time: 发生时间（ms）
        :type happen_time: int
        :param time: 死锁时间
        :type time: str
        :param rollback_trx_id: 回滚事务ID
        :type rollback_trx_id: str
        :param mysql_transactions: 事务列表
        :type mysql_transactions: list[:class:`huaweicloudsdkdas.v3.MySQLTransaction`]
        """
        
        

        self._raw = None
        self._happen_time = None
        self._time = None
        self._rollback_trx_id = None
        self._mysql_transactions = None
        self.discriminator = None

        if raw is not None:
            self.raw = raw
        if happen_time is not None:
            self.happen_time = happen_time
        if time is not None:
            self.time = time
        if rollback_trx_id is not None:
            self.rollback_trx_id = rollback_trx_id
        if mysql_transactions is not None:
            self.mysql_transactions = mysql_transactions

    @property
    def raw(self):
        r"""Gets the raw of this MySQLLatestDeadLock.

        原始死锁内容

        :return: The raw of this MySQLLatestDeadLock.
        :rtype: str
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        r"""Sets the raw of this MySQLLatestDeadLock.

        原始死锁内容

        :param raw: The raw of this MySQLLatestDeadLock.
        :type raw: str
        """
        self._raw = raw

    @property
    def happen_time(self):
        r"""Gets the happen_time of this MySQLLatestDeadLock.

        发生时间（ms）

        :return: The happen_time of this MySQLLatestDeadLock.
        :rtype: int
        """
        return self._happen_time

    @happen_time.setter
    def happen_time(self, happen_time):
        r"""Sets the happen_time of this MySQLLatestDeadLock.

        发生时间（ms）

        :param happen_time: The happen_time of this MySQLLatestDeadLock.
        :type happen_time: int
        """
        self._happen_time = happen_time

    @property
    def time(self):
        r"""Gets the time of this MySQLLatestDeadLock.

        死锁时间

        :return: The time of this MySQLLatestDeadLock.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this MySQLLatestDeadLock.

        死锁时间

        :param time: The time of this MySQLLatestDeadLock.
        :type time: str
        """
        self._time = time

    @property
    def rollback_trx_id(self):
        r"""Gets the rollback_trx_id of this MySQLLatestDeadLock.

        回滚事务ID

        :return: The rollback_trx_id of this MySQLLatestDeadLock.
        :rtype: str
        """
        return self._rollback_trx_id

    @rollback_trx_id.setter
    def rollback_trx_id(self, rollback_trx_id):
        r"""Sets the rollback_trx_id of this MySQLLatestDeadLock.

        回滚事务ID

        :param rollback_trx_id: The rollback_trx_id of this MySQLLatestDeadLock.
        :type rollback_trx_id: str
        """
        self._rollback_trx_id = rollback_trx_id

    @property
    def mysql_transactions(self):
        r"""Gets the mysql_transactions of this MySQLLatestDeadLock.

        事务列表

        :return: The mysql_transactions of this MySQLLatestDeadLock.
        :rtype: list[:class:`huaweicloudsdkdas.v3.MySQLTransaction`]
        """
        return self._mysql_transactions

    @mysql_transactions.setter
    def mysql_transactions(self, mysql_transactions):
        r"""Sets the mysql_transactions of this MySQLLatestDeadLock.

        事务列表

        :param mysql_transactions: The mysql_transactions of this MySQLLatestDeadLock.
        :type mysql_transactions: list[:class:`huaweicloudsdkdas.v3.MySQLTransaction`]
        """
        self._mysql_transactions = mysql_transactions

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
        if not isinstance(other, MySQLLatestDeadLock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
