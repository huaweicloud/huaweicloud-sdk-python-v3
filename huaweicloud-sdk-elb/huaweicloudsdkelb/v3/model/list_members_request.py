# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'name': 'list[str]',
        'weight': 'list[int]',
        'admin_state_up': 'bool',
        'subnet_cidr_id': 'list[str]',
        'address': 'list[str]',
        'protocol_port': 'list[int]',
        'id': 'list[str]',
        'operating_status': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'ip_version': 'list[str]',
        'member_type': 'list[str]',
        'instance_id': 'list[str]'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'name': 'name',
        'weight': 'weight',
        'admin_state_up': 'admin_state_up',
        'subnet_cidr_id': 'subnet_cidr_id',
        'address': 'address',
        'protocol_port': 'protocol_port',
        'id': 'id',
        'operating_status': 'operating_status',
        'enterprise_project_id': 'enterprise_project_id',
        'ip_version': 'ip_version',
        'member_type': 'member_type',
        'instance_id': 'instance_id'
    }

    def __init__(self, pool_id=None, marker=None, limit=None, page_reverse=None, name=None, weight=None, admin_state_up=None, subnet_cidr_id=None, address=None, protocol_port=None, id=None, operating_status=None, enterprise_project_id=None, ip_version=None, member_type=None, instance_id=None):
        """ListMembersRequest

        The model defined in huaweicloud sdk

        :param pool_id: 后端服务器组ID。
        :type pool_id: str
        :param marker: 上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。
        :type marker: str
        :param limit: 每页返回的个数。
        :type limit: int
        :param page_reverse: 是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。
        :type page_reverse: bool
        :param name: 后端云服务器名称。  支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。
        :type name: list[str]
        :param weight: 后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100。  支持多值查询，查询条件格式：*weight&#x3D;xxx&amp;weight&#x3D;xxx*。
        :type weight: list[int]
        :param admin_state_up: 后端云服务器的管理状态。  取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。
        :type admin_state_up: bool
        :param subnet_cidr_id: 后端云服务器所在子网的IPv4子网ID或IPv6子网ID。  支持多值查询，查询条件格式：***subnet_cidr_id&#x3D;xxx&amp;subnet_cidr_id&#x3D;xxx*。  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)
        :type subnet_cidr_id: list[str]
        :param address: 后端服务器对应的IPv4或IPv6地址。  支持多值查询，查询条件格式：*address&#x3D;xxx&amp;address&#x3D;xxx*。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)
        :type address: list[str]
        :param protocol_port: 后端服务器业务端口号。  支持多值查询，查询条件格式：*protocol_port&#x3D;xxx&amp;protocol_port&#x3D;xxx*。
        :type protocol_port: list[int]
        :param id: 后端云服务器ID。  支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。
        :type id: list[str]
        :param operating_status: 后端云服务器的健康状态。  取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。  支持多值查询，查询条件格式：*operating_status&#x3D;xxx&amp;operating_status&#x3D;xxx*。
        :type operating_status: list[str]
        :param enterprise_project_id: 企业项目ID。不传时查询default企业项目\&quot;0\&quot;下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式：*enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)
        :type enterprise_project_id: list[str]
        :param ip_version: 当前后端服务器的IP地址版本。取值：v4、v6。
        :type ip_version: list[str]
        :param member_type: 后端云服务器的类型。  取值： - ip：跨VPC的member。 - instance：关联到ECS的member。  支持多值查询，查询条件格式：*member_type&#x3D;xxx&amp;member_type&#x3D;xxx*。
        :type member_type: list[str]
        :param instance_id: member关联的ECS实例ID，空表示跨VPC场景的member。  支持多值查询，查询条件格式：*instance_id&#x3D;xxx&amp;instance_id&#x3D;xxx*。
        :type instance_id: list[str]
        """
        
        

        self._pool_id = None
        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._name = None
        self._weight = None
        self._admin_state_up = None
        self._subnet_cidr_id = None
        self._address = None
        self._protocol_port = None
        self._id = None
        self._operating_status = None
        self._enterprise_project_id = None
        self._ip_version = None
        self._member_type = None
        self._instance_id = None
        self.discriminator = None

        self.pool_id = pool_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if name is not None:
            self.name = name
        if weight is not None:
            self.weight = weight
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        if address is not None:
            self.address = address
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if id is not None:
            self.id = id
        if operating_status is not None:
            self.operating_status = operating_status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ip_version is not None:
            self.ip_version = ip_version
        if member_type is not None:
            self.member_type = member_type
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def pool_id(self):
        """Gets the pool_id of this ListMembersRequest.

        后端服务器组ID。

        :return: The pool_id of this ListMembersRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this ListMembersRequest.

        后端服务器组ID。

        :param pool_id: The pool_id of this ListMembersRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def marker(self):
        """Gets the marker of this ListMembersRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListMembersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListMembersRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListMembersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListMembersRequest.

        每页返回的个数。

        :return: The limit of this ListMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMembersRequest.

        每页返回的个数。

        :param limit: The limit of this ListMembersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListMembersRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :return: The page_reverse of this ListMembersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListMembersRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :param page_reverse: The page_reverse of this ListMembersRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def name(self):
        """Gets the name of this ListMembersRequest.

        后端云服务器名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :return: The name of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListMembersRequest.

        后端云服务器名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :param name: The name of this ListMembersRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def weight(self):
        """Gets the weight of this ListMembersRequest.

        后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100。  支持多值查询，查询条件格式：*weight=xxx&weight=xxx*。

        :return: The weight of this ListMembersRequest.
        :rtype: list[int]
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ListMembersRequest.

        后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100。  支持多值查询，查询条件格式：*weight=xxx&weight=xxx*。

        :param weight: The weight of this ListMembersRequest.
        :type weight: list[int]
        """
        self._weight = weight

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListMembersRequest.

        后端云服务器的管理状态。  取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :return: The admin_state_up of this ListMembersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListMembersRequest.

        后端云服务器的管理状态。  取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :param admin_state_up: The admin_state_up of this ListMembersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def subnet_cidr_id(self):
        """Gets the subnet_cidr_id of this ListMembersRequest.

        后端云服务器所在子网的IPv4子网ID或IPv6子网ID。  支持多值查询，查询条件格式：***subnet_cidr_id=xxx&subnet_cidr_id=xxx*。  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)

        :return: The subnet_cidr_id of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        """Sets the subnet_cidr_id of this ListMembersRequest.

        后端云服务器所在子网的IPv4子网ID或IPv6子网ID。  支持多值查询，查询条件格式：***subnet_cidr_id=xxx&subnet_cidr_id=xxx*。  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)

        :param subnet_cidr_id: The subnet_cidr_id of this ListMembersRequest.
        :type subnet_cidr_id: list[str]
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def address(self):
        """Gets the address of this ListMembersRequest.

        后端服务器对应的IPv4或IPv6地址。  支持多值查询，查询条件格式：*address=xxx&address=xxx*。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)

        :return: The address of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ListMembersRequest.

        后端服务器对应的IPv4或IPv6地址。  支持多值查询，查询条件格式：*address=xxx&address=xxx*。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)

        :param address: The address of this ListMembersRequest.
        :type address: list[str]
        """
        self._address = address

    @property
    def protocol_port(self):
        """Gets the protocol_port of this ListMembersRequest.

        后端服务器业务端口号。  支持多值查询，查询条件格式：*protocol_port=xxx&protocol_port=xxx*。

        :return: The protocol_port of this ListMembersRequest.
        :rtype: list[int]
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this ListMembersRequest.

        后端服务器业务端口号。  支持多值查询，查询条件格式：*protocol_port=xxx&protocol_port=xxx*。

        :param protocol_port: The protocol_port of this ListMembersRequest.
        :type protocol_port: list[int]
        """
        self._protocol_port = protocol_port

    @property
    def id(self):
        """Gets the id of this ListMembersRequest.

        后端云服务器ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :return: The id of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListMembersRequest.

        后端云服务器ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :param id: The id of this ListMembersRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def operating_status(self):
        """Gets the operating_status of this ListMembersRequest.

        后端云服务器的健康状态。  取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。  支持多值查询，查询条件格式：*operating_status=xxx&operating_status=xxx*。

        :return: The operating_status of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this ListMembersRequest.

        后端云服务器的健康状态。  取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。  支持多值查询，查询条件格式：*operating_status=xxx&operating_status=xxx*。

        :param operating_status: The operating_status of this ListMembersRequest.
        :type operating_status: list[str]
        """
        self._operating_status = operating_status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListMembersRequest.

        企业项目ID。不传时查询default企业项目\"0\"下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :return: The enterprise_project_id of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListMembersRequest.

        企业项目ID。不传时查询default企业项目\"0\"下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListMembersRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_version(self):
        """Gets the ip_version of this ListMembersRequest.

        当前后端服务器的IP地址版本。取值：v4、v6。

        :return: The ip_version of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListMembersRequest.

        当前后端服务器的IP地址版本。取值：v4、v6。

        :param ip_version: The ip_version of this ListMembersRequest.
        :type ip_version: list[str]
        """
        self._ip_version = ip_version

    @property
    def member_type(self):
        """Gets the member_type of this ListMembersRequest.

        后端云服务器的类型。  取值： - ip：跨VPC的member。 - instance：关联到ECS的member。  支持多值查询，查询条件格式：*member_type=xxx&member_type=xxx*。

        :return: The member_type of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """Sets the member_type of this ListMembersRequest.

        后端云服务器的类型。  取值： - ip：跨VPC的member。 - instance：关联到ECS的member。  支持多值查询，查询条件格式：*member_type=xxx&member_type=xxx*。

        :param member_type: The member_type of this ListMembersRequest.
        :type member_type: list[str]
        """
        self._member_type = member_type

    @property
    def instance_id(self):
        """Gets the instance_id of this ListMembersRequest.

        member关联的ECS实例ID，空表示跨VPC场景的member。  支持多值查询，查询条件格式：*instance_id=xxx&instance_id=xxx*。

        :return: The instance_id of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListMembersRequest.

        member关联的ECS实例ID，空表示跨VPC场景的member。  支持多值查询，查询条件格式：*instance_id=xxx&instance_id=xxx*。

        :param instance_id: The instance_id of this ListMembersRequest.
        :type instance_id: list[str]
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
