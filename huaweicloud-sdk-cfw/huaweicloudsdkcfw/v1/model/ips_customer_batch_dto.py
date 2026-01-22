# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsCustomerBatchDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_type': 'int',
        'ips_ids': 'list[str]',
        'fw_instance_id': 'str'
    }

    attribute_map = {
        'action_type': 'action_type',
        'ips_ids': 'ips_ids',
        'fw_instance_id': 'fw_instance_id'
    }

    def __init__(self, action_type=None, ips_ids=None, fw_instance_id=None):
        r"""IpsCustomerBatchDto

        The model defined in huaweicloud sdk

        :param action_type: **参数解释**： 自定义IPS规则执行动作,仅更新自定义IPS规则场景下需要设置，其他场景无需设置 **约束限制**：   不涉及 **取值范围**： 0：只记录日志 1：重置/拦截 **默认取值**：   不涉及
        :type action_type: int
        :param ips_ids: **参数解释**： ips规则ID， 可通过调用获取ips规则列表获取，通过data.records.ips_id获取。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type ips_ids: list[str]
        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        """
        
        

        self._action_type = None
        self._ips_ids = None
        self._fw_instance_id = None
        self.discriminator = None

        if action_type is not None:
            self.action_type = action_type
        self.ips_ids = ips_ids
        self.fw_instance_id = fw_instance_id

    @property
    def action_type(self):
        r"""Gets the action_type of this IpsCustomerBatchDto.

        **参数解释**： 自定义IPS规则执行动作,仅更新自定义IPS规则场景下需要设置，其他场景无需设置 **约束限制**：   不涉及 **取值范围**： 0：只记录日志 1：重置/拦截 **默认取值**：   不涉及

        :return: The action_type of this IpsCustomerBatchDto.
        :rtype: int
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this IpsCustomerBatchDto.

        **参数解释**： 自定义IPS规则执行动作,仅更新自定义IPS规则场景下需要设置，其他场景无需设置 **约束限制**：   不涉及 **取值范围**： 0：只记录日志 1：重置/拦截 **默认取值**：   不涉及

        :param action_type: The action_type of this IpsCustomerBatchDto.
        :type action_type: int
        """
        self._action_type = action_type

    @property
    def ips_ids(self):
        r"""Gets the ips_ids of this IpsCustomerBatchDto.

        **参数解释**： ips规则ID， 可通过调用获取ips规则列表获取，通过data.records.ips_id获取。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The ips_ids of this IpsCustomerBatchDto.
        :rtype: list[str]
        """
        return self._ips_ids

    @ips_ids.setter
    def ips_ids(self, ips_ids):
        r"""Sets the ips_ids of this IpsCustomerBatchDto.

        **参数解释**： ips规则ID， 可通过调用获取ips规则列表获取，通过data.records.ips_id获取。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param ips_ids: The ips_ids of this IpsCustomerBatchDto.
        :type ips_ids: list[str]
        """
        self._ips_ids = ips_ids

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this IpsCustomerBatchDto.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this IpsCustomerBatchDto.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this IpsCustomerBatchDto.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this IpsCustomerBatchDto.
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
        if not isinstance(other, IpsCustomerBatchDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
