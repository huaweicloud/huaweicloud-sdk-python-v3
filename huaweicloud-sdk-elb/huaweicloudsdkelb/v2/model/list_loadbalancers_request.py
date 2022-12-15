# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLoadbalancersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'str',
        'description': 'str',
        'name': 'str',
        'operating_status': 'str',
        'provisioning_status': 'str',
        'vip_address': 'str',
        'vip_port_id': 'str',
        'vip_subnet_id': 'str',
        'vpc_id': 'str',
        'enterprise_project_id': 'str',
        'admin_state_up': 'bool',
        'member_address': 'str',
        'member_device_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'description': 'description',
        'name': 'name',
        'operating_status': 'operating_status',
        'provisioning_status': 'provisioning_status',
        'vip_address': 'vip_address',
        'vip_port_id': 'vip_port_id',
        'vip_subnet_id': 'vip_subnet_id',
        'vpc_id': 'vpc_id',
        'enterprise_project_id': 'enterprise_project_id',
        'admin_state_up': 'admin_state_up',
        'member_address': 'member_address',
        'member_device_id': 'member_device_id'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, description=None, name=None, operating_status=None, provisioning_status=None, vip_address=None, vip_port_id=None, vip_subnet_id=None, vpc_id=None, enterprise_project_id=None, admin_state_up=None, member_address=None, member_device_id=None):
        """ListLoadbalancersRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询中每页的负载均衡器个数
        :type limit: int
        :param marker: 分页查询的起始的资源id，表示上一页最后一条查询记录的负载均衡器的id。不指定时表示查询第一页。
        :type marker: str
        :param page_reverse: 分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。
        :type page_reverse: bool
        :param id: 负载均衡器的ID。
        :type id: str
        :param description: 负载均衡器的描述信息。
        :type description: str
        :param name: 负载均衡器的名称。
        :type name: str
        :param operating_status: 负载均衡器的操作状态。取值范围：可以为ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。
        :type operating_status: str
        :param provisioning_status: 负载均衡器的配置状态。取值范围：可以为ACTIVE、PENDING_CREATE 或者ERROR。
        :type provisioning_status: str
        :param vip_address: 负载均衡器的内网IP。
        :type vip_address: str
        :param vip_port_id: 负载均衡器内网IP对应的端口ID。
        :type vip_port_id: str
        :param vip_subnet_id: 负载均衡器所在的子网IPv4网络ID。
        :type vip_subnet_id: str
        :param vpc_id: 负载均衡器所在的虚拟私有云ID。
        :type vpc_id: str
        :param enterprise_project_id: 企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\&quot;0\&quot;表示查询默认企业项目资源；或者指定的企业项目ID下的资源。
        :type enterprise_project_id: str
        :param admin_state_up: 负载均衡器的管理状态。负载均衡器停用时不再接收流量。取值范围：true：启用负载均衡器；false：停用负载均衡器。
        :type admin_state_up: bool
        :param member_address: 负载均衡器的后端服务器的IP地址
        :type member_address: str
        :param member_device_id: 负载均衡器的后端服务器对应的弹性云服务器ID
        :type member_device_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._description = None
        self._name = None
        self._operating_status = None
        self._provisioning_status = None
        self._vip_address = None
        self._vip_port_id = None
        self._vip_subnet_id = None
        self._vpc_id = None
        self._enterprise_project_id = None
        self._admin_state_up = None
        self._member_address = None
        self._member_device_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if operating_status is not None:
            self.operating_status = operating_status
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if vip_address is not None:
            self.vip_address = vip_address
        if vip_port_id is not None:
            self.vip_port_id = vip_port_id
        if vip_subnet_id is not None:
            self.vip_subnet_id = vip_subnet_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if member_address is not None:
            self.member_address = member_address
        if member_device_id is not None:
            self.member_device_id = member_device_id

    @property
    def limit(self):
        """Gets the limit of this ListLoadbalancersRequest.

        分页查询中每页的负载均衡器个数

        :return: The limit of this ListLoadbalancersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListLoadbalancersRequest.

        分页查询中每页的负载均衡器个数

        :param limit: The limit of this ListLoadbalancersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListLoadbalancersRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的负载均衡器的id。不指定时表示查询第一页。

        :return: The marker of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListLoadbalancersRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的负载均衡器的id。不指定时表示查询第一页。

        :param marker: The marker of this ListLoadbalancersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListLoadbalancersRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :return: The page_reverse of this ListLoadbalancersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListLoadbalancersRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :param page_reverse: The page_reverse of this ListLoadbalancersRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListLoadbalancersRequest.

        负载均衡器的ID。

        :return: The id of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListLoadbalancersRequest.

        负载均衡器的ID。

        :param id: The id of this ListLoadbalancersRequest.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this ListLoadbalancersRequest.

        负载均衡器的描述信息。

        :return: The description of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListLoadbalancersRequest.

        负载均衡器的描述信息。

        :param description: The description of this ListLoadbalancersRequest.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this ListLoadbalancersRequest.

        负载均衡器的名称。

        :return: The name of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListLoadbalancersRequest.

        负载均衡器的名称。

        :param name: The name of this ListLoadbalancersRequest.
        :type name: str
        """
        self._name = name

    @property
    def operating_status(self):
        """Gets the operating_status of this ListLoadbalancersRequest.

        负载均衡器的操作状态。取值范围：可以为ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。

        :return: The operating_status of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this ListLoadbalancersRequest.

        负载均衡器的操作状态。取值范围：可以为ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。

        :param operating_status: The operating_status of this ListLoadbalancersRequest.
        :type operating_status: str
        """
        self._operating_status = operating_status

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this ListLoadbalancersRequest.

        负载均衡器的配置状态。取值范围：可以为ACTIVE、PENDING_CREATE 或者ERROR。

        :return: The provisioning_status of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this ListLoadbalancersRequest.

        负载均衡器的配置状态。取值范围：可以为ACTIVE、PENDING_CREATE 或者ERROR。

        :param provisioning_status: The provisioning_status of this ListLoadbalancersRequest.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def vip_address(self):
        """Gets the vip_address of this ListLoadbalancersRequest.

        负载均衡器的内网IP。

        :return: The vip_address of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this ListLoadbalancersRequest.

        负载均衡器的内网IP。

        :param vip_address: The vip_address of this ListLoadbalancersRequest.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def vip_port_id(self):
        """Gets the vip_port_id of this ListLoadbalancersRequest.

        负载均衡器内网IP对应的端口ID。

        :return: The vip_port_id of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        """Sets the vip_port_id of this ListLoadbalancersRequest.

        负载均衡器内网IP对应的端口ID。

        :param vip_port_id: The vip_port_id of this ListLoadbalancersRequest.
        :type vip_port_id: str
        """
        self._vip_port_id = vip_port_id

    @property
    def vip_subnet_id(self):
        """Gets the vip_subnet_id of this ListLoadbalancersRequest.

        负载均衡器所在的子网IPv4网络ID。

        :return: The vip_subnet_id of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._vip_subnet_id

    @vip_subnet_id.setter
    def vip_subnet_id(self, vip_subnet_id):
        """Sets the vip_subnet_id of this ListLoadbalancersRequest.

        负载均衡器所在的子网IPv4网络ID。

        :param vip_subnet_id: The vip_subnet_id of this ListLoadbalancersRequest.
        :type vip_subnet_id: str
        """
        self._vip_subnet_id = vip_subnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListLoadbalancersRequest.

        负载均衡器所在的虚拟私有云ID。

        :return: The vpc_id of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListLoadbalancersRequest.

        负载均衡器所在的虚拟私有云ID。

        :param vpc_id: The vpc_id of this ListLoadbalancersRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListLoadbalancersRequest.

        企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\"0\"表示查询默认企业项目资源；或者指定的企业项目ID下的资源。

        :return: The enterprise_project_id of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListLoadbalancersRequest.

        企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\"0\"表示查询默认企业项目资源；或者指定的企业项目ID下的资源。

        :param enterprise_project_id: The enterprise_project_id of this ListLoadbalancersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListLoadbalancersRequest.

        负载均衡器的管理状态。负载均衡器停用时不再接收流量。取值范围：true：启用负载均衡器；false：停用负载均衡器。

        :return: The admin_state_up of this ListLoadbalancersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListLoadbalancersRequest.

        负载均衡器的管理状态。负载均衡器停用时不再接收流量。取值范围：true：启用负载均衡器；false：停用负载均衡器。

        :param admin_state_up: The admin_state_up of this ListLoadbalancersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def member_address(self):
        """Gets the member_address of this ListLoadbalancersRequest.

        负载均衡器的后端服务器的IP地址

        :return: The member_address of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        """Sets the member_address of this ListLoadbalancersRequest.

        负载均衡器的后端服务器的IP地址

        :param member_address: The member_address of this ListLoadbalancersRequest.
        :type member_address: str
        """
        self._member_address = member_address

    @property
    def member_device_id(self):
        """Gets the member_device_id of this ListLoadbalancersRequest.

        负载均衡器的后端服务器对应的弹性云服务器ID

        :return: The member_device_id of this ListLoadbalancersRequest.
        :rtype: str
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        """Sets the member_device_id of this ListLoadbalancersRequest.

        负载均衡器的后端服务器对应的弹性云服务器ID

        :param member_device_id: The member_device_id of this ListLoadbalancersRequest.
        :type member_device_id: str
        """
        self._member_device_id = member_device_id

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
        if not isinstance(other, ListLoadbalancersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
