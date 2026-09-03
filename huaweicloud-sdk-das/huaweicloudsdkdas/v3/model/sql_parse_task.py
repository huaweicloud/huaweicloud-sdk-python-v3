# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlParseTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'instance_id': 'str',
        'instance_name': 'str',
        'node_id': 'str',
        'domain_id': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'batch_id': 'str',
        'user_list': 'list[str]',
        'keyword': 'list[str]',
        'db_list': 'list[str]',
        'operation_list': 'list[str]',
        'thread_id_list': 'list[str]',
        'trx_id_list': 'list[str]',
        'status_list': 'list[str]',
        'sql_template_ids': 'list[str]',
        'status': 'int',
        'create_at': 'int',
        'update_at': 'int',
        'progress': 'float',
        'reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'node_id': 'node_id',
        'domain_id': 'domain_id',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'batch_id': 'batch_id',
        'user_list': 'user_list',
        'keyword': 'keyword',
        'db_list': 'db_list',
        'operation_list': 'operation_list',
        'thread_id_list': 'thread_id_list',
        'trx_id_list': 'trx_id_list',
        'status_list': 'status_list',
        'sql_template_ids': 'sql_template_ids',
        'status': 'status',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'progress': 'progress',
        'reason': 'reason'
    }

    def __init__(self, id=None, instance_id=None, instance_name=None, node_id=None, domain_id=None, start_at=None, end_at=None, batch_id=None, user_list=None, keyword=None, db_list=None, operation_list=None, thread_id_list=None, trx_id_list=None, status_list=None, sql_template_ids=None, status=None, create_at=None, update_at=None, progress=None, reason=None):
        r"""SqlParseTask

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: int
        :param instance_id: 实例ID
        :type instance_id: str
        :param instance_name: 实例名
        :type instance_name: str
        :param node_id: 节点ID
        :type node_id: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param start_at: 开始时间（Unix timestamp），单位：毫秒
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒
        :type end_at: int
        :param batch_id: 批次ID
        :type batch_id: str
        :param user_list: 用户名
        :type user_list: list[str]
        :param keyword: 关键字
        :type keyword: list[str]
        :param db_list: 数据库
        :type db_list: list[str]
        :param operation_list: 操作类型
        :type operation_list: list[str]
        :param thread_id_list: 线程ID
        :type thread_id_list: list[str]
        :param trx_id_list: 事务ID
        :type trx_id_list: list[str]
        :param status_list: 执行状态
        :type status_list: list[str]
        :param sql_template_ids: SQL模板ID
        :type sql_template_ids: list[str]
        :param status: 任务状态
        :type status: int
        :param create_at: 创建时间（Unix timestamp），单位：毫秒
        :type create_at: int
        :param update_at: 更新时间（Unix timestamp），单位：毫秒
        :type update_at: int
        :param progress: 任务进度
        :type progress: float
        :param reason: 失败原因
        :type reason: str
        """
        
        

        self._id = None
        self._instance_id = None
        self._instance_name = None
        self._node_id = None
        self._domain_id = None
        self._start_at = None
        self._end_at = None
        self._batch_id = None
        self._user_list = None
        self._keyword = None
        self._db_list = None
        self._operation_list = None
        self._thread_id_list = None
        self._trx_id_list = None
        self._status_list = None
        self._sql_template_ids = None
        self._status = None
        self._create_at = None
        self._update_at = None
        self._progress = None
        self._reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if node_id is not None:
            self.node_id = node_id
        if domain_id is not None:
            self.domain_id = domain_id
        if start_at is not None:
            self.start_at = start_at
        if end_at is not None:
            self.end_at = end_at
        if batch_id is not None:
            self.batch_id = batch_id
        if user_list is not None:
            self.user_list = user_list
        if keyword is not None:
            self.keyword = keyword
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
        if status is not None:
            self.status = status
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if progress is not None:
            self.progress = progress
        if reason is not None:
            self.reason = reason

    @property
    def id(self):
        r"""Gets the id of this SqlParseTask.

        任务ID

        :return: The id of this SqlParseTask.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SqlParseTask.

        任务ID

        :param id: The id of this SqlParseTask.
        :type id: int
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SqlParseTask.

        实例ID

        :return: The instance_id of this SqlParseTask.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SqlParseTask.

        实例ID

        :param instance_id: The instance_id of this SqlParseTask.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this SqlParseTask.

        实例名

        :return: The instance_name of this SqlParseTask.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this SqlParseTask.

        实例名

        :param instance_name: The instance_name of this SqlParseTask.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def node_id(self):
        r"""Gets the node_id of this SqlParseTask.

        节点ID

        :return: The node_id of this SqlParseTask.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SqlParseTask.

        节点ID

        :param node_id: The node_id of this SqlParseTask.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this SqlParseTask.

        租户ID

        :return: The domain_id of this SqlParseTask.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this SqlParseTask.

        租户ID

        :param domain_id: The domain_id of this SqlParseTask.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def start_at(self):
        r"""Gets the start_at of this SqlParseTask.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_at of this SqlParseTask.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this SqlParseTask.

        开始时间（Unix timestamp），单位：毫秒

        :param start_at: The start_at of this SqlParseTask.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this SqlParseTask.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_at of this SqlParseTask.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this SqlParseTask.

        结束时间（Unix timestamp），单位：毫秒

        :param end_at: The end_at of this SqlParseTask.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def batch_id(self):
        r"""Gets the batch_id of this SqlParseTask.

        批次ID

        :return: The batch_id of this SqlParseTask.
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        r"""Sets the batch_id of this SqlParseTask.

        批次ID

        :param batch_id: The batch_id of this SqlParseTask.
        :type batch_id: str
        """
        self._batch_id = batch_id

    @property
    def user_list(self):
        r"""Gets the user_list of this SqlParseTask.

        用户名

        :return: The user_list of this SqlParseTask.
        :rtype: list[str]
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        r"""Sets the user_list of this SqlParseTask.

        用户名

        :param user_list: The user_list of this SqlParseTask.
        :type user_list: list[str]
        """
        self._user_list = user_list

    @property
    def keyword(self):
        r"""Gets the keyword of this SqlParseTask.

        关键字

        :return: The keyword of this SqlParseTask.
        :rtype: list[str]
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this SqlParseTask.

        关键字

        :param keyword: The keyword of this SqlParseTask.
        :type keyword: list[str]
        """
        self._keyword = keyword

    @property
    def db_list(self):
        r"""Gets the db_list of this SqlParseTask.

        数据库

        :return: The db_list of this SqlParseTask.
        :rtype: list[str]
        """
        return self._db_list

    @db_list.setter
    def db_list(self, db_list):
        r"""Sets the db_list of this SqlParseTask.

        数据库

        :param db_list: The db_list of this SqlParseTask.
        :type db_list: list[str]
        """
        self._db_list = db_list

    @property
    def operation_list(self):
        r"""Gets the operation_list of this SqlParseTask.

        操作类型

        :return: The operation_list of this SqlParseTask.
        :rtype: list[str]
        """
        return self._operation_list

    @operation_list.setter
    def operation_list(self, operation_list):
        r"""Sets the operation_list of this SqlParseTask.

        操作类型

        :param operation_list: The operation_list of this SqlParseTask.
        :type operation_list: list[str]
        """
        self._operation_list = operation_list

    @property
    def thread_id_list(self):
        r"""Gets the thread_id_list of this SqlParseTask.

        线程ID

        :return: The thread_id_list of this SqlParseTask.
        :rtype: list[str]
        """
        return self._thread_id_list

    @thread_id_list.setter
    def thread_id_list(self, thread_id_list):
        r"""Sets the thread_id_list of this SqlParseTask.

        线程ID

        :param thread_id_list: The thread_id_list of this SqlParseTask.
        :type thread_id_list: list[str]
        """
        self._thread_id_list = thread_id_list

    @property
    def trx_id_list(self):
        r"""Gets the trx_id_list of this SqlParseTask.

        事务ID

        :return: The trx_id_list of this SqlParseTask.
        :rtype: list[str]
        """
        return self._trx_id_list

    @trx_id_list.setter
    def trx_id_list(self, trx_id_list):
        r"""Sets the trx_id_list of this SqlParseTask.

        事务ID

        :param trx_id_list: The trx_id_list of this SqlParseTask.
        :type trx_id_list: list[str]
        """
        self._trx_id_list = trx_id_list

    @property
    def status_list(self):
        r"""Gets the status_list of this SqlParseTask.

        执行状态

        :return: The status_list of this SqlParseTask.
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this SqlParseTask.

        执行状态

        :param status_list: The status_list of this SqlParseTask.
        :type status_list: list[str]
        """
        self._status_list = status_list

    @property
    def sql_template_ids(self):
        r"""Gets the sql_template_ids of this SqlParseTask.

        SQL模板ID

        :return: The sql_template_ids of this SqlParseTask.
        :rtype: list[str]
        """
        return self._sql_template_ids

    @sql_template_ids.setter
    def sql_template_ids(self, sql_template_ids):
        r"""Sets the sql_template_ids of this SqlParseTask.

        SQL模板ID

        :param sql_template_ids: The sql_template_ids of this SqlParseTask.
        :type sql_template_ids: list[str]
        """
        self._sql_template_ids = sql_template_ids

    @property
    def status(self):
        r"""Gets the status of this SqlParseTask.

        任务状态

        :return: The status of this SqlParseTask.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SqlParseTask.

        任务状态

        :param status: The status of this SqlParseTask.
        :type status: int
        """
        self._status = status

    @property
    def create_at(self):
        r"""Gets the create_at of this SqlParseTask.

        创建时间（Unix timestamp），单位：毫秒

        :return: The create_at of this SqlParseTask.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this SqlParseTask.

        创建时间（Unix timestamp），单位：毫秒

        :param create_at: The create_at of this SqlParseTask.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this SqlParseTask.

        更新时间（Unix timestamp），单位：毫秒

        :return: The update_at of this SqlParseTask.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this SqlParseTask.

        更新时间（Unix timestamp），单位：毫秒

        :param update_at: The update_at of this SqlParseTask.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def progress(self):
        r"""Gets the progress of this SqlParseTask.

        任务进度

        :return: The progress of this SqlParseTask.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this SqlParseTask.

        任务进度

        :param progress: The progress of this SqlParseTask.
        :type progress: float
        """
        self._progress = progress

    @property
    def reason(self):
        r"""Gets the reason of this SqlParseTask.

        失败原因

        :return: The reason of this SqlParseTask.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this SqlParseTask.

        失败原因

        :param reason: The reason of this SqlParseTask.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, SqlParseTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
