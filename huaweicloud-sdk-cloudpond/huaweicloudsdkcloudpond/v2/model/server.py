# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Server:

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
        'domain_id': 'str',
        'edge_site_id': 'str',
        'name': 'str',
        'status': 'str',
        'offering_id': 'str',
        'spec': 'ServerResourceSpec',
        'market_options': 'MarketOptions',
        'location': 'LayoutLocation',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'edge_site_id': 'edge_site_id',
        'name': 'name',
        'status': 'status',
        'offering_id': 'offering_id',
        'spec': 'spec',
        'market_options': 'market_options',
        'location': 'location',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, domain_id=None, edge_site_id=None, name=None, status=None, offering_id=None, spec=None, market_options=None, location=None, created_at=None, updated_at=None):
        r"""Server

        The model defined in huaweicloud sdk

        :param id: 资源ID
        :type id: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param edge_site_id: 站点ID
        :type edge_site_id: str
        :param name: 名称
        :type name: str
        :param status: - PENDING_PAYMENT：待支付 - DELIVERING：交付中 - USING：使用中
        :type status: str
        :param offering_id: 商品ID
        :type offering_id: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkcloudpond.v2.ServerResourceSpec`
        :param market_options: 
        :type market_options: :class:`huaweicloudsdkcloudpond.v2.MarketOptions`
        :param location: 
        :type location: :class:`huaweicloudsdkcloudpond.v2.LayoutLocation`
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._domain_id = None
        self._edge_site_id = None
        self._name = None
        self._status = None
        self._offering_id = None
        self._spec = None
        self._market_options = None
        self._location = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if edge_site_id is not None:
            self.edge_site_id = edge_site_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if offering_id is not None:
            self.offering_id = offering_id
        if spec is not None:
            self.spec = spec
        if market_options is not None:
            self.market_options = market_options
        if location is not None:
            self.location = location
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this Server.

        资源ID

        :return: The id of this Server.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Server.

        资源ID

        :param id: The id of this Server.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this Server.

        账号ID

        :return: The domain_id of this Server.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this Server.

        账号ID

        :param domain_id: The domain_id of this Server.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def edge_site_id(self):
        r"""Gets the edge_site_id of this Server.

        站点ID

        :return: The edge_site_id of this Server.
        :rtype: str
        """
        return self._edge_site_id

    @edge_site_id.setter
    def edge_site_id(self, edge_site_id):
        r"""Sets the edge_site_id of this Server.

        站点ID

        :param edge_site_id: The edge_site_id of this Server.
        :type edge_site_id: str
        """
        self._edge_site_id = edge_site_id

    @property
    def name(self):
        r"""Gets the name of this Server.

        名称

        :return: The name of this Server.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Server.

        名称

        :param name: The name of this Server.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this Server.

        - PENDING_PAYMENT：待支付 - DELIVERING：交付中 - USING：使用中

        :return: The status of this Server.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Server.

        - PENDING_PAYMENT：待支付 - DELIVERING：交付中 - USING：使用中

        :param status: The status of this Server.
        :type status: str
        """
        self._status = status

    @property
    def offering_id(self):
        r"""Gets the offering_id of this Server.

        商品ID

        :return: The offering_id of this Server.
        :rtype: str
        """
        return self._offering_id

    @offering_id.setter
    def offering_id(self, offering_id):
        r"""Sets the offering_id of this Server.

        商品ID

        :param offering_id: The offering_id of this Server.
        :type offering_id: str
        """
        self._offering_id = offering_id

    @property
    def spec(self):
        r"""Gets the spec of this Server.

        :return: The spec of this Server.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ServerResourceSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this Server.

        :param spec: The spec of this Server.
        :type spec: :class:`huaweicloudsdkcloudpond.v2.ServerResourceSpec`
        """
        self._spec = spec

    @property
    def market_options(self):
        r"""Gets the market_options of this Server.

        :return: The market_options of this Server.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.MarketOptions`
        """
        return self._market_options

    @market_options.setter
    def market_options(self, market_options):
        r"""Sets the market_options of this Server.

        :param market_options: The market_options of this Server.
        :type market_options: :class:`huaweicloudsdkcloudpond.v2.MarketOptions`
        """
        self._market_options = market_options

    @property
    def location(self):
        r"""Gets the location of this Server.

        :return: The location of this Server.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.LayoutLocation`
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this Server.

        :param location: The location of this Server.
        :type location: :class:`huaweicloudsdkcloudpond.v2.LayoutLocation`
        """
        self._location = location

    @property
    def created_at(self):
        r"""Gets the created_at of this Server.

        创建时间

        :return: The created_at of this Server.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Server.

        创建时间

        :param created_at: The created_at of this Server.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Server.

        更新时间

        :return: The updated_at of this Server.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Server.

        更新时间

        :param updated_at: The updated_at of this Server.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, Server):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
