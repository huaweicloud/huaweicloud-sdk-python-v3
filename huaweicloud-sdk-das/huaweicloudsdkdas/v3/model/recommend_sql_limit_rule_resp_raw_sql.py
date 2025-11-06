# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecommendSqlLimitRuleRespRawSql:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'host': 'str',
        'sql': 'str',
        'db': 'str',
        'time': 'int'
    }

    attribute_map = {
        'session_id': 'session_id',
        'host': 'host',
        'sql': 'sql',
        'db': 'db',
        'time': 'time'
    }

    def __init__(self, session_id=None, host=None, sql=None, db=None, time=None):
        r"""RecommendSqlLimitRuleRespRawSql

        The model defined in huaweicloud sdk

        :param session_id: 会话id
        :type session_id: str
        :param host: 主机ip
        :type host: str
        :param sql: sql
        :type sql: str
        :param db: 数据库名称
        :type db: str
        :param time: 时间
        :type time: int
        """
        
        

        self._session_id = None
        self._host = None
        self._sql = None
        self._db = None
        self._time = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if host is not None:
            self.host = host
        if sql is not None:
            self.sql = sql
        if db is not None:
            self.db = db
        if time is not None:
            self.time = time

    @property
    def session_id(self):
        r"""Gets the session_id of this RecommendSqlLimitRuleRespRawSql.

        会话id

        :return: The session_id of this RecommendSqlLimitRuleRespRawSql.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this RecommendSqlLimitRuleRespRawSql.

        会话id

        :param session_id: The session_id of this RecommendSqlLimitRuleRespRawSql.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def host(self):
        r"""Gets the host of this RecommendSqlLimitRuleRespRawSql.

        主机ip

        :return: The host of this RecommendSqlLimitRuleRespRawSql.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this RecommendSqlLimitRuleRespRawSql.

        主机ip

        :param host: The host of this RecommendSqlLimitRuleRespRawSql.
        :type host: str
        """
        self._host = host

    @property
    def sql(self):
        r"""Gets the sql of this RecommendSqlLimitRuleRespRawSql.

        sql

        :return: The sql of this RecommendSqlLimitRuleRespRawSql.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this RecommendSqlLimitRuleRespRawSql.

        sql

        :param sql: The sql of this RecommendSqlLimitRuleRespRawSql.
        :type sql: str
        """
        self._sql = sql

    @property
    def db(self):
        r"""Gets the db of this RecommendSqlLimitRuleRespRawSql.

        数据库名称

        :return: The db of this RecommendSqlLimitRuleRespRawSql.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this RecommendSqlLimitRuleRespRawSql.

        数据库名称

        :param db: The db of this RecommendSqlLimitRuleRespRawSql.
        :type db: str
        """
        self._db = db

    @property
    def time(self):
        r"""Gets the time of this RecommendSqlLimitRuleRespRawSql.

        时间

        :return: The time of this RecommendSqlLimitRuleRespRawSql.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this RecommendSqlLimitRuleRespRawSql.

        时间

        :param time: The time of this RecommendSqlLimitRuleRespRawSql.
        :type time: int
        """
        self._time = time

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
        if not isinstance(other, RecommendSqlLimitRuleRespRawSql):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
