# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateSnat:

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
        'project_id': 'str',
        'gateway_id': 'str',
        'cidr': 'str',
        'virsubnet_id': 'str',
        'description': 'str',
        'transit_ip_associations': 'list[AssociatedTransitIp]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'gateway_id': 'gateway_id',
        'cidr': 'cidr',
        'virsubnet_id': 'virsubnet_id',
        'description': 'description',
        'transit_ip_associations': 'transit_ip_associations',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, project_id=None, gateway_id=None, cidr=None, virsubnet_id=None, description=None, transit_ip_associations=None, created_at=None, updated_at=None, enterprise_project_id=None):
        """PrivateSnat

        The model defined in huaweicloud sdk

        :param id: SNAT规则的ID。
        :type id: str
        :param project_id: 项目的ID。
        :type project_id: str
        :param gateway_id: 私网NAT网关实例的ID。
        :type gateway_id: str
        :param cidr: 功能说明：规则匹配的CIDR。 取值约束： - 与virsubnet_id参数二选一。 - cidr不能与已有snat规则的网段相同。
        :type cidr: str
        :param virsubnet_id: 功能说明：规则匹配的子网的ID。 取值约束：与cidr参数二选一。
        :type virsubnet_id: str
        :param description: SNAT规则的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param transit_ip_associations: 关联的中转IP详情列表。
        :type transit_ip_associations: list[:class:`huaweicloudsdknat.v2.AssociatedTransitIp`]
        :param created_at: SNAT规则的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。
        :type created_at: datetime
        :param updated_at: SNAT规则的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。
        :type updated_at: datetime
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._project_id = None
        self._gateway_id = None
        self._cidr = None
        self._virsubnet_id = None
        self._description = None
        self._transit_ip_associations = None
        self._created_at = None
        self._updated_at = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if cidr is not None:
            self.cidr = cidr
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if description is not None:
            self.description = description
        if transit_ip_associations is not None:
            self.transit_ip_associations = transit_ip_associations
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this PrivateSnat.

        SNAT规则的ID。

        :return: The id of this PrivateSnat.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivateSnat.

        SNAT规则的ID。

        :param id: The id of this PrivateSnat.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this PrivateSnat.

        项目的ID。

        :return: The project_id of this PrivateSnat.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PrivateSnat.

        项目的ID。

        :param project_id: The project_id of this PrivateSnat.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def gateway_id(self):
        """Gets the gateway_id of this PrivateSnat.

        私网NAT网关实例的ID。

        :return: The gateway_id of this PrivateSnat.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this PrivateSnat.

        私网NAT网关实例的ID。

        :param gateway_id: The gateway_id of this PrivateSnat.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def cidr(self):
        """Gets the cidr of this PrivateSnat.

        功能说明：规则匹配的CIDR。 取值约束： - 与virsubnet_id参数二选一。 - cidr不能与已有snat规则的网段相同。

        :return: The cidr of this PrivateSnat.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this PrivateSnat.

        功能说明：规则匹配的CIDR。 取值约束： - 与virsubnet_id参数二选一。 - cidr不能与已有snat规则的网段相同。

        :param cidr: The cidr of this PrivateSnat.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this PrivateSnat.

        功能说明：规则匹配的子网的ID。 取值约束：与cidr参数二选一。

        :return: The virsubnet_id of this PrivateSnat.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this PrivateSnat.

        功能说明：规则匹配的子网的ID。 取值约束：与cidr参数二选一。

        :param virsubnet_id: The virsubnet_id of this PrivateSnat.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def description(self):
        """Gets the description of this PrivateSnat.

        SNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this PrivateSnat.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PrivateSnat.

        SNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this PrivateSnat.
        :type description: str
        """
        self._description = description

    @property
    def transit_ip_associations(self):
        """Gets the transit_ip_associations of this PrivateSnat.

        关联的中转IP详情列表。

        :return: The transit_ip_associations of this PrivateSnat.
        :rtype: list[:class:`huaweicloudsdknat.v2.AssociatedTransitIp`]
        """
        return self._transit_ip_associations

    @transit_ip_associations.setter
    def transit_ip_associations(self, transit_ip_associations):
        """Sets the transit_ip_associations of this PrivateSnat.

        关联的中转IP详情列表。

        :param transit_ip_associations: The transit_ip_associations of this PrivateSnat.
        :type transit_ip_associations: list[:class:`huaweicloudsdknat.v2.AssociatedTransitIp`]
        """
        self._transit_ip_associations = transit_ip_associations

    @property
    def created_at(self):
        """Gets the created_at of this PrivateSnat.

        SNAT规则的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :return: The created_at of this PrivateSnat.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PrivateSnat.

        SNAT规则的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :param created_at: The created_at of this PrivateSnat.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PrivateSnat.

        SNAT规则的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :return: The updated_at of this PrivateSnat.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PrivateSnat.

        SNAT规则的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :param updated_at: The updated_at of this PrivateSnat.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PrivateSnat.

        企业项目id

        :return: The enterprise_project_id of this PrivateSnat.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PrivateSnat.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this PrivateSnat.
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
        if not isinstance(other, PrivateSnat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
