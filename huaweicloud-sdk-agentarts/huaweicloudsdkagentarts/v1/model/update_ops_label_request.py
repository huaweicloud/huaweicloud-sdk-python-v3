# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOpsLabelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label_id': 'str',
        'body': 'UpdateOpsLabelRequestBody'
    }

    attribute_map = {
        'label_id': 'label_id',
        'body': 'body'
    }

    def __init__(self, label_id=None, body=None):
        r"""UpdateOpsLabelRequest

        The model defined in huaweicloud sdk

        :param label_id: **参数解释：** 需要被更新的标签唯一标识符（ID）。 **约束限制：** 字符串长度为0到100。 **取值范围：** 0-100字符。 **默认取值：** 不涉及。
        :type label_id: str
        :param body: Body of the UpdateOpsLabelRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateOpsLabelRequestBody`
        """
        
        

        self._label_id = None
        self._body = None
        self.discriminator = None

        self.label_id = label_id
        if body is not None:
            self.body = body

    @property
    def label_id(self):
        r"""Gets the label_id of this UpdateOpsLabelRequest.

        **参数解释：** 需要被更新的标签唯一标识符（ID）。 **约束限制：** 字符串长度为0到100。 **取值范围：** 0-100字符。 **默认取值：** 不涉及。

        :return: The label_id of this UpdateOpsLabelRequest.
        :rtype: str
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        r"""Sets the label_id of this UpdateOpsLabelRequest.

        **参数解释：** 需要被更新的标签唯一标识符（ID）。 **约束限制：** 字符串长度为0到100。 **取值范围：** 0-100字符。 **默认取值：** 不涉及。

        :param label_id: The label_id of this UpdateOpsLabelRequest.
        :type label_id: str
        """
        self._label_id = label_id

    @property
    def body(self):
        r"""Gets the body of this UpdateOpsLabelRequest.

        :return: The body of this UpdateOpsLabelRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsLabelRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateOpsLabelRequest.

        :param body: The body of this UpdateOpsLabelRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateOpsLabelRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateOpsLabelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
