# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeadLockResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lock_label': 'str',
        'db_id': 'str',
        'db_name': 'str',
        'index_name': 'str',
        'associated_object_id': 'str',
        'object_name': 'str',
        'lock_mode': 'str',
        'owner_list': 'list[DeadLockObject]',
        'waiter_list': 'list[DeadLockObject]'
    }

    attribute_map = {
        'lock_label': 'lock_label',
        'db_id': 'db_id',
        'db_name': 'db_name',
        'index_name': 'index_name',
        'associated_object_id': 'associated_object_id',
        'object_name': 'object_name',
        'lock_mode': 'lock_mode',
        'owner_list': 'owner_list',
        'waiter_list': 'waiter_list'
    }

    def __init__(self, lock_label=None, db_id=None, db_name=None, index_name=None, associated_object_id=None, object_name=None, lock_mode=None, owner_list=None, waiter_list=None):
        r"""DeadLockResource

        The model defined in huaweicloud sdk

        :param lock_label: 死锁标签（keylock、objectlock、ridlock、pagelock、compilelock）
        :type lock_label: str
        :param db_id: 数据库ID
        :type db_id: str
        :param db_name: 数据库名称
        :type db_name: str
        :param index_name: 索引名（仅keylock展示）
        :type index_name: str
        :param associated_object_id: 关联对象ID
        :type associated_object_id: str
        :param object_name: 对象名称，死锁名称
        :type object_name: str
        :param lock_mode: 锁模式
        :type lock_mode: str
        :param owner_list: 持有者列表
        :type owner_list: list[:class:`huaweicloudsdkdas.v3.DeadLockObject`]
        :param waiter_list: 等待者列表
        :type waiter_list: list[:class:`huaweicloudsdkdas.v3.DeadLockObject`]
        """
        
        

        self._lock_label = None
        self._db_id = None
        self._db_name = None
        self._index_name = None
        self._associated_object_id = None
        self._object_name = None
        self._lock_mode = None
        self._owner_list = None
        self._waiter_list = None
        self.discriminator = None

        if lock_label is not None:
            self.lock_label = lock_label
        if db_id is not None:
            self.db_id = db_id
        if db_name is not None:
            self.db_name = db_name
        if index_name is not None:
            self.index_name = index_name
        if associated_object_id is not None:
            self.associated_object_id = associated_object_id
        if object_name is not None:
            self.object_name = object_name
        if lock_mode is not None:
            self.lock_mode = lock_mode
        if owner_list is not None:
            self.owner_list = owner_list
        if waiter_list is not None:
            self.waiter_list = waiter_list

    @property
    def lock_label(self):
        r"""Gets the lock_label of this DeadLockResource.

        死锁标签（keylock、objectlock、ridlock、pagelock、compilelock）

        :return: The lock_label of this DeadLockResource.
        :rtype: str
        """
        return self._lock_label

    @lock_label.setter
    def lock_label(self, lock_label):
        r"""Sets the lock_label of this DeadLockResource.

        死锁标签（keylock、objectlock、ridlock、pagelock、compilelock）

        :param lock_label: The lock_label of this DeadLockResource.
        :type lock_label: str
        """
        self._lock_label = lock_label

    @property
    def db_id(self):
        r"""Gets the db_id of this DeadLockResource.

        数据库ID

        :return: The db_id of this DeadLockResource.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this DeadLockResource.

        数据库ID

        :param db_id: The db_id of this DeadLockResource.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def db_name(self):
        r"""Gets the db_name of this DeadLockResource.

        数据库名称

        :return: The db_name of this DeadLockResource.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this DeadLockResource.

        数据库名称

        :param db_name: The db_name of this DeadLockResource.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def index_name(self):
        r"""Gets the index_name of this DeadLockResource.

        索引名（仅keylock展示）

        :return: The index_name of this DeadLockResource.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        r"""Sets the index_name of this DeadLockResource.

        索引名（仅keylock展示）

        :param index_name: The index_name of this DeadLockResource.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def associated_object_id(self):
        r"""Gets the associated_object_id of this DeadLockResource.

        关联对象ID

        :return: The associated_object_id of this DeadLockResource.
        :rtype: str
        """
        return self._associated_object_id

    @associated_object_id.setter
    def associated_object_id(self, associated_object_id):
        r"""Sets the associated_object_id of this DeadLockResource.

        关联对象ID

        :param associated_object_id: The associated_object_id of this DeadLockResource.
        :type associated_object_id: str
        """
        self._associated_object_id = associated_object_id

    @property
    def object_name(self):
        r"""Gets the object_name of this DeadLockResource.

        对象名称，死锁名称

        :return: The object_name of this DeadLockResource.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this DeadLockResource.

        对象名称，死锁名称

        :param object_name: The object_name of this DeadLockResource.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def lock_mode(self):
        r"""Gets the lock_mode of this DeadLockResource.

        锁模式

        :return: The lock_mode of this DeadLockResource.
        :rtype: str
        """
        return self._lock_mode

    @lock_mode.setter
    def lock_mode(self, lock_mode):
        r"""Sets the lock_mode of this DeadLockResource.

        锁模式

        :param lock_mode: The lock_mode of this DeadLockResource.
        :type lock_mode: str
        """
        self._lock_mode = lock_mode

    @property
    def owner_list(self):
        r"""Gets the owner_list of this DeadLockResource.

        持有者列表

        :return: The owner_list of this DeadLockResource.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DeadLockObject`]
        """
        return self._owner_list

    @owner_list.setter
    def owner_list(self, owner_list):
        r"""Sets the owner_list of this DeadLockResource.

        持有者列表

        :param owner_list: The owner_list of this DeadLockResource.
        :type owner_list: list[:class:`huaweicloudsdkdas.v3.DeadLockObject`]
        """
        self._owner_list = owner_list

    @property
    def waiter_list(self):
        r"""Gets the waiter_list of this DeadLockResource.

        等待者列表

        :return: The waiter_list of this DeadLockResource.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DeadLockObject`]
        """
        return self._waiter_list

    @waiter_list.setter
    def waiter_list(self, waiter_list):
        r"""Sets the waiter_list of this DeadLockResource.

        等待者列表

        :param waiter_list: The waiter_list of this DeadLockResource.
        :type waiter_list: list[:class:`huaweicloudsdkdas.v3.DeadLockObject`]
        """
        self._waiter_list = waiter_list

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
        if not isinstance(other, DeadLockResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
