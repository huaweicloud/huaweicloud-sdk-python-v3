# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSubscriptionRequestBody:

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
        'extension': 'SubscriptionExtension',
        'subscriptions': 'list[BatchAddSubscriptionsRequestBody]'
    }

    attribute_map = {
        'protocol': 'protocol',
        'endpoint': 'endpoint',
        'remark': 'remark',
        'extension': 'extension',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, protocol=None, endpoint=None, remark=None, extension=None, subscriptions=None):
        r"""AddSubscriptionRequestBody

        The model defined in huaweicloud sdk

        :param protocol: 不同协议对应不同的endpoint（接受消息的接入点）。 目前支持的协议包括：  “email”：邮件传输协议，endpoint为邮箱地址。  “sms”：短信传输协议，endpoint为手机号码。  “functionstage”：FunctionGraph（函数）传输协议，endpoint为一个函数。  “functiongraph”：FunctionGraph（工作流）传输协议，endpoint为由一组函数编排成的工作流。  “http”、“https”：HTTP/HTTPS传输协议，endpoint为URL。  “callnotify”：语音通知传输协议，endpoint为手机号码。  “wechat”：微信群机器人传输协议。  “dingding”：钉钉群机器人传输协议。  “feishu”：飞书群机器人传输协议。  “welink”：welink群机器人传输协议。  “dingTalkBot”：个人钉钉传输协议。
        :type protocol: str
        :param endpoint: 说明：  http协议，接入点必须以“http://”开头，且必须为公网的IPV4地址、IPV6地址或域名地址。不支持使用内网地址，包括但不限于IPv4私有地址、IPv6本地地址、回环地址等。需确保该地址可通过公网路由访问，避免因防火墙、NAT或DNS配置导致不可达。  https协议，接入点必须以“https://”开头，且必须为公网的IPV4地址、IPV6地址或域名地址。不支持使用内网地址，包括但不限于IPv4私有地址、IPv6本地地址、回环地址等。需确保该地址可通过公网路由访问，避免因防火墙、NAT或DNS配置导致不可达。  email协议，接入点必须是邮件地址。  sms协议，接入点必须是一个电话号码。  functionstage协议，接入点必须是一个函数。  functiongraph协议，接入点必须是一个函数工作流。  callnotify协议，接入点必须是一个电话号码。  dingding协议，接入点必须是一个钉钉自定义群机器人的地址，或添加了钉钉企业内部机器人的群组openConversationId。添加钉钉企业内部机器人对应的群组openConversationId时，该字段不能以“http://”或“https://”为开头。  wechat协议，接入点必须是一个微信群机器人的地址。  feishu协议，接入点必须是一个飞书群机器人的地址。  welink协议，接入点必须是一个welink的群号。  dingTalkBot协议，接入点必须是一个钉钉企业用户的userId。
        :type endpoint: str
        :param remark: 备注。最大支持128字节，约42个中文，必须是UTF-8编码的字符串，否则无法正常显示中文。
        :type remark: str
        :param extension: 
        :type extension: :class:`huaweicloudsdksmn.v2.SubscriptionExtension`
        :param subscriptions: 当需要批量创建订阅时，需要传入该字段。SMN支持一次最多创建50个订阅。
        :type subscriptions: list[:class:`huaweicloudsdksmn.v2.BatchAddSubscriptionsRequestBody`]
        """
        
        

        self._protocol = None
        self._endpoint = None
        self._remark = None
        self._extension = None
        self._subscriptions = None
        self.discriminator = None

        self.protocol = protocol
        self.endpoint = endpoint
        if remark is not None:
            self.remark = remark
        if extension is not None:
            self.extension = extension
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def protocol(self):
        r"""Gets the protocol of this AddSubscriptionRequestBody.

        不同协议对应不同的endpoint（接受消息的接入点）。 目前支持的协议包括：  “email”：邮件传输协议，endpoint为邮箱地址。  “sms”：短信传输协议，endpoint为手机号码。  “functionstage”：FunctionGraph（函数）传输协议，endpoint为一个函数。  “functiongraph”：FunctionGraph（工作流）传输协议，endpoint为由一组函数编排成的工作流。  “http”、“https”：HTTP/HTTPS传输协议，endpoint为URL。  “callnotify”：语音通知传输协议，endpoint为手机号码。  “wechat”：微信群机器人传输协议。  “dingding”：钉钉群机器人传输协议。  “feishu”：飞书群机器人传输协议。  “welink”：welink群机器人传输协议。  “dingTalkBot”：个人钉钉传输协议。

        :return: The protocol of this AddSubscriptionRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this AddSubscriptionRequestBody.

        不同协议对应不同的endpoint（接受消息的接入点）。 目前支持的协议包括：  “email”：邮件传输协议，endpoint为邮箱地址。  “sms”：短信传输协议，endpoint为手机号码。  “functionstage”：FunctionGraph（函数）传输协议，endpoint为一个函数。  “functiongraph”：FunctionGraph（工作流）传输协议，endpoint为由一组函数编排成的工作流。  “http”、“https”：HTTP/HTTPS传输协议，endpoint为URL。  “callnotify”：语音通知传输协议，endpoint为手机号码。  “wechat”：微信群机器人传输协议。  “dingding”：钉钉群机器人传输协议。  “feishu”：飞书群机器人传输协议。  “welink”：welink群机器人传输协议。  “dingTalkBot”：个人钉钉传输协议。

        :param protocol: The protocol of this AddSubscriptionRequestBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def endpoint(self):
        r"""Gets the endpoint of this AddSubscriptionRequestBody.

        说明：  http协议，接入点必须以“http://”开头，且必须为公网的IPV4地址、IPV6地址或域名地址。不支持使用内网地址，包括但不限于IPv4私有地址、IPv6本地地址、回环地址等。需确保该地址可通过公网路由访问，避免因防火墙、NAT或DNS配置导致不可达。  https协议，接入点必须以“https://”开头，且必须为公网的IPV4地址、IPV6地址或域名地址。不支持使用内网地址，包括但不限于IPv4私有地址、IPv6本地地址、回环地址等。需确保该地址可通过公网路由访问，避免因防火墙、NAT或DNS配置导致不可达。  email协议，接入点必须是邮件地址。  sms协议，接入点必须是一个电话号码。  functionstage协议，接入点必须是一个函数。  functiongraph协议，接入点必须是一个函数工作流。  callnotify协议，接入点必须是一个电话号码。  dingding协议，接入点必须是一个钉钉自定义群机器人的地址，或添加了钉钉企业内部机器人的群组openConversationId。添加钉钉企业内部机器人对应的群组openConversationId时，该字段不能以“http://”或“https://”为开头。  wechat协议，接入点必须是一个微信群机器人的地址。  feishu协议，接入点必须是一个飞书群机器人的地址。  welink协议，接入点必须是一个welink的群号。  dingTalkBot协议，接入点必须是一个钉钉企业用户的userId。

        :return: The endpoint of this AddSubscriptionRequestBody.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this AddSubscriptionRequestBody.

        说明：  http协议，接入点必须以“http://”开头，且必须为公网的IPV4地址、IPV6地址或域名地址。不支持使用内网地址，包括但不限于IPv4私有地址、IPv6本地地址、回环地址等。需确保该地址可通过公网路由访问，避免因防火墙、NAT或DNS配置导致不可达。  https协议，接入点必须以“https://”开头，且必须为公网的IPV4地址、IPV6地址或域名地址。不支持使用内网地址，包括但不限于IPv4私有地址、IPv6本地地址、回环地址等。需确保该地址可通过公网路由访问，避免因防火墙、NAT或DNS配置导致不可达。  email协议，接入点必须是邮件地址。  sms协议，接入点必须是一个电话号码。  functionstage协议，接入点必须是一个函数。  functiongraph协议，接入点必须是一个函数工作流。  callnotify协议，接入点必须是一个电话号码。  dingding协议，接入点必须是一个钉钉自定义群机器人的地址，或添加了钉钉企业内部机器人的群组openConversationId。添加钉钉企业内部机器人对应的群组openConversationId时，该字段不能以“http://”或“https://”为开头。  wechat协议，接入点必须是一个微信群机器人的地址。  feishu协议，接入点必须是一个飞书群机器人的地址。  welink协议，接入点必须是一个welink的群号。  dingTalkBot协议，接入点必须是一个钉钉企业用户的userId。

        :param endpoint: The endpoint of this AddSubscriptionRequestBody.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def remark(self):
        r"""Gets the remark of this AddSubscriptionRequestBody.

        备注。最大支持128字节，约42个中文，必须是UTF-8编码的字符串，否则无法正常显示中文。

        :return: The remark of this AddSubscriptionRequestBody.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this AddSubscriptionRequestBody.

        备注。最大支持128字节，约42个中文，必须是UTF-8编码的字符串，否则无法正常显示中文。

        :param remark: The remark of this AddSubscriptionRequestBody.
        :type remark: str
        """
        self._remark = remark

    @property
    def extension(self):
        r"""Gets the extension of this AddSubscriptionRequestBody.

        :return: The extension of this AddSubscriptionRequestBody.
        :rtype: :class:`huaweicloudsdksmn.v2.SubscriptionExtension`
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        r"""Sets the extension of this AddSubscriptionRequestBody.

        :param extension: The extension of this AddSubscriptionRequestBody.
        :type extension: :class:`huaweicloudsdksmn.v2.SubscriptionExtension`
        """
        self._extension = extension

    @property
    def subscriptions(self):
        r"""Gets the subscriptions of this AddSubscriptionRequestBody.

        当需要批量创建订阅时，需要传入该字段。SMN支持一次最多创建50个订阅。

        :return: The subscriptions of this AddSubscriptionRequestBody.
        :rtype: list[:class:`huaweicloudsdksmn.v2.BatchAddSubscriptionsRequestBody`]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        r"""Sets the subscriptions of this AddSubscriptionRequestBody.

        当需要批量创建订阅时，需要传入该字段。SMN支持一次最多创建50个订阅。

        :param subscriptions: The subscriptions of this AddSubscriptionRequestBody.
        :type subscriptions: list[:class:`huaweicloudsdksmn.v2.BatchAddSubscriptionsRequestBody`]
        """
        self._subscriptions = subscriptions

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
        if not isinstance(other, AddSubscriptionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
