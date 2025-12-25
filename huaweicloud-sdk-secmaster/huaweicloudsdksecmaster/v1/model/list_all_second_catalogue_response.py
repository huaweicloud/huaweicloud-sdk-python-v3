# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllSecondCatalogueResponse(SdkResponse):

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
        'data': 'list[CatalogueDetailInfo]',
        'message': 'str',
        'request_id': 'str',
        'success': 'bool',
        'total': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'data': 'data',
        'message': 'message',
        'request_id': 'request_id',
        'success': 'success',
        'total': 'total',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, total=None, x_request_id=None):
        r"""ListAllSecondCatalogueResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param data: 数据列表
        :type data: list[:class:`huaweicloudsdksecmaster.v1.CatalogueDetailInfo`]
        :param message: 响应信息
        :type message: str
        :param request_id: 请求ID
        :type request_id: str
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
        self._request_id = None
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
        if request_id is not None:
            self.request_id = request_id
        if success is not None:
            self.success = success
        if total is not None:
            self.total = total
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def code(self):
        r"""Gets the code of this ListAllSecondCatalogueResponse.

        错误码

        :return: The code of this ListAllSecondCatalogueResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListAllSecondCatalogueResponse.

        错误码

        :param code: The code of this ListAllSecondCatalogueResponse.
        :type code: str
        """
        self._code = code

    @property
    def data(self):
        r"""Gets the data of this ListAllSecondCatalogueResponse.

        数据列表

        :return: The data of this ListAllSecondCatalogueResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.CatalogueDetailInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListAllSecondCatalogueResponse.

        数据列表

        :param data: The data of this ListAllSecondCatalogueResponse.
        :type data: list[:class:`huaweicloudsdksecmaster.v1.CatalogueDetailInfo`]
        """
        self._data = data

    @property
    def message(self):
        r"""Gets the message of this ListAllSecondCatalogueResponse.

        响应信息

        :return: The message of this ListAllSecondCatalogueResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListAllSecondCatalogueResponse.

        响应信息

        :param message: The message of this ListAllSecondCatalogueResponse.
        :type message: str
        """
        self._message = message

    @property
    def request_id(self):
        r"""Gets the request_id of this ListAllSecondCatalogueResponse.

        请求ID

        :return: The request_id of this ListAllSecondCatalogueResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListAllSecondCatalogueResponse.

        请求ID

        :param request_id: The request_id of this ListAllSecondCatalogueResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def success(self):
        r"""Gets the success of this ListAllSecondCatalogueResponse.

        是否响应成功

        :return: The success of this ListAllSecondCatalogueResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ListAllSecondCatalogueResponse.

        是否响应成功

        :param success: The success of this ListAllSecondCatalogueResponse.
        :type success: bool
        """
        self._success = success

    @property
    def total(self):
        r"""Gets the total of this ListAllSecondCatalogueResponse.

        总数

        :return: The total of this ListAllSecondCatalogueResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAllSecondCatalogueResponse.

        总数

        :param total: The total of this ListAllSecondCatalogueResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListAllSecondCatalogueResponse.

        :return: The x_request_id of this ListAllSecondCatalogueResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListAllSecondCatalogueResponse.

        :param x_request_id: The x_request_id of this ListAllSecondCatalogueResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListAllSecondCatalogueResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAllSecondCatalogueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
