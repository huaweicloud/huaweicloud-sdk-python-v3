# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDelegatedAccountsRequest:

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
        'refresh': 'bool'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'region': 'region',
        'refresh': 'refresh'
    }

    def __init__(self, x_security_token=None, region=None, refresh=None):
        r"""ListDelegatedAccountsRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param refresh: **参数解释**: 是否强制从organization同步组织信息 **约束限制**: 不涉及 **取值范围**: - true：强制从organization同步组织信息 - false：使用本地缓存的组织信息  **默认取值**: false 
        :type refresh: bool
        """
        
        

        self._x_security_token = None
        self._region = None
        self._refresh = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        if region is not None:
            self.region = region
        if refresh is not None:
            self.refresh = refresh

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListDelegatedAccountsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListDelegatedAccountsRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListDelegatedAccountsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListDelegatedAccountsRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def region(self):
        r"""Gets the region of this ListDelegatedAccountsRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListDelegatedAccountsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListDelegatedAccountsRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListDelegatedAccountsRequest.
        :type region: str
        """
        self._region = region

    @property
    def refresh(self):
        r"""Gets the refresh of this ListDelegatedAccountsRequest.

        **参数解释**: 是否强制从organization同步组织信息 **约束限制**: 不涉及 **取值范围**: - true：强制从organization同步组织信息 - false：使用本地缓存的组织信息  **默认取值**: false 

        :return: The refresh of this ListDelegatedAccountsRequest.
        :rtype: bool
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        r"""Sets the refresh of this ListDelegatedAccountsRequest.

        **参数解释**: 是否强制从organization同步组织信息 **约束限制**: 不涉及 **取值范围**: - true：强制从organization同步组织信息 - false：使用本地缓存的组织信息  **默认取值**: false 

        :param refresh: The refresh of this ListDelegatedAccountsRequest.
        :type refresh: bool
        """
        self._refresh = refresh

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
        if not isinstance(other, ListDelegatedAccountsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
