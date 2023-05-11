# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInnodbLocksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'innodb_trx': 'list[InnodbTrx]',
        'innodb_lock_waits': 'list[InnodbLockWaits]',
        'count': 'int'
    }

    attribute_map = {
        'innodb_trx': 'innodb_trx',
        'innodb_lock_waits': 'innodb_lock_waits',
        'count': 'count'
    }

    def __init__(self, innodb_trx=None, innodb_lock_waits=None, count=None):
        """ListInnodbLocksResponse

        The model defined in huaweicloud sdk

        :param innodb_trx: 当前持有或等待锁的事务信息
        :type innodb_trx: list[:class:`huaweicloudsdkdas.v3.InnodbTrx`]
        :param innodb_lock_waits: 每个事务请求的锁以及阻塞该请求的锁的对应关系
        :type innodb_lock_waits: list[:class:`huaweicloudsdkdas.v3.InnodbLockWaits`]
        :param count: 当前持有或等待锁的事务数量
        :type count: int
        """
        
        super(ListInnodbLocksResponse, self).__init__()

        self._innodb_trx = None
        self._innodb_lock_waits = None
        self._count = None
        self.discriminator = None

        if innodb_trx is not None:
            self.innodb_trx = innodb_trx
        if innodb_lock_waits is not None:
            self.innodb_lock_waits = innodb_lock_waits
        if count is not None:
            self.count = count

    @property
    def innodb_trx(self):
        """Gets the innodb_trx of this ListInnodbLocksResponse.

        当前持有或等待锁的事务信息

        :return: The innodb_trx of this ListInnodbLocksResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InnodbTrx`]
        """
        return self._innodb_trx

    @innodb_trx.setter
    def innodb_trx(self, innodb_trx):
        """Sets the innodb_trx of this ListInnodbLocksResponse.

        当前持有或等待锁的事务信息

        :param innodb_trx: The innodb_trx of this ListInnodbLocksResponse.
        :type innodb_trx: list[:class:`huaweicloudsdkdas.v3.InnodbTrx`]
        """
        self._innodb_trx = innodb_trx

    @property
    def innodb_lock_waits(self):
        """Gets the innodb_lock_waits of this ListInnodbLocksResponse.

        每个事务请求的锁以及阻塞该请求的锁的对应关系

        :return: The innodb_lock_waits of this ListInnodbLocksResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InnodbLockWaits`]
        """
        return self._innodb_lock_waits

    @innodb_lock_waits.setter
    def innodb_lock_waits(self, innodb_lock_waits):
        """Sets the innodb_lock_waits of this ListInnodbLocksResponse.

        每个事务请求的锁以及阻塞该请求的锁的对应关系

        :param innodb_lock_waits: The innodb_lock_waits of this ListInnodbLocksResponse.
        :type innodb_lock_waits: list[:class:`huaweicloudsdkdas.v3.InnodbLockWaits`]
        """
        self._innodb_lock_waits = innodb_lock_waits

    @property
    def count(self):
        """Gets the count of this ListInnodbLocksResponse.

        当前持有或等待锁的事务数量

        :return: The count of this ListInnodbLocksResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListInnodbLocksResponse.

        当前持有或等待锁的事务数量

        :param count: The count of this ListInnodbLocksResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListInnodbLocksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
