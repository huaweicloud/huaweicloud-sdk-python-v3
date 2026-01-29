# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmnSubscription:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'owner': 'str',
        'endpoint': 'str',
        'protocol': 'str',
        'subscription_urn': 'str',
        'topic_urn': 'str',
        'status': 'int'
    }

    attribute_map = {
        'owner': 'owner',
        'endpoint': 'endpoint',
        'protocol': 'protocol',
        'subscription_urn': 'subscription_urn',
        'topic_urn': 'topic_urn',
        'status': 'status'
    }

    def __init__(self, owner=None, endpoint=None, protocol=None, subscription_urn=None, topic_urn=None, status=None):
        r"""SmnSubscription

        The model defined in huaweicloud sdk

        :param owner: 租户project_id
        :type owner: str
        :param endpoint: 订阅终端
        :type endpoint: str
        :param protocol: 终端协议，比如HTTPS协议，SMS协议，EMAIL协议，HTTP协议
        :type protocol: str
        :param subscription_urn: smn订阅的urn
        :type subscription_urn: str
        :param topic_urn: 订阅topic对应的urn
        :type topic_urn: str
        :param status: 订阅状态 0：未确认 1：已确认 2：不需要确认 3：已取消确认 4：已经删除。
        :type status: int
        """
        
        

        self._owner = None
        self._endpoint = None
        self._protocol = None
        self._subscription_urn = None
        self._topic_urn = None
        self._status = None
        self.discriminator = None

        self.owner = owner
        self.endpoint = endpoint
        self.protocol = protocol
        self.subscription_urn = subscription_urn
        self.topic_urn = topic_urn
        self.status = status

    @property
    def owner(self):
        r"""Gets the owner of this SmnSubscription.

        租户project_id

        :return: The owner of this SmnSubscription.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this SmnSubscription.

        租户project_id

        :param owner: The owner of this SmnSubscription.
        :type owner: str
        """
        self._owner = owner

    @property
    def endpoint(self):
        r"""Gets the endpoint of this SmnSubscription.

        订阅终端

        :return: The endpoint of this SmnSubscription.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this SmnSubscription.

        订阅终端

        :param endpoint: The endpoint of this SmnSubscription.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def protocol(self):
        r"""Gets the protocol of this SmnSubscription.

        终端协议，比如HTTPS协议，SMS协议，EMAIL协议，HTTP协议

        :return: The protocol of this SmnSubscription.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this SmnSubscription.

        终端协议，比如HTTPS协议，SMS协议，EMAIL协议，HTTP协议

        :param protocol: The protocol of this SmnSubscription.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def subscription_urn(self):
        r"""Gets the subscription_urn of this SmnSubscription.

        smn订阅的urn

        :return: The subscription_urn of this SmnSubscription.
        :rtype: str
        """
        return self._subscription_urn

    @subscription_urn.setter
    def subscription_urn(self, subscription_urn):
        r"""Sets the subscription_urn of this SmnSubscription.

        smn订阅的urn

        :param subscription_urn: The subscription_urn of this SmnSubscription.
        :type subscription_urn: str
        """
        self._subscription_urn = subscription_urn

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this SmnSubscription.

        订阅topic对应的urn

        :return: The topic_urn of this SmnSubscription.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this SmnSubscription.

        订阅topic对应的urn

        :param topic_urn: The topic_urn of this SmnSubscription.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def status(self):
        r"""Gets the status of this SmnSubscription.

        订阅状态 0：未确认 1：已确认 2：不需要确认 3：已取消确认 4：已经删除。

        :return: The status of this SmnSubscription.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SmnSubscription.

        订阅状态 0：未确认 1：已确认 2：不需要确认 3：已取消确认 4：已经删除。

        :param status: The status of this SmnSubscription.
        :type status: int
        """
        self._status = status

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SmnSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
