# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmnResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sent_time': 'int',
        'smn_notified_history': 'list[SmnInfo]',
        'smn_request_id': 'str',
        'smn_response_body': 'str',
        'smn_response_code': 'str',
        'smn_topic': 'str'
    }

    attribute_map = {
        'sent_time': 'sent_time',
        'smn_notified_history': 'smn_notified_history',
        'smn_request_id': 'smn_request_id',
        'smn_response_body': 'smn_response_body',
        'smn_response_code': 'smn_response_code',
        'smn_topic': 'smn_topic'
    }

    def __init__(self, sent_time=None, smn_notified_history=None, smn_request_id=None, smn_response_body=None, smn_response_code=None, smn_topic=None):
        r"""SmnResponse

        The model defined in huaweicloud sdk

        :param sent_time: 发送时间。
        :type sent_time: int
        :param smn_notified_history: 发送的通知的消息内容。
        :type smn_notified_history: list[:class:`huaweicloudsdkaom.v2.SmnInfo`]
        :param smn_request_id: 请求smn服务的请求id。
        :type smn_request_id: str
        :param smn_response_body: 调用smn服务返回的信息。
        :type smn_response_body: str
        :param smn_response_code: 调用smn服务返回的http状态码。
        :type smn_response_code: str
        :param smn_topic: smn的主题。
        :type smn_topic: str
        """
        
        

        self._sent_time = None
        self._smn_notified_history = None
        self._smn_request_id = None
        self._smn_response_body = None
        self._smn_response_code = None
        self._smn_topic = None
        self.discriminator = None

        if sent_time is not None:
            self.sent_time = sent_time
        if smn_notified_history is not None:
            self.smn_notified_history = smn_notified_history
        if smn_request_id is not None:
            self.smn_request_id = smn_request_id
        if smn_response_body is not None:
            self.smn_response_body = smn_response_body
        if smn_response_code is not None:
            self.smn_response_code = smn_response_code
        if smn_topic is not None:
            self.smn_topic = smn_topic

    @property
    def sent_time(self):
        r"""Gets the sent_time of this SmnResponse.

        发送时间。

        :return: The sent_time of this SmnResponse.
        :rtype: int
        """
        return self._sent_time

    @sent_time.setter
    def sent_time(self, sent_time):
        r"""Sets the sent_time of this SmnResponse.

        发送时间。

        :param sent_time: The sent_time of this SmnResponse.
        :type sent_time: int
        """
        self._sent_time = sent_time

    @property
    def smn_notified_history(self):
        r"""Gets the smn_notified_history of this SmnResponse.

        发送的通知的消息内容。

        :return: The smn_notified_history of this SmnResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.SmnInfo`]
        """
        return self._smn_notified_history

    @smn_notified_history.setter
    def smn_notified_history(self, smn_notified_history):
        r"""Sets the smn_notified_history of this SmnResponse.

        发送的通知的消息内容。

        :param smn_notified_history: The smn_notified_history of this SmnResponse.
        :type smn_notified_history: list[:class:`huaweicloudsdkaom.v2.SmnInfo`]
        """
        self._smn_notified_history = smn_notified_history

    @property
    def smn_request_id(self):
        r"""Gets the smn_request_id of this SmnResponse.

        请求smn服务的请求id。

        :return: The smn_request_id of this SmnResponse.
        :rtype: str
        """
        return self._smn_request_id

    @smn_request_id.setter
    def smn_request_id(self, smn_request_id):
        r"""Sets the smn_request_id of this SmnResponse.

        请求smn服务的请求id。

        :param smn_request_id: The smn_request_id of this SmnResponse.
        :type smn_request_id: str
        """
        self._smn_request_id = smn_request_id

    @property
    def smn_response_body(self):
        r"""Gets the smn_response_body of this SmnResponse.

        调用smn服务返回的信息。

        :return: The smn_response_body of this SmnResponse.
        :rtype: str
        """
        return self._smn_response_body

    @smn_response_body.setter
    def smn_response_body(self, smn_response_body):
        r"""Sets the smn_response_body of this SmnResponse.

        调用smn服务返回的信息。

        :param smn_response_body: The smn_response_body of this SmnResponse.
        :type smn_response_body: str
        """
        self._smn_response_body = smn_response_body

    @property
    def smn_response_code(self):
        r"""Gets the smn_response_code of this SmnResponse.

        调用smn服务返回的http状态码。

        :return: The smn_response_code of this SmnResponse.
        :rtype: str
        """
        return self._smn_response_code

    @smn_response_code.setter
    def smn_response_code(self, smn_response_code):
        r"""Sets the smn_response_code of this SmnResponse.

        调用smn服务返回的http状态码。

        :param smn_response_code: The smn_response_code of this SmnResponse.
        :type smn_response_code: str
        """
        self._smn_response_code = smn_response_code

    @property
    def smn_topic(self):
        r"""Gets the smn_topic of this SmnResponse.

        smn的主题。

        :return: The smn_topic of this SmnResponse.
        :rtype: str
        """
        return self._smn_topic

    @smn_topic.setter
    def smn_topic(self, smn_topic):
        r"""Sets the smn_topic of this SmnResponse.

        smn的主题。

        :param smn_topic: The smn_topic of this SmnResponse.
        :type smn_topic: str
        """
        self._smn_topic = smn_topic

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
        if not isinstance(other, SmnResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
