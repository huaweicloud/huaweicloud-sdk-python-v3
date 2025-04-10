# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotifyPolicyRequestBody:

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
        'polling': 'list[PollingPolicyRequest]'
    }

    attribute_map = {
        'protocol': 'protocol',
        'polling': 'polling'
    }

    def __init__(self, protocol=None, polling=None):
        r"""NotifyPolicyRequestBody

        The model defined in huaweicloud sdk

        :param protocol: 通知策略类型，当前仅支持语音。
        :type protocol: str
        :param polling: 轮询策略订阅终端。
        :type polling: list[:class:`huaweicloudsdksmn.v2.PollingPolicyRequest`]
        """
        
        

        self._protocol = None
        self._polling = None
        self.discriminator = None

        self.protocol = protocol
        self.polling = polling

    @property
    def protocol(self):
        r"""Gets the protocol of this NotifyPolicyRequestBody.

        通知策略类型，当前仅支持语音。

        :return: The protocol of this NotifyPolicyRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this NotifyPolicyRequestBody.

        通知策略类型，当前仅支持语音。

        :param protocol: The protocol of this NotifyPolicyRequestBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def polling(self):
        r"""Gets the polling of this NotifyPolicyRequestBody.

        轮询策略订阅终端。

        :return: The polling of this NotifyPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdksmn.v2.PollingPolicyRequest`]
        """
        return self._polling

    @polling.setter
    def polling(self, polling):
        r"""Sets the polling of this NotifyPolicyRequestBody.

        轮询策略订阅终端。

        :param polling: The polling of this NotifyPolicyRequestBody.
        :type polling: list[:class:`huaweicloudsdksmn.v2.PollingPolicyRequest`]
        """
        self._polling = polling

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
        if not isinstance(other, NotifyPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
