# coding: utf-8

import six

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
        'encrypt_flag': 'str',
        'kms_key': 'str',
        'key_alias': 'str',
        'type': 'VolumeType',
        'size': 'int',
        'kms_grant_id': 'str',
        'device': 'str',
        'id': 'str',
        'volume_id': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'encrypt_flag': 'encrypt_flag',
        'kms_key': 'kms_key',
        'key_alias': 'key_alias',
        'type': 'type',
        'size': 'size',
        'kms_grant_id': 'kms_grant_id',
        'device': 'device',
        'id': 'id',
        'volume_id': 'volume_id',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, encrypt_flag=None, kms_key=None, key_alias=None, type=None, size=None, kms_grant_id=None, device=None, id=None, volume_id=None, cluster_id=None):
        r"""VolumeDetail

        The model defined in huaweicloud sdk

        :param encrypt_flag: 标识磁盘是否加密，如果为1就是加密，0非加密。
        :type encrypt_flag: str
        :param kms_key: 如果磁盘加密，传递的密钥。
        :type kms_key: str
        :param key_alias: 如果磁盘加密，传递的密钥。
        :type key_alias: str
        :param type: 
        :type type: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
        :param size: 磁盘容量，单位GB。
        :type size: int
        :param kms_grant_id: 如果磁盘加密，授权ID。
        :type kms_grant_id: str
        :param device: 挂载目录。
        :type device: str
        :param id: 磁盘表唯一标识ID。
        :type id: str
        :param volume_id: 磁盘ID。
        :type volume_id: str
        :param cluster_id: 专属分布式存储池id。
        :type cluster_id: str
        """
        
        

        self._encrypt_flag = None
        self._kms_key = None
        self._key_alias = None
        self._type = None
        self._size = None
        self._kms_grant_id = None
        self._device = None
        self._id = None
        self._volume_id = None
        self._cluster_id = None
        self.discriminator = None

        if encrypt_flag is not None:
            self.encrypt_flag = encrypt_flag
        if kms_key is not None:
            self.kms_key = kms_key
        if key_alias is not None:
            self.key_alias = key_alias
        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if kms_grant_id is not None:
            self.kms_grant_id = kms_grant_id
        if device is not None:
            self.device = device
        if id is not None:
            self.id = id
        if volume_id is not None:
            self.volume_id = volume_id
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def encrypt_flag(self):
        r"""Gets the encrypt_flag of this VolumeDetail.

        标识磁盘是否加密，如果为1就是加密，0非加密。

        :return: The encrypt_flag of this VolumeDetail.
        :rtype: str
        """
        return self._encrypt_flag

    @encrypt_flag.setter
    def encrypt_flag(self, encrypt_flag):
        r"""Sets the encrypt_flag of this VolumeDetail.

        标识磁盘是否加密，如果为1就是加密，0非加密。

        :param encrypt_flag: The encrypt_flag of this VolumeDetail.
        :type encrypt_flag: str
        """
        self._encrypt_flag = encrypt_flag

    @property
    def kms_key(self):
        r"""Gets the kms_key of this VolumeDetail.

        如果磁盘加密，传递的密钥。

        :return: The kms_key of this VolumeDetail.
        :rtype: str
        """
        return self._kms_key

    @kms_key.setter
    def kms_key(self, kms_key):
        r"""Sets the kms_key of this VolumeDetail.

        如果磁盘加密，传递的密钥。

        :param kms_key: The kms_key of this VolumeDetail.
        :type kms_key: str
        """
        self._kms_key = kms_key

    @property
    def key_alias(self):
        r"""Gets the key_alias of this VolumeDetail.

        如果磁盘加密，传递的密钥。

        :return: The key_alias of this VolumeDetail.
        :rtype: str
        """
        return self._key_alias

    @key_alias.setter
    def key_alias(self, key_alias):
        r"""Sets the key_alias of this VolumeDetail.

        如果磁盘加密，传递的密钥。

        :param key_alias: The key_alias of this VolumeDetail.
        :type key_alias: str
        """
        self._key_alias = key_alias

    @property
    def type(self):
        r"""Gets the type of this VolumeDetail.

        :return: The type of this VolumeDetail.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VolumeDetail.

        :param type: The type of this VolumeDetail.
        :type type: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
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
    def kms_grant_id(self):
        r"""Gets the kms_grant_id of this VolumeDetail.

        如果磁盘加密，授权ID。

        :return: The kms_grant_id of this VolumeDetail.
        :rtype: str
        """
        return self._kms_grant_id

    @kms_grant_id.setter
    def kms_grant_id(self, kms_grant_id):
        r"""Sets the kms_grant_id of this VolumeDetail.

        如果磁盘加密，授权ID。

        :param kms_grant_id: The kms_grant_id of this VolumeDetail.
        :type kms_grant_id: str
        """
        self._kms_grant_id = kms_grant_id

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

        磁盘表唯一标识ID。

        :return: The id of this VolumeDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VolumeDetail.

        磁盘表唯一标识ID。

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
    def cluster_id(self):
        r"""Gets the cluster_id of this VolumeDetail.

        专属分布式存储池id。

        :return: The cluster_id of this VolumeDetail.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this VolumeDetail.

        专属分布式存储池id。

        :param cluster_id: The cluster_id of this VolumeDetail.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, VolumeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
