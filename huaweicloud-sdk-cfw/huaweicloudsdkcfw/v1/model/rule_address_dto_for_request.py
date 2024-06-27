# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleAddressDtoForRequest:

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
        'address_set_type': 'int',
        'predefined_group': 'list[str]',
        'address_group': 'list[str]'
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
        'address_set_type': 'address_set_type',
        'predefined_group': 'predefined_group',
        'address_group': 'address_group'
    }

    def __init__(self, type=None, address_type=None, address=None, address_set_id=None, address_set_name=None, domain_address_name=None, region_list_json=None, region_list=None, domain_set_id=None, domain_set_name=None, ip_address=None, address_set_type=None, predefined_group=None, address_group=None):
        """RuleAddressDtoForRequest

        The model defined in huaweicloud sdk

        :param type: 源类型0手工输入,1关联IP地址组,2域名，3地理位置，4域名组，5多对象，6域名组-DNS解析，7域名组-URL过滤。
        :type type: int
        :param address_type: 源类型0 ipv4,1 ipv6
        :type address_type: int
        :param address: 源IP，手动类型不能为空，自动及domain类型为空
        :type address: str
        :param address_set_id: 关联IP地址组ID，自动类型不能为空，手动类型合domain类型为空
        :type address_set_id: str
        :param address_set_name: 地址组名称
        :type address_set_name: str
        :param domain_address_name: 域名地址名称，域名类型时不能为空，手动类型及自动类型时为空
        :type domain_address_name: str
        :param region_list_json: 规则region列表json值
        :type region_list_json: str
        :param region_list: 规则region列表
        :type region_list: list[:class:`huaweicloudsdkcfw.v1.IpRegionDto`]
        :param domain_set_id: 域名组id
        :type domain_set_id: str
        :param domain_set_name: 域名组名称
        :type domain_set_name: str
        :param ip_address: IP地址列表
        :type ip_address: list[str]
        :param address_set_type: 地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组
        :type address_set_type: int
        :param predefined_group: 预定义地址组列表
        :type predefined_group: list[str]
        :param address_group: 地址组列表
        :type address_group: list[str]
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
        self._address_set_type = None
        self._predefined_group = None
        self._address_group = None
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
        if address_set_type is not None:
            self.address_set_type = address_set_type
        if predefined_group is not None:
            self.predefined_group = predefined_group
        if address_group is not None:
            self.address_group = address_group

    @property
    def type(self):
        """Gets the type of this RuleAddressDtoForRequest.

        源类型0手工输入,1关联IP地址组,2域名，3地理位置，4域名组，5多对象，6域名组-DNS解析，7域名组-URL过滤。

        :return: The type of this RuleAddressDtoForRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleAddressDtoForRequest.

        源类型0手工输入,1关联IP地址组,2域名，3地理位置，4域名组，5多对象，6域名组-DNS解析，7域名组-URL过滤。

        :param type: The type of this RuleAddressDtoForRequest.
        :type type: int
        """
        self._type = type

    @property
    def address_type(self):
        """Gets the address_type of this RuleAddressDtoForRequest.

        源类型0 ipv4,1 ipv6

        :return: The address_type of this RuleAddressDtoForRequest.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this RuleAddressDtoForRequest.

        源类型0 ipv4,1 ipv6

        :param address_type: The address_type of this RuleAddressDtoForRequest.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def address(self):
        """Gets the address of this RuleAddressDtoForRequest.

        源IP，手动类型不能为空，自动及domain类型为空

        :return: The address of this RuleAddressDtoForRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RuleAddressDtoForRequest.

        源IP，手动类型不能为空，自动及domain类型为空

        :param address: The address of this RuleAddressDtoForRequest.
        :type address: str
        """
        self._address = address

    @property
    def address_set_id(self):
        """Gets the address_set_id of this RuleAddressDtoForRequest.

        关联IP地址组ID，自动类型不能为空，手动类型合domain类型为空

        :return: The address_set_id of this RuleAddressDtoForRequest.
        :rtype: str
        """
        return self._address_set_id

    @address_set_id.setter
    def address_set_id(self, address_set_id):
        """Sets the address_set_id of this RuleAddressDtoForRequest.

        关联IP地址组ID，自动类型不能为空，手动类型合domain类型为空

        :param address_set_id: The address_set_id of this RuleAddressDtoForRequest.
        :type address_set_id: str
        """
        self._address_set_id = address_set_id

    @property
    def address_set_name(self):
        """Gets the address_set_name of this RuleAddressDtoForRequest.

        地址组名称

        :return: The address_set_name of this RuleAddressDtoForRequest.
        :rtype: str
        """
        return self._address_set_name

    @address_set_name.setter
    def address_set_name(self, address_set_name):
        """Sets the address_set_name of this RuleAddressDtoForRequest.

        地址组名称

        :param address_set_name: The address_set_name of this RuleAddressDtoForRequest.
        :type address_set_name: str
        """
        self._address_set_name = address_set_name

    @property
    def domain_address_name(self):
        """Gets the domain_address_name of this RuleAddressDtoForRequest.

        域名地址名称，域名类型时不能为空，手动类型及自动类型时为空

        :return: The domain_address_name of this RuleAddressDtoForRequest.
        :rtype: str
        """
        return self._domain_address_name

    @domain_address_name.setter
    def domain_address_name(self, domain_address_name):
        """Sets the domain_address_name of this RuleAddressDtoForRequest.

        域名地址名称，域名类型时不能为空，手动类型及自动类型时为空

        :param domain_address_name: The domain_address_name of this RuleAddressDtoForRequest.
        :type domain_address_name: str
        """
        self._domain_address_name = domain_address_name

    @property
    def region_list_json(self):
        """Gets the region_list_json of this RuleAddressDtoForRequest.

        规则region列表json值

        :return: The region_list_json of this RuleAddressDtoForRequest.
        :rtype: str
        """
        return self._region_list_json

    @region_list_json.setter
    def region_list_json(self, region_list_json):
        """Sets the region_list_json of this RuleAddressDtoForRequest.

        规则region列表json值

        :param region_list_json: The region_list_json of this RuleAddressDtoForRequest.
        :type region_list_json: str
        """
        self._region_list_json = region_list_json

    @property
    def region_list(self):
        """Gets the region_list of this RuleAddressDtoForRequest.

        规则region列表

        :return: The region_list of this RuleAddressDtoForRequest.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.IpRegionDto`]
        """
        return self._region_list

    @region_list.setter
    def region_list(self, region_list):
        """Sets the region_list of this RuleAddressDtoForRequest.

        规则region列表

        :param region_list: The region_list of this RuleAddressDtoForRequest.
        :type region_list: list[:class:`huaweicloudsdkcfw.v1.IpRegionDto`]
        """
        self._region_list = region_list

    @property
    def domain_set_id(self):
        """Gets the domain_set_id of this RuleAddressDtoForRequest.

        域名组id

        :return: The domain_set_id of this RuleAddressDtoForRequest.
        :rtype: str
        """
        return self._domain_set_id

    @domain_set_id.setter
    def domain_set_id(self, domain_set_id):
        """Sets the domain_set_id of this RuleAddressDtoForRequest.

        域名组id

        :param domain_set_id: The domain_set_id of this RuleAddressDtoForRequest.
        :type domain_set_id: str
        """
        self._domain_set_id = domain_set_id

    @property
    def domain_set_name(self):
        """Gets the domain_set_name of this RuleAddressDtoForRequest.

        域名组名称

        :return: The domain_set_name of this RuleAddressDtoForRequest.
        :rtype: str
        """
        return self._domain_set_name

    @domain_set_name.setter
    def domain_set_name(self, domain_set_name):
        """Sets the domain_set_name of this RuleAddressDtoForRequest.

        域名组名称

        :param domain_set_name: The domain_set_name of this RuleAddressDtoForRequest.
        :type domain_set_name: str
        """
        self._domain_set_name = domain_set_name

    @property
    def ip_address(self):
        """Gets the ip_address of this RuleAddressDtoForRequest.

        IP地址列表

        :return: The ip_address of this RuleAddressDtoForRequest.
        :rtype: list[str]
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this RuleAddressDtoForRequest.

        IP地址列表

        :param ip_address: The ip_address of this RuleAddressDtoForRequest.
        :type ip_address: list[str]
        """
        self._ip_address = ip_address

    @property
    def address_set_type(self):
        """Gets the address_set_type of this RuleAddressDtoForRequest.

        地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组

        :return: The address_set_type of this RuleAddressDtoForRequest.
        :rtype: int
        """
        return self._address_set_type

    @address_set_type.setter
    def address_set_type(self, address_set_type):
        """Sets the address_set_type of this RuleAddressDtoForRequest.

        地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组

        :param address_set_type: The address_set_type of this RuleAddressDtoForRequest.
        :type address_set_type: int
        """
        self._address_set_type = address_set_type

    @property
    def predefined_group(self):
        """Gets the predefined_group of this RuleAddressDtoForRequest.

        预定义地址组列表

        :return: The predefined_group of this RuleAddressDtoForRequest.
        :rtype: list[str]
        """
        return self._predefined_group

    @predefined_group.setter
    def predefined_group(self, predefined_group):
        """Sets the predefined_group of this RuleAddressDtoForRequest.

        预定义地址组列表

        :param predefined_group: The predefined_group of this RuleAddressDtoForRequest.
        :type predefined_group: list[str]
        """
        self._predefined_group = predefined_group

    @property
    def address_group(self):
        """Gets the address_group of this RuleAddressDtoForRequest.

        地址组列表

        :return: The address_group of this RuleAddressDtoForRequest.
        :rtype: list[str]
        """
        return self._address_group

    @address_group.setter
    def address_group(self, address_group):
        """Sets the address_group of this RuleAddressDtoForRequest.

        地址组列表

        :param address_group: The address_group of this RuleAddressDtoForRequest.
        :type address_group: list[str]
        """
        self._address_group = address_group

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
        if not isinstance(other, RuleAddressDtoForRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
