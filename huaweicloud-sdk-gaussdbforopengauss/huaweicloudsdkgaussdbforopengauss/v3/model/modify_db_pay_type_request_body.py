# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyDBPayTypeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entity_ids': 'list[str]',
        'charge_info': 'PeriodChargeInfoOption'
    }

    attribute_map = {
        'entity_ids': 'entity_ids',
        'charge_info': 'charge_info'
    }

    def __init__(self, entity_ids=None, charge_info=None):
        r"""ModifyDBPayTypeRequestBody

        The model defined in huaweicloud sdk

        :param entity_ids: **参数解释**: 需要转成包周期计费模式的实例ID列表。 **约束限制**: 不涉及。
        :type entity_ids: list[str]
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.PeriodChargeInfoOption`
        """
        
        

        self._entity_ids = None
        self._charge_info = None
        self.discriminator = None

        self.entity_ids = entity_ids
        self.charge_info = charge_info

    @property
    def entity_ids(self):
        r"""Gets the entity_ids of this ModifyDBPayTypeRequestBody.

        **参数解释**: 需要转成包周期计费模式的实例ID列表。 **约束限制**: 不涉及。

        :return: The entity_ids of this ModifyDBPayTypeRequestBody.
        :rtype: list[str]
        """
        return self._entity_ids

    @entity_ids.setter
    def entity_ids(self, entity_ids):
        r"""Sets the entity_ids of this ModifyDBPayTypeRequestBody.

        **参数解释**: 需要转成包周期计费模式的实例ID列表。 **约束限制**: 不涉及。

        :param entity_ids: The entity_ids of this ModifyDBPayTypeRequestBody.
        :type entity_ids: list[str]
        """
        self._entity_ids = entity_ids

    @property
    def charge_info(self):
        r"""Gets the charge_info of this ModifyDBPayTypeRequestBody.

        :return: The charge_info of this ModifyDBPayTypeRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.PeriodChargeInfoOption`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this ModifyDBPayTypeRequestBody.

        :param charge_info: The charge_info of this ModifyDBPayTypeRequestBody.
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.PeriodChargeInfoOption`
        """
        self._charge_info = charge_info

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
        if not isinstance(other, ModifyDBPayTypeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
