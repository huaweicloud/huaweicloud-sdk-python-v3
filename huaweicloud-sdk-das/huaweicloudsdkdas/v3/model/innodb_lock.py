# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InnodbLock:

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
        'lock_trx_id': 'str',
        'lock_mode': 'str',
        'lock_type': 'str',
        'lock_table': 'str',
        'lock_index': 'str',
        'lock_space': 'str',
        'lock_page': 'str',
        'lock_rec': 'str',
        'lock_data': 'str'
    }

    attribute_map = {
        'lock_id': 'lock_id',
        'lock_trx_id': 'lock_trx_id',
        'lock_mode': 'lock_mode',
        'lock_type': 'lock_type',
        'lock_table': 'lock_table',
        'lock_index': 'lock_index',
        'lock_space': 'lock_space',
        'lock_page': 'lock_page',
        'lock_rec': 'lock_rec',
        'lock_data': 'lock_data'
    }

    def __init__(self, lock_id=None, lock_trx_id=None, lock_mode=None, lock_type=None, lock_table=None, lock_index=None, lock_space=None, lock_page=None, lock_rec=None, lock_data=None):
        r"""InnodbLock

        The model defined in huaweicloud sdk

        :param lock_id: 锁ID
        :type lock_id: str
        :param lock_trx_id: 事务ID
        :type lock_trx_id: str
        :param lock_mode: 锁模式，取值为S[,GAP], X[,GAP], IS[,GAP], IX[,GAP], AUTO_INC, and UNKNOWN。
        :type lock_mode: str
        :param lock_type: 锁类型，取值为RECORD或TABLE。RECORD为行锁, TABLE为表锁
        :type lock_type: str
        :param lock_table: 加锁的表
        :type lock_table: str
        :param lock_index: 如果是lock_type&#x3D;&#39;RECORD&#39; 行级锁 ,为锁住的索引，如果是表锁为null
        :type lock_index: str
        :param lock_space: 如果是lock_type&#x3D;&#39;RECORD&#39; 行级锁 ,为锁住的索引，如果是表锁为null
        :type lock_space: str
        :param lock_page: 如果是lock_type&#x3D;&#39;RECORD&#39; 行级锁 ,为锁住的页号，如果是表锁为null
        :type lock_page: str
        :param lock_rec: 如果是lock_type&#x3D;&#39;RECORD&#39; 行级锁 ,为锁住的堆号，如果是表锁为null
        :type lock_rec: str
        :param lock_data: 事务锁住的主键值，若是表锁，则该值为null
        :type lock_data: str
        """
        
        

        self._lock_id = None
        self._lock_trx_id = None
        self._lock_mode = None
        self._lock_type = None
        self._lock_table = None
        self._lock_index = None
        self._lock_space = None
        self._lock_page = None
        self._lock_rec = None
        self._lock_data = None
        self.discriminator = None

        self.lock_id = lock_id
        self.lock_trx_id = lock_trx_id
        self.lock_mode = lock_mode
        self.lock_type = lock_type
        self.lock_table = lock_table
        self.lock_index = lock_index
        self.lock_space = lock_space
        self.lock_page = lock_page
        self.lock_rec = lock_rec
        self.lock_data = lock_data

    @property
    def lock_id(self):
        r"""Gets the lock_id of this InnodbLock.

        锁ID

        :return: The lock_id of this InnodbLock.
        :rtype: str
        """
        return self._lock_id

    @lock_id.setter
    def lock_id(self, lock_id):
        r"""Sets the lock_id of this InnodbLock.

        锁ID

        :param lock_id: The lock_id of this InnodbLock.
        :type lock_id: str
        """
        self._lock_id = lock_id

    @property
    def lock_trx_id(self):
        r"""Gets the lock_trx_id of this InnodbLock.

        事务ID

        :return: The lock_trx_id of this InnodbLock.
        :rtype: str
        """
        return self._lock_trx_id

    @lock_trx_id.setter
    def lock_trx_id(self, lock_trx_id):
        r"""Sets the lock_trx_id of this InnodbLock.

        事务ID

        :param lock_trx_id: The lock_trx_id of this InnodbLock.
        :type lock_trx_id: str
        """
        self._lock_trx_id = lock_trx_id

    @property
    def lock_mode(self):
        r"""Gets the lock_mode of this InnodbLock.

        锁模式，取值为S[,GAP], X[,GAP], IS[,GAP], IX[,GAP], AUTO_INC, and UNKNOWN。

        :return: The lock_mode of this InnodbLock.
        :rtype: str
        """
        return self._lock_mode

    @lock_mode.setter
    def lock_mode(self, lock_mode):
        r"""Sets the lock_mode of this InnodbLock.

        锁模式，取值为S[,GAP], X[,GAP], IS[,GAP], IX[,GAP], AUTO_INC, and UNKNOWN。

        :param lock_mode: The lock_mode of this InnodbLock.
        :type lock_mode: str
        """
        self._lock_mode = lock_mode

    @property
    def lock_type(self):
        r"""Gets the lock_type of this InnodbLock.

        锁类型，取值为RECORD或TABLE。RECORD为行锁, TABLE为表锁

        :return: The lock_type of this InnodbLock.
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        r"""Sets the lock_type of this InnodbLock.

        锁类型，取值为RECORD或TABLE。RECORD为行锁, TABLE为表锁

        :param lock_type: The lock_type of this InnodbLock.
        :type lock_type: str
        """
        self._lock_type = lock_type

    @property
    def lock_table(self):
        r"""Gets the lock_table of this InnodbLock.

        加锁的表

        :return: The lock_table of this InnodbLock.
        :rtype: str
        """
        return self._lock_table

    @lock_table.setter
    def lock_table(self, lock_table):
        r"""Sets the lock_table of this InnodbLock.

        加锁的表

        :param lock_table: The lock_table of this InnodbLock.
        :type lock_table: str
        """
        self._lock_table = lock_table

    @property
    def lock_index(self):
        r"""Gets the lock_index of this InnodbLock.

        如果是lock_type='RECORD' 行级锁 ,为锁住的索引，如果是表锁为null

        :return: The lock_index of this InnodbLock.
        :rtype: str
        """
        return self._lock_index

    @lock_index.setter
    def lock_index(self, lock_index):
        r"""Sets the lock_index of this InnodbLock.

        如果是lock_type='RECORD' 行级锁 ,为锁住的索引，如果是表锁为null

        :param lock_index: The lock_index of this InnodbLock.
        :type lock_index: str
        """
        self._lock_index = lock_index

    @property
    def lock_space(self):
        r"""Gets the lock_space of this InnodbLock.

        如果是lock_type='RECORD' 行级锁 ,为锁住的索引，如果是表锁为null

        :return: The lock_space of this InnodbLock.
        :rtype: str
        """
        return self._lock_space

    @lock_space.setter
    def lock_space(self, lock_space):
        r"""Sets the lock_space of this InnodbLock.

        如果是lock_type='RECORD' 行级锁 ,为锁住的索引，如果是表锁为null

        :param lock_space: The lock_space of this InnodbLock.
        :type lock_space: str
        """
        self._lock_space = lock_space

    @property
    def lock_page(self):
        r"""Gets the lock_page of this InnodbLock.

        如果是lock_type='RECORD' 行级锁 ,为锁住的页号，如果是表锁为null

        :return: The lock_page of this InnodbLock.
        :rtype: str
        """
        return self._lock_page

    @lock_page.setter
    def lock_page(self, lock_page):
        r"""Sets the lock_page of this InnodbLock.

        如果是lock_type='RECORD' 行级锁 ,为锁住的页号，如果是表锁为null

        :param lock_page: The lock_page of this InnodbLock.
        :type lock_page: str
        """
        self._lock_page = lock_page

    @property
    def lock_rec(self):
        r"""Gets the lock_rec of this InnodbLock.

        如果是lock_type='RECORD' 行级锁 ,为锁住的堆号，如果是表锁为null

        :return: The lock_rec of this InnodbLock.
        :rtype: str
        """
        return self._lock_rec

    @lock_rec.setter
    def lock_rec(self, lock_rec):
        r"""Sets the lock_rec of this InnodbLock.

        如果是lock_type='RECORD' 行级锁 ,为锁住的堆号，如果是表锁为null

        :param lock_rec: The lock_rec of this InnodbLock.
        :type lock_rec: str
        """
        self._lock_rec = lock_rec

    @property
    def lock_data(self):
        r"""Gets the lock_data of this InnodbLock.

        事务锁住的主键值，若是表锁，则该值为null

        :return: The lock_data of this InnodbLock.
        :rtype: str
        """
        return self._lock_data

    @lock_data.setter
    def lock_data(self, lock_data):
        r"""Sets the lock_data of this InnodbLock.

        事务锁住的主键值，若是表锁，则该值为null

        :param lock_data: The lock_data of this InnodbLock.
        :type lock_data: str
        """
        self._lock_data = lock_data

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
        if not isinstance(other, InnodbLock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
