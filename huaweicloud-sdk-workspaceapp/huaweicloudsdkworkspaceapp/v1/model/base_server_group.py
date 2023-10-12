# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseServerGroup:

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
        'name': 'str',
        'description': 'str',
        'image_id': 'str',
        'os_type': 'OsTypeEnum',
        'product_id': 'str',
        'subnet_id': 'str',
        'system_disk_type': 'VolumeType',
        'system_disk_size': 'int',
        'is_vdi': 'bool',
        'extra_session_type': 'ExtraSessionTypeEnum',
        'extra_session_size': 'int',
        'app_type': 'AppTypeEnum',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'storage_mount_policy': 'StorageFolderMountType'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'image_id': 'image_id',
        'os_type': 'os_type',
        'product_id': 'product_id',
        'subnet_id': 'subnet_id',
        'system_disk_type': 'system_disk_type',
        'system_disk_size': 'system_disk_size',
        'is_vdi': 'is_vdi',
        'extra_session_type': 'extra_session_type',
        'extra_session_size': 'extra_session_size',
        'app_type': 'app_type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'storage_mount_policy': 'storage_mount_policy'
    }

    def __init__(self, id=None, name=None, description=None, image_id=None, os_type=None, product_id=None, subnet_id=None, system_disk_type=None, system_disk_size=None, is_vdi=None, extra_session_type=None, extra_session_size=None, app_type=None, create_time=None, update_time=None, storage_mount_policy=None):
        """BaseServerGroup

        The model defined in huaweicloud sdk

        :param id: 服务器组的唯一标识
        :type id: str
        :param name: 服务器组名称
        :type name: str
        :param description: 服务器组描述
        :type description: str
        :param image_id: 服务器组关联的镜像ID，用于创建对应组下的云服务器
        :type image_id: str
        :param os_type: 
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        :param product_id: 产品id
        :type product_id: str
        :param subnet_id: 网卡对应的子网ID
        :type subnet_id: str
        :param system_disk_type: 
        :type system_disk_type: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
        :param system_disk_size: 磁盘容量，单位GB
        :type system_disk_size: int
        :param is_vdi: 是否为vdi单会话模式
        :type is_vdi: bool
        :param extra_session_type: 
        :type extra_session_type: :class:`huaweicloudsdkworkspaceapp.v1.ExtraSessionTypeEnum`
        :param extra_session_size: 付费会话个数
        :type extra_session_size: int
        :param app_type: 
        :type app_type: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        :param create_time: 服务器组创建时间
        :type create_time: datetime
        :param update_time: 服务器组更新时间
        :type update_time: datetime
        :param storage_mount_policy: 
        :type storage_mount_policy: :class:`huaweicloudsdkworkspaceapp.v1.StorageFolderMountType`
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._image_id = None
        self._os_type = None
        self._product_id = None
        self._subnet_id = None
        self._system_disk_type = None
        self._system_disk_size = None
        self._is_vdi = None
        self._extra_session_type = None
        self._extra_session_size = None
        self._app_type = None
        self._create_time = None
        self._update_time = None
        self._storage_mount_policy = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if image_id is not None:
            self.image_id = image_id
        if os_type is not None:
            self.os_type = os_type
        if product_id is not None:
            self.product_id = product_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if system_disk_type is not None:
            self.system_disk_type = system_disk_type
        if system_disk_size is not None:
            self.system_disk_size = system_disk_size
        if is_vdi is not None:
            self.is_vdi = is_vdi
        if extra_session_type is not None:
            self.extra_session_type = extra_session_type
        if extra_session_size is not None:
            self.extra_session_size = extra_session_size
        if app_type is not None:
            self.app_type = app_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if storage_mount_policy is not None:
            self.storage_mount_policy = storage_mount_policy

    @property
    def id(self):
        """Gets the id of this BaseServerGroup.

        服务器组的唯一标识

        :return: The id of this BaseServerGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseServerGroup.

        服务器组的唯一标识

        :param id: The id of this BaseServerGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BaseServerGroup.

        服务器组名称

        :return: The name of this BaseServerGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BaseServerGroup.

        服务器组名称

        :param name: The name of this BaseServerGroup.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this BaseServerGroup.

        服务器组描述

        :return: The description of this BaseServerGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BaseServerGroup.

        服务器组描述

        :param description: The description of this BaseServerGroup.
        :type description: str
        """
        self._description = description

    @property
    def image_id(self):
        """Gets the image_id of this BaseServerGroup.

        服务器组关联的镜像ID，用于创建对应组下的云服务器

        :return: The image_id of this BaseServerGroup.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this BaseServerGroup.

        服务器组关联的镜像ID，用于创建对应组下的云服务器

        :param image_id: The image_id of this BaseServerGroup.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def os_type(self):
        """Gets the os_type of this BaseServerGroup.

        :return: The os_type of this BaseServerGroup.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this BaseServerGroup.

        :param os_type: The os_type of this BaseServerGroup.
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        self._os_type = os_type

    @property
    def product_id(self):
        """Gets the product_id of this BaseServerGroup.

        产品id

        :return: The product_id of this BaseServerGroup.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this BaseServerGroup.

        产品id

        :param product_id: The product_id of this BaseServerGroup.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this BaseServerGroup.

        网卡对应的子网ID

        :return: The subnet_id of this BaseServerGroup.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this BaseServerGroup.

        网卡对应的子网ID

        :param subnet_id: The subnet_id of this BaseServerGroup.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def system_disk_type(self):
        """Gets the system_disk_type of this BaseServerGroup.

        :return: The system_disk_type of this BaseServerGroup.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
        """
        return self._system_disk_type

    @system_disk_type.setter
    def system_disk_type(self, system_disk_type):
        """Sets the system_disk_type of this BaseServerGroup.

        :param system_disk_type: The system_disk_type of this BaseServerGroup.
        :type system_disk_type: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
        """
        self._system_disk_type = system_disk_type

    @property
    def system_disk_size(self):
        """Gets the system_disk_size of this BaseServerGroup.

        磁盘容量，单位GB

        :return: The system_disk_size of this BaseServerGroup.
        :rtype: int
        """
        return self._system_disk_size

    @system_disk_size.setter
    def system_disk_size(self, system_disk_size):
        """Sets the system_disk_size of this BaseServerGroup.

        磁盘容量，单位GB

        :param system_disk_size: The system_disk_size of this BaseServerGroup.
        :type system_disk_size: int
        """
        self._system_disk_size = system_disk_size

    @property
    def is_vdi(self):
        """Gets the is_vdi of this BaseServerGroup.

        是否为vdi单会话模式

        :return: The is_vdi of this BaseServerGroup.
        :rtype: bool
        """
        return self._is_vdi

    @is_vdi.setter
    def is_vdi(self, is_vdi):
        """Sets the is_vdi of this BaseServerGroup.

        是否为vdi单会话模式

        :param is_vdi: The is_vdi of this BaseServerGroup.
        :type is_vdi: bool
        """
        self._is_vdi = is_vdi

    @property
    def extra_session_type(self):
        """Gets the extra_session_type of this BaseServerGroup.

        :return: The extra_session_type of this BaseServerGroup.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ExtraSessionTypeEnum`
        """
        return self._extra_session_type

    @extra_session_type.setter
    def extra_session_type(self, extra_session_type):
        """Sets the extra_session_type of this BaseServerGroup.

        :param extra_session_type: The extra_session_type of this BaseServerGroup.
        :type extra_session_type: :class:`huaweicloudsdkworkspaceapp.v1.ExtraSessionTypeEnum`
        """
        self._extra_session_type = extra_session_type

    @property
    def extra_session_size(self):
        """Gets the extra_session_size of this BaseServerGroup.

        付费会话个数

        :return: The extra_session_size of this BaseServerGroup.
        :rtype: int
        """
        return self._extra_session_size

    @extra_session_size.setter
    def extra_session_size(self, extra_session_size):
        """Sets the extra_session_size of this BaseServerGroup.

        付费会话个数

        :param extra_session_size: The extra_session_size of this BaseServerGroup.
        :type extra_session_size: int
        """
        self._extra_session_size = extra_session_size

    @property
    def app_type(self):
        """Gets the app_type of this BaseServerGroup.

        :return: The app_type of this BaseServerGroup.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this BaseServerGroup.

        :param app_type: The app_type of this BaseServerGroup.
        :type app_type: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        self._app_type = app_type

    @property
    def create_time(self):
        """Gets the create_time of this BaseServerGroup.

        服务器组创建时间

        :return: The create_time of this BaseServerGroup.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BaseServerGroup.

        服务器组创建时间

        :param create_time: The create_time of this BaseServerGroup.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this BaseServerGroup.

        服务器组更新时间

        :return: The update_time of this BaseServerGroup.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this BaseServerGroup.

        服务器组更新时间

        :param update_time: The update_time of this BaseServerGroup.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def storage_mount_policy(self):
        """Gets the storage_mount_policy of this BaseServerGroup.

        :return: The storage_mount_policy of this BaseServerGroup.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.StorageFolderMountType`
        """
        return self._storage_mount_policy

    @storage_mount_policy.setter
    def storage_mount_policy(self, storage_mount_policy):
        """Sets the storage_mount_policy of this BaseServerGroup.

        :param storage_mount_policy: The storage_mount_policy of this BaseServerGroup.
        :type storage_mount_policy: :class:`huaweicloudsdkworkspaceapp.v1.StorageFolderMountType`
        """
        self._storage_mount_policy = storage_mount_policy

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
        if not isinstance(other, BaseServerGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
