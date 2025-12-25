# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModulesResponse(SdkResponse):

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
        'data': 'list[ModuleDetailInfo]',
        'message': 'str',
        'offset': 'int',
        'request_id': 'str',
        'limit': 'int',
        'success': 'bool',
        'total': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'data': 'data',
        'message': 'message',
        'offset': 'offset',
        'request_id': 'request_id',
        'limit': 'limit',
        'success': 'success',
        'total': 'total',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, code=None, data=None, message=None, offset=None, request_id=None, limit=None, success=None, total=None, x_request_id=None):
        r"""ListModulesResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param data: 数据列表
        :type data: list[:class:`huaweicloudsdksecmaster.v1.ModuleDetailInfo`]
        :param message: 错误信息
        :type message: str
        :param offset: 页码
        :type offset: int
        :param request_id: 请求ID
        :type request_id: str
        :param limit: 数量
        :type limit: int
        :param success: 是否响应成功
        :type success: bool
        :param total: 总数
        :type total: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._code = None
        self._data = None
        self._message = None
        self._offset = None
        self._request_id = None
        self._limit = None
        self._success = None
        self._total = None
        self._x_request_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if data is not None:
            self.data = data
        if message is not None:
            self.message = message
        if offset is not None:
            self.offset = offset
        if request_id is not None:
            self.request_id = request_id
        if limit is not None:
            self.limit = limit
        if success is not None:
            self.success = success
        if total is not None:
            self.total = total
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def code(self):
        r"""Gets the code of this ListModulesResponse.

        错误码

        :return: The code of this ListModulesResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListModulesResponse.

        错误码

        :param code: The code of this ListModulesResponse.
        :type code: str
        """
        self._code = code

    @property
    def data(self):
        r"""Gets the data of this ListModulesResponse.

        数据列表

        :return: The data of this ListModulesResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ModuleDetailInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListModulesResponse.

        数据列表

        :param data: The data of this ListModulesResponse.
        :type data: list[:class:`huaweicloudsdksecmaster.v1.ModuleDetailInfo`]
        """
        self._data = data

    @property
    def message(self):
        r"""Gets the message of this ListModulesResponse.

        错误信息

        :return: The message of this ListModulesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListModulesResponse.

        错误信息

        :param message: The message of this ListModulesResponse.
        :type message: str
        """
        self._message = message

    @property
    def offset(self):
        r"""Gets the offset of this ListModulesResponse.

        页码

        :return: The offset of this ListModulesResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListModulesResponse.

        页码

        :param offset: The offset of this ListModulesResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def request_id(self):
        r"""Gets the request_id of this ListModulesResponse.

        请求ID

        :return: The request_id of this ListModulesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListModulesResponse.

        请求ID

        :param request_id: The request_id of this ListModulesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def limit(self):
        r"""Gets the limit of this ListModulesResponse.

        数量

        :return: The limit of this ListModulesResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListModulesResponse.

        数量

        :param limit: The limit of this ListModulesResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def success(self):
        r"""Gets the success of this ListModulesResponse.

        是否响应成功

        :return: The success of this ListModulesResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ListModulesResponse.

        是否响应成功

        :param success: The success of this ListModulesResponse.
        :type success: bool
        """
        self._success = success

    @property
    def total(self):
        r"""Gets the total of this ListModulesResponse.

        总数

        :return: The total of this ListModulesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListModulesResponse.

        总数

        :param total: The total of this ListModulesResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListModulesResponse.

        :return: The x_request_id of this ListModulesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListModulesResponse.

        :param x_request_id: The x_request_id of this ListModulesResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListModulesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListModulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
