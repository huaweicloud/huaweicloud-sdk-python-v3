# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkspaceLockResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_lock': 'int',
        'lock_time': 'str',
        'lock_reason': 'str'
    }

    attribute_map = {
        'is_lock': 'is_lock',
        'lock_time': 'lock_time',
        'lock_reason': 'lock_reason'
    }

    def __init__(self, is_lock=None, lock_time=None, lock_reason=None):
        """ShowWorkspaceLockResponse

        The model defined in huaweicloud sdk

        :param is_lock: 云办公服务是否被锁定，0代表未锁定，1代表锁定。
        :type is_lock: int
        :param lock_time: 云办公服务锁定时间，格式：yyyy-MM-dd HH:mm:ss，时区：UTC。
        :type lock_time: str
        :param lock_reason: 云办公服务锁定原因。
        :type lock_reason: str
        """
        
        super(ShowWorkspaceLockResponse, self).__init__()

        self._is_lock = None
        self._lock_time = None
        self._lock_reason = None
        self.discriminator = None

        if is_lock is not None:
            self.is_lock = is_lock
        if lock_time is not None:
            self.lock_time = lock_time
        if lock_reason is not None:
            self.lock_reason = lock_reason

    @property
    def is_lock(self):
        """Gets the is_lock of this ShowWorkspaceLockResponse.

        云办公服务是否被锁定，0代表未锁定，1代表锁定。

        :return: The is_lock of this ShowWorkspaceLockResponse.
        :rtype: int
        """
        return self._is_lock

    @is_lock.setter
    def is_lock(self, is_lock):
        """Sets the is_lock of this ShowWorkspaceLockResponse.

        云办公服务是否被锁定，0代表未锁定，1代表锁定。

        :param is_lock: The is_lock of this ShowWorkspaceLockResponse.
        :type is_lock: int
        """
        self._is_lock = is_lock

    @property
    def lock_time(self):
        """Gets the lock_time of this ShowWorkspaceLockResponse.

        云办公服务锁定时间，格式：yyyy-MM-dd HH:mm:ss，时区：UTC。

        :return: The lock_time of this ShowWorkspaceLockResponse.
        :rtype: str
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this ShowWorkspaceLockResponse.

        云办公服务锁定时间，格式：yyyy-MM-dd HH:mm:ss，时区：UTC。

        :param lock_time: The lock_time of this ShowWorkspaceLockResponse.
        :type lock_time: str
        """
        self._lock_time = lock_time

    @property
    def lock_reason(self):
        """Gets the lock_reason of this ShowWorkspaceLockResponse.

        云办公服务锁定原因。

        :return: The lock_reason of this ShowWorkspaceLockResponse.
        :rtype: str
        """
        return self._lock_reason

    @lock_reason.setter
    def lock_reason(self, lock_reason):
        """Sets the lock_reason of this ShowWorkspaceLockResponse.

        云办公服务锁定原因。

        :param lock_reason: The lock_reason of this ShowWorkspaceLockResponse.
        :type lock_reason: str
        """
        self._lock_reason = lock_reason

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
        if not isinstance(other, ShowWorkspaceLockResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
