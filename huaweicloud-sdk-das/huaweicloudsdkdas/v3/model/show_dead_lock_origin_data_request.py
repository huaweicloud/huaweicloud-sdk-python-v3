# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockOriginDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'dead_lock_id': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'dead_lock_id': 'dead_lock_id',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, instance_id=None, dead_lock_id=None, start_time=None, end_time=None):
        r"""ShowDeadLockOriginDataRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param dead_lock_id: 死锁ID
        :type dead_lock_id: str
        :param start_time: 开始时间戳 ms
        :type start_time: int
        :param end_time: 结束时间戳 ms
        :type end_time: int
        """
        
        

        self._instance_id = None
        self._dead_lock_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.instance_id = instance_id
        self.dead_lock_id = dead_lock_id
        self.start_time = start_time
        self.end_time = end_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowDeadLockOriginDataRequest.

        实例ID

        :return: The instance_id of this ShowDeadLockOriginDataRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowDeadLockOriginDataRequest.

        实例ID

        :param instance_id: The instance_id of this ShowDeadLockOriginDataRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def dead_lock_id(self):
        r"""Gets the dead_lock_id of this ShowDeadLockOriginDataRequest.

        死锁ID

        :return: The dead_lock_id of this ShowDeadLockOriginDataRequest.
        :rtype: str
        """
        return self._dead_lock_id

    @dead_lock_id.setter
    def dead_lock_id(self, dead_lock_id):
        r"""Sets the dead_lock_id of this ShowDeadLockOriginDataRequest.

        死锁ID

        :param dead_lock_id: The dead_lock_id of this ShowDeadLockOriginDataRequest.
        :type dead_lock_id: str
        """
        self._dead_lock_id = dead_lock_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowDeadLockOriginDataRequest.

        开始时间戳 ms

        :return: The start_time of this ShowDeadLockOriginDataRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowDeadLockOriginDataRequest.

        开始时间戳 ms

        :param start_time: The start_time of this ShowDeadLockOriginDataRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowDeadLockOriginDataRequest.

        结束时间戳 ms

        :return: The end_time of this ShowDeadLockOriginDataRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowDeadLockOriginDataRequest.

        结束时间戳 ms

        :param end_time: The end_time of this ShowDeadLockOriginDataRequest.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowDeadLockOriginDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
