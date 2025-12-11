# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationTreeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'region': 'str',
        'enterprise_project_id': 'str',
        'is_refresh': 'bool'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'is_refresh': 'is_refresh'
    }

    def __init__(self, x_security_token=None, region=None, enterprise_project_id=None, is_refresh=None):
        r"""ListOrganizationTreeRequest

        The model defined in huaweicloud sdk

        :param x_security_token: **参数解释**: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。 **约束限制**: 不涉及 **取值范围**: 字符长度1-2048位 **默认取值**: 不涉及 
        :type x_security_token: str
        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param is_refresh: **参数解释**: 控制是否忽略本地缓存，强制从组织服务同步最新的组织树信息； **约束限制**: 无特殊约束，按需选择是否强制同步； **取值范围**: true（强制同步）、false（使用本地缓存，默认） **默认取值**: false 
        :type is_refresh: bool
        """
        
        

        self._x_security_token = None
        self._region = None
        self._enterprise_project_id = None
        self._is_refresh = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if is_refresh is not None:
            self.is_refresh = is_refresh

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListOrganizationTreeRequest.

        **参数解释**: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。 **约束限制**: 不涉及 **取值范围**: 字符长度1-2048位 **默认取值**: 不涉及 

        :return: The x_security_token of this ListOrganizationTreeRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListOrganizationTreeRequest.

        **参数解释**: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。 **约束限制**: 不涉及 **取值范围**: 字符长度1-2048位 **默认取值**: 不涉及 

        :param x_security_token: The x_security_token of this ListOrganizationTreeRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def region(self):
        r"""Gets the region of this ListOrganizationTreeRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListOrganizationTreeRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListOrganizationTreeRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListOrganizationTreeRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListOrganizationTreeRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListOrganizationTreeRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListOrganizationTreeRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListOrganizationTreeRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def is_refresh(self):
        r"""Gets the is_refresh of this ListOrganizationTreeRequest.

        **参数解释**: 控制是否忽略本地缓存，强制从组织服务同步最新的组织树信息； **约束限制**: 无特殊约束，按需选择是否强制同步； **取值范围**: true（强制同步）、false（使用本地缓存，默认） **默认取值**: false 

        :return: The is_refresh of this ListOrganizationTreeRequest.
        :rtype: bool
        """
        return self._is_refresh

    @is_refresh.setter
    def is_refresh(self, is_refresh):
        r"""Sets the is_refresh of this ListOrganizationTreeRequest.

        **参数解释**: 控制是否忽略本地缓存，强制从组织服务同步最新的组织树信息； **约束限制**: 无特殊约束，按需选择是否强制同步； **取值范围**: true（强制同步）、false（使用本地缓存，默认） **默认取值**: false 

        :param is_refresh: The is_refresh of this ListOrganizationTreeRequest.
        :type is_refresh: bool
        """
        self._is_refresh = is_refresh

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
        if not isinstance(other, ListOrganizationTreeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
