# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveEventCallBackConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'live_event_type_callback_url': 'str',
        'auth_type': 'str',
        'key': 'str',
        'callback_event_type': 'list[str]'
    }

    attribute_map = {
        'live_event_type_callback_url': 'live_event_type_callback_url',
        'auth_type': 'auth_type',
        'key': 'key',
        'callback_event_type': 'callback_event_type'
    }

    def __init__(self, live_event_type_callback_url=None, auth_type=None, key=None, callback_event_type=None):
        """LiveEventCallBackConfig

        The model defined in huaweicloud sdk

        :param live_event_type_callback_url: 直播事件回调地址。https地址，需自带鉴权串。
        :type live_event_type_callback_url: str
        :param auth_type: 认证类型。 * NONE。URL中自带认证。 * MSS_A。HMACSHA256签名模式，在URL中追加参数:hwSecret,hwTime。取值方式：hwSecret&#x3D;hmac_sha256(Key, URI（live_event_callback_url）+ hwTime)&amp;hwTime&#x3D;hex(timestamp) * MSS_A_HEAD。HMACSHA256签名模式，参数hwSecret,hwTime放置在Head中。   取值方式：x-hw-mss-secret&#x3D;hmac_sha256(Key, URI（live_event_callback_url）+ hwTime)     x-hw-mss-time&#x3D;hex(timestamp) * MEITUAN_DEFAULT。仅用于美团平台调用回调使用。
        :type auth_type: str
        :param key: 密钥Key
        :type key: str
        :param callback_event_type: 回调的直播事件类型列表。  当前仅支持取值：   SHOOT_SCRIPT_SWITCH，剧本段落切换事件。    RTMP_STREAM_STATE_CHANGE,RTMP链接发生变化回调事件。   REPLY_COMMAND_FINISH,回复播放完成通知 回调事件结构体定义： * event_type: 事件类型。 * message: 事件描述。 SHOOT_SCRIPT_SWITCH事件回调定义如下： &#x60;&#x60;&#x60;json {   \&quot;event_type\&quot;:  \&quot;SHOOT_SCRIPT_SWITCH\&quot;,   \&quot;message\&quot;:\&quot;{\\\&quot;room_id\\\&quot;:\\\&quot;26f065244f754b3aa853b649a21aaf66\\\&quot;,\\\&quot;job_id\\\&quot;:\\\&quot;e87104f76d7546ce8a46ac6b04c49c3c\\\&quot;,\\\&quot;scene_script_name\\\&quot;:\\\&quot;商品1\\\&quot;,\\\&quot;shoot_script_sequence_no\\\&quot;:\\\&quot;2\\\&quot;,\\\&quot;shoot_script_title\\\&quot;:\\\&quot;段落2\\\&quot;}\&quot; } &#x60;&#x60;&#x60; RTMP_STREAM_STATE_CHANGE回调定义如下： &#x60;&#x60;&#x60;json {   \&quot;event_type\&quot;:  \&quot;RTMP_STREAM_STATE_CHANGE\&quot;,   \&quot;message\&quot;:\&quot;{\\\&quot;room_id\\\&quot;:\\\&quot;26f065244f754b3aa853b649a21aaf66\\\&quot;,\\\&quot;job_id\\\&quot;:\\\&quot;e87104f76d7546ce8a46ac6b04c49c3c\\\&quot;,\\\&quot;output_url\\\&quot;:\\\&quot;rtmp://xxx/xx/xx\\\&quot;,\\\&quot;stream_key\\\&quot;:\\\&quot;xxxxx\\\&quot;,\\\&quot;state\\\&quot;:\\\&quot;CONNECTED\\\&quot;}\&quot; } &#x60;&#x60;&#x60; 其中state取值： CONNECTING 链路连接中, CONNECTED 链路已连接，DISCONNECTED 链路已断开，RECONNECTING 链路重连中, END 联络不再重连，链路已结束  REPLY_COMMAND_FINISH回调定义如下： &#x60;&#x60;&#x60;json {   \&quot;event_type\&quot;:  \&quot;REPLY_COMMAND_FINISH\&quot;,   \&quot;message\&quot;:\&quot;{\\\&quot;room_id\\\&quot;:\\\&quot;26f065244f754b3aa853b649a21aaf66\\\&quot;,\\\&quot;job_id\\\&quot;:\\\&quot;e87104f76d7546ce8a46ac6b04c49c3c\\\&quot;,\\\&quot;reply_id\\\&quot;:\\\&quot;e87104f76d7546ce8a46ac6b04c49c3c\&quot;}\&quot; }
        :type callback_event_type: list[str]
        """
        
        

        self._live_event_type_callback_url = None
        self._auth_type = None
        self._key = None
        self._callback_event_type = None
        self.discriminator = None

        if live_event_type_callback_url is not None:
            self.live_event_type_callback_url = live_event_type_callback_url
        if auth_type is not None:
            self.auth_type = auth_type
        if key is not None:
            self.key = key
        if callback_event_type is not None:
            self.callback_event_type = callback_event_type

    @property
    def live_event_type_callback_url(self):
        """Gets the live_event_type_callback_url of this LiveEventCallBackConfig.

        直播事件回调地址。https地址，需自带鉴权串。

        :return: The live_event_type_callback_url of this LiveEventCallBackConfig.
        :rtype: str
        """
        return self._live_event_type_callback_url

    @live_event_type_callback_url.setter
    def live_event_type_callback_url(self, live_event_type_callback_url):
        """Sets the live_event_type_callback_url of this LiveEventCallBackConfig.

        直播事件回调地址。https地址，需自带鉴权串。

        :param live_event_type_callback_url: The live_event_type_callback_url of this LiveEventCallBackConfig.
        :type live_event_type_callback_url: str
        """
        self._live_event_type_callback_url = live_event_type_callback_url

    @property
    def auth_type(self):
        """Gets the auth_type of this LiveEventCallBackConfig.

        认证类型。 * NONE。URL中自带认证。 * MSS_A。HMACSHA256签名模式，在URL中追加参数:hwSecret,hwTime。取值方式：hwSecret=hmac_sha256(Key, URI（live_event_callback_url）+ hwTime)&hwTime=hex(timestamp) * MSS_A_HEAD。HMACSHA256签名模式，参数hwSecret,hwTime放置在Head中。   取值方式：x-hw-mss-secret=hmac_sha256(Key, URI（live_event_callback_url）+ hwTime)     x-hw-mss-time=hex(timestamp) * MEITUAN_DEFAULT。仅用于美团平台调用回调使用。

        :return: The auth_type of this LiveEventCallBackConfig.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this LiveEventCallBackConfig.

        认证类型。 * NONE。URL中自带认证。 * MSS_A。HMACSHA256签名模式，在URL中追加参数:hwSecret,hwTime。取值方式：hwSecret=hmac_sha256(Key, URI（live_event_callback_url）+ hwTime)&hwTime=hex(timestamp) * MSS_A_HEAD。HMACSHA256签名模式，参数hwSecret,hwTime放置在Head中。   取值方式：x-hw-mss-secret=hmac_sha256(Key, URI（live_event_callback_url）+ hwTime)     x-hw-mss-time=hex(timestamp) * MEITUAN_DEFAULT。仅用于美团平台调用回调使用。

        :param auth_type: The auth_type of this LiveEventCallBackConfig.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def key(self):
        """Gets the key of this LiveEventCallBackConfig.

        密钥Key

        :return: The key of this LiveEventCallBackConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LiveEventCallBackConfig.

        密钥Key

        :param key: The key of this LiveEventCallBackConfig.
        :type key: str
        """
        self._key = key

    @property
    def callback_event_type(self):
        """Gets the callback_event_type of this LiveEventCallBackConfig.

        回调的直播事件类型列表。  当前仅支持取值：   SHOOT_SCRIPT_SWITCH，剧本段落切换事件。    RTMP_STREAM_STATE_CHANGE,RTMP链接发生变化回调事件。   REPLY_COMMAND_FINISH,回复播放完成通知 回调事件结构体定义： * event_type: 事件类型。 * message: 事件描述。 SHOOT_SCRIPT_SWITCH事件回调定义如下： ```json {   \"event_type\":  \"SHOOT_SCRIPT_SWITCH\",   \"message\":\"{\\\"room_id\\\":\\\"26f065244f754b3aa853b649a21aaf66\\\",\\\"job_id\\\":\\\"e87104f76d7546ce8a46ac6b04c49c3c\\\",\\\"scene_script_name\\\":\\\"商品1\\\",\\\"shoot_script_sequence_no\\\":\\\"2\\\",\\\"shoot_script_title\\\":\\\"段落2\\\"}\" } ``` RTMP_STREAM_STATE_CHANGE回调定义如下： ```json {   \"event_type\":  \"RTMP_STREAM_STATE_CHANGE\",   \"message\":\"{\\\"room_id\\\":\\\"26f065244f754b3aa853b649a21aaf66\\\",\\\"job_id\\\":\\\"e87104f76d7546ce8a46ac6b04c49c3c\\\",\\\"output_url\\\":\\\"rtmp://xxx/xx/xx\\\",\\\"stream_key\\\":\\\"xxxxx\\\",\\\"state\\\":\\\"CONNECTED\\\"}\" } ``` 其中state取值： CONNECTING 链路连接中, CONNECTED 链路已连接，DISCONNECTED 链路已断开，RECONNECTING 链路重连中, END 联络不再重连，链路已结束  REPLY_COMMAND_FINISH回调定义如下： ```json {   \"event_type\":  \"REPLY_COMMAND_FINISH\",   \"message\":\"{\\\"room_id\\\":\\\"26f065244f754b3aa853b649a21aaf66\\\",\\\"job_id\\\":\\\"e87104f76d7546ce8a46ac6b04c49c3c\\\",\\\"reply_id\\\":\\\"e87104f76d7546ce8a46ac6b04c49c3c\"}\" }

        :return: The callback_event_type of this LiveEventCallBackConfig.
        :rtype: list[str]
        """
        return self._callback_event_type

    @callback_event_type.setter
    def callback_event_type(self, callback_event_type):
        """Sets the callback_event_type of this LiveEventCallBackConfig.

        回调的直播事件类型列表。  当前仅支持取值：   SHOOT_SCRIPT_SWITCH，剧本段落切换事件。    RTMP_STREAM_STATE_CHANGE,RTMP链接发生变化回调事件。   REPLY_COMMAND_FINISH,回复播放完成通知 回调事件结构体定义： * event_type: 事件类型。 * message: 事件描述。 SHOOT_SCRIPT_SWITCH事件回调定义如下： ```json {   \"event_type\":  \"SHOOT_SCRIPT_SWITCH\",   \"message\":\"{\\\"room_id\\\":\\\"26f065244f754b3aa853b649a21aaf66\\\",\\\"job_id\\\":\\\"e87104f76d7546ce8a46ac6b04c49c3c\\\",\\\"scene_script_name\\\":\\\"商品1\\\",\\\"shoot_script_sequence_no\\\":\\\"2\\\",\\\"shoot_script_title\\\":\\\"段落2\\\"}\" } ``` RTMP_STREAM_STATE_CHANGE回调定义如下： ```json {   \"event_type\":  \"RTMP_STREAM_STATE_CHANGE\",   \"message\":\"{\\\"room_id\\\":\\\"26f065244f754b3aa853b649a21aaf66\\\",\\\"job_id\\\":\\\"e87104f76d7546ce8a46ac6b04c49c3c\\\",\\\"output_url\\\":\\\"rtmp://xxx/xx/xx\\\",\\\"stream_key\\\":\\\"xxxxx\\\",\\\"state\\\":\\\"CONNECTED\\\"}\" } ``` 其中state取值： CONNECTING 链路连接中, CONNECTED 链路已连接，DISCONNECTED 链路已断开，RECONNECTING 链路重连中, END 联络不再重连，链路已结束  REPLY_COMMAND_FINISH回调定义如下： ```json {   \"event_type\":  \"REPLY_COMMAND_FINISH\",   \"message\":\"{\\\"room_id\\\":\\\"26f065244f754b3aa853b649a21aaf66\\\",\\\"job_id\\\":\\\"e87104f76d7546ce8a46ac6b04c49c3c\\\",\\\"reply_id\\\":\\\"e87104f76d7546ce8a46ac6b04c49c3c\"}\" }

        :param callback_event_type: The callback_event_type of this LiveEventCallBackConfig.
        :type callback_event_type: list[str]
        """
        self._callback_event_type = callback_event_type

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
        if not isinstance(other, LiveEventCallBackConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
