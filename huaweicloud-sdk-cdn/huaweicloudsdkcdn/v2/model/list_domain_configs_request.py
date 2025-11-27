# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_names': 'str',
        'item': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain_names': 'domain_names',
        'item': 'item',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain_names=None, item=None, enterprise_project_id=None):
        r"""ListDomainConfigsRequest

        The model defined in huaweicloud sdk

        :param domain_names: **参数解释：** 加速域名  - 多个域名使用英文半角逗号分隔  - 当查询cname状态时，该参数必传  **约束限制：** 仅支持查询已经在CDN添加成功的域名 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type domain_names: str
        :param item: **参数解释：** 查询数据类型 **约束限制：** 不涉及 **取值范围：** - cname_status: 域名cname状态 - copy: 查询账号下哪些加速域名支持复制配置  **默认取值：** 不涉及
        :type item: str
        :param enterprise_project_id: **参数解释：** 企业项目id。您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id **约束限制：** 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type enterprise_project_id: str
        """
        
        

        self._domain_names = None
        self._item = None
        self._enterprise_project_id = None
        self.discriminator = None

        if domain_names is not None:
            self.domain_names = domain_names
        self.item = item
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain_names(self):
        r"""Gets the domain_names of this ListDomainConfigsRequest.

        **参数解释：** 加速域名  - 多个域名使用英文半角逗号分隔  - 当查询cname状态时，该参数必传  **约束限制：** 仅支持查询已经在CDN添加成功的域名 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The domain_names of this ListDomainConfigsRequest.
        :rtype: str
        """
        return self._domain_names

    @domain_names.setter
    def domain_names(self, domain_names):
        r"""Sets the domain_names of this ListDomainConfigsRequest.

        **参数解释：** 加速域名  - 多个域名使用英文半角逗号分隔  - 当查询cname状态时，该参数必传  **约束限制：** 仅支持查询已经在CDN添加成功的域名 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param domain_names: The domain_names of this ListDomainConfigsRequest.
        :type domain_names: str
        """
        self._domain_names = domain_names

    @property
    def item(self):
        r"""Gets the item of this ListDomainConfigsRequest.

        **参数解释：** 查询数据类型 **约束限制：** 不涉及 **取值范围：** - cname_status: 域名cname状态 - copy: 查询账号下哪些加速域名支持复制配置  **默认取值：** 不涉及

        :return: The item of this ListDomainConfigsRequest.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this ListDomainConfigsRequest.

        **参数解释：** 查询数据类型 **约束限制：** 不涉及 **取值范围：** - cname_status: 域名cname状态 - copy: 查询账号下哪些加速域名支持复制配置  **默认取值：** 不涉及

        :param item: The item of this ListDomainConfigsRequest.
        :type item: str
        """
        self._item = item

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListDomainConfigsRequest.

        **参数解释：** 企业项目id。您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id **约束限制：** 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The enterprise_project_id of this ListDomainConfigsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListDomainConfigsRequest.

        **参数解释：** 企业项目id。您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id **约束限制：** 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param enterprise_project_id: The enterprise_project_id of this ListDomainConfigsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListDomainConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
