# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWebTamperProtectionConfigRequestBodyQuotaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'str',
        'resource_id_list': 'list[str]'
    }

    attribute_map = {
        'charging_mode': 'charging_mode',
        'resource_id_list': 'resource_id_list'
    }

    def __init__(self, charging_mode=None, resource_id_list=None):
        r"""CreateWebTamperProtectionConfigRequestBodyQuotaInfo

        The model defined in huaweicloud sdk

        :param charging_mode: **参数解释**: 计费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle：包年包月  **默认取值**: 不涉及 
        :type charging_mode: str
        :param resource_id_list: **参数解释**: 配额id列表 **约束限制**: 若该字段值为空，则随机选取配额 **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 
        :type resource_id_list: list[str]
        """
        
        

        self._charging_mode = None
        self._resource_id_list = None
        self.discriminator = None

        self.charging_mode = charging_mode
        if resource_id_list is not None:
            self.resource_id_list = resource_id_list

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this CreateWebTamperProtectionConfigRequestBodyQuotaInfo.

        **参数解释**: 计费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle：包年包月  **默认取值**: 不涉及 

        :return: The charging_mode of this CreateWebTamperProtectionConfigRequestBodyQuotaInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this CreateWebTamperProtectionConfigRequestBodyQuotaInfo.

        **参数解释**: 计费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle：包年包月  **默认取值**: 不涉及 

        :param charging_mode: The charging_mode of this CreateWebTamperProtectionConfigRequestBodyQuotaInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_id_list(self):
        r"""Gets the resource_id_list of this CreateWebTamperProtectionConfigRequestBodyQuotaInfo.

        **参数解释**: 配额id列表 **约束限制**: 若该字段值为空，则随机选取配额 **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 

        :return: The resource_id_list of this CreateWebTamperProtectionConfigRequestBodyQuotaInfo.
        :rtype: list[str]
        """
        return self._resource_id_list

    @resource_id_list.setter
    def resource_id_list(self, resource_id_list):
        r"""Sets the resource_id_list of this CreateWebTamperProtectionConfigRequestBodyQuotaInfo.

        **参数解释**: 配额id列表 **约束限制**: 若该字段值为空，则随机选取配额 **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 

        :param resource_id_list: The resource_id_list of this CreateWebTamperProtectionConfigRequestBodyQuotaInfo.
        :type resource_id_list: list[str]
        """
        self._resource_id_list = resource_id_list

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
        if not isinstance(other, CreateWebTamperProtectionConfigRequestBodyQuotaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
