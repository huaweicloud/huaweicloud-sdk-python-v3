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
        'type': 'str',
        'size': 'int',
        'kms_grant_id': 'str',
        'device': 'str',
        'id': 'str',
        'volume_id': 'str',
        'bill_resource_id': 'str',
        'create_time': 'str',
        'display_name': 'str',
        'cluster_id': 'str',
        'resource_spec_code': 'str'
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
        'bill_resource_id': 'bill_resource_id',
        'create_time': 'create_time',
        'display_name': 'display_name',
        'cluster_id': 'cluster_id',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, encrypt_flag=None, kms_key=None, key_alias=None, type=None, size=None, kms_grant_id=None, device=None, id=None, volume_id=None, bill_resource_id=None, create_time=None, display_name=None, cluster_id=None, resource_spec_code=None):
        """VolumeDetail

        The model defined in huaweicloud sdk

        :param encrypt_flag: 标识磁盘是否加密，如果为1就是加密。
        :type encrypt_flag: str
        :param kms_key: 如果磁盘加密，传递的密钥。
        :type kms_key: str
        :param key_alias: 如果磁盘加密，传递的密钥。
        :type key_alias: str
        :param type: 桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  - SAS：高IO。 - SSD：超高IO。
        :type type: str
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
        :param bill_resource_id: 磁盘计费资源ID。
        :type bill_resource_id: str
        :param create_time: 磁盘的创建时间
        :type create_time: str
        :param display_name: 磁盘名
        :type display_name: str
        :param cluster_id: 云服务器系统盘对应的存储池的ID。
        :type cluster_id: str
        :param resource_spec_code: 规格
        :type resource_spec_code: str
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
        self._bill_resource_id = None
        self._create_time = None
        self._display_name = None
        self._cluster_id = None
        self._resource_spec_code = None
        self.discriminator = None

        if encrypt_flag is not None:
            self.encrypt_flag = encrypt_flag
        if kms_key is not None:
            self.kms_key = kms_key
        if key_alias is not None:
            self.key_alias = key_alias
        self.type = type
        self.size = size
        if kms_grant_id is not None:
            self.kms_grant_id = kms_grant_id
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
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code

    @property
    def encrypt_flag(self):
        """Gets the encrypt_flag of this VolumeDetail.

        标识磁盘是否加密，如果为1就是加密。

        :return: The encrypt_flag of this VolumeDetail.
        :rtype: str
        """
        return self._encrypt_flag

    @encrypt_flag.setter
    def encrypt_flag(self, encrypt_flag):
        """Sets the encrypt_flag of this VolumeDetail.

        标识磁盘是否加密，如果为1就是加密。

        :param encrypt_flag: The encrypt_flag of this VolumeDetail.
        :type encrypt_flag: str
        """
        self._encrypt_flag = encrypt_flag

    @property
    def kms_key(self):
        """Gets the kms_key of this VolumeDetail.

        如果磁盘加密，传递的密钥。

        :return: The kms_key of this VolumeDetail.
        :rtype: str
        """
        return self._kms_key

    @kms_key.setter
    def kms_key(self, kms_key):
        """Sets the kms_key of this VolumeDetail.

        如果磁盘加密，传递的密钥。

        :param kms_key: The kms_key of this VolumeDetail.
        :type kms_key: str
        """
        self._kms_key = kms_key

    @property
    def key_alias(self):
        """Gets the key_alias of this VolumeDetail.

        如果磁盘加密，传递的密钥。

        :return: The key_alias of this VolumeDetail.
        :rtype: str
        """
        return self._key_alias

    @key_alias.setter
    def key_alias(self, key_alias):
        """Sets the key_alias of this VolumeDetail.

        如果磁盘加密，传递的密钥。

        :param key_alias: The key_alias of this VolumeDetail.
        :type key_alias: str
        """
        self._key_alias = key_alias

    @property
    def type(self):
        """Gets the type of this VolumeDetail.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  - SAS：高IO。 - SSD：超高IO。

        :return: The type of this VolumeDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VolumeDetail.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  - SAS：高IO。 - SSD：超高IO。

        :param type: The type of this VolumeDetail.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        """Gets the size of this VolumeDetail.

        磁盘容量，单位GB。

        :return: The size of this VolumeDetail.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeDetail.

        磁盘容量，单位GB。

        :param size: The size of this VolumeDetail.
        :type size: int
        """
        self._size = size

    @property
    def kms_grant_id(self):
        """Gets the kms_grant_id of this VolumeDetail.

        如果磁盘加密，授权ID。

        :return: The kms_grant_id of this VolumeDetail.
        :rtype: str
        """
        return self._kms_grant_id

    @kms_grant_id.setter
    def kms_grant_id(self, kms_grant_id):
        """Sets the kms_grant_id of this VolumeDetail.

        如果磁盘加密，授权ID。

        :param kms_grant_id: The kms_grant_id of this VolumeDetail.
        :type kms_grant_id: str
        """
        self._kms_grant_id = kms_grant_id

    @property
    def device(self):
        """Gets the device of this VolumeDetail.

        挂载目录。

        :return: The device of this VolumeDetail.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this VolumeDetail.

        挂载目录。

        :param device: The device of this VolumeDetail.
        :type device: str
        """
        self._device = device

    @property
    def id(self):
        """Gets the id of this VolumeDetail.

        磁盘表唯一标识ID。

        :return: The id of this VolumeDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeDetail.

        磁盘表唯一标识ID。

        :param id: The id of this VolumeDetail.
        :type id: str
        """
        self._id = id

    @property
    def volume_id(self):
        """Gets the volume_id of this VolumeDetail.

        磁盘ID。

        :return: The volume_id of this VolumeDetail.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this VolumeDetail.

        磁盘ID。

        :param volume_id: The volume_id of this VolumeDetail.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def bill_resource_id(self):
        """Gets the bill_resource_id of this VolumeDetail.

        磁盘计费资源ID。

        :return: The bill_resource_id of this VolumeDetail.
        :rtype: str
        """
        return self._bill_resource_id

    @bill_resource_id.setter
    def bill_resource_id(self, bill_resource_id):
        """Sets the bill_resource_id of this VolumeDetail.

        磁盘计费资源ID。

        :param bill_resource_id: The bill_resource_id of this VolumeDetail.
        :type bill_resource_id: str
        """
        self._bill_resource_id = bill_resource_id

    @property
    def create_time(self):
        """Gets the create_time of this VolumeDetail.

        磁盘的创建时间

        :return: The create_time of this VolumeDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VolumeDetail.

        磁盘的创建时间

        :param create_time: The create_time of this VolumeDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def display_name(self):
        """Gets the display_name of this VolumeDetail.

        磁盘名

        :return: The display_name of this VolumeDetail.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this VolumeDetail.

        磁盘名

        :param display_name: The display_name of this VolumeDetail.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this VolumeDetail.

        云服务器系统盘对应的存储池的ID。

        :return: The cluster_id of this VolumeDetail.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this VolumeDetail.

        云服务器系统盘对应的存储池的ID。

        :param cluster_id: The cluster_id of this VolumeDetail.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this VolumeDetail.

        规格

        :return: The resource_spec_code of this VolumeDetail.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this VolumeDetail.

        规格

        :param resource_spec_code: The resource_spec_code of this VolumeDetail.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

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
