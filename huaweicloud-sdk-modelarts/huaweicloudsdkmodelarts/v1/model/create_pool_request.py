# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePoolRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_model_arts_user_id': 'str',
        'body': 'CreatePoolRequestBody'
    }

    attribute_map = {
        'x_model_arts_user_id': 'X-ModelArts-User-ID',
        'body': 'body'
    }

    def __init__(self, x_model_arts_user_id=None, body=None):
        r"""CreatePoolRequest

        The model defined in huaweicloud sdk

        :param x_model_arts_user_id: **参数解释**：实际的外部租户ID，如果有的话，工作空间鉴权以该ID为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type x_model_arts_user_id: str
        :param body: Body of the CreatePoolRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.CreatePoolRequestBody`
        """
        
        

        self._x_model_arts_user_id = None
        self._body = None
        self.discriminator = None

        if x_model_arts_user_id is not None:
            self.x_model_arts_user_id = x_model_arts_user_id
        if body is not None:
            self.body = body

    @property
    def x_model_arts_user_id(self):
        r"""Gets the x_model_arts_user_id of this CreatePoolRequest.

        **参数解释**：实际的外部租户ID，如果有的话，工作空间鉴权以该ID为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The x_model_arts_user_id of this CreatePoolRequest.
        :rtype: str
        """
        return self._x_model_arts_user_id

    @x_model_arts_user_id.setter
    def x_model_arts_user_id(self, x_model_arts_user_id):
        r"""Sets the x_model_arts_user_id of this CreatePoolRequest.

        **参数解释**：实际的外部租户ID，如果有的话，工作空间鉴权以该ID为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param x_model_arts_user_id: The x_model_arts_user_id of this CreatePoolRequest.
        :type x_model_arts_user_id: str
        """
        self._x_model_arts_user_id = x_model_arts_user_id

    @property
    def body(self):
        r"""Gets the body of this CreatePoolRequest.

        :return: The body of this CreatePoolRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreatePoolRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreatePoolRequest.

        :param body: The body of this CreatePoolRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.CreatePoolRequestBody`
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
        if not isinstance(other, CreatePoolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
