# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateImageServerReq:

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
        'root_volume': 'Volume',
        'image_ref': 'ImageRef',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'product_id': 'str',
        'flavor_id': 'str',
        'availability_zone': 'str',
        'attach_apps': 'list[str]',
        'authorize_accounts': 'list[ImageAccountInfo]',
        'ou_name': 'str',
        'is_vdi': 'bool',
        'scheduler_hints': 'WdhParam',
        'extra_session_type': 'ExtraSessionTypeEnum',
        'extra_session_size': 'int',
        'route_policy': 'RoutePolicy',
        'tags': 'list[TmsTag]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'root_volume': 'root_volume',
        'image_ref': 'image_ref',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'product_id': 'product_id',
        'flavor_id': 'flavor_id',
        'availability_zone': 'availability_zone',
        'attach_apps': 'attach_apps',
        'authorize_accounts': 'authorize_accounts',
        'ou_name': 'ou_name',
        'is_vdi': 'is_vdi',
        'scheduler_hints': 'scheduler_hints',
        'extra_session_type': 'extra_session_type',
        'extra_session_size': 'extra_session_size',
        'route_policy': 'route_policy',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, description=None, root_volume=None, image_ref=None, vpc_id=None, subnet_id=None, product_id=None, flavor_id=None, availability_zone=None, attach_apps=None, authorize_accounts=None, ou_name=None, is_vdi=None, scheduler_hints=None, extra_session_type=None, extra_session_size=None, route_policy=None, tags=None, enterprise_project_id=None):
        """CreateImageServerReq

        The model defined in huaweicloud sdk

        :param name: 镜像实例名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成，不能有空格 2. 长度范围1~64个字符
        :type name: str
        :param description: 镜像实例描述
        :type description: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkworkspaceapp.v1.Volume`
        :param image_ref: 
        :type image_ref: :class:`huaweicloudsdkworkspaceapp.v1.ImageRef`
        :param vpc_id: 镜像实例所属虚拟私有云唯一标识。
        :type vpc_id: str
        :param subnet_id: 镜像实例网卡对应的子网唯一标识
        :type subnet_id: str
        :param product_id: 镜像实例产品套餐ID
        :type product_id: str
        :param flavor_id: 规格ID。
        :type flavor_id: str
        :param availability_zone: 镜像实例的可用区，空值表示随机选取可用区
        :type availability_zone: str
        :param attach_apps: 云应用仓库软件唯一标识请求列表
        :type attach_apps: list[str]
        :param authorize_accounts: 应用组授权用户， * 限制用户类型：&#39;USER&#39; - 用户
        :type authorize_accounts: list[:class:`huaweicloudsdkworkspaceapp.v1.ImageAccountInfo`]
        :param ou_name: 组织名称
        :type ou_name: str
        :param is_vdi: 是否为vdi单会话模式
        :type is_vdi: bool
        :param scheduler_hints: 
        :type scheduler_hints: :class:`huaweicloudsdkworkspaceapp.v1.WdhParam`
        :param extra_session_type: 
        :type extra_session_type: :class:`huaweicloudsdkworkspaceapp.v1.ExtraSessionTypeEnum`
        :param extra_session_size: 需要付费的会话数，单位/个
        :type extra_session_size: int
        :param route_policy: 
        :type route_policy: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        :param tags: 标签信息，最多包含20个key,不允许重复
        :type tags: list[:class:`huaweicloudsdkworkspaceapp.v1.TmsTag`]
        :param enterprise_project_id: **⚠ : 此属性是预留字段，不需要传值，目前镜像产物默认属于default企业项目** 镜像所属的企业项目ID，默认属于default企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参考“[企业中心总览](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)”。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._description = None
        self._root_volume = None
        self._image_ref = None
        self._vpc_id = None
        self._subnet_id = None
        self._product_id = None
        self._flavor_id = None
        self._availability_zone = None
        self._attach_apps = None
        self._authorize_accounts = None
        self._ou_name = None
        self._is_vdi = None
        self._scheduler_hints = None
        self._extra_session_type = None
        self._extra_session_size = None
        self._route_policy = None
        self._tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.root_volume = root_volume
        self.image_ref = image_ref
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.product_id = product_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if attach_apps is not None:
            self.attach_apps = attach_apps
        self.authorize_accounts = authorize_accounts
        if ou_name is not None:
            self.ou_name = ou_name
        if is_vdi is not None:
            self.is_vdi = is_vdi
        if scheduler_hints is not None:
            self.scheduler_hints = scheduler_hints
        if extra_session_type is not None:
            self.extra_session_type = extra_session_type
        if extra_session_size is not None:
            self.extra_session_size = extra_session_size
        if route_policy is not None:
            self.route_policy = route_policy
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this CreateImageServerReq.

        镜像实例名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成，不能有空格 2. 长度范围1~64个字符

        :return: The name of this CreateImageServerReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateImageServerReq.

        镜像实例名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成，不能有空格 2. 长度范围1~64个字符

        :param name: The name of this CreateImageServerReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateImageServerReq.

        镜像实例描述

        :return: The description of this CreateImageServerReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateImageServerReq.

        镜像实例描述

        :param description: The description of this CreateImageServerReq.
        :type description: str
        """
        self._description = description

    @property
    def root_volume(self):
        """Gets the root_volume of this CreateImageServerReq.

        :return: The root_volume of this CreateImageServerReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Volume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this CreateImageServerReq.

        :param root_volume: The root_volume of this CreateImageServerReq.
        :type root_volume: :class:`huaweicloudsdkworkspaceapp.v1.Volume`
        """
        self._root_volume = root_volume

    @property
    def image_ref(self):
        """Gets the image_ref of this CreateImageServerReq.

        :return: The image_ref of this CreateImageServerReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ImageRef`
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this CreateImageServerReq.

        :param image_ref: The image_ref of this CreateImageServerReq.
        :type image_ref: :class:`huaweicloudsdkworkspaceapp.v1.ImageRef`
        """
        self._image_ref = image_ref

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateImageServerReq.

        镜像实例所属虚拟私有云唯一标识。

        :return: The vpc_id of this CreateImageServerReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateImageServerReq.

        镜像实例所属虚拟私有云唯一标识。

        :param vpc_id: The vpc_id of this CreateImageServerReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateImageServerReq.

        镜像实例网卡对应的子网唯一标识

        :return: The subnet_id of this CreateImageServerReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateImageServerReq.

        镜像实例网卡对应的子网唯一标识

        :param subnet_id: The subnet_id of this CreateImageServerReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def product_id(self):
        """Gets the product_id of this CreateImageServerReq.

        镜像实例产品套餐ID

        :return: The product_id of this CreateImageServerReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateImageServerReq.

        镜像实例产品套餐ID

        :param product_id: The product_id of this CreateImageServerReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def flavor_id(self):
        """Gets the flavor_id of this CreateImageServerReq.

        规格ID。

        :return: The flavor_id of this CreateImageServerReq.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this CreateImageServerReq.

        规格ID。

        :param flavor_id: The flavor_id of this CreateImageServerReq.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateImageServerReq.

        镜像实例的可用区，空值表示随机选取可用区

        :return: The availability_zone of this CreateImageServerReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateImageServerReq.

        镜像实例的可用区，空值表示随机选取可用区

        :param availability_zone: The availability_zone of this CreateImageServerReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def attach_apps(self):
        """Gets the attach_apps of this CreateImageServerReq.

        云应用仓库软件唯一标识请求列表

        :return: The attach_apps of this CreateImageServerReq.
        :rtype: list[str]
        """
        return self._attach_apps

    @attach_apps.setter
    def attach_apps(self, attach_apps):
        """Sets the attach_apps of this CreateImageServerReq.

        云应用仓库软件唯一标识请求列表

        :param attach_apps: The attach_apps of this CreateImageServerReq.
        :type attach_apps: list[str]
        """
        self._attach_apps = attach_apps

    @property
    def authorize_accounts(self):
        """Gets the authorize_accounts of this CreateImageServerReq.

        应用组授权用户， * 限制用户类型：'USER' - 用户

        :return: The authorize_accounts of this CreateImageServerReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.ImageAccountInfo`]
        """
        return self._authorize_accounts

    @authorize_accounts.setter
    def authorize_accounts(self, authorize_accounts):
        """Sets the authorize_accounts of this CreateImageServerReq.

        应用组授权用户， * 限制用户类型：'USER' - 用户

        :param authorize_accounts: The authorize_accounts of this CreateImageServerReq.
        :type authorize_accounts: list[:class:`huaweicloudsdkworkspaceapp.v1.ImageAccountInfo`]
        """
        self._authorize_accounts = authorize_accounts

    @property
    def ou_name(self):
        """Gets the ou_name of this CreateImageServerReq.

        组织名称

        :return: The ou_name of this CreateImageServerReq.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        """Sets the ou_name of this CreateImageServerReq.

        组织名称

        :param ou_name: The ou_name of this CreateImageServerReq.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def is_vdi(self):
        """Gets the is_vdi of this CreateImageServerReq.

        是否为vdi单会话模式

        :return: The is_vdi of this CreateImageServerReq.
        :rtype: bool
        """
        return self._is_vdi

    @is_vdi.setter
    def is_vdi(self, is_vdi):
        """Sets the is_vdi of this CreateImageServerReq.

        是否为vdi单会话模式

        :param is_vdi: The is_vdi of this CreateImageServerReq.
        :type is_vdi: bool
        """
        self._is_vdi = is_vdi

    @property
    def scheduler_hints(self):
        """Gets the scheduler_hints of this CreateImageServerReq.

        :return: The scheduler_hints of this CreateImageServerReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.WdhParam`
        """
        return self._scheduler_hints

    @scheduler_hints.setter
    def scheduler_hints(self, scheduler_hints):
        """Sets the scheduler_hints of this CreateImageServerReq.

        :param scheduler_hints: The scheduler_hints of this CreateImageServerReq.
        :type scheduler_hints: :class:`huaweicloudsdkworkspaceapp.v1.WdhParam`
        """
        self._scheduler_hints = scheduler_hints

    @property
    def extra_session_type(self):
        """Gets the extra_session_type of this CreateImageServerReq.

        :return: The extra_session_type of this CreateImageServerReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ExtraSessionTypeEnum`
        """
        return self._extra_session_type

    @extra_session_type.setter
    def extra_session_type(self, extra_session_type):
        """Sets the extra_session_type of this CreateImageServerReq.

        :param extra_session_type: The extra_session_type of this CreateImageServerReq.
        :type extra_session_type: :class:`huaweicloudsdkworkspaceapp.v1.ExtraSessionTypeEnum`
        """
        self._extra_session_type = extra_session_type

    @property
    def extra_session_size(self):
        """Gets the extra_session_size of this CreateImageServerReq.

        需要付费的会话数，单位/个

        :return: The extra_session_size of this CreateImageServerReq.
        :rtype: int
        """
        return self._extra_session_size

    @extra_session_size.setter
    def extra_session_size(self, extra_session_size):
        """Sets the extra_session_size of this CreateImageServerReq.

        需要付费的会话数，单位/个

        :param extra_session_size: The extra_session_size of this CreateImageServerReq.
        :type extra_session_size: int
        """
        self._extra_session_size = extra_session_size

    @property
    def route_policy(self):
        """Gets the route_policy of this CreateImageServerReq.

        :return: The route_policy of this CreateImageServerReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        """
        return self._route_policy

    @route_policy.setter
    def route_policy(self, route_policy):
        """Sets the route_policy of this CreateImageServerReq.

        :param route_policy: The route_policy of this CreateImageServerReq.
        :type route_policy: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        """
        self._route_policy = route_policy

    @property
    def tags(self):
        """Gets the tags of this CreateImageServerReq.

        标签信息，最多包含20个key,不允许重复

        :return: The tags of this CreateImageServerReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.TmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateImageServerReq.

        标签信息，最多包含20个key,不允许重复

        :param tags: The tags of this CreateImageServerReq.
        :type tags: list[:class:`huaweicloudsdkworkspaceapp.v1.TmsTag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateImageServerReq.

        **⚠ : 此属性是预留字段，不需要传值，目前镜像产物默认属于default企业项目** 镜像所属的企业项目ID，默认属于default企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参考“[企业中心总览](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)”。

        :return: The enterprise_project_id of this CreateImageServerReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateImageServerReq.

        **⚠ : 此属性是预留字段，不需要传值，目前镜像产物默认属于default企业项目** 镜像所属的企业项目ID，默认属于default企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参考“[企业中心总览](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)”。

        :param enterprise_project_id: The enterprise_project_id of this CreateImageServerReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateImageServerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
