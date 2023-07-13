# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceResponse(SdkResponse):

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
        'created': 'str',
        'updated': 'str',
        'available_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'node_count': 'int',
        'access_ip': 'str',
        'access_port': 'str',
        'node_status': 'str',
        'core_count': 'str',
        'ram_capacity': 'str',
        'error_msg': 'str',
        'project_id': 'str',
        'order_id': 'str',
        'enterprise_project_id': 'str',
        'engine_version': 'str',
        'nodes': 'list[GetDetailfNodesInfo]',
        'admin_user_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'created': 'created',
        'updated': 'updated',
        'available_zone': 'available_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'node_count': 'node_count',
        'access_ip': 'access_ip',
        'access_port': 'access_port',
        'node_status': 'node_status',
        'core_count': 'core_count',
        'ram_capacity': 'ram_capacity',
        'error_msg': 'error_msg',
        'project_id': 'project_id',
        'order_id': 'order_id',
        'enterprise_project_id': 'enterprise_project_id',
        'engine_version': 'engine_version',
        'nodes': 'nodes',
        'admin_user_name': 'admin_user_name'
    }

    def __init__(self, id=None, status=None, name=None, created=None, updated=None, available_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, node_count=None, access_ip=None, access_port=None, node_status=None, core_count=None, ram_capacity=None, error_msg=None, project_id=None, order_id=None, enterprise_project_id=None, engine_version=None, nodes=None, admin_user_name=None):
        """ShowInstanceResponse

        The model defined in huaweicloud sdk

        :param id: DDM实例ID。
        :type id: str
        :param status: DDM实例状态。
        :type status: str
        :param name: DDM实例名称。
        :type name: str
        :param created: DDM实例创建时间。
        :type created: str
        :param updated: DDM实例最后更新时间。
        :type updated: str
        :param available_zone: DDM实例可用区名称。
        :type available_zone: str
        :param vpc_id: 虚拟私有云的ID。
        :type vpc_id: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param node_count: 节点数量。
        :type node_count: int
        :param access_ip: DDM实例访问地址。
        :type access_ip: str
        :param access_port: DDM实例访问端口。
        :type access_port: str
        :param node_status: 节点状态。
        :type node_status: str
        :param core_count: cpu个数。
        :type core_count: str
        :param ram_capacity: 内存大小，单位为G。
        :type ram_capacity: str
        :param error_msg: 响应信息，若无异常信息则不返回该参数。
        :type error_msg: str
        :param project_id: 项目ID。
        :type project_id: str
        :param order_id: 订单ID。包周期实例的订单ID，按需实例为空。
        :type order_id: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param engine_version: 引擎版本号（Core实例版本号）。
        :type engine_version: str
        :param nodes: 节点信息。
        :type nodes: list[:class:`huaweicloudsdkddm.v1.GetDetailfNodesInfo`]
        :param admin_user_name: 管理员账号用户名。 - 长度为1-32个字符。 - 必须以字母开头。 - 可以包含字母，数字、下划线，不能包含其它特殊字符。
        :type admin_user_name: str
        """
        
        super(ShowInstanceResponse, self).__init__()

        self._id = None
        self._status = None
        self._name = None
        self._created = None
        self._updated = None
        self._available_zone = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._node_count = None
        self._access_ip = None
        self._access_port = None
        self._node_status = None
        self._core_count = None
        self._ram_capacity = None
        self._error_msg = None
        self._project_id = None
        self._order_id = None
        self._enterprise_project_id = None
        self._engine_version = None
        self._nodes = None
        self._admin_user_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
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
        if node_status is not None:
            self.node_status = node_status
        if core_count is not None:
            self.core_count = core_count
        if ram_capacity is not None:
            self.ram_capacity = ram_capacity
        if error_msg is not None:
            self.error_msg = error_msg
        if project_id is not None:
            self.project_id = project_id
        if order_id is not None:
            self.order_id = order_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if engine_version is not None:
            self.engine_version = engine_version
        if nodes is not None:
            self.nodes = nodes
        if admin_user_name is not None:
            self.admin_user_name = admin_user_name

    @property
    def id(self):
        """Gets the id of this ShowInstanceResponse.

        DDM实例ID。

        :return: The id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowInstanceResponse.

        DDM实例ID。

        :param id: The id of this ShowInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ShowInstanceResponse.

        DDM实例状态。

        :return: The status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowInstanceResponse.

        DDM实例状态。

        :param status: The status of this ShowInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this ShowInstanceResponse.

        DDM实例名称。

        :return: The name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowInstanceResponse.

        DDM实例名称。

        :param name: The name of this ShowInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def created(self):
        """Gets the created of this ShowInstanceResponse.

        DDM实例创建时间。

        :return: The created of this ShowInstanceResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowInstanceResponse.

        DDM实例创建时间。

        :param created: The created of this ShowInstanceResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ShowInstanceResponse.

        DDM实例最后更新时间。

        :return: The updated of this ShowInstanceResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowInstanceResponse.

        DDM实例最后更新时间。

        :param updated: The updated of this ShowInstanceResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def available_zone(self):
        """Gets the available_zone of this ShowInstanceResponse.

        DDM实例可用区名称。

        :return: The available_zone of this ShowInstanceResponse.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        """Sets the available_zone of this ShowInstanceResponse.

        DDM实例可用区名称。

        :param available_zone: The available_zone of this ShowInstanceResponse.
        :type available_zone: str
        """
        self._available_zone = available_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ShowInstanceResponse.

        虚拟私有云的ID。

        :return: The vpc_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ShowInstanceResponse.

        虚拟私有云的ID。

        :param vpc_id: The vpc_id of this ShowInstanceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ShowInstanceResponse.

        子网ID。

        :return: The subnet_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ShowInstanceResponse.

        子网ID。

        :param subnet_id: The subnet_id of this ShowInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ShowInstanceResponse.

        安全组ID。

        :return: The security_group_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ShowInstanceResponse.

        安全组ID。

        :param security_group_id: The security_group_id of this ShowInstanceResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def node_count(self):
        """Gets the node_count of this ShowInstanceResponse.

        节点数量。

        :return: The node_count of this ShowInstanceResponse.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """Sets the node_count of this ShowInstanceResponse.

        节点数量。

        :param node_count: The node_count of this ShowInstanceResponse.
        :type node_count: int
        """
        self._node_count = node_count

    @property
    def access_ip(self):
        """Gets the access_ip of this ShowInstanceResponse.

        DDM实例访问地址。

        :return: The access_ip of this ShowInstanceResponse.
        :rtype: str
        """
        return self._access_ip

    @access_ip.setter
    def access_ip(self, access_ip):
        """Sets the access_ip of this ShowInstanceResponse.

        DDM实例访问地址。

        :param access_ip: The access_ip of this ShowInstanceResponse.
        :type access_ip: str
        """
        self._access_ip = access_ip

    @property
    def access_port(self):
        """Gets the access_port of this ShowInstanceResponse.

        DDM实例访问端口。

        :return: The access_port of this ShowInstanceResponse.
        :rtype: str
        """
        return self._access_port

    @access_port.setter
    def access_port(self, access_port):
        """Sets the access_port of this ShowInstanceResponse.

        DDM实例访问端口。

        :param access_port: The access_port of this ShowInstanceResponse.
        :type access_port: str
        """
        self._access_port = access_port

    @property
    def node_status(self):
        """Gets the node_status of this ShowInstanceResponse.

        节点状态。

        :return: The node_status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._node_status

    @node_status.setter
    def node_status(self, node_status):
        """Sets the node_status of this ShowInstanceResponse.

        节点状态。

        :param node_status: The node_status of this ShowInstanceResponse.
        :type node_status: str
        """
        self._node_status = node_status

    @property
    def core_count(self):
        """Gets the core_count of this ShowInstanceResponse.

        cpu个数。

        :return: The core_count of this ShowInstanceResponse.
        :rtype: str
        """
        return self._core_count

    @core_count.setter
    def core_count(self, core_count):
        """Sets the core_count of this ShowInstanceResponse.

        cpu个数。

        :param core_count: The core_count of this ShowInstanceResponse.
        :type core_count: str
        """
        self._core_count = core_count

    @property
    def ram_capacity(self):
        """Gets the ram_capacity of this ShowInstanceResponse.

        内存大小，单位为G。

        :return: The ram_capacity of this ShowInstanceResponse.
        :rtype: str
        """
        return self._ram_capacity

    @ram_capacity.setter
    def ram_capacity(self, ram_capacity):
        """Sets the ram_capacity of this ShowInstanceResponse.

        内存大小，单位为G。

        :param ram_capacity: The ram_capacity of this ShowInstanceResponse.
        :type ram_capacity: str
        """
        self._ram_capacity = ram_capacity

    @property
    def error_msg(self):
        """Gets the error_msg of this ShowInstanceResponse.

        响应信息，若无异常信息则不返回该参数。

        :return: The error_msg of this ShowInstanceResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ShowInstanceResponse.

        响应信息，若无异常信息则不返回该参数。

        :param error_msg: The error_msg of this ShowInstanceResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def project_id(self):
        """Gets the project_id of this ShowInstanceResponse.

        项目ID。

        :return: The project_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowInstanceResponse.

        项目ID。

        :param project_id: The project_id of this ShowInstanceResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def order_id(self):
        """Gets the order_id of this ShowInstanceResponse.

        订单ID。包周期实例的订单ID，按需实例为空。

        :return: The order_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ShowInstanceResponse.

        订单ID。包周期实例的订单ID，按需实例为空。

        :param order_id: The order_id of this ShowInstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowInstanceResponse.

        企业项目ID。

        :return: The enterprise_project_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowInstanceResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ShowInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def engine_version(self):
        """Gets the engine_version of this ShowInstanceResponse.

        引擎版本号（Core实例版本号）。

        :return: The engine_version of this ShowInstanceResponse.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this ShowInstanceResponse.

        引擎版本号（Core实例版本号）。

        :param engine_version: The engine_version of this ShowInstanceResponse.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def nodes(self):
        """Gets the nodes of this ShowInstanceResponse.

        节点信息。

        :return: The nodes of this ShowInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.GetDetailfNodesInfo`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ShowInstanceResponse.

        节点信息。

        :param nodes: The nodes of this ShowInstanceResponse.
        :type nodes: list[:class:`huaweicloudsdkddm.v1.GetDetailfNodesInfo`]
        """
        self._nodes = nodes

    @property
    def admin_user_name(self):
        """Gets the admin_user_name of this ShowInstanceResponse.

        管理员账号用户名。 - 长度为1-32个字符。 - 必须以字母开头。 - 可以包含字母，数字、下划线，不能包含其它特殊字符。

        :return: The admin_user_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._admin_user_name

    @admin_user_name.setter
    def admin_user_name(self, admin_user_name):
        """Sets the admin_user_name of this ShowInstanceResponse.

        管理员账号用户名。 - 长度为1-32个字符。 - 必须以字母开头。 - 可以包含字母，数字、下划线，不能包含其它特殊字符。

        :param admin_user_name: The admin_user_name of this ShowInstanceResponse.
        :type admin_user_name: str
        """
        self._admin_user_name = admin_user_name

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
        if not isinstance(other, ShowInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
