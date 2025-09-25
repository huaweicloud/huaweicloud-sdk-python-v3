# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateChatRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chat_id': 'str',
        'body': 'UpdateChatReq'
    }

    attribute_map = {
        'chat_id': 'chat_id',
        'body': 'body'
    }

    def __init__(self, chat_id=None, body=None):
        r"""UpdateChatRequest

        The model defined in huaweicloud sdk

        :param chat_id: **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type chat_id: str
        :param body: Body of the UpdateChatRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.UpdateChatReq`
        """
        
        

        self._chat_id = None
        self._body = None
        self.discriminator = None

        self.chat_id = chat_id
        if body is not None:
            self.body = body

    @property
    def chat_id(self):
        r"""Gets the chat_id of this UpdateChatRequest.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The chat_id of this UpdateChatRequest.
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        r"""Sets the chat_id of this UpdateChatRequest.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param chat_id: The chat_id of this UpdateChatRequest.
        :type chat_id: str
        """
        self._chat_id = chat_id

    @property
    def body(self):
        r"""Gets the body of this UpdateChatRequest.

        :return: The body of this UpdateChatRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateChatReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateChatRequest.

        :param body: The body of this UpdateChatRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.UpdateChatReq`
        """
        self._body = body

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateChatRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
