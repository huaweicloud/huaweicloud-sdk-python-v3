# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockTopologyGraphRespLocks:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lock_id': 'str',
        'transaction_id': 'str',
        'index_name': 'str',
        'lock_type': 'str',
        'lock_mode': 'str',
        'lock_status': 'str',
        'space_id': 'int',
        'page_no': 'int',
        'heap_no': 'int',
        'table_name': 'str',
        'primary_key': 'bool',
        'locked_data': 'list[ShowDeadLockTopologyGraphRespLockedData]',
        'unknown': 'bool'
    }

    attribute_map = {
        'lock_id': 'lock_id',
        'transaction_id': 'transaction_id',
        'index_name': 'index_name',
        'lock_type': 'lock_type',
        'lock_mode': 'lock_mode',
        'lock_status': 'lock_status',
        'space_id': 'space_id',
        'page_no': 'page_no',
        'heap_no': 'heap_no',
        'table_name': 'table_name',
        'primary_key': 'primary_key',
        'locked_data': 'locked_data',
        'unknown': 'unknown'
    }

    def __init__(self, lock_id=None, transaction_id=None, index_name=None, lock_type=None, lock_mode=None, lock_status=None, space_id=None, page_no=None, heap_no=None, table_name=None, primary_key=None, locked_data=None, unknown=None):
        r"""ShowDeadLockTopologyGraphRespLocks

        The model defined in huaweicloud sdk

        :param lock_id: 锁节点唯一标识
        :type lock_id: str
        :param transaction_id: 事务节点唯一标识
        :type transaction_id: str
        :param index_name: 索引名字
        :type index_name: str
        :param lock_type: 锁类型
        :type lock_type: str
        :param lock_mode: 锁模式
        :type lock_mode: str
        :param lock_status: 锁状态
        :type lock_status: str
        :param space_id: 表空间ID
        :type space_id: int
        :param page_no: 页号
        :type page_no: int
        :param heap_no: 堆号
        :type heap_no: int
        :param table_name: 操作的表名
        :type table_name: str
        :param primary_key: 是否主键索引
        :type primary_key: bool
        :param locked_data: 锁定的字段数据
        :type locked_data: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespLockedData`]
        :param unknown: 是否未知锁
        :type unknown: bool
        """
        
        

        self._lock_id = None
        self._transaction_id = None
        self._index_name = None
        self._lock_type = None
        self._lock_mode = None
        self._lock_status = None
        self._space_id = None
        self._page_no = None
        self._heap_no = None
        self._table_name = None
        self._primary_key = None
        self._locked_data = None
        self._unknown = None
        self.discriminator = None

        self.lock_id = lock_id
        self.transaction_id = transaction_id
        self.index_name = index_name
        self.lock_type = lock_type
        self.lock_mode = lock_mode
        self.lock_status = lock_status
        self.space_id = space_id
        self.page_no = page_no
        self.heap_no = heap_no
        self.table_name = table_name
        self.primary_key = primary_key
        self.locked_data = locked_data
        self.unknown = unknown

    @property
    def lock_id(self):
        r"""Gets the lock_id of this ShowDeadLockTopologyGraphRespLocks.

        锁节点唯一标识

        :return: The lock_id of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: str
        """
        return self._lock_id

    @lock_id.setter
    def lock_id(self, lock_id):
        r"""Sets the lock_id of this ShowDeadLockTopologyGraphRespLocks.

        锁节点唯一标识

        :param lock_id: The lock_id of this ShowDeadLockTopologyGraphRespLocks.
        :type lock_id: str
        """
        self._lock_id = lock_id

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this ShowDeadLockTopologyGraphRespLocks.

        事务节点唯一标识

        :return: The transaction_id of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this ShowDeadLockTopologyGraphRespLocks.

        事务节点唯一标识

        :param transaction_id: The transaction_id of this ShowDeadLockTopologyGraphRespLocks.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def index_name(self):
        r"""Gets the index_name of this ShowDeadLockTopologyGraphRespLocks.

        索引名字

        :return: The index_name of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        r"""Sets the index_name of this ShowDeadLockTopologyGraphRespLocks.

        索引名字

        :param index_name: The index_name of this ShowDeadLockTopologyGraphRespLocks.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def lock_type(self):
        r"""Gets the lock_type of this ShowDeadLockTopologyGraphRespLocks.

        锁类型

        :return: The lock_type of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        r"""Sets the lock_type of this ShowDeadLockTopologyGraphRespLocks.

        锁类型

        :param lock_type: The lock_type of this ShowDeadLockTopologyGraphRespLocks.
        :type lock_type: str
        """
        self._lock_type = lock_type

    @property
    def lock_mode(self):
        r"""Gets the lock_mode of this ShowDeadLockTopologyGraphRespLocks.

        锁模式

        :return: The lock_mode of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: str
        """
        return self._lock_mode

    @lock_mode.setter
    def lock_mode(self, lock_mode):
        r"""Sets the lock_mode of this ShowDeadLockTopologyGraphRespLocks.

        锁模式

        :param lock_mode: The lock_mode of this ShowDeadLockTopologyGraphRespLocks.
        :type lock_mode: str
        """
        self._lock_mode = lock_mode

    @property
    def lock_status(self):
        r"""Gets the lock_status of this ShowDeadLockTopologyGraphRespLocks.

        锁状态

        :return: The lock_status of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        r"""Sets the lock_status of this ShowDeadLockTopologyGraphRespLocks.

        锁状态

        :param lock_status: The lock_status of this ShowDeadLockTopologyGraphRespLocks.
        :type lock_status: str
        """
        self._lock_status = lock_status

    @property
    def space_id(self):
        r"""Gets the space_id of this ShowDeadLockTopologyGraphRespLocks.

        表空间ID

        :return: The space_id of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: int
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        r"""Sets the space_id of this ShowDeadLockTopologyGraphRespLocks.

        表空间ID

        :param space_id: The space_id of this ShowDeadLockTopologyGraphRespLocks.
        :type space_id: int
        """
        self._space_id = space_id

    @property
    def page_no(self):
        r"""Gets the page_no of this ShowDeadLockTopologyGraphRespLocks.

        页号

        :return: The page_no of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ShowDeadLockTopologyGraphRespLocks.

        页号

        :param page_no: The page_no of this ShowDeadLockTopologyGraphRespLocks.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def heap_no(self):
        r"""Gets the heap_no of this ShowDeadLockTopologyGraphRespLocks.

        堆号

        :return: The heap_no of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: int
        """
        return self._heap_no

    @heap_no.setter
    def heap_no(self, heap_no):
        r"""Sets the heap_no of this ShowDeadLockTopologyGraphRespLocks.

        堆号

        :param heap_no: The heap_no of this ShowDeadLockTopologyGraphRespLocks.
        :type heap_no: int
        """
        self._heap_no = heap_no

    @property
    def table_name(self):
        r"""Gets the table_name of this ShowDeadLockTopologyGraphRespLocks.

        操作的表名

        :return: The table_name of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ShowDeadLockTopologyGraphRespLocks.

        操作的表名

        :param table_name: The table_name of this ShowDeadLockTopologyGraphRespLocks.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def primary_key(self):
        r"""Gets the primary_key of this ShowDeadLockTopologyGraphRespLocks.

        是否主键索引

        :return: The primary_key of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: bool
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        r"""Sets the primary_key of this ShowDeadLockTopologyGraphRespLocks.

        是否主键索引

        :param primary_key: The primary_key of this ShowDeadLockTopologyGraphRespLocks.
        :type primary_key: bool
        """
        self._primary_key = primary_key

    @property
    def locked_data(self):
        r"""Gets the locked_data of this ShowDeadLockTopologyGraphRespLocks.

        锁定的字段数据

        :return: The locked_data of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespLockedData`]
        """
        return self._locked_data

    @locked_data.setter
    def locked_data(self, locked_data):
        r"""Sets the locked_data of this ShowDeadLockTopologyGraphRespLocks.

        锁定的字段数据

        :param locked_data: The locked_data of this ShowDeadLockTopologyGraphRespLocks.
        :type locked_data: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespLockedData`]
        """
        self._locked_data = locked_data

    @property
    def unknown(self):
        r"""Gets the unknown of this ShowDeadLockTopologyGraphRespLocks.

        是否未知锁

        :return: The unknown of this ShowDeadLockTopologyGraphRespLocks.
        :rtype: bool
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        r"""Sets the unknown of this ShowDeadLockTopologyGraphRespLocks.

        是否未知锁

        :param unknown: The unknown of this ShowDeadLockTopologyGraphRespLocks.
        :type unknown: bool
        """
        self._unknown = unknown

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
        if not isinstance(other, ShowDeadLockTopologyGraphRespLocks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
