# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DnsConfigResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vip_address': 'str',
        'ipv6_vip_address': 'str',
        'eips': 'list[EipInfo]',
        'global_eips': 'list[GlobalEipInfo]',
        'public_domain_name_enable': 'bool',
        'public_dns_zone_name': 'str',
        'public_dns_zone_id': 'str',
        'public_domain_name': 'str',
        'public_dns_record_set_ttl': 'int',
        'private_domain_name_enable': 'bool',
        'private_dns_zone_name': 'str',
        'private_dns_zone_id': 'str',
        'private_domain_name': 'str',
        'private_dns_zone_type': 'str',
        'private_dns_record_set_ttl': 'int'
    }

    attribute_map = {
        'vip_address': 'vip_address',
        'ipv6_vip_address': 'ipv6_vip_address',
        'eips': 'eips',
        'global_eips': 'global_eips',
        'public_domain_name_enable': 'public_domain_name_enable',
        'public_dns_zone_name': 'public_dns_zone_name',
        'public_dns_zone_id': 'public_dns_zone_id',
        'public_domain_name': 'public_domain_name',
        'public_dns_record_set_ttl': 'public_dns_record_set_ttl',
        'private_domain_name_enable': 'private_domain_name_enable',
        'private_dns_zone_name': 'private_dns_zone_name',
        'private_dns_zone_id': 'private_dns_zone_id',
        'private_domain_name': 'private_domain_name',
        'private_dns_zone_type': 'private_dns_zone_type',
        'private_dns_record_set_ttl': 'private_dns_record_set_ttl'
    }

    def __init__(self, vip_address=None, ipv6_vip_address=None, eips=None, global_eips=None, public_domain_name_enable=None, public_dns_zone_name=None, public_dns_zone_id=None, public_domain_name=None, public_dns_record_set_ttl=None, private_domain_name_enable=None, private_dns_zone_name=None, private_dns_zone_id=None, private_domain_name=None, private_dns_zone_type=None, private_dns_record_set_ttl=None):
        r"""DnsConfigResponseBody

        The model defined in huaweicloud sdk

        :param vip_address: **参数解释**：负载均衡器的IPv4虚拟IP地址。
        :type vip_address: str
        :param ipv6_vip_address: **参数解释**：双栈类型负载均衡器的IPv6地址。  **约束限制**：[不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_address: str
        :param eips: **参数解释**：负载均衡器绑定的EIP。  注：该字段与publicips一致。
        :type eips: list[:class:`huaweicloudsdkelb.v3.EipInfo`]
        :param global_eips: **参数解释**：负载均衡器绑定的GEIP。
        :type global_eips: list[:class:`huaweicloudsdkelb.v3.GlobalEipInfo`]
        :param public_domain_name_enable: **参数解释**：是否配置公网域名。 **取值范围**：   true：开启公网域名   false：关闭公网域名
        :type public_domain_name_enable: bool
        :param public_dns_zone_name: **参数解释**：公网域名所使用的zone名称。 **约束限制**：   公网域名只能使用公网类型的zone。   当配置公网域名开关打开时，该字段不能置空。   所填的公网zone必须在云解析服务已注册过。
        :type public_dns_zone_name: str
        :param public_dns_zone_id: **参数解释**：   公网域名所使用的zone对应的id。   根据传入的公网zone 名称查询得出。
        :type public_dns_zone_id: str
        :param public_domain_name: **参数解释**：   负载均衡实例的公网域名。 **约束限制**：   根据负载均衡实例id，局点id和zone信息以如下格式生成：   {lb_id}.elb.{region_id}.{zone_name}
        :type public_domain_name: str
        :param public_dns_record_set_ttl: 参数解释:   公网解析记录集超时时间。   解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。   如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些。 **取值范围**：   1-2147483647 **默认取值**：   300
        :type public_dns_record_set_ttl: int
        :param private_domain_name_enable: **参数解释**：   是否配置私网域名。 **取值范围**：   true：开启私网域名   false：关闭私网域名
        :type private_domain_name_enable: bool
        :param private_dns_zone_name: **参数解释**：   私网域名所使用的zone的名称。 **约束限制**：   私网域名既能使用公网zone，也能使用私网zone，zone的类型在private_dns_zone_type字段中指定。   当配置私网域名开关打开时，该字段不能置空。   所填的私网zone必须在云解析服务已注册过。
        :type private_dns_zone_name: str
        :param private_dns_zone_id: **参数解释**：   私网域名所使用的zone对应的id。 **约束限制**：   根据传入的私网zone 名称查询得出。
        :type private_dns_zone_id: str
        :param private_domain_name: **参数解释**：负载均衡实例的私网域名。 **约束限制**：   根据负载均衡实例id，局点id和zone信息以如下格式生成：   {lb_id}-internal.elb.{region_id}.{zone_name}
        :type private_domain_name: str
        :param private_dns_zone_type: **参数解释**：私网域名所使用的zone的类型。 **约束限制**：不涉及 **取值范围**：private public **默认取值**：private
        :type private_dns_zone_type: str
        :param private_dns_record_set_ttl: **参数解释**：   私网解析记录集超时时间。   解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。   如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些。 **取值范围**：   1-2147483647 **默认取值**：   300
        :type private_dns_record_set_ttl: int
        """
        
        

        self._vip_address = None
        self._ipv6_vip_address = None
        self._eips = None
        self._global_eips = None
        self._public_domain_name_enable = None
        self._public_dns_zone_name = None
        self._public_dns_zone_id = None
        self._public_domain_name = None
        self._public_dns_record_set_ttl = None
        self._private_domain_name_enable = None
        self._private_dns_zone_name = None
        self._private_dns_zone_id = None
        self._private_domain_name = None
        self._private_dns_zone_type = None
        self._private_dns_record_set_ttl = None
        self.discriminator = None

        if vip_address is not None:
            self.vip_address = vip_address
        if ipv6_vip_address is not None:
            self.ipv6_vip_address = ipv6_vip_address
        if eips is not None:
            self.eips = eips
        if global_eips is not None:
            self.global_eips = global_eips
        if public_domain_name_enable is not None:
            self.public_domain_name_enable = public_domain_name_enable
        if public_dns_zone_name is not None:
            self.public_dns_zone_name = public_dns_zone_name
        if public_dns_zone_id is not None:
            self.public_dns_zone_id = public_dns_zone_id
        if public_domain_name is not None:
            self.public_domain_name = public_domain_name
        if public_dns_record_set_ttl is not None:
            self.public_dns_record_set_ttl = public_dns_record_set_ttl
        if private_domain_name_enable is not None:
            self.private_domain_name_enable = private_domain_name_enable
        if private_dns_zone_name is not None:
            self.private_dns_zone_name = private_dns_zone_name
        if private_dns_zone_id is not None:
            self.private_dns_zone_id = private_dns_zone_id
        if private_domain_name is not None:
            self.private_domain_name = private_domain_name
        if private_dns_zone_type is not None:
            self.private_dns_zone_type = private_dns_zone_type
        if private_dns_record_set_ttl is not None:
            self.private_dns_record_set_ttl = private_dns_record_set_ttl

    @property
    def vip_address(self):
        r"""Gets the vip_address of this DnsConfigResponseBody.

        **参数解释**：负载均衡器的IPv4虚拟IP地址。

        :return: The vip_address of this DnsConfigResponseBody.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this DnsConfigResponseBody.

        **参数解释**：负载均衡器的IPv4虚拟IP地址。

        :param vip_address: The vip_address of this DnsConfigResponseBody.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def ipv6_vip_address(self):
        r"""Gets the ipv6_vip_address of this DnsConfigResponseBody.

        **参数解释**：双栈类型负载均衡器的IPv6地址。  **约束限制**：[不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_address of this DnsConfigResponseBody.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        r"""Sets the ipv6_vip_address of this DnsConfigResponseBody.

        **参数解释**：双栈类型负载均衡器的IPv6地址。  **约束限制**：[不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_address: The ipv6_vip_address of this DnsConfigResponseBody.
        :type ipv6_vip_address: str
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def eips(self):
        r"""Gets the eips of this DnsConfigResponseBody.

        **参数解释**：负载均衡器绑定的EIP。  注：该字段与publicips一致。

        :return: The eips of this DnsConfigResponseBody.
        :rtype: list[:class:`huaweicloudsdkelb.v3.EipInfo`]
        """
        return self._eips

    @eips.setter
    def eips(self, eips):
        r"""Sets the eips of this DnsConfigResponseBody.

        **参数解释**：负载均衡器绑定的EIP。  注：该字段与publicips一致。

        :param eips: The eips of this DnsConfigResponseBody.
        :type eips: list[:class:`huaweicloudsdkelb.v3.EipInfo`]
        """
        self._eips = eips

    @property
    def global_eips(self):
        r"""Gets the global_eips of this DnsConfigResponseBody.

        **参数解释**：负载均衡器绑定的GEIP。

        :return: The global_eips of this DnsConfigResponseBody.
        :rtype: list[:class:`huaweicloudsdkelb.v3.GlobalEipInfo`]
        """
        return self._global_eips

    @global_eips.setter
    def global_eips(self, global_eips):
        r"""Sets the global_eips of this DnsConfigResponseBody.

        **参数解释**：负载均衡器绑定的GEIP。

        :param global_eips: The global_eips of this DnsConfigResponseBody.
        :type global_eips: list[:class:`huaweicloudsdkelb.v3.GlobalEipInfo`]
        """
        self._global_eips = global_eips

    @property
    def public_domain_name_enable(self):
        r"""Gets the public_domain_name_enable of this DnsConfigResponseBody.

        **参数解释**：是否配置公网域名。 **取值范围**：   true：开启公网域名   false：关闭公网域名

        :return: The public_domain_name_enable of this DnsConfigResponseBody.
        :rtype: bool
        """
        return self._public_domain_name_enable

    @public_domain_name_enable.setter
    def public_domain_name_enable(self, public_domain_name_enable):
        r"""Sets the public_domain_name_enable of this DnsConfigResponseBody.

        **参数解释**：是否配置公网域名。 **取值范围**：   true：开启公网域名   false：关闭公网域名

        :param public_domain_name_enable: The public_domain_name_enable of this DnsConfigResponseBody.
        :type public_domain_name_enable: bool
        """
        self._public_domain_name_enable = public_domain_name_enable

    @property
    def public_dns_zone_name(self):
        r"""Gets the public_dns_zone_name of this DnsConfigResponseBody.

        **参数解释**：公网域名所使用的zone名称。 **约束限制**：   公网域名只能使用公网类型的zone。   当配置公网域名开关打开时，该字段不能置空。   所填的公网zone必须在云解析服务已注册过。

        :return: The public_dns_zone_name of this DnsConfigResponseBody.
        :rtype: str
        """
        return self._public_dns_zone_name

    @public_dns_zone_name.setter
    def public_dns_zone_name(self, public_dns_zone_name):
        r"""Sets the public_dns_zone_name of this DnsConfigResponseBody.

        **参数解释**：公网域名所使用的zone名称。 **约束限制**：   公网域名只能使用公网类型的zone。   当配置公网域名开关打开时，该字段不能置空。   所填的公网zone必须在云解析服务已注册过。

        :param public_dns_zone_name: The public_dns_zone_name of this DnsConfigResponseBody.
        :type public_dns_zone_name: str
        """
        self._public_dns_zone_name = public_dns_zone_name

    @property
    def public_dns_zone_id(self):
        r"""Gets the public_dns_zone_id of this DnsConfigResponseBody.

        **参数解释**：   公网域名所使用的zone对应的id。   根据传入的公网zone 名称查询得出。

        :return: The public_dns_zone_id of this DnsConfigResponseBody.
        :rtype: str
        """
        return self._public_dns_zone_id

    @public_dns_zone_id.setter
    def public_dns_zone_id(self, public_dns_zone_id):
        r"""Sets the public_dns_zone_id of this DnsConfigResponseBody.

        **参数解释**：   公网域名所使用的zone对应的id。   根据传入的公网zone 名称查询得出。

        :param public_dns_zone_id: The public_dns_zone_id of this DnsConfigResponseBody.
        :type public_dns_zone_id: str
        """
        self._public_dns_zone_id = public_dns_zone_id

    @property
    def public_domain_name(self):
        r"""Gets the public_domain_name of this DnsConfigResponseBody.

        **参数解释**：   负载均衡实例的公网域名。 **约束限制**：   根据负载均衡实例id，局点id和zone信息以如下格式生成：   {lb_id}.elb.{region_id}.{zone_name}

        :return: The public_domain_name of this DnsConfigResponseBody.
        :rtype: str
        """
        return self._public_domain_name

    @public_domain_name.setter
    def public_domain_name(self, public_domain_name):
        r"""Sets the public_domain_name of this DnsConfigResponseBody.

        **参数解释**：   负载均衡实例的公网域名。 **约束限制**：   根据负载均衡实例id，局点id和zone信息以如下格式生成：   {lb_id}.elb.{region_id}.{zone_name}

        :param public_domain_name: The public_domain_name of this DnsConfigResponseBody.
        :type public_domain_name: str
        """
        self._public_domain_name = public_domain_name

    @property
    def public_dns_record_set_ttl(self):
        r"""Gets the public_dns_record_set_ttl of this DnsConfigResponseBody.

        参数解释:   公网解析记录集超时时间。   解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。   如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些。 **取值范围**：   1-2147483647 **默认取值**：   300

        :return: The public_dns_record_set_ttl of this DnsConfigResponseBody.
        :rtype: int
        """
        return self._public_dns_record_set_ttl

    @public_dns_record_set_ttl.setter
    def public_dns_record_set_ttl(self, public_dns_record_set_ttl):
        r"""Sets the public_dns_record_set_ttl of this DnsConfigResponseBody.

        参数解释:   公网解析记录集超时时间。   解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。   如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些。 **取值范围**：   1-2147483647 **默认取值**：   300

        :param public_dns_record_set_ttl: The public_dns_record_set_ttl of this DnsConfigResponseBody.
        :type public_dns_record_set_ttl: int
        """
        self._public_dns_record_set_ttl = public_dns_record_set_ttl

    @property
    def private_domain_name_enable(self):
        r"""Gets the private_domain_name_enable of this DnsConfigResponseBody.

        **参数解释**：   是否配置私网域名。 **取值范围**：   true：开启私网域名   false：关闭私网域名

        :return: The private_domain_name_enable of this DnsConfigResponseBody.
        :rtype: bool
        """
        return self._private_domain_name_enable

    @private_domain_name_enable.setter
    def private_domain_name_enable(self, private_domain_name_enable):
        r"""Sets the private_domain_name_enable of this DnsConfigResponseBody.

        **参数解释**：   是否配置私网域名。 **取值范围**：   true：开启私网域名   false：关闭私网域名

        :param private_domain_name_enable: The private_domain_name_enable of this DnsConfigResponseBody.
        :type private_domain_name_enable: bool
        """
        self._private_domain_name_enable = private_domain_name_enable

    @property
    def private_dns_zone_name(self):
        r"""Gets the private_dns_zone_name of this DnsConfigResponseBody.

        **参数解释**：   私网域名所使用的zone的名称。 **约束限制**：   私网域名既能使用公网zone，也能使用私网zone，zone的类型在private_dns_zone_type字段中指定。   当配置私网域名开关打开时，该字段不能置空。   所填的私网zone必须在云解析服务已注册过。

        :return: The private_dns_zone_name of this DnsConfigResponseBody.
        :rtype: str
        """
        return self._private_dns_zone_name

    @private_dns_zone_name.setter
    def private_dns_zone_name(self, private_dns_zone_name):
        r"""Sets the private_dns_zone_name of this DnsConfigResponseBody.

        **参数解释**：   私网域名所使用的zone的名称。 **约束限制**：   私网域名既能使用公网zone，也能使用私网zone，zone的类型在private_dns_zone_type字段中指定。   当配置私网域名开关打开时，该字段不能置空。   所填的私网zone必须在云解析服务已注册过。

        :param private_dns_zone_name: The private_dns_zone_name of this DnsConfigResponseBody.
        :type private_dns_zone_name: str
        """
        self._private_dns_zone_name = private_dns_zone_name

    @property
    def private_dns_zone_id(self):
        r"""Gets the private_dns_zone_id of this DnsConfigResponseBody.

        **参数解释**：   私网域名所使用的zone对应的id。 **约束限制**：   根据传入的私网zone 名称查询得出。

        :return: The private_dns_zone_id of this DnsConfigResponseBody.
        :rtype: str
        """
        return self._private_dns_zone_id

    @private_dns_zone_id.setter
    def private_dns_zone_id(self, private_dns_zone_id):
        r"""Sets the private_dns_zone_id of this DnsConfigResponseBody.

        **参数解释**：   私网域名所使用的zone对应的id。 **约束限制**：   根据传入的私网zone 名称查询得出。

        :param private_dns_zone_id: The private_dns_zone_id of this DnsConfigResponseBody.
        :type private_dns_zone_id: str
        """
        self._private_dns_zone_id = private_dns_zone_id

    @property
    def private_domain_name(self):
        r"""Gets the private_domain_name of this DnsConfigResponseBody.

        **参数解释**：负载均衡实例的私网域名。 **约束限制**：   根据负载均衡实例id，局点id和zone信息以如下格式生成：   {lb_id}-internal.elb.{region_id}.{zone_name}

        :return: The private_domain_name of this DnsConfigResponseBody.
        :rtype: str
        """
        return self._private_domain_name

    @private_domain_name.setter
    def private_domain_name(self, private_domain_name):
        r"""Sets the private_domain_name of this DnsConfigResponseBody.

        **参数解释**：负载均衡实例的私网域名。 **约束限制**：   根据负载均衡实例id，局点id和zone信息以如下格式生成：   {lb_id}-internal.elb.{region_id}.{zone_name}

        :param private_domain_name: The private_domain_name of this DnsConfigResponseBody.
        :type private_domain_name: str
        """
        self._private_domain_name = private_domain_name

    @property
    def private_dns_zone_type(self):
        r"""Gets the private_dns_zone_type of this DnsConfigResponseBody.

        **参数解释**：私网域名所使用的zone的类型。 **约束限制**：不涉及 **取值范围**：private public **默认取值**：private

        :return: The private_dns_zone_type of this DnsConfigResponseBody.
        :rtype: str
        """
        return self._private_dns_zone_type

    @private_dns_zone_type.setter
    def private_dns_zone_type(self, private_dns_zone_type):
        r"""Sets the private_dns_zone_type of this DnsConfigResponseBody.

        **参数解释**：私网域名所使用的zone的类型。 **约束限制**：不涉及 **取值范围**：private public **默认取值**：private

        :param private_dns_zone_type: The private_dns_zone_type of this DnsConfigResponseBody.
        :type private_dns_zone_type: str
        """
        self._private_dns_zone_type = private_dns_zone_type

    @property
    def private_dns_record_set_ttl(self):
        r"""Gets the private_dns_record_set_ttl of this DnsConfigResponseBody.

        **参数解释**：   私网解析记录集超时时间。   解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。   如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些。 **取值范围**：   1-2147483647 **默认取值**：   300

        :return: The private_dns_record_set_ttl of this DnsConfigResponseBody.
        :rtype: int
        """
        return self._private_dns_record_set_ttl

    @private_dns_record_set_ttl.setter
    def private_dns_record_set_ttl(self, private_dns_record_set_ttl):
        r"""Sets the private_dns_record_set_ttl of this DnsConfigResponseBody.

        **参数解释**：   私网解析记录集超时时间。   解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。   如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些。 **取值范围**：   1-2147483647 **默认取值**：   300

        :param private_dns_record_set_ttl: The private_dns_record_set_ttl of this DnsConfigResponseBody.
        :type private_dns_record_set_ttl: int
        """
        self._private_dns_record_set_ttl = private_dns_record_set_ttl

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
        if not isinstance(other, DnsConfigResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
