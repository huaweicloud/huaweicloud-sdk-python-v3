# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDesktopPoolReq:

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
        'type': 'str',
        'size': 'int',
        'description': 'str',
        'availability_zone': 'str',
        'product_id': 'str',
        'flavor_id': 'str',
        'image_type': 'str',
        'image_id': 'str',
        'root_volume': 'VolumeInfo',
        'data_volumes': 'list[VolumeInfo]',
        'vpc_id': 'str',
        'subnet_ids': 'list[str]',
        'security_groups': 'list[SecurityGroup]',
        'authorized_objects': 'list[AuthorizedObjects]',
        'ou_name': 'str',
        'tags': 'list[Tag]',
        'enterprise_project_id': 'str',
        'disconnected_retention_period': 'int',
        'enable_autoscale': 'bool',
        'autoscale_policy': 'AutoscalePolicy',
        'desktop_name_policy_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'size': 'size',
        'description': 'description',
        'availability_zone': 'availability_zone',
        'product_id': 'product_id',
        'flavor_id': 'flavor_id',
        'image_type': 'image_type',
        'image_id': 'image_id',
        'root_volume': 'root_volume',
        'data_volumes': 'data_volumes',
        'vpc_id': 'vpc_id',
        'subnet_ids': 'subnet_ids',
        'security_groups': 'security_groups',
        'authorized_objects': 'authorized_objects',
        'ou_name': 'ou_name',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'disconnected_retention_period': 'disconnected_retention_period',
        'enable_autoscale': 'enable_autoscale',
        'autoscale_policy': 'autoscale_policy',
        'desktop_name_policy_id': 'desktop_name_policy_id'
    }

    def __init__(self, name=None, type=None, size=None, description=None, availability_zone=None, product_id=None, flavor_id=None, image_type=None, image_id=None, root_volume=None, data_volumes=None, vpc_id=None, subnet_ids=None, security_groups=None, authorized_objects=None, ou_name=None, tags=None, enterprise_project_id=None, disconnected_retention_period=None, enable_autoscale=None, autoscale_policy=None, desktop_name_policy_id=None):
        r"""CreateDesktopPoolReq

        The model defined in huaweicloud sdk

        :param name: 桌面池名称，桌面池名称必须保证唯一。桌面名称只允许输入中文、大写字母、小写字母、数字、中划线，长度范围为1~255。
        :type name: str
        :param type: 桌面池类型，DYNAMIC：动态池，STATIC：静态池。
        :type type: str
        :param size: 桌面池大小：当前桌面池要创建多少台桌面。
        :type size: int
        :param description: 桌面池描述。
        :type description: str
        :param availability_zone: 可用分区。将桌面创建到指定的可用分区。如果不指定则使用系统随机的可用分区。
        :type availability_zone: str
        :param product_id: 套餐ID。
        :type product_id: str
        :param flavor_id: 产品规格ID。可用区是边缘可用区时，必填此参数。
        :type flavor_id: str
        :param image_type: 镜像类型。默认值为private。  - private：私有镜像。 - gold：公共镜像。
        :type image_type: str
        :param image_id: 镜像ID，用于私有镜像创建桌面场景，配合product_id使用。
        :type image_id: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.VolumeInfo`
        :param data_volumes: 数据盘列表。
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.VolumeInfo`]
        :param vpc_id: 创建桌面时的VPC ID。
        :type vpc_id: str
        :param subnet_ids: 创建桌面使用的子网ID。
        :type subnet_ids: list[str]
        :param security_groups: 桌面使用的安全组，如果不指定则默认使用桌面代理中指定的安全组。
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        :param authorized_objects: 要授权的用户/用户组列表。
        :type authorized_objects: list[:class:`huaweicloudsdkworkspace.v2.AuthorizedObjects`]
        :param ou_name: OU名称，在对接AD时使用，需提前在AD中创建OU。
        :type ou_name: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        :param enterprise_project_id: 企业项目ID，默认\&quot;0。\&quot;
        :type enterprise_project_id: str
        :param disconnected_retention_period: 动态池桌面断连多少分钟内，保留用户与桌面的绑定关系，超时后自动解绑。
        :type disconnected_retention_period: int
        :param enable_autoscale: 桌面池是否开启弹性伸缩类型，为false则表示不开启弹性伸缩，为true则表示开启弹性伸缩。
        :type enable_autoscale: bool
        :param autoscale_policy: 
        :type autoscale_policy: :class:`huaweicloudsdkworkspace.v2.AutoscalePolicy`
        :param desktop_name_policy_id: 策略id，用于指定生成桌面名称策略。
        :type desktop_name_policy_id: str
        """
        
        

        self._name = None
        self._type = None
        self._size = None
        self._description = None
        self._availability_zone = None
        self._product_id = None
        self._flavor_id = None
        self._image_type = None
        self._image_id = None
        self._root_volume = None
        self._data_volumes = None
        self._vpc_id = None
        self._subnet_ids = None
        self._security_groups = None
        self._authorized_objects = None
        self._ou_name = None
        self._tags = None
        self._enterprise_project_id = None
        self._disconnected_retention_period = None
        self._enable_autoscale = None
        self._autoscale_policy = None
        self._desktop_name_policy_id = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.size = size
        if description is not None:
            self.description = description
        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.product_id = product_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        self.image_type = image_type
        self.image_id = image_id
        self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if vpc_id is not None:
            self.vpc_id = vpc_id
        self.subnet_ids = subnet_ids
        if security_groups is not None:
            self.security_groups = security_groups
        if authorized_objects is not None:
            self.authorized_objects = authorized_objects
        if ou_name is not None:
            self.ou_name = ou_name
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if disconnected_retention_period is not None:
            self.disconnected_retention_period = disconnected_retention_period
        if enable_autoscale is not None:
            self.enable_autoscale = enable_autoscale
        if autoscale_policy is not None:
            self.autoscale_policy = autoscale_policy
        if desktop_name_policy_id is not None:
            self.desktop_name_policy_id = desktop_name_policy_id

    @property
    def name(self):
        r"""Gets the name of this CreateDesktopPoolReq.

        桌面池名称，桌面池名称必须保证唯一。桌面名称只允许输入中文、大写字母、小写字母、数字、中划线，长度范围为1~255。

        :return: The name of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDesktopPoolReq.

        桌面池名称，桌面池名称必须保证唯一。桌面名称只允许输入中文、大写字母、小写字母、数字、中划线，长度范围为1~255。

        :param name: The name of this CreateDesktopPoolReq.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CreateDesktopPoolReq.

        桌面池类型，DYNAMIC：动态池，STATIC：静态池。

        :return: The type of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateDesktopPoolReq.

        桌面池类型，DYNAMIC：动态池，STATIC：静态池。

        :param type: The type of this CreateDesktopPoolReq.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this CreateDesktopPoolReq.

        桌面池大小：当前桌面池要创建多少台桌面。

        :return: The size of this CreateDesktopPoolReq.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this CreateDesktopPoolReq.

        桌面池大小：当前桌面池要创建多少台桌面。

        :param size: The size of this CreateDesktopPoolReq.
        :type size: int
        """
        self._size = size

    @property
    def description(self):
        r"""Gets the description of this CreateDesktopPoolReq.

        桌面池描述。

        :return: The description of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDesktopPoolReq.

        桌面池描述。

        :param description: The description of this CreateDesktopPoolReq.
        :type description: str
        """
        self._description = description

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateDesktopPoolReq.

        可用分区。将桌面创建到指定的可用分区。如果不指定则使用系统随机的可用分区。

        :return: The availability_zone of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateDesktopPoolReq.

        可用分区。将桌面创建到指定的可用分区。如果不指定则使用系统随机的可用分区。

        :param availability_zone: The availability_zone of this CreateDesktopPoolReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateDesktopPoolReq.

        套餐ID。

        :return: The product_id of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateDesktopPoolReq.

        套餐ID。

        :param product_id: The product_id of this CreateDesktopPoolReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this CreateDesktopPoolReq.

        产品规格ID。可用区是边缘可用区时，必填此参数。

        :return: The flavor_id of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this CreateDesktopPoolReq.

        产品规格ID。可用区是边缘可用区时，必填此参数。

        :param flavor_id: The flavor_id of this CreateDesktopPoolReq.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def image_type(self):
        r"""Gets the image_type of this CreateDesktopPoolReq.

        镜像类型。默认值为private。  - private：私有镜像。 - gold：公共镜像。

        :return: The image_type of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this CreateDesktopPoolReq.

        镜像类型。默认值为private。  - private：私有镜像。 - gold：公共镜像。

        :param image_type: The image_type of this CreateDesktopPoolReq.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_id(self):
        r"""Gets the image_id of this CreateDesktopPoolReq.

        镜像ID，用于私有镜像创建桌面场景，配合product_id使用。

        :return: The image_id of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this CreateDesktopPoolReq.

        镜像ID，用于私有镜像创建桌面场景，配合product_id使用。

        :param image_id: The image_id of this CreateDesktopPoolReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def root_volume(self):
        r"""Gets the root_volume of this CreateDesktopPoolReq.

        :return: The root_volume of this CreateDesktopPoolReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.VolumeInfo`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this CreateDesktopPoolReq.

        :param root_volume: The root_volume of this CreateDesktopPoolReq.
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.VolumeInfo`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this CreateDesktopPoolReq.

        数据盘列表。

        :return: The data_volumes of this CreateDesktopPoolReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.VolumeInfo`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this CreateDesktopPoolReq.

        数据盘列表。

        :param data_volumes: The data_volumes of this CreateDesktopPoolReq.
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.VolumeInfo`]
        """
        self._data_volumes = data_volumes

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateDesktopPoolReq.

        创建桌面时的VPC ID。

        :return: The vpc_id of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateDesktopPoolReq.

        创建桌面时的VPC ID。

        :param vpc_id: The vpc_id of this CreateDesktopPoolReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_ids(self):
        r"""Gets the subnet_ids of this CreateDesktopPoolReq.

        创建桌面使用的子网ID。

        :return: The subnet_ids of this CreateDesktopPoolReq.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        r"""Sets the subnet_ids of this CreateDesktopPoolReq.

        创建桌面使用的子网ID。

        :param subnet_ids: The subnet_ids of this CreateDesktopPoolReq.
        :type subnet_ids: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def security_groups(self):
        r"""Gets the security_groups of this CreateDesktopPoolReq.

        桌面使用的安全组，如果不指定则默认使用桌面代理中指定的安全组。

        :return: The security_groups of this CreateDesktopPoolReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this CreateDesktopPoolReq.

        桌面使用的安全组，如果不指定则默认使用桌面代理中指定的安全组。

        :param security_groups: The security_groups of this CreateDesktopPoolReq.
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def authorized_objects(self):
        r"""Gets the authorized_objects of this CreateDesktopPoolReq.

        要授权的用户/用户组列表。

        :return: The authorized_objects of this CreateDesktopPoolReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AuthorizedObjects`]
        """
        return self._authorized_objects

    @authorized_objects.setter
    def authorized_objects(self, authorized_objects):
        r"""Sets the authorized_objects of this CreateDesktopPoolReq.

        要授权的用户/用户组列表。

        :param authorized_objects: The authorized_objects of this CreateDesktopPoolReq.
        :type authorized_objects: list[:class:`huaweicloudsdkworkspace.v2.AuthorizedObjects`]
        """
        self._authorized_objects = authorized_objects

    @property
    def ou_name(self):
        r"""Gets the ou_name of this CreateDesktopPoolReq.

        OU名称，在对接AD时使用，需提前在AD中创建OU。

        :return: The ou_name of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        r"""Sets the ou_name of this CreateDesktopPoolReq.

        OU名称，在对接AD时使用，需提前在AD中创建OU。

        :param ou_name: The ou_name of this CreateDesktopPoolReq.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def tags(self):
        r"""Gets the tags of this CreateDesktopPoolReq.

        标签列表。

        :return: The tags of this CreateDesktopPoolReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateDesktopPoolReq.

        标签列表。

        :param tags: The tags of this CreateDesktopPoolReq.
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateDesktopPoolReq.

        企业项目ID，默认\"0。\"

        :return: The enterprise_project_id of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateDesktopPoolReq.

        企业项目ID，默认\"0。\"

        :param enterprise_project_id: The enterprise_project_id of this CreateDesktopPoolReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def disconnected_retention_period(self):
        r"""Gets the disconnected_retention_period of this CreateDesktopPoolReq.

        动态池桌面断连多少分钟内，保留用户与桌面的绑定关系，超时后自动解绑。

        :return: The disconnected_retention_period of this CreateDesktopPoolReq.
        :rtype: int
        """
        return self._disconnected_retention_period

    @disconnected_retention_period.setter
    def disconnected_retention_period(self, disconnected_retention_period):
        r"""Sets the disconnected_retention_period of this CreateDesktopPoolReq.

        动态池桌面断连多少分钟内，保留用户与桌面的绑定关系，超时后自动解绑。

        :param disconnected_retention_period: The disconnected_retention_period of this CreateDesktopPoolReq.
        :type disconnected_retention_period: int
        """
        self._disconnected_retention_period = disconnected_retention_period

    @property
    def enable_autoscale(self):
        r"""Gets the enable_autoscale of this CreateDesktopPoolReq.

        桌面池是否开启弹性伸缩类型，为false则表示不开启弹性伸缩，为true则表示开启弹性伸缩。

        :return: The enable_autoscale of this CreateDesktopPoolReq.
        :rtype: bool
        """
        return self._enable_autoscale

    @enable_autoscale.setter
    def enable_autoscale(self, enable_autoscale):
        r"""Sets the enable_autoscale of this CreateDesktopPoolReq.

        桌面池是否开启弹性伸缩类型，为false则表示不开启弹性伸缩，为true则表示开启弹性伸缩。

        :param enable_autoscale: The enable_autoscale of this CreateDesktopPoolReq.
        :type enable_autoscale: bool
        """
        self._enable_autoscale = enable_autoscale

    @property
    def autoscale_policy(self):
        r"""Gets the autoscale_policy of this CreateDesktopPoolReq.

        :return: The autoscale_policy of this CreateDesktopPoolReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AutoscalePolicy`
        """
        return self._autoscale_policy

    @autoscale_policy.setter
    def autoscale_policy(self, autoscale_policy):
        r"""Sets the autoscale_policy of this CreateDesktopPoolReq.

        :param autoscale_policy: The autoscale_policy of this CreateDesktopPoolReq.
        :type autoscale_policy: :class:`huaweicloudsdkworkspace.v2.AutoscalePolicy`
        """
        self._autoscale_policy = autoscale_policy

    @property
    def desktop_name_policy_id(self):
        r"""Gets the desktop_name_policy_id of this CreateDesktopPoolReq.

        策略id，用于指定生成桌面名称策略。

        :return: The desktop_name_policy_id of this CreateDesktopPoolReq.
        :rtype: str
        """
        return self._desktop_name_policy_id

    @desktop_name_policy_id.setter
    def desktop_name_policy_id(self, desktop_name_policy_id):
        r"""Sets the desktop_name_policy_id of this CreateDesktopPoolReq.

        策略id，用于指定生成桌面名称策略。

        :param desktop_name_policy_id: The desktop_name_policy_id of this CreateDesktopPoolReq.
        :type desktop_name_policy_id: str
        """
        self._desktop_name_policy_id = desktop_name_policy_id

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
        if not isinstance(other, CreateDesktopPoolReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
