# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainAllResourceCountRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'resource_type': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'resource_type': 'resource_type',
        'region_id': 'region_id'
    }

    def __init__(self, domain_id=None, resource_type=None, region_id=None):
        r"""ShowDomainAllResourceCountRequest

        The model defined in huaweicloud sdk

        :param domain_id: **参数解释**： 账户ID。 通过调用IAM服务[查询IAM用户详情]接口获取 **约束限制**： 不涉及 **取值范围**： 以IAM服务[查询IAM用户详情]接口值为准。 **默认取值**： 不涉及 
        :type domain_id: str
        :param resource_type: **参数解释**：  资源类型 **约束限制**： 不涉及 **取值范围**：  - cloudservers: 审计  - dbEncrypt: 加密  - dbOm: 运维 **默认取值**： 不涉及 
        :type resource_type: str
        :param region_id: **参数解释**：  以当前region id为准 **约束限制**： 不涉及 **取值范围**： 以当前region id为准 **默认取值**： 以当前region id为准 
        :type region_id: str
        """
        
        

        self._domain_id = None
        self._resource_type = None
        self._region_id = None
        self.discriminator = None

        self.domain_id = domain_id
        self.resource_type = resource_type
        self.region_id = region_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowDomainAllResourceCountRequest.

        **参数解释**： 账户ID。 通过调用IAM服务[查询IAM用户详情]接口获取 **约束限制**： 不涉及 **取值范围**： 以IAM服务[查询IAM用户详情]接口值为准。 **默认取值**： 不涉及 

        :return: The domain_id of this ShowDomainAllResourceCountRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowDomainAllResourceCountRequest.

        **参数解释**： 账户ID。 通过调用IAM服务[查询IAM用户详情]接口获取 **约束限制**： 不涉及 **取值范围**： 以IAM服务[查询IAM用户详情]接口值为准。 **默认取值**： 不涉及 

        :param domain_id: The domain_id of this ShowDomainAllResourceCountRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowDomainAllResourceCountRequest.

        **参数解释**：  资源类型 **约束限制**： 不涉及 **取值范围**：  - cloudservers: 审计  - dbEncrypt: 加密  - dbOm: 运维 **默认取值**： 不涉及 

        :return: The resource_type of this ShowDomainAllResourceCountRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowDomainAllResourceCountRequest.

        **参数解释**：  资源类型 **约束限制**： 不涉及 **取值范围**：  - cloudservers: 审计  - dbEncrypt: 加密  - dbOm: 运维 **默认取值**： 不涉及 

        :param resource_type: The resource_type of this ShowDomainAllResourceCountRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowDomainAllResourceCountRequest.

        **参数解释**：  以当前region id为准 **约束限制**： 不涉及 **取值范围**： 以当前region id为准 **默认取值**： 以当前region id为准 

        :return: The region_id of this ShowDomainAllResourceCountRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowDomainAllResourceCountRequest.

        **参数解释**：  以当前region id为准 **约束限制**： 不涉及 **取值范围**： 以当前region id为准 **默认取值**： 以当前region id为准 

        :param region_id: The region_id of this ShowDomainAllResourceCountRequest.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, ShowDomainAllResourceCountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
