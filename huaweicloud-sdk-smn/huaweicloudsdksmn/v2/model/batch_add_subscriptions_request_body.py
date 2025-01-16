# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddSubscriptionsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'endpoint': 'str',
        'remark': 'str',
        'extension': 'SubscriptionExtension'
    }

    attribute_map = {
        'protocol': 'protocol',
        'endpoint': 'endpoint',
        'remark': 'remark',
        'extension': 'extension'
    }

    def __init__(self, protocol=None, endpoint=None, remark=None, extension=None):
        """BatchAddSubscriptionsRequestBody

        The model defined in huaweicloud sdk

        :param protocol: 不同协议对应不同的endpoint（接受消息的接入点）。 目前支持的协议包括：  “email”：邮件传输协议，endpoint为邮箱地址。  “sms”：短信传输协议，endpoint为手机号码。  “functionstage”：FunctionGraph（函数）传输协议，endpoint为一个函数。  “functiongraph”：FunctionGraph（工作流）传输协议，endpoint为由一组函数编排成的工作流。  “http”、“https”：HTTP/HTTPS传输协议，endpoint为URL。  “callnotify”：语音通知传输协议，endpoint为手机号码。  “wechat”：微信群机器人传输协议。  “dingding”：钉钉群机器人传输协议。  “feishu”：飞书群机器人传输协议。  “welink”：welink群机器人传输协议。
        :type protocol: str
        :param endpoint: 说明：  http协议，接入点必须以“http://”开头。  https协议，接入点必须以“https://”开头。  email协议，接入点必须是邮件地址。  sms协议，接入点必须是一个电话号码。  functionstage协议，接入点必须是一个函数。  functiongraph协议，接入点必须是一个函数工作流。  callnotify协议，接入点必须是一个电话号码。  dingding协议，接入点必须是一个钉钉自定义群机器人的地址，或添加了钉钉企业内部机器人的群组openConversationId。添加钉钉企业内部机器人对应的群组openConversationId时，该字段不能以“http://”或“https://”为开头。  wechat协议，接入点必须是一个微信群机器人的地址。  feishu协议，接入点必须是一个飞书群机器人的地址。  welink协议，接入点必须是一个welink的群号。
        :type endpoint: str
        :param remark: 备注。最大支持128字节，约42个中文，必须是UTF-8编码的字符串，否则无法正常显示中文。
        :type remark: str
        :param extension: 
        :type extension: :class:`huaweicloudsdksmn.v2.SubscriptionExtension`
        """
        
        

        self._protocol = None
        self._endpoint = None
        self._remark = None
        self._extension = None
        self.discriminator = None

        self.protocol = protocol
        self.endpoint = endpoint
        if remark is not None:
            self.remark = remark
        if extension is not None:
            self.extension = extension

    @property
    def protocol(self):
        """Gets the protocol of this BatchAddSubscriptionsRequestBody.

        不同协议对应不同的endpoint（接受消息的接入点）。 目前支持的协议包括：  “email”：邮件传输协议，endpoint为邮箱地址。  “sms”：短信传输协议，endpoint为手机号码。  “functionstage”：FunctionGraph（函数）传输协议，endpoint为一个函数。  “functiongraph”：FunctionGraph（工作流）传输协议，endpoint为由一组函数编排成的工作流。  “http”、“https”：HTTP/HTTPS传输协议，endpoint为URL。  “callnotify”：语音通知传输协议，endpoint为手机号码。  “wechat”：微信群机器人传输协议。  “dingding”：钉钉群机器人传输协议。  “feishu”：飞书群机器人传输协议。  “welink”：welink群机器人传输协议。

        :return: The protocol of this BatchAddSubscriptionsRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this BatchAddSubscriptionsRequestBody.

        不同协议对应不同的endpoint（接受消息的接入点）。 目前支持的协议包括：  “email”：邮件传输协议，endpoint为邮箱地址。  “sms”：短信传输协议，endpoint为手机号码。  “functionstage”：FunctionGraph（函数）传输协议，endpoint为一个函数。  “functiongraph”：FunctionGraph（工作流）传输协议，endpoint为由一组函数编排成的工作流。  “http”、“https”：HTTP/HTTPS传输协议，endpoint为URL。  “callnotify”：语音通知传输协议，endpoint为手机号码。  “wechat”：微信群机器人传输协议。  “dingding”：钉钉群机器人传输协议。  “feishu”：飞书群机器人传输协议。  “welink”：welink群机器人传输协议。

        :param protocol: The protocol of this BatchAddSubscriptionsRequestBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def endpoint(self):
        """Gets the endpoint of this BatchAddSubscriptionsRequestBody.

        说明：  http协议，接入点必须以“http://”开头。  https协议，接入点必须以“https://”开头。  email协议，接入点必须是邮件地址。  sms协议，接入点必须是一个电话号码。  functionstage协议，接入点必须是一个函数。  functiongraph协议，接入点必须是一个函数工作流。  callnotify协议，接入点必须是一个电话号码。  dingding协议，接入点必须是一个钉钉自定义群机器人的地址，或添加了钉钉企业内部机器人的群组openConversationId。添加钉钉企业内部机器人对应的群组openConversationId时，该字段不能以“http://”或“https://”为开头。  wechat协议，接入点必须是一个微信群机器人的地址。  feishu协议，接入点必须是一个飞书群机器人的地址。  welink协议，接入点必须是一个welink的群号。

        :return: The endpoint of this BatchAddSubscriptionsRequestBody.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this BatchAddSubscriptionsRequestBody.

        说明：  http协议，接入点必须以“http://”开头。  https协议，接入点必须以“https://”开头。  email协议，接入点必须是邮件地址。  sms协议，接入点必须是一个电话号码。  functionstage协议，接入点必须是一个函数。  functiongraph协议，接入点必须是一个函数工作流。  callnotify协议，接入点必须是一个电话号码。  dingding协议，接入点必须是一个钉钉自定义群机器人的地址，或添加了钉钉企业内部机器人的群组openConversationId。添加钉钉企业内部机器人对应的群组openConversationId时，该字段不能以“http://”或“https://”为开头。  wechat协议，接入点必须是一个微信群机器人的地址。  feishu协议，接入点必须是一个飞书群机器人的地址。  welink协议，接入点必须是一个welink的群号。

        :param endpoint: The endpoint of this BatchAddSubscriptionsRequestBody.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def remark(self):
        """Gets the remark of this BatchAddSubscriptionsRequestBody.

        备注。最大支持128字节，约42个中文，必须是UTF-8编码的字符串，否则无法正常显示中文。

        :return: The remark of this BatchAddSubscriptionsRequestBody.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this BatchAddSubscriptionsRequestBody.

        备注。最大支持128字节，约42个中文，必须是UTF-8编码的字符串，否则无法正常显示中文。

        :param remark: The remark of this BatchAddSubscriptionsRequestBody.
        :type remark: str
        """
        self._remark = remark

    @property
    def extension(self):
        """Gets the extension of this BatchAddSubscriptionsRequestBody.

        :return: The extension of this BatchAddSubscriptionsRequestBody.
        :rtype: :class:`huaweicloudsdksmn.v2.SubscriptionExtension`
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this BatchAddSubscriptionsRequestBody.

        :param extension: The extension of this BatchAddSubscriptionsRequestBody.
        :type extension: :class:`huaweicloudsdksmn.v2.SubscriptionExtension`
        """
        self._extension = extension

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
        if not isinstance(other, BatchAddSubscriptionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
