# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGeoIpRuleRequestBody:

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
        'status': 'int',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'geoip': 'geoip',
        'white': 'white',
        'status': 'status',
        'description': 'description'
    }

    def __init__(self, name=None, geoip=None, white=None, status=None, description=None):
        r"""CreateGeoIpRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 地理位置控制规则名称
        :type name: str
        :param geoip: 地理位置封禁区域，选择区域对应的字母代号,用中划线|分隔，可通过ShowPolicyGeoipMap接口查询支持的区域
        :type geoip: str
        :param white: 防护动作：  - 0 拦截  - 1 放行  - 2 仅记录
        :type white: int
        :param status: **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及
        :type status: int
        :param description: 规则描述
        :type description: str
        """
        
        

        self._name = None
        self._geoip = None
        self._white = None
        self._status = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.geoip = geoip
        self.white = white
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this CreateGeoIpRuleRequestBody.

        地理位置控制规则名称

        :return: The name of this CreateGeoIpRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateGeoIpRuleRequestBody.

        地理位置控制规则名称

        :param name: The name of this CreateGeoIpRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def geoip(self):
        r"""Gets the geoip of this CreateGeoIpRuleRequestBody.

        地理位置封禁区域，选择区域对应的字母代号,用中划线|分隔，可通过ShowPolicyGeoipMap接口查询支持的区域

        :return: The geoip of this CreateGeoIpRuleRequestBody.
        :rtype: str
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        r"""Sets the geoip of this CreateGeoIpRuleRequestBody.

        地理位置封禁区域，选择区域对应的字母代号,用中划线|分隔，可通过ShowPolicyGeoipMap接口查询支持的区域

        :param geoip: The geoip of this CreateGeoIpRuleRequestBody.
        :type geoip: str
        """
        self._geoip = geoip

    @property
    def white(self):
        r"""Gets the white of this CreateGeoIpRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :return: The white of this CreateGeoIpRuleRequestBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        r"""Sets the white of this CreateGeoIpRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :param white: The white of this CreateGeoIpRuleRequestBody.
        :type white: int
        """
        self._white = white

    @property
    def status(self):
        r"""Gets the status of this CreateGeoIpRuleRequestBody.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :return: The status of this CreateGeoIpRuleRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateGeoIpRuleRequestBody.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :param status: The status of this CreateGeoIpRuleRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this CreateGeoIpRuleRequestBody.

        规则描述

        :return: The description of this CreateGeoIpRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateGeoIpRuleRequestBody.

        规则描述

        :param description: The description of this CreateGeoIpRuleRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateGeoIpRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
