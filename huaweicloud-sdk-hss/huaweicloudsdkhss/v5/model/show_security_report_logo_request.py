# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityReportLogoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'logo_type': 'str',
        'logo_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'logo_type': 'logo_type',
        'logo_id': 'logo_id'
    }

    def __init__(self, enterprise_project_id=None, logo_type=None, logo_id=None):
        r"""ShowSecurityReportLogoRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param logo_type: **参数解释**: logo类型 **约束限制**: 必填 **取值范围**: - default：华为logo - customize：自定义logo  **默认取值**: 不涉及 
        :type logo_type: str
        :param logo_id: **参数解释**: logo唯一ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type logo_id: str
        """
        
        

        self._enterprise_project_id = None
        self._logo_type = None
        self._logo_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.logo_type = logo_type
        if logo_id is not None:
            self.logo_id = logo_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowSecurityReportLogoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowSecurityReportLogoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowSecurityReportLogoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowSecurityReportLogoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def logo_type(self):
        r"""Gets the logo_type of this ShowSecurityReportLogoRequest.

        **参数解释**: logo类型 **约束限制**: 必填 **取值范围**: - default：华为logo - customize：自定义logo  **默认取值**: 不涉及 

        :return: The logo_type of this ShowSecurityReportLogoRequest.
        :rtype: str
        """
        return self._logo_type

    @logo_type.setter
    def logo_type(self, logo_type):
        r"""Sets the logo_type of this ShowSecurityReportLogoRequest.

        **参数解释**: logo类型 **约束限制**: 必填 **取值范围**: - default：华为logo - customize：自定义logo  **默认取值**: 不涉及 

        :param logo_type: The logo_type of this ShowSecurityReportLogoRequest.
        :type logo_type: str
        """
        self._logo_type = logo_type

    @property
    def logo_id(self):
        r"""Gets the logo_id of this ShowSecurityReportLogoRequest.

        **参数解释**: logo唯一ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The logo_id of this ShowSecurityReportLogoRequest.
        :rtype: str
        """
        return self._logo_id

    @logo_id.setter
    def logo_id(self, logo_id):
        r"""Sets the logo_id of this ShowSecurityReportLogoRequest.

        **参数解释**: logo唯一ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param logo_id: The logo_id of this ShowSecurityReportLogoRequest.
        :type logo_id: str
        """
        self._logo_id = logo_id

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
        if not isinstance(other, ShowSecurityReportLogoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
