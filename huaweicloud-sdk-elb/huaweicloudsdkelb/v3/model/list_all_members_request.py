# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
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
        'pool_id': 'list[str]',
        'loadbalancer_id': 'list[str]'
    }

    attribute_map = {
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
        'pool_id': 'pool_id',
        'loadbalancer_id': 'loadbalancer_id'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, name=None, weight=None, admin_state_up=None, subnet_cidr_id=None, address=None, protocol_port=None, id=None, operating_status=None, enterprise_project_id=None, ip_version=None, pool_id=None, loadbalancer_id=None):
        """ListAllMembersRequest

        The model defined in huaweicloud sdk

        :param marker: 上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。
        :type marker: str
        :param limit: 每页返回的个数。
        :type limit: int
        :param page_reverse: 是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。
        :type page_reverse: bool
        :param name: 后端云服务器名称。  支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。
        :type name: list[str]
        :param weight: 后端云服务器的权重，请求按权重在同一后端云服务器组下的后端云服务器间分发。 权重为0的后端不再接受新的请求。 当后端云服务器所在的后端云服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。  支持多值查询，查询条件格式：*weight&#x3D;xxx&amp;weight&#x3D;xxx*。
        :type weight: list[int]
        :param admin_state_up: 后端云服务器的管理状态；该字段虽然支持创建、更新，但实际取值决定于member对应的弹性云服务器是否存在。 若存在，该值为true，否则，该值为false。
        :type admin_state_up: bool
        :param subnet_cidr_id: 后端云服务器所在的子网ID。该子网和后端云服务器关联的负载均衡器的子网必须在同一VPC下。只支持指定IPv4的子网ID。  支持多值查询，查询条件格式：***subnet_cidr_id&#x3D;xxx&amp;subnet_cidr_id&#x3D;xxx*。
        :type subnet_cidr_id: list[str]
        :param address: 后端云服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。 例如：192.168.3.11。只能指定为主网卡的IP。  支持多值查询，查询条件格式：*address&#x3D;xxx&amp;address&#x3D;xxx*。
        :type address: list[str]
        :param protocol_port: 后端服务器端口号。  支持多值查询，查询条件格式：*protocol_port&#x3D;xxx&amp;protocol_port&#x3D;xxx*。
        :type protocol_port: list[int]
        :param id: 后端云服务器ID。  支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。
        :type id: list[str]
        :param operating_status: 后端云服务器的健康状态。  取值： - ONLINE，后端服务器正常运行。 - NO_MONITOR，后端服务器无健康检查。 - OFFLINE，已下线。  支持多值查询，查询条件格式：*operating_status&#x3D;xxx&amp;operating_status&#x3D;*。
        :type operating_status: list[str]
        :param enterprise_project_id: 企业项目ID。不传时查询default企业项目\&quot;0\&quot;下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式： *enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)
        :type enterprise_project_id: list[str]
        :param ip_version: IP版本，取值v4、v6。  支持多值查询，查询条件格式：*ip_version&#x3D;xxx&amp;ip_version&#x3D;xxx*。
        :type ip_version: list[str]
        :param pool_id: member所属的服务器组ID  支持多值查询，查询条件格式：*pool_id&#x3D;xxx&amp;pool_id&#x3D;xxx*。
        :type pool_id: list[str]
        :param loadbalancer_id: member所属的负载均衡器ID。  支持多值查询，查询条件格式：*loadbalancer_id&#x3D;xxx&amp;loadbalancer_id&#x3D;xxx*。
        :type loadbalancer_id: list[str]
        """
        
        

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
        self._pool_id = None
        self._loadbalancer_id = None
        self.discriminator = None

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
        if pool_id is not None:
            self.pool_id = pool_id
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id

    @property
    def marker(self):
        """Gets the marker of this ListAllMembersRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListAllMembersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAllMembersRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListAllMembersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListAllMembersRequest.

        每页返回的个数。

        :return: The limit of this ListAllMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAllMembersRequest.

        每页返回的个数。

        :param limit: The limit of this ListAllMembersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListAllMembersRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :return: The page_reverse of this ListAllMembersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListAllMembersRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :param page_reverse: The page_reverse of this ListAllMembersRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def name(self):
        """Gets the name of this ListAllMembersRequest.

        后端云服务器名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :return: The name of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAllMembersRequest.

        后端云服务器名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :param name: The name of this ListAllMembersRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def weight(self):
        """Gets the weight of this ListAllMembersRequest.

        后端云服务器的权重，请求按权重在同一后端云服务器组下的后端云服务器间分发。 权重为0的后端不再接受新的请求。 当后端云服务器所在的后端云服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。  支持多值查询，查询条件格式：*weight=xxx&weight=xxx*。

        :return: The weight of this ListAllMembersRequest.
        :rtype: list[int]
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ListAllMembersRequest.

        后端云服务器的权重，请求按权重在同一后端云服务器组下的后端云服务器间分发。 权重为0的后端不再接受新的请求。 当后端云服务器所在的后端云服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。  支持多值查询，查询条件格式：*weight=xxx&weight=xxx*。

        :param weight: The weight of this ListAllMembersRequest.
        :type weight: list[int]
        """
        self._weight = weight

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListAllMembersRequest.

        后端云服务器的管理状态；该字段虽然支持创建、更新，但实际取值决定于member对应的弹性云服务器是否存在。 若存在，该值为true，否则，该值为false。

        :return: The admin_state_up of this ListAllMembersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListAllMembersRequest.

        后端云服务器的管理状态；该字段虽然支持创建、更新，但实际取值决定于member对应的弹性云服务器是否存在。 若存在，该值为true，否则，该值为false。

        :param admin_state_up: The admin_state_up of this ListAllMembersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def subnet_cidr_id(self):
        """Gets the subnet_cidr_id of this ListAllMembersRequest.

        后端云服务器所在的子网ID。该子网和后端云服务器关联的负载均衡器的子网必须在同一VPC下。只支持指定IPv4的子网ID。  支持多值查询，查询条件格式：***subnet_cidr_id=xxx&subnet_cidr_id=xxx*。

        :return: The subnet_cidr_id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        """Sets the subnet_cidr_id of this ListAllMembersRequest.

        后端云服务器所在的子网ID。该子网和后端云服务器关联的负载均衡器的子网必须在同一VPC下。只支持指定IPv4的子网ID。  支持多值查询，查询条件格式：***subnet_cidr_id=xxx&subnet_cidr_id=xxx*。

        :param subnet_cidr_id: The subnet_cidr_id of this ListAllMembersRequest.
        :type subnet_cidr_id: list[str]
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def address(self):
        """Gets the address of this ListAllMembersRequest.

        后端云服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。 例如：192.168.3.11。只能指定为主网卡的IP。  支持多值查询，查询条件格式：*address=xxx&address=xxx*。

        :return: The address of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ListAllMembersRequest.

        后端云服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。 例如：192.168.3.11。只能指定为主网卡的IP。  支持多值查询，查询条件格式：*address=xxx&address=xxx*。

        :param address: The address of this ListAllMembersRequest.
        :type address: list[str]
        """
        self._address = address

    @property
    def protocol_port(self):
        """Gets the protocol_port of this ListAllMembersRequest.

        后端服务器端口号。  支持多值查询，查询条件格式：*protocol_port=xxx&protocol_port=xxx*。

        :return: The protocol_port of this ListAllMembersRequest.
        :rtype: list[int]
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this ListAllMembersRequest.

        后端服务器端口号。  支持多值查询，查询条件格式：*protocol_port=xxx&protocol_port=xxx*。

        :param protocol_port: The protocol_port of this ListAllMembersRequest.
        :type protocol_port: list[int]
        """
        self._protocol_port = protocol_port

    @property
    def id(self):
        """Gets the id of this ListAllMembersRequest.

        后端云服务器ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :return: The id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAllMembersRequest.

        后端云服务器ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :param id: The id of this ListAllMembersRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def operating_status(self):
        """Gets the operating_status of this ListAllMembersRequest.

        后端云服务器的健康状态。  取值： - ONLINE，后端服务器正常运行。 - NO_MONITOR，后端服务器无健康检查。 - OFFLINE，已下线。  支持多值查询，查询条件格式：*operating_status=xxx&operating_status=*。

        :return: The operating_status of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this ListAllMembersRequest.

        后端云服务器的健康状态。  取值： - ONLINE，后端服务器正常运行。 - NO_MONITOR，后端服务器无健康检查。 - OFFLINE，已下线。  支持多值查询，查询条件格式：*operating_status=xxx&operating_status=*。

        :param operating_status: The operating_status of this ListAllMembersRequest.
        :type operating_status: list[str]
        """
        self._operating_status = operating_status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAllMembersRequest.

        企业项目ID。不传时查询default企业项目\"0\"下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :return: The enterprise_project_id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAllMembersRequest.

        企业项目ID。不传时查询default企业项目\"0\"下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListAllMembersRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_version(self):
        """Gets the ip_version of this ListAllMembersRequest.

        IP版本，取值v4、v6。  支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。

        :return: The ip_version of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListAllMembersRequest.

        IP版本，取值v4、v6。  支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。

        :param ip_version: The ip_version of this ListAllMembersRequest.
        :type ip_version: list[str]
        """
        self._ip_version = ip_version

    @property
    def pool_id(self):
        """Gets the pool_id of this ListAllMembersRequest.

        member所属的服务器组ID  支持多值查询，查询条件格式：*pool_id=xxx&pool_id=xxx*。

        :return: The pool_id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this ListAllMembersRequest.

        member所属的服务器组ID  支持多值查询，查询条件格式：*pool_id=xxx&pool_id=xxx*。

        :param pool_id: The pool_id of this ListAllMembersRequest.
        :type pool_id: list[str]
        """
        self._pool_id = pool_id

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this ListAllMembersRequest.

        member所属的负载均衡器ID。  支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。

        :return: The loadbalancer_id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this ListAllMembersRequest.

        member所属的负载均衡器ID。  支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。

        :param loadbalancer_id: The loadbalancer_id of this ListAllMembersRequest.
        :type loadbalancer_id: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

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
        if not isinstance(other, ListAllMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
