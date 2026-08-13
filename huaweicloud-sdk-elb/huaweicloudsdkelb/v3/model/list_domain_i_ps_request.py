# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainIPsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancer_id': 'str',
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'ip_address': 'list[str]',
        'enable': 'bool',
        'type': 'list[str]',
        'domain_name': 'list[str]',
        'enterprise_project_id': 'list[str]'
    }

    attribute_map = {
        'loadbalancer_id': 'loadbalancer_id',
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'ip_address': 'ip_address',
        'enable': 'enable',
        'type': 'type',
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, loadbalancer_id=None, marker=None, limit=None, page_reverse=None, ip_address=None, enable=None, type=None, domain_name=None, enterprise_project_id=None):
        r"""ListDomainIPsRequest

        The model defined in huaweicloud sdk

        :param loadbalancer_id: **参数解释**：负载均衡器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type loadbalancer_id: str
        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param ip_address: **参数解释**：IPv4或IPv6地址。 支持多值查询，查询条件格式： *ip_address&#x3D;xxx&amp;ip_address&#x3D;xxx*。  **约束限制**：必须是当前负载均衡器绑定的私网地址或者公网地址。  **取值范围**：不涉及  **默认取值**：不涉及
        :type ip_address: list[str]
        :param enable: **参数解释**：IP地址是否已加入到域名解析。  **约束限制**：不涉及  **取值范围**： - true：已加入域名解析。 - false：未加入域名解析。  **默认取值**：不涉及
        :type enable: bool
        :param type: **参数解释**：IP地址类型。 支持多值查询，查询条件格式： *type&#x3D;xxx&amp;type&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**： - vip：私网IP。 - eip：公网IP。  **默认取值**：不涉及
        :type type: list[str]
        :param domain_name: **参数解释**：当前IP地址关联的负载均衡实例域名。 支持多值查询，查询条件格式： *domain_name&#x3D;xxx&amp;domain_name&#x3D;xxx*。  **约束限制**： - 如果IP为私网类型，则这里为负载均衡实例的私网域名。 - 如果IP为公网类型，则这里为负载均衡实例的公网域名。  **取值范围**：不涉及  **默认取值**：不涉及
        :type domain_name: list[str]
        :param enterprise_project_id: **参数解释**：所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:loadbalancers:listDnsConfig权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及
        :type enterprise_project_id: list[str]
        """
        
        

        self._loadbalancer_id = None
        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._ip_address = None
        self._enable = None
        self._type = None
        self._domain_name = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.loadbalancer_id = loadbalancer_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if ip_address is not None:
            self.ip_address = ip_address
        if enable is not None:
            self.enable = enable
        if type is not None:
            self.type = type
        if domain_name is not None:
            self.domain_name = domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this ListDomainIPsRequest.

        **参数解释**：负载均衡器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The loadbalancer_id of this ListDomainIPsRequest.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this ListDomainIPsRequest.

        **参数解释**：负载均衡器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param loadbalancer_id: The loadbalancer_id of this ListDomainIPsRequest.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def marker(self):
        r"""Gets the marker of this ListDomainIPsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListDomainIPsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListDomainIPsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListDomainIPsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListDomainIPsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListDomainIPsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDomainIPsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListDomainIPsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListDomainIPsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListDomainIPsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListDomainIPsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListDomainIPsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ListDomainIPsRequest.

        **参数解释**：IPv4或IPv6地址。 支持多值查询，查询条件格式： *ip_address=xxx&ip_address=xxx*。  **约束限制**：必须是当前负载均衡器绑定的私网地址或者公网地址。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The ip_address of this ListDomainIPsRequest.
        :rtype: list[str]
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ListDomainIPsRequest.

        **参数解释**：IPv4或IPv6地址。 支持多值查询，查询条件格式： *ip_address=xxx&ip_address=xxx*。  **约束限制**：必须是当前负载均衡器绑定的私网地址或者公网地址。  **取值范围**：不涉及  **默认取值**：不涉及

        :param ip_address: The ip_address of this ListDomainIPsRequest.
        :type ip_address: list[str]
        """
        self._ip_address = ip_address

    @property
    def enable(self):
        r"""Gets the enable of this ListDomainIPsRequest.

        **参数解释**：IP地址是否已加入到域名解析。  **约束限制**：不涉及  **取值范围**： - true：已加入域名解析。 - false：未加入域名解析。  **默认取值**：不涉及

        :return: The enable of this ListDomainIPsRequest.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ListDomainIPsRequest.

        **参数解释**：IP地址是否已加入到域名解析。  **约束限制**：不涉及  **取值范围**： - true：已加入域名解析。 - false：未加入域名解析。  **默认取值**：不涉及

        :param enable: The enable of this ListDomainIPsRequest.
        :type enable: bool
        """
        self._enable = enable

    @property
    def type(self):
        r"""Gets the type of this ListDomainIPsRequest.

        **参数解释**：IP地址类型。 支持多值查询，查询条件格式： *type=xxx&type=xxx*。  **约束限制**：不涉及  **取值范围**： - vip：私网IP。 - eip：公网IP。  **默认取值**：不涉及

        :return: The type of this ListDomainIPsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListDomainIPsRequest.

        **参数解释**：IP地址类型。 支持多值查询，查询条件格式： *type=xxx&type=xxx*。  **约束限制**：不涉及  **取值范围**： - vip：私网IP。 - eip：公网IP。  **默认取值**：不涉及

        :param type: The type of this ListDomainIPsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListDomainIPsRequest.

        **参数解释**：当前IP地址关联的负载均衡实例域名。 支持多值查询，查询条件格式： *domain_name=xxx&domain_name=xxx*。  **约束限制**： - 如果IP为私网类型，则这里为负载均衡实例的私网域名。 - 如果IP为公网类型，则这里为负载均衡实例的公网域名。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The domain_name of this ListDomainIPsRequest.
        :rtype: list[str]
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListDomainIPsRequest.

        **参数解释**：当前IP地址关联的负载均衡实例域名。 支持多值查询，查询条件格式： *domain_name=xxx&domain_name=xxx*。  **约束限制**： - 如果IP为私网类型，则这里为负载均衡实例的私网域名。 - 如果IP为公网类型，则这里为负载均衡实例的公网域名。  **取值范围**：不涉及  **默认取值**：不涉及

        :param domain_name: The domain_name of this ListDomainIPsRequest.
        :type domain_name: list[str]
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListDomainIPsRequest.

        **参数解释**：所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:loadbalancers:listDnsConfig权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The enterprise_project_id of this ListDomainIPsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListDomainIPsRequest.

        **参数解释**：所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:loadbalancers:listDnsConfig权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及

        :param enterprise_project_id: The enterprise_project_id of this ListDomainIPsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListDomainIPsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
