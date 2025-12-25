# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulnerabilitiesResponse(SdkResponse):

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
        'success': 'bool',
        'data': 'list[VulnerabilityDetail]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'total': 'total',
        'size': 'size',
        'page': 'page',
        'success': 'success',
        'data': 'data'
    }

    def __init__(self, code=None, message=None, total=None, size=None, page=None, success=None, data=None):
        r"""ListVulnerabilitiesResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param message: 错误信息
        :type message: str
        :param total: 漏洞总数
        :type total: int
        :param size: 分页大小
        :type size: int
        :param page: 偏移量
        :type page: int
        :param success: 是否成功
        :type success: bool
        :param data: 漏洞列表
        :type data: list[:class:`huaweicloudsdksecmaster.v1.VulnerabilityDetail`]
        """
        
        super().__init__()

        self._code = None
        self._message = None
        self._total = None
        self._size = None
        self._page = None
        self._success = None
        self._data = None
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
        if success is not None:
            self.success = success
        if data is not None:
            self.data = data

    @property
    def code(self):
        r"""Gets the code of this ListVulnerabilitiesResponse.

        错误码

        :return: The code of this ListVulnerabilitiesResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListVulnerabilitiesResponse.

        错误码

        :param code: The code of this ListVulnerabilitiesResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ListVulnerabilitiesResponse.

        错误信息

        :return: The message of this ListVulnerabilitiesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListVulnerabilitiesResponse.

        错误信息

        :param message: The message of this ListVulnerabilitiesResponse.
        :type message: str
        """
        self._message = message

    @property
    def total(self):
        r"""Gets the total of this ListVulnerabilitiesResponse.

        漏洞总数

        :return: The total of this ListVulnerabilitiesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListVulnerabilitiesResponse.

        漏洞总数

        :param total: The total of this ListVulnerabilitiesResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        r"""Gets the size of this ListVulnerabilitiesResponse.

        分页大小

        :return: The size of this ListVulnerabilitiesResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListVulnerabilitiesResponse.

        分页大小

        :param size: The size of this ListVulnerabilitiesResponse.
        :type size: int
        """
        self._size = size

    @property
    def page(self):
        r"""Gets the page of this ListVulnerabilitiesResponse.

        偏移量

        :return: The page of this ListVulnerabilitiesResponse.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListVulnerabilitiesResponse.

        偏移量

        :param page: The page of this ListVulnerabilitiesResponse.
        :type page: int
        """
        self._page = page

    @property
    def success(self):
        r"""Gets the success of this ListVulnerabilitiesResponse.

        是否成功

        :return: The success of this ListVulnerabilitiesResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ListVulnerabilitiesResponse.

        是否成功

        :param success: The success of this ListVulnerabilitiesResponse.
        :type success: bool
        """
        self._success = success

    @property
    def data(self):
        r"""Gets the data of this ListVulnerabilitiesResponse.

        漏洞列表

        :return: The data of this ListVulnerabilitiesResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.VulnerabilityDetail`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListVulnerabilitiesResponse.

        漏洞列表

        :param data: The data of this ListVulnerabilitiesResponse.
        :type data: list[:class:`huaweicloudsdksecmaster.v1.VulnerabilityDetail`]
        """
        self._data = data

    def to_dict(self):
        import warnings
        warnings.warn("ListVulnerabilitiesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListVulnerabilitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
