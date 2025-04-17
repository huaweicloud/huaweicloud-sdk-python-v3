# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddFullSqlTaskBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'str',
        'node_id': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'user_list': 'list[str]',
        'keyword_list': 'list[str]',
        'db_list': 'list[str]',
        'operation_list': 'list[str]',
        'thread_id_list': 'list[str]',
        'status_list': 'list[str]'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'node_id': 'node_id',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'user_list': 'user_list',
        'keyword_list': 'keyword_list',
        'db_list': 'db_list',
        'operation_list': 'operation_list',
        'thread_id_list': 'thread_id_list',
        'status_list': 'status_list'
    }

    def __init__(self, datastore_type=None, node_id=None, start_at=None, end_at=None, user_list=None, keyword_list=None, db_list=None, operation_list=None, thread_id_list=None, status_list=None):
        r"""AddFullSqlTaskBody

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库引擎
        :type datastore_type: str
        :param node_id: 节点ID，有值时创建节点维度任务
        :type node_id: str
        :param start_at: 开始时间（Unix timestamp），单位：毫秒
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒
        :type end_at: int
        :param user_list: 用户名列表，最大长度20
        :type user_list: list[str]
        :param keyword_list: 关键字列表，最大长度20
        :type keyword_list: list[str]
        :param db_list: 数据库列表，最大长度20
        :type db_list: list[str]
        :param operation_list: 操作类型列表，最大长度20
        :type operation_list: list[str]
        :param thread_id_list: 线程id列表，最大长度20
        :type thread_id_list: list[str]
        :param status_list: 执行状态列表，\&quot;0\&quot;为成功，\&quot;1\&quot;为失败，最大长度20
        :type status_list: list[str]
        """
        
        

        self._datastore_type = None
        self._node_id = None
        self._start_at = None
        self._end_at = None
        self._user_list = None
        self._keyword_list = None
        self._db_list = None
        self._operation_list = None
        self._thread_id_list = None
        self._status_list = None
        self.discriminator = None

        self.datastore_type = datastore_type
        if node_id is not None:
            self.node_id = node_id
        self.start_at = start_at
        self.end_at = end_at
        if user_list is not None:
            self.user_list = user_list
        if keyword_list is not None:
            self.keyword_list = keyword_list
        if db_list is not None:
            self.db_list = db_list
        if operation_list is not None:
            self.operation_list = operation_list
        if thread_id_list is not None:
            self.thread_id_list = thread_id_list
        if status_list is not None:
            self.status_list = status_list

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this AddFullSqlTaskBody.

        数据库引擎

        :return: The datastore_type of this AddFullSqlTaskBody.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this AddFullSqlTaskBody.

        数据库引擎

        :param datastore_type: The datastore_type of this AddFullSqlTaskBody.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def node_id(self):
        r"""Gets the node_id of this AddFullSqlTaskBody.

        节点ID，有值时创建节点维度任务

        :return: The node_id of this AddFullSqlTaskBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this AddFullSqlTaskBody.

        节点ID，有值时创建节点维度任务

        :param node_id: The node_id of this AddFullSqlTaskBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def start_at(self):
        r"""Gets the start_at of this AddFullSqlTaskBody.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_at of this AddFullSqlTaskBody.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this AddFullSqlTaskBody.

        开始时间（Unix timestamp），单位：毫秒

        :param start_at: The start_at of this AddFullSqlTaskBody.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this AddFullSqlTaskBody.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_at of this AddFullSqlTaskBody.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this AddFullSqlTaskBody.

        结束时间（Unix timestamp），单位：毫秒

        :param end_at: The end_at of this AddFullSqlTaskBody.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def user_list(self):
        r"""Gets the user_list of this AddFullSqlTaskBody.

        用户名列表，最大长度20

        :return: The user_list of this AddFullSqlTaskBody.
        :rtype: list[str]
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        r"""Sets the user_list of this AddFullSqlTaskBody.

        用户名列表，最大长度20

        :param user_list: The user_list of this AddFullSqlTaskBody.
        :type user_list: list[str]
        """
        self._user_list = user_list

    @property
    def keyword_list(self):
        r"""Gets the keyword_list of this AddFullSqlTaskBody.

        关键字列表，最大长度20

        :return: The keyword_list of this AddFullSqlTaskBody.
        :rtype: list[str]
        """
        return self._keyword_list

    @keyword_list.setter
    def keyword_list(self, keyword_list):
        r"""Sets the keyword_list of this AddFullSqlTaskBody.

        关键字列表，最大长度20

        :param keyword_list: The keyword_list of this AddFullSqlTaskBody.
        :type keyword_list: list[str]
        """
        self._keyword_list = keyword_list

    @property
    def db_list(self):
        r"""Gets the db_list of this AddFullSqlTaskBody.

        数据库列表，最大长度20

        :return: The db_list of this AddFullSqlTaskBody.
        :rtype: list[str]
        """
        return self._db_list

    @db_list.setter
    def db_list(self, db_list):
        r"""Sets the db_list of this AddFullSqlTaskBody.

        数据库列表，最大长度20

        :param db_list: The db_list of this AddFullSqlTaskBody.
        :type db_list: list[str]
        """
        self._db_list = db_list

    @property
    def operation_list(self):
        r"""Gets the operation_list of this AddFullSqlTaskBody.

        操作类型列表，最大长度20

        :return: The operation_list of this AddFullSqlTaskBody.
        :rtype: list[str]
        """
        return self._operation_list

    @operation_list.setter
    def operation_list(self, operation_list):
        r"""Sets the operation_list of this AddFullSqlTaskBody.

        操作类型列表，最大长度20

        :param operation_list: The operation_list of this AddFullSqlTaskBody.
        :type operation_list: list[str]
        """
        self._operation_list = operation_list

    @property
    def thread_id_list(self):
        r"""Gets the thread_id_list of this AddFullSqlTaskBody.

        线程id列表，最大长度20

        :return: The thread_id_list of this AddFullSqlTaskBody.
        :rtype: list[str]
        """
        return self._thread_id_list

    @thread_id_list.setter
    def thread_id_list(self, thread_id_list):
        r"""Sets the thread_id_list of this AddFullSqlTaskBody.

        线程id列表，最大长度20

        :param thread_id_list: The thread_id_list of this AddFullSqlTaskBody.
        :type thread_id_list: list[str]
        """
        self._thread_id_list = thread_id_list

    @property
    def status_list(self):
        r"""Gets the status_list of this AddFullSqlTaskBody.

        执行状态列表，\"0\"为成功，\"1\"为失败，最大长度20

        :return: The status_list of this AddFullSqlTaskBody.
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this AddFullSqlTaskBody.

        执行状态列表，\"0\"为成功，\"1\"为失败，最大长度20

        :param status_list: The status_list of this AddFullSqlTaskBody.
        :type status_list: list[str]
        """
        self._status_list = status_list

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
        if not isinstance(other, AddFullSqlTaskBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
