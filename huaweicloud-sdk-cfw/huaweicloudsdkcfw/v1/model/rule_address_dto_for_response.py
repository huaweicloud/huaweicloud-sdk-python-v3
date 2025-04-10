# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleAddressDtoForResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'address_type': 'int',
        'address': 'str',
        'address_set_id': 'str',
        'address_set_name': 'str',
        'domain_address_name': 'str',
        'region_list_json': 'str',
        'region_list': 'list[IpRegionDto]',
        'domain_set_id': 'str',
        'domain_set_name': 'str',
        'ip_address': 'list[str]',
        'address_group': 'list[str]',
        'address_group_names': 'list[AddressGroupVO]',
        'address_set_type': 'int'
    }

    attribute_map = {
        'type': 'type',
        'address_type': 'address_type',
        'address': 'address',
        'address_set_id': 'address_set_id',
        'address_set_name': 'address_set_name',
        'domain_address_name': 'domain_address_name',
        'region_list_json': 'region_list_json',
        'region_list': 'region_list',
        'domain_set_id': 'domain_set_id',
        'domain_set_name': 'domain_set_name',
        'ip_address': 'ip_address',
        'address_group': 'address_group',
        'address_group_names': 'address_group_names',
        'address_set_type': 'address_set_type'
    }

    def __init__(self, type=None, address_type=None, address=None, address_set_id=None, address_set_name=None, domain_address_name=None, region_list_json=None, region_list=None, domain_set_id=None, domain_set_name=None, ip_address=None, address_group=None, address_group_names=None, address_set_type=None):
        r"""RuleAddressDtoForResponse

        The model defined in huaweicloud sdk

        :param type: 地址类型0手工输入，1关联IP地址组，2域名，3地理位置，4域名组，5多对象，6域名组-DNS解析，7域名组-应用型。
        :type type: int
        :param address_type: 地址类型0 ipv4，1 ipv6，当type为0手动输入类型时不能为空
        :type address_type: int
        :param address: IP地址信息
        :type address: str
        :param address_set_id: 关联IP地址组ID
        :type address_set_id: str
        :param address_set_name: 地址组名称
        :type address_set_name: str
        :param domain_address_name: 域名地址名称
        :type domain_address_name: str
        :param region_list_json: 规则地域列表json值
        :type region_list_json: str
        :param region_list: 规则地域列表
        :type region_list: list[:class:`huaweicloudsdkcfw.v1.IpRegionDto`]
        :param domain_set_id: 域名组id
        :type domain_set_id: str
        :param domain_set_name: 域名组名称
        :type domain_set_name: str
        :param ip_address: IP地址列表
        :type ip_address: list[str]
        :param address_group: 地址组id列表
        :type address_group: list[str]
        :param address_group_names: 地址组名称列表
        :type address_group_names: list[:class:`huaweicloudsdkcfw.v1.AddressGroupVO`]
        :param address_set_type: 地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组
        :type address_set_type: int
        """
        
        

        self._type = None
        self._address_type = None
        self._address = None
        self._address_set_id = None
        self._address_set_name = None
        self._domain_address_name = None
        self._region_list_json = None
        self._region_list = None
        self._domain_set_id = None
        self._domain_set_name = None
        self._ip_address = None
        self._address_group = None
        self._address_group_names = None
        self._address_set_type = None
        self.discriminator = None

        self.type = type
        if address_type is not None:
            self.address_type = address_type
        if address is not None:
            self.address = address
        if address_set_id is not None:
            self.address_set_id = address_set_id
        if address_set_name is not None:
            self.address_set_name = address_set_name
        if domain_address_name is not None:
            self.domain_address_name = domain_address_name
        if region_list_json is not None:
            self.region_list_json = region_list_json
        if region_list is not None:
            self.region_list = region_list
        if domain_set_id is not None:
            self.domain_set_id = domain_set_id
        if domain_set_name is not None:
            self.domain_set_name = domain_set_name
        if ip_address is not None:
            self.ip_address = ip_address
        if address_group is not None:
            self.address_group = address_group
        if address_group_names is not None:
            self.address_group_names = address_group_names
        if address_set_type is not None:
            self.address_set_type = address_set_type

    @property
    def type(self):
        r"""Gets the type of this RuleAddressDtoForResponse.

        地址类型0手工输入，1关联IP地址组，2域名，3地理位置，4域名组，5多对象，6域名组-DNS解析，7域名组-应用型。

        :return: The type of this RuleAddressDtoForResponse.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RuleAddressDtoForResponse.

        地址类型0手工输入，1关联IP地址组，2域名，3地理位置，4域名组，5多对象，6域名组-DNS解析，7域名组-应用型。

        :param type: The type of this RuleAddressDtoForResponse.
        :type type: int
        """
        self._type = type

    @property
    def address_type(self):
        r"""Gets the address_type of this RuleAddressDtoForResponse.

        地址类型0 ipv4，1 ipv6，当type为0手动输入类型时不能为空

        :return: The address_type of this RuleAddressDtoForResponse.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this RuleAddressDtoForResponse.

        地址类型0 ipv4，1 ipv6，当type为0手动输入类型时不能为空

        :param address_type: The address_type of this RuleAddressDtoForResponse.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def address(self):
        r"""Gets the address of this RuleAddressDtoForResponse.

        IP地址信息

        :return: The address of this RuleAddressDtoForResponse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this RuleAddressDtoForResponse.

        IP地址信息

        :param address: The address of this RuleAddressDtoForResponse.
        :type address: str
        """
        self._address = address

    @property
    def address_set_id(self):
        r"""Gets the address_set_id of this RuleAddressDtoForResponse.

        关联IP地址组ID

        :return: The address_set_id of this RuleAddressDtoForResponse.
        :rtype: str
        """
        return self._address_set_id

    @address_set_id.setter
    def address_set_id(self, address_set_id):
        r"""Sets the address_set_id of this RuleAddressDtoForResponse.

        关联IP地址组ID

        :param address_set_id: The address_set_id of this RuleAddressDtoForResponse.
        :type address_set_id: str
        """
        self._address_set_id = address_set_id

    @property
    def address_set_name(self):
        r"""Gets the address_set_name of this RuleAddressDtoForResponse.

        地址组名称

        :return: The address_set_name of this RuleAddressDtoForResponse.
        :rtype: str
        """
        return self._address_set_name

    @address_set_name.setter
    def address_set_name(self, address_set_name):
        r"""Sets the address_set_name of this RuleAddressDtoForResponse.

        地址组名称

        :param address_set_name: The address_set_name of this RuleAddressDtoForResponse.
        :type address_set_name: str
        """
        self._address_set_name = address_set_name

    @property
    def domain_address_name(self):
        r"""Gets the domain_address_name of this RuleAddressDtoForResponse.

        域名地址名称

        :return: The domain_address_name of this RuleAddressDtoForResponse.
        :rtype: str
        """
        return self._domain_address_name

    @domain_address_name.setter
    def domain_address_name(self, domain_address_name):
        r"""Sets the domain_address_name of this RuleAddressDtoForResponse.

        域名地址名称

        :param domain_address_name: The domain_address_name of this RuleAddressDtoForResponse.
        :type domain_address_name: str
        """
        self._domain_address_name = domain_address_name

    @property
    def region_list_json(self):
        r"""Gets the region_list_json of this RuleAddressDtoForResponse.

        规则地域列表json值

        :return: The region_list_json of this RuleAddressDtoForResponse.
        :rtype: str
        """
        return self._region_list_json

    @region_list_json.setter
    def region_list_json(self, region_list_json):
        r"""Sets the region_list_json of this RuleAddressDtoForResponse.

        规则地域列表json值

        :param region_list_json: The region_list_json of this RuleAddressDtoForResponse.
        :type region_list_json: str
        """
        self._region_list_json = region_list_json

    @property
    def region_list(self):
        r"""Gets the region_list of this RuleAddressDtoForResponse.

        规则地域列表

        :return: The region_list of this RuleAddressDtoForResponse.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.IpRegionDto`]
        """
        return self._region_list

    @region_list.setter
    def region_list(self, region_list):
        r"""Sets the region_list of this RuleAddressDtoForResponse.

        规则地域列表

        :param region_list: The region_list of this RuleAddressDtoForResponse.
        :type region_list: list[:class:`huaweicloudsdkcfw.v1.IpRegionDto`]
        """
        self._region_list = region_list

    @property
    def domain_set_id(self):
        r"""Gets the domain_set_id of this RuleAddressDtoForResponse.

        域名组id

        :return: The domain_set_id of this RuleAddressDtoForResponse.
        :rtype: str
        """
        return self._domain_set_id

    @domain_set_id.setter
    def domain_set_id(self, domain_set_id):
        r"""Sets the domain_set_id of this RuleAddressDtoForResponse.

        域名组id

        :param domain_set_id: The domain_set_id of this RuleAddressDtoForResponse.
        :type domain_set_id: str
        """
        self._domain_set_id = domain_set_id

    @property
    def domain_set_name(self):
        r"""Gets the domain_set_name of this RuleAddressDtoForResponse.

        域名组名称

        :return: The domain_set_name of this RuleAddressDtoForResponse.
        :rtype: str
        """
        return self._domain_set_name

    @domain_set_name.setter
    def domain_set_name(self, domain_set_name):
        r"""Sets the domain_set_name of this RuleAddressDtoForResponse.

        域名组名称

        :param domain_set_name: The domain_set_name of this RuleAddressDtoForResponse.
        :type domain_set_name: str
        """
        self._domain_set_name = domain_set_name

    @property
    def ip_address(self):
        r"""Gets the ip_address of this RuleAddressDtoForResponse.

        IP地址列表

        :return: The ip_address of this RuleAddressDtoForResponse.
        :rtype: list[str]
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this RuleAddressDtoForResponse.

        IP地址列表

        :param ip_address: The ip_address of this RuleAddressDtoForResponse.
        :type ip_address: list[str]
        """
        self._ip_address = ip_address

    @property
    def address_group(self):
        r"""Gets the address_group of this RuleAddressDtoForResponse.

        地址组id列表

        :return: The address_group of this RuleAddressDtoForResponse.
        :rtype: list[str]
        """
        return self._address_group

    @address_group.setter
    def address_group(self, address_group):
        r"""Sets the address_group of this RuleAddressDtoForResponse.

        地址组id列表

        :param address_group: The address_group of this RuleAddressDtoForResponse.
        :type address_group: list[str]
        """
        self._address_group = address_group

    @property
    def address_group_names(self):
        r"""Gets the address_group_names of this RuleAddressDtoForResponse.

        地址组名称列表

        :return: The address_group_names of this RuleAddressDtoForResponse.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AddressGroupVO`]
        """
        return self._address_group_names

    @address_group_names.setter
    def address_group_names(self, address_group_names):
        r"""Sets the address_group_names of this RuleAddressDtoForResponse.

        地址组名称列表

        :param address_group_names: The address_group_names of this RuleAddressDtoForResponse.
        :type address_group_names: list[:class:`huaweicloudsdkcfw.v1.AddressGroupVO`]
        """
        self._address_group_names = address_group_names

    @property
    def address_set_type(self):
        r"""Gets the address_set_type of this RuleAddressDtoForResponse.

        地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组

        :return: The address_set_type of this RuleAddressDtoForResponse.
        :rtype: int
        """
        return self._address_set_type

    @address_set_type.setter
    def address_set_type(self, address_set_type):
        r"""Sets the address_set_type of this RuleAddressDtoForResponse.

        地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组

        :param address_set_type: The address_set_type of this RuleAddressDtoForResponse.
        :type address_set_type: int
        """
        self._address_set_type = address_set_type

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
        if not isinstance(other, RuleAddressDtoForResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
