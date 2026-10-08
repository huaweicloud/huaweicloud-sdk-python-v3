# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelManagementQuotasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_model_provider_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'custom_model_provider_id': 'custom_model_provider_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, custom_model_provider_id=None, limit=None, offset=None):
        r"""ListModelManagementQuotasRequest

        The model defined in huaweicloud sdk

        :param custom_model_provider_id: **参数解释：** 模型提供商的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type custom_model_provider_id: str
        :param limit: **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** int32，取值范围为1-100条。 **默认取值：** 50 
        :type limit: int
        :param offset: **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** int32，取值范围为0-100000条。 **默认取值：** 0 
        :type offset: int
        """
        
        

        self._custom_model_provider_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if custom_model_provider_id is not None:
            self.custom_model_provider_id = custom_model_provider_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def custom_model_provider_id(self):
        r"""Gets the custom_model_provider_id of this ListModelManagementQuotasRequest.

        **参数解释：** 模型提供商的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The custom_model_provider_id of this ListModelManagementQuotasRequest.
        :rtype: str
        """
        return self._custom_model_provider_id

    @custom_model_provider_id.setter
    def custom_model_provider_id(self, custom_model_provider_id):
        r"""Sets the custom_model_provider_id of this ListModelManagementQuotasRequest.

        **参数解释：** 模型提供商的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param custom_model_provider_id: The custom_model_provider_id of this ListModelManagementQuotasRequest.
        :type custom_model_provider_id: str
        """
        self._custom_model_provider_id = custom_model_provider_id

    @property
    def limit(self):
        r"""Gets the limit of this ListModelManagementQuotasRequest.

        **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** int32，取值范围为1-100条。 **默认取值：** 50 

        :return: The limit of this ListModelManagementQuotasRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListModelManagementQuotasRequest.

        **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** int32，取值范围为1-100条。 **默认取值：** 50 

        :param limit: The limit of this ListModelManagementQuotasRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListModelManagementQuotasRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** int32，取值范围为0-100000条。 **默认取值：** 0 

        :return: The offset of this ListModelManagementQuotasRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListModelManagementQuotasRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** int32，取值范围为0-100000条。 **默认取值：** 0 

        :param offset: The offset of this ListModelManagementQuotasRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListModelManagementQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
