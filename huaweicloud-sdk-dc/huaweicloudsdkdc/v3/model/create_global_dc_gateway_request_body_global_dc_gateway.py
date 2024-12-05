# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGlobalDcGatewayRequestBodyGlobalDcGateway:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'bgp_asn': 'int',
        'enterprise_project_id': 'str',
        'address_family': 'str',
        'tags': 'list[CreateGlobalDcGatewayRequestBodyGlobalDcGatewayTags]'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'bgp_asn': 'bgp_asn',
        'enterprise_project_id': 'enterprise_project_id',
        'address_family': 'address_family',
        'tags': 'tags'
    }

    def __init__(self, tenant_id=None, name=None, description=None, bgp_asn=None, enterprise_project_id=None, address_family=None, tags=None):
        """CreateGlobalDcGatewayRequestBodyGlobalDcGateway

        The model defined in huaweicloud sdk

        :param tenant_id: 租户ID
        :type tenant_id: str
        :param name: 全球接入网关名称
        :type name: str
        :param description: 描述信息
        :type description: str
        :param bgp_asn: BGP模式的AS号
        :type bgp_asn: int
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param address_family: 地址簇类型
        :type address_family: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdc.v3.CreateGlobalDcGatewayRequestBodyGlobalDcGatewayTags`]
        """
        
        

        self._tenant_id = None
        self._name = None
        self._description = None
        self._bgp_asn = None
        self._enterprise_project_id = None
        self._address_family = None
        self._tags = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.name = name
        if description is not None:
            self.description = description
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if address_family is not None:
            self.address_family = address_family
        if tags is not None:
            self.tags = tags

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        租户ID

        :return: The tenant_id of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        租户ID

        :param tenant_id: The tenant_id of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        全球接入网关名称

        :return: The name of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        全球接入网关名称

        :param name: The name of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        描述信息

        :return: The description of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        描述信息

        :param description: The description of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :type description: str
        """
        self._description = description

    @property
    def bgp_asn(self):
        """Gets the bgp_asn of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        BGP模式的AS号

        :return: The bgp_asn of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        """Sets the bgp_asn of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        BGP模式的AS号

        :param bgp_asn: The bgp_asn of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        企业项目ID

        :return: The enterprise_project_id of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def address_family(self):
        """Gets the address_family of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        地址簇类型

        :return: The address_family of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        地址簇类型

        :param address_family: The address_family of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :type address_family: str
        """
        self._address_family = address_family

    @property
    def tags(self):
        """Gets the tags of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        标签

        :return: The tags of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :rtype: list[:class:`huaweicloudsdkdc.v3.CreateGlobalDcGatewayRequestBodyGlobalDcGatewayTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.

        标签

        :param tags: The tags of this CreateGlobalDcGatewayRequestBodyGlobalDcGateway.
        :type tags: list[:class:`huaweicloudsdkdc.v3.CreateGlobalDcGatewayRequestBodyGlobalDcGatewayTags`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateGlobalDcGatewayRequestBodyGlobalDcGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
