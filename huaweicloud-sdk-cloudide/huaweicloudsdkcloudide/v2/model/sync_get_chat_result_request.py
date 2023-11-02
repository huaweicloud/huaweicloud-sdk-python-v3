# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncGetChatResultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'body': 'ChatResultRequestMessage'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'body': 'body'
    }

    def __init__(self, content_type=None, body=None):
        """SyncGetChatResultRequest

        The model defined in huaweicloud sdk

        :param content_type: content enumeration - application/json
        :type content_type: str
        :param body: Body of the SyncGetChatResultRequest
        :type body: :class:`huaweicloudsdkcloudide.v2.ChatResultRequestMessage`
        """
        
        

        self._content_type = None
        self._body = None
        self.discriminator = None

        if content_type is not None:
            self.content_type = content_type
        if body is not None:
            self.body = body

    @property
    def content_type(self):
        """Gets the content_type of this SyncGetChatResultRequest.

        content enumeration - application/json

        :return: The content_type of this SyncGetChatResultRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this SyncGetChatResultRequest.

        content enumeration - application/json

        :param content_type: The content_type of this SyncGetChatResultRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def body(self):
        """Gets the body of this SyncGetChatResultRequest.

        :return: The body of this SyncGetChatResultRequest.
        :rtype: :class:`huaweicloudsdkcloudide.v2.ChatResultRequestMessage`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SyncGetChatResultRequest.

        :param body: The body of this SyncGetChatResultRequest.
        :type body: :class:`huaweicloudsdkcloudide.v2.ChatResultRequestMessage`
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
        if not isinstance(other, SyncGetChatResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
