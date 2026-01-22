# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConfigQuotaDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_info': 'ItemInfo',
        'max_quota': 'int',
        'quota_type': 'str',
        'used_quota': 'int'
    }

    attribute_map = {
        'item_info': 'item_info',
        'max_quota': 'max_quota',
        'quota_type': 'quota_type',
        'used_quota': 'used_quota'
    }

    def __init__(self, item_info=None, max_quota=None, quota_type=None, used_quota=None):
        r"""ShowConfigQuotaDto

        The model defined in huaweicloud sdk

        :param item_info: 
        :type item_info: :class:`huaweicloudsdkcfw.v1.ItemInfo`
        :param max_quota: **参数解释**： 防火墙成员最大配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type max_quota: int
        :param quota_type: **参数解释**： 防火墙成员配额类型 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type quota_type: str
        :param used_quota: **参数解释**： 已使用配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type used_quota: int
        """
        
        

        self._item_info = None
        self._max_quota = None
        self._quota_type = None
        self._used_quota = None
        self.discriminator = None

        if item_info is not None:
            self.item_info = item_info
        if max_quota is not None:
            self.max_quota = max_quota
        if quota_type is not None:
            self.quota_type = quota_type
        if used_quota is not None:
            self.used_quota = used_quota

    @property
    def item_info(self):
        r"""Gets the item_info of this ShowConfigQuotaDto.

        :return: The item_info of this ShowConfigQuotaDto.
        :rtype: :class:`huaweicloudsdkcfw.v1.ItemInfo`
        """
        return self._item_info

    @item_info.setter
    def item_info(self, item_info):
        r"""Sets the item_info of this ShowConfigQuotaDto.

        :param item_info: The item_info of this ShowConfigQuotaDto.
        :type item_info: :class:`huaweicloudsdkcfw.v1.ItemInfo`
        """
        self._item_info = item_info

    @property
    def max_quota(self):
        r"""Gets the max_quota of this ShowConfigQuotaDto.

        **参数解释**： 防火墙成员最大配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The max_quota of this ShowConfigQuotaDto.
        :rtype: int
        """
        return self._max_quota

    @max_quota.setter
    def max_quota(self, max_quota):
        r"""Sets the max_quota of this ShowConfigQuotaDto.

        **参数解释**： 防火墙成员最大配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param max_quota: The max_quota of this ShowConfigQuotaDto.
        :type max_quota: int
        """
        self._max_quota = max_quota

    @property
    def quota_type(self):
        r"""Gets the quota_type of this ShowConfigQuotaDto.

        **参数解释**： 防火墙成员配额类型 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The quota_type of this ShowConfigQuotaDto.
        :rtype: str
        """
        return self._quota_type

    @quota_type.setter
    def quota_type(self, quota_type):
        r"""Sets the quota_type of this ShowConfigQuotaDto.

        **参数解释**： 防火墙成员配额类型 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param quota_type: The quota_type of this ShowConfigQuotaDto.
        :type quota_type: str
        """
        self._quota_type = quota_type

    @property
    def used_quota(self):
        r"""Gets the used_quota of this ShowConfigQuotaDto.

        **参数解释**： 已使用配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The used_quota of this ShowConfigQuotaDto.
        :rtype: int
        """
        return self._used_quota

    @used_quota.setter
    def used_quota(self, used_quota):
        r"""Sets the used_quota of this ShowConfigQuotaDto.

        **参数解释**： 已使用配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param used_quota: The used_quota of this ShowConfigQuotaDto.
        :type used_quota: int
        """
        self._used_quota = used_quota

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
        if not isinstance(other, ShowConfigQuotaDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
