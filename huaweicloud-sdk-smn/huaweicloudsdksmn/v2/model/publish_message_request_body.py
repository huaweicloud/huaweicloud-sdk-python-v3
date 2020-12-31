# coding: utf-8

import pprint
import re

import six





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
        'time_to_live': 'str'
    }

    attribute_map = {
        'subject': 'subject',
        'message': 'message',
        'message_structure': 'message_structure',
        'message_template_name': 'message_template_name',
        'tags': 'tags',
        'time_to_live': 'time_to_live'
    }

    def __init__(self, subject=None, message=None, message_structure=None, message_template_name=None, tags=None, time_to_live=None):
        """PublishMessageRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._subject = None
        self._message = None
        self._message_structure = None
        self._message_template_name = None
        self._tags = None
        self._time_to_live = None
        self.discriminator = None

        self.subject = subject
        if message is not None:
            self.message = message
        if message_structure is not None:
            self.message_structure = message_structure
        if message_template_name is not None:
            self.message_template_name = message_template_name
        if tags is not None:
            self.tags = tags
        self.time_to_live = time_to_live

    @property
    def subject(self):
        """Gets the subject of this PublishMessageRequestBody.

        消息标题，给邮箱订阅者发送邮件时作为邮件主题，长度不能超过512个字符。

        :return: The subject of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PublishMessageRequestBody.

        消息标题，给邮箱订阅者发送邮件时作为邮件主题，长度不能超过512个字符。

        :param subject: The subject of this PublishMessageRequestBody.
        :type: str
        """
        self._subject = subject

    @property
    def message(self):
        """Gets the message of this PublishMessageRequestBody.

        发送的消息。消息体必须是UTF-8编码的字符串，大小至多256KB。如果订阅者是手机号码，长度不超过490个字符，超出部分系统自动截断。短信内容不能包含“[]”或者“【】”符号。  对于移动推送订阅者推送消息，message消息必须符合移动推送平台的消息格式，消息格式请参见application消息体格式。否则移动app无法收到消息，目前支持的平台有HMS、APNS、APNS_SANDBOX。

        :return: The message of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PublishMessageRequestBody.

        发送的消息。消息体必须是UTF-8编码的字符串，大小至多256KB。如果订阅者是手机号码，长度不超过490个字符，超出部分系统自动截断。短信内容不能包含“[]”或者“【】”符号。  对于移动推送订阅者推送消息，message消息必须符合移动推送平台的消息格式，消息格式请参见application消息体格式。否则移动app无法收到消息，目前支持的平台有HMS、APNS、APNS_SANDBOX。

        :param message: The message of this PublishMessageRequestBody.
        :type: str
        """
        self._message = message

    @property
    def message_structure(self):
        """Gets the message_structure of this PublishMessageRequestBody.

        Json格式的字符串。支持“email”、“sms”、 “http”、“https”、“dms”、“functiongraph”、“functionstage”、“HMS”、“APNS”以及“APNS_SANDBOX”。其中，“HMS”、“APNS”以及“APNS_SANDBOX”三种消息的格式请参见application消息体格式。必须设置默认的消息“default”，当匹配不到消息协议时，按“default”中的内容发送。  说明： 三种消息发送方式  message  message_structure  message_template_name  只需要设置其中一个，如果同时设置，生效的优先级为 message_structure > message_template_name > message。  华为透传消息  {   \"hps\": {     \"msg\": {       \"type\": 1,       \"body\": {         \"key\": \"value\"       }     }   } }  华为系统通知栏消息  {   \"hps\": {     \"msg\": {       \"type\": 3,       \"body\": {         \"content\": \"Push message content\",         \"title\": \"Push message content\"       },       \"action\": {         \"type\": 1,         \"param\": {           \"intent\": \"#Intent;compo=com.rvr/.Activity;S.W=U;end\"         }       }     },     \"ext\": {       \"biTag\": \"Trump\",       \"icon\": \"http://upload.w.org/00/150pxsvg.png\"     }   } }  苹果平台消息格式  {   \"aps\": {     \"alert\": \"hello world\"   } }

        :return: The message_structure of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._message_structure

    @message_structure.setter
    def message_structure(self, message_structure):
        """Sets the message_structure of this PublishMessageRequestBody.

        Json格式的字符串。支持“email”、“sms”、 “http”、“https”、“dms”、“functiongraph”、“functionstage”、“HMS”、“APNS”以及“APNS_SANDBOX”。其中，“HMS”、“APNS”以及“APNS_SANDBOX”三种消息的格式请参见application消息体格式。必须设置默认的消息“default”，当匹配不到消息协议时，按“default”中的内容发送。  说明： 三种消息发送方式  message  message_structure  message_template_name  只需要设置其中一个，如果同时设置，生效的优先级为 message_structure > message_template_name > message。  华为透传消息  {   \"hps\": {     \"msg\": {       \"type\": 1,       \"body\": {         \"key\": \"value\"       }     }   } }  华为系统通知栏消息  {   \"hps\": {     \"msg\": {       \"type\": 3,       \"body\": {         \"content\": \"Push message content\",         \"title\": \"Push message content\"       },       \"action\": {         \"type\": 1,         \"param\": {           \"intent\": \"#Intent;compo=com.rvr/.Activity;S.W=U;end\"         }       }     },     \"ext\": {       \"biTag\": \"Trump\",       \"icon\": \"http://upload.w.org/00/150pxsvg.png\"     }   } }  苹果平台消息格式  {   \"aps\": {     \"alert\": \"hello world\"   } }

        :param message_structure: The message_structure of this PublishMessageRequestBody.
        :type: str
        """
        self._message_structure = message_structure

    @property
    def message_template_name(self):
        """Gets the message_template_name of this PublishMessageRequestBody.

        消息模板名称，可通过[查询消息模板列表](https://support.huaweicloud.com/api-smn/smn_api_53004.html)获取名称。  说明： 三种消息发送方式:  message  message_structure  message_template_name  只需要设置其中一个，如果同时设置，生效的优先级为 message_structure > message_template_name > message。

        :return: The message_template_name of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._message_template_name

    @message_template_name.setter
    def message_template_name(self, message_template_name):
        """Sets the message_template_name of this PublishMessageRequestBody.

        消息模板名称，可通过[查询消息模板列表](https://support.huaweicloud.com/api-smn/smn_api_53004.html)获取名称。  说明： 三种消息发送方式:  message  message_structure  message_template_name  只需要设置其中一个，如果同时设置，生效的优先级为 message_structure > message_template_name > message。

        :param message_template_name: The message_template_name of this PublishMessageRequestBody.
        :type: str
        """
        self._message_template_name = message_template_name

    @property
    def tags(self):
        """Gets the tags of this PublishMessageRequestBody.

        tag以及替换tag的参数组成的字典。消息模板中的标签对应的值。使用消息模板方式的消息发布必须携带该参数。字典中的key为消息模板中的参数名称，不超过21个字符。字典中的value为消息模板中的参数被替换后的值，不超过1KB。

        :return: The tags of this PublishMessageRequestBody.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PublishMessageRequestBody.

        tag以及替换tag的参数组成的字典。消息模板中的标签对应的值。使用消息模板方式的消息发布必须携带该参数。字典中的key为消息模板中的参数名称，不超过21个字符。字典中的value为消息模板中的参数被替换后的值，不超过1KB。

        :param tags: The tags of this PublishMessageRequestBody.
        :type: dict(str, str)
        """
        self._tags = tags

    @property
    def time_to_live(self):
        """Gets the time_to_live of this PublishMessageRequestBody.

        指消息在SMN系统内部的最长存留时间。超过该存留时间，系统将不再发送该消息。单位是s，变量默认值是3600s，即一小时。值为正整数且小于等于3600*24。

        :return: The time_to_live of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        """Sets the time_to_live of this PublishMessageRequestBody.

        指消息在SMN系统内部的最长存留时间。超过该存留时间，系统将不再发送该消息。单位是s，变量默认值是3600s，即一小时。值为正整数且小于等于3600*24。

        :param time_to_live: The time_to_live of this PublishMessageRequestBody.
        :type: str
        """
        self._time_to_live = time_to_live

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublishMessageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
