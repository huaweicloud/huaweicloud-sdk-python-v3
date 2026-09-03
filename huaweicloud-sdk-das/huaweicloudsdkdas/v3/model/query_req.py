# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'node_id': 'str',
        'keyword': 'str',
        'user_list': 'str',
        'db_list': 'str',
        'operation_list': 'str',
        'thread_id_list': 'str',
        'trx_id_list': 'str',
        'status_list': 'str',
        'sql_template_ids': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'node_id': 'node_id',
        'keyword': 'keyword',
        'user_list': 'user_list',
        'db_list': 'db_list',
        'operation_list': 'operation_list',
        'thread_id_list': 'thread_id_list',
        'trx_id_list': 'trx_id_list',
        'status_list': 'status_list',
        'sql_template_ids': 'sql_template_ids'
    }

    def __init__(self, instance_id=None, start_at=None, end_at=None, node_id=None, keyword=None, user_list=None, db_list=None, operation_list=None, thread_id_list=None, trx_id_list=None, status_list=None, sql_template_ids=None):
        r"""QueryReq

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，实例的唯一标识
        :type instance_id: str
        :param start_at: 开始时间（Unix timestamp），单位：毫秒
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒
        :type end_at: int
        :param node_id: 节点ID，实例节点的唯一标识
        :type node_id: str
        :param keyword: 关键字，可组合，用逗号分隔
        :type keyword: str
        :param user_list: 用户名，可组合，用逗号分隔
        :type user_list: str
        :param db_list: 数据库，可组合，用逗号分隔
        :type db_list: str
        :param operation_list: 操作类型，可组合，用逗号分隔
        :type operation_list: str
        :param thread_id_list: 线程ID，可组合，用逗号分隔
        :type thread_id_list: str
        :param trx_id_list: 事务ID，可组合，用逗号分隔
        :type trx_id_list: str
        :param status_list: 执行状态，可组合，用逗号分隔
        :type status_list: str
        :param sql_template_ids: SQL模板ID，可组合，用逗号分隔
        :type sql_template_ids: str
        """
        
        

        self._instance_id = None
        self._start_at = None
        self._end_at = None
        self._node_id = None
        self._keyword = None
        self._user_list = None
        self._db_list = None
        self._operation_list = None
        self._thread_id_list = None
        self._trx_id_list = None
        self._status_list = None
        self._sql_template_ids = None
        self.discriminator = None

        self.instance_id = instance_id
        self.start_at = start_at
        self.end_at = end_at
        if node_id is not None:
            self.node_id = node_id
        if keyword is not None:
            self.keyword = keyword
        if user_list is not None:
            self.user_list = user_list
        if db_list is not None:
            self.db_list = db_list
        if operation_list is not None:
            self.operation_list = operation_list
        if thread_id_list is not None:
            self.thread_id_list = thread_id_list
        if trx_id_list is not None:
            self.trx_id_list = trx_id_list
        if status_list is not None:
            self.status_list = status_list
        if sql_template_ids is not None:
            self.sql_template_ids = sql_template_ids

    @property
    def instance_id(self):
        r"""Gets the instance_id of this QueryReq.

        实例ID，实例的唯一标识

        :return: The instance_id of this QueryReq.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this QueryReq.

        实例ID，实例的唯一标识

        :param instance_id: The instance_id of this QueryReq.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_at(self):
        r"""Gets the start_at of this QueryReq.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_at of this QueryReq.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this QueryReq.

        开始时间（Unix timestamp），单位：毫秒

        :param start_at: The start_at of this QueryReq.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this QueryReq.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_at of this QueryReq.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this QueryReq.

        结束时间（Unix timestamp），单位：毫秒

        :param end_at: The end_at of this QueryReq.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def node_id(self):
        r"""Gets the node_id of this QueryReq.

        节点ID，实例节点的唯一标识

        :return: The node_id of this QueryReq.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this QueryReq.

        节点ID，实例节点的唯一标识

        :param node_id: The node_id of this QueryReq.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def keyword(self):
        r"""Gets the keyword of this QueryReq.

        关键字，可组合，用逗号分隔

        :return: The keyword of this QueryReq.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this QueryReq.

        关键字，可组合，用逗号分隔

        :param keyword: The keyword of this QueryReq.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def user_list(self):
        r"""Gets the user_list of this QueryReq.

        用户名，可组合，用逗号分隔

        :return: The user_list of this QueryReq.
        :rtype: str
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        r"""Sets the user_list of this QueryReq.

        用户名，可组合，用逗号分隔

        :param user_list: The user_list of this QueryReq.
        :type user_list: str
        """
        self._user_list = user_list

    @property
    def db_list(self):
        r"""Gets the db_list of this QueryReq.

        数据库，可组合，用逗号分隔

        :return: The db_list of this QueryReq.
        :rtype: str
        """
        return self._db_list

    @db_list.setter
    def db_list(self, db_list):
        r"""Sets the db_list of this QueryReq.

        数据库，可组合，用逗号分隔

        :param db_list: The db_list of this QueryReq.
        :type db_list: str
        """
        self._db_list = db_list

    @property
    def operation_list(self):
        r"""Gets the operation_list of this QueryReq.

        操作类型，可组合，用逗号分隔

        :return: The operation_list of this QueryReq.
        :rtype: str
        """
        return self._operation_list

    @operation_list.setter
    def operation_list(self, operation_list):
        r"""Sets the operation_list of this QueryReq.

        操作类型，可组合，用逗号分隔

        :param operation_list: The operation_list of this QueryReq.
        :type operation_list: str
        """
        self._operation_list = operation_list

    @property
    def thread_id_list(self):
        r"""Gets the thread_id_list of this QueryReq.

        线程ID，可组合，用逗号分隔

        :return: The thread_id_list of this QueryReq.
        :rtype: str
        """
        return self._thread_id_list

    @thread_id_list.setter
    def thread_id_list(self, thread_id_list):
        r"""Sets the thread_id_list of this QueryReq.

        线程ID，可组合，用逗号分隔

        :param thread_id_list: The thread_id_list of this QueryReq.
        :type thread_id_list: str
        """
        self._thread_id_list = thread_id_list

    @property
    def trx_id_list(self):
        r"""Gets the trx_id_list of this QueryReq.

        事务ID，可组合，用逗号分隔

        :return: The trx_id_list of this QueryReq.
        :rtype: str
        """
        return self._trx_id_list

    @trx_id_list.setter
    def trx_id_list(self, trx_id_list):
        r"""Sets the trx_id_list of this QueryReq.

        事务ID，可组合，用逗号分隔

        :param trx_id_list: The trx_id_list of this QueryReq.
        :type trx_id_list: str
        """
        self._trx_id_list = trx_id_list

    @property
    def status_list(self):
        r"""Gets the status_list of this QueryReq.

        执行状态，可组合，用逗号分隔

        :return: The status_list of this QueryReq.
        :rtype: str
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this QueryReq.

        执行状态，可组合，用逗号分隔

        :param status_list: The status_list of this QueryReq.
        :type status_list: str
        """
        self._status_list = status_list

    @property
    def sql_template_ids(self):
        r"""Gets the sql_template_ids of this QueryReq.

        SQL模板ID，可组合，用逗号分隔

        :return: The sql_template_ids of this QueryReq.
        :rtype: str
        """
        return self._sql_template_ids

    @sql_template_ids.setter
    def sql_template_ids(self, sql_template_ids):
        r"""Sets the sql_template_ids of this QueryReq.

        SQL模板ID，可组合，用逗号分隔

        :param sql_template_ids: The sql_template_ids of this QueryReq.
        :type sql_template_ids: str
        """
        self._sql_template_ids = sql_template_ids

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
        if not isinstance(other, QueryReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
