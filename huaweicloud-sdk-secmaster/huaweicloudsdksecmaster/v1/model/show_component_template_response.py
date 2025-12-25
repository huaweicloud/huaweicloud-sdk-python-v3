# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowComponentTemplateResponse(SdkResponse):

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
        'success': 'bool',
        'request_id': 'str',
        'data': 'TemplateInfo'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'success': 'success',
        'request_id': 'request_id',
        'data': 'data'
    }

    def __init__(self, code=None, message=None, success=None, request_id=None, data=None):
        r"""ShowComponentTemplateResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param message: 错误信息
        :type message: str
        :param success: 请求状态
        :type success: bool
        :param request_id: 请求id
        :type request_id: str
        :param data: 
        :type data: :class:`huaweicloudsdksecmaster.v1.TemplateInfo`
        """
        
        super().__init__()

        self._code = None
        self._message = None
        self._success = None
        self._request_id = None
        self._data = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if success is not None:
            self.success = success
        if request_id is not None:
            self.request_id = request_id
        if data is not None:
            self.data = data

    @property
    def code(self):
        r"""Gets the code of this ShowComponentTemplateResponse.

        错误码

        :return: The code of this ShowComponentTemplateResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowComponentTemplateResponse.

        错误码

        :param code: The code of this ShowComponentTemplateResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ShowComponentTemplateResponse.

        错误信息

        :return: The message of this ShowComponentTemplateResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowComponentTemplateResponse.

        错误信息

        :param message: The message of this ShowComponentTemplateResponse.
        :type message: str
        """
        self._message = message

    @property
    def success(self):
        r"""Gets the success of this ShowComponentTemplateResponse.

        请求状态

        :return: The success of this ShowComponentTemplateResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ShowComponentTemplateResponse.

        请求状态

        :param success: The success of this ShowComponentTemplateResponse.
        :type success: bool
        """
        self._success = success

    @property
    def request_id(self):
        r"""Gets the request_id of this ShowComponentTemplateResponse.

        请求id

        :return: The request_id of this ShowComponentTemplateResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ShowComponentTemplateResponse.

        请求id

        :param request_id: The request_id of this ShowComponentTemplateResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def data(self):
        r"""Gets the data of this ShowComponentTemplateResponse.

        :return: The data of this ShowComponentTemplateResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.TemplateInfo`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ShowComponentTemplateResponse.

        :param data: The data of this ShowComponentTemplateResponse.
        :type data: :class:`huaweicloudsdksecmaster.v1.TemplateInfo`
        """
        self._data = data

    def to_dict(self):
        import warnings
        warnings.warn("ShowComponentTemplateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowComponentTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
