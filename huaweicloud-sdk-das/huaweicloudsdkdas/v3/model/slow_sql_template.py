# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowSqlTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_template': 'str',
        'sql_template_id': 'str',
        'sql_sample': 'str',
        'sql_sample_user': 'str',
        'db_names': 'list[str]',
        'execute_count': 'int',
        'avg_execute_time': 'float',
        'max_execute_time': 'float',
        'avg_lock_wait_time': 'float',
        'max_lock_wait_time': 'float',
        'avg_rows_examined': 'float',
        'max_rows_examined': 'float',
        'avg_rows_sent': 'float',
        'max_rows_sent': 'float'
    }

    attribute_map = {
        'sql_template': 'sql_template',
        'sql_template_id': 'sql_template_id',
        'sql_sample': 'sql_sample',
        'sql_sample_user': 'sql_sample_user',
        'db_names': 'db_names',
        'execute_count': 'execute_count',
        'avg_execute_time': 'avg_execute_time',
        'max_execute_time': 'max_execute_time',
        'avg_lock_wait_time': 'avg_lock_wait_time',
        'max_lock_wait_time': 'max_lock_wait_time',
        'avg_rows_examined': 'avg_rows_examined',
        'max_rows_examined': 'max_rows_examined',
        'avg_rows_sent': 'avg_rows_sent',
        'max_rows_sent': 'max_rows_sent'
    }

    def __init__(self, sql_template=None, sql_template_id=None, sql_sample=None, sql_sample_user=None, db_names=None, execute_count=None, avg_execute_time=None, max_execute_time=None, avg_lock_wait_time=None, max_lock_wait_time=None, avg_rows_examined=None, max_rows_examined=None, avg_rows_sent=None, max_rows_sent=None):
        r"""SlowSqlTemplate

        The model defined in huaweicloud sdk

        :param sql_template: SQL模板。
        :type sql_template: str
        :param sql_template_id: SQL模板ID。
        :type sql_template_id: str
        :param sql_sample: SQL样本。
        :type sql_sample: str
        :param sql_sample_user: SQL样本执行用户。
        :type sql_sample_user: str
        :param db_names: 库名。
        :type db_names: list[str]
        :param execute_count: 执行次数。
        :type execute_count: int
        :param avg_execute_time: 平均执行耗时(ms)。
        :type avg_execute_time: float
        :param max_execute_time: 最大执行耗时(ms)。
        :type max_execute_time: float
        :param avg_lock_wait_time: 平均锁等待时间(ms)。
        :type avg_lock_wait_time: float
        :param max_lock_wait_time: 最大锁等待时间(ms)。
        :type max_lock_wait_time: float
        :param avg_rows_examined: 平均扫描行数。
        :type avg_rows_examined: float
        :param max_rows_examined: 最大扫描行数。
        :type max_rows_examined: float
        :param avg_rows_sent: 平均返回行数。
        :type avg_rows_sent: float
        :param max_rows_sent: 最大返回行数。
        :type max_rows_sent: float
        """
        
        

        self._sql_template = None
        self._sql_template_id = None
        self._sql_sample = None
        self._sql_sample_user = None
        self._db_names = None
        self._execute_count = None
        self._avg_execute_time = None
        self._max_execute_time = None
        self._avg_lock_wait_time = None
        self._max_lock_wait_time = None
        self._avg_rows_examined = None
        self._max_rows_examined = None
        self._avg_rows_sent = None
        self._max_rows_sent = None
        self.discriminator = None

        self.sql_template = sql_template
        self.sql_template_id = sql_template_id
        if sql_sample is not None:
            self.sql_sample = sql_sample
        if sql_sample_user is not None:
            self.sql_sample_user = sql_sample_user
        self.db_names = db_names
        self.execute_count = execute_count
        self.avg_execute_time = avg_execute_time
        self.max_execute_time = max_execute_time
        self.avg_lock_wait_time = avg_lock_wait_time
        self.max_lock_wait_time = max_lock_wait_time
        self.avg_rows_examined = avg_rows_examined
        self.max_rows_examined = max_rows_examined
        self.avg_rows_sent = avg_rows_sent
        self.max_rows_sent = max_rows_sent

    @property
    def sql_template(self):
        r"""Gets the sql_template of this SlowSqlTemplate.

        SQL模板。

        :return: The sql_template of this SlowSqlTemplate.
        :rtype: str
        """
        return self._sql_template

    @sql_template.setter
    def sql_template(self, sql_template):
        r"""Sets the sql_template of this SlowSqlTemplate.

        SQL模板。

        :param sql_template: The sql_template of this SlowSqlTemplate.
        :type sql_template: str
        """
        self._sql_template = sql_template

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this SlowSqlTemplate.

        SQL模板ID。

        :return: The sql_template_id of this SlowSqlTemplate.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this SlowSqlTemplate.

        SQL模板ID。

        :param sql_template_id: The sql_template_id of this SlowSqlTemplate.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def sql_sample(self):
        r"""Gets the sql_sample of this SlowSqlTemplate.

        SQL样本。

        :return: The sql_sample of this SlowSqlTemplate.
        :rtype: str
        """
        return self._sql_sample

    @sql_sample.setter
    def sql_sample(self, sql_sample):
        r"""Sets the sql_sample of this SlowSqlTemplate.

        SQL样本。

        :param sql_sample: The sql_sample of this SlowSqlTemplate.
        :type sql_sample: str
        """
        self._sql_sample = sql_sample

    @property
    def sql_sample_user(self):
        r"""Gets the sql_sample_user of this SlowSqlTemplate.

        SQL样本执行用户。

        :return: The sql_sample_user of this SlowSqlTemplate.
        :rtype: str
        """
        return self._sql_sample_user

    @sql_sample_user.setter
    def sql_sample_user(self, sql_sample_user):
        r"""Sets the sql_sample_user of this SlowSqlTemplate.

        SQL样本执行用户。

        :param sql_sample_user: The sql_sample_user of this SlowSqlTemplate.
        :type sql_sample_user: str
        """
        self._sql_sample_user = sql_sample_user

    @property
    def db_names(self):
        r"""Gets the db_names of this SlowSqlTemplate.

        库名。

        :return: The db_names of this SlowSqlTemplate.
        :rtype: list[str]
        """
        return self._db_names

    @db_names.setter
    def db_names(self, db_names):
        r"""Sets the db_names of this SlowSqlTemplate.

        库名。

        :param db_names: The db_names of this SlowSqlTemplate.
        :type db_names: list[str]
        """
        self._db_names = db_names

    @property
    def execute_count(self):
        r"""Gets the execute_count of this SlowSqlTemplate.

        执行次数。

        :return: The execute_count of this SlowSqlTemplate.
        :rtype: int
        """
        return self._execute_count

    @execute_count.setter
    def execute_count(self, execute_count):
        r"""Sets the execute_count of this SlowSqlTemplate.

        执行次数。

        :param execute_count: The execute_count of this SlowSqlTemplate.
        :type execute_count: int
        """
        self._execute_count = execute_count

    @property
    def avg_execute_time(self):
        r"""Gets the avg_execute_time of this SlowSqlTemplate.

        平均执行耗时(ms)。

        :return: The avg_execute_time of this SlowSqlTemplate.
        :rtype: float
        """
        return self._avg_execute_time

    @avg_execute_time.setter
    def avg_execute_time(self, avg_execute_time):
        r"""Sets the avg_execute_time of this SlowSqlTemplate.

        平均执行耗时(ms)。

        :param avg_execute_time: The avg_execute_time of this SlowSqlTemplate.
        :type avg_execute_time: float
        """
        self._avg_execute_time = avg_execute_time

    @property
    def max_execute_time(self):
        r"""Gets the max_execute_time of this SlowSqlTemplate.

        最大执行耗时(ms)。

        :return: The max_execute_time of this SlowSqlTemplate.
        :rtype: float
        """
        return self._max_execute_time

    @max_execute_time.setter
    def max_execute_time(self, max_execute_time):
        r"""Sets the max_execute_time of this SlowSqlTemplate.

        最大执行耗时(ms)。

        :param max_execute_time: The max_execute_time of this SlowSqlTemplate.
        :type max_execute_time: float
        """
        self._max_execute_time = max_execute_time

    @property
    def avg_lock_wait_time(self):
        r"""Gets the avg_lock_wait_time of this SlowSqlTemplate.

        平均锁等待时间(ms)。

        :return: The avg_lock_wait_time of this SlowSqlTemplate.
        :rtype: float
        """
        return self._avg_lock_wait_time

    @avg_lock_wait_time.setter
    def avg_lock_wait_time(self, avg_lock_wait_time):
        r"""Sets the avg_lock_wait_time of this SlowSqlTemplate.

        平均锁等待时间(ms)。

        :param avg_lock_wait_time: The avg_lock_wait_time of this SlowSqlTemplate.
        :type avg_lock_wait_time: float
        """
        self._avg_lock_wait_time = avg_lock_wait_time

    @property
    def max_lock_wait_time(self):
        r"""Gets the max_lock_wait_time of this SlowSqlTemplate.

        最大锁等待时间(ms)。

        :return: The max_lock_wait_time of this SlowSqlTemplate.
        :rtype: float
        """
        return self._max_lock_wait_time

    @max_lock_wait_time.setter
    def max_lock_wait_time(self, max_lock_wait_time):
        r"""Sets the max_lock_wait_time of this SlowSqlTemplate.

        最大锁等待时间(ms)。

        :param max_lock_wait_time: The max_lock_wait_time of this SlowSqlTemplate.
        :type max_lock_wait_time: float
        """
        self._max_lock_wait_time = max_lock_wait_time

    @property
    def avg_rows_examined(self):
        r"""Gets the avg_rows_examined of this SlowSqlTemplate.

        平均扫描行数。

        :return: The avg_rows_examined of this SlowSqlTemplate.
        :rtype: float
        """
        return self._avg_rows_examined

    @avg_rows_examined.setter
    def avg_rows_examined(self, avg_rows_examined):
        r"""Sets the avg_rows_examined of this SlowSqlTemplate.

        平均扫描行数。

        :param avg_rows_examined: The avg_rows_examined of this SlowSqlTemplate.
        :type avg_rows_examined: float
        """
        self._avg_rows_examined = avg_rows_examined

    @property
    def max_rows_examined(self):
        r"""Gets the max_rows_examined of this SlowSqlTemplate.

        最大扫描行数。

        :return: The max_rows_examined of this SlowSqlTemplate.
        :rtype: float
        """
        return self._max_rows_examined

    @max_rows_examined.setter
    def max_rows_examined(self, max_rows_examined):
        r"""Sets the max_rows_examined of this SlowSqlTemplate.

        最大扫描行数。

        :param max_rows_examined: The max_rows_examined of this SlowSqlTemplate.
        :type max_rows_examined: float
        """
        self._max_rows_examined = max_rows_examined

    @property
    def avg_rows_sent(self):
        r"""Gets the avg_rows_sent of this SlowSqlTemplate.

        平均返回行数。

        :return: The avg_rows_sent of this SlowSqlTemplate.
        :rtype: float
        """
        return self._avg_rows_sent

    @avg_rows_sent.setter
    def avg_rows_sent(self, avg_rows_sent):
        r"""Sets the avg_rows_sent of this SlowSqlTemplate.

        平均返回行数。

        :param avg_rows_sent: The avg_rows_sent of this SlowSqlTemplate.
        :type avg_rows_sent: float
        """
        self._avg_rows_sent = avg_rows_sent

    @property
    def max_rows_sent(self):
        r"""Gets the max_rows_sent of this SlowSqlTemplate.

        最大返回行数。

        :return: The max_rows_sent of this SlowSqlTemplate.
        :rtype: float
        """
        return self._max_rows_sent

    @max_rows_sent.setter
    def max_rows_sent(self, max_rows_sent):
        r"""Sets the max_rows_sent of this SlowSqlTemplate.

        最大返回行数。

        :param max_rows_sent: The max_rows_sent of this SlowSqlTemplate.
        :type max_rows_sent: float
        """
        self._max_rows_sent = max_rows_sent

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
        if not isinstance(other, SlowSqlTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
