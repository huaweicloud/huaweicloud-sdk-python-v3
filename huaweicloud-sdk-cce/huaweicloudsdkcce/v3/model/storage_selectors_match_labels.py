# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageSelectorsMatchLabels:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'str',
        'volume_type': 'str',
        'metadata_encrypted': 'str',
        'metadata_cmkid': 'str',
        'count': 'str'
    }

    attribute_map = {
        'size': 'size',
        'volume_type': 'volumeType',
        'metadata_encrypted': 'metadataEncrypted',
        'metadata_cmkid': 'metadataCmkid',
        'count': 'count'
    }

    def __init__(self, size=None, volume_type=None, metadata_encrypted=None, metadata_cmkid=None, count=None):
        """StorageSelectorsMatchLabels

        The model defined in huaweicloud sdk

        :param size: 匹配的磁盘大小，不填则无磁盘大小限制。例如：100.
        :type size: str
        :param volume_type: 云硬盘类型，目前支持SSD\\GPSSD\\SAS三种。
        :type volume_type: str
        :param metadata_encrypted: 磁盘加密标识符，0代表不加密，1代表加密。
        :type metadata_encrypted: str
        :param metadata_cmkid: 加密磁盘的用户主密钥ID，长度为36字节的字符串。
        :type metadata_cmkid: str
        :param count: 磁盘选择个数，不填则选择所有此类磁盘。
        :type count: str
        """
        
        

        self._size = None
        self._volume_type = None
        self._metadata_encrypted = None
        self._metadata_cmkid = None
        self._count = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if volume_type is not None:
            self.volume_type = volume_type
        if metadata_encrypted is not None:
            self.metadata_encrypted = metadata_encrypted
        if metadata_cmkid is not None:
            self.metadata_cmkid = metadata_cmkid
        if count is not None:
            self.count = count

    @property
    def size(self):
        """Gets the size of this StorageSelectorsMatchLabels.

        匹配的磁盘大小，不填则无磁盘大小限制。例如：100.

        :return: The size of this StorageSelectorsMatchLabels.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this StorageSelectorsMatchLabels.

        匹配的磁盘大小，不填则无磁盘大小限制。例如：100.

        :param size: The size of this StorageSelectorsMatchLabels.
        :type size: str
        """
        self._size = size

    @property
    def volume_type(self):
        """Gets the volume_type of this StorageSelectorsMatchLabels.

        云硬盘类型，目前支持SSD\\GPSSD\\SAS三种。

        :return: The volume_type of this StorageSelectorsMatchLabels.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this StorageSelectorsMatchLabels.

        云硬盘类型，目前支持SSD\\GPSSD\\SAS三种。

        :param volume_type: The volume_type of this StorageSelectorsMatchLabels.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def metadata_encrypted(self):
        """Gets the metadata_encrypted of this StorageSelectorsMatchLabels.

        磁盘加密标识符，0代表不加密，1代表加密。

        :return: The metadata_encrypted of this StorageSelectorsMatchLabels.
        :rtype: str
        """
        return self._metadata_encrypted

    @metadata_encrypted.setter
    def metadata_encrypted(self, metadata_encrypted):
        """Sets the metadata_encrypted of this StorageSelectorsMatchLabels.

        磁盘加密标识符，0代表不加密，1代表加密。

        :param metadata_encrypted: The metadata_encrypted of this StorageSelectorsMatchLabels.
        :type metadata_encrypted: str
        """
        self._metadata_encrypted = metadata_encrypted

    @property
    def metadata_cmkid(self):
        """Gets the metadata_cmkid of this StorageSelectorsMatchLabels.

        加密磁盘的用户主密钥ID，长度为36字节的字符串。

        :return: The metadata_cmkid of this StorageSelectorsMatchLabels.
        :rtype: str
        """
        return self._metadata_cmkid

    @metadata_cmkid.setter
    def metadata_cmkid(self, metadata_cmkid):
        """Sets the metadata_cmkid of this StorageSelectorsMatchLabels.

        加密磁盘的用户主密钥ID，长度为36字节的字符串。

        :param metadata_cmkid: The metadata_cmkid of this StorageSelectorsMatchLabels.
        :type metadata_cmkid: str
        """
        self._metadata_cmkid = metadata_cmkid

    @property
    def count(self):
        """Gets the count of this StorageSelectorsMatchLabels.

        磁盘选择个数，不填则选择所有此类磁盘。

        :return: The count of this StorageSelectorsMatchLabels.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this StorageSelectorsMatchLabels.

        磁盘选择个数，不填则选择所有此类磁盘。

        :param count: The count of this StorageSelectorsMatchLabels.
        :type count: str
        """
        self._count = count

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
        if not isinstance(other, StorageSelectorsMatchLabels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
