# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParseIpListResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'excess_ip': 'list[str]',
        'parsed_success_ip': 'list[str]'
    }

    attribute_map = {
        'excess_ip': 'excess_ip',
        'parsed_success_ip': 'parsed_success_ip'
    }

    def __init__(self, excess_ip=None, parsed_success_ip=None):
        r"""ParseIpListResponse

        The model defined in huaweicloud sdk

        :param excess_ip: **参数解释**： 超过限制的ip列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type excess_ip: list[str]
        :param parsed_success_ip: **参数解释**： 成功解析的ip列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type parsed_success_ip: list[str]
        """
        
        

        self._excess_ip = None
        self._parsed_success_ip = None
        self.discriminator = None

        if excess_ip is not None:
            self.excess_ip = excess_ip
        if parsed_success_ip is not None:
            self.parsed_success_ip = parsed_success_ip

    @property
    def excess_ip(self):
        r"""Gets the excess_ip of this ParseIpListResponse.

        **参数解释**： 超过限制的ip列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The excess_ip of this ParseIpListResponse.
        :rtype: list[str]
        """
        return self._excess_ip

    @excess_ip.setter
    def excess_ip(self, excess_ip):
        r"""Sets the excess_ip of this ParseIpListResponse.

        **参数解释**： 超过限制的ip列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param excess_ip: The excess_ip of this ParseIpListResponse.
        :type excess_ip: list[str]
        """
        self._excess_ip = excess_ip

    @property
    def parsed_success_ip(self):
        r"""Gets the parsed_success_ip of this ParseIpListResponse.

        **参数解释**： 成功解析的ip列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The parsed_success_ip of this ParseIpListResponse.
        :rtype: list[str]
        """
        return self._parsed_success_ip

    @parsed_success_ip.setter
    def parsed_success_ip(self, parsed_success_ip):
        r"""Sets the parsed_success_ip of this ParseIpListResponse.

        **参数解释**： 成功解析的ip列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param parsed_success_ip: The parsed_success_ip of this ParseIpListResponse.
        :type parsed_success_ip: list[str]
        """
        self._parsed_success_ip = parsed_success_ip

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
        if not isinstance(other, ParseIpListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
