# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLatestDeadLockSnapshot4ApiResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'find_lock': 'bool',
        'happen_time': 'int',
        'mysql_dead_lock': 'MySQLDeadLock'
    }

    attribute_map = {
        'find_lock': 'find_lock',
        'happen_time': 'happen_time',
        'mysql_dead_lock': 'mysql_dead_lock'
    }

    def __init__(self, find_lock=None, happen_time=None, mysql_dead_lock=None):
        r"""ShowLatestDeadLockSnapshot4ApiResponse

        The model defined in huaweicloud sdk

        :param find_lock: 是否找到有锁
        :type find_lock: bool
        :param happen_time: 发生时间（ms）
        :type happen_time: int
        :param mysql_dead_lock: 
        :type mysql_dead_lock: :class:`huaweicloudsdkdas.v3.MySQLDeadLock`
        """
        
        super().__init__()

        self._find_lock = None
        self._happen_time = None
        self._mysql_dead_lock = None
        self.discriminator = None

        if find_lock is not None:
            self.find_lock = find_lock
        if happen_time is not None:
            self.happen_time = happen_time
        if mysql_dead_lock is not None:
            self.mysql_dead_lock = mysql_dead_lock

    @property
    def find_lock(self):
        r"""Gets the find_lock of this ShowLatestDeadLockSnapshot4ApiResponse.

        是否找到有锁

        :return: The find_lock of this ShowLatestDeadLockSnapshot4ApiResponse.
        :rtype: bool
        """
        return self._find_lock

    @find_lock.setter
    def find_lock(self, find_lock):
        r"""Sets the find_lock of this ShowLatestDeadLockSnapshot4ApiResponse.

        是否找到有锁

        :param find_lock: The find_lock of this ShowLatestDeadLockSnapshot4ApiResponse.
        :type find_lock: bool
        """
        self._find_lock = find_lock

    @property
    def happen_time(self):
        r"""Gets the happen_time of this ShowLatestDeadLockSnapshot4ApiResponse.

        发生时间（ms）

        :return: The happen_time of this ShowLatestDeadLockSnapshot4ApiResponse.
        :rtype: int
        """
        return self._happen_time

    @happen_time.setter
    def happen_time(self, happen_time):
        r"""Sets the happen_time of this ShowLatestDeadLockSnapshot4ApiResponse.

        发生时间（ms）

        :param happen_time: The happen_time of this ShowLatestDeadLockSnapshot4ApiResponse.
        :type happen_time: int
        """
        self._happen_time = happen_time

    @property
    def mysql_dead_lock(self):
        r"""Gets the mysql_dead_lock of this ShowLatestDeadLockSnapshot4ApiResponse.

        :return: The mysql_dead_lock of this ShowLatestDeadLockSnapshot4ApiResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.MySQLDeadLock`
        """
        return self._mysql_dead_lock

    @mysql_dead_lock.setter
    def mysql_dead_lock(self, mysql_dead_lock):
        r"""Sets the mysql_dead_lock of this ShowLatestDeadLockSnapshot4ApiResponse.

        :param mysql_dead_lock: The mysql_dead_lock of this ShowLatestDeadLockSnapshot4ApiResponse.
        :type mysql_dead_lock: :class:`huaweicloudsdkdas.v3.MySQLDeadLock`
        """
        self._mysql_dead_lock = mysql_dead_lock

    def to_dict(self):
        import warnings
        warnings.warn("ShowLatestDeadLockSnapshot4ApiResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowLatestDeadLockSnapshot4ApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
