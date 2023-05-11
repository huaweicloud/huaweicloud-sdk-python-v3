# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BroadcastMessageResponse(SdkResponse):

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
        'message_id': 'str',
        'created_time': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'topic_full_name': 'topic_full_name',
        'message_id': 'message_id',
        'created_time': 'created_time'
    }

    def __init__(self, app_id=None, topic_full_name=None, message_id=None, created_time=None):
        """BroadcastMessageResponse

        The model defined in huaweicloud sdk

        :param app_id: **参数说明**：资源空间ID。
        :type app_id: str
        :param topic_full_name: **参数说明**：接收广播消息的完整Topic名称
        :type topic_full_name: str
        :param message_id: 消息id，由物联网平台生成，用于标识该消息。
        :type message_id: str
        :param created_time: 消息的创建时间，\&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;格式的UTC字符串。
        :type created_time: str
        """
        
        super(BroadcastMessageResponse, self).__init__()

        self._app_id = None
        self._topic_full_name = None
        self._message_id = None
        self._created_time = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if topic_full_name is not None:
            self.topic_full_name = topic_full_name
        if message_id is not None:
            self.message_id = message_id
        if created_time is not None:
            self.created_time = created_time

    @property
    def app_id(self):
        """Gets the app_id of this BroadcastMessageResponse.

        **参数说明**：资源空间ID。

        :return: The app_id of this BroadcastMessageResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this BroadcastMessageResponse.

        **参数说明**：资源空间ID。

        :param app_id: The app_id of this BroadcastMessageResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def topic_full_name(self):
        """Gets the topic_full_name of this BroadcastMessageResponse.

        **参数说明**：接收广播消息的完整Topic名称

        :return: The topic_full_name of this BroadcastMessageResponse.
        :rtype: str
        """
        return self._topic_full_name

    @topic_full_name.setter
    def topic_full_name(self, topic_full_name):
        """Sets the topic_full_name of this BroadcastMessageResponse.

        **参数说明**：接收广播消息的完整Topic名称

        :param topic_full_name: The topic_full_name of this BroadcastMessageResponse.
        :type topic_full_name: str
        """
        self._topic_full_name = topic_full_name

    @property
    def message_id(self):
        """Gets the message_id of this BroadcastMessageResponse.

        消息id，由物联网平台生成，用于标识该消息。

        :return: The message_id of this BroadcastMessageResponse.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this BroadcastMessageResponse.

        消息id，由物联网平台生成，用于标识该消息。

        :param message_id: The message_id of this BroadcastMessageResponse.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def created_time(self):
        """Gets the created_time of this BroadcastMessageResponse.

        消息的创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :return: The created_time of this BroadcastMessageResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this BroadcastMessageResponse.

        消息的创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :param created_time: The created_time of this BroadcastMessageResponse.
        :type created_time: str
        """
        self._created_time = created_time

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
        if not isinstance(other, BroadcastMessageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
