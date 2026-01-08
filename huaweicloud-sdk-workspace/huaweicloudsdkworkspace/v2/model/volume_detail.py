# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kms_id': 'str',
        'type': 'str',
        'size': 'int',
        'iops': 'int',
        'throughput': 'int',
        'device': 'str',
        'id': 'str',
        'volume_id': 'str',
        'bill_resource_id': 'str',
        'create_time': 'str',
        'display_name': 'str',
        'resource_spec_code': 'str'
    }

    attribute_map = {
        'kms_id': 'kms_id',
        'type': 'type',
        'size': 'size',
        'iops': 'iops',
        'throughput': 'throughput',
        'device': 'device',
        'id': 'id',
        'volume_id': 'volume_id',
        'bill_resource_id': 'bill_resource_id',
        'create_time': 'create_time',
        'display_name': 'display_name',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, kms_id=None, type=None, size=None, iops=None, throughput=None, device=None, id=None, volume_id=None, bill_resource_id=None, create_time=None, display_name=None, resource_spec_code=None):
        r"""VolumeDetail

        The model defined in huaweicloud sdk

        :param kms_id: 如果磁盘加密，传递的密钥。
        :type kms_id: str
        :param type: 桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  - SAS：高IO。 - SSD：超高IO。
        :type type: str
        :param size: 磁盘容量，单位GB。
        :type size: int
        :param iops: iops，云硬盘每秒进行读写的操作次数。
        :type iops: int
        :param throughput: 吞吐量，云硬盘每秒成功传送的数据量，即读取和写入的数据量。
        :type throughput: int
        :param device: 挂载目录。
        :type device: str
        :param id: 磁盘唯一标识ID。
        :type id: str
        :param volume_id: 磁盘ID。
        :type volume_id: str
        :param bill_resource_id: 磁盘计费资源ID。
        :type bill_resource_id: str
        :param create_time: 磁盘的创建时间。
        :type create_time: str
        :param display_name: 磁盘名。
        :type display_name: str
        :param resource_spec_code: 规格。
        :type resource_spec_code: str
        """
        
        

        self._kms_id = None
        self._type = None
        self._size = None
        self._iops = None
        self._throughput = None
        self._device = None
        self._id = None
        self._volume_id = None
        self._bill_resource_id = None
        self._create_time = None
        self._display_name = None
        self._resource_spec_code = None
        self.discriminator = None

        if kms_id is not None:
            self.kms_id = kms_id
        self.type = type
        self.size = size
        if iops is not None:
            self.iops = iops
        if throughput is not None:
            self.throughput = throughput
        if device is not None:
            self.device = device
        if id is not None:
            self.id = id
        if volume_id is not None:
            self.volume_id = volume_id
        if bill_resource_id is not None:
            self.bill_resource_id = bill_resource_id
        if create_time is not None:
            self.create_time = create_time
        if display_name is not None:
            self.display_name = display_name
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code

    @property
    def kms_id(self):
        r"""Gets the kms_id of this VolumeDetail.

        如果磁盘加密，传递的密钥。

        :return: The kms_id of this VolumeDetail.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        r"""Sets the kms_id of this VolumeDetail.

        如果磁盘加密，传递的密钥。

        :param kms_id: The kms_id of this VolumeDetail.
        :type kms_id: str
        """
        self._kms_id = kms_id

    @property
    def type(self):
        r"""Gets the type of this VolumeDetail.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  - SAS：高IO。 - SSD：超高IO。

        :return: The type of this VolumeDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VolumeDetail.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  - SAS：高IO。 - SSD：超高IO。

        :param type: The type of this VolumeDetail.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this VolumeDetail.

        磁盘容量，单位GB。

        :return: The size of this VolumeDetail.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this VolumeDetail.

        磁盘容量，单位GB。

        :param size: The size of this VolumeDetail.
        :type size: int
        """
        self._size = size

    @property
    def iops(self):
        r"""Gets the iops of this VolumeDetail.

        iops，云硬盘每秒进行读写的操作次数。

        :return: The iops of this VolumeDetail.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        r"""Sets the iops of this VolumeDetail.

        iops，云硬盘每秒进行读写的操作次数。

        :param iops: The iops of this VolumeDetail.
        :type iops: int
        """
        self._iops = iops

    @property
    def throughput(self):
        r"""Gets the throughput of this VolumeDetail.

        吞吐量，云硬盘每秒成功传送的数据量，即读取和写入的数据量。

        :return: The throughput of this VolumeDetail.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        r"""Sets the throughput of this VolumeDetail.

        吞吐量，云硬盘每秒成功传送的数据量，即读取和写入的数据量。

        :param throughput: The throughput of this VolumeDetail.
        :type throughput: int
        """
        self._throughput = throughput

    @property
    def device(self):
        r"""Gets the device of this VolumeDetail.

        挂载目录。

        :return: The device of this VolumeDetail.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        r"""Sets the device of this VolumeDetail.

        挂载目录。

        :param device: The device of this VolumeDetail.
        :type device: str
        """
        self._device = device

    @property
    def id(self):
        r"""Gets the id of this VolumeDetail.

        磁盘唯一标识ID。

        :return: The id of this VolumeDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VolumeDetail.

        磁盘唯一标识ID。

        :param id: The id of this VolumeDetail.
        :type id: str
        """
        self._id = id

    @property
    def volume_id(self):
        r"""Gets the volume_id of this VolumeDetail.

        磁盘ID。

        :return: The volume_id of this VolumeDetail.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this VolumeDetail.

        磁盘ID。

        :param volume_id: The volume_id of this VolumeDetail.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def bill_resource_id(self):
        r"""Gets the bill_resource_id of this VolumeDetail.

        磁盘计费资源ID。

        :return: The bill_resource_id of this VolumeDetail.
        :rtype: str
        """
        return self._bill_resource_id

    @bill_resource_id.setter
    def bill_resource_id(self, bill_resource_id):
        r"""Sets the bill_resource_id of this VolumeDetail.

        磁盘计费资源ID。

        :param bill_resource_id: The bill_resource_id of this VolumeDetail.
        :type bill_resource_id: str
        """
        self._bill_resource_id = bill_resource_id

    @property
    def create_time(self):
        r"""Gets the create_time of this VolumeDetail.

        磁盘的创建时间。

        :return: The create_time of this VolumeDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this VolumeDetail.

        磁盘的创建时间。

        :param create_time: The create_time of this VolumeDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def display_name(self):
        r"""Gets the display_name of this VolumeDetail.

        磁盘名。

        :return: The display_name of this VolumeDetail.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this VolumeDetail.

        磁盘名。

        :param display_name: The display_name of this VolumeDetail.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this VolumeDetail.

        规格。

        :return: The resource_spec_code of this VolumeDetail.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this VolumeDetail.

        规格。

        :param resource_spec_code: The resource_spec_code of this VolumeDetail.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

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
        if not isinstance(other, VolumeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
