# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishAppMessageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'message_id': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'message_id': 'message_id',
        'request_id': 'request_id'
    }

    def __init__(self, message_id=None, request_id=None):
        """PublishAppMessageResponse

        The model defined in huaweicloud sdk

        :param message_id: 唯一的消息ID。
        :type message_id: str
        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        """
        
        super(PublishAppMessageResponse, self).__init__()

        self._message_id = None
        self._request_id = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if request_id is not None:
            self.request_id = request_id

    @property
    def message_id(self):
        """Gets the message_id of this PublishAppMessageResponse.

        唯一的消息ID。

        :return: The message_id of this PublishAppMessageResponse.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this PublishAppMessageResponse.

        唯一的消息ID。

        :param message_id: The message_id of this PublishAppMessageResponse.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def request_id(self):
        """Gets the request_id of this PublishAppMessageResponse.

        请求的唯一标识ID。

        :return: The request_id of this PublishAppMessageResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PublishAppMessageResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this PublishAppMessageResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, PublishAppMessageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
