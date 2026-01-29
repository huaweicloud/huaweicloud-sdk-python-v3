# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopPoolVolumeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'iops': 'int',
        'throughput': 'int',
        'kms_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'iops': 'iops',
        'throughput': 'throughput',
        'kms_id': 'kms_id'
    }

    def __init__(self, id=None, type=None, iops=None, throughput=None, kms_id=None):
        r"""DesktopPoolVolumeInfo

        The model defined in huaweicloud sdk

        :param id: 批量操作磁盘的磁盘集合id。
        :type id: str
        :param type: 桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。 - SAS：高IO。 - SSD：超高IO。
        :type type: str
        :param iops: iops，磁盘每秒进行读写的操作次数。
        :type iops: int
        :param throughput: 吞吐量，磁盘每秒成功传送的数据量，即读取和写入的数据量。
        :type throughput: int
        :param kms_id: kms密钥id。变更密钥时传入密钥id；如需删除密钥则传入空字符串；默认null，不变更密钥。
        :type kms_id: str
        """
        
        

        self._id = None
        self._type = None
        self._iops = None
        self._throughput = None
        self._kms_id = None
        self.discriminator = None

        self.id = id
        self.type = type
        if iops is not None:
            self.iops = iops
        if throughput is not None:
            self.throughput = throughput
        if kms_id is not None:
            self.kms_id = kms_id

    @property
    def id(self):
        r"""Gets the id of this DesktopPoolVolumeInfo.

        批量操作磁盘的磁盘集合id。

        :return: The id of this DesktopPoolVolumeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DesktopPoolVolumeInfo.

        批量操作磁盘的磁盘集合id。

        :param id: The id of this DesktopPoolVolumeInfo.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this DesktopPoolVolumeInfo.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。 - SAS：高IO。 - SSD：超高IO。

        :return: The type of this DesktopPoolVolumeInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DesktopPoolVolumeInfo.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。 - SAS：高IO。 - SSD：超高IO。

        :param type: The type of this DesktopPoolVolumeInfo.
        :type type: str
        """
        self._type = type

    @property
    def iops(self):
        r"""Gets the iops of this DesktopPoolVolumeInfo.

        iops，磁盘每秒进行读写的操作次数。

        :return: The iops of this DesktopPoolVolumeInfo.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        r"""Sets the iops of this DesktopPoolVolumeInfo.

        iops，磁盘每秒进行读写的操作次数。

        :param iops: The iops of this DesktopPoolVolumeInfo.
        :type iops: int
        """
        self._iops = iops

    @property
    def throughput(self):
        r"""Gets the throughput of this DesktopPoolVolumeInfo.

        吞吐量，磁盘每秒成功传送的数据量，即读取和写入的数据量。

        :return: The throughput of this DesktopPoolVolumeInfo.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        r"""Sets the throughput of this DesktopPoolVolumeInfo.

        吞吐量，磁盘每秒成功传送的数据量，即读取和写入的数据量。

        :param throughput: The throughput of this DesktopPoolVolumeInfo.
        :type throughput: int
        """
        self._throughput = throughput

    @property
    def kms_id(self):
        r"""Gets the kms_id of this DesktopPoolVolumeInfo.

        kms密钥id。变更密钥时传入密钥id；如需删除密钥则传入空字符串；默认null，不变更密钥。

        :return: The kms_id of this DesktopPoolVolumeInfo.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        r"""Sets the kms_id of this DesktopPoolVolumeInfo.

        kms密钥id。变更密钥时传入密钥id；如需删除密钥则传入空字符串；默认null，不变更密钥。

        :param kms_id: The kms_id of this DesktopPoolVolumeInfo.
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
        if not isinstance(other, DesktopPoolVolumeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
