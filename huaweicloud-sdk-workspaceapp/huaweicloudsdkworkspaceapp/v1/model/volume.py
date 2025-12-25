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
        'cluster_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'size': 'size',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, type=None, size=None, cluster_id=None):
        r"""Volume

        The model defined in huaweicloud sdk

        :param type: 磁盘类型，获取可用磁盘类型详见接口磁盘管理ListVolumeType。 * &#x60;ESSD&#x60; - 极速型SSD * &#x60;SSD&#x60; - 超高IO * &#x60;GPSSD&#x60; - 通用型SSD * &#x60;SAS&#x60; - 高IO * &#x60;SATA&#x60; - 普通IO
        :type type: str
        :param size: 磁盘容量，单位GB，数值约束为10的倍数。 * &#x60;系统盘&#x60; minLength: 10，maxLength: 1024 * &#x60;数据盘&#x60; minLength: 10，maxLength: 32768
        :type size: int
        :param cluster_id: 云服务器系统盘对应的存储池的ID。
        :type cluster_id: str
        """
        
        

        self._type = None
        self._size = None
        self._cluster_id = None
        self.discriminator = None

        self.type = type
        self.size = size
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def type(self):
        r"""Gets the type of this Volume.

        磁盘类型，获取可用磁盘类型详见接口磁盘管理ListVolumeType。 * `ESSD` - 极速型SSD * `SSD` - 超高IO * `GPSSD` - 通用型SSD * `SAS` - 高IO * `SATA` - 普通IO

        :return: The type of this Volume.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Volume.

        磁盘类型，获取可用磁盘类型详见接口磁盘管理ListVolumeType。 * `ESSD` - 极速型SSD * `SSD` - 超高IO * `GPSSD` - 通用型SSD * `SAS` - 高IO * `SATA` - 普通IO

        :param type: The type of this Volume.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this Volume.

        磁盘容量，单位GB，数值约束为10的倍数。 * `系统盘` minLength: 10，maxLength: 1024 * `数据盘` minLength: 10，maxLength: 32768

        :return: The size of this Volume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Volume.

        磁盘容量，单位GB，数值约束为10的倍数。 * `系统盘` minLength: 10，maxLength: 1024 * `数据盘` minLength: 10，maxLength: 32768

        :param size: The size of this Volume.
        :type size: int
        """
        self._size = size

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this Volume.

        云服务器系统盘对应的存储池的ID。

        :return: The cluster_id of this Volume.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this Volume.

        云服务器系统盘对应的存储池的ID。

        :param cluster_id: The cluster_id of this Volume.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
