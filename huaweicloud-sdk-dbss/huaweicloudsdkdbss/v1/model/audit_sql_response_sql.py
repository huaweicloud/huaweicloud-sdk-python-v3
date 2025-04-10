# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditSqlResponseSql:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'sql_statement': 'str',
        'client_ip': 'str',
        'client_name': 'str',
        'db_ip': 'str',
        'db_user': 'str',
        'query_type': 'str',
        'operated_obj_info': 'list[AuditSqlResponseSqlOperatedObjInfo]',
        'rule_name': 'str',
        'risk_level': 'str',
        'start_time': 'str',
        'sql_response': 'str',
        'db_instance': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sql_statement': 'sql_statement',
        'client_ip': 'client_ip',
        'client_name': 'client_name',
        'db_ip': 'db_ip',
        'db_user': 'db_user',
        'query_type': 'query_type',
        'operated_obj_info': 'operated_obj_info',
        'rule_name': 'rule_name',
        'risk_level': 'risk_level',
        'start_time': 'start_time',
        'sql_response': 'sql_response',
        'db_instance': 'db_instance'
    }

    def __init__(self, id=None, sql_statement=None, client_ip=None, client_name=None, db_ip=None, db_user=None, query_type=None, operated_obj_info=None, rule_name=None, risk_level=None, start_time=None, sql_response=None, db_instance=None):
        r"""AuditSqlResponseSql

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param sql_statement: sql语句
        :type sql_statement: str
        :param client_ip: 客户端IP
        :type client_ip: str
        :param client_name: 客户端名称
        :type client_name: str
        :param db_ip: 数据库IP
        :type db_ip: str
        :param db_user: 数据库用户名
        :type db_user: str
        :param query_type: 查询类型 LOGIN,CREATE_TABLE,CREATE_TABLESPACE,DROP_TABLE, DROP_TABLESPACE,DELETE,INSERT,INSERT_SELECT,SELECT,SELECT_FOR_UPDATE, UPDATE,CREATE_USER,DROP_USER,GRANT,OPERATE ALL
        :type query_type: str
        :param operated_obj_info: 操作对象列表
        :type operated_obj_info: list[:class:`huaweicloudsdkdbss.v1.AuditSqlResponseSqlOperatedObjInfo`]
        :param rule_name: 规则名称
        :type rule_name: str
        :param risk_level: 风险级别 - HIGH - MEDIUM - LOW - NO_RISK
        :type risk_level: str
        :param start_time: 审计开始时间
        :type start_time: str
        :param sql_response: 响应结果 - SUCCESS - FAILED
        :type sql_response: str
        :param db_instance: 数据库实例
        :type db_instance: str
        """
        
        

        self._id = None
        self._sql_statement = None
        self._client_ip = None
        self._client_name = None
        self._db_ip = None
        self._db_user = None
        self._query_type = None
        self._operated_obj_info = None
        self._rule_name = None
        self._risk_level = None
        self._start_time = None
        self._sql_response = None
        self._db_instance = None
        self.discriminator = None

        self.id = id
        if sql_statement is not None:
            self.sql_statement = sql_statement
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
        if operated_obj_info is not None:
            self.operated_obj_info = operated_obj_info
        if rule_name is not None:
            self.rule_name = rule_name
        if risk_level is not None:
            self.risk_level = risk_level
        if start_time is not None:
            self.start_time = start_time
        self.sql_response = sql_response
        if db_instance is not None:
            self.db_instance = db_instance

    @property
    def id(self):
        r"""Gets the id of this AuditSqlResponseSql.

        ID

        :return: The id of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AuditSqlResponseSql.

        ID

        :param id: The id of this AuditSqlResponseSql.
        :type id: str
        """
        self._id = id

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this AuditSqlResponseSql.

        sql语句

        :return: The sql_statement of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this AuditSqlResponseSql.

        sql语句

        :param sql_statement: The sql_statement of this AuditSqlResponseSql.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def client_ip(self):
        r"""Gets the client_ip of this AuditSqlResponseSql.

        客户端IP

        :return: The client_ip of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this AuditSqlResponseSql.

        客户端IP

        :param client_ip: The client_ip of this AuditSqlResponseSql.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def client_name(self):
        r"""Gets the client_name of this AuditSqlResponseSql.

        客户端名称

        :return: The client_name of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        r"""Sets the client_name of this AuditSqlResponseSql.

        客户端名称

        :param client_name: The client_name of this AuditSqlResponseSql.
        :type client_name: str
        """
        self._client_name = client_name

    @property
    def db_ip(self):
        r"""Gets the db_ip of this AuditSqlResponseSql.

        数据库IP

        :return: The db_ip of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._db_ip

    @db_ip.setter
    def db_ip(self, db_ip):
        r"""Sets the db_ip of this AuditSqlResponseSql.

        数据库IP

        :param db_ip: The db_ip of this AuditSqlResponseSql.
        :type db_ip: str
        """
        self._db_ip = db_ip

    @property
    def db_user(self):
        r"""Gets the db_user of this AuditSqlResponseSql.

        数据库用户名

        :return: The db_user of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        r"""Sets the db_user of this AuditSqlResponseSql.

        数据库用户名

        :param db_user: The db_user of this AuditSqlResponseSql.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def query_type(self):
        r"""Gets the query_type of this AuditSqlResponseSql.

        查询类型 LOGIN,CREATE_TABLE,CREATE_TABLESPACE,DROP_TABLE, DROP_TABLESPACE,DELETE,INSERT,INSERT_SELECT,SELECT,SELECT_FOR_UPDATE, UPDATE,CREATE_USER,DROP_USER,GRANT,OPERATE ALL

        :return: The query_type of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this AuditSqlResponseSql.

        查询类型 LOGIN,CREATE_TABLE,CREATE_TABLESPACE,DROP_TABLE, DROP_TABLESPACE,DELETE,INSERT,INSERT_SELECT,SELECT,SELECT_FOR_UPDATE, UPDATE,CREATE_USER,DROP_USER,GRANT,OPERATE ALL

        :param query_type: The query_type of this AuditSqlResponseSql.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def operated_obj_info(self):
        r"""Gets the operated_obj_info of this AuditSqlResponseSql.

        操作对象列表

        :return: The operated_obj_info of this AuditSqlResponseSql.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.AuditSqlResponseSqlOperatedObjInfo`]
        """
        return self._operated_obj_info

    @operated_obj_info.setter
    def operated_obj_info(self, operated_obj_info):
        r"""Sets the operated_obj_info of this AuditSqlResponseSql.

        操作对象列表

        :param operated_obj_info: The operated_obj_info of this AuditSqlResponseSql.
        :type operated_obj_info: list[:class:`huaweicloudsdkdbss.v1.AuditSqlResponseSqlOperatedObjInfo`]
        """
        self._operated_obj_info = operated_obj_info

    @property
    def rule_name(self):
        r"""Gets the rule_name of this AuditSqlResponseSql.

        规则名称

        :return: The rule_name of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this AuditSqlResponseSql.

        规则名称

        :param rule_name: The rule_name of this AuditSqlResponseSql.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def risk_level(self):
        r"""Gets the risk_level of this AuditSqlResponseSql.

        风险级别 - HIGH - MEDIUM - LOW - NO_RISK

        :return: The risk_level of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this AuditSqlResponseSql.

        风险级别 - HIGH - MEDIUM - LOW - NO_RISK

        :param risk_level: The risk_level of this AuditSqlResponseSql.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def start_time(self):
        r"""Gets the start_time of this AuditSqlResponseSql.

        审计开始时间

        :return: The start_time of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this AuditSqlResponseSql.

        审计开始时间

        :param start_time: The start_time of this AuditSqlResponseSql.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def sql_response(self):
        r"""Gets the sql_response of this AuditSqlResponseSql.

        响应结果 - SUCCESS - FAILED

        :return: The sql_response of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._sql_response

    @sql_response.setter
    def sql_response(self, sql_response):
        r"""Sets the sql_response of this AuditSqlResponseSql.

        响应结果 - SUCCESS - FAILED

        :param sql_response: The sql_response of this AuditSqlResponseSql.
        :type sql_response: str
        """
        self._sql_response = sql_response

    @property
    def db_instance(self):
        r"""Gets the db_instance of this AuditSqlResponseSql.

        数据库实例

        :return: The db_instance of this AuditSqlResponseSql.
        :rtype: str
        """
        return self._db_instance

    @db_instance.setter
    def db_instance(self, db_instance):
        r"""Sets the db_instance of this AuditSqlResponseSql.

        数据库实例

        :param db_instance: The db_instance of this AuditSqlResponseSql.
        :type db_instance: str
        """
        self._db_instance = db_instance

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
        if not isinstance(other, AuditSqlResponseSql):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
