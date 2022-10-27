# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoolsRequest:

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
        'name': 'str',
        'description': 'str',
        'healthmonitor_id': 'str',
        'loadbalancer_id': 'str',
        'protocol': 'str',
        'lb_algorithm': 'str',
        'member_address': 'str',
        'member_device_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'healthmonitor_id': 'healthmonitor_id',
        'loadbalancer_id': 'loadbalancer_id',
        'protocol': 'protocol',
        'lb_algorithm': 'lb_algorithm',
        'member_address': 'member_address',
        'member_device_id': 'member_device_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, name=None, description=None, healthmonitor_id=None, loadbalancer_id=None, protocol=None, lb_algorithm=None, member_address=None, member_device_id=None, enterprise_project_id=None):
        """ListPoolsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询中每页的后端服务器组个数
        :type limit: int
        :param marker: 分页查询的起始的资源id，表示上一页最后一条查询记录的后端服务器组的id。不指定时表示查询第一页。
        :type marker: str
        :param page_reverse: 分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。
        :type page_reverse: bool
        :param id: 后端云服务器组ID。
        :type id: str
        :param name: 后端云服务器组名称。
        :type name: str
        :param description: 后端云服务器组的描述信息。
        :type description: str
        :param healthmonitor_id: 后端云服务器组关联的健康检查的ID。
        :type healthmonitor_id: str
        :param loadbalancer_id: 后端云服务器组关联的负载均衡器ID。
        :type loadbalancer_id: str
        :param protocol: 后端云服务器组的后端协议。支持TCP、UDP和HTTP。
        :type protocol: str
        :param lb_algorithm: 后端云服务器组的负载均衡算法。取值范围：ROUND_ROBIN：加权轮询算法。LEAST_CONNECTIONS：加权最少连接算法。SOURCE_IP：源IP算法。当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。
        :type lb_algorithm: str
        :param member_address: 后端云服务器组关联的后端云服务器IP。
        :type member_address: str
        :param member_device_id: 后端云服务器组关联的后端云服务器对应的弹性云服务器的ID。
        :type member_device_id: str
        :param enterprise_project_id: 企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\&quot;0\&quot;表示查询默认企业项目资源；或者指定的企业项目ID下的资源。
        :type enterprise_project_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._healthmonitor_id = None
        self._loadbalancer_id = None
        self._protocol = None
        self._lb_algorithm = None
        self._member_address = None
        self._member_device_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if healthmonitor_id is not None:
            self.healthmonitor_id = healthmonitor_id
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if protocol is not None:
            self.protocol = protocol
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if member_address is not None:
            self.member_address = member_address
        if member_device_id is not None:
            self.member_device_id = member_device_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListPoolsRequest.

        分页查询中每页的后端服务器组个数

        :return: The limit of this ListPoolsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPoolsRequest.

        分页查询中每页的后端服务器组个数

        :param limit: The limit of this ListPoolsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPoolsRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的后端服务器组的id。不指定时表示查询第一页。

        :return: The marker of this ListPoolsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPoolsRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的后端服务器组的id。不指定时表示查询第一页。

        :param marker: The marker of this ListPoolsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListPoolsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :return: The page_reverse of this ListPoolsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListPoolsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :param page_reverse: The page_reverse of this ListPoolsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListPoolsRequest.

        后端云服务器组ID。

        :return: The id of this ListPoolsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPoolsRequest.

        后端云服务器组ID。

        :param id: The id of this ListPoolsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListPoolsRequest.

        后端云服务器组名称。

        :return: The name of this ListPoolsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPoolsRequest.

        后端云服务器组名称。

        :param name: The name of this ListPoolsRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListPoolsRequest.

        后端云服务器组的描述信息。

        :return: The description of this ListPoolsRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListPoolsRequest.

        后端云服务器组的描述信息。

        :param description: The description of this ListPoolsRequest.
        :type description: str
        """
        self._description = description

    @property
    def healthmonitor_id(self):
        """Gets the healthmonitor_id of this ListPoolsRequest.

        后端云服务器组关联的健康检查的ID。

        :return: The healthmonitor_id of this ListPoolsRequest.
        :rtype: str
        """
        return self._healthmonitor_id

    @healthmonitor_id.setter
    def healthmonitor_id(self, healthmonitor_id):
        """Sets the healthmonitor_id of this ListPoolsRequest.

        后端云服务器组关联的健康检查的ID。

        :param healthmonitor_id: The healthmonitor_id of this ListPoolsRequest.
        :type healthmonitor_id: str
        """
        self._healthmonitor_id = healthmonitor_id

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this ListPoolsRequest.

        后端云服务器组关联的负载均衡器ID。

        :return: The loadbalancer_id of this ListPoolsRequest.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this ListPoolsRequest.

        后端云服务器组关联的负载均衡器ID。

        :param loadbalancer_id: The loadbalancer_id of this ListPoolsRequest.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def protocol(self):
        """Gets the protocol of this ListPoolsRequest.

        后端云服务器组的后端协议。支持TCP、UDP和HTTP。

        :return: The protocol of this ListPoolsRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListPoolsRequest.

        后端云服务器组的后端协议。支持TCP、UDP和HTTP。

        :param protocol: The protocol of this ListPoolsRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this ListPoolsRequest.

        后端云服务器组的负载均衡算法。取值范围：ROUND_ROBIN：加权轮询算法。LEAST_CONNECTIONS：加权最少连接算法。SOURCE_IP：源IP算法。当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。

        :return: The lb_algorithm of this ListPoolsRequest.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this ListPoolsRequest.

        后端云服务器组的负载均衡算法。取值范围：ROUND_ROBIN：加权轮询算法。LEAST_CONNECTIONS：加权最少连接算法。SOURCE_IP：源IP算法。当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。

        :param lb_algorithm: The lb_algorithm of this ListPoolsRequest.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def member_address(self):
        """Gets the member_address of this ListPoolsRequest.

        后端云服务器组关联的后端云服务器IP。

        :return: The member_address of this ListPoolsRequest.
        :rtype: str
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        """Sets the member_address of this ListPoolsRequest.

        后端云服务器组关联的后端云服务器IP。

        :param member_address: The member_address of this ListPoolsRequest.
        :type member_address: str
        """
        self._member_address = member_address

    @property
    def member_device_id(self):
        """Gets the member_device_id of this ListPoolsRequest.

        后端云服务器组关联的后端云服务器对应的弹性云服务器的ID。

        :return: The member_device_id of this ListPoolsRequest.
        :rtype: str
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        """Sets the member_device_id of this ListPoolsRequest.

        后端云服务器组关联的后端云服务器对应的弹性云服务器的ID。

        :param member_device_id: The member_device_id of this ListPoolsRequest.
        :type member_device_id: str
        """
        self._member_device_id = member_device_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPoolsRequest.

        企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\"0\"表示查询默认企业项目资源；或者指定的企业项目ID下的资源。

        :return: The enterprise_project_id of this ListPoolsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPoolsRequest.

        企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\"0\"表示查询默认企业项目资源；或者指定的企业项目ID下的资源。

        :param enterprise_project_id: The enterprise_project_id of this ListPoolsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListPoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
