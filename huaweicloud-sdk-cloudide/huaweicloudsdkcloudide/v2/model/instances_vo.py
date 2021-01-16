# coding: utf-8

import pprint
import re

import six





class InstancesVO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'action_list': 'list[RoleAction]',
        'arch': 'str',
        'attributes': 'Attributes',
        'cpu_memory': 'str',
        'created_time': 'str',
        'description': 'str',
        'display_name': 'str',
        'domain_name': 'str',
        'id': 'str',
        'is_temporary': 'bool',
        'label': 'str',
        'link': 'str',
        'name': 'str',
        'organization_id': 'str',
        'owner_id': 'str',
        'owner_name': 'str',
        'platform_id': 'int',
        'private': 'bool',
        'pvc_quantity': 'str',
        'refresh_interval': 'int',
        'region': 'str',
        'role': 'Role',
        'role_id': 'str',
        'server_map': 'dict(str, str)',
        'server_url': 'str',
        'stack_id': 'str',
        'status': 'str',
        'sub_org': 'str',
        'updated_time': 'str'
    }

    attribute_map = {
        'action_list': 'action_list',
        'arch': 'arch',
        'attributes': 'attributes',
        'cpu_memory': 'cpu_memory',
        'created_time': 'created_time',
        'description': 'description',
        'display_name': 'display_name',
        'domain_name': 'domain_name',
        'id': 'id',
        'is_temporary': 'is_temporary',
        'label': 'label',
        'link': 'link',
        'name': 'name',
        'organization_id': 'organization_id',
        'owner_id': 'owner_id',
        'owner_name': 'owner_name',
        'platform_id': 'platform_id',
        'private': 'private',
        'pvc_quantity': 'pvc_quantity',
        'refresh_interval': 'refresh_interval',
        'region': 'region',
        'role': 'role',
        'role_id': 'role_id',
        'server_map': 'server_map',
        'server_url': 'server_url',
        'stack_id': 'stack_id',
        'status': 'status',
        'sub_org': 'sub_org',
        'updated_time': 'updated_time'
    }

    def __init__(self, action_list=None, arch=None, attributes=None, cpu_memory=None, created_time=None, description=None, display_name=None, domain_name=None, id=None, is_temporary=None, label=None, link=None, name=None, organization_id=None, owner_id=None, owner_name=None, platform_id=None, private=None, pvc_quantity=None, refresh_interval=None, region=None, role=None, role_id=None, server_map=None, server_url=None, stack_id=None, status=None, sub_org=None, updated_time=None):
        """InstancesVO - a model defined in huaweicloud sdk"""
        
        

        self._action_list = None
        self._arch = None
        self._attributes = None
        self._cpu_memory = None
        self._created_time = None
        self._description = None
        self._display_name = None
        self._domain_name = None
        self._id = None
        self._is_temporary = None
        self._label = None
        self._link = None
        self._name = None
        self._organization_id = None
        self._owner_id = None
        self._owner_name = None
        self._platform_id = None
        self._private = None
        self._pvc_quantity = None
        self._refresh_interval = None
        self._region = None
        self._role = None
        self._role_id = None
        self._server_map = None
        self._server_url = None
        self._stack_id = None
        self._status = None
        self._sub_org = None
        self._updated_time = None
        self.discriminator = None

        if action_list is not None:
            self.action_list = action_list
        if arch is not None:
            self.arch = arch
        if attributes is not None:
            self.attributes = attributes
        if cpu_memory is not None:
            self.cpu_memory = cpu_memory
        if created_time is not None:
            self.created_time = created_time
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if domain_name is not None:
            self.domain_name = domain_name
        if id is not None:
            self.id = id
        if is_temporary is not None:
            self.is_temporary = is_temporary
        if label is not None:
            self.label = label
        if link is not None:
            self.link = link
        if name is not None:
            self.name = name
        if organization_id is not None:
            self.organization_id = organization_id
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_name is not None:
            self.owner_name = owner_name
        if platform_id is not None:
            self.platform_id = platform_id
        if private is not None:
            self.private = private
        if pvc_quantity is not None:
            self.pvc_quantity = pvc_quantity
        if refresh_interval is not None:
            self.refresh_interval = refresh_interval
        if region is not None:
            self.region = region
        if role is not None:
            self.role = role
        if role_id is not None:
            self.role_id = role_id
        if server_map is not None:
            self.server_map = server_map
        if server_url is not None:
            self.server_url = server_url
        if stack_id is not None:
            self.stack_id = stack_id
        if status is not None:
            self.status = status
        if sub_org is not None:
            self.sub_org = sub_org
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def action_list(self):
        """Gets the action_list of this InstancesVO.

        角色权限列表

        :return: The action_list of this InstancesVO.
        :rtype: list[RoleAction]
        """
        return self._action_list

    @action_list.setter
    def action_list(self, action_list):
        """Sets the action_list of this InstancesVO.

        角色权限列表

        :param action_list: The action_list of this InstancesVO.
        :type: list[RoleAction]
        """
        self._action_list = action_list

    @property
    def arch(self):
        """Gets the arch of this InstancesVO.

        cpu架构 x86|arm

        :return: The arch of this InstancesVO.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this InstancesVO.

        cpu架构 x86|arm

        :param arch: The arch of this InstancesVO.
        :type: str
        """
        self._arch = arch

    @property
    def attributes(self):
        """Gets the attributes of this InstancesVO.


        :return: The attributes of this InstancesVO.
        :rtype: Attributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this InstancesVO.


        :param attributes: The attributes of this InstancesVO.
        :type: Attributes
        """
        self._attributes = attributes

    @property
    def cpu_memory(self):
        """Gets the cpu_memory of this InstancesVO.

        cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacksByTag接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G

        :return: The cpu_memory of this InstancesVO.
        :rtype: str
        """
        return self._cpu_memory

    @cpu_memory.setter
    def cpu_memory(self, cpu_memory):
        """Sets the cpu_memory of this InstancesVO.

        cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacksByTag接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G

        :param cpu_memory: The cpu_memory of this InstancesVO.
        :type: str
        """
        self._cpu_memory = cpu_memory

    @property
    def created_time(self):
        """Gets the created_time of this InstancesVO.

        创建时间

        :return: The created_time of this InstancesVO.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this InstancesVO.

        创建时间

        :param created_time: The created_time of this InstancesVO.
        :type: str
        """
        self._created_time = created_time

    @property
    def description(self):
        """Gets the description of this InstancesVO.

        描述

        :return: The description of this InstancesVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstancesVO.

        描述

        :param description: The description of this InstancesVO.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this InstancesVO.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :return: The display_name of this InstancesVO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InstancesVO.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :param display_name: The display_name of this InstancesVO.
        :type: str
        """
        self._display_name = display_name

    @property
    def domain_name(self):
        """Gets the domain_name of this InstancesVO.

        组织名

        :return: The domain_name of this InstancesVO.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this InstancesVO.

        组织名

        :param domain_name: The domain_name of this InstancesVO.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def id(self):
        """Gets the id of this InstancesVO.

        id

        :return: The id of this InstancesVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstancesVO.

        id

        :param id: The id of this InstancesVO.
        :type: str
        """
        self._id = id

    @property
    def is_temporary(self):
        """Gets the is_temporary of this InstancesVO.

        是否页面显示（以标签配置为准）

        :return: The is_temporary of this InstancesVO.
        :rtype: bool
        """
        return self._is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary):
        """Sets the is_temporary of this InstancesVO.

        是否页面显示（以标签配置为准）

        :param is_temporary: The is_temporary of this InstancesVO.
        :type: bool
        """
        self._is_temporary = is_temporary

    @property
    def label(self):
        """Gets the label of this InstancesVO.

        标签

        :return: The label of this InstancesVO.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this InstancesVO.

        标签

        :param label: The label of this InstancesVO.
        :type: str
        """
        self._label = label

    @property
    def link(self):
        """Gets the link of this InstancesVO.

        链接

        :return: The link of this InstancesVO.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this InstancesVO.

        链接

        :param link: The link of this InstancesVO.
        :type: str
        """
        self._link = link

    @property
    def name(self):
        """Gets the name of this InstancesVO.

        名称

        :return: The name of this InstancesVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstancesVO.

        名称

        :param name: The name of this InstancesVO.
        :type: str
        """
        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this InstancesVO.

        组织id（对应华为云账号的domainId）

        :return: The organization_id of this InstancesVO.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this InstancesVO.

        组织id（对应华为云账号的domainId）

        :param organization_id: The organization_id of this InstancesVO.
        :type: str
        """
        self._organization_id = organization_id

    @property
    def owner_id(self):
        """Gets the owner_id of this InstancesVO.

        用户id

        :return: The owner_id of this InstancesVO.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this InstancesVO.

        用户id

        :param owner_id: The owner_id of this InstancesVO.
        :type: str
        """
        self._owner_id = owner_id

    @property
    def owner_name(self):
        """Gets the owner_name of this InstancesVO.

        用户名

        :return: The owner_name of this InstancesVO.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this InstancesVO.

        用户名

        :param owner_name: The owner_name of this InstancesVO.
        :type: str
        """
        self._owner_name = owner_name

    @property
    def platform_id(self):
        """Gets the platform_id of this InstancesVO.

        平台ID

        :return: The platform_id of this InstancesVO.
        :rtype: int
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this InstancesVO.

        平台ID

        :param platform_id: The platform_id of this InstancesVO.
        :type: int
        """
        self._platform_id = platform_id

    @property
    def private(self):
        """Gets the private of this InstancesVO.

        是否私有平台

        :return: The private of this InstancesVO.
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this InstancesVO.

        是否私有平台

        :param private: The private of this InstancesVO.
        :type: bool
        """
        self._private = private

    @property
    def pvc_quantity(self):
        """Gets the pvc_quantity of this InstancesVO.

        PVC规格 5GB|10GB|20GB

        :return: The pvc_quantity of this InstancesVO.
        :rtype: str
        """
        return self._pvc_quantity

    @pvc_quantity.setter
    def pvc_quantity(self, pvc_quantity):
        """Sets the pvc_quantity of this InstancesVO.

        PVC规格 5GB|10GB|20GB

        :param pvc_quantity: The pvc_quantity of this InstancesVO.
        :type: str
        """
        self._pvc_quantity = pvc_quantity

    @property
    def refresh_interval(self):
        """Gets the refresh_interval of this InstancesVO.

        实例的生命周期。 arm架构,生命周期只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例在到达生命周期后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止。

        :return: The refresh_interval of this InstancesVO.
        :rtype: int
        """
        return self._refresh_interval

    @refresh_interval.setter
    def refresh_interval(self, refresh_interval):
        """Sets the refresh_interval of this InstancesVO.

        实例的生命周期。 arm架构,生命周期只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例在到达生命周期后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止。

        :param refresh_interval: The refresh_interval of this InstancesVO.
        :type: int
        """
        self._refresh_interval = refresh_interval

    @property
    def region(self):
        """Gets the region of this InstancesVO.

        区域

        :return: The region of this InstancesVO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this InstancesVO.

        区域

        :param region: The region of this InstancesVO.
        :type: str
        """
        self._region = region

    @property
    def role(self):
        """Gets the role of this InstancesVO.


        :return: The role of this InstancesVO.
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InstancesVO.


        :param role: The role of this InstancesVO.
        :type: Role
        """
        self._role = role

    @property
    def role_id(self):
        """Gets the role_id of this InstancesVO.

        角色id

        :return: The role_id of this InstancesVO.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this InstancesVO.

        角色id

        :param role_id: The role_id of this InstancesVO.
        :type: str
        """
        self._role_id = role_id

    @property
    def server_map(self):
        """Gets the server_map of this InstancesVO.

        server

        :return: The server_map of this InstancesVO.
        :rtype: dict(str, str)
        """
        return self._server_map

    @server_map.setter
    def server_map(self, server_map):
        """Sets the server_map of this InstancesVO.

        server

        :param server_map: The server_map of this InstancesVO.
        :type: dict(str, str)
        """
        self._server_map = server_map

    @property
    def server_url(self):
        """Gets the server_url of this InstancesVO.

        服务链接

        :return: The server_url of this InstancesVO.
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """Sets the server_url of this InstancesVO.

        服务链接

        :param server_url: The server_url of this InstancesVO.
        :type: str
        """
        self._server_url = server_url

    @property
    def stack_id(self):
        """Gets the stack_id of this InstancesVO.

        技术栈ID，通过技术栈管理ListStacksByTag接口获取。

        :return: The stack_id of this InstancesVO.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this InstancesVO.

        技术栈ID，通过技术栈管理ListStacksByTag接口获取。

        :param stack_id: The stack_id of this InstancesVO.
        :type: str
        """
        self._stack_id = stack_id

    @property
    def status(self):
        """Gets the status of this InstancesVO.

        实例状态

        :return: The status of this InstancesVO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstancesVO.

        实例状态

        :param status: The status of this InstancesVO.
        :type: str
        """
        self._status = status

    @property
    def sub_org(self):
        """Gets the sub_org of this InstancesVO.

        子组织

        :return: The sub_org of this InstancesVO.
        :rtype: str
        """
        return self._sub_org

    @sub_org.setter
    def sub_org(self, sub_org):
        """Sets the sub_org of this InstancesVO.

        子组织

        :param sub_org: The sub_org of this InstancesVO.
        :type: str
        """
        self._sub_org = sub_org

    @property
    def updated_time(self):
        """Gets the updated_time of this InstancesVO.

        更新时间

        :return: The updated_time of this InstancesVO.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this InstancesVO.

        更新时间

        :param updated_time: The updated_time of this InstancesVO.
        :type: str
        """
        self._updated_time = updated_time

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
        if not isinstance(other, InstancesVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
