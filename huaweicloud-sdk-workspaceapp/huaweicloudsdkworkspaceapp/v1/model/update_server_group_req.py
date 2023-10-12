# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerGroupReq:

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
        'description': 'str',
        'route_policy': 'RoutePolicy',
        'storage_mount_policy': 'StorageFolderMountType',
        'image_id': 'str',
        'image_product_id': 'str',
        'image_type': 'ImageTypeEnum',
        'system_disk_type': 'VolumeType',
        'system_disk_size': 'int',
        'ou_name': 'str',
        'app_type': 'AppTypeEnum'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'route_policy': 'route_policy',
        'storage_mount_policy': 'storage_mount_policy',
        'image_id': 'image_id',
        'image_product_id': 'image_product_id',
        'image_type': 'image_type',
        'system_disk_type': 'system_disk_type',
        'system_disk_size': 'system_disk_size',
        'ou_name': 'ou_name',
        'app_type': 'app_type'
    }

    def __init__(self, name=None, description=None, route_policy=None, storage_mount_policy=None, image_id=None, image_product_id=None, image_type=None, system_disk_type=None, system_disk_size=None, ou_name=None, app_type=None):
        """UpdateServerGroupReq

        The model defined in huaweicloud sdk

        :param name: 服务器组名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-空格组成，不能全为空格, 首位不为空 2. 长度范围1~64个字符
        :type name: str
        :param description: 服务器组描述
        :type description: str
        :param route_policy: 
        :type route_policy: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        :param storage_mount_policy: 
        :type storage_mount_policy: :class:`huaweicloudsdkworkspaceapp.v1.StorageFolderMountType`
        :param image_id: 服务器组关联的镜像ID，更新镜像ID只对组下新创建的云服务器生效
        :type image_id: str
        :param image_product_id: 服务器组的镜像的productId
        :type image_product_id: str
        :param image_type: 
        :type image_type: :class:`huaweicloudsdkworkspaceapp.v1.ImageTypeEnum`
        :param system_disk_type: 
        :type system_disk_type: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
        :param system_disk_size: 磁盘容量，单位GB
        :type system_disk_size: int
        :param ou_name: 默认组织名称
        :type ou_name: str
        :param app_type: 
        :type app_type: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        
        

        self._name = None
        self._description = None
        self._route_policy = None
        self._storage_mount_policy = None
        self._image_id = None
        self._image_product_id = None
        self._image_type = None
        self._system_disk_type = None
        self._system_disk_size = None
        self._ou_name = None
        self._app_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if route_policy is not None:
            self.route_policy = route_policy
        if storage_mount_policy is not None:
            self.storage_mount_policy = storage_mount_policy
        if image_id is not None:
            self.image_id = image_id
        if image_product_id is not None:
            self.image_product_id = image_product_id
        if image_type is not None:
            self.image_type = image_type
        if system_disk_type is not None:
            self.system_disk_type = system_disk_type
        if system_disk_size is not None:
            self.system_disk_size = system_disk_size
        if ou_name is not None:
            self.ou_name = ou_name
        if app_type is not None:
            self.app_type = app_type

    @property
    def name(self):
        """Gets the name of this UpdateServerGroupReq.

        服务器组名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-空格组成，不能全为空格, 首位不为空 2. 长度范围1~64个字符

        :return: The name of this UpdateServerGroupReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateServerGroupReq.

        服务器组名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-空格组成，不能全为空格, 首位不为空 2. 长度范围1~64个字符

        :param name: The name of this UpdateServerGroupReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateServerGroupReq.

        服务器组描述

        :return: The description of this UpdateServerGroupReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateServerGroupReq.

        服务器组描述

        :param description: The description of this UpdateServerGroupReq.
        :type description: str
        """
        self._description = description

    @property
    def route_policy(self):
        """Gets the route_policy of this UpdateServerGroupReq.

        :return: The route_policy of this UpdateServerGroupReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        """
        return self._route_policy

    @route_policy.setter
    def route_policy(self, route_policy):
        """Sets the route_policy of this UpdateServerGroupReq.

        :param route_policy: The route_policy of this UpdateServerGroupReq.
        :type route_policy: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        """
        self._route_policy = route_policy

    @property
    def storage_mount_policy(self):
        """Gets the storage_mount_policy of this UpdateServerGroupReq.

        :return: The storage_mount_policy of this UpdateServerGroupReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.StorageFolderMountType`
        """
        return self._storage_mount_policy

    @storage_mount_policy.setter
    def storage_mount_policy(self, storage_mount_policy):
        """Sets the storage_mount_policy of this UpdateServerGroupReq.

        :param storage_mount_policy: The storage_mount_policy of this UpdateServerGroupReq.
        :type storage_mount_policy: :class:`huaweicloudsdkworkspaceapp.v1.StorageFolderMountType`
        """
        self._storage_mount_policy = storage_mount_policy

    @property
    def image_id(self):
        """Gets the image_id of this UpdateServerGroupReq.

        服务器组关联的镜像ID，更新镜像ID只对组下新创建的云服务器生效

        :return: The image_id of this UpdateServerGroupReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this UpdateServerGroupReq.

        服务器组关联的镜像ID，更新镜像ID只对组下新创建的云服务器生效

        :param image_id: The image_id of this UpdateServerGroupReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_product_id(self):
        """Gets the image_product_id of this UpdateServerGroupReq.

        服务器组的镜像的productId

        :return: The image_product_id of this UpdateServerGroupReq.
        :rtype: str
        """
        return self._image_product_id

    @image_product_id.setter
    def image_product_id(self, image_product_id):
        """Sets the image_product_id of this UpdateServerGroupReq.

        服务器组的镜像的productId

        :param image_product_id: The image_product_id of this UpdateServerGroupReq.
        :type image_product_id: str
        """
        self._image_product_id = image_product_id

    @property
    def image_type(self):
        """Gets the image_type of this UpdateServerGroupReq.

        :return: The image_type of this UpdateServerGroupReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ImageTypeEnum`
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this UpdateServerGroupReq.

        :param image_type: The image_type of this UpdateServerGroupReq.
        :type image_type: :class:`huaweicloudsdkworkspaceapp.v1.ImageTypeEnum`
        """
        self._image_type = image_type

    @property
    def system_disk_type(self):
        """Gets the system_disk_type of this UpdateServerGroupReq.

        :return: The system_disk_type of this UpdateServerGroupReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
        """
        return self._system_disk_type

    @system_disk_type.setter
    def system_disk_type(self, system_disk_type):
        """Sets the system_disk_type of this UpdateServerGroupReq.

        :param system_disk_type: The system_disk_type of this UpdateServerGroupReq.
        :type system_disk_type: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
        """
        self._system_disk_type = system_disk_type

    @property
    def system_disk_size(self):
        """Gets the system_disk_size of this UpdateServerGroupReq.

        磁盘容量，单位GB

        :return: The system_disk_size of this UpdateServerGroupReq.
        :rtype: int
        """
        return self._system_disk_size

    @system_disk_size.setter
    def system_disk_size(self, system_disk_size):
        """Sets the system_disk_size of this UpdateServerGroupReq.

        磁盘容量，单位GB

        :param system_disk_size: The system_disk_size of this UpdateServerGroupReq.
        :type system_disk_size: int
        """
        self._system_disk_size = system_disk_size

    @property
    def ou_name(self):
        """Gets the ou_name of this UpdateServerGroupReq.

        默认组织名称

        :return: The ou_name of this UpdateServerGroupReq.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        """Sets the ou_name of this UpdateServerGroupReq.

        默认组织名称

        :param ou_name: The ou_name of this UpdateServerGroupReq.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def app_type(self):
        """Gets the app_type of this UpdateServerGroupReq.

        :return: The app_type of this UpdateServerGroupReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this UpdateServerGroupReq.

        :param app_type: The app_type of this UpdateServerGroupReq.
        :type app_type: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        self._app_type = app_type

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
        if not isinstance(other, UpdateServerGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
