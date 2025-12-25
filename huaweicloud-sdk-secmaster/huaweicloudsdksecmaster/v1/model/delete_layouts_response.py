# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteLayoutsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, code=None, message=None, x_request_id=None):
        r"""DeleteLayoutsResponse

        The model defined in huaweicloud sdk

        :param code: 响应码
        :type code: str
        :param message: 响应消息
        :type message: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._code = None
        self._message = None
        self._x_request_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def code(self):
        r"""Gets the code of this DeleteLayoutsResponse.

        响应码

        :return: The code of this DeleteLayoutsResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this DeleteLayoutsResponse.

        响应码

        :param code: The code of this DeleteLayoutsResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this DeleteLayoutsResponse.

        响应消息

        :return: The message of this DeleteLayoutsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this DeleteLayoutsResponse.

        响应消息

        :param message: The message of this DeleteLayoutsResponse.
        :type message: str
        """
        self._message = message

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this DeleteLayoutsResponse.

        :return: The x_request_id of this DeleteLayoutsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this DeleteLayoutsResponse.

        :param x_request_id: The x_request_id of this DeleteLayoutsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("DeleteLayoutsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteLayoutsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
