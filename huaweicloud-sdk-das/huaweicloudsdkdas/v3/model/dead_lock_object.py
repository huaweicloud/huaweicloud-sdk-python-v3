# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeadLockObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_id': 'str',
        'spid': 'str',
        'lock_mode': 'str'
    }

    attribute_map = {
        'process_id': 'process_id',
        'spid': 'spid',
        'lock_mode': 'lock_mode'
    }

    def __init__(self, process_id=None, spid=None, lock_mode=None):
        r"""DeadLockObject

        The model defined in huaweicloud sdk

        :param process_id: 会话ID
        :type process_id: str
        :param spid: 服务进程ID
        :type spid: str
        :param lock_mode: 锁模式
        :type lock_mode: str
        """
        
        

        self._process_id = None
        self._spid = None
        self._lock_mode = None
        self.discriminator = None

        if process_id is not None:
            self.process_id = process_id
        if spid is not None:
            self.spid = spid
        if lock_mode is not None:
            self.lock_mode = lock_mode

    @property
    def process_id(self):
        r"""Gets the process_id of this DeadLockObject.

        会话ID

        :return: The process_id of this DeadLockObject.
        :rtype: str
        """
        return self._process_id

    @process_id.setter
    def process_id(self, process_id):
        r"""Sets the process_id of this DeadLockObject.

        会话ID

        :param process_id: The process_id of this DeadLockObject.
        :type process_id: str
        """
        self._process_id = process_id

    @property
    def spid(self):
        r"""Gets the spid of this DeadLockObject.

        服务进程ID

        :return: The spid of this DeadLockObject.
        :rtype: str
        """
        return self._spid

    @spid.setter
    def spid(self, spid):
        r"""Sets the spid of this DeadLockObject.

        服务进程ID

        :param spid: The spid of this DeadLockObject.
        :type spid: str
        """
        self._spid = spid

    @property
    def lock_mode(self):
        r"""Gets the lock_mode of this DeadLockObject.

        锁模式

        :return: The lock_mode of this DeadLockObject.
        :rtype: str
        """
        return self._lock_mode

    @lock_mode.setter
    def lock_mode(self, lock_mode):
        r"""Sets the lock_mode of this DeadLockObject.

        锁模式

        :param lock_mode: The lock_mode of this DeadLockObject.
        :type lock_mode: str
        """
        self._lock_mode = lock_mode

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
        if not isinstance(other, DeadLockObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
