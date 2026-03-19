# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGeoipRuleRequestBody:

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
        'description': 'str',
        'geoip': 'str',
        'white': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'geoip': 'geoip',
        'white': 'white'
    }

    def __init__(self, name=None, description=None, geoip=None, white=None):
        r"""UpdateGeoipRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 地理位置控制规则名称
        :type name: str
        :param description: 描述
        :type description: str
        :param geoip: 地理位置封禁区域，选择区域对应的字母代号，可通过ShowPolicyGeoipMap接口查询支持的区域
        :type geoip: str
        :param white: 防护动作：  - 0 拦截  - 1 放行  - 2 仅记录
        :type white: int
        """
        
        

        self._name = None
        self._description = None
        self._geoip = None
        self._white = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.geoip = geoip
        self.white = white

    @property
    def name(self):
        r"""Gets the name of this UpdateGeoipRuleRequestBody.

        地理位置控制规则名称

        :return: The name of this UpdateGeoipRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateGeoipRuleRequestBody.

        地理位置控制规则名称

        :param name: The name of this UpdateGeoipRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateGeoipRuleRequestBody.

        描述

        :return: The description of this UpdateGeoipRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateGeoipRuleRequestBody.

        描述

        :param description: The description of this UpdateGeoipRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def geoip(self):
        r"""Gets the geoip of this UpdateGeoipRuleRequestBody.

        地理位置封禁区域，选择区域对应的字母代号，可通过ShowPolicyGeoipMap接口查询支持的区域

        :return: The geoip of this UpdateGeoipRuleRequestBody.
        :rtype: str
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        r"""Sets the geoip of this UpdateGeoipRuleRequestBody.

        地理位置封禁区域，选择区域对应的字母代号，可通过ShowPolicyGeoipMap接口查询支持的区域

        :param geoip: The geoip of this UpdateGeoipRuleRequestBody.
        :type geoip: str
        """
        self._geoip = geoip

    @property
    def white(self):
        r"""Gets the white of this UpdateGeoipRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :return: The white of this UpdateGeoipRuleRequestBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        r"""Sets the white of this UpdateGeoipRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :param white: The white of this UpdateGeoipRuleRequestBody.
        :type white: int
        """
        self._white = white

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
        if not isinstance(other, UpdateGeoipRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
