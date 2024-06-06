# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoticeRuleNotification:

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
        'endpoint': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'endpoint': 'endpoint'
    }

    def __init__(self, protocol=None, endpoint=None):
        """NoticeRuleNotification

        The model defined in huaweicloud sdk

        :param protocol: 通知的协议类型，包括短信，邮件，企业微信群消息等。
        :type protocol: str
        :param endpoint: 通知的终端地址。 email协议，接入点必须是邮件地址。 sms协议，接入点必须是一个电话号码。 wechat协议，参考https://support.huaweicloud.com/smn_faq/smn_faq_0027.html获取订阅终端， 企业微信群消息为SMN服务公测功能，需提交工单申请开通。
        :type endpoint: str
        """
        
        

        self._protocol = None
        self._endpoint = None
        self.discriminator = None

        self.protocol = protocol
        self.endpoint = endpoint

    @property
    def protocol(self):
        """Gets the protocol of this NoticeRuleNotification.

        通知的协议类型，包括短信，邮件，企业微信群消息等。

        :return: The protocol of this NoticeRuleNotification.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NoticeRuleNotification.

        通知的协议类型，包括短信，邮件，企业微信群消息等。

        :param protocol: The protocol of this NoticeRuleNotification.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def endpoint(self):
        """Gets the endpoint of this NoticeRuleNotification.

        通知的终端地址。 email协议，接入点必须是邮件地址。 sms协议，接入点必须是一个电话号码。 wechat协议，参考https://support.huaweicloud.com/smn_faq/smn_faq_0027.html获取订阅终端， 企业微信群消息为SMN服务公测功能，需提交工单申请开通。

        :return: The endpoint of this NoticeRuleNotification.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this NoticeRuleNotification.

        通知的终端地址。 email协议，接入点必须是邮件地址。 sms协议，接入点必须是一个电话号码。 wechat协议，参考https://support.huaweicloud.com/smn_faq/smn_faq_0027.html获取订阅终端， 企业微信群消息为SMN服务公测功能，需提交工单申请开通。

        :param endpoint: The endpoint of this NoticeRuleNotification.
        :type endpoint: str
        """
        self._endpoint = endpoint

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
        if not isinstance(other, NoticeRuleNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
