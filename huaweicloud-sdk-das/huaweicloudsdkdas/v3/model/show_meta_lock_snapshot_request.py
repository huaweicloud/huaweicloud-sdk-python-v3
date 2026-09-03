# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMetaLockSnapshotRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'id': 'int',
        'thread_id': 'str',
        'db_name': 'str',
        'table_name': 'str',
        'lock_status': 'str',
        'lock_type': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'id': 'id',
        'thread_id': 'thread_id',
        'db_name': 'db_name',
        'table_name': 'table_name',
        'lock_status': 'lock_status',
        'lock_type': 'lock_type'
    }

    def __init__(self, connection_id=None, id=None, thread_id=None, db_name=None, table_name=None, lock_status=None, lock_type=None):
        r"""ShowMetaLockSnapshotRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param id: 元数据锁快照ID
        :type id: int
        :param thread_id: 线程ID
        :type thread_id: str
        :param db_name: 数据库名称
        :type db_name: str
        :param table_name: 表名
        :type table_name: str
        :param lock_status: 锁状态
        :type lock_status: str
        :param lock_type: 锁类型
        :type lock_type: str
        """
        
        

        self._connection_id = None
        self._id = None
        self._thread_id = None
        self._db_name = None
        self._table_name = None
        self._lock_status = None
        self._lock_type = None
        self.discriminator = None

        self.connection_id = connection_id
        self.id = id
        if thread_id is not None:
            self.thread_id = thread_id
        if db_name is not None:
            self.db_name = db_name
        if table_name is not None:
            self.table_name = table_name
        if lock_status is not None:
            self.lock_status = lock_status
        if lock_type is not None:
            self.lock_type = lock_type

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ShowMetaLockSnapshotRequest.

        连接ID

        :return: The connection_id of this ShowMetaLockSnapshotRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ShowMetaLockSnapshotRequest.

        连接ID

        :param connection_id: The connection_id of this ShowMetaLockSnapshotRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def id(self):
        r"""Gets the id of this ShowMetaLockSnapshotRequest.

        元数据锁快照ID

        :return: The id of this ShowMetaLockSnapshotRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowMetaLockSnapshotRequest.

        元数据锁快照ID

        :param id: The id of this ShowMetaLockSnapshotRequest.
        :type id: int
        """
        self._id = id

    @property
    def thread_id(self):
        r"""Gets the thread_id of this ShowMetaLockSnapshotRequest.

        线程ID

        :return: The thread_id of this ShowMetaLockSnapshotRequest.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this ShowMetaLockSnapshotRequest.

        线程ID

        :param thread_id: The thread_id of this ShowMetaLockSnapshotRequest.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def db_name(self):
        r"""Gets the db_name of this ShowMetaLockSnapshotRequest.

        数据库名称

        :return: The db_name of this ShowMetaLockSnapshotRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ShowMetaLockSnapshotRequest.

        数据库名称

        :param db_name: The db_name of this ShowMetaLockSnapshotRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ShowMetaLockSnapshotRequest.

        表名

        :return: The table_name of this ShowMetaLockSnapshotRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ShowMetaLockSnapshotRequest.

        表名

        :param table_name: The table_name of this ShowMetaLockSnapshotRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def lock_status(self):
        r"""Gets the lock_status of this ShowMetaLockSnapshotRequest.

        锁状态

        :return: The lock_status of this ShowMetaLockSnapshotRequest.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        r"""Sets the lock_status of this ShowMetaLockSnapshotRequest.

        锁状态

        :param lock_status: The lock_status of this ShowMetaLockSnapshotRequest.
        :type lock_status: str
        """
        self._lock_status = lock_status

    @property
    def lock_type(self):
        r"""Gets the lock_type of this ShowMetaLockSnapshotRequest.

        锁类型

        :return: The lock_type of this ShowMetaLockSnapshotRequest.
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        r"""Sets the lock_type of this ShowMetaLockSnapshotRequest.

        锁类型

        :param lock_type: The lock_type of this ShowMetaLockSnapshotRequest.
        :type lock_type: str
        """
        self._lock_type = lock_type

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
        if not isinstance(other, ShowMetaLockSnapshotRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
