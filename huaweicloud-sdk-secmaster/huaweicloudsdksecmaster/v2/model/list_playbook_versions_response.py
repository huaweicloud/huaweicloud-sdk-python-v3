# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlaybookVersionsResponse(SdkResponse):

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
        'size': 'int',
        'page': 'int',
        'total': 'int',
        'data': 'list[PlaybookVersionListEntity]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'size': 'size',
        'page': 'page',
        'total': 'total',
        'data': 'data',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, code=None, message=None, size=None, page=None, total=None, data=None, x_request_id=None):
        r"""ListPlaybookVersionsResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param message: 错误信息
        :type message: str
        :param size: 分页查询数据大小
        :type size: int
        :param page: 当前页码
        :type page: int
        :param total: 总数
        :type total: int
        :param data: 剧本版本列表信息
        :type data: list[:class:`huaweicloudsdksecmaster.v2.PlaybookVersionListEntity`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListPlaybookVersionsResponse, self).__init__()

        self._code = None
        self._message = None
        self._size = None
        self._page = None
        self._total = None
        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if size is not None:
            self.size = size
        if page is not None:
            self.page = page
        if total is not None:
            self.total = total
        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def code(self):
        r"""Gets the code of this ListPlaybookVersionsResponse.

        错误码

        :return: The code of this ListPlaybookVersionsResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListPlaybookVersionsResponse.

        错误码

        :param code: The code of this ListPlaybookVersionsResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ListPlaybookVersionsResponse.

        错误信息

        :return: The message of this ListPlaybookVersionsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListPlaybookVersionsResponse.

        错误信息

        :param message: The message of this ListPlaybookVersionsResponse.
        :type message: str
        """
        self._message = message

    @property
    def size(self):
        r"""Gets the size of this ListPlaybookVersionsResponse.

        分页查询数据大小

        :return: The size of this ListPlaybookVersionsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListPlaybookVersionsResponse.

        分页查询数据大小

        :param size: The size of this ListPlaybookVersionsResponse.
        :type size: int
        """
        self._size = size

    @property
    def page(self):
        r"""Gets the page of this ListPlaybookVersionsResponse.

        当前页码

        :return: The page of this ListPlaybookVersionsResponse.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListPlaybookVersionsResponse.

        当前页码

        :param page: The page of this ListPlaybookVersionsResponse.
        :type page: int
        """
        self._page = page

    @property
    def total(self):
        r"""Gets the total of this ListPlaybookVersionsResponse.

        总数

        :return: The total of this ListPlaybookVersionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListPlaybookVersionsResponse.

        总数

        :param total: The total of this ListPlaybookVersionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def data(self):
        r"""Gets the data of this ListPlaybookVersionsResponse.

        剧本版本列表信息

        :return: The data of this ListPlaybookVersionsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.PlaybookVersionListEntity`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListPlaybookVersionsResponse.

        剧本版本列表信息

        :param data: The data of this ListPlaybookVersionsResponse.
        :type data: list[:class:`huaweicloudsdksecmaster.v2.PlaybookVersionListEntity`]
        """
        self._data = data

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListPlaybookVersionsResponse.

        :return: The x_request_id of this ListPlaybookVersionsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListPlaybookVersionsResponse.

        :param x_request_id: The x_request_id of this ListPlaybookVersionsResponse.
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
        if not isinstance(other, ListPlaybookVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
