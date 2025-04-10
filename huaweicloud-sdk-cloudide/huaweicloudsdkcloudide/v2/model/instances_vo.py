# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'server_map': 'dict(str, str)',
        'server_url': 'str',
        'stack_id': 'str',
        'status': 'str',
        'updated_time': 'str',
        'visitor_id': 'str',
        'visitor_name': 'str',
        'visitor_domain_name': 'str'
    }

    attribute_map = {
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
        'server_map': 'server_map',
        'server_url': 'server_url',
        'stack_id': 'stack_id',
        'status': 'status',
        'updated_time': 'updated_time',
        'visitor_id': 'visitor_id',
        'visitor_name': 'visitor_name',
        'visitor_domain_name': 'visitor_domain_name'
    }

    def __init__(self, arch=None, attributes=None, cpu_memory=None, created_time=None, description=None, display_name=None, domain_name=None, id=None, is_temporary=None, label=None, link=None, name=None, organization_id=None, owner_id=None, owner_name=None, platform_id=None, private=None, pvc_quantity=None, refresh_interval=None, region=None, server_map=None, server_url=None, stack_id=None, status=None, updated_time=None, visitor_id=None, visitor_name=None, visitor_domain_name=None):
        r"""InstancesVO

        The model defined in huaweicloud sdk

        :param arch: cpu架构 x86|arm
        :type arch: str
        :param attributes: 
        :type attributes: :class:`huaweicloudsdkcloudide.v2.Attributes`
        :param cpu_memory: cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacks接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G
        :type cpu_memory: str
        :param created_time: 创建时间
        :type created_time: str
        :param description: 描述
        :type description: str
        :param display_name: 实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间
        :type display_name: str
        :param domain_name: 租户名
        :type domain_name: str
        :param id: id
        :type id: str
        :param is_temporary: 是否页面显示（以标签配置为准）
        :type is_temporary: bool
        :param label: 标签
        :type label: str
        :param link: 链接
        :type link: str
        :param name: 名称
        :type name: str
        :param organization_id: 租户id（对应华为云帐号的domainId）
        :type organization_id: str
        :param owner_id: 用户id
        :type owner_id: str
        :param owner_name: 用户名
        :type owner_name: str
        :param platform_id: 平台ID
        :type platform_id: int
        :param private: 是否私有平台
        :type private: bool
        :param pvc_quantity: PVC规格 5GB|10GB|20GB
        :type pvc_quantity: str
        :param refresh_interval: 自动休眠时长。 arm架构,自动休眠时长只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例无操作超过自动休眠时长后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止
        :type refresh_interval: int
        :param region: 区域
        :type region: str
        :param server_map: server
        :type server_map: dict(str, str)
        :param server_url: 服务链接
        :type server_url: str
        :param stack_id: 技术栈ID，通过技术栈管理ListStacks接口获取。
        :type stack_id: str
        :param status: 实例状态 。 - INIT 初始化 - STARTING 启动中 - RUNNING 运行中 - STOPPING 停止中 - STOPPED 已停止 - DELETING 删除中 - DELETED 已删除 - DELETE_FAILED 删除失败
        :type status: str
        :param updated_time: 更新时间
        :type updated_time: str
        :param visitor_id: 访问者id
        :type visitor_id: str
        :param visitor_name: 访问者名称
        :type visitor_name: str
        :param visitor_domain_name: 访问者租户名称
        :type visitor_domain_name: str
        """
        
        

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
        self._server_map = None
        self._server_url = None
        self._stack_id = None
        self._status = None
        self._updated_time = None
        self._visitor_id = None
        self._visitor_name = None
        self._visitor_domain_name = None
        self.discriminator = None

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
        if server_map is not None:
            self.server_map = server_map
        if server_url is not None:
            self.server_url = server_url
        if stack_id is not None:
            self.stack_id = stack_id
        if status is not None:
            self.status = status
        if updated_time is not None:
            self.updated_time = updated_time
        if visitor_id is not None:
            self.visitor_id = visitor_id
        if visitor_name is not None:
            self.visitor_name = visitor_name
        if visitor_domain_name is not None:
            self.visitor_domain_name = visitor_domain_name

    @property
    def arch(self):
        r"""Gets the arch of this InstancesVO.

        cpu架构 x86|arm

        :return: The arch of this InstancesVO.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this InstancesVO.

        cpu架构 x86|arm

        :param arch: The arch of this InstancesVO.
        :type arch: str
        """
        self._arch = arch

    @property
    def attributes(self):
        r"""Gets the attributes of this InstancesVO.

        :return: The attributes of this InstancesVO.
        :rtype: :class:`huaweicloudsdkcloudide.v2.Attributes`
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this InstancesVO.

        :param attributes: The attributes of this InstancesVO.
        :type attributes: :class:`huaweicloudsdkcloudide.v2.Attributes`
        """
        self._attributes = attributes

    @property
    def cpu_memory(self):
        r"""Gets the cpu_memory of this InstancesVO.

        cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacks接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G

        :return: The cpu_memory of this InstancesVO.
        :rtype: str
        """
        return self._cpu_memory

    @cpu_memory.setter
    def cpu_memory(self, cpu_memory):
        r"""Sets the cpu_memory of this InstancesVO.

        cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacks接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G

        :param cpu_memory: The cpu_memory of this InstancesVO.
        :type cpu_memory: str
        """
        self._cpu_memory = cpu_memory

    @property
    def created_time(self):
        r"""Gets the created_time of this InstancesVO.

        创建时间

        :return: The created_time of this InstancesVO.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this InstancesVO.

        创建时间

        :param created_time: The created_time of this InstancesVO.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def description(self):
        r"""Gets the description of this InstancesVO.

        描述

        :return: The description of this InstancesVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InstancesVO.

        描述

        :param description: The description of this InstancesVO.
        :type description: str
        """
        self._description = description

    @property
    def display_name(self):
        r"""Gets the display_name of this InstancesVO.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :return: The display_name of this InstancesVO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this InstancesVO.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :param display_name: The display_name of this InstancesVO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def domain_name(self):
        r"""Gets the domain_name of this InstancesVO.

        租户名

        :return: The domain_name of this InstancesVO.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this InstancesVO.

        租户名

        :param domain_name: The domain_name of this InstancesVO.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def id(self):
        r"""Gets the id of this InstancesVO.

        id

        :return: The id of this InstancesVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstancesVO.

        id

        :param id: The id of this InstancesVO.
        :type id: str
        """
        self._id = id

    @property
    def is_temporary(self):
        r"""Gets the is_temporary of this InstancesVO.

        是否页面显示（以标签配置为准）

        :return: The is_temporary of this InstancesVO.
        :rtype: bool
        """
        return self._is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary):
        r"""Sets the is_temporary of this InstancesVO.

        是否页面显示（以标签配置为准）

        :param is_temporary: The is_temporary of this InstancesVO.
        :type is_temporary: bool
        """
        self._is_temporary = is_temporary

    @property
    def label(self):
        r"""Gets the label of this InstancesVO.

        标签

        :return: The label of this InstancesVO.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this InstancesVO.

        标签

        :param label: The label of this InstancesVO.
        :type label: str
        """
        self._label = label

    @property
    def link(self):
        r"""Gets the link of this InstancesVO.

        链接

        :return: The link of this InstancesVO.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this InstancesVO.

        链接

        :param link: The link of this InstancesVO.
        :type link: str
        """
        self._link = link

    @property
    def name(self):
        r"""Gets the name of this InstancesVO.

        名称

        :return: The name of this InstancesVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstancesVO.

        名称

        :param name: The name of this InstancesVO.
        :type name: str
        """
        self._name = name

    @property
    def organization_id(self):
        r"""Gets the organization_id of this InstancesVO.

        租户id（对应华为云帐号的domainId）

        :return: The organization_id of this InstancesVO.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this InstancesVO.

        租户id（对应华为云帐号的domainId）

        :param organization_id: The organization_id of this InstancesVO.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def owner_id(self):
        r"""Gets the owner_id of this InstancesVO.

        用户id

        :return: The owner_id of this InstancesVO.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this InstancesVO.

        用户id

        :param owner_id: The owner_id of this InstancesVO.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def owner_name(self):
        r"""Gets the owner_name of this InstancesVO.

        用户名

        :return: The owner_name of this InstancesVO.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this InstancesVO.

        用户名

        :param owner_name: The owner_name of this InstancesVO.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def platform_id(self):
        r"""Gets the platform_id of this InstancesVO.

        平台ID

        :return: The platform_id of this InstancesVO.
        :rtype: int
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        r"""Sets the platform_id of this InstancesVO.

        平台ID

        :param platform_id: The platform_id of this InstancesVO.
        :type platform_id: int
        """
        self._platform_id = platform_id

    @property
    def private(self):
        r"""Gets the private of this InstancesVO.

        是否私有平台

        :return: The private of this InstancesVO.
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        r"""Sets the private of this InstancesVO.

        是否私有平台

        :param private: The private of this InstancesVO.
        :type private: bool
        """
        self._private = private

    @property
    def pvc_quantity(self):
        r"""Gets the pvc_quantity of this InstancesVO.

        PVC规格 5GB|10GB|20GB

        :return: The pvc_quantity of this InstancesVO.
        :rtype: str
        """
        return self._pvc_quantity

    @pvc_quantity.setter
    def pvc_quantity(self, pvc_quantity):
        r"""Sets the pvc_quantity of this InstancesVO.

        PVC规格 5GB|10GB|20GB

        :param pvc_quantity: The pvc_quantity of this InstancesVO.
        :type pvc_quantity: str
        """
        self._pvc_quantity = pvc_quantity

    @property
    def refresh_interval(self):
        r"""Gets the refresh_interval of this InstancesVO.

        自动休眠时长。 arm架构,自动休眠时长只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例无操作超过自动休眠时长后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止

        :return: The refresh_interval of this InstancesVO.
        :rtype: int
        """
        return self._refresh_interval

    @refresh_interval.setter
    def refresh_interval(self, refresh_interval):
        r"""Sets the refresh_interval of this InstancesVO.

        自动休眠时长。 arm架构,自动休眠时长只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例无操作超过自动休眠时长后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止

        :param refresh_interval: The refresh_interval of this InstancesVO.
        :type refresh_interval: int
        """
        self._refresh_interval = refresh_interval

    @property
    def region(self):
        r"""Gets the region of this InstancesVO.

        区域

        :return: The region of this InstancesVO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this InstancesVO.

        区域

        :param region: The region of this InstancesVO.
        :type region: str
        """
        self._region = region

    @property
    def server_map(self):
        r"""Gets the server_map of this InstancesVO.

        server

        :return: The server_map of this InstancesVO.
        :rtype: dict(str, str)
        """
        return self._server_map

    @server_map.setter
    def server_map(self, server_map):
        r"""Sets the server_map of this InstancesVO.

        server

        :param server_map: The server_map of this InstancesVO.
        :type server_map: dict(str, str)
        """
        self._server_map = server_map

    @property
    def server_url(self):
        r"""Gets the server_url of this InstancesVO.

        服务链接

        :return: The server_url of this InstancesVO.
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        r"""Sets the server_url of this InstancesVO.

        服务链接

        :param server_url: The server_url of this InstancesVO.
        :type server_url: str
        """
        self._server_url = server_url

    @property
    def stack_id(self):
        r"""Gets the stack_id of this InstancesVO.

        技术栈ID，通过技术栈管理ListStacks接口获取。

        :return: The stack_id of this InstancesVO.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        r"""Sets the stack_id of this InstancesVO.

        技术栈ID，通过技术栈管理ListStacks接口获取。

        :param stack_id: The stack_id of this InstancesVO.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def status(self):
        r"""Gets the status of this InstancesVO.

        实例状态 。 - INIT 初始化 - STARTING 启动中 - RUNNING 运行中 - STOPPING 停止中 - STOPPED 已停止 - DELETING 删除中 - DELETED 已删除 - DELETE_FAILED 删除失败

        :return: The status of this InstancesVO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstancesVO.

        实例状态 。 - INIT 初始化 - STARTING 启动中 - RUNNING 运行中 - STOPPING 停止中 - STOPPED 已停止 - DELETING 删除中 - DELETED 已删除 - DELETE_FAILED 删除失败

        :param status: The status of this InstancesVO.
        :type status: str
        """
        self._status = status

    @property
    def updated_time(self):
        r"""Gets the updated_time of this InstancesVO.

        更新时间

        :return: The updated_time of this InstancesVO.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this InstancesVO.

        更新时间

        :param updated_time: The updated_time of this InstancesVO.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def visitor_id(self):
        r"""Gets the visitor_id of this InstancesVO.

        访问者id

        :return: The visitor_id of this InstancesVO.
        :rtype: str
        """
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, visitor_id):
        r"""Sets the visitor_id of this InstancesVO.

        访问者id

        :param visitor_id: The visitor_id of this InstancesVO.
        :type visitor_id: str
        """
        self._visitor_id = visitor_id

    @property
    def visitor_name(self):
        r"""Gets the visitor_name of this InstancesVO.

        访问者名称

        :return: The visitor_name of this InstancesVO.
        :rtype: str
        """
        return self._visitor_name

    @visitor_name.setter
    def visitor_name(self, visitor_name):
        r"""Sets the visitor_name of this InstancesVO.

        访问者名称

        :param visitor_name: The visitor_name of this InstancesVO.
        :type visitor_name: str
        """
        self._visitor_name = visitor_name

    @property
    def visitor_domain_name(self):
        r"""Gets the visitor_domain_name of this InstancesVO.

        访问者租户名称

        :return: The visitor_domain_name of this InstancesVO.
        :rtype: str
        """
        return self._visitor_domain_name

    @visitor_domain_name.setter
    def visitor_domain_name(self, visitor_domain_name):
        r"""Sets the visitor_domain_name of this InstancesVO.

        访问者租户名称

        :param visitor_domain_name: The visitor_domain_name of this InstancesVO.
        :type visitor_domain_name: str
        """
        self._visitor_domain_name = visitor_domain_name

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
        if not isinstance(other, InstancesVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
