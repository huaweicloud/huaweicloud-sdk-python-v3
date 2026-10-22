# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomLlmRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'model_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'name': 'name',
        'model_name': 'model_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, name=None, model_name=None, offset=None, limit=None):
        r"""ListCustomLlmRequest

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 自定义大模型名称筛选 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param model_name: **参数解释：** 模型名称筛选 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type model_name: str
        :param offset: **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 0
        :type offset: int
        :param limit: **参数解释：** 每页数量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 10
        :type limit: int
        """
        
        

        self._name = None
        self._model_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if model_name is not None:
            self.model_name = model_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListCustomLlmRequest.

        **参数解释：** 自定义大模型名称筛选 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this ListCustomLlmRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCustomLlmRequest.

        **参数解释：** 自定义大模型名称筛选 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this ListCustomLlmRequest.
        :type name: str
        """
        self._name = name

    @property
    def model_name(self):
        r"""Gets the model_name of this ListCustomLlmRequest.

        **参数解释：** 模型名称筛选 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The model_name of this ListCustomLlmRequest.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this ListCustomLlmRequest.

        **参数解释：** 模型名称筛选 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param model_name: The model_name of this ListCustomLlmRequest.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def offset(self):
        r"""Gets the offset of this ListCustomLlmRequest.

        **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 0

        :return: The offset of this ListCustomLlmRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCustomLlmRequest.

        **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 0

        :param offset: The offset of this ListCustomLlmRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCustomLlmRequest.

        **参数解释：** 每页数量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 10

        :return: The limit of this ListCustomLlmRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCustomLlmRequest.

        **参数解释：** 每页数量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 10

        :param limit: The limit of this ListCustomLlmRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListCustomLlmRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
