# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str'
    }

    attribute_map = {
        'template_id': 'template_id'
    }

    def __init__(self, template_id=None):
        r"""ShowOpsEvaluatorTemplateRequest

        The model defined in huaweicloud sdk

        :param template_id: **参数解释：** 模板的唯一标识符（ID）。该参数用于在API路径中定位特定的配置模板或评估模板资源。 **约束限制：** 长度为1到100个字符的字符串。 **取值范围：** 通常由英文、数字、中划线（-）及下划线（_）组成，建议字符位数不超过 64 位。 **默认取值：** 不涉及。
        :type template_id: str
        """
        
        

        self._template_id = None
        self.discriminator = None

        self.template_id = template_id

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowOpsEvaluatorTemplateRequest.

        **参数解释：** 模板的唯一标识符（ID）。该参数用于在API路径中定位特定的配置模板或评估模板资源。 **约束限制：** 长度为1到100个字符的字符串。 **取值范围：** 通常由英文、数字、中划线（-）及下划线（_）组成，建议字符位数不超过 64 位。 **默认取值：** 不涉及。

        :return: The template_id of this ShowOpsEvaluatorTemplateRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowOpsEvaluatorTemplateRequest.

        **参数解释：** 模板的唯一标识符（ID）。该参数用于在API路径中定位特定的配置模板或评估模板资源。 **约束限制：** 长度为1到100个字符的字符串。 **取值范围：** 通常由英文、数字、中划线（-）及下划线（_）组成，建议字符位数不超过 64 位。 **默认取值：** 不涉及。

        :param template_id: The template_id of this ShowOpsEvaluatorTemplateRequest.
        :type template_id: str
        """
        self._template_id = template_id

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
        if not isinstance(other, ShowOpsEvaluatorTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
