# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCodeGateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operator': 'str',
        'body': 'UpdateCodeGateRequestBody'
    }

    attribute_map = {
        'operator': 'operator',
        'body': 'body'
    }

    def __init__(self, operator=None, body=None):
        r"""UpdateCodeGateRequest

        The model defined in huaweicloud sdk

        :param operator: **参数解释：** 操作者。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type operator: str
        :param body: Body of the UpdateCodeGateRequest
        :type body: :class:`huaweicloudsdkcodeartscheck.v2.UpdateCodeGateRequestBody`
        """
        
        

        self._operator = None
        self._body = None
        self.discriminator = None

        if operator is not None:
            self.operator = operator
        if body is not None:
            self.body = body

    @property
    def operator(self):
        r"""Gets the operator of this UpdateCodeGateRequest.

        **参数解释：** 操作者。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The operator of this UpdateCodeGateRequest.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this UpdateCodeGateRequest.

        **参数解释：** 操作者。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param operator: The operator of this UpdateCodeGateRequest.
        :type operator: str
        """
        self._operator = operator

    @property
    def body(self):
        r"""Gets the body of this UpdateCodeGateRequest.

        :return: The body of this UpdateCodeGateRequest.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.UpdateCodeGateRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCodeGateRequest.

        :param body: The body of this UpdateCodeGateRequest.
        :type body: :class:`huaweicloudsdkcodeartscheck.v2.UpdateCodeGateRequestBody`
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
        if not isinstance(other, UpdateCodeGateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
