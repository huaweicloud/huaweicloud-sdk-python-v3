# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_chat_route_id': 'str',
        'body': 'UploadFileRequestBody'
    }

    attribute_map = {
        'x_chat_route_id': 'X-Chat-Route-Id',
        'body': 'body'
    }

    def __init__(self, x_chat_route_id=None, body=None):
        r"""UploadFileRequest

        The model defined in huaweicloud sdk

        :param x_chat_route_id: **参数解释**： 对话路由ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-64]个字符。 **默认取值**： 不涉及 
        :type x_chat_route_id: str
        :param body: Body of the UploadFileRequest
        :type body: :class:`huaweicloudsdkoptverse.v1.UploadFileRequestBody`
        """
        
        

        self._x_chat_route_id = None
        self._body = None
        self.discriminator = None

        self.x_chat_route_id = x_chat_route_id
        if body is not None:
            self.body = body

    @property
    def x_chat_route_id(self):
        r"""Gets the x_chat_route_id of this UploadFileRequest.

        **参数解释**： 对话路由ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-64]个字符。 **默认取值**： 不涉及 

        :return: The x_chat_route_id of this UploadFileRequest.
        :rtype: str
        """
        return self._x_chat_route_id

    @x_chat_route_id.setter
    def x_chat_route_id(self, x_chat_route_id):
        r"""Sets the x_chat_route_id of this UploadFileRequest.

        **参数解释**： 对话路由ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-64]个字符。 **默认取值**： 不涉及 

        :param x_chat_route_id: The x_chat_route_id of this UploadFileRequest.
        :type x_chat_route_id: str
        """
        self._x_chat_route_id = x_chat_route_id

    @property
    def body(self):
        r"""Gets the body of this UploadFileRequest.

        :return: The body of this UploadFileRequest.
        :rtype: :class:`huaweicloudsdkoptverse.v1.UploadFileRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UploadFileRequest.

        :param body: The body of this UploadFileRequest.
        :type body: :class:`huaweicloudsdkoptverse.v1.UploadFileRequestBody`
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
        if not isinstance(other, UploadFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
