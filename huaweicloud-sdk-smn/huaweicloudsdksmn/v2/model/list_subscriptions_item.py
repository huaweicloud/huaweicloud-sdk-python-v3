# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_urn': 'str',
        'protocol': 'str',
        'subscription_urn': 'str',
        'owner': 'str',
        'endpoint': 'str',
        'remark': 'str',
        'status': 'int'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'protocol': 'protocol',
        'subscription_urn': 'subscription_urn',
        'owner': 'owner',
        'endpoint': 'endpoint',
        'remark': 'remark',
        'status': 'status'
    }

    def __init__(self, topic_urn=None, protocol=None, subscription_urn=None, owner=None, endpoint=None, remark=None, status=None):
        """ListSubscriptionsItem

        The model defined in huaweicloud sdk

        :param topic_urn: Topic的唯一的资源标识。
        :type topic_urn: str
        :param protocol: 不同协议对应不同的endpoint（接受消息的接入点）。目前支持的协议包括：  \&quot;default\&quot;: 默认协议。  “email”：邮件传输协议，endpoint为邮箱地址。  “sms”：短信传输协议，endpoint为手机号码。  “functionstage”：FunctionGraph（函数）传输协议，endpoint为一个函数。  “http”、“https”：HTTP/HTTPS传输协议，endpoint为URL。
        :type protocol: str
        :param subscription_urn: 订阅者的唯一资源标识。
        :type subscription_urn: str
        :param owner: Topic创建者的项目ID。
        :type owner: str
        :param endpoint: 接受消息的接入点。
        :type endpoint: str
        :param remark: 备注。
        :type remark: str
        :param status: 订阅者状态：0表示订阅还未确认，1表示已经确认，3表示已经取消确认。
        :type status: int
        """
        
        

        self._topic_urn = None
        self._protocol = None
        self._subscription_urn = None
        self._owner = None
        self._endpoint = None
        self._remark = None
        self._status = None
        self.discriminator = None

        self.topic_urn = topic_urn
        self.protocol = protocol
        self.subscription_urn = subscription_urn
        self.owner = owner
        self.endpoint = endpoint
        self.remark = remark
        self.status = status

    @property
    def topic_urn(self):
        """Gets the topic_urn of this ListSubscriptionsItem.

        Topic的唯一的资源标识。

        :return: The topic_urn of this ListSubscriptionsItem.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this ListSubscriptionsItem.

        Topic的唯一的资源标识。

        :param topic_urn: The topic_urn of this ListSubscriptionsItem.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def protocol(self):
        """Gets the protocol of this ListSubscriptionsItem.

        不同协议对应不同的endpoint（接受消息的接入点）。目前支持的协议包括：  \"default\": 默认协议。  “email”：邮件传输协议，endpoint为邮箱地址。  “sms”：短信传输协议，endpoint为手机号码。  “functionstage”：FunctionGraph（函数）传输协议，endpoint为一个函数。  “http”、“https”：HTTP/HTTPS传输协议，endpoint为URL。

        :return: The protocol of this ListSubscriptionsItem.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListSubscriptionsItem.

        不同协议对应不同的endpoint（接受消息的接入点）。目前支持的协议包括：  \"default\": 默认协议。  “email”：邮件传输协议，endpoint为邮箱地址。  “sms”：短信传输协议，endpoint为手机号码。  “functionstage”：FunctionGraph（函数）传输协议，endpoint为一个函数。  “http”、“https”：HTTP/HTTPS传输协议，endpoint为URL。

        :param protocol: The protocol of this ListSubscriptionsItem.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def subscription_urn(self):
        """Gets the subscription_urn of this ListSubscriptionsItem.

        订阅者的唯一资源标识。

        :return: The subscription_urn of this ListSubscriptionsItem.
        :rtype: str
        """
        return self._subscription_urn

    @subscription_urn.setter
    def subscription_urn(self, subscription_urn):
        """Sets the subscription_urn of this ListSubscriptionsItem.

        订阅者的唯一资源标识。

        :param subscription_urn: The subscription_urn of this ListSubscriptionsItem.
        :type subscription_urn: str
        """
        self._subscription_urn = subscription_urn

    @property
    def owner(self):
        """Gets the owner of this ListSubscriptionsItem.

        Topic创建者的项目ID。

        :return: The owner of this ListSubscriptionsItem.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ListSubscriptionsItem.

        Topic创建者的项目ID。

        :param owner: The owner of this ListSubscriptionsItem.
        :type owner: str
        """
        self._owner = owner

    @property
    def endpoint(self):
        """Gets the endpoint of this ListSubscriptionsItem.

        接受消息的接入点。

        :return: The endpoint of this ListSubscriptionsItem.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ListSubscriptionsItem.

        接受消息的接入点。

        :param endpoint: The endpoint of this ListSubscriptionsItem.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def remark(self):
        """Gets the remark of this ListSubscriptionsItem.

        备注。

        :return: The remark of this ListSubscriptionsItem.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ListSubscriptionsItem.

        备注。

        :param remark: The remark of this ListSubscriptionsItem.
        :type remark: str
        """
        self._remark = remark

    @property
    def status(self):
        """Gets the status of this ListSubscriptionsItem.

        订阅者状态：0表示订阅还未确认，1表示已经确认，3表示已经取消确认。

        :return: The status of this ListSubscriptionsItem.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSubscriptionsItem.

        订阅者状态：0表示订阅还未确认，1表示已经确认，3表示已经取消确认。

        :param status: The status of this ListSubscriptionsItem.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ListSubscriptionsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
