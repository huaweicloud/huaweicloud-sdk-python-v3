# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFirewallNameDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_name': 'str'
    }

    attribute_map = {
        'fw_instance_name': 'fw_instance_name'
    }

    def __init__(self, fw_instance_name=None):
        r"""UpdateFirewallNameDto

        The model defined in huaweicloud sdk

        :param fw_instance_name: **参数解释**： 防火墙名称 **约束限制**： 防火墙名称为中英文，包含数字，下划线，中划线，长度为1-48 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type fw_instance_name: str
        """
        
        

        self._fw_instance_name = None
        self.discriminator = None

        self.fw_instance_name = fw_instance_name

    @property
    def fw_instance_name(self):
        r"""Gets the fw_instance_name of this UpdateFirewallNameDto.

        **参数解释**： 防火墙名称 **约束限制**： 防火墙名称为中英文，包含数字，下划线，中划线，长度为1-48 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The fw_instance_name of this UpdateFirewallNameDto.
        :rtype: str
        """
        return self._fw_instance_name

    @fw_instance_name.setter
    def fw_instance_name(self, fw_instance_name):
        r"""Sets the fw_instance_name of this UpdateFirewallNameDto.

        **参数解释**： 防火墙名称 **约束限制**： 防火墙名称为中英文，包含数字，下划线，中划线，长度为1-48 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param fw_instance_name: The fw_instance_name of this UpdateFirewallNameDto.
        :type fw_instance_name: str
        """
        self._fw_instance_name = fw_instance_name

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
        if not isinstance(other, UpdateFirewallNameDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
