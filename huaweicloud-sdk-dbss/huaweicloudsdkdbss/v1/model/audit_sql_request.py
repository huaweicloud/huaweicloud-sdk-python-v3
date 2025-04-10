# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditSqlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'AuditSqlRequestTime',
        'risk_levels': 'str',
        'client_ip': 'str',
        'client_name': 'str',
        'db_ip': 'str',
        'db_user': 'str',
        'query_type': 'str',
        'rule_name': 'str',
        'sql_statement': 'str',
        'sql_response': 'str',
        'page': 'int',
        'size': 'int',
        'time_order': 'str'
    }

    attribute_map = {
        'time': 'time',
        'risk_levels': 'risk_levels',
        'client_ip': 'client_ip',
        'client_name': 'client_name',
        'db_ip': 'db_ip',
        'db_user': 'db_user',
        'query_type': 'query_type',
        'rule_name': 'rule_name',
        'sql_statement': 'sql_statement',
        'sql_response': 'sql_response',
        'page': 'page',
        'size': 'size',
        'time_order': 'time_order'
    }

    def __init__(self, time=None, risk_levels=None, client_ip=None, client_name=None, db_ip=None, db_user=None, query_type=None, rule_name=None, sql_statement=None, sql_response=None, page=None, size=None, time_order=None):
        r"""AuditSqlRequest

        The model defined in huaweicloud sdk

        :param time: 
        :type time: :class:`huaweicloudsdkdbss.v1.AuditSqlRequestTime`
        :param risk_levels: 风险级别 - HIGH - MEDIUM - LOW - NO_RISK
        :type risk_levels: str
        :param client_ip: 客户端IP
        :type client_ip: str
        :param client_name: 客户端名称
        :type client_name: str
        :param db_ip: 数据库IP
        :type db_ip: str
        :param db_user: 数据库用户
        :type db_user: str
        :param query_type: 查询类型 LOGIN,CREATE_TABLE,CREATE_TABLESPACE,DROP_TABLE, DROP_TABLESPACE,DELETE,INSERT,INSERT_SELECT,SELECT,SELECT_FOR_UPDATE, UPDATE,CREATE_USER,DROP_USER,GRANT,OPERATE ALL
        :type query_type: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param sql_statement: sql语句
        :type sql_statement: str
        :param sql_response: 响应结果 - SUCCESS - FAILED
        :type sql_response: str
        :param page: 页码
        :type page: int
        :param size: 条数
        :type size: int
        :param time_order: 时间顺序 - DESC - ASC
        :type time_order: str
        """
        
        

        self._time = None
        self._risk_levels = None
        self._client_ip = None
        self._client_name = None
        self._db_ip = None
        self._db_user = None
        self._query_type = None
        self._rule_name = None
        self._sql_statement = None
        self._sql_response = None
        self._page = None
        self._size = None
        self._time_order = None
        self.discriminator = None

        self.time = time
        if risk_levels is not None:
            self.risk_levels = risk_levels
        if client_ip is not None:
            self.client_ip = client_ip
        if client_name is not None:
            self.client_name = client_name
        if db_ip is not None:
            self.db_ip = db_ip
        if db_user is not None:
            self.db_user = db_user
        if query_type is not None:
            self.query_type = query_type
        if rule_name is not None:
            self.rule_name = rule_name
        if sql_statement is not None:
            self.sql_statement = sql_statement
        if sql_response is not None:
            self.sql_response = sql_response
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if time_order is not None:
            self.time_order = time_order

    @property
    def time(self):
        r"""Gets the time of this AuditSqlRequest.

        :return: The time of this AuditSqlRequest.
        :rtype: :class:`huaweicloudsdkdbss.v1.AuditSqlRequestTime`
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this AuditSqlRequest.

        :param time: The time of this AuditSqlRequest.
        :type time: :class:`huaweicloudsdkdbss.v1.AuditSqlRequestTime`
        """
        self._time = time

    @property
    def risk_levels(self):
        r"""Gets the risk_levels of this AuditSqlRequest.

        风险级别 - HIGH - MEDIUM - LOW - NO_RISK

        :return: The risk_levels of this AuditSqlRequest.
        :rtype: str
        """
        return self._risk_levels

    @risk_levels.setter
    def risk_levels(self, risk_levels):
        r"""Sets the risk_levels of this AuditSqlRequest.

        风险级别 - HIGH - MEDIUM - LOW - NO_RISK

        :param risk_levels: The risk_levels of this AuditSqlRequest.
        :type risk_levels: str
        """
        self._risk_levels = risk_levels

    @property
    def client_ip(self):
        r"""Gets the client_ip of this AuditSqlRequest.

        客户端IP

        :return: The client_ip of this AuditSqlRequest.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this AuditSqlRequest.

        客户端IP

        :param client_ip: The client_ip of this AuditSqlRequest.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def client_name(self):
        r"""Gets the client_name of this AuditSqlRequest.

        客户端名称

        :return: The client_name of this AuditSqlRequest.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        r"""Sets the client_name of this AuditSqlRequest.

        客户端名称

        :param client_name: The client_name of this AuditSqlRequest.
        :type client_name: str
        """
        self._client_name = client_name

    @property
    def db_ip(self):
        r"""Gets the db_ip of this AuditSqlRequest.

        数据库IP

        :return: The db_ip of this AuditSqlRequest.
        :rtype: str
        """
        return self._db_ip

    @db_ip.setter
    def db_ip(self, db_ip):
        r"""Sets the db_ip of this AuditSqlRequest.

        数据库IP

        :param db_ip: The db_ip of this AuditSqlRequest.
        :type db_ip: str
        """
        self._db_ip = db_ip

    @property
    def db_user(self):
        r"""Gets the db_user of this AuditSqlRequest.

        数据库用户

        :return: The db_user of this AuditSqlRequest.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        r"""Sets the db_user of this AuditSqlRequest.

        数据库用户

        :param db_user: The db_user of this AuditSqlRequest.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def query_type(self):
        r"""Gets the query_type of this AuditSqlRequest.

        查询类型 LOGIN,CREATE_TABLE,CREATE_TABLESPACE,DROP_TABLE, DROP_TABLESPACE,DELETE,INSERT,INSERT_SELECT,SELECT,SELECT_FOR_UPDATE, UPDATE,CREATE_USER,DROP_USER,GRANT,OPERATE ALL

        :return: The query_type of this AuditSqlRequest.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this AuditSqlRequest.

        查询类型 LOGIN,CREATE_TABLE,CREATE_TABLESPACE,DROP_TABLE, DROP_TABLESPACE,DELETE,INSERT,INSERT_SELECT,SELECT,SELECT_FOR_UPDATE, UPDATE,CREATE_USER,DROP_USER,GRANT,OPERATE ALL

        :param query_type: The query_type of this AuditSqlRequest.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def rule_name(self):
        r"""Gets the rule_name of this AuditSqlRequest.

        规则名称

        :return: The rule_name of this AuditSqlRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this AuditSqlRequest.

        规则名称

        :param rule_name: The rule_name of this AuditSqlRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this AuditSqlRequest.

        sql语句

        :return: The sql_statement of this AuditSqlRequest.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this AuditSqlRequest.

        sql语句

        :param sql_statement: The sql_statement of this AuditSqlRequest.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def sql_response(self):
        r"""Gets the sql_response of this AuditSqlRequest.

        响应结果 - SUCCESS - FAILED

        :return: The sql_response of this AuditSqlRequest.
        :rtype: str
        """
        return self._sql_response

    @sql_response.setter
    def sql_response(self, sql_response):
        r"""Sets the sql_response of this AuditSqlRequest.

        响应结果 - SUCCESS - FAILED

        :param sql_response: The sql_response of this AuditSqlRequest.
        :type sql_response: str
        """
        self._sql_response = sql_response

    @property
    def page(self):
        r"""Gets the page of this AuditSqlRequest.

        页码

        :return: The page of this AuditSqlRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this AuditSqlRequest.

        页码

        :param page: The page of this AuditSqlRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this AuditSqlRequest.

        条数

        :return: The size of this AuditSqlRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this AuditSqlRequest.

        条数

        :param size: The size of this AuditSqlRequest.
        :type size: int
        """
        self._size = size

    @property
    def time_order(self):
        r"""Gets the time_order of this AuditSqlRequest.

        时间顺序 - DESC - ASC

        :return: The time_order of this AuditSqlRequest.
        :rtype: str
        """
        return self._time_order

    @time_order.setter
    def time_order(self, time_order):
        r"""Sets the time_order of this AuditSqlRequest.

        时间顺序 - DESC - ASC

        :param time_order: The time_order of this AuditSqlRequest.
        :type time_order: str
        """
        self._time_order = time_order

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
        if not isinstance(other, AuditSqlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
