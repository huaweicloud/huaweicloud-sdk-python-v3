# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateDataobjectRelationsResponse(SdkResponse):

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
        'request_id': 'str',
        'total': 'int',
        'limit': 'int',
        'offset': 'int',
        'success': 'bool',
        'data': 'BatchOperateDataobjectResult'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'request_id': 'request_id',
        'total': 'total',
        'limit': 'limit',
        'offset': 'offset',
        'success': 'success',
        'data': 'data'
    }

    def __init__(self, code=None, message=None, request_id=None, total=None, limit=None, offset=None, success=None, data=None):
        r"""BatchCreateDataobjectRelationsResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param message: 错误信息
        :type message: str
        :param request_id: 请求ID
        :type request_id: str
        :param total: 总数
        :type total: int
        :param limit: 分页大小
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        :param success: 是否成功
        :type success: bool
        :param data: 
        :type data: :class:`huaweicloudsdksecmaster.v1.BatchOperateDataobjectResult`
        """
        
        super().__init__()

        self._code = None
        self._message = None
        self._request_id = None
        self._total = None
        self._limit = None
        self._offset = None
        self._success = None
        self._data = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if request_id is not None:
            self.request_id = request_id
        if total is not None:
            self.total = total
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if success is not None:
            self.success = success
        if data is not None:
            self.data = data

    @property
    def code(self):
        r"""Gets the code of this BatchCreateDataobjectRelationsResponse.

        错误码

        :return: The code of this BatchCreateDataobjectRelationsResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this BatchCreateDataobjectRelationsResponse.

        错误码

        :param code: The code of this BatchCreateDataobjectRelationsResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this BatchCreateDataobjectRelationsResponse.

        错误信息

        :return: The message of this BatchCreateDataobjectRelationsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this BatchCreateDataobjectRelationsResponse.

        错误信息

        :param message: The message of this BatchCreateDataobjectRelationsResponse.
        :type message: str
        """
        self._message = message

    @property
    def request_id(self):
        r"""Gets the request_id of this BatchCreateDataobjectRelationsResponse.

        请求ID

        :return: The request_id of this BatchCreateDataobjectRelationsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this BatchCreateDataobjectRelationsResponse.

        请求ID

        :param request_id: The request_id of this BatchCreateDataobjectRelationsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def total(self):
        r"""Gets the total of this BatchCreateDataobjectRelationsResponse.

        总数

        :return: The total of this BatchCreateDataobjectRelationsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this BatchCreateDataobjectRelationsResponse.

        总数

        :param total: The total of this BatchCreateDataobjectRelationsResponse.
        :type total: int
        """
        self._total = total

    @property
    def limit(self):
        r"""Gets the limit of this BatchCreateDataobjectRelationsResponse.

        分页大小

        :return: The limit of this BatchCreateDataobjectRelationsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BatchCreateDataobjectRelationsResponse.

        分页大小

        :param limit: The limit of this BatchCreateDataobjectRelationsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this BatchCreateDataobjectRelationsResponse.

        偏移量

        :return: The offset of this BatchCreateDataobjectRelationsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BatchCreateDataobjectRelationsResponse.

        偏移量

        :param offset: The offset of this BatchCreateDataobjectRelationsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def success(self):
        r"""Gets the success of this BatchCreateDataobjectRelationsResponse.

        是否成功

        :return: The success of this BatchCreateDataobjectRelationsResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this BatchCreateDataobjectRelationsResponse.

        是否成功

        :param success: The success of this BatchCreateDataobjectRelationsResponse.
        :type success: bool
        """
        self._success = success

    @property
    def data(self):
        r"""Gets the data of this BatchCreateDataobjectRelationsResponse.

        :return: The data of this BatchCreateDataobjectRelationsResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.BatchOperateDataobjectResult`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this BatchCreateDataobjectRelationsResponse.

        :param data: The data of this BatchCreateDataobjectRelationsResponse.
        :type data: :class:`huaweicloudsdksecmaster.v1.BatchOperateDataobjectResult`
        """
        self._data = data

    def to_dict(self):
        import warnings
        warnings.warn("BatchCreateDataobjectRelationsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchCreateDataobjectRelationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
