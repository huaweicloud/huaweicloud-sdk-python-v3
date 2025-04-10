# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmnNotify:

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
        'subscription_name': 'str'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'subscription_name': 'subscription_name'
    }

    def __init__(self, topic_urn=None, subscription_name=None):
        r"""SmnNotify

        The model defined in huaweicloud sdk

        :param topic_urn: SMN消息通知服务的主题urn，如果需要开启告警订阅，则必填。
        :type topic_urn: str
        :param subscription_name: 该订阅规则名称。如果不填写，则默认为default_alert_rule。
        :type subscription_name: str
        """
        
        

        self._topic_urn = None
        self._subscription_name = None
        self.discriminator = None

        if topic_urn is not None:
            self.topic_urn = topic_urn
        if subscription_name is not None:
            self.subscription_name = subscription_name

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this SmnNotify.

        SMN消息通知服务的主题urn，如果需要开启告警订阅，则必填。

        :return: The topic_urn of this SmnNotify.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this SmnNotify.

        SMN消息通知服务的主题urn，如果需要开启告警订阅，则必填。

        :param topic_urn: The topic_urn of this SmnNotify.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def subscription_name(self):
        r"""Gets the subscription_name of this SmnNotify.

        该订阅规则名称。如果不填写，则默认为default_alert_rule。

        :return: The subscription_name of this SmnNotify.
        :rtype: str
        """
        return self._subscription_name

    @subscription_name.setter
    def subscription_name(self, subscription_name):
        r"""Sets the subscription_name of this SmnNotify.

        该订阅规则名称。如果不填写，则默认为default_alert_rule。

        :param subscription_name: The subscription_name of this SmnNotify.
        :type subscription_name: str
        """
        self._subscription_name = subscription_name

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
        if not isinstance(other, SmnNotify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
