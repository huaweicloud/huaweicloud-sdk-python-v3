# coding: utf-8

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
        'type': 'str',
        'size': 'int',
        'iops': 'int',
        'throughput': 'int',
        'kms_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'size': 'size',
        'iops': 'iops',
        'throughput': 'throughput',
        'kms_id': 'kms_id'
    }

    def __init__(self, type=None, size=None, iops=None, throughput=None, kms_id=None):
        r"""Volume

        The model defined in huaweicloud sdk

        :param type: 桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  -SAS：高IO。 -SSD：超高IO。 -GPSSD：通用型SSD。
        :type type: str
        :param size: 磁盘容量，单位GB。系统盘大小范围[80-32760]，数据盘范围[10-32760]，大小为10的倍数。
        :type size: int
        :param iops: iops，云硬盘每秒进行读写的操作次数。
        :type iops: int
        :param throughput: 吞吐量，云硬盘每秒成功传送的数据量，即读取和写入的数据量。
        :type throughput: int
        :param kms_id: kms密钥id，对创建的磁盘进行加密。
        :type kms_id: str
        """
        
        

        self._type = None
        self._size = None
        self._iops = None
        self._throughput = None
        self._kms_id = None
        self.discriminator = None

        self.type = type
        self.size = size
        if iops is not None:
            self.iops = iops
        if throughput is not None:
            self.throughput = throughput
        if kms_id is not None:
            self.kms_id = kms_id

    @property
    def type(self):
        r"""Gets the type of this Volume.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  -SAS：高IO。 -SSD：超高IO。 -GPSSD：通用型SSD。

        :return: The type of this Volume.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Volume.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  -SAS：高IO。 -SSD：超高IO。 -GPSSD：通用型SSD。

        :param type: The type of this Volume.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this Volume.

        磁盘容量，单位GB。系统盘大小范围[80-32760]，数据盘范围[10-32760]，大小为10的倍数。

        :return: The size of this Volume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Volume.

        磁盘容量，单位GB。系统盘大小范围[80-32760]，数据盘范围[10-32760]，大小为10的倍数。

        :param size: The size of this Volume.
        :type size: int
        """
        self._size = size

    @property
    def iops(self):
        r"""Gets the iops of this Volume.

        iops，云硬盘每秒进行读写的操作次数。

        :return: The iops of this Volume.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        r"""Sets the iops of this Volume.

        iops，云硬盘每秒进行读写的操作次数。

        :param iops: The iops of this Volume.
        :type iops: int
        """
        self._iops = iops

    @property
    def throughput(self):
        r"""Gets the throughput of this Volume.

        吞吐量，云硬盘每秒成功传送的数据量，即读取和写入的数据量。

        :return: The throughput of this Volume.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        r"""Sets the throughput of this Volume.

        吞吐量，云硬盘每秒成功传送的数据量，即读取和写入的数据量。

        :param throughput: The throughput of this Volume.
        :type throughput: int
        """
        self._throughput = throughput

    @property
    def kms_id(self):
        r"""Gets the kms_id of this Volume.

        kms密钥id，对创建的磁盘进行加密。

        :return: The kms_id of this Volume.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        r"""Sets the kms_id of this Volume.

        kms密钥id，对创建的磁盘进行加密。

        :param kms_id: The kms_id of this Volume.
        :type kms_id: str
        """
        self._kms_id = kms_id

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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
