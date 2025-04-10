# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartChatResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'chat_id': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'status': 'status',
        'chat_id': 'chat_id',
        'error_message': 'error_message'
    }

    def __init__(self, status=None, chat_id=None, error_message=None):
        r"""StartChatResponse

        The model defined in huaweicloud sdk

        :param status: status
        :type status: str
        :param chat_id: chat id
        :type chat_id: str
        :param error_message: error message
        :type error_message: str
        """
        
        super(StartChatResponse, self).__init__()

        self._status = None
        self._chat_id = None
        self._error_message = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if chat_id is not None:
            self.chat_id = chat_id
        if error_message is not None:
            self.error_message = error_message

    @property
    def status(self):
        r"""Gets the status of this StartChatResponse.

        status

        :return: The status of this StartChatResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StartChatResponse.

        status

        :param status: The status of this StartChatResponse.
        :type status: str
        """
        self._status = status

    @property
    def chat_id(self):
        r"""Gets the chat_id of this StartChatResponse.

        chat id

        :return: The chat_id of this StartChatResponse.
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        r"""Sets the chat_id of this StartChatResponse.

        chat id

        :param chat_id: The chat_id of this StartChatResponse.
        :type chat_id: str
        """
        self._chat_id = chat_id

    @property
    def error_message(self):
        r"""Gets the error_message of this StartChatResponse.

        error message

        :return: The error_message of this StartChatResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this StartChatResponse.

        error message

        :param error_message: The error_message of this StartChatResponse.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, StartChatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
