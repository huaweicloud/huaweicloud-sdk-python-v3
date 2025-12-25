# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLayoutResponse(SdkResponse):

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
        'request_id': 'str',
        'success': 'bool',
        'data': 'LayoutDetailInfo',
        'x_request_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'request_id': 'request_id',
        'success': 'success',
        'data': 'data',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, code=None, message=None, request_id=None, success=None, data=None, x_request_id=None):
        r"""CreateLayoutResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param message: 错误信息
        :type message: str
        :param request_id: 请求ID
        :type request_id: str
        :param success: 请求结果
        :type success: bool
        :param data: 
        :type data: :class:`huaweicloudsdksecmaster.v1.LayoutDetailInfo`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._code = None
        self._message = None
        self._request_id = None
        self._success = None
        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if request_id is not None:
            self.request_id = request_id
        if success is not None:
            self.success = success
        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def code(self):
        r"""Gets the code of this CreateLayoutResponse.

        错误码

        :return: The code of this CreateLayoutResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CreateLayoutResponse.

        错误码

        :param code: The code of this CreateLayoutResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this CreateLayoutResponse.

        错误信息

        :return: The message of this CreateLayoutResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateLayoutResponse.

        错误信息

        :param message: The message of this CreateLayoutResponse.
        :type message: str
        """
        self._message = message

    @property
    def request_id(self):
        r"""Gets the request_id of this CreateLayoutResponse.

        请求ID

        :return: The request_id of this CreateLayoutResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this CreateLayoutResponse.

        请求ID

        :param request_id: The request_id of this CreateLayoutResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def success(self):
        r"""Gets the success of this CreateLayoutResponse.

        请求结果

        :return: The success of this CreateLayoutResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this CreateLayoutResponse.

        请求结果

        :param success: The success of this CreateLayoutResponse.
        :type success: bool
        """
        self._success = success

    @property
    def data(self):
        r"""Gets the data of this CreateLayoutResponse.

        :return: The data of this CreateLayoutResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.LayoutDetailInfo`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this CreateLayoutResponse.

        :param data: The data of this CreateLayoutResponse.
        :type data: :class:`huaweicloudsdksecmaster.v1.LayoutDetailInfo`
        """
        self._data = data

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateLayoutResponse.

        :return: The x_request_id of this CreateLayoutResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateLayoutResponse.

        :param x_request_id: The x_request_id of this CreateLayoutResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateLayoutResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateLayoutResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
