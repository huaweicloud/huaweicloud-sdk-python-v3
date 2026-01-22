# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirewallProtectionStatusVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protection_status': 'int',
        'id': 'str',
        'object_id': 'str',
        'failed_eip_list': 'list[str]',
        'failed_eip_id_list': 'list[str]'
    }

    attribute_map = {
        'protection_status': 'protection_status',
        'id': 'id',
        'object_id': 'object_id',
        'failed_eip_list': 'failed_eip_list',
        'failed_eip_id_list': 'failed_eip_id_list'
    }

    def __init__(self, protection_status=None, id=None, object_id=None, failed_eip_list=None, failed_eip_id_list=None):
        r"""FirewallProtectionStatusVO

        The model defined in huaweicloud sdk

        :param protection_status: **参数解释**： 防火墙防护状态，0: 正常状态, 1: bypass进行中, 2: bypass成功, 3: bypass失败, 4: 恢复中, 5: 恢复失败 **取值范围**： 不涉及
        :type protection_status: int
        :param id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type id: str
        :param object_id: **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type object_id: str
        :param failed_eip_list: **参数解释**： bypass失败的eip列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type failed_eip_list: list[str]
        :param failed_eip_id_list: **参数解释**： bypass失败的eip id列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type failed_eip_id_list: list[str]
        """
        
        

        self._protection_status = None
        self._id = None
        self._object_id = None
        self._failed_eip_list = None
        self._failed_eip_id_list = None
        self.discriminator = None

        if protection_status is not None:
            self.protection_status = protection_status
        if id is not None:
            self.id = id
        if object_id is not None:
            self.object_id = object_id
        if failed_eip_list is not None:
            self.failed_eip_list = failed_eip_list
        if failed_eip_id_list is not None:
            self.failed_eip_id_list = failed_eip_id_list

    @property
    def protection_status(self):
        r"""Gets the protection_status of this FirewallProtectionStatusVO.

        **参数解释**： 防火墙防护状态，0: 正常状态, 1: bypass进行中, 2: bypass成功, 3: bypass失败, 4: 恢复中, 5: 恢复失败 **取值范围**： 不涉及

        :return: The protection_status of this FirewallProtectionStatusVO.
        :rtype: int
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this FirewallProtectionStatusVO.

        **参数解释**： 防火墙防护状态，0: 正常状态, 1: bypass进行中, 2: bypass成功, 3: bypass失败, 4: 恢复中, 5: 恢复失败 **取值范围**： 不涉及

        :param protection_status: The protection_status of this FirewallProtectionStatusVO.
        :type protection_status: int
        """
        self._protection_status = protection_status

    @property
    def id(self):
        r"""Gets the id of this FirewallProtectionStatusVO.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The id of this FirewallProtectionStatusVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FirewallProtectionStatusVO.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param id: The id of this FirewallProtectionStatusVO.
        :type id: str
        """
        self._id = id

    @property
    def object_id(self):
        r"""Gets the object_id of this FirewallProtectionStatusVO.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The object_id of this FirewallProtectionStatusVO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this FirewallProtectionStatusVO.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param object_id: The object_id of this FirewallProtectionStatusVO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def failed_eip_list(self):
        r"""Gets the failed_eip_list of this FirewallProtectionStatusVO.

        **参数解释**： bypass失败的eip列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The failed_eip_list of this FirewallProtectionStatusVO.
        :rtype: list[str]
        """
        return self._failed_eip_list

    @failed_eip_list.setter
    def failed_eip_list(self, failed_eip_list):
        r"""Sets the failed_eip_list of this FirewallProtectionStatusVO.

        **参数解释**： bypass失败的eip列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param failed_eip_list: The failed_eip_list of this FirewallProtectionStatusVO.
        :type failed_eip_list: list[str]
        """
        self._failed_eip_list = failed_eip_list

    @property
    def failed_eip_id_list(self):
        r"""Gets the failed_eip_id_list of this FirewallProtectionStatusVO.

        **参数解释**： bypass失败的eip id列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The failed_eip_id_list of this FirewallProtectionStatusVO.
        :rtype: list[str]
        """
        return self._failed_eip_id_list

    @failed_eip_id_list.setter
    def failed_eip_id_list(self, failed_eip_id_list):
        r"""Sets the failed_eip_id_list of this FirewallProtectionStatusVO.

        **参数解释**： bypass失败的eip id列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param failed_eip_id_list: The failed_eip_id_list of this FirewallProtectionStatusVO.
        :type failed_eip_id_list: list[str]
        """
        self._failed_eip_id_list = failed_eip_id_list

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
        if not isinstance(other, FirewallProtectionStatusVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
