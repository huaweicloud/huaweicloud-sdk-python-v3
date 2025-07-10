# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNatGatewaysRequest:

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
        'enterprise_project_id': 'str',
        'description': 'str',
        'created_at': 'str',
        'name': 'str',
        'status': 'list[str]',
        'spec': 'list[str]',
        'router_id': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'id': 'id',
        'enterprise_project_id': 'enterprise_project_id',
        'description': 'description',
        'created_at': 'created_at',
        'name': 'name',
        'status': 'status',
        'spec': 'spec',
        'router_id': 'router_id',
        'limit': 'limit'
    }

    def __init__(self, id=None, enterprise_project_id=None, description=None, created_at=None, name=None, status=None, spec=None, router_id=None, limit=None):
        r"""ListNatGatewaysRequest

        The model defined in huaweicloud sdk

        :param id: 公网NAT网关实例的ID。
        :type id: str
        :param enterprise_project_id: 企业项目ID。创建公网NAT网关实例时，关联的企业项目ID。
        :type enterprise_project_id: str
        :param description: 公网NAT网关实例的描述，长度限制为255。
        :type description: str
        :param created_at: 公网NAT网关实例的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。
        :type created_at: str
        :param name: 公网NAT网关实例的名字，长度限制为64。公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。
        :type name: str
        :param status: 公网NAT网关实例的状态。 枚举值：  ACTIVE PENDING_CREATE PENDING_UPDATE PENDING_DELETE INACTIVE
        :type status: list[str]
        :param spec: 公网NAT网关实例的规格。取值为： \&quot;1\&quot;：小型，SNAT最大连接数10000；\&quot;2\&quot;：中型，SNAT最大连接数50000；\&quot;3\&quot;：大型，SNAT最大连接数200000；\&quot;4\&quot;：超大型，SNAT最大连接数1000000。
        :type spec: list[str]
        :param router_id: VPC的id。
        :type router_id: str
        :param limit: 功能说明：每页返回的个数。取值范围：1~2000。默认值：2000。
        :type limit: int
        """
        
        

        self._id = None
        self._enterprise_project_id = None
        self._description = None
        self._created_at = None
        self._name = None
        self._status = None
        self._spec = None
        self._router_id = None
        self._limit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if spec is not None:
            self.spec = spec
        if router_id is not None:
            self.router_id = router_id
        if limit is not None:
            self.limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListNatGatewaysRequest.

        公网NAT网关实例的ID。

        :return: The id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListNatGatewaysRequest.

        公网NAT网关实例的ID。

        :param id: The id of this ListNatGatewaysRequest.
        :type id: str
        """
        self._id = id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListNatGatewaysRequest.

        企业项目ID。创建公网NAT网关实例时，关联的企业项目ID。

        :return: The enterprise_project_id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListNatGatewaysRequest.

        企业项目ID。创建公网NAT网关实例时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListNatGatewaysRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def description(self):
        r"""Gets the description of this ListNatGatewaysRequest.

        公网NAT网关实例的描述，长度限制为255。

        :return: The description of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListNatGatewaysRequest.

        公网NAT网关实例的描述，长度限制为255。

        :param description: The description of this ListNatGatewaysRequest.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this ListNatGatewaysRequest.

        公网NAT网关实例的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :return: The created_at of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ListNatGatewaysRequest.

        公网NAT网关实例的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :param created_at: The created_at of this ListNatGatewaysRequest.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def name(self):
        r"""Gets the name of this ListNatGatewaysRequest.

        公网NAT网关实例的名字，长度限制为64。公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :return: The name of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListNatGatewaysRequest.

        公网NAT网关实例的名字，长度限制为64。公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :param name: The name of this ListNatGatewaysRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListNatGatewaysRequest.

        公网NAT网关实例的状态。 枚举值：  ACTIVE PENDING_CREATE PENDING_UPDATE PENDING_DELETE INACTIVE

        :return: The status of this ListNatGatewaysRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListNatGatewaysRequest.

        公网NAT网关实例的状态。 枚举值：  ACTIVE PENDING_CREATE PENDING_UPDATE PENDING_DELETE INACTIVE

        :param status: The status of this ListNatGatewaysRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def spec(self):
        r"""Gets the spec of this ListNatGatewaysRequest.

        公网NAT网关实例的规格。取值为： \"1\"：小型，SNAT最大连接数10000；\"2\"：中型，SNAT最大连接数50000；\"3\"：大型，SNAT最大连接数200000；\"4\"：超大型，SNAT最大连接数1000000。

        :return: The spec of this ListNatGatewaysRequest.
        :rtype: list[str]
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ListNatGatewaysRequest.

        公网NAT网关实例的规格。取值为： \"1\"：小型，SNAT最大连接数10000；\"2\"：中型，SNAT最大连接数50000；\"3\"：大型，SNAT最大连接数200000；\"4\"：超大型，SNAT最大连接数1000000。

        :param spec: The spec of this ListNatGatewaysRequest.
        :type spec: list[str]
        """
        self._spec = spec

    @property
    def router_id(self):
        r"""Gets the router_id of this ListNatGatewaysRequest.

        VPC的id。

        :return: The router_id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        r"""Sets the router_id of this ListNatGatewaysRequest.

        VPC的id。

        :param router_id: The router_id of this ListNatGatewaysRequest.
        :type router_id: str
        """
        self._router_id = router_id

    @property
    def limit(self):
        r"""Gets the limit of this ListNatGatewaysRequest.

        功能说明：每页返回的个数。取值范围：1~2000。默认值：2000。

        :return: The limit of this ListNatGatewaysRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNatGatewaysRequest.

        功能说明：每页返回的个数。取值范围：1~2000。默认值：2000。

        :param limit: The limit of this ListNatGatewaysRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListNatGatewaysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
