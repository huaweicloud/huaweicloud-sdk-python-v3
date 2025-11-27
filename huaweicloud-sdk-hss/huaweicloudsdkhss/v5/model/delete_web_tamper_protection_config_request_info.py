# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteWebTamperProtectionConfigRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'protection_config_id_list': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'protection_config_id_list': 'protection_config_id_list'
    }

    def __init__(self, type=None, protection_config_id_list=None):
        r"""DeleteWebTamperProtectionConfigRequestInfo

        The model defined in huaweicloud sdk

        :param type: **参数解释**: 网页防篡改的类型 **约束限制**: 不涉及 **取值范围**: - container_wtp：容器网页防篡改  **默认取值**: 不涉及 
        :type type: str
        :param protection_config_id_list: **参数解释**: 防护配置id列表 **约束限制**: 不涉及 **取值范围**: 最少0条，最多100条 **默认取值**: 不涉及 
        :type protection_config_id_list: list[str]
        """
        
        

        self._type = None
        self._protection_config_id_list = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if protection_config_id_list is not None:
            self.protection_config_id_list = protection_config_id_list

    @property
    def type(self):
        r"""Gets the type of this DeleteWebTamperProtectionConfigRequestInfo.

        **参数解释**: 网页防篡改的类型 **约束限制**: 不涉及 **取值范围**: - container_wtp：容器网页防篡改  **默认取值**: 不涉及 

        :return: The type of this DeleteWebTamperProtectionConfigRequestInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeleteWebTamperProtectionConfigRequestInfo.

        **参数解释**: 网页防篡改的类型 **约束限制**: 不涉及 **取值范围**: - container_wtp：容器网页防篡改  **默认取值**: 不涉及 

        :param type: The type of this DeleteWebTamperProtectionConfigRequestInfo.
        :type type: str
        """
        self._type = type

    @property
    def protection_config_id_list(self):
        r"""Gets the protection_config_id_list of this DeleteWebTamperProtectionConfigRequestInfo.

        **参数解释**: 防护配置id列表 **约束限制**: 不涉及 **取值范围**: 最少0条，最多100条 **默认取值**: 不涉及 

        :return: The protection_config_id_list of this DeleteWebTamperProtectionConfigRequestInfo.
        :rtype: list[str]
        """
        return self._protection_config_id_list

    @protection_config_id_list.setter
    def protection_config_id_list(self, protection_config_id_list):
        r"""Sets the protection_config_id_list of this DeleteWebTamperProtectionConfigRequestInfo.

        **参数解释**: 防护配置id列表 **约束限制**: 不涉及 **取值范围**: 最少0条，最多100条 **默认取值**: 不涉及 

        :param protection_config_id_list: The protection_config_id_list of this DeleteWebTamperProtectionConfigRequestInfo.
        :type protection_config_id_list: list[str]
        """
        self._protection_config_id_list = protection_config_id_list

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
        if not isinstance(other, DeleteWebTamperProtectionConfigRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
