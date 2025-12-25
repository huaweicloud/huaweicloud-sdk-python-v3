# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlaybookActionsResponse(SdkResponse):

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
        'total': 'int',
        'size': 'int',
        'page': 'int',
        'data': 'list[ActionInfo]',
        'x_request_id': 'str',
        'x_api_deprecation_info': 'str',
        'x_api_deprecation_date': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'total': 'total',
        'size': 'size',
        'page': 'page',
        'data': 'data',
        'x_request_id': 'X-request-id',
        'x_api_deprecation_info': 'X-API-Deprecation-Info',
        'x_api_deprecation_date': 'X-API-Deprecation-Date'
    }

    def __init__(self, code=None, message=None, total=None, size=None, page=None, data=None, x_request_id=None, x_api_deprecation_info=None, x_api_deprecation_date=None):
        r"""ListPlaybookActionsResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param message: 错误信息
        :type message: str
        :param total: 总数
        :type total: int
        :param size: 分页大小
        :type size: int
        :param page: 当前页数
        :type page: int
        :param data: 剧本动作列表信息
        :type data: list[:class:`huaweicloudsdksecmaster.v1.ActionInfo`]
        :param x_request_id: 
        :type x_request_id: str
        :param x_api_deprecation_info: 
        :type x_api_deprecation_info: str
        :param x_api_deprecation_date: 
        :type x_api_deprecation_date: str
        """
        
        super().__init__()

        self._code = None
        self._message = None
        self._total = None
        self._size = None
        self._page = None
        self._data = None
        self._x_request_id = None
        self._x_api_deprecation_info = None
        self._x_api_deprecation_date = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if page is not None:
            self.page = page
        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if x_api_deprecation_info is not None:
            self.x_api_deprecation_info = x_api_deprecation_info
        if x_api_deprecation_date is not None:
            self.x_api_deprecation_date = x_api_deprecation_date

    @property
    def code(self):
        r"""Gets the code of this ListPlaybookActionsResponse.

        错误码

        :return: The code of this ListPlaybookActionsResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListPlaybookActionsResponse.

        错误码

        :param code: The code of this ListPlaybookActionsResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ListPlaybookActionsResponse.

        错误信息

        :return: The message of this ListPlaybookActionsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListPlaybookActionsResponse.

        错误信息

        :param message: The message of this ListPlaybookActionsResponse.
        :type message: str
        """
        self._message = message

    @property
    def total(self):
        r"""Gets the total of this ListPlaybookActionsResponse.

        总数

        :return: The total of this ListPlaybookActionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListPlaybookActionsResponse.

        总数

        :param total: The total of this ListPlaybookActionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        r"""Gets the size of this ListPlaybookActionsResponse.

        分页大小

        :return: The size of this ListPlaybookActionsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListPlaybookActionsResponse.

        分页大小

        :param size: The size of this ListPlaybookActionsResponse.
        :type size: int
        """
        self._size = size

    @property
    def page(self):
        r"""Gets the page of this ListPlaybookActionsResponse.

        当前页数

        :return: The page of this ListPlaybookActionsResponse.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListPlaybookActionsResponse.

        当前页数

        :param page: The page of this ListPlaybookActionsResponse.
        :type page: int
        """
        self._page = page

    @property
    def data(self):
        r"""Gets the data of this ListPlaybookActionsResponse.

        剧本动作列表信息

        :return: The data of this ListPlaybookActionsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ActionInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListPlaybookActionsResponse.

        剧本动作列表信息

        :param data: The data of this ListPlaybookActionsResponse.
        :type data: list[:class:`huaweicloudsdksecmaster.v1.ActionInfo`]
        """
        self._data = data

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListPlaybookActionsResponse.

        :return: The x_request_id of this ListPlaybookActionsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListPlaybookActionsResponse.

        :param x_request_id: The x_request_id of this ListPlaybookActionsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def x_api_deprecation_info(self):
        r"""Gets the x_api_deprecation_info of this ListPlaybookActionsResponse.

        :return: The x_api_deprecation_info of this ListPlaybookActionsResponse.
        :rtype: str
        """
        return self._x_api_deprecation_info

    @x_api_deprecation_info.setter
    def x_api_deprecation_info(self, x_api_deprecation_info):
        r"""Sets the x_api_deprecation_info of this ListPlaybookActionsResponse.

        :param x_api_deprecation_info: The x_api_deprecation_info of this ListPlaybookActionsResponse.
        :type x_api_deprecation_info: str
        """
        self._x_api_deprecation_info = x_api_deprecation_info

    @property
    def x_api_deprecation_date(self):
        r"""Gets the x_api_deprecation_date of this ListPlaybookActionsResponse.

        :return: The x_api_deprecation_date of this ListPlaybookActionsResponse.
        :rtype: str
        """
        return self._x_api_deprecation_date

    @x_api_deprecation_date.setter
    def x_api_deprecation_date(self, x_api_deprecation_date):
        r"""Sets the x_api_deprecation_date of this ListPlaybookActionsResponse.

        :param x_api_deprecation_date: The x_api_deprecation_date of this ListPlaybookActionsResponse.
        :type x_api_deprecation_date: str
        """
        self._x_api_deprecation_date = x_api_deprecation_date

    def to_dict(self):
        import warnings
        warnings.warn("ListPlaybookActionsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListPlaybookActionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
