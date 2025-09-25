# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateP2cVgwRequestBodyContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'vpc_id': 'str',
        'connect_subnet': 'str',
        'flavor': 'str',
        'availability_zone_ids': 'list[str]',
        'eip': 'CreateP2cRequestEip',
        'max_connection_number': 'int',
        'enterprise_project_id': 'str',
        'tags': 'list[VpnResourceTag]'
    }

    attribute_map = {
        'name': 'name',
        'vpc_id': 'vpc_id',
        'connect_subnet': 'connect_subnet',
        'flavor': 'flavor',
        'availability_zone_ids': 'availability_zone_ids',
        'eip': 'eip',
        'max_connection_number': 'max_connection_number',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, name=None, vpc_id=None, connect_subnet=None, flavor=None, availability_zone_ids=None, eip=None, max_connection_number=None, enterprise_project_id=None, tags=None):
        r"""CreateP2cVgwRequestBodyContent

        The model defined in huaweicloud sdk

        :param name: P2C VPN网关名称。1-64字符，中文、英文、数字包含下划线
        :type name: str
        :param vpc_id: P2C VPN网关所连接的VPC的ID。标准UUID
        :type vpc_id: str
        :param connect_subnet: P2C VPN网关所使用的VPC子网ID。标准的UUID
        :type connect_subnet: str
        :param flavor: P2C VPN网关的规格类型
        :type flavor: str
        :param availability_zone_ids: 不填时自动为P2C VPN网关选择可用区。如果需要指定可用区可以通过查询VPN网关可用区查询可用区列表
        :type availability_zone_ids: list[str]
        :param eip: 
        :type eip: :class:`huaweicloudsdkvpn.v5.CreateP2cRequestEip`
        :param max_connection_number: 最大并发客户端连接数，且不超过规格的最大连接数
        :type max_connection_number: int
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param tags: 
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        
        

        self._name = None
        self._vpc_id = None
        self._connect_subnet = None
        self._flavor = None
        self._availability_zone_ids = None
        self._eip = None
        self._max_connection_number = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.vpc_id = vpc_id
        self.connect_subnet = connect_subnet
        if flavor is not None:
            self.flavor = flavor
        if availability_zone_ids is not None:
            self.availability_zone_ids = availability_zone_ids
        self.eip = eip
        if max_connection_number is not None:
            self.max_connection_number = max_connection_number
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateP2cVgwRequestBodyContent.

        P2C VPN网关名称。1-64字符，中文、英文、数字包含下划线

        :return: The name of this CreateP2cVgwRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateP2cVgwRequestBodyContent.

        P2C VPN网关名称。1-64字符，中文、英文、数字包含下划线

        :param name: The name of this CreateP2cVgwRequestBodyContent.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateP2cVgwRequestBodyContent.

        P2C VPN网关所连接的VPC的ID。标准UUID

        :return: The vpc_id of this CreateP2cVgwRequestBodyContent.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateP2cVgwRequestBodyContent.

        P2C VPN网关所连接的VPC的ID。标准UUID

        :param vpc_id: The vpc_id of this CreateP2cVgwRequestBodyContent.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def connect_subnet(self):
        r"""Gets the connect_subnet of this CreateP2cVgwRequestBodyContent.

        P2C VPN网关所使用的VPC子网ID。标准的UUID

        :return: The connect_subnet of this CreateP2cVgwRequestBodyContent.
        :rtype: str
        """
        return self._connect_subnet

    @connect_subnet.setter
    def connect_subnet(self, connect_subnet):
        r"""Sets the connect_subnet of this CreateP2cVgwRequestBodyContent.

        P2C VPN网关所使用的VPC子网ID。标准的UUID

        :param connect_subnet: The connect_subnet of this CreateP2cVgwRequestBodyContent.
        :type connect_subnet: str
        """
        self._connect_subnet = connect_subnet

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateP2cVgwRequestBodyContent.

        P2C VPN网关的规格类型

        :return: The flavor of this CreateP2cVgwRequestBodyContent.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateP2cVgwRequestBodyContent.

        P2C VPN网关的规格类型

        :param flavor: The flavor of this CreateP2cVgwRequestBodyContent.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def availability_zone_ids(self):
        r"""Gets the availability_zone_ids of this CreateP2cVgwRequestBodyContent.

        不填时自动为P2C VPN网关选择可用区。如果需要指定可用区可以通过查询VPN网关可用区查询可用区列表

        :return: The availability_zone_ids of this CreateP2cVgwRequestBodyContent.
        :rtype: list[str]
        """
        return self._availability_zone_ids

    @availability_zone_ids.setter
    def availability_zone_ids(self, availability_zone_ids):
        r"""Sets the availability_zone_ids of this CreateP2cVgwRequestBodyContent.

        不填时自动为P2C VPN网关选择可用区。如果需要指定可用区可以通过查询VPN网关可用区查询可用区列表

        :param availability_zone_ids: The availability_zone_ids of this CreateP2cVgwRequestBodyContent.
        :type availability_zone_ids: list[str]
        """
        self._availability_zone_ids = availability_zone_ids

    @property
    def eip(self):
        r"""Gets the eip of this CreateP2cVgwRequestBodyContent.

        :return: The eip of this CreateP2cVgwRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateP2cRequestEip`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this CreateP2cVgwRequestBodyContent.

        :param eip: The eip of this CreateP2cVgwRequestBodyContent.
        :type eip: :class:`huaweicloudsdkvpn.v5.CreateP2cRequestEip`
        """
        self._eip = eip

    @property
    def max_connection_number(self):
        r"""Gets the max_connection_number of this CreateP2cVgwRequestBodyContent.

        最大并发客户端连接数，且不超过规格的最大连接数

        :return: The max_connection_number of this CreateP2cVgwRequestBodyContent.
        :rtype: int
        """
        return self._max_connection_number

    @max_connection_number.setter
    def max_connection_number(self, max_connection_number):
        r"""Sets the max_connection_number of this CreateP2cVgwRequestBodyContent.

        最大并发客户端连接数，且不超过规格的最大连接数

        :param max_connection_number: The max_connection_number of this CreateP2cVgwRequestBodyContent.
        :type max_connection_number: int
        """
        self._max_connection_number = max_connection_number

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateP2cVgwRequestBodyContent.

        企业项目ID

        :return: The enterprise_project_id of this CreateP2cVgwRequestBodyContent.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateP2cVgwRequestBodyContent.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateP2cVgwRequestBodyContent.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateP2cVgwRequestBodyContent.

        :return: The tags of this CreateP2cVgwRequestBodyContent.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateP2cVgwRequestBodyContent.

        :param tags: The tags of this CreateP2cVgwRequestBodyContent.
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
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
        if not isinstance(other, CreateP2cVgwRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
