# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncGetChatResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text': 'str',
        'request_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'text': 'text',
        'request_id': 'request_id',
        'status': 'status'
    }

    def __init__(self, text=None, request_id=None, status=None):
        """SyncGetChatResultResponse

        The model defined in huaweicloud sdk

        :param text: text
        :type text: str
        :param request_id: request id
        :type request_id: str
        :param status: status
        :type status: str
        """
        
        super(SyncGetChatResultResponse, self).__init__()

        self._text = None
        self._request_id = None
        self._status = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if request_id is not None:
            self.request_id = request_id
        if status is not None:
            self.status = status

    @property
    def text(self):
        """Gets the text of this SyncGetChatResultResponse.

        text

        :return: The text of this SyncGetChatResultResponse.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SyncGetChatResultResponse.

        text

        :param text: The text of this SyncGetChatResultResponse.
        :type text: str
        """
        self._text = text

    @property
    def request_id(self):
        """Gets the request_id of this SyncGetChatResultResponse.

        request id

        :return: The request_id of this SyncGetChatResultResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this SyncGetChatResultResponse.

        request id

        :param request_id: The request_id of this SyncGetChatResultResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def status(self):
        """Gets the status of this SyncGetChatResultResponse.

        status

        :return: The status of this SyncGetChatResultResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SyncGetChatResultResponse.

        status

        :param status: The status of this SyncGetChatResultResponse.
        :type status: str
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
        if not isinstance(other, SyncGetChatResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
