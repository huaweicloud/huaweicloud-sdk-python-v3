# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfirmSubscriptionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('token')

    openapi_types = {
        'topic_urn': 'str',
        'endpoint': 'str',
        'token': 'str'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'endpoint': 'endpoint',
        'token': 'token'
    }

    def __init__(self, topic_urn=None, endpoint=None, token=None):
        r"""ConfirmSubscriptionRequest

        The model defined in huaweicloud sdk

        :param topic_urn: Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。
        :type topic_urn: str
        :param endpoint: 订阅终端地址。
        :type endpoint: str
        :param token: 确认订阅Token信息。
        :type token: str
        """
        
        

        self._topic_urn = None
        self._endpoint = None
        self._token = None
        self.discriminator = None

        if topic_urn is not None:
            self.topic_urn = topic_urn
        if endpoint is not None:
            self.endpoint = endpoint
        self.token = token

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ConfirmSubscriptionRequest.

        Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。

        :return: The topic_urn of this ConfirmSubscriptionRequest.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ConfirmSubscriptionRequest.

        Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。

        :param topic_urn: The topic_urn of this ConfirmSubscriptionRequest.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def endpoint(self):
        r"""Gets the endpoint of this ConfirmSubscriptionRequest.

        订阅终端地址。

        :return: The endpoint of this ConfirmSubscriptionRequest.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this ConfirmSubscriptionRequest.

        订阅终端地址。

        :param endpoint: The endpoint of this ConfirmSubscriptionRequest.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def token(self):
        r"""Gets the token of this ConfirmSubscriptionRequest.

        确认订阅Token信息。

        :return: The token of this ConfirmSubscriptionRequest.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this ConfirmSubscriptionRequest.

        确认订阅Token信息。

        :param token: The token of this ConfirmSubscriptionRequest.
        :type token: str
        """
        self._token = token

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
        if not isinstance(other, ConfirmSubscriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
