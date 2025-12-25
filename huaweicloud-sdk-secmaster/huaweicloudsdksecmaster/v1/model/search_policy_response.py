# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchPolicyResponse(SdkResponse):

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
        'data': 'list[object]',
        'message': 'str',
        'page': 'int',
        'request_id': 'str',
        'size': 'int',
        'success': 'bool',
        'total': 'int',
        'content_type': 'str'
    }

    attribute_map = {
        'code': 'code',
        'data': 'data',
        'message': 'message',
        'page': 'page',
        'request_id': 'request_id',
        'size': 'size',
        'success': 'success',
        'total': 'total',
        'content_type': 'content-type'
    }

    def __init__(self, code=None, data=None, message=None, page=None, request_id=None, size=None, success=None, total=None, content_type=None):
        r"""SearchPolicyResponse

        The model defined in huaweicloud sdk

        :param code: 返回编码
        :type code: str
        :param data: 返回数据
        :type data: list[object]
        :param message: 返回消息
        :type message: str
        :param page: 页码
        :type page: int
        :param request_id: 请求ID
        :type request_id: str
        :param size: 单页数量
        :type size: int
        :param success: 成功状态
        :type success: bool
        :param total: 总量
        :type total: int
        :param content_type: 
        :type content_type: str
        """
        
        super().__init__()

        self._code = None
        self._data = None
        self._message = None
        self._page = None
        self._request_id = None
        self._size = None
        self._success = None
        self._total = None
        self._content_type = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if data is not None:
            self.data = data
        if message is not None:
            self.message = message
        if page is not None:
            self.page = page
        if request_id is not None:
            self.request_id = request_id
        if size is not None:
            self.size = size
        if success is not None:
            self.success = success
        if total is not None:
            self.total = total
        if content_type is not None:
            self.content_type = content_type

    @property
    def code(self):
        r"""Gets the code of this SearchPolicyResponse.

        返回编码

        :return: The code of this SearchPolicyResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this SearchPolicyResponse.

        返回编码

        :param code: The code of this SearchPolicyResponse.
        :type code: str
        """
        self._code = code

    @property
    def data(self):
        r"""Gets the data of this SearchPolicyResponse.

        返回数据

        :return: The data of this SearchPolicyResponse.
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this SearchPolicyResponse.

        返回数据

        :param data: The data of this SearchPolicyResponse.
        :type data: list[object]
        """
        self._data = data

    @property
    def message(self):
        r"""Gets the message of this SearchPolicyResponse.

        返回消息

        :return: The message of this SearchPolicyResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this SearchPolicyResponse.

        返回消息

        :param message: The message of this SearchPolicyResponse.
        :type message: str
        """
        self._message = message

    @property
    def page(self):
        r"""Gets the page of this SearchPolicyResponse.

        页码

        :return: The page of this SearchPolicyResponse.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this SearchPolicyResponse.

        页码

        :param page: The page of this SearchPolicyResponse.
        :type page: int
        """
        self._page = page

    @property
    def request_id(self):
        r"""Gets the request_id of this SearchPolicyResponse.

        请求ID

        :return: The request_id of this SearchPolicyResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this SearchPolicyResponse.

        请求ID

        :param request_id: The request_id of this SearchPolicyResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def size(self):
        r"""Gets the size of this SearchPolicyResponse.

        单页数量

        :return: The size of this SearchPolicyResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this SearchPolicyResponse.

        单页数量

        :param size: The size of this SearchPolicyResponse.
        :type size: int
        """
        self._size = size

    @property
    def success(self):
        r"""Gets the success of this SearchPolicyResponse.

        成功状态

        :return: The success of this SearchPolicyResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this SearchPolicyResponse.

        成功状态

        :param success: The success of this SearchPolicyResponse.
        :type success: bool
        """
        self._success = success

    @property
    def total(self):
        r"""Gets the total of this SearchPolicyResponse.

        总量

        :return: The total of this SearchPolicyResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SearchPolicyResponse.

        总量

        :param total: The total of this SearchPolicyResponse.
        :type total: int
        """
        self._total = total

    @property
    def content_type(self):
        r"""Gets the content_type of this SearchPolicyResponse.

        :return: The content_type of this SearchPolicyResponse.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this SearchPolicyResponse.

        :param content_type: The content_type of this SearchPolicyResponse.
        :type content_type: str
        """
        self._content_type = content_type

    def to_dict(self):
        import warnings
        warnings.warn("SearchPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SearchPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
