# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMessageTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_template_name': 'str',
        'protocol': 'str',
        'content': 'str'
    }

    attribute_map = {
        'message_template_name': 'message_template_name',
        'protocol': 'protocol',
        'content': 'content'
    }

    def __init__(self, message_template_name=None, protocol=None, content=None):
        r"""CreateMessageTemplateRequestBody

        The model defined in huaweicloud sdk

        :param message_template_name: 创建模板的名称。只能包含大写字母、小写字母、数字、-和_，且必须由大写字母、小写字母或数字开头，长度在1到64个字符之间。
        :type message_template_name: str
        :param protocol: 模板支持的协议类型。  目前支持的协议包括：  “default”：默认协议。  “email”：邮件传输协议。  “sms”：短信传输协议。  “functionstage”：FunctionGraph（函数）传输协议。  “http”、“https”：HTTP/HTTPS传输协议。
        :type protocol: str
        :param content: 模板内容，模板目前仅支持纯文本模式。模板内容不能空，最大支持256KB。
        :type content: str
        """
        
        

        self._message_template_name = None
        self._protocol = None
        self._content = None
        self.discriminator = None

        self.message_template_name = message_template_name
        self.protocol = protocol
        self.content = content

    @property
    def message_template_name(self):
        r"""Gets the message_template_name of this CreateMessageTemplateRequestBody.

        创建模板的名称。只能包含大写字母、小写字母、数字、-和_，且必须由大写字母、小写字母或数字开头，长度在1到64个字符之间。

        :return: The message_template_name of this CreateMessageTemplateRequestBody.
        :rtype: str
        """
        return self._message_template_name

    @message_template_name.setter
    def message_template_name(self, message_template_name):
        r"""Sets the message_template_name of this CreateMessageTemplateRequestBody.

        创建模板的名称。只能包含大写字母、小写字母、数字、-和_，且必须由大写字母、小写字母或数字开头，长度在1到64个字符之间。

        :param message_template_name: The message_template_name of this CreateMessageTemplateRequestBody.
        :type message_template_name: str
        """
        self._message_template_name = message_template_name

    @property
    def protocol(self):
        r"""Gets the protocol of this CreateMessageTemplateRequestBody.

        模板支持的协议类型。  目前支持的协议包括：  “default”：默认协议。  “email”：邮件传输协议。  “sms”：短信传输协议。  “functionstage”：FunctionGraph（函数）传输协议。  “http”、“https”：HTTP/HTTPS传输协议。

        :return: The protocol of this CreateMessageTemplateRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this CreateMessageTemplateRequestBody.

        模板支持的协议类型。  目前支持的协议包括：  “default”：默认协议。  “email”：邮件传输协议。  “sms”：短信传输协议。  “functionstage”：FunctionGraph（函数）传输协议。  “http”、“https”：HTTP/HTTPS传输协议。

        :param protocol: The protocol of this CreateMessageTemplateRequestBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def content(self):
        r"""Gets the content of this CreateMessageTemplateRequestBody.

        模板内容，模板目前仅支持纯文本模式。模板内容不能空，最大支持256KB。

        :return: The content of this CreateMessageTemplateRequestBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this CreateMessageTemplateRequestBody.

        模板内容，模板目前仅支持纯文本模式。模板内容不能空，最大支持256KB。

        :param content: The content of this CreateMessageTemplateRequestBody.
        :type content: str
        """
        self._content = content

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
        if not isinstance(other, CreateMessageTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
