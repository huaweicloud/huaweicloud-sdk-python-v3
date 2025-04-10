# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNotifyPolicyRequest:

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
        'notify_policy_id': 'str',
        'body': 'NotifyPolicyRequestBody'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'notify_policy_id': 'notify_policy_id',
        'body': 'body'
    }

    def __init__(self, topic_urn=None, notify_policy_id=None, body=None):
        r"""UpdateNotifyPolicyRequest

        The model defined in huaweicloud sdk

        :param topic_urn: Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。
        :type topic_urn: str
        :param notify_policy_id: 通知策略ID。
        :type notify_policy_id: str
        :param body: Body of the UpdateNotifyPolicyRequest
        :type body: :class:`huaweicloudsdksmn.v2.NotifyPolicyRequestBody`
        """
        
        

        self._topic_urn = None
        self._notify_policy_id = None
        self._body = None
        self.discriminator = None

        self.topic_urn = topic_urn
        self.notify_policy_id = notify_policy_id
        if body is not None:
            self.body = body

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this UpdateNotifyPolicyRequest.

        Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。

        :return: The topic_urn of this UpdateNotifyPolicyRequest.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this UpdateNotifyPolicyRequest.

        Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。

        :param topic_urn: The topic_urn of this UpdateNotifyPolicyRequest.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def notify_policy_id(self):
        r"""Gets the notify_policy_id of this UpdateNotifyPolicyRequest.

        通知策略ID。

        :return: The notify_policy_id of this UpdateNotifyPolicyRequest.
        :rtype: str
        """
        return self._notify_policy_id

    @notify_policy_id.setter
    def notify_policy_id(self, notify_policy_id):
        r"""Sets the notify_policy_id of this UpdateNotifyPolicyRequest.

        通知策略ID。

        :param notify_policy_id: The notify_policy_id of this UpdateNotifyPolicyRequest.
        :type notify_policy_id: str
        """
        self._notify_policy_id = notify_policy_id

    @property
    def body(self):
        r"""Gets the body of this UpdateNotifyPolicyRequest.

        :return: The body of this UpdateNotifyPolicyRequest.
        :rtype: :class:`huaweicloudsdksmn.v2.NotifyPolicyRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateNotifyPolicyRequest.

        :param body: The body of this UpdateNotifyPolicyRequest.
        :type body: :class:`huaweicloudsdksmn.v2.NotifyPolicyRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateNotifyPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
