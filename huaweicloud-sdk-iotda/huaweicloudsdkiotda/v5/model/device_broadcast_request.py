# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceBroadcastRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'topic_full_name': 'str',
        'message': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'topic_full_name': 'topic_full_name',
        'message': 'message'
    }

    def __init__(self, app_id=None, topic_full_name=None, message=None):
        """DeviceBroadcastRequest

        The model defined in huaweicloud sdk

        :param app_id: **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定广播消息所属的资源空间，否则广播消息将会向[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下订阅指定topic的设备发送。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        :param topic_full_name: **参数说明**：接收广播消息的完整Topic名称, 必选。用户需要发布广播消息给设备时，可以使用该参数指定完整的topic名称，物联网平台会向指定资源空间下订阅了该topic的所有在线设备发送消息。广播的topic无需控制台创建，但topic的前缀必须为$oc/broadcast/
        :type topic_full_name: str
        :param message: **参数说明**：广播消息的内容，您需要将消息原文转换成二进制数据并进行Base64编码，Base64编码后的长度不超过128KB。
        :type message: str
        """
        
        

        self._app_id = None
        self._topic_full_name = None
        self._message = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        self.topic_full_name = topic_full_name
        self.message = message

    @property
    def app_id(self):
        """Gets the app_id of this DeviceBroadcastRequest.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定广播消息所属的资源空间，否则广播消息将会向[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下订阅指定topic的设备发送。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this DeviceBroadcastRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this DeviceBroadcastRequest.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定广播消息所属的资源空间，否则广播消息将会向[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下订阅指定topic的设备发送。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this DeviceBroadcastRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def topic_full_name(self):
        """Gets the topic_full_name of this DeviceBroadcastRequest.

        **参数说明**：接收广播消息的完整Topic名称, 必选。用户需要发布广播消息给设备时，可以使用该参数指定完整的topic名称，物联网平台会向指定资源空间下订阅了该topic的所有在线设备发送消息。广播的topic无需控制台创建，但topic的前缀必须为$oc/broadcast/

        :return: The topic_full_name of this DeviceBroadcastRequest.
        :rtype: str
        """
        return self._topic_full_name

    @topic_full_name.setter
    def topic_full_name(self, topic_full_name):
        """Sets the topic_full_name of this DeviceBroadcastRequest.

        **参数说明**：接收广播消息的完整Topic名称, 必选。用户需要发布广播消息给设备时，可以使用该参数指定完整的topic名称，物联网平台会向指定资源空间下订阅了该topic的所有在线设备发送消息。广播的topic无需控制台创建，但topic的前缀必须为$oc/broadcast/

        :param topic_full_name: The topic_full_name of this DeviceBroadcastRequest.
        :type topic_full_name: str
        """
        self._topic_full_name = topic_full_name

    @property
    def message(self):
        """Gets the message of this DeviceBroadcastRequest.

        **参数说明**：广播消息的内容，您需要将消息原文转换成二进制数据并进行Base64编码，Base64编码后的长度不超过128KB。

        :return: The message of this DeviceBroadcastRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DeviceBroadcastRequest.

        **参数说明**：广播消息的内容，您需要将消息原文转换成二进制数据并进行Base64编码，Base64编码后的长度不超过128KB。

        :param message: The message of this DeviceBroadcastRequest.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, DeviceBroadcastRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
