# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishMessageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subject': 'str',
        'message': 'str',
        'message_structure': 'str',
        'message_template_name': 'str',
        'tags': 'dict(str, str)',
        'time_to_live': 'str',
        'message_attributes': 'list[MessageAttribute]',
        'locale': 'str'
    }

    attribute_map = {
        'subject': 'subject',
        'message': 'message',
        'message_structure': 'message_structure',
        'message_template_name': 'message_template_name',
        'tags': 'tags',
        'time_to_live': 'time_to_live',
        'message_attributes': 'message_attributes',
        'locale': 'locale'
    }

    def __init__(self, subject=None, message=None, message_structure=None, message_template_name=None, tags=None, time_to_live=None, message_attributes=None, locale=None):
        r"""PublishMessageRequestBody

        The model defined in huaweicloud sdk

        :param subject: 消息标题，给邮箱订阅者发送邮件时作为邮件主题，长度不能超过512个字节。
        :type subject: str
        :param message: 发送的消息。消息体必须是UTF-8编码的字符串，大小至多256KB。如果订阅者是手机号码，短信长度限制为490字，超出则可能被运营商拦截。短信内容不能包含“[]”或者“【】”符号。 说明： 三种消息发送方式：message、message_structure、message_template_name  至少设置其中一个，如果同时设置，生效的优先级为 message_structure &gt; message_template_name &gt; message。
        :type message: str
        :param message_structure: Json格式的字符串。支持“email”、“sms”、“http”、“https”、“functiongraph”、“functionstage”、“dingding”、“wechat”、“feishu”、“welink”、“dingTalkBot”。必须设置默认的消息“default”，当匹配不到消息协议时，按“default”中的内容发送。  - 其中，钉钉、微信、飞书、welink、dingTalkBot协议类型的消息需指定msgType字段；钉钉，微信和飞书机器人协议支持msgType为text（纯文本）和markdown（MD）格式消息，welink机器人类型暂仅支持msgType为text的纯文本消息。   - 企业微信机器人对消息长度的限制请参考[官方文档](https://developer.work.weixin.qq.com/document/path/91770)。  - 钉钉机器人协议支持通过at字段实现@群组成员。当您需要@群成员时，可以在isAtAll字段中传入布尔值，表示是否需要@群组内所有人。您可以在atMobiles字段中传入需要@的人的手机号列表，或在atUserIds字段中传入需要@的钉钉userID列表。当您使用atMobiles字段或atUserIds字段时，需要在消息内容中同时传入@对应手机号或userID的信息。展示效果请参考钉钉[官方文档](https://open.dingtalk.com/document/orgapp/custom-robots-send-group-messages)。钉钉群机器人消息限制在20000bytes以内，详情请参考[钉钉官方文档](https://open.dingtalk.com/document/orgapp/custom-robot-access)描述。  - 飞书机器人协议的markdown消息支持通过传入color字段设置标题的底色。能够支持的color字段可参考飞书[官方文档](https://open.feishu.cn/document/common-capabilities/message-card/message-cards-content/card-header)。飞书群机器人消息限制在30KB以内，详情请参考[飞书官方文档](https://feishu.apifox.cn/doc-1944903)描述。   - 个人钉钉消息对长度的限制请参考[官方文档](https://open.dingtalk.com/document/orgapp/the-robot-sends-a-group-message)。  说明： 三种消息发送方式：message、message_structure、message_template_name  至少设置其中一个，如果同时设置，生效的优先级为 message_structure &gt; message_template_name &gt; message。
        :type message_structure: str
        :param message_template_name: 消息模板名称，可通过[查询消息模板列表](ListMessageTemplates.xml)获取名称。  说明： 三种消息发送方式：message、message_structure、message_template_name  至少设置其中一个，如果同时设置，生效的优先级为 message_structure &gt; message_template_name &gt; message。
        :type message_template_name: str
        :param tags: tag以及替换tag的参数组成的字典。消息模板中的标签对应的值。使用消息模板方式的消息发布必须携带该参数。字典中的key为消息模板中的参数名称，不超过21个字符。字典中的value为消息模板中的参数被替换后的值，不超过1KB。
        :type tags: dict(str, str)
        :param time_to_live: 指消息在SMN系统内部的最长存留时间。超过该存留时间，系统将不再发送该消息。单位是s，变量默认值是3600s，即一小时。值为正整数且小于等于3600*24。
        :type time_to_live: str
        :param message_attributes: 消息属性列表
        :type message_attributes: list[:class:`huaweicloudsdksmn.v2.MessageAttribute`]
        :param locale: 语言，发送出去的消息中SMN附加系统内容的语言，若没传入，使用账号的语言。取值范围是该局点支持的语言，比如：zh-cn,en-us等
        :type locale: str
        """
        
        

        self._subject = None
        self._message = None
        self._message_structure = None
        self._message_template_name = None
        self._tags = None
        self._time_to_live = None
        self._message_attributes = None
        self._locale = None
        self.discriminator = None

        if subject is not None:
            self.subject = subject
        if message is not None:
            self.message = message
        if message_structure is not None:
            self.message_structure = message_structure
        if message_template_name is not None:
            self.message_template_name = message_template_name
        if tags is not None:
            self.tags = tags
        if time_to_live is not None:
            self.time_to_live = time_to_live
        if message_attributes is not None:
            self.message_attributes = message_attributes
        if locale is not None:
            self.locale = locale

    @property
    def subject(self):
        r"""Gets the subject of this PublishMessageRequestBody.

        消息标题，给邮箱订阅者发送邮件时作为邮件主题，长度不能超过512个字节。

        :return: The subject of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this PublishMessageRequestBody.

        消息标题，给邮箱订阅者发送邮件时作为邮件主题，长度不能超过512个字节。

        :param subject: The subject of this PublishMessageRequestBody.
        :type subject: str
        """
        self._subject = subject

    @property
    def message(self):
        r"""Gets the message of this PublishMessageRequestBody.

        发送的消息。消息体必须是UTF-8编码的字符串，大小至多256KB。如果订阅者是手机号码，短信长度限制为490字，超出则可能被运营商拦截。短信内容不能包含“[]”或者“【】”符号。 说明： 三种消息发送方式：message、message_structure、message_template_name  至少设置其中一个，如果同时设置，生效的优先级为 message_structure > message_template_name > message。

        :return: The message of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this PublishMessageRequestBody.

        发送的消息。消息体必须是UTF-8编码的字符串，大小至多256KB。如果订阅者是手机号码，短信长度限制为490字，超出则可能被运营商拦截。短信内容不能包含“[]”或者“【】”符号。 说明： 三种消息发送方式：message、message_structure、message_template_name  至少设置其中一个，如果同时设置，生效的优先级为 message_structure > message_template_name > message。

        :param message: The message of this PublishMessageRequestBody.
        :type message: str
        """
        self._message = message

    @property
    def message_structure(self):
        r"""Gets the message_structure of this PublishMessageRequestBody.

        Json格式的字符串。支持“email”、“sms”、“http”、“https”、“functiongraph”、“functionstage”、“dingding”、“wechat”、“feishu”、“welink”、“dingTalkBot”。必须设置默认的消息“default”，当匹配不到消息协议时，按“default”中的内容发送。  - 其中，钉钉、微信、飞书、welink、dingTalkBot协议类型的消息需指定msgType字段；钉钉，微信和飞书机器人协议支持msgType为text（纯文本）和markdown（MD）格式消息，welink机器人类型暂仅支持msgType为text的纯文本消息。   - 企业微信机器人对消息长度的限制请参考[官方文档](https://developer.work.weixin.qq.com/document/path/91770)。  - 钉钉机器人协议支持通过at字段实现@群组成员。当您需要@群成员时，可以在isAtAll字段中传入布尔值，表示是否需要@群组内所有人。您可以在atMobiles字段中传入需要@的人的手机号列表，或在atUserIds字段中传入需要@的钉钉userID列表。当您使用atMobiles字段或atUserIds字段时，需要在消息内容中同时传入@对应手机号或userID的信息。展示效果请参考钉钉[官方文档](https://open.dingtalk.com/document/orgapp/custom-robots-send-group-messages)。钉钉群机器人消息限制在20000bytes以内，详情请参考[钉钉官方文档](https://open.dingtalk.com/document/orgapp/custom-robot-access)描述。  - 飞书机器人协议的markdown消息支持通过传入color字段设置标题的底色。能够支持的color字段可参考飞书[官方文档](https://open.feishu.cn/document/common-capabilities/message-card/message-cards-content/card-header)。飞书群机器人消息限制在30KB以内，详情请参考[飞书官方文档](https://feishu.apifox.cn/doc-1944903)描述。   - 个人钉钉消息对长度的限制请参考[官方文档](https://open.dingtalk.com/document/orgapp/the-robot-sends-a-group-message)。  说明： 三种消息发送方式：message、message_structure、message_template_name  至少设置其中一个，如果同时设置，生效的优先级为 message_structure > message_template_name > message。

        :return: The message_structure of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._message_structure

    @message_structure.setter
    def message_structure(self, message_structure):
        r"""Sets the message_structure of this PublishMessageRequestBody.

        Json格式的字符串。支持“email”、“sms”、“http”、“https”、“functiongraph”、“functionstage”、“dingding”、“wechat”、“feishu”、“welink”、“dingTalkBot”。必须设置默认的消息“default”，当匹配不到消息协议时，按“default”中的内容发送。  - 其中，钉钉、微信、飞书、welink、dingTalkBot协议类型的消息需指定msgType字段；钉钉，微信和飞书机器人协议支持msgType为text（纯文本）和markdown（MD）格式消息，welink机器人类型暂仅支持msgType为text的纯文本消息。   - 企业微信机器人对消息长度的限制请参考[官方文档](https://developer.work.weixin.qq.com/document/path/91770)。  - 钉钉机器人协议支持通过at字段实现@群组成员。当您需要@群成员时，可以在isAtAll字段中传入布尔值，表示是否需要@群组内所有人。您可以在atMobiles字段中传入需要@的人的手机号列表，或在atUserIds字段中传入需要@的钉钉userID列表。当您使用atMobiles字段或atUserIds字段时，需要在消息内容中同时传入@对应手机号或userID的信息。展示效果请参考钉钉[官方文档](https://open.dingtalk.com/document/orgapp/custom-robots-send-group-messages)。钉钉群机器人消息限制在20000bytes以内，详情请参考[钉钉官方文档](https://open.dingtalk.com/document/orgapp/custom-robot-access)描述。  - 飞书机器人协议的markdown消息支持通过传入color字段设置标题的底色。能够支持的color字段可参考飞书[官方文档](https://open.feishu.cn/document/common-capabilities/message-card/message-cards-content/card-header)。飞书群机器人消息限制在30KB以内，详情请参考[飞书官方文档](https://feishu.apifox.cn/doc-1944903)描述。   - 个人钉钉消息对长度的限制请参考[官方文档](https://open.dingtalk.com/document/orgapp/the-robot-sends-a-group-message)。  说明： 三种消息发送方式：message、message_structure、message_template_name  至少设置其中一个，如果同时设置，生效的优先级为 message_structure > message_template_name > message。

        :param message_structure: The message_structure of this PublishMessageRequestBody.
        :type message_structure: str
        """
        self._message_structure = message_structure

    @property
    def message_template_name(self):
        r"""Gets the message_template_name of this PublishMessageRequestBody.

        消息模板名称，可通过[查询消息模板列表](ListMessageTemplates.xml)获取名称。  说明： 三种消息发送方式：message、message_structure、message_template_name  至少设置其中一个，如果同时设置，生效的优先级为 message_structure > message_template_name > message。

        :return: The message_template_name of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._message_template_name

    @message_template_name.setter
    def message_template_name(self, message_template_name):
        r"""Sets the message_template_name of this PublishMessageRequestBody.

        消息模板名称，可通过[查询消息模板列表](ListMessageTemplates.xml)获取名称。  说明： 三种消息发送方式：message、message_structure、message_template_name  至少设置其中一个，如果同时设置，生效的优先级为 message_structure > message_template_name > message。

        :param message_template_name: The message_template_name of this PublishMessageRequestBody.
        :type message_template_name: str
        """
        self._message_template_name = message_template_name

    @property
    def tags(self):
        r"""Gets the tags of this PublishMessageRequestBody.

        tag以及替换tag的参数组成的字典。消息模板中的标签对应的值。使用消息模板方式的消息发布必须携带该参数。字典中的key为消息模板中的参数名称，不超过21个字符。字典中的value为消息模板中的参数被替换后的值，不超过1KB。

        :return: The tags of this PublishMessageRequestBody.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this PublishMessageRequestBody.

        tag以及替换tag的参数组成的字典。消息模板中的标签对应的值。使用消息模板方式的消息发布必须携带该参数。字典中的key为消息模板中的参数名称，不超过21个字符。字典中的value为消息模板中的参数被替换后的值，不超过1KB。

        :param tags: The tags of this PublishMessageRequestBody.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def time_to_live(self):
        r"""Gets the time_to_live of this PublishMessageRequestBody.

        指消息在SMN系统内部的最长存留时间。超过该存留时间，系统将不再发送该消息。单位是s，变量默认值是3600s，即一小时。值为正整数且小于等于3600*24。

        :return: The time_to_live of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        r"""Sets the time_to_live of this PublishMessageRequestBody.

        指消息在SMN系统内部的最长存留时间。超过该存留时间，系统将不再发送该消息。单位是s，变量默认值是3600s，即一小时。值为正整数且小于等于3600*24。

        :param time_to_live: The time_to_live of this PublishMessageRequestBody.
        :type time_to_live: str
        """
        self._time_to_live = time_to_live

    @property
    def message_attributes(self):
        r"""Gets the message_attributes of this PublishMessageRequestBody.

        消息属性列表

        :return: The message_attributes of this PublishMessageRequestBody.
        :rtype: list[:class:`huaweicloudsdksmn.v2.MessageAttribute`]
        """
        return self._message_attributes

    @message_attributes.setter
    def message_attributes(self, message_attributes):
        r"""Sets the message_attributes of this PublishMessageRequestBody.

        消息属性列表

        :param message_attributes: The message_attributes of this PublishMessageRequestBody.
        :type message_attributes: list[:class:`huaweicloudsdksmn.v2.MessageAttribute`]
        """
        self._message_attributes = message_attributes

    @property
    def locale(self):
        r"""Gets the locale of this PublishMessageRequestBody.

        语言，发送出去的消息中SMN附加系统内容的语言，若没传入，使用账号的语言。取值范围是该局点支持的语言，比如：zh-cn,en-us等

        :return: The locale of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this PublishMessageRequestBody.

        语言，发送出去的消息中SMN附加系统内容的语言，若没传入，使用账号的语言。取值范围是该局点支持的语言，比如：zh-cn,en-us等

        :param locale: The locale of this PublishMessageRequestBody.
        :type locale: str
        """
        self._locale = locale

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
        if not isinstance(other, PublishMessageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
