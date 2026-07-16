# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'json_schema': 'str',
        'key': 'str',
        'support_content_types': 'list[str]'
    }

    attribute_map = {
        'json_schema': 'json_schema',
        'key': 'key',
        'support_content_types': 'support_content_types'
    }

    def __init__(self, json_schema=None, key=None, support_content_types=None):
        r"""ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas

        The model defined in huaweicloud sdk

        :param json_schema: **参数解释：** JSON出参描述输出返回值的数据结构。 **取值范围：** 符合JSONSchema 标准的字符串。 
        :type json_schema: str
        :param key: **参数解释：** 关键字用于标识输出参数。 **取值范围：** 合法的参数标识符。 
        :type key: str
        :param support_content_types: **参数解释：** 支持的类型标识输出参数可以返回的格式。 **取值范围：** 不涉及。 
        :type support_content_types: list[str]
        """
        
        

        self._json_schema = None
        self._key = None
        self._support_content_types = None
        self.discriminator = None

        if json_schema is not None:
            self.json_schema = json_schema
        if key is not None:
            self.key = key
        if support_content_types is not None:
            self.support_content_types = support_content_types

    @property
    def json_schema(self):
        r"""Gets the json_schema of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.

        **参数解释：** JSON出参描述输出返回值的数据结构。 **取值范围：** 符合JSONSchema 标准的字符串。 

        :return: The json_schema of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.
        :rtype: str
        """
        return self._json_schema

    @json_schema.setter
    def json_schema(self, json_schema):
        r"""Sets the json_schema of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.

        **参数解释：** JSON出参描述输出返回值的数据结构。 **取值范围：** 符合JSONSchema 标准的字符串。 

        :param json_schema: The json_schema of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.
        :type json_schema: str
        """
        self._json_schema = json_schema

    @property
    def key(self):
        r"""Gets the key of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.

        **参数解释：** 关键字用于标识输出参数。 **取值范围：** 合法的参数标识符。 

        :return: The key of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.

        **参数解释：** 关键字用于标识输出参数。 **取值范围：** 合法的参数标识符。 

        :param key: The key of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.
        :type key: str
        """
        self._key = key

    @property
    def support_content_types(self):
        r"""Gets the support_content_types of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.

        **参数解释：** 支持的类型标识输出参数可以返回的格式。 **取值范围：** 不涉及。 

        :return: The support_content_types of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.
        :rtype: list[str]
        """
        return self._support_content_types

    @support_content_types.setter
    def support_content_types(self, support_content_types):
        r"""Sets the support_content_types of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.

        **参数解释：** 支持的类型标识输出参数可以返回的格式。 **取值范围：** 不涉及。 

        :param support_content_types: The support_content_types of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas.
        :type support_content_types: list[str]
        """
        self._support_content_types = support_content_types

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
        if not isinstance(other, ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
