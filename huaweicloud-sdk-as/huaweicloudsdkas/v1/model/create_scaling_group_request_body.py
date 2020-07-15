# coding: utf-8

import pprint
import re

import six





class CreateScalingGroupRequestBody:


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
        'scaling_configuration_id': 'str',
        'desire_instance_number': 'int',
        'min_instance_number': 'int',
        'max_instance_number': 'int',
        'cool_down_time': 'int',
        'lb_listener_id': 'str',
        'lbaas_listeners': 'list[LbaasListeners]',
        'available_zones': 'list[str]',
        'networks': 'list[Networks]',
        'security_groups': 'list[SecurityGroups]',
        'vpc_id': 'str',
        'health_periodic_audit_method': 'str',
        'health_periodic_audit_time': 'int',
        'health_periodic_audit_grace_period': 'int',
        'instance_terminate_policy': 'str',
        'notifications': 'list[str]',
        'delete_publicip': 'bool',
        'enterprise_project_id': 'str',
        'multi_az_priority_policy': 'str'
    }

    attribute_map = {
        'scaling_group_name': 'scaling_group_name',
        'scaling_configuration_id': 'scaling_configuration_id',
        'desire_instance_number': 'desire_instance_number',
        'min_instance_number': 'min_instance_number',
        'max_instance_number': 'max_instance_number',
        'cool_down_time': 'cool_down_time',
        'lb_listener_id': 'lb_listener_id',
        'lbaas_listeners': 'lbaas_listeners',
        'available_zones': 'available_zones',
        'networks': 'networks',
        'security_groups': 'security_groups',
        'vpc_id': 'vpc_id',
        'health_periodic_audit_method': 'health_periodic_audit_method',
        'health_periodic_audit_time': 'health_periodic_audit_time',
        'health_periodic_audit_grace_period': 'health_periodic_audit_grace_period',
        'instance_terminate_policy': 'instance_terminate_policy',
        'notifications': 'notifications',
        'delete_publicip': 'delete_publicip',
        'enterprise_project_id': 'enterprise_project_id',
        'multi_az_priority_policy': 'multi_az_priority_policy'
    }

    def __init__(self, scaling_group_name=None, scaling_configuration_id=None, desire_instance_number=None, min_instance_number=None, max_instance_number=None, cool_down_time=None, lb_listener_id=None, lbaas_listeners=None, available_zones=None, networks=None, security_groups=None, vpc_id=None, health_periodic_audit_method=None, health_periodic_audit_time=None, health_periodic_audit_grace_period=None, instance_terminate_policy=None, notifications=None, delete_publicip=None, enterprise_project_id=None, multi_az_priority_policy=None):
        """CreateScalingGroupRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._scaling_group_name = None
        self._scaling_configuration_id = None
        self._desire_instance_number = None
        self._min_instance_number = None
        self._max_instance_number = None
        self._cool_down_time = None
        self._lb_listener_id = None
        self._lbaas_listeners = None
        self._available_zones = None
        self._networks = None
        self._security_groups = None
        self._vpc_id = None
        self._health_periodic_audit_method = None
        self._health_periodic_audit_time = None
        self._health_periodic_audit_grace_period = None
        self._instance_terminate_policy = None
        self._notifications = None
        self._delete_publicip = None
        self._enterprise_project_id = None
        self._multi_az_priority_policy = None
        self.discriminator = None

        self.scaling_group_name = scaling_group_name
        if scaling_configuration_id is not None:
            self.scaling_configuration_id = scaling_configuration_id
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
        self.networks = networks
        if security_groups is not None:
            self.security_groups = security_groups
        self.vpc_id = vpc_id
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
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if multi_az_priority_policy is not None:
            self.multi_az_priority_policy = multi_az_priority_policy

    @property
    def scaling_group_name(self):
        """Gets the scaling_group_name of this CreateScalingGroupRequestBody.

        伸缩组名称(1-64个字符)，只能包含中文、字母、数字、下划线、中划线。

        :return: The scaling_group_name of this CreateScalingGroupRequestBody.
        :rtype: str
        """
        return self._scaling_group_name

    @scaling_group_name.setter
    def scaling_group_name(self, scaling_group_name):
        """Sets the scaling_group_name of this CreateScalingGroupRequestBody.

        伸缩组名称(1-64个字符)，只能包含中文、字母、数字、下划线、中划线。

        :param scaling_group_name: The scaling_group_name of this CreateScalingGroupRequestBody.
        :type: str
        """
        self._scaling_group_name = scaling_group_name

    @property
    def scaling_configuration_id(self):
        """Gets the scaling_configuration_id of this CreateScalingGroupRequestBody.

        伸缩配置ID，通过查询弹性伸缩配置列表接口获取。

        :return: The scaling_configuration_id of this CreateScalingGroupRequestBody.
        :rtype: str
        """
        return self._scaling_configuration_id

    @scaling_configuration_id.setter
    def scaling_configuration_id(self, scaling_configuration_id):
        """Sets the scaling_configuration_id of this CreateScalingGroupRequestBody.

        伸缩配置ID，通过查询弹性伸缩配置列表接口获取。

        :param scaling_configuration_id: The scaling_configuration_id of this CreateScalingGroupRequestBody.
        :type: str
        """
        self._scaling_configuration_id = scaling_configuration_id

    @property
    def desire_instance_number(self):
        """Gets the desire_instance_number of this CreateScalingGroupRequestBody.

        期望实例数量，默认值为最小实例数。最小实例数<=期望实例数<=最大实例数

        :return: The desire_instance_number of this CreateScalingGroupRequestBody.
        :rtype: int
        """
        return self._desire_instance_number

    @desire_instance_number.setter
    def desire_instance_number(self, desire_instance_number):
        """Sets the desire_instance_number of this CreateScalingGroupRequestBody.

        期望实例数量，默认值为最小实例数。最小实例数<=期望实例数<=最大实例数

        :param desire_instance_number: The desire_instance_number of this CreateScalingGroupRequestBody.
        :type: int
        """
        self._desire_instance_number = desire_instance_number

    @property
    def min_instance_number(self):
        """Gets the min_instance_number of this CreateScalingGroupRequestBody.

        最小实例数量，默认值为0。

        :return: The min_instance_number of this CreateScalingGroupRequestBody.
        :rtype: int
        """
        return self._min_instance_number

    @min_instance_number.setter
    def min_instance_number(self, min_instance_number):
        """Sets the min_instance_number of this CreateScalingGroupRequestBody.

        最小实例数量，默认值为0。

        :param min_instance_number: The min_instance_number of this CreateScalingGroupRequestBody.
        :type: int
        """
        self._min_instance_number = min_instance_number

    @property
    def max_instance_number(self):
        """Gets the max_instance_number of this CreateScalingGroupRequestBody.

        最大实例数量，默认值为0。

        :return: The max_instance_number of this CreateScalingGroupRequestBody.
        :rtype: int
        """
        return self._max_instance_number

    @max_instance_number.setter
    def max_instance_number(self, max_instance_number):
        """Sets the max_instance_number of this CreateScalingGroupRequestBody.

        最大实例数量，默认值为0。

        :param max_instance_number: The max_instance_number of this CreateScalingGroupRequestBody.
        :type: int
        """
        self._max_instance_number = max_instance_number

    @property
    def cool_down_time(self):
        """Gets the cool_down_time of this CreateScalingGroupRequestBody.

        冷却时间，取值范围0-86400，默认为900，单位是秒。 只针对告警策略生效，定时、周期策略和手动触发策略不受该参数限制。

        :return: The cool_down_time of this CreateScalingGroupRequestBody.
        :rtype: int
        """
        return self._cool_down_time

    @cool_down_time.setter
    def cool_down_time(self, cool_down_time):
        """Sets the cool_down_time of this CreateScalingGroupRequestBody.

        冷却时间，取值范围0-86400，默认为900，单位是秒。 只针对告警策略生效，定时、周期策略和手动触发策略不受该参数限制。

        :param cool_down_time: The cool_down_time of this CreateScalingGroupRequestBody.
        :type: int
        """
        self._cool_down_time = cool_down_time

    @property
    def lb_listener_id(self):
        """Gets the lb_listener_id of this CreateScalingGroupRequestBody.

        弹性负载均衡（经典型）监听器ID，最多支持绑定3个负载均衡监听器，多个负载均衡监听器ID以逗号分隔。首先使用vpc_id通过查询ELB服务负载均衡器列表接口获取负载均衡器的ID，详见《弹性负载均衡API参考》的“查询负载均衡器列表”，再使用该ID查询监听器列表获取，详见《弹性负载均衡API参考》的“查询监听器列表”。

        :return: The lb_listener_id of this CreateScalingGroupRequestBody.
        :rtype: str
        """
        return self._lb_listener_id

    @lb_listener_id.setter
    def lb_listener_id(self, lb_listener_id):
        """Sets the lb_listener_id of this CreateScalingGroupRequestBody.

        弹性负载均衡（经典型）监听器ID，最多支持绑定3个负载均衡监听器，多个负载均衡监听器ID以逗号分隔。首先使用vpc_id通过查询ELB服务负载均衡器列表接口获取负载均衡器的ID，详见《弹性负载均衡API参考》的“查询负载均衡器列表”，再使用该ID查询监听器列表获取，详见《弹性负载均衡API参考》的“查询监听器列表”。

        :param lb_listener_id: The lb_listener_id of this CreateScalingGroupRequestBody.
        :type: str
        """
        self._lb_listener_id = lb_listener_id

    @property
    def lbaas_listeners(self):
        """Gets the lbaas_listeners of this CreateScalingGroupRequestBody.

        弹性负载均衡器（增强型）信息，最多支持绑定3个负载均衡。该字段与lb_listener_id互斥。

        :return: The lbaas_listeners of this CreateScalingGroupRequestBody.
        :rtype: list[LbaasListeners]
        """
        return self._lbaas_listeners

    @lbaas_listeners.setter
    def lbaas_listeners(self, lbaas_listeners):
        """Sets the lbaas_listeners of this CreateScalingGroupRequestBody.

        弹性负载均衡器（增强型）信息，最多支持绑定3个负载均衡。该字段与lb_listener_id互斥。

        :param lbaas_listeners: The lbaas_listeners of this CreateScalingGroupRequestBody.
        :type: list[LbaasListeners]
        """
        self._lbaas_listeners = lbaas_listeners

    @property
    def available_zones(self):
        """Gets the available_zones of this CreateScalingGroupRequestBody.

        可用分区信息。弹性伸缩活动中自动添加的云服务器会被创建在指定的可用区中。如果没有指定可用分区，会由系统自动指定可用分区。详情请参考地区和终端节点。

        :return: The available_zones of this CreateScalingGroupRequestBody.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this CreateScalingGroupRequestBody.

        可用分区信息。弹性伸缩活动中自动添加的云服务器会被创建在指定的可用区中。如果没有指定可用分区，会由系统自动指定可用分区。详情请参考地区和终端节点。

        :param available_zones: The available_zones of this CreateScalingGroupRequestBody.
        :type: list[str]
        """
        self._available_zones = available_zones

    @property
    def networks(self):
        """Gets the networks of this CreateScalingGroupRequestBody.

        网络信息，最多支持选择5个子网，传入的第一个子网默认作为云服务器的主网卡。使用vpc_id通过查询VPC服务子网列表接口获取， 查询子网列表”。

        :return: The networks of this CreateScalingGroupRequestBody.
        :rtype: list[Networks]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this CreateScalingGroupRequestBody.

        网络信息，最多支持选择5个子网，传入的第一个子网默认作为云服务器的主网卡。使用vpc_id通过查询VPC服务子网列表接口获取， 查询子网列表”。

        :param networks: The networks of this CreateScalingGroupRequestBody.
        :type: list[Networks]
        """
        self._networks = networks

    @property
    def security_groups(self):
        """Gets the security_groups of this CreateScalingGroupRequestBody.

        安全组信息，最多支持选择1个安全组。使用vpc_id通过查询VPC服务安全组列表接口获取，详见《虚拟私有云API参考》的“查询安全组列表”。当伸缩配置和伸缩组同时指定安全组时，将以伸缩配置中的安全组为准；当伸缩配置和伸缩组都没有指定安全组时，将使用默认安全组。为了使用灵活性更高，推荐在伸缩配置中指定安全组。

        :return: The security_groups of this CreateScalingGroupRequestBody.
        :rtype: list[SecurityGroups]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this CreateScalingGroupRequestBody.

        安全组信息，最多支持选择1个安全组。使用vpc_id通过查询VPC服务安全组列表接口获取，详见《虚拟私有云API参考》的“查询安全组列表”。当伸缩配置和伸缩组同时指定安全组时，将以伸缩配置中的安全组为准；当伸缩配置和伸缩组都没有指定安全组时，将使用默认安全组。为了使用灵活性更高，推荐在伸缩配置中指定安全组。

        :param security_groups: The security_groups of this CreateScalingGroupRequestBody.
        :type: list[SecurityGroups]
        """
        self._security_groups = security_groups

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateScalingGroupRequestBody.

        VPC信息，通过查询VPC服务VPC列表接口获取，详见《虚拟私有云API参考》的“查询VPC列表”。

        :return: The vpc_id of this CreateScalingGroupRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateScalingGroupRequestBody.

        VPC信息，通过查询VPC服务VPC列表接口获取，详见《虚拟私有云API参考》的“查询VPC列表”。

        :param vpc_id: The vpc_id of this CreateScalingGroupRequestBody.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def health_periodic_audit_method(self):
        """Gets the health_periodic_audit_method of this CreateScalingGroupRequestBody.

        伸缩组实例健康检查方式：ELB_AUDIT和NOVA_AUDIT。当伸缩组参数中设置负载均衡时，默认为ELB_AUDIT；否则默认为NOVA_AUDIT。ELB_AUDIT表示负载均衡健康检查方式，在有监听器的伸缩组中有效。NOVA_AUDIT表示弹性伸缩自带的健康检查方式。

        :return: The health_periodic_audit_method of this CreateScalingGroupRequestBody.
        :rtype: str
        """
        return self._health_periodic_audit_method

    @health_periodic_audit_method.setter
    def health_periodic_audit_method(self, health_periodic_audit_method):
        """Sets the health_periodic_audit_method of this CreateScalingGroupRequestBody.

        伸缩组实例健康检查方式：ELB_AUDIT和NOVA_AUDIT。当伸缩组参数中设置负载均衡时，默认为ELB_AUDIT；否则默认为NOVA_AUDIT。ELB_AUDIT表示负载均衡健康检查方式，在有监听器的伸缩组中有效。NOVA_AUDIT表示弹性伸缩自带的健康检查方式。

        :param health_periodic_audit_method: The health_periodic_audit_method of this CreateScalingGroupRequestBody.
        :type: str
        """
        self._health_periodic_audit_method = health_periodic_audit_method

    @property
    def health_periodic_audit_time(self):
        """Gets the health_periodic_audit_time of this CreateScalingGroupRequestBody.

        伸缩组实例的健康检查周期，可设置为1、5、15、60、180（分钟），若不设置该参数，默认为5。若设置为0，可以实现10秒级健康检查。

        :return: The health_periodic_audit_time of this CreateScalingGroupRequestBody.
        :rtype: int
        """
        return self._health_periodic_audit_time

    @health_periodic_audit_time.setter
    def health_periodic_audit_time(self, health_periodic_audit_time):
        """Sets the health_periodic_audit_time of this CreateScalingGroupRequestBody.

        伸缩组实例的健康检查周期，可设置为1、5、15、60、180（分钟），若不设置该参数，默认为5。若设置为0，可以实现10秒级健康检查。

        :param health_periodic_audit_time: The health_periodic_audit_time of this CreateScalingGroupRequestBody.
        :type: int
        """
        self._health_periodic_audit_time = health_periodic_audit_time

    @property
    def health_periodic_audit_grace_period(self):
        """Gets the health_periodic_audit_grace_period of this CreateScalingGroupRequestBody.

        伸缩组实例健康状况检查宽限期，取值范围0-86400，单位是秒。当实例加入伸缩组并且进入已启用状态后，健康状况检查宽限期才会启动，伸缩组会等健康状况检查宽限期结束后才检查实例的运行状况。当伸缩组实例健康检查方式为ELB_AUDIT时，该参数生效，若不设置该参数，默认为600秒。

        :return: The health_periodic_audit_grace_period of this CreateScalingGroupRequestBody.
        :rtype: int
        """
        return self._health_periodic_audit_grace_period

    @health_periodic_audit_grace_period.setter
    def health_periodic_audit_grace_period(self, health_periodic_audit_grace_period):
        """Sets the health_periodic_audit_grace_period of this CreateScalingGroupRequestBody.

        伸缩组实例健康状况检查宽限期，取值范围0-86400，单位是秒。当实例加入伸缩组并且进入已启用状态后，健康状况检查宽限期才会启动，伸缩组会等健康状况检查宽限期结束后才检查实例的运行状况。当伸缩组实例健康检查方式为ELB_AUDIT时，该参数生效，若不设置该参数，默认为600秒。

        :param health_periodic_audit_grace_period: The health_periodic_audit_grace_period of this CreateScalingGroupRequestBody.
        :type: int
        """
        self._health_periodic_audit_grace_period = health_periodic_audit_grace_period

    @property
    def instance_terminate_policy(self):
        """Gets the instance_terminate_policy of this CreateScalingGroupRequestBody.

        伸缩组实例移除策略：OLD_CONFIG_OLD_INSTANCE（默认）：从根据“较早创建的配置”创建的实例中筛选出较早创建的实例被优先移除。OLD_CONFIG_NEW_INSTANCE：从根据“较早创建的配置”创建的实例中筛选出较新创建的实例被优先移除。OLD_INSTANCE：较早创建的实例被优先移除。NEW_INSTANCE：较新创建的实例将被优先移除。

        :return: The instance_terminate_policy of this CreateScalingGroupRequestBody.
        :rtype: str
        """
        return self._instance_terminate_policy

    @instance_terminate_policy.setter
    def instance_terminate_policy(self, instance_terminate_policy):
        """Sets the instance_terminate_policy of this CreateScalingGroupRequestBody.

        伸缩组实例移除策略：OLD_CONFIG_OLD_INSTANCE（默认）：从根据“较早创建的配置”创建的实例中筛选出较早创建的实例被优先移除。OLD_CONFIG_NEW_INSTANCE：从根据“较早创建的配置”创建的实例中筛选出较新创建的实例被优先移除。OLD_INSTANCE：较早创建的实例被优先移除。NEW_INSTANCE：较新创建的实例将被优先移除。

        :param instance_terminate_policy: The instance_terminate_policy of this CreateScalingGroupRequestBody.
        :type: str
        """
        self._instance_terminate_policy = instance_terminate_policy

    @property
    def notifications(self):
        """Gets the notifications of this CreateScalingGroupRequestBody.

        通知方式：EMAIL为发送邮件通知。该通知方式即将被废除，建议给弹性伸缩组配置通知功能。详见通知。

        :return: The notifications of this CreateScalingGroupRequestBody.
        :rtype: list[str]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this CreateScalingGroupRequestBody.

        通知方式：EMAIL为发送邮件通知。该通知方式即将被废除，建议给弹性伸缩组配置通知功能。详见通知。

        :param notifications: The notifications of this CreateScalingGroupRequestBody.
        :type: list[str]
        """
        self._notifications = notifications

    @property
    def delete_publicip(self):
        """Gets the delete_publicip of this CreateScalingGroupRequestBody.

        配置删除云服务器时是否删除云服务器绑定的弹性IP。取值为true或false，默认为false。true：删除云服务器时，会同时删除绑定在云服务器上的弹性IP。当弹性IP的计费方式为包年包月时，不会被删除。false：删除云服务器时，仅解绑定在云服务器上的弹性IP，不删除弹性IP。

        :return: The delete_publicip of this CreateScalingGroupRequestBody.
        :rtype: bool
        """
        return self._delete_publicip

    @delete_publicip.setter
    def delete_publicip(self, delete_publicip):
        """Sets the delete_publicip of this CreateScalingGroupRequestBody.

        配置删除云服务器时是否删除云服务器绑定的弹性IP。取值为true或false，默认为false。true：删除云服务器时，会同时删除绑定在云服务器上的弹性IP。当弹性IP的计费方式为包年包月时，不会被删除。false：删除云服务器时，仅解绑定在云服务器上的弹性IP，不删除弹性IP。

        :param delete_publicip: The delete_publicip of this CreateScalingGroupRequestBody.
        :type: bool
        """
        self._delete_publicip = delete_publicip

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateScalingGroupRequestBody.

        企业项目ID，用于指定伸缩组归属的企业项目。当伸缩组配置企业项目时，由该伸缩组创建的弹性云服务器将归属于该企业项目。当没有指定企业项目时，将使用企业项目ID为0的默认项目。

        :return: The enterprise_project_id of this CreateScalingGroupRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateScalingGroupRequestBody.

        企业项目ID，用于指定伸缩组归属的企业项目。当伸缩组配置企业项目时，由该伸缩组创建的弹性云服务器将归属于该企业项目。当没有指定企业项目时，将使用企业项目ID为0的默认项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateScalingGroupRequestBody.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def multi_az_priority_policy(self):
        """Gets the multi_az_priority_policy of this CreateScalingGroupRequestBody.

        伸缩组扩缩容时目标AZ选择的优先级策略：EQUILIBRIUM_DISTRIBUTE（默认）：均衡分布，云服务器扩缩容时优先保证available_zones列表中各AZ下虚拟机数量均衡，当无法在目标AZ下完成虚拟机扩容时，按照PICK_FIRST原则选择其他可用AZ。PICK_FIRST：选择优先，虚拟机扩缩容时目标AZ的选择按照available_zones列表的顺序进行优先级排序。

        :return: The multi_az_priority_policy of this CreateScalingGroupRequestBody.
        :rtype: str
        """
        return self._multi_az_priority_policy

    @multi_az_priority_policy.setter
    def multi_az_priority_policy(self, multi_az_priority_policy):
        """Sets the multi_az_priority_policy of this CreateScalingGroupRequestBody.

        伸缩组扩缩容时目标AZ选择的优先级策略：EQUILIBRIUM_DISTRIBUTE（默认）：均衡分布，云服务器扩缩容时优先保证available_zones列表中各AZ下虚拟机数量均衡，当无法在目标AZ下完成虚拟机扩容时，按照PICK_FIRST原则选择其他可用AZ。PICK_FIRST：选择优先，虚拟机扩缩容时目标AZ的选择按照available_zones列表的顺序进行优先级排序。

        :param multi_az_priority_policy: The multi_az_priority_policy of this CreateScalingGroupRequestBody.
        :type: str
        """
        self._multi_az_priority_policy = multi_az_priority_policy

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateScalingGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
