# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchTransferPublicZonesTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_names': 'list[str]',
        'target_user': 'str'
    }

    attribute_map = {
        'zone_names': 'zone_names',
        'target_user': 'target_user'
    }

    def __init__(self, zone_names=None, target_user=None):
        r"""BatchTransferPublicZonesTaskRequestBody

        The model defined in huaweicloud sdk

        :param zone_names: **参数解释：** 域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type zone_names: list[str]
        :param target_user: **参数解释：** 对方账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type target_user: str
        """
        
        

        self._zone_names = None
        self._target_user = None
        self.discriminator = None

        self.zone_names = zone_names
        self.target_user = target_user

    @property
    def zone_names(self):
        r"""Gets the zone_names of this BatchTransferPublicZonesTaskRequestBody.

        **参数解释：** 域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The zone_names of this BatchTransferPublicZonesTaskRequestBody.
        :rtype: list[str]
        """
        return self._zone_names

    @zone_names.setter
    def zone_names(self, zone_names):
        r"""Sets the zone_names of this BatchTransferPublicZonesTaskRequestBody.

        **参数解释：** 域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param zone_names: The zone_names of this BatchTransferPublicZonesTaskRequestBody.
        :type zone_names: list[str]
        """
        self._zone_names = zone_names

    @property
    def target_user(self):
        r"""Gets the target_user of this BatchTransferPublicZonesTaskRequestBody.

        **参数解释：** 对方账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The target_user of this BatchTransferPublicZonesTaskRequestBody.
        :rtype: str
        """
        return self._target_user

    @target_user.setter
    def target_user(self, target_user):
        r"""Sets the target_user of this BatchTransferPublicZonesTaskRequestBody.

        **参数解释：** 对方账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param target_user: The target_user of this BatchTransferPublicZonesTaskRequestBody.
        :type target_user: str
        """
        self._target_user = target_user

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
        if not isinstance(other, BatchTransferPublicZonesTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
