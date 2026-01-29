# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksResponse(SdkResponse):

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
        'total': 'float',
        'page': 'float',
        'size': 'float',
        'request_id': 'str',
        'success': 'bool',
        'data': 'list[TaskInfo]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'total': 'total',
        'page': 'page',
        'size': 'size',
        'request_id': 'request_id',
        'success': 'success',
        'data': 'data'
    }

    def __init__(self, code=None, message=None, total=None, page=None, size=None, request_id=None, success=None, data=None):
        r"""ListTasksResponse

        The model defined in huaweicloud sdk

        :param code: **参数解释**: 错误码，当请求成功时值为 \&quot;00000000\&quot; **取值范围**: 不涉及
        :type code: str
        :param message: **参数解释**: 错误信息的描述 **取值范围**: 不涉及
        :type message: str
        :param total: **参数解释**: 待办的总数 **取值范围**: 不涉及
        :type total: float
        :param page: **参数解释**: 待办请求的偏移量 **取值范围**: 1-100
        :type page: float
        :param size: **参数解释**: 待办的分页的大小 **取值范围**: 1-100
        :type size: float
        :param request_id: **参数解释**: 请求的ID **约束限制**: 不涉及
        :type request_id: str
        :param success: **参数解释**: 是否成功 **取值范围**: - true  成功 - false 失败
        :type success: bool
        :param data: list of informations of task
        :type data: list[:class:`huaweicloudsdksecmaster.v1.TaskInfo`]
        """
        
        super().__init__()

        self._code = None
        self._message = None
        self._total = None
        self._page = None
        self._size = None
        self._request_id = None
        self._success = None
        self._data = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if total is not None:
            self.total = total
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if request_id is not None:
            self.request_id = request_id
        if success is not None:
            self.success = success
        if data is not None:
            self.data = data

    @property
    def code(self):
        r"""Gets the code of this ListTasksResponse.

        **参数解释**: 错误码，当请求成功时值为 \"00000000\" **取值范围**: 不涉及

        :return: The code of this ListTasksResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListTasksResponse.

        **参数解释**: 错误码，当请求成功时值为 \"00000000\" **取值范围**: 不涉及

        :param code: The code of this ListTasksResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ListTasksResponse.

        **参数解释**: 错误信息的描述 **取值范围**: 不涉及

        :return: The message of this ListTasksResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListTasksResponse.

        **参数解释**: 错误信息的描述 **取值范围**: 不涉及

        :param message: The message of this ListTasksResponse.
        :type message: str
        """
        self._message = message

    @property
    def total(self):
        r"""Gets the total of this ListTasksResponse.

        **参数解释**: 待办的总数 **取值范围**: 不涉及

        :return: The total of this ListTasksResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListTasksResponse.

        **参数解释**: 待办的总数 **取值范围**: 不涉及

        :param total: The total of this ListTasksResponse.
        :type total: float
        """
        self._total = total

    @property
    def page(self):
        r"""Gets the page of this ListTasksResponse.

        **参数解释**: 待办请求的偏移量 **取值范围**: 1-100

        :return: The page of this ListTasksResponse.
        :rtype: float
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListTasksResponse.

        **参数解释**: 待办请求的偏移量 **取值范围**: 1-100

        :param page: The page of this ListTasksResponse.
        :type page: float
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this ListTasksResponse.

        **参数解释**: 待办的分页的大小 **取值范围**: 1-100

        :return: The size of this ListTasksResponse.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListTasksResponse.

        **参数解释**: 待办的分页的大小 **取值范围**: 1-100

        :param size: The size of this ListTasksResponse.
        :type size: float
        """
        self._size = size

    @property
    def request_id(self):
        r"""Gets the request_id of this ListTasksResponse.

        **参数解释**: 请求的ID **约束限制**: 不涉及

        :return: The request_id of this ListTasksResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListTasksResponse.

        **参数解释**: 请求的ID **约束限制**: 不涉及

        :param request_id: The request_id of this ListTasksResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def success(self):
        r"""Gets the success of this ListTasksResponse.

        **参数解释**: 是否成功 **取值范围**: - true  成功 - false 失败

        :return: The success of this ListTasksResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ListTasksResponse.

        **参数解释**: 是否成功 **取值范围**: - true  成功 - false 失败

        :param success: The success of this ListTasksResponse.
        :type success: bool
        """
        self._success = success

    @property
    def data(self):
        r"""Gets the data of this ListTasksResponse.

        list of informations of task

        :return: The data of this ListTasksResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.TaskInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListTasksResponse.

        list of informations of task

        :param data: The data of this ListTasksResponse.
        :type data: list[:class:`huaweicloudsdksecmaster.v1.TaskInfo`]
        """
        self._data = data

    def to_dict(self):
        import warnings
        warnings.warn("ListTasksResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
