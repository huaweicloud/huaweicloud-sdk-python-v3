# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingGroups:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_group_name': 'str',
        'scaling_group_id': 'str',
        'scaling_group_status': 'str',
        'scaling_configuration_id': 'str',
        'scaling_configuration_name': 'str',
        'current_instance_number': 'int',
        'desire_instance_number': 'int',
        'min_instance_number': 'int',
        'max_instance_number': 'int',
        'cool_down_time': 'int',
        'lb_listener_id': 'str',
        'lbaas_listeners': 'list[LbaasListenersResult]',
        'available_zones': 'list[str]',
        'networks': 'list[NetworksResult]',
        'security_groups': 'list[SecurityGroupsResult]',
        'create_time': 'datetime',
        'vpc_id': 'str',
        'detail': 'str',
        'is_scaling': 'bool',
        'health_periodic_audit_method': 'str',
        'health_periodic_audit_time': 'int',
        'health_periodic_audit_grace_period': 'int',
        'instance_terminate_policy': 'str',
        'notifications': 'list[str]',
        'delete_publicip': 'bool',
        'delete_volume': 'bool',
        'cloud_location_id': 'str',
        'enterprise_project_id': 'str',
        'activity_type': 'str',
        'multi_az_priority_policy': 'str',
        'iam_agency_name': 'str',
        'description': 'str',
        'tags': 'list[TagsSingleValue]'
    }

    attribute_map = {
        'scaling_group_name': 'scaling_group_name',
        'scaling_group_id': 'scaling_group_id',
        'scaling_group_status': 'scaling_group_status',
        'scaling_configuration_id': 'scaling_configuration_id',
        'scaling_configuration_name': 'scaling_configuration_name',
        'current_instance_number': 'current_instance_number',
        'desire_instance_number': 'desire_instance_number',
        'min_instance_number': 'min_instance_number',
        'max_instance_number': 'max_instance_number',
        'cool_down_time': 'cool_down_time',
        'lb_listener_id': 'lb_listener_id',
        'lbaas_listeners': 'lbaas_listeners',
        'available_zones': 'available_zones',
        'networks': 'networks',
        'security_groups': 'security_groups',
        'create_time': 'create_time',
        'vpc_id': 'vpc_id',
        'detail': 'detail',
        'is_scaling': 'is_scaling',
        'health_periodic_audit_method': 'health_periodic_audit_method',
        'health_periodic_audit_time': 'health_periodic_audit_time',
        'health_periodic_audit_grace_period': 'health_periodic_audit_grace_period',
        'instance_terminate_policy': 'instance_terminate_policy',
        'notifications': 'notifications',
        'delete_publicip': 'delete_publicip',
        'delete_volume': 'delete_volume',
        'cloud_location_id': 'cloud_location_id',
        'enterprise_project_id': 'enterprise_project_id',
        'activity_type': 'activity_type',
        'multi_az_priority_policy': 'multi_az_priority_policy',
        'iam_agency_name': 'iam_agency_name',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, scaling_group_name=None, scaling_group_id=None, scaling_group_status=None, scaling_configuration_id=None, scaling_configuration_name=None, current_instance_number=None, desire_instance_number=None, min_instance_number=None, max_instance_number=None, cool_down_time=None, lb_listener_id=None, lbaas_listeners=None, available_zones=None, networks=None, security_groups=None, create_time=None, vpc_id=None, detail=None, is_scaling=None, health_periodic_audit_method=None, health_periodic_audit_time=None, health_periodic_audit_grace_period=None, instance_terminate_policy=None, notifications=None, delete_publicip=None, delete_volume=None, cloud_location_id=None, enterprise_project_id=None, activity_type=None, multi_az_priority_policy=None, iam_agency_name=None, description=None, tags=None):
        """ScalingGroups

        The model defined in huaweicloud sdk

        :param scaling_group_name: 伸缩组名称。
        :type scaling_group_name: str
        :param scaling_group_id: 伸缩组ID。
        :type scaling_group_id: str
        :param scaling_group_status: 伸缩组状态。
        :type scaling_group_status: str
        :param scaling_configuration_id: 伸缩配置ID。
        :type scaling_configuration_id: str
        :param scaling_configuration_name: 伸缩配置名称。
        :type scaling_configuration_name: str
        :param current_instance_number: 伸缩组中当前实例数。
        :type current_instance_number: int
        :param desire_instance_number: 伸缩组期望实例数。
        :type desire_instance_number: int
        :param min_instance_number: 伸缩组最小实例数。
        :type min_instance_number: int
        :param max_instance_number: 伸缩组最大实例数
        :type max_instance_number: int
        :param cool_down_time: 冷却时间，单位是秒。
        :type cool_down_time: int
        :param lb_listener_id: 经典型负载均衡监听器ID，多个负载均衡监听器ID以逗号分隔。
        :type lb_listener_id: str
        :param lbaas_listeners: 增强型负载均衡器信息，该参数为预留字段。
        :type lbaas_listeners: list[:class:`huaweicloudsdkas.v1.LbaasListenersResult`]
        :param available_zones: 可用分区信息
        :type available_zones: list[str]
        :param networks: 网络信息
        :type networks: list[:class:`huaweicloudsdkas.v1.NetworksResult`]
        :param security_groups: 安全组信息
        :type security_groups: list[:class:`huaweicloudsdkas.v1.SecurityGroupsResult`]
        :param create_time: 创建伸缩组时间，遵循UTC时间。
        :type create_time: datetime
        :param vpc_id: 伸缩组所在的VPC ID。
        :type vpc_id: str
        :param detail: 伸缩组详情。
        :type detail: str
        :param is_scaling: 伸缩组伸缩标志。
        :type is_scaling: bool
        :param health_periodic_audit_method: 健康检查方式。
        :type health_periodic_audit_method: str
        :param health_periodic_audit_time: 健康检查的间隔时间。
        :type health_periodic_audit_time: int
        :param health_periodic_audit_grace_period: 健康状况检查宽限期。
        :type health_periodic_audit_grace_period: int
        :param instance_terminate_policy: 移除策略。
        :type instance_terminate_policy: str
        :param notifications: 通知方式：EMAIL为发送邮件通知。该通知方式已经被废除，建议给弹性伸缩组配置通知功能。请参考[通知](https://support.huaweicloud.com/api-as/as_06_0800.html)。
        :type notifications: list[str]
        :param delete_publicip: 删除云服务器是否删除云服务器绑定的弹性IP。
        :type delete_publicip: bool
        :param delete_volume: 删除云服务器是否删除云服务器绑定的数据盘
        :type delete_volume: bool
        :param cloud_location_id: 该参数为预留字段
        :type cloud_location_id: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param activity_type: 伸缩组活动类型
        :type activity_type: str
        :param multi_az_priority_policy: 伸缩组扩缩容时目标AZ选择的优先级策略
        :type multi_az_priority_policy: str
        :param iam_agency_name: 委托的名称委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务的临时凭证。
        :type iam_agency_name: str
        :param description: 伸缩组描述信息
        :type description: str
        :param tags: 添加到伸缩组的标签。
        :type tags: list[:class:`huaweicloudsdkas.v1.TagsSingleValue`]
        """
        
        

        self._scaling_group_name = None
        self._scaling_group_id = None
        self._scaling_group_status = None
        self._scaling_configuration_id = None
        self._scaling_configuration_name = None
        self._current_instance_number = None
        self._desire_instance_number = None
        self._min_instance_number = None
        self._max_instance_number = None
        self._cool_down_time = None
        self._lb_listener_id = None
        self._lbaas_listeners = None
        self._available_zones = None
        self._networks = None
        self._security_groups = None
        self._create_time = None
        self._vpc_id = None
        self._detail = None
        self._is_scaling = None
        self._health_periodic_audit_method = None
        self._health_periodic_audit_time = None
        self._health_periodic_audit_grace_period = None
        self._instance_terminate_policy = None
        self._notifications = None
        self._delete_publicip = None
        self._delete_volume = None
        self._cloud_location_id = None
        self._enterprise_project_id = None
        self._activity_type = None
        self._multi_az_priority_policy = None
        self._iam_agency_name = None
        self._description = None
        self._tags = None
        self.discriminator = None

        if scaling_group_name is not None:
            self.scaling_group_name = scaling_group_name
        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id
        if scaling_group_status is not None:
            self.scaling_group_status = scaling_group_status
        if scaling_configuration_id is not None:
            self.scaling_configuration_id = scaling_configuration_id
        if scaling_configuration_name is not None:
            self.scaling_configuration_name = scaling_configuration_name
        if current_instance_number is not None:
            self.current_instance_number = current_instance_number
        if desire_instance_number is not None:
            self.desire_instance_number = desire_instance_number
        if min_instance_number is not None:
            self.min_instance_number = min_instance_number
        if max_instance_number is not None:
            self.max_instance_number = max_instance_number
        if cool_down_time is not None:
            self.cool_down_time = cool_down_time
        if lb_listener_id is not None:
            self.lb_listener_id = lb_listener_id
        if lbaas_listeners is not None:
            self.lbaas_listeners = lbaas_listeners
        if available_zones is not None:
            self.available_zones = available_zones
        if networks is not None:
            self.networks = networks
        if security_groups is not None:
            self.security_groups = security_groups
        if create_time is not None:
            self.create_time = create_time
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if detail is not None:
            self.detail = detail
        if is_scaling is not None:
            self.is_scaling = is_scaling
        if health_periodic_audit_method is not None:
            self.health_periodic_audit_method = health_periodic_audit_method
        if health_periodic_audit_time is not None:
            self.health_periodic_audit_time = health_periodic_audit_time
        if health_periodic_audit_grace_period is not None:
            self.health_periodic_audit_grace_period = health_periodic_audit_grace_period
        if instance_terminate_policy is not None:
            self.instance_terminate_policy = instance_terminate_policy
        if notifications is not None:
            self.notifications = notifications
        if delete_publicip is not None:
            self.delete_publicip = delete_publicip
        if delete_volume is not None:
            self.delete_volume = delete_volume
        if cloud_location_id is not None:
            self.cloud_location_id = cloud_location_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if activity_type is not None:
            self.activity_type = activity_type
        if multi_az_priority_policy is not None:
            self.multi_az_priority_policy = multi_az_priority_policy
        if iam_agency_name is not None:
            self.iam_agency_name = iam_agency_name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def scaling_group_name(self):
        """Gets the scaling_group_name of this ScalingGroups.

        伸缩组名称。

        :return: The scaling_group_name of this ScalingGroups.
        :rtype: str
        """
        return self._scaling_group_name

    @scaling_group_name.setter
    def scaling_group_name(self, scaling_group_name):
        """Sets the scaling_group_name of this ScalingGroups.

        伸缩组名称。

        :param scaling_group_name: The scaling_group_name of this ScalingGroups.
        :type scaling_group_name: str
        """
        self._scaling_group_name = scaling_group_name

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ScalingGroups.

        伸缩组ID。

        :return: The scaling_group_id of this ScalingGroups.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ScalingGroups.

        伸缩组ID。

        :param scaling_group_id: The scaling_group_id of this ScalingGroups.
        :type scaling_group_id: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def scaling_group_status(self):
        """Gets the scaling_group_status of this ScalingGroups.

        伸缩组状态。

        :return: The scaling_group_status of this ScalingGroups.
        :rtype: str
        """
        return self._scaling_group_status

    @scaling_group_status.setter
    def scaling_group_status(self, scaling_group_status):
        """Sets the scaling_group_status of this ScalingGroups.

        伸缩组状态。

        :param scaling_group_status: The scaling_group_status of this ScalingGroups.
        :type scaling_group_status: str
        """
        self._scaling_group_status = scaling_group_status

    @property
    def scaling_configuration_id(self):
        """Gets the scaling_configuration_id of this ScalingGroups.

        伸缩配置ID。

        :return: The scaling_configuration_id of this ScalingGroups.
        :rtype: str
        """
        return self._scaling_configuration_id

    @scaling_configuration_id.setter
    def scaling_configuration_id(self, scaling_configuration_id):
        """Sets the scaling_configuration_id of this ScalingGroups.

        伸缩配置ID。

        :param scaling_configuration_id: The scaling_configuration_id of this ScalingGroups.
        :type scaling_configuration_id: str
        """
        self._scaling_configuration_id = scaling_configuration_id

    @property
    def scaling_configuration_name(self):
        """Gets the scaling_configuration_name of this ScalingGroups.

        伸缩配置名称。

        :return: The scaling_configuration_name of this ScalingGroups.
        :rtype: str
        """
        return self._scaling_configuration_name

    @scaling_configuration_name.setter
    def scaling_configuration_name(self, scaling_configuration_name):
        """Sets the scaling_configuration_name of this ScalingGroups.

        伸缩配置名称。

        :param scaling_configuration_name: The scaling_configuration_name of this ScalingGroups.
        :type scaling_configuration_name: str
        """
        self._scaling_configuration_name = scaling_configuration_name

    @property
    def current_instance_number(self):
        """Gets the current_instance_number of this ScalingGroups.

        伸缩组中当前实例数。

        :return: The current_instance_number of this ScalingGroups.
        :rtype: int
        """
        return self._current_instance_number

    @current_instance_number.setter
    def current_instance_number(self, current_instance_number):
        """Sets the current_instance_number of this ScalingGroups.

        伸缩组中当前实例数。

        :param current_instance_number: The current_instance_number of this ScalingGroups.
        :type current_instance_number: int
        """
        self._current_instance_number = current_instance_number

    @property
    def desire_instance_number(self):
        """Gets the desire_instance_number of this ScalingGroups.

        伸缩组期望实例数。

        :return: The desire_instance_number of this ScalingGroups.
        :rtype: int
        """
        return self._desire_instance_number

    @desire_instance_number.setter
    def desire_instance_number(self, desire_instance_number):
        """Sets the desire_instance_number of this ScalingGroups.

        伸缩组期望实例数。

        :param desire_instance_number: The desire_instance_number of this ScalingGroups.
        :type desire_instance_number: int
        """
        self._desire_instance_number = desire_instance_number

    @property
    def min_instance_number(self):
        """Gets the min_instance_number of this ScalingGroups.

        伸缩组最小实例数。

        :return: The min_instance_number of this ScalingGroups.
        :rtype: int
        """
        return self._min_instance_number

    @min_instance_number.setter
    def min_instance_number(self, min_instance_number):
        """Sets the min_instance_number of this ScalingGroups.

        伸缩组最小实例数。

        :param min_instance_number: The min_instance_number of this ScalingGroups.
        :type min_instance_number: int
        """
        self._min_instance_number = min_instance_number

    @property
    def max_instance_number(self):
        """Gets the max_instance_number of this ScalingGroups.

        伸缩组最大实例数

        :return: The max_instance_number of this ScalingGroups.
        :rtype: int
        """
        return self._max_instance_number

    @max_instance_number.setter
    def max_instance_number(self, max_instance_number):
        """Sets the max_instance_number of this ScalingGroups.

        伸缩组最大实例数

        :param max_instance_number: The max_instance_number of this ScalingGroups.
        :type max_instance_number: int
        """
        self._max_instance_number = max_instance_number

    @property
    def cool_down_time(self):
        """Gets the cool_down_time of this ScalingGroups.

        冷却时间，单位是秒。

        :return: The cool_down_time of this ScalingGroups.
        :rtype: int
        """
        return self._cool_down_time

    @cool_down_time.setter
    def cool_down_time(self, cool_down_time):
        """Sets the cool_down_time of this ScalingGroups.

        冷却时间，单位是秒。

        :param cool_down_time: The cool_down_time of this ScalingGroups.
        :type cool_down_time: int
        """
        self._cool_down_time = cool_down_time

    @property
    def lb_listener_id(self):
        """Gets the lb_listener_id of this ScalingGroups.

        经典型负载均衡监听器ID，多个负载均衡监听器ID以逗号分隔。

        :return: The lb_listener_id of this ScalingGroups.
        :rtype: str
        """
        return self._lb_listener_id

    @lb_listener_id.setter
    def lb_listener_id(self, lb_listener_id):
        """Sets the lb_listener_id of this ScalingGroups.

        经典型负载均衡监听器ID，多个负载均衡监听器ID以逗号分隔。

        :param lb_listener_id: The lb_listener_id of this ScalingGroups.
        :type lb_listener_id: str
        """
        self._lb_listener_id = lb_listener_id

    @property
    def lbaas_listeners(self):
        """Gets the lbaas_listeners of this ScalingGroups.

        增强型负载均衡器信息，该参数为预留字段。

        :return: The lbaas_listeners of this ScalingGroups.
        :rtype: list[:class:`huaweicloudsdkas.v1.LbaasListenersResult`]
        """
        return self._lbaas_listeners

    @lbaas_listeners.setter
    def lbaas_listeners(self, lbaas_listeners):
        """Sets the lbaas_listeners of this ScalingGroups.

        增强型负载均衡器信息，该参数为预留字段。

        :param lbaas_listeners: The lbaas_listeners of this ScalingGroups.
        :type lbaas_listeners: list[:class:`huaweicloudsdkas.v1.LbaasListenersResult`]
        """
        self._lbaas_listeners = lbaas_listeners

    @property
    def available_zones(self):
        """Gets the available_zones of this ScalingGroups.

        可用分区信息

        :return: The available_zones of this ScalingGroups.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this ScalingGroups.

        可用分区信息

        :param available_zones: The available_zones of this ScalingGroups.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def networks(self):
        """Gets the networks of this ScalingGroups.

        网络信息

        :return: The networks of this ScalingGroups.
        :rtype: list[:class:`huaweicloudsdkas.v1.NetworksResult`]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this ScalingGroups.

        网络信息

        :param networks: The networks of this ScalingGroups.
        :type networks: list[:class:`huaweicloudsdkas.v1.NetworksResult`]
        """
        self._networks = networks

    @property
    def security_groups(self):
        """Gets the security_groups of this ScalingGroups.

        安全组信息

        :return: The security_groups of this ScalingGroups.
        :rtype: list[:class:`huaweicloudsdkas.v1.SecurityGroupsResult`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this ScalingGroups.

        安全组信息

        :param security_groups: The security_groups of this ScalingGroups.
        :type security_groups: list[:class:`huaweicloudsdkas.v1.SecurityGroupsResult`]
        """
        self._security_groups = security_groups

    @property
    def create_time(self):
        """Gets the create_time of this ScalingGroups.

        创建伸缩组时间，遵循UTC时间。

        :return: The create_time of this ScalingGroups.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScalingGroups.

        创建伸缩组时间，遵循UTC时间。

        :param create_time: The create_time of this ScalingGroups.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ScalingGroups.

        伸缩组所在的VPC ID。

        :return: The vpc_id of this ScalingGroups.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ScalingGroups.

        伸缩组所在的VPC ID。

        :param vpc_id: The vpc_id of this ScalingGroups.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def detail(self):
        """Gets the detail of this ScalingGroups.

        伸缩组详情。

        :return: The detail of this ScalingGroups.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ScalingGroups.

        伸缩组详情。

        :param detail: The detail of this ScalingGroups.
        :type detail: str
        """
        self._detail = detail

    @property
    def is_scaling(self):
        """Gets the is_scaling of this ScalingGroups.

        伸缩组伸缩标志。

        :return: The is_scaling of this ScalingGroups.
        :rtype: bool
        """
        return self._is_scaling

    @is_scaling.setter
    def is_scaling(self, is_scaling):
        """Sets the is_scaling of this ScalingGroups.

        伸缩组伸缩标志。

        :param is_scaling: The is_scaling of this ScalingGroups.
        :type is_scaling: bool
        """
        self._is_scaling = is_scaling

    @property
    def health_periodic_audit_method(self):
        """Gets the health_periodic_audit_method of this ScalingGroups.

        健康检查方式。

        :return: The health_periodic_audit_method of this ScalingGroups.
        :rtype: str
        """
        return self._health_periodic_audit_method

    @health_periodic_audit_method.setter
    def health_periodic_audit_method(self, health_periodic_audit_method):
        """Sets the health_periodic_audit_method of this ScalingGroups.

        健康检查方式。

        :param health_periodic_audit_method: The health_periodic_audit_method of this ScalingGroups.
        :type health_periodic_audit_method: str
        """
        self._health_periodic_audit_method = health_periodic_audit_method

    @property
    def health_periodic_audit_time(self):
        """Gets the health_periodic_audit_time of this ScalingGroups.

        健康检查的间隔时间。

        :return: The health_periodic_audit_time of this ScalingGroups.
        :rtype: int
        """
        return self._health_periodic_audit_time

    @health_periodic_audit_time.setter
    def health_periodic_audit_time(self, health_periodic_audit_time):
        """Sets the health_periodic_audit_time of this ScalingGroups.

        健康检查的间隔时间。

        :param health_periodic_audit_time: The health_periodic_audit_time of this ScalingGroups.
        :type health_periodic_audit_time: int
        """
        self._health_periodic_audit_time = health_periodic_audit_time

    @property
    def health_periodic_audit_grace_period(self):
        """Gets the health_periodic_audit_grace_period of this ScalingGroups.

        健康状况检查宽限期。

        :return: The health_periodic_audit_grace_period of this ScalingGroups.
        :rtype: int
        """
        return self._health_periodic_audit_grace_period

    @health_periodic_audit_grace_period.setter
    def health_periodic_audit_grace_period(self, health_periodic_audit_grace_period):
        """Sets the health_periodic_audit_grace_period of this ScalingGroups.

        健康状况检查宽限期。

        :param health_periodic_audit_grace_period: The health_periodic_audit_grace_period of this ScalingGroups.
        :type health_periodic_audit_grace_period: int
        """
        self._health_periodic_audit_grace_period = health_periodic_audit_grace_period

    @property
    def instance_terminate_policy(self):
        """Gets the instance_terminate_policy of this ScalingGroups.

        移除策略。

        :return: The instance_terminate_policy of this ScalingGroups.
        :rtype: str
        """
        return self._instance_terminate_policy

    @instance_terminate_policy.setter
    def instance_terminate_policy(self, instance_terminate_policy):
        """Sets the instance_terminate_policy of this ScalingGroups.

        移除策略。

        :param instance_terminate_policy: The instance_terminate_policy of this ScalingGroups.
        :type instance_terminate_policy: str
        """
        self._instance_terminate_policy = instance_terminate_policy

    @property
    def notifications(self):
        """Gets the notifications of this ScalingGroups.

        通知方式：EMAIL为发送邮件通知。该通知方式已经被废除，建议给弹性伸缩组配置通知功能。请参考[通知](https://support.huaweicloud.com/api-as/as_06_0800.html)。

        :return: The notifications of this ScalingGroups.
        :rtype: list[str]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this ScalingGroups.

        通知方式：EMAIL为发送邮件通知。该通知方式已经被废除，建议给弹性伸缩组配置通知功能。请参考[通知](https://support.huaweicloud.com/api-as/as_06_0800.html)。

        :param notifications: The notifications of this ScalingGroups.
        :type notifications: list[str]
        """
        self._notifications = notifications

    @property
    def delete_publicip(self):
        """Gets the delete_publicip of this ScalingGroups.

        删除云服务器是否删除云服务器绑定的弹性IP。

        :return: The delete_publicip of this ScalingGroups.
        :rtype: bool
        """
        return self._delete_publicip

    @delete_publicip.setter
    def delete_publicip(self, delete_publicip):
        """Sets the delete_publicip of this ScalingGroups.

        删除云服务器是否删除云服务器绑定的弹性IP。

        :param delete_publicip: The delete_publicip of this ScalingGroups.
        :type delete_publicip: bool
        """
        self._delete_publicip = delete_publicip

    @property
    def delete_volume(self):
        """Gets the delete_volume of this ScalingGroups.

        删除云服务器是否删除云服务器绑定的数据盘

        :return: The delete_volume of this ScalingGroups.
        :rtype: bool
        """
        return self._delete_volume

    @delete_volume.setter
    def delete_volume(self, delete_volume):
        """Sets the delete_volume of this ScalingGroups.

        删除云服务器是否删除云服务器绑定的数据盘

        :param delete_volume: The delete_volume of this ScalingGroups.
        :type delete_volume: bool
        """
        self._delete_volume = delete_volume

    @property
    def cloud_location_id(self):
        """Gets the cloud_location_id of this ScalingGroups.

        该参数为预留字段

        :return: The cloud_location_id of this ScalingGroups.
        :rtype: str
        """
        return self._cloud_location_id

    @cloud_location_id.setter
    def cloud_location_id(self, cloud_location_id):
        """Sets the cloud_location_id of this ScalingGroups.

        该参数为预留字段

        :param cloud_location_id: The cloud_location_id of this ScalingGroups.
        :type cloud_location_id: str
        """
        self._cloud_location_id = cloud_location_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ScalingGroups.

        企业项目ID

        :return: The enterprise_project_id of this ScalingGroups.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ScalingGroups.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ScalingGroups.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def activity_type(self):
        """Gets the activity_type of this ScalingGroups.

        伸缩组活动类型

        :return: The activity_type of this ScalingGroups.
        :rtype: str
        """
        return self._activity_type

    @activity_type.setter
    def activity_type(self, activity_type):
        """Sets the activity_type of this ScalingGroups.

        伸缩组活动类型

        :param activity_type: The activity_type of this ScalingGroups.
        :type activity_type: str
        """
        self._activity_type = activity_type

    @property
    def multi_az_priority_policy(self):
        """Gets the multi_az_priority_policy of this ScalingGroups.

        伸缩组扩缩容时目标AZ选择的优先级策略

        :return: The multi_az_priority_policy of this ScalingGroups.
        :rtype: str
        """
        return self._multi_az_priority_policy

    @multi_az_priority_policy.setter
    def multi_az_priority_policy(self, multi_az_priority_policy):
        """Sets the multi_az_priority_policy of this ScalingGroups.

        伸缩组扩缩容时目标AZ选择的优先级策略

        :param multi_az_priority_policy: The multi_az_priority_policy of this ScalingGroups.
        :type multi_az_priority_policy: str
        """
        self._multi_az_priority_policy = multi_az_priority_policy

    @property
    def iam_agency_name(self):
        """Gets the iam_agency_name of this ScalingGroups.

        委托的名称委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务的临时凭证。

        :return: The iam_agency_name of this ScalingGroups.
        :rtype: str
        """
        return self._iam_agency_name

    @iam_agency_name.setter
    def iam_agency_name(self, iam_agency_name):
        """Sets the iam_agency_name of this ScalingGroups.

        委托的名称委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务的临时凭证。

        :param iam_agency_name: The iam_agency_name of this ScalingGroups.
        :type iam_agency_name: str
        """
        self._iam_agency_name = iam_agency_name

    @property
    def description(self):
        """Gets the description of this ScalingGroups.

        伸缩组描述信息

        :return: The description of this ScalingGroups.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScalingGroups.

        伸缩组描述信息

        :param description: The description of this ScalingGroups.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        """Gets the tags of this ScalingGroups.

        添加到伸缩组的标签。

        :return: The tags of this ScalingGroups.
        :rtype: list[:class:`huaweicloudsdkas.v1.TagsSingleValue`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ScalingGroups.

        添加到伸缩组的标签。

        :param tags: The tags of this ScalingGroups.
        :type tags: list[:class:`huaweicloudsdkas.v1.TagsSingleValue`]
        """
        self._tags = tags

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
        if not isinstance(other, ScalingGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
