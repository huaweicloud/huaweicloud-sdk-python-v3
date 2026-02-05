# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerInstanceVO:

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
        'status': 'str',
        'name': 'str',
        'updated': 'str',
        'description': 'str',
        'available_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'node_count': 'int',
        'access_ip': 'str',
        'access_port': 'str',
        'core_count': 'str',
        'ram_capacity': 'str',
        'error_msg': 'str',
        'node_status': 'str',
        'maintenance_time': 'str',
        'enterprise_project_id': 'str',
        'project_id': 'str',
        'engine_version': 'str',
        'order_id': 'str',
        'admin_user_name': 'str',
        'enable_ssl': 'bool',
        'flavor_ref': 'str',
        'tags': 'list[Tags]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'updated': 'updated',
        'description': 'description',
        'available_zone': 'available_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'node_count': 'node_count',
        'access_ip': 'access_ip',
        'access_port': 'access_port',
        'core_count': 'core_count',
        'ram_capacity': 'ram_capacity',
        'error_msg': 'error_msg',
        'node_status': 'node_status',
        'maintenance_time': 'maintenance_time',
        'enterprise_project_id': 'enterprise_project_id',
        'project_id': 'project_id',
        'engine_version': 'engine_version',
        'order_id': 'order_id',
        'admin_user_name': 'admin_user_name',
        'enable_ssl': 'enable_ssl',
        'flavor_ref': 'flavor_ref',
        'tags': 'tags'
    }

    def __init__(self, id=None, status=None, name=None, updated=None, description=None, available_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, node_count=None, access_ip=None, access_port=None, core_count=None, ram_capacity=None, error_msg=None, node_status=None, maintenance_time=None, enterprise_project_id=None, project_id=None, engine_version=None, order_id=None, admin_user_name=None, enable_ssl=None, flavor_ref=None, tags=None):
        r"""CustomerInstanceVO

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  实例ID。  **参数范围**：  不涉及。
        :type id: str
        :param status: **参数解释**：  实例状态。  **参数范围**：  不涉及。
        :type status: str
        :param name: **参数解释**：  实例名称。  **参数范围**：  不涉及。
        :type name: str
        :param updated: **参数解释**：  更新时间。  **参数范围**：  不涉及。
        :type updated: str
        :param description: **参数解释**：  描述。  **参数范围**：  不涉及。
        :type description: str
        :param available_zone: **参数解释**：  可用区。  **参数范围**：  不涉及。
        :type available_zone: str
        :param vpc_id: **参数解释**：  虚拟私有云ID。  **参数范围**：  不涉及。
        :type vpc_id: str
        :param subnet_id: **参数解释**：  子网ID。  **参数范围**：  不涉及。
        :type subnet_id: str
        :param security_group_id: **参数解释**：  安全组ID。  **参数范围**：  不涉及。
        :type security_group_id: str
        :param node_count: **参数解释**：  节点数量。  **参数范围**：  不涉及。
        :type node_count: int
        :param access_ip: **参数解释**：  访问IP。  **参数范围**：  不涉及。
        :type access_ip: str
        :param access_port: **参数解释**：  访问端口。  **参数范围**：  不涉及。
        :type access_port: str
        :param core_count: **参数解释**：  核数。  **参数范围**：  不涉及。
        :type core_count: str
        :param ram_capacity: **参数解释**：  内存大小。  **参数范围**：  不涉及。
        :type ram_capacity: str
        :param error_msg: **参数解释**：  错误信息。  **参数范围**：  不涉及。
        :type error_msg: str
        :param node_status: **参数解释**：  节点状态。  **参数范围**：  不涉及。
        :type node_status: str
        :param maintenance_time: **参数解释**：  维护时间。  **参数范围**：  不涉及。
        :type maintenance_time: str
        :param enterprise_project_id: **参数解释**：  企业项目ID。  **参数范围**：  不涉及。
        :type enterprise_project_id: str
        :param project_id: **参数解释**：  项目ID。  **参数范围**：  不涉及。
        :type project_id: str
        :param engine_version: **参数解释**：  引擎版本。  **参数范围**：  不涉及。
        :type engine_version: str
        :param order_id: **参数解释**：  订单ID。  **参数范围**：  不涉及。
        :type order_id: str
        :param admin_user_name: **参数解释**：  管理员账号。  **参数范围**：  不涉及。
        :type admin_user_name: str
        :param enable_ssl: **参数解释**：  是否支持ssl。  **参数范围**：  不涉及。
        :type enable_ssl: bool
        :param flavor_ref: **参数解释**：  规格码。  **参数范围**：  不涉及。
        :type flavor_ref: str
        :param tags: **参数解释**：  标签的集合。  **参数范围**：  不涉及。
        :type tags: list[:class:`huaweicloudsdkddm.v1.Tags`]
        """
        
        

        self._id = None
        self._status = None
        self._name = None
        self._updated = None
        self._description = None
        self._available_zone = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._node_count = None
        self._access_ip = None
        self._access_port = None
        self._core_count = None
        self._ram_capacity = None
        self._error_msg = None
        self._node_status = None
        self._maintenance_time = None
        self._enterprise_project_id = None
        self._project_id = None
        self._engine_version = None
        self._order_id = None
        self._admin_user_name = None
        self._enable_ssl = None
        self._flavor_ref = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if updated is not None:
            self.updated = updated
        if description is not None:
            self.description = description
        if available_zone is not None:
            self.available_zone = available_zone
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if node_count is not None:
            self.node_count = node_count
        if access_ip is not None:
            self.access_ip = access_ip
        if access_port is not None:
            self.access_port = access_port
        if core_count is not None:
            self.core_count = core_count
        if ram_capacity is not None:
            self.ram_capacity = ram_capacity
        if error_msg is not None:
            self.error_msg = error_msg
        if node_status is not None:
            self.node_status = node_status
        if maintenance_time is not None:
            self.maintenance_time = maintenance_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if project_id is not None:
            self.project_id = project_id
        if engine_version is not None:
            self.engine_version = engine_version
        if order_id is not None:
            self.order_id = order_id
        if admin_user_name is not None:
            self.admin_user_name = admin_user_name
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this CustomerInstanceVO.

        **参数解释**：  实例ID。  **参数范围**：  不涉及。

        :return: The id of this CustomerInstanceVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CustomerInstanceVO.

        **参数解释**：  实例ID。  **参数范围**：  不涉及。

        :param id: The id of this CustomerInstanceVO.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this CustomerInstanceVO.

        **参数解释**：  实例状态。  **参数范围**：  不涉及。

        :return: The status of this CustomerInstanceVO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CustomerInstanceVO.

        **参数解释**：  实例状态。  **参数范围**：  不涉及。

        :param status: The status of this CustomerInstanceVO.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this CustomerInstanceVO.

        **参数解释**：  实例名称。  **参数范围**：  不涉及。

        :return: The name of this CustomerInstanceVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CustomerInstanceVO.

        **参数解释**：  实例名称。  **参数范围**：  不涉及。

        :param name: The name of this CustomerInstanceVO.
        :type name: str
        """
        self._name = name

    @property
    def updated(self):
        r"""Gets the updated of this CustomerInstanceVO.

        **参数解释**：  更新时间。  **参数范围**：  不涉及。

        :return: The updated of this CustomerInstanceVO.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this CustomerInstanceVO.

        **参数解释**：  更新时间。  **参数范围**：  不涉及。

        :param updated: The updated of this CustomerInstanceVO.
        :type updated: str
        """
        self._updated = updated

    @property
    def description(self):
        r"""Gets the description of this CustomerInstanceVO.

        **参数解释**：  描述。  **参数范围**：  不涉及。

        :return: The description of this CustomerInstanceVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CustomerInstanceVO.

        **参数解释**：  描述。  **参数范围**：  不涉及。

        :param description: The description of this CustomerInstanceVO.
        :type description: str
        """
        self._description = description

    @property
    def available_zone(self):
        r"""Gets the available_zone of this CustomerInstanceVO.

        **参数解释**：  可用区。  **参数范围**：  不涉及。

        :return: The available_zone of this CustomerInstanceVO.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        r"""Sets the available_zone of this CustomerInstanceVO.

        **参数解释**：  可用区。  **参数范围**：  不涉及。

        :param available_zone: The available_zone of this CustomerInstanceVO.
        :type available_zone: str
        """
        self._available_zone = available_zone

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CustomerInstanceVO.

        **参数解释**：  虚拟私有云ID。  **参数范围**：  不涉及。

        :return: The vpc_id of this CustomerInstanceVO.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CustomerInstanceVO.

        **参数解释**：  虚拟私有云ID。  **参数范围**：  不涉及。

        :param vpc_id: The vpc_id of this CustomerInstanceVO.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CustomerInstanceVO.

        **参数解释**：  子网ID。  **参数范围**：  不涉及。

        :return: The subnet_id of this CustomerInstanceVO.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CustomerInstanceVO.

        **参数解释**：  子网ID。  **参数范围**：  不涉及。

        :param subnet_id: The subnet_id of this CustomerInstanceVO.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this CustomerInstanceVO.

        **参数解释**：  安全组ID。  **参数范围**：  不涉及。

        :return: The security_group_id of this CustomerInstanceVO.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this CustomerInstanceVO.

        **参数解释**：  安全组ID。  **参数范围**：  不涉及。

        :param security_group_id: The security_group_id of this CustomerInstanceVO.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def node_count(self):
        r"""Gets the node_count of this CustomerInstanceVO.

        **参数解释**：  节点数量。  **参数范围**：  不涉及。

        :return: The node_count of this CustomerInstanceVO.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        r"""Sets the node_count of this CustomerInstanceVO.

        **参数解释**：  节点数量。  **参数范围**：  不涉及。

        :param node_count: The node_count of this CustomerInstanceVO.
        :type node_count: int
        """
        self._node_count = node_count

    @property
    def access_ip(self):
        r"""Gets the access_ip of this CustomerInstanceVO.

        **参数解释**：  访问IP。  **参数范围**：  不涉及。

        :return: The access_ip of this CustomerInstanceVO.
        :rtype: str
        """
        return self._access_ip

    @access_ip.setter
    def access_ip(self, access_ip):
        r"""Sets the access_ip of this CustomerInstanceVO.

        **参数解释**：  访问IP。  **参数范围**：  不涉及。

        :param access_ip: The access_ip of this CustomerInstanceVO.
        :type access_ip: str
        """
        self._access_ip = access_ip

    @property
    def access_port(self):
        r"""Gets the access_port of this CustomerInstanceVO.

        **参数解释**：  访问端口。  **参数范围**：  不涉及。

        :return: The access_port of this CustomerInstanceVO.
        :rtype: str
        """
        return self._access_port

    @access_port.setter
    def access_port(self, access_port):
        r"""Sets the access_port of this CustomerInstanceVO.

        **参数解释**：  访问端口。  **参数范围**：  不涉及。

        :param access_port: The access_port of this CustomerInstanceVO.
        :type access_port: str
        """
        self._access_port = access_port

    @property
    def core_count(self):
        r"""Gets the core_count of this CustomerInstanceVO.

        **参数解释**：  核数。  **参数范围**：  不涉及。

        :return: The core_count of this CustomerInstanceVO.
        :rtype: str
        """
        return self._core_count

    @core_count.setter
    def core_count(self, core_count):
        r"""Sets the core_count of this CustomerInstanceVO.

        **参数解释**：  核数。  **参数范围**：  不涉及。

        :param core_count: The core_count of this CustomerInstanceVO.
        :type core_count: str
        """
        self._core_count = core_count

    @property
    def ram_capacity(self):
        r"""Gets the ram_capacity of this CustomerInstanceVO.

        **参数解释**：  内存大小。  **参数范围**：  不涉及。

        :return: The ram_capacity of this CustomerInstanceVO.
        :rtype: str
        """
        return self._ram_capacity

    @ram_capacity.setter
    def ram_capacity(self, ram_capacity):
        r"""Sets the ram_capacity of this CustomerInstanceVO.

        **参数解释**：  内存大小。  **参数范围**：  不涉及。

        :param ram_capacity: The ram_capacity of this CustomerInstanceVO.
        :type ram_capacity: str
        """
        self._ram_capacity = ram_capacity

    @property
    def error_msg(self):
        r"""Gets the error_msg of this CustomerInstanceVO.

        **参数解释**：  错误信息。  **参数范围**：  不涉及。

        :return: The error_msg of this CustomerInstanceVO.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this CustomerInstanceVO.

        **参数解释**：  错误信息。  **参数范围**：  不涉及。

        :param error_msg: The error_msg of this CustomerInstanceVO.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def node_status(self):
        r"""Gets the node_status of this CustomerInstanceVO.

        **参数解释**：  节点状态。  **参数范围**：  不涉及。

        :return: The node_status of this CustomerInstanceVO.
        :rtype: str
        """
        return self._node_status

    @node_status.setter
    def node_status(self, node_status):
        r"""Sets the node_status of this CustomerInstanceVO.

        **参数解释**：  节点状态。  **参数范围**：  不涉及。

        :param node_status: The node_status of this CustomerInstanceVO.
        :type node_status: str
        """
        self._node_status = node_status

    @property
    def maintenance_time(self):
        r"""Gets the maintenance_time of this CustomerInstanceVO.

        **参数解释**：  维护时间。  **参数范围**：  不涉及。

        :return: The maintenance_time of this CustomerInstanceVO.
        :rtype: str
        """
        return self._maintenance_time

    @maintenance_time.setter
    def maintenance_time(self, maintenance_time):
        r"""Sets the maintenance_time of this CustomerInstanceVO.

        **参数解释**：  维护时间。  **参数范围**：  不涉及。

        :param maintenance_time: The maintenance_time of this CustomerInstanceVO.
        :type maintenance_time: str
        """
        self._maintenance_time = maintenance_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CustomerInstanceVO.

        **参数解释**：  企业项目ID。  **参数范围**：  不涉及。

        :return: The enterprise_project_id of this CustomerInstanceVO.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CustomerInstanceVO.

        **参数解释**：  企业项目ID。  **参数范围**：  不涉及。

        :param enterprise_project_id: The enterprise_project_id of this CustomerInstanceVO.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CustomerInstanceVO.

        **参数解释**：  项目ID。  **参数范围**：  不涉及。

        :return: The project_id of this CustomerInstanceVO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CustomerInstanceVO.

        **参数解释**：  项目ID。  **参数范围**：  不涉及。

        :param project_id: The project_id of this CustomerInstanceVO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def engine_version(self):
        r"""Gets the engine_version of this CustomerInstanceVO.

        **参数解释**：  引擎版本。  **参数范围**：  不涉及。

        :return: The engine_version of this CustomerInstanceVO.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this CustomerInstanceVO.

        **参数解释**：  引擎版本。  **参数范围**：  不涉及。

        :param engine_version: The engine_version of this CustomerInstanceVO.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def order_id(self):
        r"""Gets the order_id of this CustomerInstanceVO.

        **参数解释**：  订单ID。  **参数范围**：  不涉及。

        :return: The order_id of this CustomerInstanceVO.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CustomerInstanceVO.

        **参数解释**：  订单ID。  **参数范围**：  不涉及。

        :param order_id: The order_id of this CustomerInstanceVO.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def admin_user_name(self):
        r"""Gets the admin_user_name of this CustomerInstanceVO.

        **参数解释**：  管理员账号。  **参数范围**：  不涉及。

        :return: The admin_user_name of this CustomerInstanceVO.
        :rtype: str
        """
        return self._admin_user_name

    @admin_user_name.setter
    def admin_user_name(self, admin_user_name):
        r"""Sets the admin_user_name of this CustomerInstanceVO.

        **参数解释**：  管理员账号。  **参数范围**：  不涉及。

        :param admin_user_name: The admin_user_name of this CustomerInstanceVO.
        :type admin_user_name: str
        """
        self._admin_user_name = admin_user_name

    @property
    def enable_ssl(self):
        r"""Gets the enable_ssl of this CustomerInstanceVO.

        **参数解释**：  是否支持ssl。  **参数范围**：  不涉及。

        :return: The enable_ssl of this CustomerInstanceVO.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        r"""Sets the enable_ssl of this CustomerInstanceVO.

        **参数解释**：  是否支持ssl。  **参数范围**：  不涉及。

        :param enable_ssl: The enable_ssl of this CustomerInstanceVO.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this CustomerInstanceVO.

        **参数解释**：  规格码。  **参数范围**：  不涉及。

        :return: The flavor_ref of this CustomerInstanceVO.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this CustomerInstanceVO.

        **参数解释**：  规格码。  **参数范围**：  不涉及。

        :param flavor_ref: The flavor_ref of this CustomerInstanceVO.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def tags(self):
        r"""Gets the tags of this CustomerInstanceVO.

        **参数解释**：  标签的集合。  **参数范围**：  不涉及。

        :return: The tags of this CustomerInstanceVO.
        :rtype: list[:class:`huaweicloudsdkddm.v1.Tags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CustomerInstanceVO.

        **参数解释**：  标签的集合。  **参数范围**：  不涉及。

        :param tags: The tags of this CustomerInstanceVO.
        :type tags: list[:class:`huaweicloudsdkddm.v1.Tags`]
        """
        self._tags = tags

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomerInstanceVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
