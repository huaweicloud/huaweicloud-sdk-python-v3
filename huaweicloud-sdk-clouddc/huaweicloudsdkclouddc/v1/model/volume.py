# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Volume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'volume_raid_level': 'str',
        'capacity_bytes': 'int',
        'optimum_io_size_bytes': 'int',
        'current_read_policy': 'str',
        'default_read_policy': 'str',
        'current_write_policy': 'str',
        'default_write_policy': 'str',
        'access_policy': 'str',
        'current_io_policy': 'str',
        'default_io_policy': 'str',
        'drives': 'list[Drive]',
        'status': 'Status'
    }

    attribute_map = {
        'name': 'name',
        'volume_raid_level': 'volume_raid_level',
        'capacity_bytes': 'capacity_bytes',
        'optimum_io_size_bytes': 'optimum_io_size_bytes',
        'current_read_policy': 'current_read_policy',
        'default_read_policy': 'default_read_policy',
        'current_write_policy': 'current_write_policy',
        'default_write_policy': 'default_write_policy',
        'access_policy': 'access_policy',
        'current_io_policy': 'current_io_policy',
        'default_io_policy': 'default_io_policy',
        'drives': 'drives',
        'status': 'status'
    }

    def __init__(self, name=None, volume_raid_level=None, capacity_bytes=None, optimum_io_size_bytes=None, current_read_policy=None, default_read_policy=None, current_write_policy=None, default_write_policy=None, access_policy=None, current_io_policy=None, default_io_policy=None, drives=None, status=None):
        r"""Volume

        The model defined in huaweicloud sdk

        :param name: 逻辑盘名称
        :type name: str
        :param volume_raid_level: RAID级别
        :type volume_raid_level: str
        :param capacity_bytes: 容量（单位：byte）
        :type capacity_bytes: int
        :param optimum_io_size_bytes: 逻辑盘的条带大小（单位：byte）
        :type optimum_io_size_bytes: int
        :param current_read_policy: 当前的读策略
        :type current_read_policy: str
        :param default_read_policy: 默认的读策略
        :type default_read_policy: str
        :param current_write_policy: 当前的写策略
        :type current_write_policy: str
        :param default_write_policy: 默认的写策略
        :type default_write_policy: str
        :param access_policy: 访问策略
        :type access_policy: str
        :param current_io_policy: 当前IO策略
        :type current_io_policy: str
        :param default_io_policy: 当前IO策略
        :type default_io_policy: str
        :param drives: 存储物理盘详细信息
        :type drives: list[:class:`huaweicloudsdkclouddc.v1.Drive`]
        :param status: 
        :type status: :class:`huaweicloudsdkclouddc.v1.Status`
        """
        
        

        self._name = None
        self._volume_raid_level = None
        self._capacity_bytes = None
        self._optimum_io_size_bytes = None
        self._current_read_policy = None
        self._default_read_policy = None
        self._current_write_policy = None
        self._default_write_policy = None
        self._access_policy = None
        self._current_io_policy = None
        self._default_io_policy = None
        self._drives = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if volume_raid_level is not None:
            self.volume_raid_level = volume_raid_level
        if capacity_bytes is not None:
            self.capacity_bytes = capacity_bytes
        if optimum_io_size_bytes is not None:
            self.optimum_io_size_bytes = optimum_io_size_bytes
        if current_read_policy is not None:
            self.current_read_policy = current_read_policy
        if default_read_policy is not None:
            self.default_read_policy = default_read_policy
        if current_write_policy is not None:
            self.current_write_policy = current_write_policy
        if default_write_policy is not None:
            self.default_write_policy = default_write_policy
        if access_policy is not None:
            self.access_policy = access_policy
        if current_io_policy is not None:
            self.current_io_policy = current_io_policy
        if default_io_policy is not None:
            self.default_io_policy = default_io_policy
        if drives is not None:
            self.drives = drives
        if status is not None:
            self.status = status

    @property
    def name(self):
        r"""Gets the name of this Volume.

        逻辑盘名称

        :return: The name of this Volume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Volume.

        逻辑盘名称

        :param name: The name of this Volume.
        :type name: str
        """
        self._name = name

    @property
    def volume_raid_level(self):
        r"""Gets the volume_raid_level of this Volume.

        RAID级别

        :return: The volume_raid_level of this Volume.
        :rtype: str
        """
        return self._volume_raid_level

    @volume_raid_level.setter
    def volume_raid_level(self, volume_raid_level):
        r"""Sets the volume_raid_level of this Volume.

        RAID级别

        :param volume_raid_level: The volume_raid_level of this Volume.
        :type volume_raid_level: str
        """
        self._volume_raid_level = volume_raid_level

    @property
    def capacity_bytes(self):
        r"""Gets the capacity_bytes of this Volume.

        容量（单位：byte）

        :return: The capacity_bytes of this Volume.
        :rtype: int
        """
        return self._capacity_bytes

    @capacity_bytes.setter
    def capacity_bytes(self, capacity_bytes):
        r"""Sets the capacity_bytes of this Volume.

        容量（单位：byte）

        :param capacity_bytes: The capacity_bytes of this Volume.
        :type capacity_bytes: int
        """
        self._capacity_bytes = capacity_bytes

    @property
    def optimum_io_size_bytes(self):
        r"""Gets the optimum_io_size_bytes of this Volume.

        逻辑盘的条带大小（单位：byte）

        :return: The optimum_io_size_bytes of this Volume.
        :rtype: int
        """
        return self._optimum_io_size_bytes

    @optimum_io_size_bytes.setter
    def optimum_io_size_bytes(self, optimum_io_size_bytes):
        r"""Sets the optimum_io_size_bytes of this Volume.

        逻辑盘的条带大小（单位：byte）

        :param optimum_io_size_bytes: The optimum_io_size_bytes of this Volume.
        :type optimum_io_size_bytes: int
        """
        self._optimum_io_size_bytes = optimum_io_size_bytes

    @property
    def current_read_policy(self):
        r"""Gets the current_read_policy of this Volume.

        当前的读策略

        :return: The current_read_policy of this Volume.
        :rtype: str
        """
        return self._current_read_policy

    @current_read_policy.setter
    def current_read_policy(self, current_read_policy):
        r"""Sets the current_read_policy of this Volume.

        当前的读策略

        :param current_read_policy: The current_read_policy of this Volume.
        :type current_read_policy: str
        """
        self._current_read_policy = current_read_policy

    @property
    def default_read_policy(self):
        r"""Gets the default_read_policy of this Volume.

        默认的读策略

        :return: The default_read_policy of this Volume.
        :rtype: str
        """
        return self._default_read_policy

    @default_read_policy.setter
    def default_read_policy(self, default_read_policy):
        r"""Sets the default_read_policy of this Volume.

        默认的读策略

        :param default_read_policy: The default_read_policy of this Volume.
        :type default_read_policy: str
        """
        self._default_read_policy = default_read_policy

    @property
    def current_write_policy(self):
        r"""Gets the current_write_policy of this Volume.

        当前的写策略

        :return: The current_write_policy of this Volume.
        :rtype: str
        """
        return self._current_write_policy

    @current_write_policy.setter
    def current_write_policy(self, current_write_policy):
        r"""Sets the current_write_policy of this Volume.

        当前的写策略

        :param current_write_policy: The current_write_policy of this Volume.
        :type current_write_policy: str
        """
        self._current_write_policy = current_write_policy

    @property
    def default_write_policy(self):
        r"""Gets the default_write_policy of this Volume.

        默认的写策略

        :return: The default_write_policy of this Volume.
        :rtype: str
        """
        return self._default_write_policy

    @default_write_policy.setter
    def default_write_policy(self, default_write_policy):
        r"""Sets the default_write_policy of this Volume.

        默认的写策略

        :param default_write_policy: The default_write_policy of this Volume.
        :type default_write_policy: str
        """
        self._default_write_policy = default_write_policy

    @property
    def access_policy(self):
        r"""Gets the access_policy of this Volume.

        访问策略

        :return: The access_policy of this Volume.
        :rtype: str
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        r"""Sets the access_policy of this Volume.

        访问策略

        :param access_policy: The access_policy of this Volume.
        :type access_policy: str
        """
        self._access_policy = access_policy

    @property
    def current_io_policy(self):
        r"""Gets the current_io_policy of this Volume.

        当前IO策略

        :return: The current_io_policy of this Volume.
        :rtype: str
        """
        return self._current_io_policy

    @current_io_policy.setter
    def current_io_policy(self, current_io_policy):
        r"""Sets the current_io_policy of this Volume.

        当前IO策略

        :param current_io_policy: The current_io_policy of this Volume.
        :type current_io_policy: str
        """
        self._current_io_policy = current_io_policy

    @property
    def default_io_policy(self):
        r"""Gets the default_io_policy of this Volume.

        当前IO策略

        :return: The default_io_policy of this Volume.
        :rtype: str
        """
        return self._default_io_policy

    @default_io_policy.setter
    def default_io_policy(self, default_io_policy):
        r"""Sets the default_io_policy of this Volume.

        当前IO策略

        :param default_io_policy: The default_io_policy of this Volume.
        :type default_io_policy: str
        """
        self._default_io_policy = default_io_policy

    @property
    def drives(self):
        r"""Gets the drives of this Volume.

        存储物理盘详细信息

        :return: The drives of this Volume.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.Drive`]
        """
        return self._drives

    @drives.setter
    def drives(self, drives):
        r"""Sets the drives of this Volume.

        存储物理盘详细信息

        :param drives: The drives of this Volume.
        :type drives: list[:class:`huaweicloudsdkclouddc.v1.Drive`]
        """
        self._drives = drives

    @property
    def status(self):
        r"""Gets the status of this Volume.

        :return: The status of this Volume.
        :rtype: :class:`huaweicloudsdkclouddc.v1.Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Volume.

        :param status: The status of this Volume.
        :type status: :class:`huaweicloudsdkclouddc.v1.Status`
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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
