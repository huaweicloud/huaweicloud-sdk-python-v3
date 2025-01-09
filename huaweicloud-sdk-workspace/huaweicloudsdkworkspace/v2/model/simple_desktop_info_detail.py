# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleDesktopInfoDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'computer_name': 'str',
        'os_host_name': 'str',
        'created': 'str',
        'ip_address': 'str',
        'user_name': 'str',
        'attach_user_infos': 'list[AttachInstancesUserInfo]',
        'user_group': 'str',
        'sid': 'str',
        'ou_name': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'in_maintenance_mode': 'bool',
        'share_resource_sku': 'str',
        'desktop_type': 'str',
        'subnet_id': 'str',
        'bill_resource_id': 'str',
        'status': 'str',
        'task_status': 'str',
        'instance_status': 'str',
        'connect_status': 'str',
        'product_name': 'str',
        'agent_version': 'str',
        'tenant_id': 'str',
        'tenant_name': 'str',
        'resource_pool_id': 'str',
        'os_type': 'str',
        'hibernate_policy_num': 'int',
        'is_auto_hibernate': 'int',
        'availability_zone': 'str',
        'exclusive_host_id': 'str',
        'deh_id': 'str'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'computer_name': 'computer_name',
        'os_host_name': 'os_host_name',
        'created': 'created',
        'ip_address': 'ip_address',
        'user_name': 'user_name',
        'attach_user_infos': 'attach_user_infos',
        'user_group': 'user_group',
        'sid': 'sid',
        'ou_name': 'ou_name',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'in_maintenance_mode': 'in_maintenance_mode',
        'share_resource_sku': 'share_resource_sku',
        'desktop_type': 'desktop_type',
        'subnet_id': 'subnet_id',
        'bill_resource_id': 'bill_resource_id',
        'status': 'status',
        'task_status': 'task_status',
        'instance_status': 'instance_status',
        'connect_status': 'connect_status',
        'product_name': 'product_name',
        'agent_version': 'agent_version',
        'tenant_id': 'tenant_id',
        'tenant_name': 'tenant_name',
        'resource_pool_id': 'resource_pool_id',
        'os_type': 'os_type',
        'hibernate_policy_num': 'hibernate_policy_num',
        'is_auto_hibernate': 'is_auto_hibernate',
        'availability_zone': 'availability_zone',
        'exclusive_host_id': 'exclusive_host_id',
        'deh_id': 'deh_id'
    }

    def __init__(self, desktop_id=None, computer_name=None, os_host_name=None, created=None, ip_address=None, user_name=None, attach_user_infos=None, user_group=None, sid=None, ou_name=None, enterprise_project_id=None, tags=None, in_maintenance_mode=None, share_resource_sku=None, desktop_type=None, subnet_id=None, bill_resource_id=None, status=None, task_status=None, instance_status=None, connect_status=None, product_name=None, agent_version=None, tenant_id=None, tenant_name=None, resource_pool_id=None, os_type=None, hibernate_policy_num=None, is_auto_hibernate=None, availability_zone=None, exclusive_host_id=None, deh_id=None):
        """SimpleDesktopInfoDetail

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param computer_name: 桌面名。
        :type computer_name: str
        :param os_host_name: 系统计算机名。
        :type os_host_name: str
        :param created: 创建时间。
        :type created: str
        :param ip_address: 桌面ip地址。
        :type ip_address: str
        :param user_name: 用户名。
        :type user_name: str
        :param attach_user_infos: 桌面已分配的用户信息列表。
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        :param user_group: 权限组。
        :type user_group: str
        :param sid: 桌面的SID信息。
        :type sid: str
        :param ou_name: ou名称。
        :type ou_name: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        :param in_maintenance_mode: 是否处于管理员维护模式
        :type in_maintenance_mode: bool
        :param share_resource_sku: 桌面协同资源SKU码
        :type share_resource_sku: str
        :param desktop_type: 桌面类型
        :type desktop_type: str
        :param subnet_id: 桌面的子网ID。
        :type subnet_id: str
        :param bill_resource_id: 桌面计费资源ID。
        :type bill_resource_id: str
        :param status: 运行状态
        :type status: str
        :param task_status: 桌面的任务状态。
        :type task_status: str
        :param instance_status: 系統状态
        :type instance_status: str
        :param connect_status: 连接状态
        :type connect_status: str
        :param product_name: 套餐名称
        :type product_name: str
        :param agent_version: AccessAgent版本号
        :type agent_version: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param tenant_name: 租户名称
        :type tenant_name: str
        :param resource_pool_id: 资源池ID
        :type resource_pool_id: str
        :param os_type: 操作系统类型：Linux、Windows或Others。
        :type os_type: str
        :param hibernate_policy_num: 智能休眠策略数。
        :type hibernate_policy_num: int
        :param is_auto_hibernate: 是否处于智能休眠中
        :type is_auto_hibernate: int
        :param availability_zone: 所属的可用区。
        :type availability_zone: str
        :param exclusive_host_id: 专享主机ID。
        :type exclusive_host_id: str
        :param deh_id: 云办公主机ID。
        :type deh_id: str
        """
        
        

        self._desktop_id = None
        self._computer_name = None
        self._os_host_name = None
        self._created = None
        self._ip_address = None
        self._user_name = None
        self._attach_user_infos = None
        self._user_group = None
        self._sid = None
        self._ou_name = None
        self._enterprise_project_id = None
        self._tags = None
        self._in_maintenance_mode = None
        self._share_resource_sku = None
        self._desktop_type = None
        self._subnet_id = None
        self._bill_resource_id = None
        self._status = None
        self._task_status = None
        self._instance_status = None
        self._connect_status = None
        self._product_name = None
        self._agent_version = None
        self._tenant_id = None
        self._tenant_name = None
        self._resource_pool_id = None
        self._os_type = None
        self._hibernate_policy_num = None
        self._is_auto_hibernate = None
        self._availability_zone = None
        self._exclusive_host_id = None
        self._deh_id = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if computer_name is not None:
            self.computer_name = computer_name
        if os_host_name is not None:
            self.os_host_name = os_host_name
        if created is not None:
            self.created = created
        if ip_address is not None:
            self.ip_address = ip_address
        if user_name is not None:
            self.user_name = user_name
        if attach_user_infos is not None:
            self.attach_user_infos = attach_user_infos
        if user_group is not None:
            self.user_group = user_group
        if sid is not None:
            self.sid = sid
        if ou_name is not None:
            self.ou_name = ou_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if in_maintenance_mode is not None:
            self.in_maintenance_mode = in_maintenance_mode
        if share_resource_sku is not None:
            self.share_resource_sku = share_resource_sku
        if desktop_type is not None:
            self.desktop_type = desktop_type
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if bill_resource_id is not None:
            self.bill_resource_id = bill_resource_id
        if status is not None:
            self.status = status
        if task_status is not None:
            self.task_status = task_status
        if instance_status is not None:
            self.instance_status = instance_status
        if connect_status is not None:
            self.connect_status = connect_status
        if product_name is not None:
            self.product_name = product_name
        if agent_version is not None:
            self.agent_version = agent_version
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if resource_pool_id is not None:
            self.resource_pool_id = resource_pool_id
        if os_type is not None:
            self.os_type = os_type
        if hibernate_policy_num is not None:
            self.hibernate_policy_num = hibernate_policy_num
        if is_auto_hibernate is not None:
            self.is_auto_hibernate = is_auto_hibernate
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if exclusive_host_id is not None:
            self.exclusive_host_id = exclusive_host_id
        if deh_id is not None:
            self.deh_id = deh_id

    @property
    def desktop_id(self):
        """Gets the desktop_id of this SimpleDesktopInfoDetail.

        桌面ID。

        :return: The desktop_id of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this SimpleDesktopInfoDetail.

        桌面ID。

        :param desktop_id: The desktop_id of this SimpleDesktopInfoDetail.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def computer_name(self):
        """Gets the computer_name of this SimpleDesktopInfoDetail.

        桌面名。

        :return: The computer_name of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this SimpleDesktopInfoDetail.

        桌面名。

        :param computer_name: The computer_name of this SimpleDesktopInfoDetail.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def os_host_name(self):
        """Gets the os_host_name of this SimpleDesktopInfoDetail.

        系统计算机名。

        :return: The os_host_name of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._os_host_name

    @os_host_name.setter
    def os_host_name(self, os_host_name):
        """Sets the os_host_name of this SimpleDesktopInfoDetail.

        系统计算机名。

        :param os_host_name: The os_host_name of this SimpleDesktopInfoDetail.
        :type os_host_name: str
        """
        self._os_host_name = os_host_name

    @property
    def created(self):
        """Gets the created of this SimpleDesktopInfoDetail.

        创建时间。

        :return: The created of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SimpleDesktopInfoDetail.

        创建时间。

        :param created: The created of this SimpleDesktopInfoDetail.
        :type created: str
        """
        self._created = created

    @property
    def ip_address(self):
        """Gets the ip_address of this SimpleDesktopInfoDetail.

        桌面ip地址。

        :return: The ip_address of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this SimpleDesktopInfoDetail.

        桌面ip地址。

        :param ip_address: The ip_address of this SimpleDesktopInfoDetail.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def user_name(self):
        """Gets the user_name of this SimpleDesktopInfoDetail.

        用户名。

        :return: The user_name of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SimpleDesktopInfoDetail.

        用户名。

        :param user_name: The user_name of this SimpleDesktopInfoDetail.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def attach_user_infos(self):
        """Gets the attach_user_infos of this SimpleDesktopInfoDetail.

        桌面已分配的用户信息列表。

        :return: The attach_user_infos of this SimpleDesktopInfoDetail.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        return self._attach_user_infos

    @attach_user_infos.setter
    def attach_user_infos(self, attach_user_infos):
        """Sets the attach_user_infos of this SimpleDesktopInfoDetail.

        桌面已分配的用户信息列表。

        :param attach_user_infos: The attach_user_infos of this SimpleDesktopInfoDetail.
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        self._attach_user_infos = attach_user_infos

    @property
    def user_group(self):
        """Gets the user_group of this SimpleDesktopInfoDetail.

        权限组。

        :return: The user_group of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this SimpleDesktopInfoDetail.

        权限组。

        :param user_group: The user_group of this SimpleDesktopInfoDetail.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def sid(self):
        """Gets the sid of this SimpleDesktopInfoDetail.

        桌面的SID信息。

        :return: The sid of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this SimpleDesktopInfoDetail.

        桌面的SID信息。

        :param sid: The sid of this SimpleDesktopInfoDetail.
        :type sid: str
        """
        self._sid = sid

    @property
    def ou_name(self):
        """Gets the ou_name of this SimpleDesktopInfoDetail.

        ou名称。

        :return: The ou_name of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        """Sets the ou_name of this SimpleDesktopInfoDetail.

        ou名称。

        :param ou_name: The ou_name of this SimpleDesktopInfoDetail.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SimpleDesktopInfoDetail.

        企业项目ID

        :return: The enterprise_project_id of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SimpleDesktopInfoDetail.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this SimpleDesktopInfoDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this SimpleDesktopInfoDetail.

        标签列表。

        :return: The tags of this SimpleDesktopInfoDetail.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SimpleDesktopInfoDetail.

        标签列表。

        :param tags: The tags of this SimpleDesktopInfoDetail.
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        self._tags = tags

    @property
    def in_maintenance_mode(self):
        """Gets the in_maintenance_mode of this SimpleDesktopInfoDetail.

        是否处于管理员维护模式

        :return: The in_maintenance_mode of this SimpleDesktopInfoDetail.
        :rtype: bool
        """
        return self._in_maintenance_mode

    @in_maintenance_mode.setter
    def in_maintenance_mode(self, in_maintenance_mode):
        """Sets the in_maintenance_mode of this SimpleDesktopInfoDetail.

        是否处于管理员维护模式

        :param in_maintenance_mode: The in_maintenance_mode of this SimpleDesktopInfoDetail.
        :type in_maintenance_mode: bool
        """
        self._in_maintenance_mode = in_maintenance_mode

    @property
    def share_resource_sku(self):
        """Gets the share_resource_sku of this SimpleDesktopInfoDetail.

        桌面协同资源SKU码

        :return: The share_resource_sku of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._share_resource_sku

    @share_resource_sku.setter
    def share_resource_sku(self, share_resource_sku):
        """Sets the share_resource_sku of this SimpleDesktopInfoDetail.

        桌面协同资源SKU码

        :param share_resource_sku: The share_resource_sku of this SimpleDesktopInfoDetail.
        :type share_resource_sku: str
        """
        self._share_resource_sku = share_resource_sku

    @property
    def desktop_type(self):
        """Gets the desktop_type of this SimpleDesktopInfoDetail.

        桌面类型

        :return: The desktop_type of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        """Sets the desktop_type of this SimpleDesktopInfoDetail.

        桌面类型

        :param desktop_type: The desktop_type of this SimpleDesktopInfoDetail.
        :type desktop_type: str
        """
        self._desktop_type = desktop_type

    @property
    def subnet_id(self):
        """Gets the subnet_id of this SimpleDesktopInfoDetail.

        桌面的子网ID。

        :return: The subnet_id of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this SimpleDesktopInfoDetail.

        桌面的子网ID。

        :param subnet_id: The subnet_id of this SimpleDesktopInfoDetail.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def bill_resource_id(self):
        """Gets the bill_resource_id of this SimpleDesktopInfoDetail.

        桌面计费资源ID。

        :return: The bill_resource_id of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._bill_resource_id

    @bill_resource_id.setter
    def bill_resource_id(self, bill_resource_id):
        """Sets the bill_resource_id of this SimpleDesktopInfoDetail.

        桌面计费资源ID。

        :param bill_resource_id: The bill_resource_id of this SimpleDesktopInfoDetail.
        :type bill_resource_id: str
        """
        self._bill_resource_id = bill_resource_id

    @property
    def status(self):
        """Gets the status of this SimpleDesktopInfoDetail.

        运行状态

        :return: The status of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SimpleDesktopInfoDetail.

        运行状态

        :param status: The status of this SimpleDesktopInfoDetail.
        :type status: str
        """
        self._status = status

    @property
    def task_status(self):
        """Gets the task_status of this SimpleDesktopInfoDetail.

        桌面的任务状态。

        :return: The task_status of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this SimpleDesktopInfoDetail.

        桌面的任务状态。

        :param task_status: The task_status of this SimpleDesktopInfoDetail.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def instance_status(self):
        """Gets the instance_status of this SimpleDesktopInfoDetail.

        系統状态

        :return: The instance_status of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this SimpleDesktopInfoDetail.

        系統状态

        :param instance_status: The instance_status of this SimpleDesktopInfoDetail.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def connect_status(self):
        """Gets the connect_status of this SimpleDesktopInfoDetail.

        连接状态

        :return: The connect_status of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._connect_status

    @connect_status.setter
    def connect_status(self, connect_status):
        """Sets the connect_status of this SimpleDesktopInfoDetail.

        连接状态

        :param connect_status: The connect_status of this SimpleDesktopInfoDetail.
        :type connect_status: str
        """
        self._connect_status = connect_status

    @property
    def product_name(self):
        """Gets the product_name of this SimpleDesktopInfoDetail.

        套餐名称

        :return: The product_name of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this SimpleDesktopInfoDetail.

        套餐名称

        :param product_name: The product_name of this SimpleDesktopInfoDetail.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def agent_version(self):
        """Gets the agent_version of this SimpleDesktopInfoDetail.

        AccessAgent版本号

        :return: The agent_version of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this SimpleDesktopInfoDetail.

        AccessAgent版本号

        :param agent_version: The agent_version of this SimpleDesktopInfoDetail.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def tenant_id(self):
        """Gets the tenant_id of this SimpleDesktopInfoDetail.

        租户ID

        :return: The tenant_id of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this SimpleDesktopInfoDetail.

        租户ID

        :param tenant_id: The tenant_id of this SimpleDesktopInfoDetail.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        """Gets the tenant_name of this SimpleDesktopInfoDetail.

        租户名称

        :return: The tenant_name of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this SimpleDesktopInfoDetail.

        租户名称

        :param tenant_name: The tenant_name of this SimpleDesktopInfoDetail.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def resource_pool_id(self):
        """Gets the resource_pool_id of this SimpleDesktopInfoDetail.

        资源池ID

        :return: The resource_pool_id of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._resource_pool_id

    @resource_pool_id.setter
    def resource_pool_id(self, resource_pool_id):
        """Sets the resource_pool_id of this SimpleDesktopInfoDetail.

        资源池ID

        :param resource_pool_id: The resource_pool_id of this SimpleDesktopInfoDetail.
        :type resource_pool_id: str
        """
        self._resource_pool_id = resource_pool_id

    @property
    def os_type(self):
        """Gets the os_type of this SimpleDesktopInfoDetail.

        操作系统类型：Linux、Windows或Others。

        :return: The os_type of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this SimpleDesktopInfoDetail.

        操作系统类型：Linux、Windows或Others。

        :param os_type: The os_type of this SimpleDesktopInfoDetail.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def hibernate_policy_num(self):
        """Gets the hibernate_policy_num of this SimpleDesktopInfoDetail.

        智能休眠策略数。

        :return: The hibernate_policy_num of this SimpleDesktopInfoDetail.
        :rtype: int
        """
        return self._hibernate_policy_num

    @hibernate_policy_num.setter
    def hibernate_policy_num(self, hibernate_policy_num):
        """Sets the hibernate_policy_num of this SimpleDesktopInfoDetail.

        智能休眠策略数。

        :param hibernate_policy_num: The hibernate_policy_num of this SimpleDesktopInfoDetail.
        :type hibernate_policy_num: int
        """
        self._hibernate_policy_num = hibernate_policy_num

    @property
    def is_auto_hibernate(self):
        """Gets the is_auto_hibernate of this SimpleDesktopInfoDetail.

        是否处于智能休眠中

        :return: The is_auto_hibernate of this SimpleDesktopInfoDetail.
        :rtype: int
        """
        return self._is_auto_hibernate

    @is_auto_hibernate.setter
    def is_auto_hibernate(self, is_auto_hibernate):
        """Sets the is_auto_hibernate of this SimpleDesktopInfoDetail.

        是否处于智能休眠中

        :param is_auto_hibernate: The is_auto_hibernate of this SimpleDesktopInfoDetail.
        :type is_auto_hibernate: int
        """
        self._is_auto_hibernate = is_auto_hibernate

    @property
    def availability_zone(self):
        """Gets the availability_zone of this SimpleDesktopInfoDetail.

        所属的可用区。

        :return: The availability_zone of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this SimpleDesktopInfoDetail.

        所属的可用区。

        :param availability_zone: The availability_zone of this SimpleDesktopInfoDetail.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def exclusive_host_id(self):
        """Gets the exclusive_host_id of this SimpleDesktopInfoDetail.

        专享主机ID。

        :return: The exclusive_host_id of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._exclusive_host_id

    @exclusive_host_id.setter
    def exclusive_host_id(self, exclusive_host_id):
        """Sets the exclusive_host_id of this SimpleDesktopInfoDetail.

        专享主机ID。

        :param exclusive_host_id: The exclusive_host_id of this SimpleDesktopInfoDetail.
        :type exclusive_host_id: str
        """
        self._exclusive_host_id = exclusive_host_id

    @property
    def deh_id(self):
        """Gets the deh_id of this SimpleDesktopInfoDetail.

        云办公主机ID。

        :return: The deh_id of this SimpleDesktopInfoDetail.
        :rtype: str
        """
        return self._deh_id

    @deh_id.setter
    def deh_id(self, deh_id):
        """Sets the deh_id of this SimpleDesktopInfoDetail.

        云办公主机ID。

        :param deh_id: The deh_id of this SimpleDesktopInfoDetail.
        :type deh_id: str
        """
        self._deh_id = deh_id

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
        if not isinstance(other, SimpleDesktopInfoDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
