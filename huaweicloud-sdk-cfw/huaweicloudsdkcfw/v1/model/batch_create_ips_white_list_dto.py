# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateIpsWhiteListDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ips_white_list_dto_list': 'list[IpsWhiteListDto]'
    }

    attribute_map = {
        'ips_white_list_dto_list': 'ips_white_list_dto_list'
    }

    def __init__(self, ips_white_list_dto_list=None):
        r"""BatchCreateIpsWhiteListDto

        The model defined in huaweicloud sdk

        :param ips_white_list_dto_list: **参数解释**：  添加的IPS白名单列表 **约束限制**：  不涉及  **取值范围**： 不涉及  **默认取值**：  不涉及
        :type ips_white_list_dto_list: list[:class:`huaweicloudsdkcfw.v1.IpsWhiteListDto`]
        """
        
        

        self._ips_white_list_dto_list = None
        self.discriminator = None

        self.ips_white_list_dto_list = ips_white_list_dto_list

    @property
    def ips_white_list_dto_list(self):
        r"""Gets the ips_white_list_dto_list of this BatchCreateIpsWhiteListDto.

        **参数解释**：  添加的IPS白名单列表 **约束限制**：  不涉及  **取值范围**： 不涉及  **默认取值**：  不涉及

        :return: The ips_white_list_dto_list of this BatchCreateIpsWhiteListDto.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.IpsWhiteListDto`]
        """
        return self._ips_white_list_dto_list

    @ips_white_list_dto_list.setter
    def ips_white_list_dto_list(self, ips_white_list_dto_list):
        r"""Sets the ips_white_list_dto_list of this BatchCreateIpsWhiteListDto.

        **参数解释**：  添加的IPS白名单列表 **约束限制**：  不涉及  **取值范围**： 不涉及  **默认取值**：  不涉及

        :param ips_white_list_dto_list: The ips_white_list_dto_list of this BatchCreateIpsWhiteListDto.
        :type ips_white_list_dto_list: list[:class:`huaweicloudsdkcfw.v1.IpsWhiteListDto`]
        """
        self._ips_white_list_dto_list = ips_white_list_dto_list

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
        if not isinstance(other, BatchCreateIpsWhiteListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
