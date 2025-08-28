# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WarmPoolInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_capacity': 'int',
        'max_capacity': 'int',
        'instance_init_wait_time': 'int',
        'status': 'str'
    }

    attribute_map = {
        'min_capacity': 'min_capacity',
        'max_capacity': 'max_capacity',
        'instance_init_wait_time': 'instance_init_wait_time',
        'status': 'status'
    }

    def __init__(self, min_capacity=None, max_capacity=None, instance_init_wait_time=None, status=None):
        r"""WarmPoolInfo

        The model defined in huaweicloud sdk

        :param min_capacity: 暖池最小容量
        :type min_capacity: int
        :param max_capacity: 暖池最大容量
        :type max_capacity: int
        :param instance_init_wait_time: 实例初始化等待时间
        :type instance_init_wait_time: int
        :param status: 暖池状态
        :type status: str
        """
        
        

        self._min_capacity = None
        self._max_capacity = None
        self._instance_init_wait_time = None
        self._status = None
        self.discriminator = None

        if min_capacity is not None:
            self.min_capacity = min_capacity
        if max_capacity is not None:
            self.max_capacity = max_capacity
        if instance_init_wait_time is not None:
            self.instance_init_wait_time = instance_init_wait_time
        if status is not None:
            self.status = status

    @property
    def min_capacity(self):
        r"""Gets the min_capacity of this WarmPoolInfo.

        暖池最小容量

        :return: The min_capacity of this WarmPoolInfo.
        :rtype: int
        """
        return self._min_capacity

    @min_capacity.setter
    def min_capacity(self, min_capacity):
        r"""Sets the min_capacity of this WarmPoolInfo.

        暖池最小容量

        :param min_capacity: The min_capacity of this WarmPoolInfo.
        :type min_capacity: int
        """
        self._min_capacity = min_capacity

    @property
    def max_capacity(self):
        r"""Gets the max_capacity of this WarmPoolInfo.

        暖池最大容量

        :return: The max_capacity of this WarmPoolInfo.
        :rtype: int
        """
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        r"""Sets the max_capacity of this WarmPoolInfo.

        暖池最大容量

        :param max_capacity: The max_capacity of this WarmPoolInfo.
        :type max_capacity: int
        """
        self._max_capacity = max_capacity

    @property
    def instance_init_wait_time(self):
        r"""Gets the instance_init_wait_time of this WarmPoolInfo.

        实例初始化等待时间

        :return: The instance_init_wait_time of this WarmPoolInfo.
        :rtype: int
        """
        return self._instance_init_wait_time

    @instance_init_wait_time.setter
    def instance_init_wait_time(self, instance_init_wait_time):
        r"""Sets the instance_init_wait_time of this WarmPoolInfo.

        实例初始化等待时间

        :param instance_init_wait_time: The instance_init_wait_time of this WarmPoolInfo.
        :type instance_init_wait_time: int
        """
        self._instance_init_wait_time = instance_init_wait_time

    @property
    def status(self):
        r"""Gets the status of this WarmPoolInfo.

        暖池状态

        :return: The status of this WarmPoolInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WarmPoolInfo.

        暖池状态

        :param status: The status of this WarmPoolInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, WarmPoolInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
