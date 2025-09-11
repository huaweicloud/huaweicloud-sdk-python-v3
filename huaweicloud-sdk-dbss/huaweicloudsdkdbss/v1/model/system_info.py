# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SystemInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_use': 'float',
        'id': 'str',
        'mem_use': 'float',
        'time': 'str'
    }

    attribute_map = {
        'cpu_use': 'cpu_use',
        'id': 'id',
        'mem_use': 'mem_use',
        'time': 'time'
    }

    def __init__(self, cpu_use=None, id=None, mem_use=None, time=None):
        r"""SystemInfo

        The model defined in huaweicloud sdk

        :param cpu_use: CPU使用量
        :type cpu_use: float
        :param id: 记录ID
        :type id: str
        :param mem_use: 内存使用量
        :type mem_use: float
        :param time: 记录时间
        :type time: str
        """
        
        

        self._cpu_use = None
        self._id = None
        self._mem_use = None
        self._time = None
        self.discriminator = None

        if cpu_use is not None:
            self.cpu_use = cpu_use
        if id is not None:
            self.id = id
        if mem_use is not None:
            self.mem_use = mem_use
        if time is not None:
            self.time = time

    @property
    def cpu_use(self):
        r"""Gets the cpu_use of this SystemInfo.

        CPU使用量

        :return: The cpu_use of this SystemInfo.
        :rtype: float
        """
        return self._cpu_use

    @cpu_use.setter
    def cpu_use(self, cpu_use):
        r"""Sets the cpu_use of this SystemInfo.

        CPU使用量

        :param cpu_use: The cpu_use of this SystemInfo.
        :type cpu_use: float
        """
        self._cpu_use = cpu_use

    @property
    def id(self):
        r"""Gets the id of this SystemInfo.

        记录ID

        :return: The id of this SystemInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SystemInfo.

        记录ID

        :param id: The id of this SystemInfo.
        :type id: str
        """
        self._id = id

    @property
    def mem_use(self):
        r"""Gets the mem_use of this SystemInfo.

        内存使用量

        :return: The mem_use of this SystemInfo.
        :rtype: float
        """
        return self._mem_use

    @mem_use.setter
    def mem_use(self, mem_use):
        r"""Sets the mem_use of this SystemInfo.

        内存使用量

        :param mem_use: The mem_use of this SystemInfo.
        :type mem_use: float
        """
        self._mem_use = mem_use

    @property
    def time(self):
        r"""Gets the time of this SystemInfo.

        记录时间

        :return: The time of this SystemInfo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this SystemInfo.

        记录时间

        :param time: The time of this SystemInfo.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, SystemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
