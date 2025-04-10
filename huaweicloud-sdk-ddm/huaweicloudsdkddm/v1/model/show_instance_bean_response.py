# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceBeanResponse:

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
        'core_count': 'str',
        'ram_capacity': 'str',
        'error_msg': 'str',
        'node_status': 'str',
        'enterprise_project_id': 'str',
        'project_id': 'str',
        'engine_version': 'str',
        'order_id': 'str',
        'enable_ssl': 'bool',
        'flavor_ref': 'str'
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
        'core_count': 'core_count',
        'ram_capacity': 'ram_capacity',
        'error_msg': 'error_msg',
        'node_status': 'node_status',
        'enterprise_project_id': 'enterprise_project_id',
        'project_id': 'project_id',
        'engine_version': 'engine_version',
        'order_id': 'order_id',
        'enable_ssl': 'enable_ssl',
        'flavor_ref': 'flavor_ref'
    }

    def __init__(self, id=None, status=None, name=None, created=None, updated=None, available_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, node_count=None, access_ip=None, access_port=None, core_count=None, ram_capacity=None, error_msg=None, node_status=None, enterprise_project_id=None, project_id=None, engine_version=None, order_id=None, enable_ssl=None, flavor_ref=None):
        r"""ShowInstanceBeanResponse

        The model defined in huaweicloud sdk

        :param id: DDM实例ID。
        :type id: str
        :param status: DDM实例状态。
        :type status: str
        :param name: 创建的实例名称。
        :type name: str
        :param created: 创建时间，格式为yyyy-mm-dd Thh:mm:ssZ。  其中，T指定某个时间的开始；Z指示 UTC 时间。
        :type created: str
        :param updated: 更新时间，格式与“created”完全相同。
        :type updated: str
        :param available_zone: 可用区名称
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
        :param core_count: cpu个数。
        :type core_count: str
        :param ram_capacity: 内存大小，单位为G。
        :type ram_capacity: str
        :param error_msg: 响应信息，若无异常信息则不返回该参数 
        :type error_msg: str
        :param node_status: 节点状态。
        :type node_status: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param project_id: 租户在某一region下的project ID。
        :type project_id: str
        :param engine_version: 引擎版本号（Core实例版本号）。
        :type engine_version: str
        :param order_id: 包周期的实例，有订单id。
        :type order_id: str
        :param enable_ssl: 是否开启SSL。
        :type enable_ssl: bool
        :param flavor_ref: 规格码。
        :type flavor_ref: str
        """
        
        

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
        self._core_count = None
        self._ram_capacity = None
        self._error_msg = None
        self._node_status = None
        self._enterprise_project_id = None
        self._project_id = None
        self._engine_version = None
        self._order_id = None
        self._enable_ssl = None
        self._flavor_ref = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.name = name
        self.created = created
        self.updated = updated
        self.available_zone = available_zone
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.node_count = node_count
        self.access_ip = access_ip
        self.access_port = access_port
        self.core_count = core_count
        self.ram_capacity = ram_capacity
        if error_msg is not None:
            self.error_msg = error_msg
        self.node_status = node_status
        self.enterprise_project_id = enterprise_project_id
        self.project_id = project_id
        self.engine_version = engine_version
        if order_id is not None:
            self.order_id = order_id
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref

    @property
    def id(self):
        r"""Gets the id of this ShowInstanceBeanResponse.

        DDM实例ID。

        :return: The id of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowInstanceBeanResponse.

        DDM实例ID。

        :param id: The id of this ShowInstanceBeanResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ShowInstanceBeanResponse.

        DDM实例状态。

        :return: The status of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInstanceBeanResponse.

        DDM实例状态。

        :param status: The status of this ShowInstanceBeanResponse.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ShowInstanceBeanResponse.

        创建的实例名称。

        :return: The name of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowInstanceBeanResponse.

        创建的实例名称。

        :param name: The name of this ShowInstanceBeanResponse.
        :type name: str
        """
        self._name = name

    @property
    def created(self):
        r"""Gets the created of this ShowInstanceBeanResponse.

        创建时间，格式为yyyy-mm-dd Thh:mm:ssZ。  其中，T指定某个时间的开始；Z指示 UTC 时间。

        :return: The created of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ShowInstanceBeanResponse.

        创建时间，格式为yyyy-mm-dd Thh:mm:ssZ。  其中，T指定某个时间的开始；Z指示 UTC 时间。

        :param created: The created of this ShowInstanceBeanResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ShowInstanceBeanResponse.

        更新时间，格式与“created”完全相同。

        :return: The updated of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ShowInstanceBeanResponse.

        更新时间，格式与“created”完全相同。

        :param updated: The updated of this ShowInstanceBeanResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def available_zone(self):
        r"""Gets the available_zone of this ShowInstanceBeanResponse.

        可用区名称

        :return: The available_zone of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        r"""Sets the available_zone of this ShowInstanceBeanResponse.

        可用区名称

        :param available_zone: The available_zone of this ShowInstanceBeanResponse.
        :type available_zone: str
        """
        self._available_zone = available_zone

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ShowInstanceBeanResponse.

        虚拟私有云的ID。

        :return: The vpc_id of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ShowInstanceBeanResponse.

        虚拟私有云的ID。

        :param vpc_id: The vpc_id of this ShowInstanceBeanResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ShowInstanceBeanResponse.

        子网ID。

        :return: The subnet_id of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ShowInstanceBeanResponse.

        子网ID。

        :param subnet_id: The subnet_id of this ShowInstanceBeanResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ShowInstanceBeanResponse.

        安全组ID。

        :return: The security_group_id of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ShowInstanceBeanResponse.

        安全组ID。

        :param security_group_id: The security_group_id of this ShowInstanceBeanResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def node_count(self):
        r"""Gets the node_count of this ShowInstanceBeanResponse.

        节点数量。

        :return: The node_count of this ShowInstanceBeanResponse.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        r"""Sets the node_count of this ShowInstanceBeanResponse.

        节点数量。

        :param node_count: The node_count of this ShowInstanceBeanResponse.
        :type node_count: int
        """
        self._node_count = node_count

    @property
    def access_ip(self):
        r"""Gets the access_ip of this ShowInstanceBeanResponse.

        DDM实例访问地址。

        :return: The access_ip of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._access_ip

    @access_ip.setter
    def access_ip(self, access_ip):
        r"""Sets the access_ip of this ShowInstanceBeanResponse.

        DDM实例访问地址。

        :param access_ip: The access_ip of this ShowInstanceBeanResponse.
        :type access_ip: str
        """
        self._access_ip = access_ip

    @property
    def access_port(self):
        r"""Gets the access_port of this ShowInstanceBeanResponse.

        DDM实例访问端口。

        :return: The access_port of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._access_port

    @access_port.setter
    def access_port(self, access_port):
        r"""Sets the access_port of this ShowInstanceBeanResponse.

        DDM实例访问端口。

        :param access_port: The access_port of this ShowInstanceBeanResponse.
        :type access_port: str
        """
        self._access_port = access_port

    @property
    def core_count(self):
        r"""Gets the core_count of this ShowInstanceBeanResponse.

        cpu个数。

        :return: The core_count of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._core_count

    @core_count.setter
    def core_count(self, core_count):
        r"""Sets the core_count of this ShowInstanceBeanResponse.

        cpu个数。

        :param core_count: The core_count of this ShowInstanceBeanResponse.
        :type core_count: str
        """
        self._core_count = core_count

    @property
    def ram_capacity(self):
        r"""Gets the ram_capacity of this ShowInstanceBeanResponse.

        内存大小，单位为G。

        :return: The ram_capacity of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._ram_capacity

    @ram_capacity.setter
    def ram_capacity(self, ram_capacity):
        r"""Sets the ram_capacity of this ShowInstanceBeanResponse.

        内存大小，单位为G。

        :param ram_capacity: The ram_capacity of this ShowInstanceBeanResponse.
        :type ram_capacity: str
        """
        self._ram_capacity = ram_capacity

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ShowInstanceBeanResponse.

        响应信息，若无异常信息则不返回该参数 

        :return: The error_msg of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ShowInstanceBeanResponse.

        响应信息，若无异常信息则不返回该参数 

        :param error_msg: The error_msg of this ShowInstanceBeanResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def node_status(self):
        r"""Gets the node_status of this ShowInstanceBeanResponse.

        节点状态。

        :return: The node_status of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._node_status

    @node_status.setter
    def node_status(self, node_status):
        r"""Sets the node_status of this ShowInstanceBeanResponse.

        节点状态。

        :param node_status: The node_status of this ShowInstanceBeanResponse.
        :type node_status: str
        """
        self._node_status = node_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowInstanceBeanResponse.

        企业项目ID。

        :return: The enterprise_project_id of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowInstanceBeanResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ShowInstanceBeanResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowInstanceBeanResponse.

        租户在某一region下的project ID。

        :return: The project_id of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowInstanceBeanResponse.

        租户在某一region下的project ID。

        :param project_id: The project_id of this ShowInstanceBeanResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ShowInstanceBeanResponse.

        引擎版本号（Core实例版本号）。

        :return: The engine_version of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ShowInstanceBeanResponse.

        引擎版本号（Core实例版本号）。

        :param engine_version: The engine_version of this ShowInstanceBeanResponse.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def order_id(self):
        r"""Gets the order_id of this ShowInstanceBeanResponse.

        包周期的实例，有订单id。

        :return: The order_id of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ShowInstanceBeanResponse.

        包周期的实例，有订单id。

        :param order_id: The order_id of this ShowInstanceBeanResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def enable_ssl(self):
        r"""Gets the enable_ssl of this ShowInstanceBeanResponse.

        是否开启SSL。

        :return: The enable_ssl of this ShowInstanceBeanResponse.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        r"""Sets the enable_ssl of this ShowInstanceBeanResponse.

        是否开启SSL。

        :param enable_ssl: The enable_ssl of this ShowInstanceBeanResponse.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this ShowInstanceBeanResponse.

        规格码。

        :return: The flavor_ref of this ShowInstanceBeanResponse.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this ShowInstanceBeanResponse.

        规格码。

        :param flavor_ref: The flavor_ref of this ShowInstanceBeanResponse.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

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
        if not isinstance(other, ShowInstanceBeanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
