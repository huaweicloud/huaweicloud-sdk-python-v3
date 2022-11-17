# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishAppMessageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'message_structure': 'str',
        'time_to_live': 'str'
    }

    attribute_map = {
        'message': 'message',
        'message_structure': 'message_structure',
        'time_to_live': 'time_to_live'
    }

    def __init__(self, message=None, message_structure=None, time_to_live=None):
        """PublishAppMessageRequestBody

        The model defined in huaweicloud sdk

        :param message:  message与message_structure二者选其一。  message, App消息发布。  message_structure, 使用消息结构体方式的App消息发布。  app推送的消息内容，当前支持的推送平台有HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。  HMS平台指定的消息内容不超过2K。  APNS和APNS_SANDBOX平台的消息内容不能超过4K。  推送平台的消息内容格式要求详情见application消息体格式。  华为透传消息  {   \&quot;hps\&quot;: {     \&quot;msg\&quot;: {       \&quot;type\&quot;: 1,       \&quot;body\&quot;: {         \&quot;key\&quot;: \&quot;value\&quot;       }     }   } }  华为系统通知栏消息  {   \&quot;hps\&quot;: {     \&quot;msg\&quot;: {       \&quot;type\&quot;: 3,       \&quot;body\&quot;: {         \&quot;content\&quot;: \&quot;Push message content\&quot;,         \&quot;title\&quot;: \&quot;Push message content\&quot;       },       \&quot;action\&quot;: {         \&quot;type\&quot;: 1,         \&quot;param\&quot;: {           \&quot;intent\&quot;: \&quot;#Intent;compo&#x3D;com.rvr/.Activity;S.W&#x3D;U;end\&quot;         }       }     },     \&quot;ext\&quot;: {       \&quot;biTag\&quot;: \&quot;Trump\&quot;,       \&quot;icon\&quot;: \&quot;http://upload.w.org/00/150pxsvg.png\&quot;     }   } }  苹果平台消息格式 {   \&quot;aps\&quot;: {     \&quot;alert\&quot;: \&quot;hello world\&quot;   } }
        :type message: str
        :param message_structure: app推送的消息内容，当前支持的推送平台有HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。  HMS平台指定的消息内容不超过2K。  APNS和APNS_SANDBOX平台的消息内容不能超过4K。  推送平台的消息内容格式要求详情见application消息体格式。  华为透传消息  {   \&quot;HMS\&quot;: {     \&quot;hps\&quot;: {       \&quot;msg\&quot;: {         \&quot;type\&quot;: 1,         \&quot;body\&quot;: {           \&quot;key\&quot;: \&quot;value\&quot;         }       }     }   } }  华为系统通知栏消息  {   \&quot;HMS\&quot;: {     \&quot;hps\&quot;: {       \&quot;msg\&quot;: {         \&quot;type\&quot;: 3,         \&quot;body\&quot;: {           \&quot;content\&quot;: \&quot;Push message content\&quot;,           \&quot;title\&quot;: \&quot;Push message content\&quot;         },         \&quot;action\&quot;: {           \&quot;type\&quot;: 1,           \&quot;param\&quot;: {             \&quot;intent\&quot;: \&quot;#Intent;compo&#x3D;com.rvr/.Activity;S.W&#x3D;U;end\&quot;           }         }       },       \&quot;ext\&quot;: {         \&quot;biTag\&quot;: \&quot;Trump\&quot;,         \&quot;icon\&quot;: \&quot;http://upload.w.org/00/150pxsvg.png\&quot;       }     }   } }  苹果平台消息格式  {   \&quot;APNS\&quot;: {     \&quot;aps\&quot;: {       \&quot;alert\&quot;: \&quot;hello world\&quot;     }   } }
        :type message_structure: str
        :param time_to_live: 消息发送的生存时间，是相对于发布时间的。  SMN系统将移动推送消息转交给推送平台前，会计算该消息在系统消耗的时间。只有消耗的时间小于time_to_live时，SMN才会将消息转交给推送平台，并将time_to_live减去消耗的时间传递给推送平台，否则消息废弃。  time _to_live的单位是s，变量默认值是3600s，即一小时。值为正整数且小于等于3600*24。
        :type time_to_live: str
        """
        
        

        self._message = None
        self._message_structure = None
        self._time_to_live = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if message_structure is not None:
            self.message_structure = message_structure
        if time_to_live is not None:
            self.time_to_live = time_to_live

    @property
    def message(self):
        """Gets the message of this PublishAppMessageRequestBody.

         message与message_structure二者选其一。  message, App消息发布。  message_structure, 使用消息结构体方式的App消息发布。  app推送的消息内容，当前支持的推送平台有HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。  HMS平台指定的消息内容不超过2K。  APNS和APNS_SANDBOX平台的消息内容不能超过4K。  推送平台的消息内容格式要求详情见application消息体格式。  华为透传消息  {   \"hps\": {     \"msg\": {       \"type\": 1,       \"body\": {         \"key\": \"value\"       }     }   } }  华为系统通知栏消息  {   \"hps\": {     \"msg\": {       \"type\": 3,       \"body\": {         \"content\": \"Push message content\",         \"title\": \"Push message content\"       },       \"action\": {         \"type\": 1,         \"param\": {           \"intent\": \"#Intent;compo=com.rvr/.Activity;S.W=U;end\"         }       }     },     \"ext\": {       \"biTag\": \"Trump\",       \"icon\": \"http://upload.w.org/00/150pxsvg.png\"     }   } }  苹果平台消息格式 {   \"aps\": {     \"alert\": \"hello world\"   } }

        :return: The message of this PublishAppMessageRequestBody.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PublishAppMessageRequestBody.

         message与message_structure二者选其一。  message, App消息发布。  message_structure, 使用消息结构体方式的App消息发布。  app推送的消息内容，当前支持的推送平台有HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。  HMS平台指定的消息内容不超过2K。  APNS和APNS_SANDBOX平台的消息内容不能超过4K。  推送平台的消息内容格式要求详情见application消息体格式。  华为透传消息  {   \"hps\": {     \"msg\": {       \"type\": 1,       \"body\": {         \"key\": \"value\"       }     }   } }  华为系统通知栏消息  {   \"hps\": {     \"msg\": {       \"type\": 3,       \"body\": {         \"content\": \"Push message content\",         \"title\": \"Push message content\"       },       \"action\": {         \"type\": 1,         \"param\": {           \"intent\": \"#Intent;compo=com.rvr/.Activity;S.W=U;end\"         }       }     },     \"ext\": {       \"biTag\": \"Trump\",       \"icon\": \"http://upload.w.org/00/150pxsvg.png\"     }   } }  苹果平台消息格式 {   \"aps\": {     \"alert\": \"hello world\"   } }

        :param message: The message of this PublishAppMessageRequestBody.
        :type message: str
        """
        self._message = message

    @property
    def message_structure(self):
        """Gets the message_structure of this PublishAppMessageRequestBody.

        app推送的消息内容，当前支持的推送平台有HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。  HMS平台指定的消息内容不超过2K。  APNS和APNS_SANDBOX平台的消息内容不能超过4K。  推送平台的消息内容格式要求详情见application消息体格式。  华为透传消息  {   \"HMS\": {     \"hps\": {       \"msg\": {         \"type\": 1,         \"body\": {           \"key\": \"value\"         }       }     }   } }  华为系统通知栏消息  {   \"HMS\": {     \"hps\": {       \"msg\": {         \"type\": 3,         \"body\": {           \"content\": \"Push message content\",           \"title\": \"Push message content\"         },         \"action\": {           \"type\": 1,           \"param\": {             \"intent\": \"#Intent;compo=com.rvr/.Activity;S.W=U;end\"           }         }       },       \"ext\": {         \"biTag\": \"Trump\",         \"icon\": \"http://upload.w.org/00/150pxsvg.png\"       }     }   } }  苹果平台消息格式  {   \"APNS\": {     \"aps\": {       \"alert\": \"hello world\"     }   } }

        :return: The message_structure of this PublishAppMessageRequestBody.
        :rtype: str
        """
        return self._message_structure

    @message_structure.setter
    def message_structure(self, message_structure):
        """Sets the message_structure of this PublishAppMessageRequestBody.

        app推送的消息内容，当前支持的推送平台有HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。  HMS平台指定的消息内容不超过2K。  APNS和APNS_SANDBOX平台的消息内容不能超过4K。  推送平台的消息内容格式要求详情见application消息体格式。  华为透传消息  {   \"HMS\": {     \"hps\": {       \"msg\": {         \"type\": 1,         \"body\": {           \"key\": \"value\"         }       }     }   } }  华为系统通知栏消息  {   \"HMS\": {     \"hps\": {       \"msg\": {         \"type\": 3,         \"body\": {           \"content\": \"Push message content\",           \"title\": \"Push message content\"         },         \"action\": {           \"type\": 1,           \"param\": {             \"intent\": \"#Intent;compo=com.rvr/.Activity;S.W=U;end\"           }         }       },       \"ext\": {         \"biTag\": \"Trump\",         \"icon\": \"http://upload.w.org/00/150pxsvg.png\"       }     }   } }  苹果平台消息格式  {   \"APNS\": {     \"aps\": {       \"alert\": \"hello world\"     }   } }

        :param message_structure: The message_structure of this PublishAppMessageRequestBody.
        :type message_structure: str
        """
        self._message_structure = message_structure

    @property
    def time_to_live(self):
        """Gets the time_to_live of this PublishAppMessageRequestBody.

        消息发送的生存时间，是相对于发布时间的。  SMN系统将移动推送消息转交给推送平台前，会计算该消息在系统消耗的时间。只有消耗的时间小于time_to_live时，SMN才会将消息转交给推送平台，并将time_to_live减去消耗的时间传递给推送平台，否则消息废弃。  time _to_live的单位是s，变量默认值是3600s，即一小时。值为正整数且小于等于3600*24。

        :return: The time_to_live of this PublishAppMessageRequestBody.
        :rtype: str
        """
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        """Sets the time_to_live of this PublishAppMessageRequestBody.

        消息发送的生存时间，是相对于发布时间的。  SMN系统将移动推送消息转交给推送平台前，会计算该消息在系统消耗的时间。只有消耗的时间小于time_to_live时，SMN才会将消息转交给推送平台，并将time_to_live减去消耗的时间传递给推送平台，否则消息废弃。  time _to_live的单位是s，变量默认值是3600s，即一小时。值为正整数且小于等于3600*24。

        :param time_to_live: The time_to_live of this PublishAppMessageRequestBody.
        :type time_to_live: str
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
        if not isinstance(other, PublishAppMessageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
