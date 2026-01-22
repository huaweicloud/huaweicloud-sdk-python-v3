# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddEipAlarmWhitelistRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_infos': 'list[EipInfo]',
        'fw_instance_id': 'str'
    }

    attribute_map = {
        'eip_infos': 'eip_infos',
        'fw_instance_id': 'fw_instance_id'
    }

    def __init__(self, eip_infos=None, fw_instance_id=None):
        r"""AddEipAlarmWhitelistRequestBody

        The model defined in huaweicloud sdk

        :param eip_infos: **参数解释**： EIP详情 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type eip_infos: list[:class:`huaweicloudsdkcfw.v1.EipInfo`]
        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        """
        
        

        self._eip_infos = None
        self._fw_instance_id = None
        self.discriminator = None

        if eip_infos is not None:
            self.eip_infos = eip_infos
        self.fw_instance_id = fw_instance_id

    @property
    def eip_infos(self):
        r"""Gets the eip_infos of this AddEipAlarmWhitelistRequestBody.

        **参数解释**： EIP详情 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The eip_infos of this AddEipAlarmWhitelistRequestBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.EipInfo`]
        """
        return self._eip_infos

    @eip_infos.setter
    def eip_infos(self, eip_infos):
        r"""Sets the eip_infos of this AddEipAlarmWhitelistRequestBody.

        **参数解释**： EIP详情 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param eip_infos: The eip_infos of this AddEipAlarmWhitelistRequestBody.
        :type eip_infos: list[:class:`huaweicloudsdkcfw.v1.EipInfo`]
        """
        self._eip_infos = eip_infos

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this AddEipAlarmWhitelistRequestBody.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this AddEipAlarmWhitelistRequestBody.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this AddEipAlarmWhitelistRequestBody.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this AddEipAlarmWhitelistRequestBody.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

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
        if not isinstance(other, AddEipAlarmWhitelistRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
