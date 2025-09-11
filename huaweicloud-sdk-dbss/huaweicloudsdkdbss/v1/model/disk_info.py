# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_available': 'float',
        'data_total': 'float',
        'data_use_percent': 'int',
        'id': 'str',
        'swap_available': 'float',
        'swap_total': 'float',
        'swap_use_percent': 'int',
        'system_available': 'float',
        'system_total': 'float',
        'system_use_percent': 'int',
        'time': 'str'
    }

    attribute_map = {
        'data_available': 'data_available',
        'data_total': 'data_total',
        'data_use_percent': 'data_use_percent',
        'id': 'id',
        'swap_available': 'swap_available',
        'swap_total': 'swap_total',
        'swap_use_percent': 'swap_use_percent',
        'system_available': 'system_available',
        'system_total': 'system_total',
        'system_use_percent': 'system_use_percent',
        'time': 'time'
    }

    def __init__(self, data_available=None, data_total=None, data_use_percent=None, id=None, swap_available=None, swap_total=None, swap_use_percent=None, system_available=None, system_total=None, system_use_percent=None, time=None):
        r"""DiskInfo

        The model defined in huaweicloud sdk

        :param data_available: 数据盘可用量
        :type data_available: float
        :param data_total: 数据盘总容量
        :type data_total: float
        :param data_use_percent: 数据盘使用百分比
        :type data_use_percent: int
        :param id: 记录ID
        :type id: str
        :param swap_available: 临时目录可用量
        :type swap_available: float
        :param swap_total: 临时目录总容量
        :type swap_total: float
        :param swap_use_percent: 临时目录使用百分比
        :type swap_use_percent: int
        :param system_available: 系统盘可用量
        :type system_available: float
        :param system_total: 系统盘容量
        :type system_total: float
        :param system_use_percent: 系统盘使用百分比
        :type system_use_percent: int
        :param time: 记录时间
        :type time: str
        """
        
        

        self._data_available = None
        self._data_total = None
        self._data_use_percent = None
        self._id = None
        self._swap_available = None
        self._swap_total = None
        self._swap_use_percent = None
        self._system_available = None
        self._system_total = None
        self._system_use_percent = None
        self._time = None
        self.discriminator = None

        if data_available is not None:
            self.data_available = data_available
        if data_total is not None:
            self.data_total = data_total
        if data_use_percent is not None:
            self.data_use_percent = data_use_percent
        if id is not None:
            self.id = id
        if swap_available is not None:
            self.swap_available = swap_available
        if swap_total is not None:
            self.swap_total = swap_total
        if swap_use_percent is not None:
            self.swap_use_percent = swap_use_percent
        if system_available is not None:
            self.system_available = system_available
        if system_total is not None:
            self.system_total = system_total
        if system_use_percent is not None:
            self.system_use_percent = system_use_percent
        if time is not None:
            self.time = time

    @property
    def data_available(self):
        r"""Gets the data_available of this DiskInfo.

        数据盘可用量

        :return: The data_available of this DiskInfo.
        :rtype: float
        """
        return self._data_available

    @data_available.setter
    def data_available(self, data_available):
        r"""Sets the data_available of this DiskInfo.

        数据盘可用量

        :param data_available: The data_available of this DiskInfo.
        :type data_available: float
        """
        self._data_available = data_available

    @property
    def data_total(self):
        r"""Gets the data_total of this DiskInfo.

        数据盘总容量

        :return: The data_total of this DiskInfo.
        :rtype: float
        """
        return self._data_total

    @data_total.setter
    def data_total(self, data_total):
        r"""Sets the data_total of this DiskInfo.

        数据盘总容量

        :param data_total: The data_total of this DiskInfo.
        :type data_total: float
        """
        self._data_total = data_total

    @property
    def data_use_percent(self):
        r"""Gets the data_use_percent of this DiskInfo.

        数据盘使用百分比

        :return: The data_use_percent of this DiskInfo.
        :rtype: int
        """
        return self._data_use_percent

    @data_use_percent.setter
    def data_use_percent(self, data_use_percent):
        r"""Sets the data_use_percent of this DiskInfo.

        数据盘使用百分比

        :param data_use_percent: The data_use_percent of this DiskInfo.
        :type data_use_percent: int
        """
        self._data_use_percent = data_use_percent

    @property
    def id(self):
        r"""Gets the id of this DiskInfo.

        记录ID

        :return: The id of this DiskInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DiskInfo.

        记录ID

        :param id: The id of this DiskInfo.
        :type id: str
        """
        self._id = id

    @property
    def swap_available(self):
        r"""Gets the swap_available of this DiskInfo.

        临时目录可用量

        :return: The swap_available of this DiskInfo.
        :rtype: float
        """
        return self._swap_available

    @swap_available.setter
    def swap_available(self, swap_available):
        r"""Sets the swap_available of this DiskInfo.

        临时目录可用量

        :param swap_available: The swap_available of this DiskInfo.
        :type swap_available: float
        """
        self._swap_available = swap_available

    @property
    def swap_total(self):
        r"""Gets the swap_total of this DiskInfo.

        临时目录总容量

        :return: The swap_total of this DiskInfo.
        :rtype: float
        """
        return self._swap_total

    @swap_total.setter
    def swap_total(self, swap_total):
        r"""Sets the swap_total of this DiskInfo.

        临时目录总容量

        :param swap_total: The swap_total of this DiskInfo.
        :type swap_total: float
        """
        self._swap_total = swap_total

    @property
    def swap_use_percent(self):
        r"""Gets the swap_use_percent of this DiskInfo.

        临时目录使用百分比

        :return: The swap_use_percent of this DiskInfo.
        :rtype: int
        """
        return self._swap_use_percent

    @swap_use_percent.setter
    def swap_use_percent(self, swap_use_percent):
        r"""Sets the swap_use_percent of this DiskInfo.

        临时目录使用百分比

        :param swap_use_percent: The swap_use_percent of this DiskInfo.
        :type swap_use_percent: int
        """
        self._swap_use_percent = swap_use_percent

    @property
    def system_available(self):
        r"""Gets the system_available of this DiskInfo.

        系统盘可用量

        :return: The system_available of this DiskInfo.
        :rtype: float
        """
        return self._system_available

    @system_available.setter
    def system_available(self, system_available):
        r"""Sets the system_available of this DiskInfo.

        系统盘可用量

        :param system_available: The system_available of this DiskInfo.
        :type system_available: float
        """
        self._system_available = system_available

    @property
    def system_total(self):
        r"""Gets the system_total of this DiskInfo.

        系统盘容量

        :return: The system_total of this DiskInfo.
        :rtype: float
        """
        return self._system_total

    @system_total.setter
    def system_total(self, system_total):
        r"""Sets the system_total of this DiskInfo.

        系统盘容量

        :param system_total: The system_total of this DiskInfo.
        :type system_total: float
        """
        self._system_total = system_total

    @property
    def system_use_percent(self):
        r"""Gets the system_use_percent of this DiskInfo.

        系统盘使用百分比

        :return: The system_use_percent of this DiskInfo.
        :rtype: int
        """
        return self._system_use_percent

    @system_use_percent.setter
    def system_use_percent(self, system_use_percent):
        r"""Sets the system_use_percent of this DiskInfo.

        系统盘使用百分比

        :param system_use_percent: The system_use_percent of this DiskInfo.
        :type system_use_percent: int
        """
        self._system_use_percent = system_use_percent

    @property
    def time(self):
        r"""Gets the time of this DiskInfo.

        记录时间

        :return: The time of this DiskInfo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this DiskInfo.

        记录时间

        :param time: The time of this DiskInfo.
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
        if not isinstance(other, DiskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
