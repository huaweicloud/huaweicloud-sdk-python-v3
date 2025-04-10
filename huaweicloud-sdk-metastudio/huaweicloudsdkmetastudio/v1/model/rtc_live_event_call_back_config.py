# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RTCLiveEventCallBackConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rtc_callback_event_type': 'list[str]'
    }

    attribute_map = {
        'rtc_callback_event_type': 'rtc_callback_event_type'
    }

    def __init__(self, rtc_callback_event_type=None):
        r"""RTCLiveEventCallBackConfig

        The model defined in huaweicloud sdk

        :param rtc_callback_event_type: RTC回调的直播事件类型列表。  当前仅支持如下取值： * LIVE_PROGRESS：直播剧本进度通知。  * REPLY_COMMAND_FINISH：回复播放完成通知。  回调事件结构体定义： * message_type：消息类型。 * data：消息描述。   - LIVE_PROGRESS事件回调定义如下：     &#x60;&#x60;&#x60;json     {         \&quot;message_type\&quot;: \&quot;live_progress_notify\&quot;,         \&quot;data\&quot;: {             \&quot;script_name\&quot;: \&quot;场景一\&quot;,             \&quot;shoot_script_sequence_no\&quot;: 2,             \&quot;shoot_script_title\&quot;: \&quot;引导语\&quot;,             \&quot;offset\&quot;: \&quot;247\&quot;,             \&quot;reply_id\&quot;: \&quot;e87104f76d7546ce8a46ac6b04c49c3c\&quot;         }     }     &#x60;&#x60;&#x60;   - REPLY_COMMAND_FINISH回调定义如下：     &#x60;&#x60;&#x60;json     {       \&quot;message_type\&quot;: \&quot;reply_command_finish_notify\&quot;,       \&quot;data\&quot;:\&quot;{         \&quot;reply_id\&quot;:\&quot;e87104f76d7546ce8a46ac6b04c49c3c\&quot;       }\&quot;     }     &#x60;&#x60;&#x60;
        :type rtc_callback_event_type: list[str]
        """
        
        

        self._rtc_callback_event_type = None
        self.discriminator = None

        if rtc_callback_event_type is not None:
            self.rtc_callback_event_type = rtc_callback_event_type

    @property
    def rtc_callback_event_type(self):
        r"""Gets the rtc_callback_event_type of this RTCLiveEventCallBackConfig.

        RTC回调的直播事件类型列表。  当前仅支持如下取值： * LIVE_PROGRESS：直播剧本进度通知。  * REPLY_COMMAND_FINISH：回复播放完成通知。  回调事件结构体定义： * message_type：消息类型。 * data：消息描述。   - LIVE_PROGRESS事件回调定义如下：     ```json     {         \"message_type\": \"live_progress_notify\",         \"data\": {             \"script_name\": \"场景一\",             \"shoot_script_sequence_no\": 2,             \"shoot_script_title\": \"引导语\",             \"offset\": \"247\",             \"reply_id\": \"e87104f76d7546ce8a46ac6b04c49c3c\"         }     }     ```   - REPLY_COMMAND_FINISH回调定义如下：     ```json     {       \"message_type\": \"reply_command_finish_notify\",       \"data\":\"{         \"reply_id\":\"e87104f76d7546ce8a46ac6b04c49c3c\"       }\"     }     ```

        :return: The rtc_callback_event_type of this RTCLiveEventCallBackConfig.
        :rtype: list[str]
        """
        return self._rtc_callback_event_type

    @rtc_callback_event_type.setter
    def rtc_callback_event_type(self, rtc_callback_event_type):
        r"""Sets the rtc_callback_event_type of this RTCLiveEventCallBackConfig.

        RTC回调的直播事件类型列表。  当前仅支持如下取值： * LIVE_PROGRESS：直播剧本进度通知。  * REPLY_COMMAND_FINISH：回复播放完成通知。  回调事件结构体定义： * message_type：消息类型。 * data：消息描述。   - LIVE_PROGRESS事件回调定义如下：     ```json     {         \"message_type\": \"live_progress_notify\",         \"data\": {             \"script_name\": \"场景一\",             \"shoot_script_sequence_no\": 2,             \"shoot_script_title\": \"引导语\",             \"offset\": \"247\",             \"reply_id\": \"e87104f76d7546ce8a46ac6b04c49c3c\"         }     }     ```   - REPLY_COMMAND_FINISH回调定义如下：     ```json     {       \"message_type\": \"reply_command_finish_notify\",       \"data\":\"{         \"reply_id\":\"e87104f76d7546ce8a46ac6b04c49c3c\"       }\"     }     ```

        :param rtc_callback_event_type: The rtc_callback_event_type of this RTCLiveEventCallBackConfig.
        :type rtc_callback_event_type: list[str]
        """
        self._rtc_callback_event_type = rtc_callback_event_type

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
        if not isinstance(other, RTCLiveEventCallBackConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
