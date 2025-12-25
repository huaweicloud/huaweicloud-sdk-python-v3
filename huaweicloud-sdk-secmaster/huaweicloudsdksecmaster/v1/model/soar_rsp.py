# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SoarRsp:

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
        'total': 'int',
        'offset': 'int',
        'limit': 'int',
        'size': 'int',
        'page': 'int'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'success': 'success',
        'request_id': 'request_id',
        'total': 'total',
        'offset': 'offset',
        'limit': 'limit',
        'size': 'size',
        'page': 'page'
    }

    def __init__(self, code=None, message=None, success=None, request_id=None, total=None, offset=None, limit=None, size=None, page=None):
        r"""SoarRsp

        The model defined in huaweicloud sdk

        :param code: **参数解释**: 错误码 **取值范围**: 不涉及
        :type code: str
        :param message: **参数解释**: 错误描述 **取值范围**: 不涉及
        :type message: str
        :param success: **参数解释**: 是否成功 **取值范围**: - true  成功 - false 失败
        :type success: bool
        :param request_id: **参数解释**: 请求的ID **约束限制**: 不涉及
        :type request_id: str
        :param total: **参数解释**: 数据总条数 **约束限制**: 不涉及
        :type total: int
        :param offset: **参数解释**: 当前页大小 **约束限制**: 不涉及
        :type offset: int
        :param limit: **参数解释**: 当前页码 **约束限制**: 不涉及
        :type limit: int
        :param size: **参数解释**: 当前页大小 **约束限制**: 不涉及
        :type size: int
        :param page: **参数解释**: 分页的页数 **约束限制**: 不涉及
        :type page: int
        """
        
        

        self._code = None
        self._message = None
        self._success = None
        self._request_id = None
        self._total = None
        self._offset = None
        self._limit = None
        self._size = None
        self._page = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if success is not None:
            self.success = success
        if request_id is not None:
            self.request_id = request_id
        if total is not None:
            self.total = total
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if size is not None:
            self.size = size
        if page is not None:
            self.page = page

    @property
    def code(self):
        r"""Gets the code of this SoarRsp.

        **参数解释**: 错误码 **取值范围**: 不涉及

        :return: The code of this SoarRsp.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this SoarRsp.

        **参数解释**: 错误码 **取值范围**: 不涉及

        :param code: The code of this SoarRsp.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this SoarRsp.

        **参数解释**: 错误描述 **取值范围**: 不涉及

        :return: The message of this SoarRsp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this SoarRsp.

        **参数解释**: 错误描述 **取值范围**: 不涉及

        :param message: The message of this SoarRsp.
        :type message: str
        """
        self._message = message

    @property
    def success(self):
        r"""Gets the success of this SoarRsp.

        **参数解释**: 是否成功 **取值范围**: - true  成功 - false 失败

        :return: The success of this SoarRsp.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this SoarRsp.

        **参数解释**: 是否成功 **取值范围**: - true  成功 - false 失败

        :param success: The success of this SoarRsp.
        :type success: bool
        """
        self._success = success

    @property
    def request_id(self):
        r"""Gets the request_id of this SoarRsp.

        **参数解释**: 请求的ID **约束限制**: 不涉及

        :return: The request_id of this SoarRsp.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this SoarRsp.

        **参数解释**: 请求的ID **约束限制**: 不涉及

        :param request_id: The request_id of this SoarRsp.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def total(self):
        r"""Gets the total of this SoarRsp.

        **参数解释**: 数据总条数 **约束限制**: 不涉及

        :return: The total of this SoarRsp.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SoarRsp.

        **参数解释**: 数据总条数 **约束限制**: 不涉及

        :param total: The total of this SoarRsp.
        :type total: int
        """
        self._total = total

    @property
    def offset(self):
        r"""Gets the offset of this SoarRsp.

        **参数解释**: 当前页大小 **约束限制**: 不涉及

        :return: The offset of this SoarRsp.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SoarRsp.

        **参数解释**: 当前页大小 **约束限制**: 不涉及

        :param offset: The offset of this SoarRsp.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this SoarRsp.

        **参数解释**: 当前页码 **约束限制**: 不涉及

        :return: The limit of this SoarRsp.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SoarRsp.

        **参数解释**: 当前页码 **约束限制**: 不涉及

        :param limit: The limit of this SoarRsp.
        :type limit: int
        """
        self._limit = limit

    @property
    def size(self):
        r"""Gets the size of this SoarRsp.

        **参数解释**: 当前页大小 **约束限制**: 不涉及

        :return: The size of this SoarRsp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this SoarRsp.

        **参数解释**: 当前页大小 **约束限制**: 不涉及

        :param size: The size of this SoarRsp.
        :type size: int
        """
        self._size = size

    @property
    def page(self):
        r"""Gets the page of this SoarRsp.

        **参数解释**: 分页的页数 **约束限制**: 不涉及

        :return: The page of this SoarRsp.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this SoarRsp.

        **参数解释**: 分页的页数 **约束限制**: 不涉及

        :param page: The page of this SoarRsp.
        :type page: int
        """
        self._page = page

    def to_dict(self):
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
        if not isinstance(other, SoarRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
