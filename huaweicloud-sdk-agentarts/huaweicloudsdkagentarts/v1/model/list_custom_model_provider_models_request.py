# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomModelProviderModelsRequest:

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
        'id': 'str',
        'model_service_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'custom_model_provider_id': 'custom_model_provider_id',
        'id': 'id',
        'model_service_name': 'model_service_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, custom_model_provider_id=None, id=None, model_service_name=None, limit=None, offset=None):
        r"""ListCustomModelProviderModelsRequest

        The model defined in huaweicloud sdk

        :param custom_model_provider_id: **参数解释：** 模型提供商ID。 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type custom_model_provider_id: str
        :param id: **参数解释：** 按模型ID过滤，支持多个ID（最多支持20个ID）。 示例: id&#x3D;id1&amp;id&#x3D;id2 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type id: str
        :param model_service_name: **参数解释：** 按显示名称过滤模型，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 长度为2-64个字符。 **默认取值：** 不涉及。 
        :type model_service_name: str
        :param limit: **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100。 **默认取值：** 50 
        :type limit: int
        :param offset: **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为0-100000。 **默认取值：** 0 
        :type offset: int
        """
        
        

        self._custom_model_provider_id = None
        self._id = None
        self._model_service_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.custom_model_provider_id = custom_model_provider_id
        if id is not None:
            self.id = id
        if model_service_name is not None:
            self.model_service_name = model_service_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def custom_model_provider_id(self):
        r"""Gets the custom_model_provider_id of this ListCustomModelProviderModelsRequest.

        **参数解释：** 模型提供商ID。 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The custom_model_provider_id of this ListCustomModelProviderModelsRequest.
        :rtype: str
        """
        return self._custom_model_provider_id

    @custom_model_provider_id.setter
    def custom_model_provider_id(self, custom_model_provider_id):
        r"""Sets the custom_model_provider_id of this ListCustomModelProviderModelsRequest.

        **参数解释：** 模型提供商ID。 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param custom_model_provider_id: The custom_model_provider_id of this ListCustomModelProviderModelsRequest.
        :type custom_model_provider_id: str
        """
        self._custom_model_provider_id = custom_model_provider_id

    @property
    def id(self):
        r"""Gets the id of this ListCustomModelProviderModelsRequest.

        **参数解释：** 按模型ID过滤，支持多个ID（最多支持20个ID）。 示例: id=id1&id=id2 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The id of this ListCustomModelProviderModelsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListCustomModelProviderModelsRequest.

        **参数解释：** 按模型ID过滤，支持多个ID（最多支持20个ID）。 示例: id=id1&id=id2 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param id: The id of this ListCustomModelProviderModelsRequest.
        :type id: str
        """
        self._id = id

    @property
    def model_service_name(self):
        r"""Gets the model_service_name of this ListCustomModelProviderModelsRequest.

        **参数解释：** 按显示名称过滤模型，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 长度为2-64个字符。 **默认取值：** 不涉及。 

        :return: The model_service_name of this ListCustomModelProviderModelsRequest.
        :rtype: str
        """
        return self._model_service_name

    @model_service_name.setter
    def model_service_name(self, model_service_name):
        r"""Sets the model_service_name of this ListCustomModelProviderModelsRequest.

        **参数解释：** 按显示名称过滤模型，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 长度为2-64个字符。 **默认取值：** 不涉及。 

        :param model_service_name: The model_service_name of this ListCustomModelProviderModelsRequest.
        :type model_service_name: str
        """
        self._model_service_name = model_service_name

    @property
    def limit(self):
        r"""Gets the limit of this ListCustomModelProviderModelsRequest.

        **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100。 **默认取值：** 50 

        :return: The limit of this ListCustomModelProviderModelsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCustomModelProviderModelsRequest.

        **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100。 **默认取值：** 50 

        :param limit: The limit of this ListCustomModelProviderModelsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCustomModelProviderModelsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为0-100000。 **默认取值：** 0 

        :return: The offset of this ListCustomModelProviderModelsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCustomModelProviderModelsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为0-100000。 **默认取值：** 0 

        :param offset: The offset of this ListCustomModelProviderModelsRequest.
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
        if not isinstance(other, ListCustomModelProviderModelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
