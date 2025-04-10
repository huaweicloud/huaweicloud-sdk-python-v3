# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip': 'str',
        'exp_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'release_time': 'str',
        'name': 'str',
        'instance_id': 'str',
        'private_ip': 'str',
        'task_status': 'str',
        'status': 'str',
        'created': 'str',
        'region': 'str',
        'zone': 'str',
        'availability_zone_display': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'specification': 'str',
        'update': 'str',
        'createinstance_status': 'str',
        'fail_reason': 'str',
        'instance_key': 'str',
        'order_id': 'str',
        'period_num': 'str',
        'resource_id': 'str',
        'bastion_type': 'str',
        'alter_permit': 'str',
        'public_id': 'str',
        'bastion_version': 'str',
        'new_bastion_version': 'str',
        'instance_status': 'str',
        'instance_description': 'str',
        'slave_zone': 'str',
        'enterprise_project_id': 'str',
        'instance_type': 'str',
        'ha_id': 'str',
        'slave_zone_display': 'str',
        'web_port': 'str',
        'vip': 'str'
    }

    attribute_map = {
        'publicip': 'publicip',
        'exp_time': 'expTime',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'release_time': 'releaseTime',
        'name': 'name',
        'instance_id': 'instanceId',
        'private_ip': 'privateIp',
        'task_status': 'taskStatus',
        'status': 'status',
        'created': 'created',
        'region': 'region',
        'zone': 'zone',
        'availability_zone_display': 'availability_zone_display',
        'vpc_id': 'vpcId',
        'subnet_id': 'subnetId',
        'security_group_id': 'securityGroupId',
        'specification': 'specification',
        'update': 'update',
        'createinstance_status': 'createinstanceStatus',
        'fail_reason': 'failReason',
        'instance_key': 'instanceKey',
        'order_id': 'orderId',
        'period_num': 'periodNum',
        'resource_id': 'resourceId',
        'bastion_type': 'bastion_type',
        'alter_permit': 'alterPermit',
        'public_id': 'publicId',
        'bastion_version': 'bastionVersion',
        'new_bastion_version': 'newBastionVersion',
        'instance_status': 'instanceStatus',
        'instance_description': 'instanceDescription',
        'slave_zone': 'slaveZone',
        'enterprise_project_id': 'enterpriseProjectId',
        'instance_type': 'instanceType',
        'ha_id': 'haId',
        'slave_zone_display': 'slaveZoneDisplay',
        'web_port': 'webPort',
        'vip': 'vip'
    }

    def __init__(self, publicip=None, exp_time=None, start_time=None, end_time=None, release_time=None, name=None, instance_id=None, private_ip=None, task_status=None, status=None, created=None, region=None, zone=None, availability_zone_display=None, vpc_id=None, subnet_id=None, security_group_id=None, specification=None, update=None, createinstance_status=None, fail_reason=None, instance_key=None, order_id=None, period_num=None, resource_id=None, bastion_type=None, alter_permit=None, public_id=None, bastion_version=None, new_bastion_version=None, instance_status=None, instance_description=None, slave_zone=None, enterprise_project_id=None, instance_type=None, ha_id=None, slave_zone_display=None, web_port=None, vip=None):
        r"""InstanceDetail

        The model defined in huaweicloud sdk

        :param publicip: 云堡垒机实例弹性公网IP，返回默认值null
        :type publicip: str
        :param exp_time: 云堡垒机实例过期时间。
        :type exp_time: str
        :param start_time: 云堡垒机实例开始时间，使用时间戳格式表示。
        :type start_time: str
        :param end_time: 云堡垒机实例结束时间，使用时间戳格式表示。
        :type end_time: str
        :param release_time: 云堡垒机释放时间，使用时间戳格式表示。
        :type release_time: str
        :param name: 云堡垒机实例名称。
        :type name: str
        :param instance_id: 云堡垒机实例ID，UUID格式。
        :type instance_id: str
        :param private_ip: 云堡垒机实例私有ip。
        :type private_ip: str
        :param task_status: 云堡垒机实例当前的任务状态。 - powering-on 开启 - powering-off 关闭 - rebooting 重启 - delete_wait 删除 - frozen 冻结 - NO_TASK 运行 - unfrozen 解冻 - alter 变更 - updating 升级中 - configuring-ha 配置HA
        :type task_status: str
        :param status: 云堡垒机实例状态。 - SHUTOFF 已关闭 - ACTIVE 运行中 - DELETING 删除中 - BUILD 创建中 - DELETED 已删除 - ERROR 故障 - HAWAIT 等待备机创建成功 - FROZEN 已冻结 - UPGRADING 升级中 - UNPAID 待支付 - RESIZE 规格变更中 - DILATATION 扩容中 - HA 配置HA中
        :type status: str
        :param created: 云堡垒机实例创建时间，使用UTC时间表示。
        :type created: str
        :param region: 云堡垒机实例所在局点。
        :type region: str
        :param zone: 云堡垒机实例所在可用区。
        :type zone: str
        :param availability_zone_display: 云堡垒机实例所在可用区中文名称。
        :type availability_zone_display: str
        :param vpc_id: 云堡垒机实例所在虚拟私有云的VPC ID。
        :type vpc_id: str
        :param subnet_id: 云堡垒机实例所在子网的ID。
        :type subnet_id: str
        :param security_group_id: 云堡垒机实例所属的安全组的ID。
        :type security_group_id: str
        :param specification: 云堡垒机实例规格。
        :type specification: str
        :param update: 云堡垒机实例是否可以升级。 - NEW，可以升级 - OLD，不能升级
        :type update: str
        :param createinstance_status: 云堡垒机实例在创建实例过程中的过程状态信息。 - Waiting for payment，等待支付 - creating-network，创建网络 - creating-server，创建服务 - tranfering-horizontal-network，网络打通 - adding-policy-route，添加路由策略 - configing-dns，配置DNS - starting-cbs-service，服务运行中 - setting-init-conf，初始化 - buying-EIP，购买弹性公网IP
        :type createinstance_status: str
        :param fail_reason: 云堡垒机实例创建实例失败原因。
        :type fail_reason: str
        :param instance_key: 云堡垒机实例key。
        :type instance_key: str
        :param order_id: 订单ID。
        :type order_id: str
        :param period_num: 云堡垒机实例订购周期数。
        :type period_num: str
        :param resource_id: 云堡垒机实例的资源id,UUID格式显示。
        :type resource_id: str
        :param bastion_type: 云堡垒机实例堡垒机类型。 - OEM
        :type bastion_type: str
        :param alter_permit: 云堡垒机实例是否可以扩容。 - 1 开启扩容 - 0 关闭扩容
        :type alter_permit: str
        :param public_id: 云堡垒机实例绑定公网的弹性IP的ID，UUID格式表示。
        :type public_id: str
        :param bastion_version: 云堡垒机实例当前版本。
        :type bastion_version: str
        :param new_bastion_version: 云堡垒机实例可以升级的版本。
        :type new_bastion_version: str
        :param instance_status: 云堡垒机实例状态。 - building  创建中 - deleting  删除中 - deleted 删除了 - unpaid  未支付 - upgrading 升级中 - resizing  扩容中 - abnormal  异常 - error 故障 - ok  正常
        :type instance_status: str
        :param instance_description: 云堡垒机实例状态描述。
        :type instance_description: str
        :param slave_zone: 备可用分区，默认返回null。
        :type slave_zone: str
        :param enterprise_project_id: 云堡垒机实例所属企业项目ID。
        :type enterprise_project_id: str
        :param instance_type: 云堡垒机实例类型。 - null  单机默认返回null - master  HA时返回主机 - slave HA时返回备机
        :type instance_type: str
        :param ha_id: 云堡垒机实例主备ID。 - 单机堡垒机实例默认返回null - HA堡垒机实例返回主机HAID
        :type ha_id: str
        :param slave_zone_display: 云堡垒机实例备机可用分区名称。 单机堡垒机实例和备机堡垒机实例返回null，HA堡垒机实例主机返回备机所在可用区名称。
        :type slave_zone_display: str
        :param web_port: 云堡垒机实例WEB界面访问的端口号。
        :type web_port: str
        :param vip: 云堡垒机实例浮动ip。返回默认值null
        :type vip: str
        """
        
        

        self._publicip = None
        self._exp_time = None
        self._start_time = None
        self._end_time = None
        self._release_time = None
        self._name = None
        self._instance_id = None
        self._private_ip = None
        self._task_status = None
        self._status = None
        self._created = None
        self._region = None
        self._zone = None
        self._availability_zone_display = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._specification = None
        self._update = None
        self._createinstance_status = None
        self._fail_reason = None
        self._instance_key = None
        self._order_id = None
        self._period_num = None
        self._resource_id = None
        self._bastion_type = None
        self._alter_permit = None
        self._public_id = None
        self._bastion_version = None
        self._new_bastion_version = None
        self._instance_status = None
        self._instance_description = None
        self._slave_zone = None
        self._enterprise_project_id = None
        self._instance_type = None
        self._ha_id = None
        self._slave_zone_display = None
        self._web_port = None
        self._vip = None
        self.discriminator = None

        self.publicip = publicip
        self.exp_time = exp_time
        self.start_time = start_time
        self.end_time = end_time
        self.release_time = release_time
        self.name = name
        self.instance_id = instance_id
        self.private_ip = private_ip
        self.task_status = task_status
        self.status = status
        self.created = created
        self.region = region
        self.zone = zone
        self.availability_zone_display = availability_zone_display
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.specification = specification
        self.update = update
        self.createinstance_status = createinstance_status
        self.fail_reason = fail_reason
        self.instance_key = instance_key
        self.order_id = order_id
        self.period_num = period_num
        self.resource_id = resource_id
        self.bastion_type = bastion_type
        self.alter_permit = alter_permit
        self.public_id = public_id
        self.bastion_version = bastion_version
        self.new_bastion_version = new_bastion_version
        self.instance_status = instance_status
        self.instance_description = instance_description
        if slave_zone is not None:
            self.slave_zone = slave_zone
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if instance_type is not None:
            self.instance_type = instance_type
        if ha_id is not None:
            self.ha_id = ha_id
        if slave_zone_display is not None:
            self.slave_zone_display = slave_zone_display
        if web_port is not None:
            self.web_port = web_port
        if vip is not None:
            self.vip = vip

    @property
    def publicip(self):
        r"""Gets the publicip of this InstanceDetail.

        云堡垒机实例弹性公网IP，返回默认值null

        :return: The publicip of this InstanceDetail.
        :rtype: str
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        r"""Sets the publicip of this InstanceDetail.

        云堡垒机实例弹性公网IP，返回默认值null

        :param publicip: The publicip of this InstanceDetail.
        :type publicip: str
        """
        self._publicip = publicip

    @property
    def exp_time(self):
        r"""Gets the exp_time of this InstanceDetail.

        云堡垒机实例过期时间。

        :return: The exp_time of this InstanceDetail.
        :rtype: str
        """
        return self._exp_time

    @exp_time.setter
    def exp_time(self, exp_time):
        r"""Sets the exp_time of this InstanceDetail.

        云堡垒机实例过期时间。

        :param exp_time: The exp_time of this InstanceDetail.
        :type exp_time: str
        """
        self._exp_time = exp_time

    @property
    def start_time(self):
        r"""Gets the start_time of this InstanceDetail.

        云堡垒机实例开始时间，使用时间戳格式表示。

        :return: The start_time of this InstanceDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this InstanceDetail.

        云堡垒机实例开始时间，使用时间戳格式表示。

        :param start_time: The start_time of this InstanceDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this InstanceDetail.

        云堡垒机实例结束时间，使用时间戳格式表示。

        :return: The end_time of this InstanceDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this InstanceDetail.

        云堡垒机实例结束时间，使用时间戳格式表示。

        :param end_time: The end_time of this InstanceDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def release_time(self):
        r"""Gets the release_time of this InstanceDetail.

        云堡垒机释放时间，使用时间戳格式表示。

        :return: The release_time of this InstanceDetail.
        :rtype: str
        """
        return self._release_time

    @release_time.setter
    def release_time(self, release_time):
        r"""Sets the release_time of this InstanceDetail.

        云堡垒机释放时间，使用时间戳格式表示。

        :param release_time: The release_time of this InstanceDetail.
        :type release_time: str
        """
        self._release_time = release_time

    @property
    def name(self):
        r"""Gets the name of this InstanceDetail.

        云堡垒机实例名称。

        :return: The name of this InstanceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceDetail.

        云堡垒机实例名称。

        :param name: The name of this InstanceDetail.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceDetail.

        云堡垒机实例ID，UUID格式。

        :return: The instance_id of this InstanceDetail.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceDetail.

        云堡垒机实例ID，UUID格式。

        :param instance_id: The instance_id of this InstanceDetail.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this InstanceDetail.

        云堡垒机实例私有ip。

        :return: The private_ip of this InstanceDetail.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this InstanceDetail.

        云堡垒机实例私有ip。

        :param private_ip: The private_ip of this InstanceDetail.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def task_status(self):
        r"""Gets the task_status of this InstanceDetail.

        云堡垒机实例当前的任务状态。 - powering-on 开启 - powering-off 关闭 - rebooting 重启 - delete_wait 删除 - frozen 冻结 - NO_TASK 运行 - unfrozen 解冻 - alter 变更 - updating 升级中 - configuring-ha 配置HA

        :return: The task_status of this InstanceDetail.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this InstanceDetail.

        云堡垒机实例当前的任务状态。 - powering-on 开启 - powering-off 关闭 - rebooting 重启 - delete_wait 删除 - frozen 冻结 - NO_TASK 运行 - unfrozen 解冻 - alter 变更 - updating 升级中 - configuring-ha 配置HA

        :param task_status: The task_status of this InstanceDetail.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def status(self):
        r"""Gets the status of this InstanceDetail.

        云堡垒机实例状态。 - SHUTOFF 已关闭 - ACTIVE 运行中 - DELETING 删除中 - BUILD 创建中 - DELETED 已删除 - ERROR 故障 - HAWAIT 等待备机创建成功 - FROZEN 已冻结 - UPGRADING 升级中 - UNPAID 待支付 - RESIZE 规格变更中 - DILATATION 扩容中 - HA 配置HA中

        :return: The status of this InstanceDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceDetail.

        云堡垒机实例状态。 - SHUTOFF 已关闭 - ACTIVE 运行中 - DELETING 删除中 - BUILD 创建中 - DELETED 已删除 - ERROR 故障 - HAWAIT 等待备机创建成功 - FROZEN 已冻结 - UPGRADING 升级中 - UNPAID 待支付 - RESIZE 规格变更中 - DILATATION 扩容中 - HA 配置HA中

        :param status: The status of this InstanceDetail.
        :type status: str
        """
        self._status = status

    @property
    def created(self):
        r"""Gets the created of this InstanceDetail.

        云堡垒机实例创建时间，使用UTC时间表示。

        :return: The created of this InstanceDetail.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this InstanceDetail.

        云堡垒机实例创建时间，使用UTC时间表示。

        :param created: The created of this InstanceDetail.
        :type created: str
        """
        self._created = created

    @property
    def region(self):
        r"""Gets the region of this InstanceDetail.

        云堡垒机实例所在局点。

        :return: The region of this InstanceDetail.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this InstanceDetail.

        云堡垒机实例所在局点。

        :param region: The region of this InstanceDetail.
        :type region: str
        """
        self._region = region

    @property
    def zone(self):
        r"""Gets the zone of this InstanceDetail.

        云堡垒机实例所在可用区。

        :return: The zone of this InstanceDetail.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        r"""Sets the zone of this InstanceDetail.

        云堡垒机实例所在可用区。

        :param zone: The zone of this InstanceDetail.
        :type zone: str
        """
        self._zone = zone

    @property
    def availability_zone_display(self):
        r"""Gets the availability_zone_display of this InstanceDetail.

        云堡垒机实例所在可用区中文名称。

        :return: The availability_zone_display of this InstanceDetail.
        :rtype: str
        """
        return self._availability_zone_display

    @availability_zone_display.setter
    def availability_zone_display(self, availability_zone_display):
        r"""Sets the availability_zone_display of this InstanceDetail.

        云堡垒机实例所在可用区中文名称。

        :param availability_zone_display: The availability_zone_display of this InstanceDetail.
        :type availability_zone_display: str
        """
        self._availability_zone_display = availability_zone_display

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this InstanceDetail.

        云堡垒机实例所在虚拟私有云的VPC ID。

        :return: The vpc_id of this InstanceDetail.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this InstanceDetail.

        云堡垒机实例所在虚拟私有云的VPC ID。

        :param vpc_id: The vpc_id of this InstanceDetail.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this InstanceDetail.

        云堡垒机实例所在子网的ID。

        :return: The subnet_id of this InstanceDetail.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this InstanceDetail.

        云堡垒机实例所在子网的ID。

        :param subnet_id: The subnet_id of this InstanceDetail.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this InstanceDetail.

        云堡垒机实例所属的安全组的ID。

        :return: The security_group_id of this InstanceDetail.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this InstanceDetail.

        云堡垒机实例所属的安全组的ID。

        :param security_group_id: The security_group_id of this InstanceDetail.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def specification(self):
        r"""Gets the specification of this InstanceDetail.

        云堡垒机实例规格。

        :return: The specification of this InstanceDetail.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this InstanceDetail.

        云堡垒机实例规格。

        :param specification: The specification of this InstanceDetail.
        :type specification: str
        """
        self._specification = specification

    @property
    def update(self):
        r"""Gets the update of this InstanceDetail.

        云堡垒机实例是否可以升级。 - NEW，可以升级 - OLD，不能升级

        :return: The update of this InstanceDetail.
        :rtype: str
        """
        return self._update

    @update.setter
    def update(self, update):
        r"""Sets the update of this InstanceDetail.

        云堡垒机实例是否可以升级。 - NEW，可以升级 - OLD，不能升级

        :param update: The update of this InstanceDetail.
        :type update: str
        """
        self._update = update

    @property
    def createinstance_status(self):
        r"""Gets the createinstance_status of this InstanceDetail.

        云堡垒机实例在创建实例过程中的过程状态信息。 - Waiting for payment，等待支付 - creating-network，创建网络 - creating-server，创建服务 - tranfering-horizontal-network，网络打通 - adding-policy-route，添加路由策略 - configing-dns，配置DNS - starting-cbs-service，服务运行中 - setting-init-conf，初始化 - buying-EIP，购买弹性公网IP

        :return: The createinstance_status of this InstanceDetail.
        :rtype: str
        """
        return self._createinstance_status

    @createinstance_status.setter
    def createinstance_status(self, createinstance_status):
        r"""Sets the createinstance_status of this InstanceDetail.

        云堡垒机实例在创建实例过程中的过程状态信息。 - Waiting for payment，等待支付 - creating-network，创建网络 - creating-server，创建服务 - tranfering-horizontal-network，网络打通 - adding-policy-route，添加路由策略 - configing-dns，配置DNS - starting-cbs-service，服务运行中 - setting-init-conf，初始化 - buying-EIP，购买弹性公网IP

        :param createinstance_status: The createinstance_status of this InstanceDetail.
        :type createinstance_status: str
        """
        self._createinstance_status = createinstance_status

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this InstanceDetail.

        云堡垒机实例创建实例失败原因。

        :return: The fail_reason of this InstanceDetail.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this InstanceDetail.

        云堡垒机实例创建实例失败原因。

        :param fail_reason: The fail_reason of this InstanceDetail.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def instance_key(self):
        r"""Gets the instance_key of this InstanceDetail.

        云堡垒机实例key。

        :return: The instance_key of this InstanceDetail.
        :rtype: str
        """
        return self._instance_key

    @instance_key.setter
    def instance_key(self, instance_key):
        r"""Sets the instance_key of this InstanceDetail.

        云堡垒机实例key。

        :param instance_key: The instance_key of this InstanceDetail.
        :type instance_key: str
        """
        self._instance_key = instance_key

    @property
    def order_id(self):
        r"""Gets the order_id of this InstanceDetail.

        订单ID。

        :return: The order_id of this InstanceDetail.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this InstanceDetail.

        订单ID。

        :param order_id: The order_id of this InstanceDetail.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def period_num(self):
        r"""Gets the period_num of this InstanceDetail.

        云堡垒机实例订购周期数。

        :return: The period_num of this InstanceDetail.
        :rtype: str
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this InstanceDetail.

        云堡垒机实例订购周期数。

        :param period_num: The period_num of this InstanceDetail.
        :type period_num: str
        """
        self._period_num = period_num

    @property
    def resource_id(self):
        r"""Gets the resource_id of this InstanceDetail.

        云堡垒机实例的资源id,UUID格式显示。

        :return: The resource_id of this InstanceDetail.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this InstanceDetail.

        云堡垒机实例的资源id,UUID格式显示。

        :param resource_id: The resource_id of this InstanceDetail.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def bastion_type(self):
        r"""Gets the bastion_type of this InstanceDetail.

        云堡垒机实例堡垒机类型。 - OEM

        :return: The bastion_type of this InstanceDetail.
        :rtype: str
        """
        return self._bastion_type

    @bastion_type.setter
    def bastion_type(self, bastion_type):
        r"""Sets the bastion_type of this InstanceDetail.

        云堡垒机实例堡垒机类型。 - OEM

        :param bastion_type: The bastion_type of this InstanceDetail.
        :type bastion_type: str
        """
        self._bastion_type = bastion_type

    @property
    def alter_permit(self):
        r"""Gets the alter_permit of this InstanceDetail.

        云堡垒机实例是否可以扩容。 - 1 开启扩容 - 0 关闭扩容

        :return: The alter_permit of this InstanceDetail.
        :rtype: str
        """
        return self._alter_permit

    @alter_permit.setter
    def alter_permit(self, alter_permit):
        r"""Sets the alter_permit of this InstanceDetail.

        云堡垒机实例是否可以扩容。 - 1 开启扩容 - 0 关闭扩容

        :param alter_permit: The alter_permit of this InstanceDetail.
        :type alter_permit: str
        """
        self._alter_permit = alter_permit

    @property
    def public_id(self):
        r"""Gets the public_id of this InstanceDetail.

        云堡垒机实例绑定公网的弹性IP的ID，UUID格式表示。

        :return: The public_id of this InstanceDetail.
        :rtype: str
        """
        return self._public_id

    @public_id.setter
    def public_id(self, public_id):
        r"""Sets the public_id of this InstanceDetail.

        云堡垒机实例绑定公网的弹性IP的ID，UUID格式表示。

        :param public_id: The public_id of this InstanceDetail.
        :type public_id: str
        """
        self._public_id = public_id

    @property
    def bastion_version(self):
        r"""Gets the bastion_version of this InstanceDetail.

        云堡垒机实例当前版本。

        :return: The bastion_version of this InstanceDetail.
        :rtype: str
        """
        return self._bastion_version

    @bastion_version.setter
    def bastion_version(self, bastion_version):
        r"""Sets the bastion_version of this InstanceDetail.

        云堡垒机实例当前版本。

        :param bastion_version: The bastion_version of this InstanceDetail.
        :type bastion_version: str
        """
        self._bastion_version = bastion_version

    @property
    def new_bastion_version(self):
        r"""Gets the new_bastion_version of this InstanceDetail.

        云堡垒机实例可以升级的版本。

        :return: The new_bastion_version of this InstanceDetail.
        :rtype: str
        """
        return self._new_bastion_version

    @new_bastion_version.setter
    def new_bastion_version(self, new_bastion_version):
        r"""Sets the new_bastion_version of this InstanceDetail.

        云堡垒机实例可以升级的版本。

        :param new_bastion_version: The new_bastion_version of this InstanceDetail.
        :type new_bastion_version: str
        """
        self._new_bastion_version = new_bastion_version

    @property
    def instance_status(self):
        r"""Gets the instance_status of this InstanceDetail.

        云堡垒机实例状态。 - building  创建中 - deleting  删除中 - deleted 删除了 - unpaid  未支付 - upgrading 升级中 - resizing  扩容中 - abnormal  异常 - error 故障 - ok  正常

        :return: The instance_status of this InstanceDetail.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this InstanceDetail.

        云堡垒机实例状态。 - building  创建中 - deleting  删除中 - deleted 删除了 - unpaid  未支付 - upgrading 升级中 - resizing  扩容中 - abnormal  异常 - error 故障 - ok  正常

        :param instance_status: The instance_status of this InstanceDetail.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def instance_description(self):
        r"""Gets the instance_description of this InstanceDetail.

        云堡垒机实例状态描述。

        :return: The instance_description of this InstanceDetail.
        :rtype: str
        """
        return self._instance_description

    @instance_description.setter
    def instance_description(self, instance_description):
        r"""Sets the instance_description of this InstanceDetail.

        云堡垒机实例状态描述。

        :param instance_description: The instance_description of this InstanceDetail.
        :type instance_description: str
        """
        self._instance_description = instance_description

    @property
    def slave_zone(self):
        r"""Gets the slave_zone of this InstanceDetail.

        备可用分区，默认返回null。

        :return: The slave_zone of this InstanceDetail.
        :rtype: str
        """
        return self._slave_zone

    @slave_zone.setter
    def slave_zone(self, slave_zone):
        r"""Sets the slave_zone of this InstanceDetail.

        备可用分区，默认返回null。

        :param slave_zone: The slave_zone of this InstanceDetail.
        :type slave_zone: str
        """
        self._slave_zone = slave_zone

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this InstanceDetail.

        云堡垒机实例所属企业项目ID。

        :return: The enterprise_project_id of this InstanceDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this InstanceDetail.

        云堡垒机实例所属企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this InstanceDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this InstanceDetail.

        云堡垒机实例类型。 - null  单机默认返回null - master  HA时返回主机 - slave HA时返回备机

        :return: The instance_type of this InstanceDetail.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this InstanceDetail.

        云堡垒机实例类型。 - null  单机默认返回null - master  HA时返回主机 - slave HA时返回备机

        :param instance_type: The instance_type of this InstanceDetail.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def ha_id(self):
        r"""Gets the ha_id of this InstanceDetail.

        云堡垒机实例主备ID。 - 单机堡垒机实例默认返回null - HA堡垒机实例返回主机HAID

        :return: The ha_id of this InstanceDetail.
        :rtype: str
        """
        return self._ha_id

    @ha_id.setter
    def ha_id(self, ha_id):
        r"""Sets the ha_id of this InstanceDetail.

        云堡垒机实例主备ID。 - 单机堡垒机实例默认返回null - HA堡垒机实例返回主机HAID

        :param ha_id: The ha_id of this InstanceDetail.
        :type ha_id: str
        """
        self._ha_id = ha_id

    @property
    def slave_zone_display(self):
        r"""Gets the slave_zone_display of this InstanceDetail.

        云堡垒机实例备机可用分区名称。 单机堡垒机实例和备机堡垒机实例返回null，HA堡垒机实例主机返回备机所在可用区名称。

        :return: The slave_zone_display of this InstanceDetail.
        :rtype: str
        """
        return self._slave_zone_display

    @slave_zone_display.setter
    def slave_zone_display(self, slave_zone_display):
        r"""Sets the slave_zone_display of this InstanceDetail.

        云堡垒机实例备机可用分区名称。 单机堡垒机实例和备机堡垒机实例返回null，HA堡垒机实例主机返回备机所在可用区名称。

        :param slave_zone_display: The slave_zone_display of this InstanceDetail.
        :type slave_zone_display: str
        """
        self._slave_zone_display = slave_zone_display

    @property
    def web_port(self):
        r"""Gets the web_port of this InstanceDetail.

        云堡垒机实例WEB界面访问的端口号。

        :return: The web_port of this InstanceDetail.
        :rtype: str
        """
        return self._web_port

    @web_port.setter
    def web_port(self, web_port):
        r"""Sets the web_port of this InstanceDetail.

        云堡垒机实例WEB界面访问的端口号。

        :param web_port: The web_port of this InstanceDetail.
        :type web_port: str
        """
        self._web_port = web_port

    @property
    def vip(self):
        r"""Gets the vip of this InstanceDetail.

        云堡垒机实例浮动ip。返回默认值null

        :return: The vip of this InstanceDetail.
        :rtype: str
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        r"""Sets the vip of this InstanceDetail.

        云堡垒机实例浮动ip。返回默认值null

        :param vip: The vip of this InstanceDetail.
        :type vip: str
        """
        self._vip = vip

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
        if not isinstance(other, InstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
