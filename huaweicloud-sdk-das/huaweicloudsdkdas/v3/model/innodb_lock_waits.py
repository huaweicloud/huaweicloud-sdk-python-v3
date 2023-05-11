# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InnodbLockWaits:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'requesting_trx_id': 'str',
        'requested_lock_id': 'str',
        'blocking_trx_id': 'str',
        'blocking_lock_id': 'str'
    }

    attribute_map = {
        'requesting_trx_id': 'requesting_trx_id',
        'requested_lock_id': 'requested_lock_id',
        'blocking_trx_id': 'blocking_trx_id',
        'blocking_lock_id': 'blocking_lock_id'
    }

    def __init__(self, requesting_trx_id=None, requested_lock_id=None, blocking_trx_id=None, blocking_lock_id=None):
        """InnodbLockWaits

        The model defined in huaweicloud sdk

        :param requesting_trx_id: 申请锁资源的事务ID
        :type requesting_trx_id: str
        :param requested_lock_id: 申请的锁的ID
        :type requested_lock_id: str
        :param blocking_trx_id: 阻塞的事务ID
        :type blocking_trx_id: str
        :param blocking_lock_id: 阻塞的锁的ID
        :type blocking_lock_id: str
        """
        
        

        self._requesting_trx_id = None
        self._requested_lock_id = None
        self._blocking_trx_id = None
        self._blocking_lock_id = None
        self.discriminator = None

        self.requesting_trx_id = requesting_trx_id
        self.requested_lock_id = requested_lock_id
        self.blocking_trx_id = blocking_trx_id
        self.blocking_lock_id = blocking_lock_id

    @property
    def requesting_trx_id(self):
        """Gets the requesting_trx_id of this InnodbLockWaits.

        申请锁资源的事务ID

        :return: The requesting_trx_id of this InnodbLockWaits.
        :rtype: str
        """
        return self._requesting_trx_id

    @requesting_trx_id.setter
    def requesting_trx_id(self, requesting_trx_id):
        """Sets the requesting_trx_id of this InnodbLockWaits.

        申请锁资源的事务ID

        :param requesting_trx_id: The requesting_trx_id of this InnodbLockWaits.
        :type requesting_trx_id: str
        """
        self._requesting_trx_id = requesting_trx_id

    @property
    def requested_lock_id(self):
        """Gets the requested_lock_id of this InnodbLockWaits.

        申请的锁的ID

        :return: The requested_lock_id of this InnodbLockWaits.
        :rtype: str
        """
        return self._requested_lock_id

    @requested_lock_id.setter
    def requested_lock_id(self, requested_lock_id):
        """Sets the requested_lock_id of this InnodbLockWaits.

        申请的锁的ID

        :param requested_lock_id: The requested_lock_id of this InnodbLockWaits.
        :type requested_lock_id: str
        """
        self._requested_lock_id = requested_lock_id

    @property
    def blocking_trx_id(self):
        """Gets the blocking_trx_id of this InnodbLockWaits.

        阻塞的事务ID

        :return: The blocking_trx_id of this InnodbLockWaits.
        :rtype: str
        """
        return self._blocking_trx_id

    @blocking_trx_id.setter
    def blocking_trx_id(self, blocking_trx_id):
        """Sets the blocking_trx_id of this InnodbLockWaits.

        阻塞的事务ID

        :param blocking_trx_id: The blocking_trx_id of this InnodbLockWaits.
        :type blocking_trx_id: str
        """
        self._blocking_trx_id = blocking_trx_id

    @property
    def blocking_lock_id(self):
        """Gets the blocking_lock_id of this InnodbLockWaits.

        阻塞的锁的ID

        :return: The blocking_lock_id of this InnodbLockWaits.
        :rtype: str
        """
        return self._blocking_lock_id

    @blocking_lock_id.setter
    def blocking_lock_id(self, blocking_lock_id):
        """Sets the blocking_lock_id of this InnodbLockWaits.

        阻塞的锁的ID

        :param blocking_lock_id: The blocking_lock_id of this InnodbLockWaits.
        :type blocking_lock_id: str
        """
        self._blocking_lock_id = blocking_lock_id

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
        if not isinstance(other, InnodbLockWaits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
