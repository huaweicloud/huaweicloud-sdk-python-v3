# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMessageAdditionsRequest:

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
        'message_id': 'str',
        'body': 'CreateMessageAdditionsReq'
    }

    attribute_map = {
        'chat_id': 'chat_id',
        'message_id': 'message_id',
        'body': 'body'
    }

    def __init__(self, chat_id=None, message_id=None, body=None):
        r"""CreateMessageAdditionsRequest

        The model defined in huaweicloud sdk

        :param chat_id: **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type chat_id: str
        :param message_id: **参数解释**： 问答ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type message_id: str
        :param body: Body of the CreateMessageAdditionsRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.CreateMessageAdditionsReq`
        """
        
        

        self._chat_id = None
        self._message_id = None
        self._body = None
        self.discriminator = None

        self.chat_id = chat_id
        self.message_id = message_id
        if body is not None:
            self.body = body

    @property
    def chat_id(self):
        r"""Gets the chat_id of this CreateMessageAdditionsRequest.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The chat_id of this CreateMessageAdditionsRequest.
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        r"""Sets the chat_id of this CreateMessageAdditionsRequest.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param chat_id: The chat_id of this CreateMessageAdditionsRequest.
        :type chat_id: str
        """
        self._chat_id = chat_id

    @property
    def message_id(self):
        r"""Gets the message_id of this CreateMessageAdditionsRequest.

        **参数解释**： 问答ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The message_id of this CreateMessageAdditionsRequest.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        r"""Sets the message_id of this CreateMessageAdditionsRequest.

        **参数解释**： 问答ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param message_id: The message_id of this CreateMessageAdditionsRequest.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def body(self):
        r"""Gets the body of this CreateMessageAdditionsRequest.

        :return: The body of this CreateMessageAdditionsRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateMessageAdditionsReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateMessageAdditionsRequest.

        :param body: The body of this CreateMessageAdditionsRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.CreateMessageAdditionsReq`
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
        if not isinstance(other, CreateMessageAdditionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
