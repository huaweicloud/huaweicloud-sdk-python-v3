# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DuplicateDomainRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reference_domain_name': 'str',
        'domain_name': 'str'
    }

    attribute_map = {
        'reference_domain_name': 'reference_domain_name',
        'domain_name': 'domain_name'
    }

    def __init__(self, reference_domain_name=None, domain_name=None):
        r"""DuplicateDomainRequestBody

        The model defined in huaweicloud sdk

        :param reference_domain_name: **参数解释：** 存量加速域名，将该域名的配置复制给新添加的域名。  **约束限制：** 已经在CDN添加成功的域名。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type reference_domain_name: str
        :param domain_name: **参数解释：** 需要添加到CDN控制台加速的域名 &gt; 添加泛域名后，该泛域名所有次级域名均默认接入CDN加速。  **约束限制：** 加速域名不允许重复添加 **取值范围：** - 域名长度不能超过200个字符 - 支持大小写字母、数字、\&quot;-\&quot;、\&quot;.\&quot;，首尾字符不能是\&quot;-\&quot;或\&quot;.\&quot; - 泛域名场景下支持\&quot;*\&quot;，且\&quot;*必须为首字符 - 域名单节点长度不超过63个字符，即：***.***.com中，***的字符数不超过63个字符  **默认取值：** 不涉及
        :type domain_name: str
        """
        
        

        self._reference_domain_name = None
        self._domain_name = None
        self.discriminator = None

        self.reference_domain_name = reference_domain_name
        self.domain_name = domain_name

    @property
    def reference_domain_name(self):
        r"""Gets the reference_domain_name of this DuplicateDomainRequestBody.

        **参数解释：** 存量加速域名，将该域名的配置复制给新添加的域名。  **约束限制：** 已经在CDN添加成功的域名。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The reference_domain_name of this DuplicateDomainRequestBody.
        :rtype: str
        """
        return self._reference_domain_name

    @reference_domain_name.setter
    def reference_domain_name(self, reference_domain_name):
        r"""Sets the reference_domain_name of this DuplicateDomainRequestBody.

        **参数解释：** 存量加速域名，将该域名的配置复制给新添加的域名。  **约束限制：** 已经在CDN添加成功的域名。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param reference_domain_name: The reference_domain_name of this DuplicateDomainRequestBody.
        :type reference_domain_name: str
        """
        self._reference_domain_name = reference_domain_name

    @property
    def domain_name(self):
        r"""Gets the domain_name of this DuplicateDomainRequestBody.

        **参数解释：** 需要添加到CDN控制台加速的域名 > 添加泛域名后，该泛域名所有次级域名均默认接入CDN加速。  **约束限制：** 加速域名不允许重复添加 **取值范围：** - 域名长度不能超过200个字符 - 支持大小写字母、数字、\"-\"、\".\"，首尾字符不能是\"-\"或\".\" - 泛域名场景下支持\"*\"，且\"*必须为首字符 - 域名单节点长度不超过63个字符，即：***.***.com中，***的字符数不超过63个字符  **默认取值：** 不涉及

        :return: The domain_name of this DuplicateDomainRequestBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this DuplicateDomainRequestBody.

        **参数解释：** 需要添加到CDN控制台加速的域名 > 添加泛域名后，该泛域名所有次级域名均默认接入CDN加速。  **约束限制：** 加速域名不允许重复添加 **取值范围：** - 域名长度不能超过200个字符 - 支持大小写字母、数字、\"-\"、\".\"，首尾字符不能是\"-\"或\".\" - 泛域名场景下支持\"*\"，且\"*必须为首字符 - 域名单节点长度不超过63个字符，即：***.***.com中，***的字符数不超过63个字符  **默认取值：** 不涉及

        :param domain_name: The domain_name of this DuplicateDomainRequestBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, DuplicateDomainRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
