# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'instance_id': 'str',
        'host_name': 'str',
        'disk_name': 'str',
        'disk_type': 'str',
        'total': 'float',
        'used': 'float',
        'available': 'float',
        'used_percentage': 'float',
        '_await': 'float',
        'svctm': 'float',
        'util': 'float',
        'read_rate': 'float',
        'write_rate': 'float'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'host_name': 'host_name',
        'disk_name': 'disk_name',
        'disk_type': 'disk_type',
        'total': 'total',
        'used': 'used',
        'available': 'available',
        'used_percentage': 'used_percentage',
        '_await': 'await',
        'svctm': 'svctm',
        'util': 'util',
        'read_rate': 'read_rate',
        'write_rate': 'write_rate'
    }

    def __init__(self, instance_name=None, instance_id=None, host_name=None, disk_name=None, disk_type=None, total=None, used=None, available=None, used_percentage=None, _await=None, svctm=None, util=None, read_rate=None, write_rate=None):
        r"""DiskResp

        The model defined in huaweicloud sdk

        :param instance_name: **参数解释**： 实例名称。 **取值范围**： 不涉及。
        :type instance_name: str
        :param instance_id: **参数解释**： 实例ID。 **取值范围**： 不涉及。
        :type instance_id: str
        :param host_name: **参数解释**： 主机名称。 **取值范围**： 不涉及。
        :type host_name: str
        :param disk_name: **参数解释**： 磁盘名称。 **取值范围**： 不涉及。
        :type disk_name: str
        :param disk_type: **参数解释**： 磁盘类型(系统盘、数据盘、日志盘)。 **取值范围**： 不涉及。
        :type disk_type: str
        :param total: **参数解释**： 磁盘总容量(GB)。 **取值范围**： 不涉及。
        :type total: float
        :param used: **参数解释**： 磁盘已使用容量(GB)。 **取值范围**： 不涉及。
        :type used: float
        :param available: **参数解释**： 磁盘可用容量(GB)。 **取值范围**： 不涉及。
        :type available: float
        :param used_percentage: **参数解释**： 磁盘使用率(%)。 **取值范围**： 不涉及。
        :type used_percentage: float
        :param _await: **参数解释**： IO等待时间(ms)。 **取值范围**： 不涉及。
        :type _await: float
        :param svctm: **参数解释**： IO服务时间(ms)。 **取值范围**： 不涉及。
        :type svctm: float
        :param util: **参数解释**： IO使用率(%)。 **取值范围**： 不涉及。
        :type util: float
        :param read_rate: **参数解释**： 磁盘读速率(KB/s)。 **取值范围**： 不涉及。
        :type read_rate: float
        :param write_rate: **参数解释**： 磁盘写速率(KB/s)。 **取值范围**： 不涉及。
        :type write_rate: float
        """
        
        

        self._instance_name = None
        self._instance_id = None
        self._host_name = None
        self._disk_name = None
        self._disk_type = None
        self._total = None
        self._used = None
        self._available = None
        self._used_percentage = None
        self.__await = None
        self._svctm = None
        self._util = None
        self._read_rate = None
        self._write_rate = None
        self.discriminator = None

        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if host_name is not None:
            self.host_name = host_name
        if disk_name is not None:
            self.disk_name = disk_name
        if disk_type is not None:
            self.disk_type = disk_type
        if total is not None:
            self.total = total
        if used is not None:
            self.used = used
        if available is not None:
            self.available = available
        if used_percentage is not None:
            self.used_percentage = used_percentage
        if _await is not None:
            self._await = _await
        if svctm is not None:
            self.svctm = svctm
        if util is not None:
            self.util = util
        if read_rate is not None:
            self.read_rate = read_rate
        if write_rate is not None:
            self.write_rate = write_rate

    @property
    def instance_name(self):
        r"""Gets the instance_name of this DiskResp.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :return: The instance_name of this DiskResp.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this DiskResp.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :param instance_name: The instance_name of this DiskResp.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DiskResp.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :return: The instance_id of this DiskResp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DiskResp.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :param instance_id: The instance_id of this DiskResp.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def host_name(self):
        r"""Gets the host_name of this DiskResp.

        **参数解释**： 主机名称。 **取值范围**： 不涉及。

        :return: The host_name of this DiskResp.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this DiskResp.

        **参数解释**： 主机名称。 **取值范围**： 不涉及。

        :param host_name: The host_name of this DiskResp.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def disk_name(self):
        r"""Gets the disk_name of this DiskResp.

        **参数解释**： 磁盘名称。 **取值范围**： 不涉及。

        :return: The disk_name of this DiskResp.
        :rtype: str
        """
        return self._disk_name

    @disk_name.setter
    def disk_name(self, disk_name):
        r"""Sets the disk_name of this DiskResp.

        **参数解释**： 磁盘名称。 **取值范围**： 不涉及。

        :param disk_name: The disk_name of this DiskResp.
        :type disk_name: str
        """
        self._disk_name = disk_name

    @property
    def disk_type(self):
        r"""Gets the disk_type of this DiskResp.

        **参数解释**： 磁盘类型(系统盘、数据盘、日志盘)。 **取值范围**： 不涉及。

        :return: The disk_type of this DiskResp.
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        r"""Sets the disk_type of this DiskResp.

        **参数解释**： 磁盘类型(系统盘、数据盘、日志盘)。 **取值范围**： 不涉及。

        :param disk_type: The disk_type of this DiskResp.
        :type disk_type: str
        """
        self._disk_type = disk_type

    @property
    def total(self):
        r"""Gets the total of this DiskResp.

        **参数解释**： 磁盘总容量(GB)。 **取值范围**： 不涉及。

        :return: The total of this DiskResp.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this DiskResp.

        **参数解释**： 磁盘总容量(GB)。 **取值范围**： 不涉及。

        :param total: The total of this DiskResp.
        :type total: float
        """
        self._total = total

    @property
    def used(self):
        r"""Gets the used of this DiskResp.

        **参数解释**： 磁盘已使用容量(GB)。 **取值范围**： 不涉及。

        :return: The used of this DiskResp.
        :rtype: float
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this DiskResp.

        **参数解释**： 磁盘已使用容量(GB)。 **取值范围**： 不涉及。

        :param used: The used of this DiskResp.
        :type used: float
        """
        self._used = used

    @property
    def available(self):
        r"""Gets the available of this DiskResp.

        **参数解释**： 磁盘可用容量(GB)。 **取值范围**： 不涉及。

        :return: The available of this DiskResp.
        :rtype: float
        """
        return self._available

    @available.setter
    def available(self, available):
        r"""Sets the available of this DiskResp.

        **参数解释**： 磁盘可用容量(GB)。 **取值范围**： 不涉及。

        :param available: The available of this DiskResp.
        :type available: float
        """
        self._available = available

    @property
    def used_percentage(self):
        r"""Gets the used_percentage of this DiskResp.

        **参数解释**： 磁盘使用率(%)。 **取值范围**： 不涉及。

        :return: The used_percentage of this DiskResp.
        :rtype: float
        """
        return self._used_percentage

    @used_percentage.setter
    def used_percentage(self, used_percentage):
        r"""Sets the used_percentage of this DiskResp.

        **参数解释**： 磁盘使用率(%)。 **取值范围**： 不涉及。

        :param used_percentage: The used_percentage of this DiskResp.
        :type used_percentage: float
        """
        self._used_percentage = used_percentage

    @property
    def _await(self):
        r"""Gets the _await of this DiskResp.

        **参数解释**： IO等待时间(ms)。 **取值范围**： 不涉及。

        :return: The _await of this DiskResp.
        :rtype: float
        """
        return self.__await

    @_await.setter
    def _await(self, _await):
        r"""Sets the _await of this DiskResp.

        **参数解释**： IO等待时间(ms)。 **取值范围**： 不涉及。

        :param _await: The _await of this DiskResp.
        :type _await: float
        """
        self.__await = _await

    @property
    def svctm(self):
        r"""Gets the svctm of this DiskResp.

        **参数解释**： IO服务时间(ms)。 **取值范围**： 不涉及。

        :return: The svctm of this DiskResp.
        :rtype: float
        """
        return self._svctm

    @svctm.setter
    def svctm(self, svctm):
        r"""Sets the svctm of this DiskResp.

        **参数解释**： IO服务时间(ms)。 **取值范围**： 不涉及。

        :param svctm: The svctm of this DiskResp.
        :type svctm: float
        """
        self._svctm = svctm

    @property
    def util(self):
        r"""Gets the util of this DiskResp.

        **参数解释**： IO使用率(%)。 **取值范围**： 不涉及。

        :return: The util of this DiskResp.
        :rtype: float
        """
        return self._util

    @util.setter
    def util(self, util):
        r"""Sets the util of this DiskResp.

        **参数解释**： IO使用率(%)。 **取值范围**： 不涉及。

        :param util: The util of this DiskResp.
        :type util: float
        """
        self._util = util

    @property
    def read_rate(self):
        r"""Gets the read_rate of this DiskResp.

        **参数解释**： 磁盘读速率(KB/s)。 **取值范围**： 不涉及。

        :return: The read_rate of this DiskResp.
        :rtype: float
        """
        return self._read_rate

    @read_rate.setter
    def read_rate(self, read_rate):
        r"""Sets the read_rate of this DiskResp.

        **参数解释**： 磁盘读速率(KB/s)。 **取值范围**： 不涉及。

        :param read_rate: The read_rate of this DiskResp.
        :type read_rate: float
        """
        self._read_rate = read_rate

    @property
    def write_rate(self):
        r"""Gets the write_rate of this DiskResp.

        **参数解释**： 磁盘写速率(KB/s)。 **取值范围**： 不涉及。

        :return: The write_rate of this DiskResp.
        :rtype: float
        """
        return self._write_rate

    @write_rate.setter
    def write_rate(self, write_rate):
        r"""Sets the write_rate of this DiskResp.

        **参数解释**： 磁盘写速率(KB/s)。 **取值范围**： 不涉及。

        :param write_rate: The write_rate of this DiskResp.
        :type write_rate: float
        """
        self._write_rate = write_rate

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
        if not isinstance(other, DiskResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
