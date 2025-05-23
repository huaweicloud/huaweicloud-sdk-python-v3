# coding: utf-8

import six

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
        'x_request_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'total': 'total',
        'size': 'size',
        'page': 'page',
        'data': 'data',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, code=None, message=None, total=None, size=None, page=None, data=None, x_request_id=None):
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
        :type data: list[:class:`huaweicloudsdksecmaster.v2.ActionInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListPlaybookActionsResponse, self).__init__()

        self._code = None
        self._message = None
        self._total = None
        self._size = None
        self._page = None
        self._data = None
        self._x_request_id = None
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
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.ActionInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListPlaybookActionsResponse.

        剧本动作列表信息

        :param data: The data of this ListPlaybookActionsResponse.
        :type data: list[:class:`huaweicloudsdksecmaster.v2.ActionInfo`]
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
        if not isinstance(other, ListPlaybookActionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
