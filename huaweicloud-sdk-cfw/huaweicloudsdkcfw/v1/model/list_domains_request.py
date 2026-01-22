# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_set_id': 'str',
        'enterprise_project_id': 'str',
        'fw_instance_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'domain_name': 'str',
        'object_id': 'str'
    }

    attribute_map = {
        'domain_set_id': 'domain_set_id',
        'enterprise_project_id': 'enterprise_project_id',
        'fw_instance_id': 'fw_instance_id',
        'limit': 'limit',
        'offset': 'offset',
        'domain_name': 'domain_name',
        'object_id': 'object_Id'
    }

    def __init__(self, domain_set_id=None, enterprise_project_id=None, fw_instance_id=None, limit=None, offset=None, domain_name=None, object_id=None):
        r"""ListDomainsRequest

        The model defined in huaweicloud sdk

        :param domain_set_id: **参数解释**： 域名组id，可通过[查询域名组列表接口](ListDomainSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type domain_set_id: str
        :param enterprise_project_id: **参数解释**： 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，配置后可根据企业项目过滤不同企业项目下的资产，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 0
        :type enterprise_project_id: str
        :param fw_instance_id: **参数解释**： 防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type fw_instance_id: str
        :param limit: **参数解释**： 每页显示个数 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及
        :type limit: int
        :param offset: **参数解释**： 偏移量：指定返回记录的开始位置 **约束限制**： 不涉及 **取值范围**： 大于或等于0 **默认取值**： 0
        :type offset: int
        :param domain_name: **参数解释**： 域名名称 **约束限制**： 域名格式，如www.example.com **取值范围**： 不涉及 **默认取值**： 不涉及
        :type domain_name: str
        :param object_id: **参数解释**： 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type object_id: str
        """
        
        

        self._domain_set_id = None
        self._enterprise_project_id = None
        self._fw_instance_id = None
        self._limit = None
        self._offset = None
        self._domain_name = None
        self._object_id = None
        self.discriminator = None

        self.domain_set_id = domain_set_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.fw_instance_id = fw_instance_id
        self.limit = limit
        self.offset = offset
        if domain_name is not None:
            self.domain_name = domain_name
        if object_id is not None:
            self.object_id = object_id

    @property
    def domain_set_id(self):
        r"""Gets the domain_set_id of this ListDomainsRequest.

        **参数解释**： 域名组id，可通过[查询域名组列表接口](ListDomainSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The domain_set_id of this ListDomainsRequest.
        :rtype: str
        """
        return self._domain_set_id

    @domain_set_id.setter
    def domain_set_id(self, domain_set_id):
        r"""Sets the domain_set_id of this ListDomainsRequest.

        **参数解释**： 域名组id，可通过[查询域名组列表接口](ListDomainSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param domain_set_id: The domain_set_id of this ListDomainsRequest.
        :type domain_set_id: str
        """
        self._domain_set_id = domain_set_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListDomainsRequest.

        **参数解释**： 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，配置后可根据企业项目过滤不同企业项目下的资产，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 0

        :return: The enterprise_project_id of this ListDomainsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListDomainsRequest.

        **参数解释**： 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，配置后可根据企业项目过滤不同企业项目下的资产，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 0

        :param enterprise_project_id: The enterprise_project_id of this ListDomainsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListDomainsRequest.

        **参数解释**： 防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The fw_instance_id of this ListDomainsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListDomainsRequest.

        **参数解释**： 防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this ListDomainsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ListDomainsRequest.

        **参数解释**： 每页显示个数 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及

        :return: The limit of this ListDomainsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDomainsRequest.

        **参数解释**： 每页显示个数 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及

        :param limit: The limit of this ListDomainsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListDomainsRequest.

        **参数解释**： 偏移量：指定返回记录的开始位置 **约束限制**： 不涉及 **取值范围**： 大于或等于0 **默认取值**： 0

        :return: The offset of this ListDomainsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDomainsRequest.

        **参数解释**： 偏移量：指定返回记录的开始位置 **约束限制**： 不涉及 **取值范围**： 大于或等于0 **默认取值**： 0

        :param offset: The offset of this ListDomainsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListDomainsRequest.

        **参数解释**： 域名名称 **约束限制**： 域名格式，如www.example.com **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The domain_name of this ListDomainsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListDomainsRequest.

        **参数解释**： 域名名称 **约束限制**： 域名格式，如www.example.com **取值范围**： 不涉及 **默认取值**： 不涉及

        :param domain_name: The domain_name of this ListDomainsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def object_id(self):
        r"""Gets the object_id of this ListDomainsRequest.

        **参数解释**： 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The object_id of this ListDomainsRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ListDomainsRequest.

        **参数解释**： 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param object_id: The object_id of this ListDomainsRequest.
        :type object_id: str
        """
        self._object_id = object_id

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
        if not isinstance(other, ListDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
