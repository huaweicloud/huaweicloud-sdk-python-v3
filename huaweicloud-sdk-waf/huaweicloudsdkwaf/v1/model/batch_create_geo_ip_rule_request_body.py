# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateGeoIpRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'geoip': 'str',
        'white': 'int',
        'ip_type': 'str',
        'description': 'str',
        'policy_ids': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'geoip': 'geoip',
        'white': 'white',
        'ip_type': 'ip_type',
        'description': 'description',
        'policy_ids': 'policy_ids'
    }

    def __init__(self, name=None, geoip=None, white=None, ip_type=None, description=None, policy_ids=None):
        r"""BatchCreateGeoIpRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 地理位置控制规则名称
        :type name: str
        :param geoip: 地理位置封禁区域，可通过ShowPolicyGeoipMap接口查询支持的区域
        :type geoip: str
        :param white: 防护动作：  - 0 拦截  - 1 放行  - 2 仅记录
        :type white: int
        :param ip_type: ip范围。若您的网站使用独享模式，请确认独享引擎是否全部升级到最新版本，避免造成异常。202412之后的版本支持配置IP范围
        :type ip_type: str
        :param description: 规则描述
        :type description: str
        :param policy_ids: 需要添加规则的策略id
        :type policy_ids: list[str]
        """
        
        

        self._name = None
        self._geoip = None
        self._white = None
        self._ip_type = None
        self._description = None
        self._policy_ids = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.geoip = geoip
        self.white = white
        self.ip_type = ip_type
        if description is not None:
            self.description = description
        self.policy_ids = policy_ids

    @property
    def name(self):
        r"""Gets the name of this BatchCreateGeoIpRuleRequestBody.

        地理位置控制规则名称

        :return: The name of this BatchCreateGeoIpRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchCreateGeoIpRuleRequestBody.

        地理位置控制规则名称

        :param name: The name of this BatchCreateGeoIpRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def geoip(self):
        r"""Gets the geoip of this BatchCreateGeoIpRuleRequestBody.

        地理位置封禁区域，可通过ShowPolicyGeoipMap接口查询支持的区域

        :return: The geoip of this BatchCreateGeoIpRuleRequestBody.
        :rtype: str
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        r"""Sets the geoip of this BatchCreateGeoIpRuleRequestBody.

        地理位置封禁区域，可通过ShowPolicyGeoipMap接口查询支持的区域

        :param geoip: The geoip of this BatchCreateGeoIpRuleRequestBody.
        :type geoip: str
        """
        self._geoip = geoip

    @property
    def white(self):
        r"""Gets the white of this BatchCreateGeoIpRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :return: The white of this BatchCreateGeoIpRuleRequestBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        r"""Sets the white of this BatchCreateGeoIpRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :param white: The white of this BatchCreateGeoIpRuleRequestBody.
        :type white: int
        """
        self._white = white

    @property
    def ip_type(self):
        r"""Gets the ip_type of this BatchCreateGeoIpRuleRequestBody.

        ip范围。若您的网站使用独享模式，请确认独享引擎是否全部升级到最新版本，避免造成异常。202412之后的版本支持配置IP范围

        :return: The ip_type of this BatchCreateGeoIpRuleRequestBody.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        r"""Sets the ip_type of this BatchCreateGeoIpRuleRequestBody.

        ip范围。若您的网站使用独享模式，请确认独享引擎是否全部升级到最新版本，避免造成异常。202412之后的版本支持配置IP范围

        :param ip_type: The ip_type of this BatchCreateGeoIpRuleRequestBody.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def description(self):
        r"""Gets the description of this BatchCreateGeoIpRuleRequestBody.

        规则描述

        :return: The description of this BatchCreateGeoIpRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchCreateGeoIpRuleRequestBody.

        规则描述

        :param description: The description of this BatchCreateGeoIpRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def policy_ids(self):
        r"""Gets the policy_ids of this BatchCreateGeoIpRuleRequestBody.

        需要添加规则的策略id

        :return: The policy_ids of this BatchCreateGeoIpRuleRequestBody.
        :rtype: list[str]
        """
        return self._policy_ids

    @policy_ids.setter
    def policy_ids(self, policy_ids):
        r"""Sets the policy_ids of this BatchCreateGeoIpRuleRequestBody.

        需要添加规则的策略id

        :param policy_ids: The policy_ids of this BatchCreateGeoIpRuleRequestBody.
        :type policy_ids: list[str]
        """
        self._policy_ids = policy_ids

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
        if not isinstance(other, BatchCreateGeoIpRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
