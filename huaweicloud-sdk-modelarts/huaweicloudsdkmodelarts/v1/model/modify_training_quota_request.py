# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyTrainingQuotaRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'quotas': 'list[ModifyTrainingQuotaItem]'
    }

    attribute_map = {
        'user_id': 'user_id',
        'quotas': 'quotas'
    }

    def __init__(self, user_id=None, quotas=None):
        r"""ModifyTrainingQuotaRequest

        The model defined in huaweicloud sdk

        :param user_id: **参数解释**：用户ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type user_id: str
        :param quotas: **参数解释**：训练作业配额组。
        :type quotas: list[:class:`huaweicloudsdkmodelarts.v1.ModifyTrainingQuotaItem`]
        """
        
        

        self._user_id = None
        self._quotas = None
        self.discriminator = None

        self.user_id = user_id
        self.quotas = quotas

    @property
    def user_id(self):
        r"""Gets the user_id of this ModifyTrainingQuotaRequest.

        **参数解释**：用户ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The user_id of this ModifyTrainingQuotaRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ModifyTrainingQuotaRequest.

        **参数解释**：用户ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param user_id: The user_id of this ModifyTrainingQuotaRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def quotas(self):
        r"""Gets the quotas of this ModifyTrainingQuotaRequest.

        **参数解释**：训练作业配额组。

        :return: The quotas of this ModifyTrainingQuotaRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ModifyTrainingQuotaItem`]
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        r"""Sets the quotas of this ModifyTrainingQuotaRequest.

        **参数解释**：训练作业配额组。

        :param quotas: The quotas of this ModifyTrainingQuotaRequest.
        :type quotas: list[:class:`huaweicloudsdkmodelarts.v1.ModifyTrainingQuotaItem`]
        """
        self._quotas = quotas

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
        if not isinstance(other, ModifyTrainingQuotaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
